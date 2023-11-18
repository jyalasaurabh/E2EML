from setuptools import find_packages,setup
from typing import List


HYPEN_E="-e ."
def getRequirements(path:str)->List[str]:
    requirements=[]
    with open(path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
    return requirements

setup(
    name="sjProject",
    version="0.0.2",
    author="Saurabh",
    author_email="jyalasaurabh.work@gmail.com",
    packages=find_packages(),
    install_requires=getRequirements("requirements.txt")
)