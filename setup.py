from setuptools import setup, find_packages

setup(
    name='tempinbox',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'user_agent'
    ],
    url='https://github.com/ishanoshada/tempinbox',  
    license='MIT',
    author='Ishan Oshada',
    author_email='ic31908@gamil.com',
    description='A Python package for generating temporary email addresses using Emailnator.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
