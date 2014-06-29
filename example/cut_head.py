from image_converter import converter
import cStringIO

f = open( "head.jpeg", "r" )

data = cStringIO.StringIO( f.read() )
output = converter.resize_and_optimize( data, 100, 80 )

f.close()

f = open( "out_head.jpeg", "w" )

f.write( output.getvalue() )

f.close()

