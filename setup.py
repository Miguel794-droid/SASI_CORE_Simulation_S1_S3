from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sasi-core",
    version="0.1.0",
    author="Miguel Abraham Saavedra Vado",
    author_email="miguelsaavedravado440@gmail.com",
    description="SASI: Structural Alignment for Safe Intelligence — constitutional safety for AGI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Miguel794-droid/SASI_CORE_Simulation_S1_S3",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[],
)
