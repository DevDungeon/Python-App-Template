from setuptools import setup
from sys import platform

requirements = [
    'pyqt5',
]

if platform == "win32":
    requirements.append('windows-curses')

setup(
    name='myapp',
    version='0.0.1',
    description='My app',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    url='https://github.com/DevDungeon',
    author='DevDungeon',
    author_email='nanodano@devdungeon.com',
    packages=['myapp'],
    # py_modules=[],
    # scripts=[  # entrypoints preferred
    #     'scripts/mycliscript',
    # ],
    entry_points={
        'console_scripts': [
            'myapp = myapp.__main__:main_cli',
        ],
        'gui_scripts': [
            'mygui = myapp.__main__:main_gui',
        ]
    },
    package_data={
        'myapp': [
            'resources/*',
        ],
    },
    zip_safe=False,
    install_requires=requirements,
    python_requires='<3.6',
    license='GPL-3.0',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)

