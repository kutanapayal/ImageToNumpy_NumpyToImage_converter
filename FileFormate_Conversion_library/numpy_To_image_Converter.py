from FormatConverter import FormatConverter
import logging
from  loggerClass import loggerClass

class numpy_To_image_Converter:

    def numpyArray_TO_image(numpy_arr):

        '''
            numpyArray_TO_image converte the user given numpy array into image.
            numpy_arr :: user given numpy array to processed further.
        '''

        b64_string = FormatConverter.numpy_to_base64(numpy_arr)
    
        loggerClass.Writetofile(logging.INFO,"Base64 Of numpyarray :: "+b64_string)
    
        file_path = FormatConverter.base64_to_image(b64_string)

        loggerClass.Writetofile(logging.INFO,"Your File Saved AT :: "+file_path)

        return (file_path)