from setuptools import setup


setup(
    name="GSVDevice",
    version="0.0.1",
    author="Dennis Rump",
    author_email="",
    description="A Python module for communicating with GSV6/8 devices",
    url="",
    packages=['GSVDevice'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux :: Windows :: OSX",
    ],
    python_requires='>=3',
    install_requires=['pyserial']
)
