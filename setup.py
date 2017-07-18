import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="protobuf-schema-test-base",
    version="0.1.0",
    author="Sabela de la Torre",
    author_email="sabela.delatorre@crg.eu",
    description="Base for tests of Protobuf schemas",
    url="https://github.com/sdelatorrep/protobuf-schema-test-base",
    license="Apache 2",
    packages=['tests','ga4gh'],
    namespace_packages=["ga4gh"],
    classifiers=[
        "License :: OSI Approved :: Apache 2 License",
    ]
)

