#This gif is a reference to the scene in Transformers the Movie (1986) where Hotrod becomes Rodimus Prime
#For those curious, here's the scene on YT: https://youtu.be/Nbz7ThFQq9U?si=Yx5lpOzqrpSwWNOC
#My fiance really likes Transformers lol 

import imageio.v3 as iio

filenames = ['Photo1.png', 'Photo2.png', 'Photo3.png', 'Photo4.png', 'Photo5.png', 'Photo6.png', 'Photo7.png', 'Photo8.png', 'Photo9.png', 'Photo10.png']
images = [ ]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('the_touch.gif', images, duration = 400, loop = 0)

