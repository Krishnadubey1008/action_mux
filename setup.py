from setuptools import setup

package_name = 'action_mux'

setup(
    name=package_name,
    version='0.1.0',
    packages=[],
    py_modules=[
        'action_server',
        'action_client',
        'generic_subscriber',
        'test_publisher'
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='ROS 2 package for action server and client with topic-based goal handling',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'action_server = action_server:main',
            'action_client = action_client:main',
            'generic_subscriber = generic_subscriber:main',
            'test_publisher = test_publisher:main',
        ],
    },
)
