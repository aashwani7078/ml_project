
from setuptools import find_packages, setup

HYPEN_E_DOT = "-e ."


def get_requirement(file_path):
    with open(file_path, "r") as file_obj:
        requirements = [
            line.strip()
            for line in file_obj
            if line.strip() and not line.startswith("#")
        ]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="mlproject",
    version="0.0.2",
    author="Aashwani",
    author_email="aashwanichouhan33@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirement("requirements.txt"),
)