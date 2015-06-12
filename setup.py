#!/usr/bin/env python   
try:                    
    from setuptools import setup, find_packages
except:                 
    from distutils.core import setup, find_packages
                        
setup(                  
    version="0.0.3",
    description="Let you convert any image size.",
    author="sparrow",    
    author_email="sprrow.jang@gmail.com",
    url="https://github.com/SparrowJang/image_converter",
    name='image_converter',
    keywords="image convert resize",
    packages=find_packages(),
    install_requires=["pil"] 
)      
