import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="context-search",
    version="0.0.1",
    author="Siddharth Menon",
    author_email="siddharth.menon1@gmail.com",
    description="A search algorithm for efficient searching in PDFs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ItsSiddharth/context-search",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)