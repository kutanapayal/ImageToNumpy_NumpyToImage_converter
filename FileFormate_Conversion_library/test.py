from image_To_numpy_Converter import image_To_numpy_Converter
from numpy_To_image_Converter import numpy_To_image_Converter
import logging

im_path = input("Enter image path :") 
numpy_arr = image_To_numpy_Converter.image_To_numpyArray(im_path)
print("Numpy Array List OF Image :: \n",numpy_arr)

file_path = numpy_To_image_Converter.numpyArray_TO_image(numpy_arr)
print("Your file saved AT :: \n",file_path)
