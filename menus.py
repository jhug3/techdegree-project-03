# menus.py created by John Hughes on 4/4/18

import logging, datetime, os, sys

from worklog import WorkLog

class Menu(WorkLog):
    '''
    Class Name: Menu
    Class Type: Child of WorkLog
    Creats the Main Menu for the Work Log program and facilitates user input for
    the main menu.
    '''
    
    def __init__(self):
        '''
        Starts the main menu, opens and sets up the logging and text file.
        '''
        # Enables the logger if self.loggin_bool is set to True.
        if self.logging_bool:
            logging.basicConfig(filename='work_log.log', 
                    filemode = 'a', 
                    level = logging.DEBUG
                    )
        logging.debug("In function: {} {}".format(Menu.__name__, 
                        "__init__"))
        try:
            # Opens file with the 'x' flag will not write if file exists already.
            with open('work_log.csv', 'x') as log_writer:
                # Header for the CSV, reason for no spaces.
                log_writer.write("Title,Date,Time,Notes\n")
        except FileExistsError:
            logging.debug("In function: {}, {}".format(Menu.__name__,
                            "__init__ of Menu class",
                            "Note: 'work_log.csv' file exists,"
                            "skipping file creation."))        
        self.main_menu()
        
    def main_menu(self):
        '''
        Sets up the main menu, gets user input, send user to next menu option.
        '''
        logging.debug("In function: {} {}".format(Menu.__name__,"main_menu",))
        self.clear_screen()
        print("Main Menu:\n"
        "Valid entries are the number or word in all caps.\n\n"
        "1) ADD a new entry\n"
        "2) SEARCH for existing entries\n"
        "3) QUIT the program\n"
        )
        user_input = input(":>")
        if user_input == '1' or user_input.upper() == 'ADD':
            logging.debug("In function: {} {},\n\tMenu choice: {}".format(
                            Menu.__name__,"main_menu",
                            user_input))
            from add_entry import AddEntry
            AddEntry.entry_title(self)
        elif user_input == '2' or user_input.upper() == 'SEARCH':
            logging.debug("In function: {} {},\n\tMenu choice: {}".format(
                            Menu.__name__,"main_menu",
                            user_input))
            from search_entry import SearchEntry
            SearchEntry.search_menu(self)
        elif user_input == '3' or user_input.upper() == 'QUIT':
            logging.debug("In function: {} {},\n\tMenu choice: {}".format(
                            Menu.__name__,"main_menu",
                            user_input))
            self.quit()
        else:
            nothing = input("Not a valid entry, hit enter to continue.")
            self.main_menu()
    
    def clear_screen(self):
        '''
        Clear screen function.
        '''
        logging.debug("In function: {} {}".format(Menu.__name__,"clear_screen"))
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def quit(self):
        '''
        Quits the program with an exit message.
        '''
        self.clear_screen()
        logging.debug("In function: {} {}".format(Menu.__name__,"quit"))
        print("Thanks for using Work Log!\nBye, bye now.")
        os._exit(0)
        
        
