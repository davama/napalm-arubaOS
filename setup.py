"""setup.py file."""
import uuid

from setuptools import setup, find_packages
from pip.req import parse_requirements

__author__ = 'david.johnnes@gmail.com'

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="napalm-arubaOS",
    version="0.0.1",
    packages=find_packages(),
    author="Kirk Byers",
    author_email="david.johnnes@gmail.com,
    description="Network Automation and Programmability Abstraction Layer with Multivendor support",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/napalm-automation/napalm-arubaOS",
    include_package_data=True,
    zip_safe=False,
    install_requires=reqs,
)
