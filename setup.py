import os
from setuptools import setup, find_packages

# Determine the correct script extension based on the operating system
script_name = 'create-project'
if os.name == 'nt':  # Windows
    script_name += '.bat'
else:  # Unix-like
    script_name += '.sh'

setup(
    name='create_cpp_project',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[],
    scripts=[f'scripts/{script_name}'],
    entry_points={
        'console_scripts': [
            'create_cpp_project=create_cpp_project.creator:main'
        ]
    },  
    author='Remco Halman',
    author_email='remco.halman@gmail.com',
    description='A utility to create C++ project structures. For now a simple structure but this is expanded on the go.'
)
