from setuptools import setup

setup(
    name="deepseek",
    version="0.2.0",
    py_modules=["chat", "main"],
    install_requires=[
        "openai>=1.0.0",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "deepseek=main:main"
        ]
    }
)
