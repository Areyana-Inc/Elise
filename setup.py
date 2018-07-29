from setuptools import setup, find_packages
from os.path import join, dirname
import Elise

setup(
    name='Elise',
    version=Elise.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts':
            ['Elise = Elise.elise:main']
    }
)