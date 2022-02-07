from importlib.metadata import entry_points
from setuptools import setup
from setuptools import find_packages

if __name__ == "__main__":
    setup( 
        name  = "qdocpyConsole",
        version = "1.0.0",
        packages = find_packages(),
        entry_points = {
            "console_scripts": [
                "QDConsole = app.console:console",
            ],
        }   
    )