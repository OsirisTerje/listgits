import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="listgits", 
    version="0.6.0",
    author="Terje Sandstrom",
    author_email="terje@hermit.no",
    description="Python command line program for listing git repositories under a folder root",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OsirisTerje/listgits",
    packages=['listgits'],
    entry_points={'console_scripts': ['listgits = listgits.listgits:main']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)