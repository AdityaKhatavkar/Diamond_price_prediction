from setuptools import find_packages, setup
from typing import List


Hypen_dot_e = "-e ."
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if Hypen_dot_e in requirements:
            requirements.remove(Hypen_dot_e)
    return requirements

setup(
    name = "Diamond price prediction",
    version = "0.0.1",
    author = "Aditya",
    author_email= "adityakhatavkar2004@gmail.com",
    install_requires = get_requirements('requirements.txt'),
    packages = find_packages()
)