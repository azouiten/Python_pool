import setuptools

with open("README.md", "r", encoding = "utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name = "my_minipack",
    version = "0.0.1",
    author = "azouiten",
    author_email = "azouiten@student.1337.ma",
    description = "a virtual coffee maker and a loading bar",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    # url = "package URL",
    # project_urls = {
    #     "Bug Tracker": "package issues URL",
    # },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)