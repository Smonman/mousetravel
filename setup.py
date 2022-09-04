from setuptools import setup


def readfile(filename):
    with open(filename, "r+") as f:
        return f.read()


setup(
    name="mousetravel",
    version="1.0.0",
    url="https://github.com/Smonman/mousetravel",
    license=readfile("LICENSE"),
    author="Simon Josef Kreuzpointner",
    author_email="simonkreuzpointner@gmail.com",
    description="An odometer for your mouse",
    long_description=readfile("README.md"),
    install_requires=["mouse~=0.7.1", "screeninfo~=0.8"],
    scripts=["mousetravel.py"],
    entry_points={
        "console_scripts": [
            "mousetravel = mousetravel:main"
        ]
    },
)
