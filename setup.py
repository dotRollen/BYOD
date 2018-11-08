import io
import re
from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

with io.open('byod_checkin/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='byod-checkin',
    version=version,
    url='https://github.com/dotRollen/BYOD-Checkin',
    maintainer='Edward Nunez',
    maintainer_email='edwardnnz@gmail.com',
    description='BYOD checkin application.',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pymongo>=3.5.1',
    ],
    extras_require={
        'dev': [
            'coverage>=4.5.1',
            'flake8>=3.5.0 ',
            'black>=18.6b4',
        ]
    },
)
