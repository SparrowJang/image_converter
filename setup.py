#!/usr/bin/env python   
try:                    
    from setuptools import setup, find_packages
except:                 
    from distutils.core import setup, find_packages
                        
setup(                  
    version="0.0.1",
    description="Let you convert any image size.",
    author="sparrow",    
    author_email="sprrow.jang@gmail.com",
    url="http://sparrowhome.twbbs.org/",
    name='image_converter',
    packages=find_packages(),
    install_requires=["pil"] 
)      
