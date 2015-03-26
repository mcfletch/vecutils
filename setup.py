import os

from setuptools import setup, find_packages
version = [
    (line.split('=')[1]).strip().strip('"').strip("'")
    for line in open(os.path.join('vecutils','version.py'))
    if line.startswith( '__version__' )
][0]

if __name__ == "__main__":
    setup(
        name='vecutils',
        version=version,
        description='Numpy-based vector utilities',
        long_description='vecutils',
        classifiers=[
            "Programming Language :: Python",
        ],
        author='Mike C. Fletcher',
        author_email='mcfletch@vrplumber.com',
        url='https://github.com/mcfletch/vecutils',
        keywords='3D Graphics, Vectors',
        packages=find_packages(),
        include_package_data=True,
        license='MIT',
        # Dev-only requirements:
        # nose
        # pychecker
        # coverage
        # globalsub
        package_data = {
            'vecutils': [
            ],
        },
        install_requires=[
        ],
        scripts = [
        ],
        entry_points = dict(
            console_scripts = [
            ],
        ),
    )

