
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='localytics',
    url='https://github.com/lexadavid/localytics',
    author='David Lexa',
    author_email='david.kaur.lexa@wunder.org',
    packages = ['localytics'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='1.41',
    license='MIT',
    description='Python API Client for Localytics Raw Data Export'
)
