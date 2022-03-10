from setuptools import setup, find_packages

setup(
    name='sp_client',
    description='Client SDK for sp-client',
    url='https://github.com/its-abinash/test-client.git',
    author='Abinash Biswal',
    author_email='abinashbiswal248@gmail.com',
    license='unlicensed',
    packages=find_packages(),
    include_package_data=True,
    zip_false=False,
    install_requires=[
        "grpcio==1.36.1",
        "grpcio-tools==1.25.0",
        "grpcio-opentracing==1.1.4",
        "jaeger-client==4.3.0",
        "protobuf==3.12.2",
        'setuptools'
    ]
)