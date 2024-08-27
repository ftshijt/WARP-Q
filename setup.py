from setuptools import setup, find_packages

setup(
    name='warpq',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        "librosa",
        "pyvad",
        "scikit-image",
        "speechpy",
        "soundfile",
        "pandas",
        "zipp",
    ],
    author='Jiatong Shi',
    author_email='ftshijt@gmail.com',
    description='A package for wraping the WARP-Q metric',
    url='https://github.com/ftshijt/WARP-Q.git',
    keywords='speech metrics',
)
