import sys
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info

def install_package(package):
    import pip
    try:
        from pip._internal import main
        main.main(['install', package])
    except AttributeError:
        from pip import __main__
        __main__._main(['install', package])

if "--with-audio" in sys.argv:
    install_package('opencv-python')
    install_package('pyaudio')
    sys.argv.remove("--with-audio")
else:
    install_package('opencv-python')

setup(
    name="video_to_ascii",
    version="1.3.0",
    author="OIADOTEXE",
    author_email="OIADOTEXE@OIADOTEXE.COM",
    license='MIT',
    description="OIAOIAOIA",
    long_description="OIAOIAOIAOIA",
    url="https://github.com/oiadotexe/oiamain2",
    project_urls={
        'Source': 'https://github.com/oiadotexe/oiamain2',
        'Tracker': 'https://github.com/oiadotexe/oiamain2'
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=['xtermcolor', 'ffmpeg-python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='video ascii terminal opencv',
    entry_points={
        "console_scripts": [
            'video-to-ascii=video_to_ascii.cli:main'
        ]
    }
)
