from setuptools import find_packages, setup
setup(
    name='mipt_lab_lib',
    packages=find_packages(),
    version='0.1.0',
    description='My first Python library',
    author='Me',
    license='MIT',
    install_requires=['numpy', 'pandas'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
