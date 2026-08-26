from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).resolve().parent
readme = (this_directory / "README.md").read_bytes()

if readme.startswith((b"\xff\xfe", b"\xfe\xff")):
    long_description = readme.decode("utf-16")
else:
    long_description = readme.decode("utf-8-sig")

setup(
    name = "dolonroy-gaussian-distributions", 
    version="0.2.2",
    description="A lightweight Python package for calculating and visualizing **Gaussian (Normal)** and **Binomial** probability distributions. It provides simple, object-oriented classes to compute mean, standard deviation, probability density functions (PDFs), and to combine distributions using the `+` operator.", 
    packages=['distributions'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False
 )
