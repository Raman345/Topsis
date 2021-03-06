import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='topsis_python',  
     version='0.1',
     author="Raman",
     author_email="sandeepooo153@gmail.com",
     description="topsis package in python",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Raman345/Topsis",
     packages=['topsis_pkg'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
