from setuptools import setup, find_namespace_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="test_repo1_od",
    version="0.0.1",
    author="Omar Abid",
    author_email="omar.abid4@gmail.com",
    description="A package for math stuff",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/omarabid59/test_repo1/",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src")
)