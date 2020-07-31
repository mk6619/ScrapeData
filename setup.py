import setuptools

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

print(long_description)
 
setuptools.setup(
    #Here is the module name.
    name="ScrapeData",
 
    #version of the module
    version="0.0.4",
 
    #Name of Author
    author="Mayank khursija",
 
    #your Email address
    author_email="mk6619@gmail.com",
 
    #Small Description about module
    description="Python module to get table data from any webpage and converts it into either Json or Csv",
    long_description_content_type="text/markdown",
    long_description=long_description,
 
    #Specifying that we are using markdown file for description
    
 
    #Any link to reach this module, if you have any webpage or github profile
    url="https://github.com/mk6619/",
    packages=setuptools.find_packages(),
    install_requires=['setuptools', 'pandas', 'requests', 'beautifulsoup4'],
 
    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
