from setuptools import find_packages, setup
from typing import List
from pathlib import Path

# Define the editable flag
EDITABLE_MODE = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """Returns a list of requirements from a file."""
    requirements = Path(file_path).read_text().splitlines()
    
    # Remove empty lines and editable mode flag if present
    requirements = [req.strip() for req in requirements if req.strip()]
    
    if EDITABLE_MODE in requirements:
        requirements.remove(EDITABLE_MODE)

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Aditya Singh",
    author_email="reings2004@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)