from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("requirements-backend.txt") as f:
    required_backend = f.read().splitlines()

with open("requirements-frontend.txt") as f:
    required_frontend = f.read().splitlines()

with open("requirements-dev.txt") as f:
    required_dev = f.read().splitlines()

with open("requirements-docs.txt") as f:
    required_docs = f.read().splitlines()

setup(
    name="aviary",
    version="0.3.1",
    description="A tool to deploy and query LLMs",
    packages=find_packages(include="aviary*"),
    include_package_data=True,
    package_data={"aviary": ["models/*"]},
    entry_points={
        "console_scripts": [
            "aviary=aviary.cli:app",
        ]
    },
    install_requires=required,
    extras_require={
        "backend": required_backend,
        "frontend": required_frontend,
        "dev": required_dev,
        "test": required_dev,
        "docs": required_docs,
    },
    dependency_links=["https://download.pytorch.org/whl/cu118"],
    python_requires=">=3.8",
)
