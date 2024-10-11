from setuptools import setup, find_packages

setup(
    name='python_plus_easy',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'googletrans==4.0.0-rc1',
        'jinja2==3.0.3',
        'pickle==0.7.5',
        'py-turtle==0.0.5',
        'pyyaml==6.0',
        'setuptools==58.1.0',
        'wheel==0.37.1'
    ],
    author='Masar',
    author_email='your_email@example.com',
    description='A Python module with various functions',
    long_description=open('README.md').read(),
    long_description_content_type='Python Module what make code easier and smaller',
    url='https://github.com/MasarOfficial/Python-Plus-V-1.8.2---inf',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)