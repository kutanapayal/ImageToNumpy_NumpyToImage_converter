import logging
import logging.config

class loggerClass:

    '''
         Declare Logger Object and intialized it.
    '''

    logging.config.dictConfig(config = {
                'disable_existing_loggers': False,
                'version': 1,
        })
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')
        
    file_handler = logging.FileHandler('sample.log')
    file_handler.setFormatter(formatter)
        
    logger.addHandler(file_handler)
        

    def WriteLog(logger,level,message):
        '''
                This Fuction writes Log message on LogFile.
                logger : object og=f Logger use to recoed logs.
                level : the level or severity of the events they are used to track.
                message : which is log to be write on logfile.
        '''

        if level==logging.INFO:
                logger.info(message)

        elif level==logging.DEBUG:
                logger.debug(message)

        elif level==logging.CRITICAL:
                logger.critical(message)

        elif level==logging.WARNING:
                logger.warning(message)

        elif level==logging.ERROR:
                logger.error(message)

    def Writetofile(level, message):
        ''' 
            Writetofile Set's the logger level and call WriteLog method to Write log message on logfile.
            level : the level or severity of the events they are used to track.
            message : which is log entry in the logfile.
        '''

        loggerClass.logger.setLevel(level)        
        
        loggerClass.WriteLog(loggerClass.logger,level,message)

        

        
        
    

