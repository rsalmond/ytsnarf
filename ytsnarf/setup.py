from setuptools import setup, find_packages

setup(name='ytsnarf',
    version='0.0.1',
    description='Execute youtube-dl remotely',
    long_description='ytsnarf will ssh into a host, execute youtube-dl on your behalf, and download the resulting file.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Video',
    ],
    keywords = 'youtube ssh remote'
    url='http://github.com/rsalmond/ytsnarf',
    author='Rob Salmond',
    author_email='rob@salmond.ca',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'fabric',
    ],
    zip_safe=True)
