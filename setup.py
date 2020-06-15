import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wltr-doc-validate",
    version="1.0.0",
    author="Walter José Avelino da Silva",
    author_email="walter.avelin@gmail.com",
    description="Wltr Doc Validate",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/walteravelino/wltr-doc-validate",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
