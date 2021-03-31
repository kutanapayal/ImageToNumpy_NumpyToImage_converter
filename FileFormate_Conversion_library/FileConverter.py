import base64
from io import BytesIO as _BytesIO
import time
import numpy as np
from PIL import Image
import logging
from  loggerClass import loggerClass

class FileConverter:
  
    # Image utility functions
    def image_to_base64(image_path, enc_format="png", verbose=False, **kwargs):
        """
        Converts a PIL Image into base64 string for HTML displaying
        :param im: PIL Image object
        :param enc_format: The image format for displaying. If saved the image will have that extension.
        :param verbose: Allow for debugging tools
        :return: base64 encoding
        """

        try:
            t_start = time.time()
            im = Image.open(image_path) 
            buff = _BytesIO()
            im.save(buff, format=enc_format, **kwargs)
            encoded = base64.b64encode(buff.getvalue()).decode("utf-8")

            t_end = time.time()
            if verbose:
                loggerClass.Writetofile(logging.INFO,f"Image converted to base64 in {t_end - t_start:.3f} sec")           
            
            return encoded

        except Exception as e:
            
            loggerClass.Writetofile(logging.ERROR,"Exception in image_to_base64... ")
                        
            return ("Sorry , there is some issue check logs for more detail...")


    def base64_to_image(string):
        decoded = base64.b64decode(string)
        buffer = _BytesIO(decoded)
        im = Image.open(buffer)
        
        return im

    def base64_to_numpy(string, to_scalar=True):
        im = FileConverter.base64_to_image(string)
        np_array = np.asarray(im)

        if to_scalar:
            np_array = np_array / 255.0

        return np_array
