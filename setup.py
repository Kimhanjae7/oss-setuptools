import setuptools

setuptools.setup (
    include_package_data = True,
    name=hanjaekim
    version='0.0.1',
    description='oss-dev my calculator 0001',
    author='hanjaekim',
    author_email='hjk2512@naver.com',
    url = "https://github.com/Kimhanjae7/oss-setuptools",
    download_url = "https://github.com/Kimhanjae7/oss-setuptools/archive/refs/tags/v0.0.1.zip",
    install_requires=['pytest'],
    long_description = 'oss-dev calculator python module',
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Os Independent",

    ],
)
