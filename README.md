# About

Code for evaluating the performance of a Parallel Convolution operation on images.

# The algorithm can be separated into five steps:
- Define N as the number of available cores;
- Slice the input image into (N^2)+2 sub-images;
- Create the parallel instances;
- Convolve each sub-image with the desired kernel;
- Create the output image with the sub-images joining.

The results are available at http://jeanvitor.com/convolution-parallel-algorithm-python/

# How to use
- Download and Install [Anaconda](https://www.continuum.io/downloads)
- To run: `py Conv.py`




