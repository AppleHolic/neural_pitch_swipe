from setuptools import setup, find_packages


def get_requirements(filename='requirements.txt'):
    deps = []
    with open(filename, 'r') as f:
        for pkg in f.readlines():
            if pkg.strip():
                deps.append(pkg)
    return deps


setup(
    name="neural_pitch_swipe",
    version="0.0.0",
    description="simple neural network for predicting 'SWIPE' pitch values",
    author="ILJI CHOI",
    author_email="choiilji@gmail.com",
    install_requires=get_requirements(),
    packages=find_packages(),
    include_package_data=True
)