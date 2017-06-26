import PyQt5
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt
from scipy import misc
import multiprocessing


f = misc.face()
print (multiprocessing.cpu_count())
misc.imsave('face.png', f)
from scipy import ndimage
face = misc.imread('face.png')
height, width, channels  = f.shape
print(width)
print(height)
print (channels)
temp=f[200:400, 100:300,:]
plt.imshow(temp)
plt.show()