import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_tuieditor",
    version="0.1.0",
    author="Qb",
    author_email="qb@qbit.moe",
    description="Markdown editor and viewer widgets for Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/QbDesu/django-tui.editor",
    project_urls={
        "Bug Tracker": "https://github.com/QbDesu/django-tui.editor/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        "cmarkgfm",
        "django"
    ],
    python_requires=">=3.6",
)