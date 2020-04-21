from setuptools import setup, find_namespace_packages

# Parse the README.md
with open("README.md", "r") as readme_file:
    readme = readme_file.read()

with open("requirements.txt", "r") as requirements_file:
    requirements = requirements_file.read().splitlines()

setup(
    name="test_repo1_od",
    version="0.0.1",
    author="First Name Last Name",
    author_email="author@email.com",
    description="Enter description here",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    # Do Not Modify these
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    test_suite='project_namespace.object_detection.test'
)
