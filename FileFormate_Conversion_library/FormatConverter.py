import base64
from io import BytesIO as _BytesIO
import time
import os 
import numpy as np
from PIL import Image
import logging
from  loggerClass import loggerClass

class FormatConverter:


    def numpy_to_base64(np_array, enc_format="png", scalar=True, **kwargs):
        """
        Converts a numpy image into base 64 string for HTML displaying
        :param np_array:
        :param enc_format: The image format for displaying. If saved the image will have that extension.
        :param scalar:
        :return:
        """
        # Convert from 0-1 to 0-255
        try:
            if scalar:
                np_array = np.uint8(255 * np_array)
            else:
                np_array = np.uint8(np_array)

            im_pil = Image.fromarray(np_array)

            buff = _BytesIO()
            im_pil.save(buff, format=enc_format, **kwargs)
            encoded = base64.b64encode(buff.getvalue()).decode("utf-8")
            
            loggerClass.Writetofile(logging.INFO,"Numpy_to_base64 has done successfully...")
            return encoded

        except Exception as e:
    
            
            loggerClass.Writetofile(logging.WARNING,"Exception in numpy_to_base64...")

            loggerClass.Writetofile(logging.WARNING,e)
            return ("Sorry , there is some issue check logs for more detail..")

    def base64_to_image(string,enc_format="png"):
        decoded = base64.b64decode(string)
        buffer = _BytesIO(decoded)
        im = Image.open(buffer)

        try:
            os.mkdir("images")
            loggerClass.Writetofile(logging.INFO,"image folder is created in current directory.")
        
        except Exception as e:  
            
            loggerClass.Writetofile(logging.WARNING,"Image Folder Already existed...Ignore This Exception. ")           


        img_num=1
        for i in os.listdir(os.getcwd()+"/images"):
            img_num+=1
        file_name=os.getcwd()+"/images/"+"img_"+str(img_num)+"."+enc_format

        im.save(file_name, enc_format)
        
        return file_name    
    

