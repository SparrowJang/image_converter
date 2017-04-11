# Image Converter

![original image](/example/head.jpeg)

80 x 80 -> 100 x 80

![resize image](/example/out_head.jpeg)

## Introduction

Let you convert any image size.

See [javascript version](https://github.com/SparrowJang/imageConverter).

## Dependency
 
If you want to run it your device, please make sure you have installed this.
 
* pil

## Installation
 
``` bash
git clone https://github.com/SparrowJang/image_converter
 
cd image_converter
 
sudo python setup.py install
```

# Usage

``` python

from image_converter import converter 
import cStringIO
 
f = open( "original.jpg", "r" )
 
data = cStringIO.StringIO( f.read() )
output = converter.resize_and_optimize( data, 400, 300 )
 
f.close()
 
f = open( "new.jpg", "w" )
f.write( output.getvalue() )
f.close() 
 
```


