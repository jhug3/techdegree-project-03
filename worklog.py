# WorkLog.py created by John Hughes on 4/4/18

import logging, csv


class WorkLog():
    ''' 
    Class Name: WorkLog
    Class Type: Parent Class
    Sets up basic attributes and initializes function calls for the program
    Work Log.
    '''
    # Attributes used in program:
    task_title = None
    task_date = None
    task_time = None
    task_notes = None
    # Note: to endable logging set this to True
    logging_bool = False
    
    # Formating attributes
    date_format = '%m/%d/%Y'
    time_format = '%H:%M'
    
    def __init__(self):
        '''
        Enables the logger if logging_bool is set to True.
        '''
        if self.logging_bool:            
            logging.basicConfig(filename='work_log.log', 
                    filemode = 'w', 
                    level = logging.DEBUG
                    )
        logging.debug("In function: {} {},".format(
                        WorkLog.__name__,"__init__"))
        
        from menus import Menu
        menu = Menu()
        
if __name__ == "__main__":
    '''
    Starts the program.
    '''
    work_log = WorkLog()
    
