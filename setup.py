import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

setup(
    # This is the name of your project as to be published at PyPI: https://pypi.org/project/sampleproject/
    name="bsci",  # https://packaging.python.org/specifications/core-metadata/#name
    version="1.0",  # https://www.python.org/dev/peps/pep-0440/
    description="Constructing frequentist confidence intervals using the statistical bootstrap",
    long_description=(here / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/famura/bsci",
    author="Fabio Muratore",
    author_email="fabio.muratore@famura.net",
    classifiers=[  # list of valid classifiers, see https://pypi.org/classifiers/
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="statistical bootstrap, the bootstrap, confidence interval",
    packages=find_packages(include=["bsci"], exclude=["tests"]),
    python_requires=">=3.7, <4",
    # List mandatory groups of dependencies, installed via `pip install -e .[dev]`
    install_requires=[  # https://packaging.python.org/en/latest/requirements.html
        "numpy",
    ],
    # List additional groups of dependencies, installed via `pip install -e .[dev]`
    extras_require={
        "dev": ["black", "isort", "matplotlib", "pytest", "pytest-cov"],
    },
    project_urls={
        "Source": "https://github.com/famura/bsci",
        "Bug Reports": "https://github.com/famura/bsci/issues",
        # 'Funding': 'https://donate.pypi.org',
    },
    # Data files outside of the package http://docs.python.org/distutils/setupscript.html#installing-additional-files
    # data_files=[('my_data', ['data/data_file'])],
)
