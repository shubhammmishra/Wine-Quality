import setuptools

with open("README.md", "r" , encoding="utf-8" ) as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME= "WINE-QUALITY"
AUTHOR_USER_NAME= "shubhammmishra"
SRC_REPO= "mlproject"
AUTHOR_EMAIL= "shubhammishra1442@gmail.com"


# we use the setuptools setup for make the local package so we can use these inside local project
setuptools.setup(
    name= SRC_REPO,
    version= __version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    descriptioin= " small project in machine learning",
    long_description= long_description,
    long_description_content= "text/markdown",
    url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls= {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir= {"":"src"},
    packages= setuptools.find_packages(where="src")

)