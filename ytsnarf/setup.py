from setuptools import setup, find_packages

setup(name='ytsnarf',
    version='0.0.1',
    description='Execute youtube-dl remotely',
    long_description='ytsnarf will ssh into a host, execute youtube-dl on your behalf, and download the resulting file.',
    url='http://github.com/rsalmond/ytsnarf',
    author='Rob Salmond',
    author_email='rob@salmond.ca',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'fabric',
    ],
    zip_safe=True)