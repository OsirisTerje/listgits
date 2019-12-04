import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="listgits-pkg-osirsiterje", 
    version="0.3.1",
    author="Terje Sandstrom",
    author_email="terje@hermit.no",
    description="Python command line program for listing all git repositories under a folder root",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OsirisTerje/listgits",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)