# -*- coding: utf-8 -*-
import Image
import cStringIO
import base64

def resize_and_optimize( img, width, height, image_type = "jpeg" ):

    img.seek( 0 )
    im = Image.open( img )
    size = im.size

    rateW = float( size[0] ) / width
    rateH = float( size[1] ) / height

    if rateW < rateH:
        rate = rateW
    else:
        rate = rateH

    if rate:
        re_width = int( size[0] / rate )
        re_height = int( size[1] / rate )
    else:
        re_width = size[0]
        re_height = size[1]
    #print re_width
    #print re_height
    resize_img = im.resize( ( re_width, re_height ), Image.BILINEAR )

    diff_w = ( re_width - width )
    diff_h = ( re_height - height )

    if diff_w:
        start_x = diff_w / 2
    else:
        start_x = 0

    if diff_h:
        start_y = diff_h / 2
    else:
        start_y = 0

    output = cStringIO.StringIO()
    output_im = resize_img.crop( (start_x, start_y, ( start_x + width ), ( start_y + height )) )
    output.seek( 0 )
    #output_im.convert('RGB').save( "test" , "jpeg" )
    if image_type == "jpeg":
        output_im.convert('RGB').save( output , "jpeg" )
    else:
        output_im.save( output , "png" )
    return output

#f = open( "3423432.jpg", "r" )

#data = cStringIO.StringIO( f.read() )
#resize_and_optimize( data, 400, 300 )

#f.close()

