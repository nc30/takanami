from setuptools import setup
from setuptools import find_packages
import takanami

#requires = ['boto3']
requires = []

setup(
    name = "takanami",
    version = takanami.__version__,
    install_requires = requires,
    author = 'Himura Asahi',
    author_email = 'himura@nitolab.com',
    packages = find_packages(),
    entry_points={
        'console_scripts': [
            'kclear = takanami.cli.clear:main',
            'kshock = takanami.cli.shock:main',
            'kstate = takanami.cli.state:main',
        ],
    },
    description = "takanami",
    url = "https://github.com/nc30/takanami"
)
