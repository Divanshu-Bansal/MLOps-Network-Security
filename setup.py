'''
This setup.py file is an essential part of the packaging and distributing
Python projects. It is used by setuptools to define the configuration
of the project, such as its metadata, dependencies, and more
'''

from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:
    '''
    This function returns the list of requirements
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()

            # Process each line
            for line in lines:
                requirement = line.strip()

                # ignore empty lines and -e .
                if requirement and requirement!="-e .":
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_lst

setup(
    name="Network Security",
    version="0.0.1",
    author="Divanshu Bansal",
    author_email="divanshubansal05@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)