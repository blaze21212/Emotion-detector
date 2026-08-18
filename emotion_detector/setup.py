"""
Setup configuration for emotion_detector package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="emotion-detector",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for emotion detection from text using Watson NLP API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/emotion-detector",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.0,<3.0",
        "ibm-watson>=11.0,<12.0",
        "python-dotenv>=0.19.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "flake8>=3.9",
            "black>=21.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "emotion-detect=emotion_detector.cli:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/yourusername/emotion-detector/issues",
        "Source": "https://github.com/yourusername/emotion-detector",
    },
)
