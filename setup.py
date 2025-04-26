from setuptools import setup, find_packages

with open("LICENSE", "r", encoding="utf-8") as f:
    license_content = f.read()

setup(
    name="game",
    version="0.0.1",
    description="Just for fun",
    author="Matt Todd",
    author_email="matt.c.todd@gmail.com",
    url="https://github.com/caspian311/game-engine-py",
    license=license_content,
    packages=find_packages(exclude=["tests", "test_*"]),
    entry_points = {
        "console_scripts": [
            "game=game.__main__:app" 
        ]
    }
)
