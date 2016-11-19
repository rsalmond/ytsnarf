import sys
import os
import argparse
from fabric.api import run, env
from fabric.operations import get
from fabric.network import ssh_config
from cStringIO import StringIO

try:
    from configparser import ConfigParser, NoOptionErorr
except ImportError:
    from ConfigParser import ConfigParser, NoOptionError

CONFIG_FILE = os.path.join(os.path.expanduser('~'), '.ytsnarfrc')
VERSION = '0.0.1'
URL = 'https://github.com/rsalmond/ytsnarf'
PROGRAM = 'ytsnarf'

def read_config():
    config = ConfigParser()
    config.read(CONFIG_FILE)
    return config

def write_config(host):
    config = ConfigParser()
    config.add_section(PROGRAM)
    config.set(PROGRAM, 'host', host)
    with open(CONFIG_FILE, 'w') as f:
        config.write(f)

def output(data):
    print('{} v{}\t{}\n'.format(PROGRAM, VERSION, URL))
    print(data)

def die_no_host_error():
    output('\tYou must either specify a host:\n\t$ ytsnarf -h <host> <url> \n\n\tOr configure a default host:\n\t$ ytsnarf -h <host> --save-default\n')
    sys.exit(1)

def validate_host(args):
    """ ensure a host has been specified either on the cmdline or in the config file and return it """
    host = args.host

    if host is None:
        config = read_config()
        if len(config.sections()) > 0:
            try:
                host = config.get(PROGRAM, 'host')
            except NoOptionError:
                die_no_host_error()
        else:
            die_no_host_error()

        if host == '':
            die_no_host_error()
    else:
        if args.save_default:
            write_config(args.host)
            output('\'{}\' has been saved in {} as default host.'.format(args.host, CONFIG_FILE))
            sys.exit(0)

    return host

def download(url):
    tmpdir = run('mktemp -d /tmp/ytsnarf-tmp-XXXXXXXX')
    outdir = os.path.join('/tmp', tmpdir)
    run('touch {}/bunk'.format(outdir))
    run('youtube-dl --output={}/%\(title\)s.%\(ext\)s {}'.format(outdir, url))
    get(os.path.join(outdir, '*'), local_path='.')
    run('rm -rf {}'.format(outdir))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run youtube-dl on a remote host and bring the resulting file back here.", add_help=False)
    parser.add_argument('-h', '--host', action='store', required=False)
    parser.add_argument('-p', '--params', action='store', required=False)
    parser.add_argument('--save-default', action='store_true', required=False)
    parser.add_argument('url', action='store', nargs='?', default=None)

    args = parser.parse_args()
    xargs = args
   
    host = validate_host(args)

    if args.url is None:
        output('No URL Specified, quitting.')
        sys.exit(1)

    env.use_ssh_config = True
    env.host_string = host

    #XXX: does every ssh config actually need a user? (shrug)
    if ssh_config().get('user') is None:
        output('Host {} does not appear to be configured in your ssh config file, it must be configured for {} to work.'.format(host, PROGRAM))
        sys.exit(1)

    download(args.url)
