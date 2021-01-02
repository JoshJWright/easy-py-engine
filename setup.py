from setuptools import find_packages, setup

setup(
    name="easy-py-engine",
    version="0.1.0",
    author="Josh Wright",
    author_email="j.wright3141@outlook.com",
    description="Simple graphics and physics engines.",
    platforms="Posix; MacOS X; Windows",
    packages=find_packages(where="./src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=("PyOpenGL",),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
)