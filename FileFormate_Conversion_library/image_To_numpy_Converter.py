from FileConverter import FileConverter
import logging
from  loggerClass import loggerClass

class image_To_numpy_Converter:

    def image_To_numpyArray(im_path):
        '''
            image_To_numpyArray convert image file into numpy array.
            im_path :: user given image path to processed further.
        '''

        
        loggerClass.Writetofile(logging.INFO,"User Enterd file :: "+im_path)
        
        b64_string = FileConverter.image_to_base64(im_path, enc_format="png", verbose=True)
        
        loggerClass.Writetofile(logging.INFO,"Base64 Of image :: "+ b64_string )

        numpy_arr = FileConverter.base64_to_numpy(b64_string)

        if numpy_arr is not None:
            loggerClass.Writetofile(logging.INFO,"base64 to numpy array conversion has done successfully.")

        return (numpy_arr)

