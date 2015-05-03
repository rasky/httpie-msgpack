from setuptools import setup


setup(
    name='httpie-msgpack',
    description='Msgpack plugin for HTTPie.',
    long_description=open('README.rst').read().strip(),
    version='1.0.0',
    author='Giovanni Bajo',
    author_email='rasky@develer.com',
    license='BSD',
    url='https://github.com/rasky/httpie-msgpack',
    download_url='https://github.com/rasky/httpie-msgpack',
    py_modules=['httpie_msgpack'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.converter.v1': [
            'httpie_msgpack = httpie_msgpack:MsgpackPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0',
        'msgpack-python'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Environment :: Plugins',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
