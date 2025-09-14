'''
The setup.py file is an0 essential part of the packaging and 
distributing python projects.It is used by setup tools 
to define the configuration of project, such as its metadata, dependencies and more

'''
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    
    return requirement_list

print(get_requirements())

setup(
    name='Network_Security',
    version='0.0.1',
    author='Raksha Akotiya',
    author_email='akotiya.raksha27@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
    
)
                   