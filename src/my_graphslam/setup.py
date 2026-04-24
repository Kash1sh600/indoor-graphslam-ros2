from setuptools import setup
import os
from glob import glob

package_name = 'my_graphslam'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        # Include rviz configs
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
        # Include config files
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        # Include world files
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.world')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='you@example.com',
    description='Indoor Localization using GraphSLAM',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [],
    },
)
