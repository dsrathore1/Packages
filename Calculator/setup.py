import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="calc-ds", # Replace with your own username
    version="0.0.1",
    author="DS Rathore",
    author_email="dsrathorebsw1234@gmail.com",
    description="This is my first test package of calculator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dsrathore1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

