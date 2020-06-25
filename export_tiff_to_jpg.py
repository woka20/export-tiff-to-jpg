from osgeo import gdal 


options_list = [
    '-ot Byte',
    '-of JPEG',
    '-b 1', #remove "-b 2" and "-b 3" for grey image
    '-b 2',
    '-b 3',
    '-b mask',
    '-scale',


] 
options_string = " ".join(options_list)

gdal.Translate('medium4.jpg', #file output
               'medium1.tif', #file input in tif
               options=options_string)
