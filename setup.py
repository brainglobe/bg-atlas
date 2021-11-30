from setuptools import setup, find_namespace_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="bg-atlasgen",
    version="0.0.2",
    description="Scripts generation atlases and utilities for BrainGlobe",
    install_requires=requirements,
    python_requires=">=3.8",
    entry_points={"console_scripts": []},
    packages=find_namespace_packages(exclude=("docs", "tests*")),
    include_package_data=True,
    url="https://github.com/brainglobe/bg-atlasgen",
    author="Luigi Petrucco, Federico Claudi, Adam Tyson",
    author_email="code@adamltyson.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    zip_safe=False,
    extras_require = {"SimpleITK":["SimpleITK"],
                     "scikit-image":["scikit-image"],
                     "magic-class":["magic-class"]}
)
