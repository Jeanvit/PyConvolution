import matplotlib
import multiprocessing
matplotlib.use('qt5agg')
from scipy import misc
from scipy import signal as sg
import numpy as np
from joblib import Parallel, delayed
import timeit
#=============================================================================================
#Function for convolving the slices with the kernel
def convolve(slice):
    return sg.convolve2d(slice, ([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]),'same','symm')

#=============================================================================================
#Function for slicing the image into  (CORES^2)+2 subimages
def split(numberOfCores,image,height, width):
    sliceWidthSize = (width / numberOfCores)
    sliceHeightSize = (height / numberOfCores)
    print ('Number of slices (avaliable processors):', numberOfCores)
    print("Image size: ", width, "x", height)
    print("Slices=", sliceWidthSize, sliceHeightSize)
    startX = 0
    endX = sliceWidthSize
    startY = 0
    endY = sliceHeightSize
    imagePieces = []
    w = 0
    for i in range (1,numberOfCores):
        for j in range (0,numberOfCores+2):
            imagePieces.append(image[int(startX):int(endX),int(startY):int(endY)])
            startY = endY
            endY += sliceHeightSize
        startY = 0
        endY = sliceHeightSize
        startX = endX
        endX += sliceWidthSize
    print("Total slices: ",imagePieces.__len__())
    return imagePieces

#=============================================================================================
#Function for building the output
def join (slices,height, width):
    sliceWidthSize = (width / imageSlices)
    sliceHeightSize = (height / imageSlices)
    startX = 0
    endX = sliceWidthSize
    startY = 0
    endY = sliceHeightSize
    pos = 0
    t = np.zeros((height, width))
    for i in range(1, imageSlices):
        for j in range(0, imageSlices + 2):
            t[int(startX):int(endX), int(startY):int(endY)] = slices[pos];
            pos = pos + 1
            startY = endY
            endY += sliceHeightSize
        startY = 0
        endY = sliceHeightSize
        startX = endX
        endX += sliceWidthSize
    return t
#=============================================================================================
#main
if __name__ == '__main__':
    f = misc.imread('5.jpg', False, mode='L')

    height, width = f.shape
    imageSlices=multiprocessing.cpu_count()
    start_time = timeit.default_timer()

    imagePieces=split(imageSlices,f,height, width)
    #sg.convolve2d(f, ([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]), 'valid')
    slices = Parallel(n_jobs=imageSlices)(delayed(convolve)(pieces) for pieces in imagePieces)
    outputImage=join (slices,height, width)
    elapsed = timeit.default_timer() - start_time

    print("Time:",elapsed,"seconds")
   # plt.imshow(outputImage,cmap = plt.get_cmap('gray'),vmin=0, vmax=255)
   # plt.show()
# =============================================================================================
