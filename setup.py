from setuptools import setup

setup(
    name='yp',
    version='0.1',
    description='Evaluate JMESPATH expressions against YAML',
    url='https://github.com/mjfroehlich/yp',
    author='Martin Froehlich',
    author_email='martin.j.froehlich@gmail.com',
    license='MIT',
    py_modules=['yp'],
    install_requires=['pyyaml', 'jmespath'],
    entry_points={'console_scripts': ['yp=yp:main']},
    zip_safe=False
)
