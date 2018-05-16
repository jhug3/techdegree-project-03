# search_entry.py created by John Hughes on 4/10/18

import logging, csv, datetime, re

from worklog import WorkLog

class SearchEntry(WorkLog):
    '''
    Class Name: SearchEntry
    Class Type: Child of WorkLog
    Creats the Main Menu for the Work Log program and facilitates user input for
    the main menu.
    '''
    
    def __init__(self):
        # Enables the logger if self.loggin_bool is set to True.
        if self.logging_bool:
            logging.basicConfig(filename='work_log.log', 
                    filemode = 'a', 
                    level = logging.DEBUG
                    )
        logging.debug("In function: {}, {}".format(SearchEntry.__name__,
                    "__init__"))
    
    def search_menu(self):
        '''
        Displays the search sub-menu, handles uers input and calls the function
            chossen.
        '''
        self.clear_screen()
        print("Search Main Menu: \n")
        choice = input( "1) Exact search by TITLE.\n"
                        "2) Exact search by DATE.\n"
                        "3) Exact search by TIME.\n"
                        "4) Exact search by NOTES.\n"
                        "5) REGEX search.\n"
                        "6) Search by a RANGE of dates.\n"
                        "7) Display ALL entries.\n"
                        "8) Hit enter to return to main menu.\n"
                        ":>")
        self.clear_screen()
        if choice == '1' or choice.upper() == 'TITLE':
            logging.debug("In function: {}, User chose to {} {}"
                        .format(SearchEntry.__name__, '1: ', "search by title"))
            SearchEntry.search_title(self)
        elif choice == '2' or choice.upper() == 'DATE':
            logging.debug("In function: {}, User chose to {} {}"
                        .format(SearchEntry.__name__, '2: ', "search by date"))
            SearchEntry.search_date(self)
        elif choice == '3' or choice.upper() == 'TIME':
            logging.debug("In function: {}, User chose to {} {}"
                        .format(SearchEntry.__name__, '3: ', "search by time"))
            SearchEntry.search_time(self) 
        elif choice == '4' or choice.upper() == 'NOTES':
            logging.debug("In function: {}, User chose to {} {}"
                        .format(SearchEntry.__name__, '4: ', "search by notes"))
            SearchEntry.search_notes(self)
            SearchEntry.exact_search(self)
        elif choice == '5' or choice.upper() == 'REGEX':
            logging.debug("In function: {}, User chose to {} {}"
                        .format(SearchEntry.__name__, '5: ', "search by regex"))
            SearchEntry.regex_search(self)
        elif choice == '6' or choice.upper() == 'RANGE':
            logging.debug("In function: {}, User chose to {} {}"
                        .format(SearchEntry.__name__, '6: ', "search by range"))
            SearchEntry.date_range_search(self)
        elif choice == '7' or choice.upper() == 'ALL':
            logging.debug("In function: {}, User chose to {} {}"
                        .format(SearchEntry.__name__, '8: ', "display all."))
            SearchEntry.search_display_all(self)
        elif choice == '8' or choice.upper() == '':
            logging.debug("In function: {}, User chose to {} {}"
                    .format(SearchEntry.__name__, '7: ', "return to main menu"))
            self.main_menu()
        else:
            nothing = input("Not a valid entry, hit enter to continue.")
            logging.debug("In function: {}, User {}"
                        .format(SearchEntry.__name__, "input invalid"))
            SearchEntry.search_menu(self)
    
    def search_title(self):
        '''
        Searches for an exact match to the title of an entry, may find multiple
            results.
        '''
        logging.debug("In function: {} {},".format(SearchEntry.__name__,
                                                "regex_search"))
        user_search_title = input("Please enter the title you wish to "
                                    "search for\n:>")
        title_list = []
        self.clear_screen()
        # Setting formatting to match the formatting of title input.
        user_search_title = user_search_title.title()
        logging.debug("In function: {} {},\n\tUser input is: {}".format(
                        SearchEntry.__name__,"regex_search",
                        user_search_title))
        # Open file and run the search against the title.
        # Try exception to handle missing file.
        try:
            with open('work_log.csv', 'r', newline='') as csv_reader:
                log_reader = csv.DictReader(csv_reader)
                lr_enum = enumerate(log_reader, start=1)
                index, row = lr_enum.__next__()
                logging.debug("In function: {} {},\n\tlr_enum.next() tuple: {}, {}"
                            .format(SearchEntry.__name__,"regex_search",
                            index, row))
                while row:
                    # Try exception to handle the end of enumeration
                    try:
                        next_row = lr_enum.__next__()
                        # Try expection to handle an empty row.
                        try:
                            if row['Title'] == user_search_title:
                                title_list.append({'Title' : row['Title'],
                                                'Date' : row['Date'],
                                                'Time' : row['Time'],
                                                'Notes' : row['Notes']})
                        except KeyError:
                            self.clear_screen()
                            choice = input("Could not find that title entry:\n"
                                            "1) [T]ry again\n"
                                            "2) Return to the [S]earch menu\n"
                                            "3) Return to the [M]ain Menu\n"
                                            "Note: Title must match exactly.\n"
                                            ":>")
                            if choice == '1' or choice.upper() == 'T' or choice == '':
                                logging.debug("In function: {} {},\n\tTry again: {}"
                                            .format(SearchEntry.__name__,
                                            "regex_search",
                                            "could not find"))
                                SearchEntry.search_title(self)
                            elif choice == '2' or choice.upper() == 'S':
                                logging.debug("In function: {} {},\n\tSearch Menu: {}"
                                            .format(SearchEntry.__name__,
                                            "regex_search",
                                            "could not find"))
                                SearchEntry.search_menu(self)
                            elif choice == '3' or choice.upper() == 'M':
                                logging.debug("In function: {} {},\n\t"
                                            "Return to main menu: {}"
                                            .format(SearchEntry.__name__,
                                            "regex_search",
                                            "could not find"))
                                self.main_menu()
                            # Catch all and return to main menu
                            else:
                                nothing = input("Hit enter to continue to the "
                                                "main menu.")
                                self.main_menu()
                        index, row = next_row
                        logging.debug("In function: {} {},\n\tlr_enum.next() "
                            "tuple: {}, {}".format(
                            SearchEntry.__name__,"regex_search",
                            index, row))
                    except StopIteration:
                        # Catches the end of file.
                        logging.debug("In function: {} {},\n\tlr_enum.next() "
                            "tuple: {}, {}".format(
                            SearchEntry.__name__,"regex_search"
                            ,index, row))
                        # Prints the last row left in the itirator/generator when done.
                        logging.debug("In function: {} {},\n\tRaw "
                                    "row: {}\n".format(
                                    SearchEntry.__name__,"regex_search",
                                    row))
                        # Try expection to handle an empty row.
                        try:
                            if row['Title'] == user_search_title:
                                title_list.append({'Title' : row['Title'],
                                                'Date' : row['Date'],
                                                'Time' : row['Time'],
                                                'Notes' : row['Notes']})
                        except KeyError:
                            self.clear_screen()
                            choice = input("Could not find that title entry:\n"
                                            "1) [T]ry again\n"
                                            "2) Return to the [S]earch menu\n"
                                            "3) Return to the [M]ain Menu\n"
                                            "Note: Title must match exactly.\n"
                                            ":>")
                            if choice == '1' or choice.upper() == 'T' or choice == '':
                                logging.debug("In function: {} {},\n\tTry "
                                            "again: {}".format(
                                            SearchEntry.__name__,"regex_search",
                                            "could not find"))
                                SearchEntry.search_title(self)
                            elif choice == '2' or choice.upper() == 'S':
                                logging.debug("In function: {} {},\n\tSearch "
                                            "Menu: {}".format(
                                            SearchEntry.__name__,"regex_search",
                                            "could not find"))
                                SearchEntry.search_menu(self)
                            elif choice == '3' or choice.upper() == 'M':
                                logging.debug("In function: {} {},\n\tReturn to "
                                            "main menu: {}".format(
                                            SearchEntry.__name__,"regex_search",
                                            "could not find"))
                                self.main_menu()
                            # Catch all and return to main menu
                            else:                            
                                nothing = input("Hit enter to continue to the main menu.")
                                self.main_menu()
                        index, row = None, None
                from display_entry import DisplayEntry
                DisplayEntry.display_entries(self, title_list)
                # When end of file is reached and no match found: choice.
                if index == None:
                    self.clear_screen()
                    choice = input("Could not find that title entry:\n"
                                    "1) [T]ry again\n"
                                    "2) Return to the [S]earch menu\n"
                                    "3) Return to the [M]ain Menu\n"
                                    "Note: Title must match exactly.\n"
                                    ":>")
                    if choice == '1' or choice.upper() == 'T' or choice == '':
                        logging.debug("In function: {} {},\n\tTry again: {}".format(
                                SearchEntry.__name__,"regex_search",
                                "could not find"))
                        SearchEntry.search_title(self)
                    elif choice == '2' or choice.upper() == 'S':
                        logging.debug("In function: {} {},\n\tSearch "
                                    "Menu: {}".format(
                                    SearchEntry.__name__,"regex_search",
                                    "could not find"))
                        SearchEntry.search_menu(self)
                    elif choice == '3' or choice.upper() == 'M':
                        logging.debug("In function: {} {},\n\tReturn to "
                                    "main menu: {}".format(
                                    SearchEntry.__name__,"regex_search",
                                    "could not find"))
                        self.main_menu()
                    # Catch all and return to main menu
                    else:
                        self.main_menu()
        # Handles exception in case the file is missing.
        except FileNotFoundError:
            nothing = input("Could not find 'work_log.csv' please check to be "
                "sure it is present and in the correct directory.\n"
                "Returning to Main Menu. Hit enter to continue.")
            self.main_menu()
    
    def search_date(self):
        '''
        Searches for the first exact match of the date.
        '''
        self.clear_screen() 
        logging.debug("In function: {} {},".format(
                    SearchEntry.__name__,"search_date"))
        date_list = []
        user_search_date = input("Please enter the date you wish to "
                                    "search for:\n"
                                    "In the following format: MM/DD/YYYY\n:>")
        self.clear_screen()
        # Checking for a valid entry date, changing user input to a datetime.
        try: 
            user_temp_date = datetime.datetime.strptime(
                                        user_search_date, self.date_format)
            logging.debug("In function: {} {},\t\ntry block: {}".format(
                            SearchEntry.__name__,"search_date",
                            user_temp_date))
        except ValueError:
            logging.debug("In function: {} {},\n\texception: ValueError, "
                        "Not a valid date. Please try again choice.".format(
                        SearchEntry.__name__,"search_date"))
            self.clear_screen()
            choice = input("That was not a valid date. Please try again:\n"
                            "1) [T]ry again\n"
                            "2) Return to the [S]earch menu\n"
                            "3) Return to the [M]ain Menu\n"
                            "Note: Date must match exactly.\n"
                            ":>")
            if choice == '1' or choice.upper() == 'T' or choice == '':
                logging.debug("In function: {} {},\n\tTry again: {}".format(
                        SearchEntry.__name__,"search_date",
                        "Invalid input"))
                SearchEntry.search_date(self)
            elif choice == '2' or choice.upper() == 'S':
                logging.debug("In function: {} {},\n\tSearch menu: {}".format(
                        SearchEntry.__name__,"search_date",
                        "return to search menu"))
                SearchEntry.search_menu(self)
            elif choice == '3' or choice.upper() == 'M':
                logging.debug("In function: {} {},\n\tReturn to "
                            "main menu: {}".format(
                            SearchEntry.__name__,"search_date",
                            "Returning to main menu"))
                self.main_menu()
            else:
                self.main_menu()
        # Setting the input back to a str (from a datetime) for the search.
        user_search_date = user_temp_date.strftime(self.date_format)
        # Open file and run the search against the date.  
        # Try exception to handle missing file. 
        try:
            with open('work_log.csv', 'r', newline='') as csv_reader:
                log_reader = csv.DictReader(csv_reader)
                lr_enum = enumerate(log_reader, start=1)
                index, row = lr_enum.__next__()
                logging.debug("In function: {} {},\n\tlr_enum.next() "
                            "tuple: {}, {}".format(
                            SearchEntry.__name__,"search_date",
                            index, row))
                while row:
                    # Try exception to handle the end of enumeration
                    try:
                        next_row = lr_enum.__next__()
                        # Try expection to handle an empty row.
                        try:
                            if row['Date'] == user_search_date:
                                date_list.append({'Title' : row['Title'],
                                                'Date' : row['Date'],
                                                'Time' : row['Time'],
                                                'Notes' : row['Notes']})
                        except KeyError:
                            self.clear_screen()
                            choice = input("Could not find that title entry:\n"
                                            "1) [T]ry again\n"
                                            "2) Return to the [S]earch menu\n"
                                            "3) Return to the [M]ain Menu\n"
                                            "Note: Date must match exactly.\n"
                                            ":>")
                            if choice == '1' or choice.upper() == 'T' or choice == '':
                                logging.debug("In function: {} {},\n\tTry "
                                            "again: {}".format(
                                            SearchEntry.__name__,"search_date",
                                            "could not find"))
                                SearchEntry.search_date(self)
                            elif choice == '2' or choice.upper() == 'S':
                                logging.debug("In function: {} {},\n\t Search "
                                            "Menu: {}".format(
                                            SearchEntry.__name__,"search_date",
                                            "could not find"))
                                SearchEntry.search_menu(self)
                            elif choice == '3' or choice.upper() == 'M':
                                logging.debug("In function: {} {},\n\tReturn to "
                                            "main menu: {}".format(
                                            SearchEntry.__name__,"search_date",
                                            "could not find"))
                                self.main_menu()
                            # Catch all and return to main menu
                            else:
                                nothing = input("Hit enter to continue to the main menu.")
                                self.main_menu()
                        index, row = next_row
                        logging.debug("In function: {} {},\n\tlr_enum.next() "
                            "tuple: {}, {}".format(
                            SearchEntry.__name__,"search_date",
                            index, row))
                    except StopIteration:
                        # Catches the end of file.
                        logging.debug("In function: {} {},\n\tlr_enum.next() "
                            "tuple: {}, {}".format(
                            SearchEntry.__name__,"search_date",
                            index, row))
                        # Prints the last row left in the itirator/generator when done.
                        logging.debug("In function: {} {},\n\tRaw row: {}\n".format(
                                    SearchEntry.__name__,"search_date",
                                    row))
                        # Try expection to handle an empty row.
                        try:
                            if row['Date'] == user_search_date:
                                date_list.append({'Title' : row['Title'],
                                                'Date' : row['Date'],
                                                'Time' : row['Time'],
                                                'Notes' : row['Notes']})
                        except KeyError:
                            self.clear_screen()
                            choice = input("Could not find that title entry:\n"
                                            "1) [T]ry again\n"
                                            "2) Return to the [S]earch menu\n"
                                            "3) Return to the [M]ain Menu\n"
                                            "Note: Date must match exactly.\n"
                                            ":>")
                            if choice == '1' or choice.upper() == 'T' or choice == '':
                                logging.debug("In function: {} {},\n\tTry "
                                            "again: {}".format(
                                            SearchEntry.__name__,"search_date",
                                            "could not find"))
                                SearchEntry.search_date(self)
                            elif choice == '2' or choice.upper() == 'S':
                                logging.debug("In function: {} {},\n\tSearch "
                                            "Menu: {}".format(
                                            SearchEntry.__name__,"search_date",
                                            "could not find"))
                                SearchEntry.search_menu(self)
                            elif choice == '3' or choice.upper() == 'M':
                                logging.debug("In function: {} {},\n\tReturn to"
                                            "main menu: {}".format(
                                            SearchEntry.__name__,"search_date",
                                            "could not find"))
                                self.main_menu()
                            # Catch all and return to main menu
                            else:                            
                                nothing = input("Hit enter to continue to the main menu.")
                                self.main_menu()
                        index, row = None, None
                from display_entry import DisplayEntry
                DisplayEntry.display_entries(self, date_list)
                if index == None:
                    self.clear_screen()
                    choice = input("Could not find that date entry:\n"
                                    "1) [T]ry again\n"
                                    "2) Return to the [S]earch menu\n"
                                    "3) Return to the [M]ain Menu\n"
                                    "Note: Date must match exactly.\n"
                                    ":>")
                    if choice == '1' or choice.upper() == 'T' or choice == '':
                        logging.debug("In function: {} {},\n\tTry "
                                    "again: {}".format(
                                    SearchEntry.__name__,"search_date", 
                                    "could not find"))
                        SearchEntry.search_date(self)
                    elif choice == '2' or choice.upper() == 'S':
                        logging.debug("In function: {} {},\n\tSearh "
                                    "Menu: {}".format(
                                    SearchEntry.__name__,"search_date", 
                                    "return to search menu"))
                        SearchEntry.search_menu(self)
                    elif choice == '3' or choice.upper() == 'M':
                        logging.debug("In function: {} {},\n\tMain "
                                    "menu: {}".format(
                                    SearchEntry.__name__,"search_date",
                                    "return to main menu"))
                        self.main_menu()
                    else:
                        self.main_menu()
        # Handles exception in case the file is missing.
        except FileNotFoundError:
            nothing = input("Could not find 'work_log.csv' please check to be "
                "sure it is present and in the correct directory.\n"
                "Returning to Main Menu. Hit enter to continue.")
            self.main_menu()
            
    def search_time(self):
        '''
        Searches for the first exact match of the time.
        '''
        logging.debug("In function: {} {}".format(SearchEntry.__name__,"search_time"))
        time_list = []
        user_search_time = input("Please enter the time you wish to "
                                "search for:\n"
                                "Please use the following formats:\n"
                                " _____________________________________\n"
                                "|MM     |For minutes                  |\n"
                                "|HH:MM  |For hours(24) and minutes    |\n"
                                "|_____________________________________|\n"
                                ":>")
        self.clear_screen()
        logging.debug("In function: {} {},\n\ttime input: {}".format(
                    SearchEntry.__name__,"search_time",
                    user_search_time))
       # Checking for minute only input:
        if len(user_search_time) == 2:
            # Checking for out of bound input on minutes.
            try:
                user_temp_time = datetime.datetime.strptime(user_search_time, '%M')
                logging.debug("In function: {} {},\n\ttime input: {}, "
                        "user_temp_time: {}".format(
                        SearchEntry.__name__,"search_time",
                        user_search_time,
                        user_temp_time))
            except ValueError:
                nothing = input("Not a valid time entry. Please try again.")
                SearchEntry.search_time(self)
            else:
                # Converting back to a str for searching.
                user_search_time = user_temp_time.strftime('%H:%M')
                logging.debug("In function: {} {},\n\tformated user "
                            "search_time: {}".format(
                            SearchEntry.__name__,"search_time",
                            user_search_time))
        # Checking for hour and minute input:
        elif len(user_search_time) == 5:
            # Checking of out of bound hour or minute input.
            try:
                user_temp_time = datetime.datetime.strptime(
                                                    user_search_time, '%H:%M')
                logging.debug("In function: {} {},\n\ttime input: {}, "
                        "user_temp_time: {}".format(
                        SearchEntry.__name__,"search_time",
                        user_search_time,
                        user_temp_time))
            except ValueError:
                nothing = input("Not a valid time entry. Please try again.")
                SearchEntry.search_time(self)
            else:
                # Converting to a str for formating.
                user_search_time = user_temp_time.strftime('%H:%M')
                logging.debug("In function: {} {},\n\tformated user "
                            "search_time: {}".format(
                            SearchEntry.__name__,"search_time",
                            user_search_time))
        # Open file and run the search against the date.   
        # Try exception to handle missing file.
        try:
            with open('work_log.csv', 'r', newline='') as csv_reader:
                log_reader = csv.DictReader(csv_reader)
                lr_enum = enumerate(log_reader, start=1)
                index, row = lr_enum.__next__()
                logging.debug("In function: {} {},\n\tlr_enum.next() "
                            "tuple: {}, {}".format(
                            SearchEntry.__name__,"search_time",
                            index, row))
                while row:
                    # Try exception to handle the end of enumeration
                    try:
                        next_row = lr_enum.__next__()
                        # Try expection to handle an empty row.
                        try:
                            if row['Time'] == user_search_time:
                                time_list.append({'Title' : row['Title'],
                                                'Date' : row['Date'],
                                                'Time' : row['Time'],
                                                'Notes' : row['Notes']})
                        except KeyError:
                            self.clear_screen()
                            choice = input("Could not find that title entry:\n"
                                            "1) [T]ry again\n"
                                            "2) Return to the [S]earch menu\n"
                                            "3) Return to the [M]ain Menu\n"
                                            "Note: time must match exactly.\n"
                                            ":>")
                            if choice == '1' or choice.upper() == 'T' or choice == '':
                                logging.debug("In function: {} {},\n\tTry "
                                            "again: {}".format(
                                            SearchEntry.__name__,"search_time",
                                            "could not find"))
                                SearchEntry.search_time(self)
                            elif choice == '2' or choice.upper() == 'S':
                                logging.debug("In function: {} {},\n\tSearch "
                                            "Menu: {}".format(
                                            SearchEntry.__name__,"search_time",
                                            "could not find"))
                                SearchEntry.search_menu(self)
                            elif choice == '3' or choice.upper() == 'M':
                                logging.debug("In function: {} {},\n\tReturn to "
                                            "main menu: {}".format(
                                            SearchEntry.__name__,"search_time",
                                            "could not find"))
                                self.main_menu()
                            # Catch all and return to main menu
                            else:
                                nothing = input("Hit enter to continue to the main menu.")
                                self.main_menu()
                        index, row = next_row
                        logging.debug("In function: {} {},\n\tlr_enum.next() "
                            "tuple: {}, {}".format(
                            SearchEntry.__name__,"search_time",
                            index, row))
                    except StopIteration:
                        # Catches the end of file.
                        logging.debug("In function: {} {},\n\tlr_enum.next() "
                            "tuple: {}, {}".format(
                            SearchEntry.__name__,"search_time",
                            index, row))
                        # Prints the last row left in the itirator/generator when done.
                        logging.debug("In function: {} {},\n\tRaw row: {}\n".format(
                                    SearchEntry.__name__,"search_time",
                                    row))
                        # Try expection to handle an empty row.
                        try:
                            if row['Time'] == user_search_time:
                                time_list.append({'Title' : row['Title'],
                                                'Date' : row['Date'],
                                                'Time' : row['Time'],
                                                'Notes' : row['Notes']})
                        except KeyError:
                            self.clear_screen()
                            choice = input("Could not find that title entry:\n"
                                            "1) [T]ry again\n"
                                            "2) Return to the [S]earch menu\n"
                                            "3) Return to the [M]ain Menu\n"
                                            "Note: time must match exactly.\n"
                                            ":>")
                            if choice == '1' or choice.upper() == 'T' or choice == '':
                                logging.debug("In function: {} {},\n\tTry "
                                            "again: {}".format(
                                            SearchEntry.__name__,"search_time",
                                            "could not find"))
                                SearchEntry.search_time(self)
                            elif choice == '2' or choice.upper() == 'S':
                                logging.debug("In function: {} {},\n\tSearch "
                                            "Menu: {}".format(
                                            SearchEntry.__name__,"search_time",
                                            "could not find"))
                                SearchEntry.search_menu(self)
                            elif choice == '3' or choice.upper() == 'M':
                                logging.debug("In function: {} {},\n\tReturn to "
                                            "main menu: {}".format(
                                            SearchEntry.__name__,"search_time",
                                            "could not find"))
                                self.main_menu()
                            # Catch all and return to main menu
                            else:                            
                                nothing = input("Hit enter to continue to the main menu.")
                                self.main_menu()
                        index, row = None, None
                from display_entry import DisplayEntry
                DisplayEntry.display_entries(self, time_list)
                # When end of file is reached and no match found: choice.
                if index == None:
                    self.clear_screen()
                    choice = input("Could not find that time entry:\n:"
                                    "1) [T]ry again\n"
                                    "2) Return to the [S]earch menu\n"
                                    "3) Return to the [M]ain Menu\n"
                                    "Note: time must match exactly.\n"
                                    ":>")
                    if choice == '1' or choice.upper() == 'T' or choice == '':
                        logging.debug("In function: {} {},\n\tTry "
                                    "again: {}".format(
                                    SearchEntry.__name__,"search_time",
                                    "could not find"))
                        SearchEntry.search_time(self)
                    elif choice == '2' or choice.upper() == 'S':
                        logging.debug("In function: {} {},\n\tSearch "
                                    "Menu: {}".format(
                                    SearchEntry.__name__,"search_time",
                                    "could not find"))
                        SearchEntry.search_menu(self)
                    elif choice == '3' or choice.upper() == 'M':
                        logging.debug("In function: {} {},\n\tReturn to "
                                    "main menu: {}".format(
                                    SearchEntry.__name__,"search_time",
                                    "could not find"))
                        self.main_menu()
                    else:
                        self.main_menu()
        # Handles exception in case the file is missing.
        except FileNotFoundError:
            nothing = input("Could not find 'work_log.csv' please check to be "
                "sure it is present and in the correct directory.\n"
                "Returning to Main Menu. Hit enter to continue.")
            self.main_menu()
        
    def search_notes(self):
        '''
        Searches for the first exact match of the notes.
        '''
        self.clear_screen()
        logging.debug("In function: {} {},".format(SearchEntry.__name__,"search_notes"))
        user_search_notes = input("Please enter the exact notes you wish to "
                                "search for.\n:>")
        notes_list = []
        self.clear_screen()
        user_temp_notes = user_search_notes.split()
        logging.debug("In function: {} {},\n\tuser input: {}\n\t"
                    "user_temp_notes (split): {}".format(
                    SearchEntry.__name__,"search_notes",
                    user_search_notes,
                    user_temp_notes))
        # Handeling the exeption for when the string is blank.
        # Matching formating to original input by capitalizing first leter of
        #   first word.
        try:
            user_split_title = user_temp_notes[0]
        except IndexError:
            logging.warning("In function: {} {},\n\ttry block: handeled exception:"
                            "IndexError for a default entry of zero len string."
                            .format(SearchEntry.__name__,"search_notes"))
        # Handeling the exeption for when the string is blank.
        try:
            user_temp_notes[0] = user_split_title.title()
        except UnboundLocalError:
            logging.warning("In function: {} {},\n\ttry block: handeled exception:"
                            "UnboundLocalError for a default entry of zero len "
                            "string.".format(SearchEntry.__name__,"search_notes",))
        logging.debug("In function: {} {},\n\tuser input: {} "
                "user_temp_notes (split): {}".format(
                SearchEntry.__name__,"search_notes",
                user_search_notes,
                user_temp_notes))
        # Joining string after formating, making first word a title/capital.
        user_search_notes = ' '.join(user_temp_notes)
        logging.debug("In function: {} {},\n\tuser input "
                "(title and joined): {}".format(
                SearchEntry.__name__,"search_notes",
                user_search_notes))
        # Open file and run the search against the notes. 
        # Try exception to handle missing file.  
        try:
            with open('work_log.csv', 'r', newline='') as csv_reader:
                log_reader = csv.DictReader(csv_reader)
                lr_enum = enumerate(log_reader, start=1)
                index, row = lr_enum.__next__()
                logging.debug("In function: {} {},\n\tlr_enum.next() "
                            "tuple: {}, {}".format(
                            SearchEntry.__name__,"search_notes",
                            index, row))
                while row:
                    # Try exception to handle the end of enumeration
                    try:
                        next_row = lr_enum.__next__()
                        # Try expection to handle an empty row.
                        try:
                            if row['Notes'] == user_search_notes:
                                notes_list.append({'Title' : row['Title'],
                                                'Date' : row['Date'],
                                                'Time' : row['Time'],
                                                'Notes' : row['Notes']})
                        except KeyError:
                            self.clear_screen()
                            choice = input("Could not find that title entry:\n"
                                            "1) [T]ry again\n"
                                            "2) Return to the [S]earch menu\n"
                                            "3) Return to the [M]ain Menu\n"
                                            "Note: notes must match exactly.\n"
                                            ":>")
                            if choice == '1' or choice.upper() == 'T' or choice == '':
                                logging.debug("In function: {} {},\n\tTry "
                                            "again: {}".format(
                                            SearchEntry.__name__,"search_notes",
                                            "could not find"))
                                SearchEntry.search_notes(self)
                            elif choice == '2' or choice.upper() == 'S':
                                logging.debug("In function: {} {},\n\tSearch "
                                            "Menu: {}".format(
                                            SearchEntry.__name__,"search_notes",
                                            "could not find"))
                                SearchEntry.search_menu(self)
                            elif choice == '3' or choice.upper() == 'M':
                                logging.debug("In function: {} {},\n\tReturn to "
                                            "main menu: {}".format(
                                            SearchEntry.__name__,"search_notes",
                                            "could not find"))
                                self.main_menu()
                            # Catch all and return to main menu
                            else:
                                nothing = input("Hit enter to continue to the main menu.")
                                self.main_menu()
                        index, row = next_row
                        logging.debug("In function: {} {},\n\tlr_enum.next() "
                            "tuple: {}, {}".format(
                            SearchEntry.__name__,"search_notes",
                            index, row))
                    except StopIteration:
                        # Catches the end of file.
                        logging.debug("In function: {} {},\n\tlr_enum.next() "
                            "tuple: {}, {}".format(
                            SearchEntry.__name__,"search_notes",
                            index, row))
                        # Prints the last row left in the itirator/generator when done.
                        logging.debug("In function: {} {},\n\tRaw row: "
                                    "{}\n".format(
                                    SearchEntry.__name__,"search_notes",
                                    row))
                        # Try expection to handle an empty row.
                        try:
                            if row['Notes'] == user_search_notes:
                                notes_list.append({'Title' : row['Title'],
                                                'Date' : row['Date'],
                                                'Time' : row['Time'],
                                                'Notes' : row['Notes']})
                        except KeyError:
                            self.clear_screen()
                            choice = input("Could not find that title entry:\n"
                                            "1) [T]ry again\n"
                                            "2) Return to the [S]earch menu\n"
                                            "3) Return to the [M]ain Menu\n"
                                            "Note: notes must match exactly.\n"
                                            ":>")
                            if choice == '1' or choice.upper() == 'T' or choice == '':
                                logging.debug("In function: {} {},\n\tTry again: "
                                            "{}".format(
                                            SearchEntry.__name__,"search_notes",
                                            "could not find"))
                                SearchEntry.search_notes(self)
                            elif choice == '2' or choice.upper() == 'S':
                                logging.debug("In function: {} {},\n\tSearch "
                                            "Menu: {}".format(
                                            SearchEntry.__name__,"search_notes",
                                            "could not find"))
                                SearchEntry.search_menu(self)
                            elif choice == '3' or choice.upper() == 'M':
                                logging.debug("In function: {} {},\n\tReturn to "
                                            "main menu: {}".format(
                                            SearchEntry.__name__,"search_notes",
                                            "could not find"))
                                self.main_menu()
                            # Catch all and return to main menu
                            else:                            
                                nothing = input("Hit enter to continue to the main menu.")
                                self.main_menu()
                        index, row = None, None
                from display_entry import DisplayEntry
                DisplayEntry.display_entries(self, notes_list)
                        # When end of file is reached and no match found: choice.
                if index == None:
                            self.clear_screen()
                            choice = input("Could not find that time entry:\n"
                                            "1) [T]ry again\n"
                                            "2) Return to the [S]earch menu\n"
                                            "3) Return to the [M]ain Menu\n"
                                            "Note: notes must match exactly.\n"
                                            ":>")
                            self.clear_screen()
                            if choice == '1' or choice.upper() == 'T' or choice == '':
                                logging.debug("In function: {} {},\n\tTry "
                                            "again: {}".format(
                                            SearchEntry.__name__,"search_notes",
                                            "could not find"))
                                SearchEntry.search_notes(self)
                            elif choice == '2' or choice.upper() == 'S':
                                logging.debug("In function: {} {},\n\tSearch "
                                            "Menu: {}".format(
                                            SearchEntry.__name__,"search_notes",
                                            "return to search menu"))
                                SearchEntry.search_menu(self)
                            elif choice == '3' or choice.upper() == 'M':
                                logging.debug("In function: {} {},\n\tMain "
                                            "Menu: {}".format(
                                            SearchEntry.__name__,"search_notes",
                                            "return to main menu"))
                                self.main_menu()
                            else:
                                self.main_menu()
        # Handles exception in case the file is missing.
        except FileNotFoundError:
            nothing = input("Could not find 'work_log.csv' please check to be "
                "sure it is present and in the correct directory.\n"
                "Returning to Main Menu. Hit enter to continue.")
            self.main_menu()
                
    def regex_search(self):
        '''
        Does a regex search on each data type of an entry, will return to a 
            display function each result.
        '''
        logging.debug("In function: {} {}".format(SearchEntry.__name__,
                        "regex_search"))
        regex_list = []
        num_list = []
        user_search_input = input("Enter the data you wish to search for.\n"
                                " _____________________________________\n"
                                "|If you enter a time or date          |\n"
                                "|please use the following formats:    |\n"
                                "|_____________________________________|\n"
                                "|For time:                            |\n"
                                "|MM     |For minutes                  |\n"
                                "|HH:MM  |For hours(24) and minutes    |\n"
                                "|_____________________________________|\n"
                                "|For dates: MM/DD/YYYY                |\n"
                                "|_____________________________________|\n"
                                ":>")
        logging.debug("In function: {} {},\m\tuser input is: {}".format(
                            SearchEntry.__name__,"regex_search",
                            user_search_input))
        # Generate the regex search text string, added extra puncuation 
            # just in case to the end.2
        regex_search_text = r'' + user_search_input #+ '[\w!\?\:\/\.]*'
        logging.debug("In function: {} {},\n\tregex search string "
                        "is: {}".format(
                        SearchEntry.__name__,"regex_search",
                        regex_search_text))
        # Try exception to handle missing file. 
        try:
            with open('work_log.csv', 'r', newline='') as csv_reader:
                log_reader = csv.DictReader(csv_reader)
                lr_enum = enumerate(log_reader, start=0)
                index, row = lr_enum.__next__()
                logging.debug("In function: {} {},\n\tlr_enum.next() "
                            "tuple: {}, {}".format(
                            SearchEntry.__name__,"regex_search",
                            index, row))
                while row:
                    # Try exception to handle the end of enumeration
                    try:
                        logging.debug("\trow is: {}, row type is: {}".format(
                                        row, type(row)))
                        next_row = lr_enum.__next__()
                        # Creating the search string out of the input from the
                            # file row data.
                        row_search_text = row['Title'] + ' ' + row['Date'] + ' ' + row['Time'] + ' ' + row['Notes']
                        logging.debug("In function: {} {}\n\t"
                                "Regex_search_text is: {}\n\t"
                                "Row_search_text is: {}".format(
                                SearchEntry.__name__,"regex_search",
                                regex_search_text,
                                row_search_text))
                        # Try expection to handle an empty row.
                        try:
                            if re.search(regex_search_text, row_search_text,re.I):
                                regex_list.append({'Title' : row['Title'],
                                                    'Date' : row['Date'],
                                                    'Time' : row['Time'],
                                                    'Notes' : row['Notes']})
                                logging.debug("In function: {} {},\n\tregex_list is: {}".format(
                                        SearchEntry.__name__,"regex_search",
                                        regex_list))
                        except KeyError:
                            self.clear_screen()
                            choice = input("Could not find any data on that entry:\n"
                                            "1) [T]ry again\n"
                                            "2) Return to the [S]earch menu\n"
                                            "3) Return to the [M]ain Menu\n"
                                            ":>")
                            self.clear_screen()
                            if choice == '1' or choice.upper() == 'T' or choice == '':
                                logging.debug("In function: {} {},\n\tTry "
                                            "again: {}".format(
                                            SearchEntry.__name__,"regex_search",
                                            "could not find"))
                                SearchEntry.regex_search(self)
                            elif choice == '2' or choice.upper() == 'S':
                                logging.debug("In function: {}, Search Menu: {}"
                                            .format(SearchEntry.__name__, "could not find"))
                                SearchEntry.search_menu(self)
                            elif choice == '3' or choice.upper() == 'M':
                                logging.debug("In function: {} {},\n\tReturn to "
                                            "main menu: {}".format(
                                            SearchEntry.__name__,"regex_search",
                                            "could not find"))
                                self.main_menu()
                            # Catch all and return to main menu
                            else:
                                self.main_menu()
                        index, row = next_row
                        logging.debug("In function: {} {},\n\tlr_enum.next() "
                            "tuple: {}, {}".format(
                            SearchEntry.__name__,"regex_search",
                            index, row))
                    except StopIteration:
                        # Catches the end of file.
                        logging.debug("In function: {} {},\n\tlr_enum.next() "
                            "tuple: {}, {}".format(
                            SearchEntry.__name__,"regex_search",
                            index, row))
                        # Prints the last row left in the itirator/generator when done.
                        logging.debug("In function: {} {},\n\tRaw row: "
                                    "{}\n".format(
                                    SearchEntry.__name__,"regex_search",
                                    row))
                        # Try expection to handle an empty row.
                        try:
                            if re.search(regex_search_text,
                                                        row['Title'],
                                                        re.I) or re.search(
                                                        regex_search_text,
                                                        row['Date'],
                                                        re.I) or re.search(
                                                        regex_search_text,
                                                        row['Time'],
                                                        re.I) or re.search(
                                                        regex_search_text,
                                                        row['Notes'],
                                                        re.I):
                                regex_list.append({'Title' : row['Title'],
                                                    'Date' : row['Date'],
                                                    'Time' : row['Time'],
                                                    'Notes' : row['Notes']})
                                logging.debug("In function: {} {}, regex_list "
                                        "is: {}".format(
                                        SearchEntry.__name__,"regex_search",
                                        regex_list))
                        except KeyError:
                            self.clear_screen()
                            choice = input("Could not find any data on that entry:\n"
                                            "1) [T]ry again\n"
                                            "2) Return to the [S]earch menu\n"
                                            "3) Return to the [M]ain Menu\n"
                                            ":>")
                            self.clear_screen()
                            if choice == '1' or choice.upper() == 'T' or choice == '':
                                logging.debug("In function: {} {},\n\tTry "
                                            "again: {}".format(
                                            SearchEntry.__name__,"regex_search",
                                            "could not find"))
                                SearchEntry.regex_search(self)
                            elif choice == '2' or choice.upper() == 'S':
                                logging.debug("In function: {} {},\n\tSearch "
                                            "Menu: {}".format(
                                            SearchEntry.__name__,"regex_search",
                                            "could not find"))
                                SearchEntry.search_menu(self)
                            elif choice == '3' or choice.upper() == 'M':
                                logging.debug("In function: {} {},\n\tReturn to "
                                            "main menu: {}".format(
                                            SearchEntry.__name__,"regex_search",
                                            "could not find"))
                                self.main_menu()
                            # Catch all and return to main menu
                            else:
                                self.main_menu()
                        index, row = None, None
                from display_entry import DisplayEntry
                DisplayEntry.display_entries(self, regex_list)
                # When end of file is reached and no match found: choice.
                if index == None:
                    self.clear_screen()
                    choice = input("Could not find any data on that entry:\n"
                                    "1) [T]ry again\n"
                                    "2) Return to the [S]earch menu\n"
                                    "3) Return to the [M]ain Menu\n"
                                    ":>")
                    self.clear_screen()
                    if choice == '1' or choice.upper() == 'T' or choice == '':
                        logging.debug("In function: {} {},\n\tTry "
                                    "again: {}".format(
                                    SearchEntry.__name__,"regex_search",
                                    "could not find"))
                        SearchEntry.regex_search(self)
                    elif choice == '2' or choice.upper() == 'S':
                        logging.debug("In function: {} {},\n\tSearch "
                                    "Menu: {}".format(
                                    SearchEntry.__name__,"regex_search",
                                    "could not find"))
                        SearchEntry.search_menu(self)
                    elif choice == '3' or choice.upper() == 'M':
                        logging.debug("In function: {} {},\n\tReturn to main "
                                    "menu: {}".format(
                                    SearchEntry.__name__,"regex_search",
                                    "could not find"))
                        self.main_menu()
                    # Catch all and return to main menu
                    else:
                        self.main_menu()
                else:
                    nothing = input("Returning to Main Menu.")
                    self.main_menu()
        # Handles exception in case the file is missing.
        except FileNotFoundError:
            nothing = input("Could not find 'work_log.csv' please check to be "
                "sure it is present and in the correct directory.\n"
                "Returning to Main Menu. Hit enter to continue.")
            self.main_menu()
        
    def date_range_search(self):
        '''
        Takes a range of dates from the user and will pass the output of a search
            within that range for display.
        '''
        logging.debug("In function: {} {}".format(
                    SearchEntry.__name__,
                    "date_range_search"))
        date_range_list = []
        print("Please input your dates in the following format: MM/DD/YYYY")
        start_date = input("Enter the starting date for your date range search:"
                            "\n:>")
        end_date = input("Enter the ending date for your date range search:"
                            "\n:>")
        # Set the start and end date strings as datetime objects.
        start_actual_date = datetime.datetime.strptime(start_date,
                                                        self.date_format)
        end_actual_date = datetime.datetime.strptime(end_date,
                                                        self.date_format)
        # Creating a timedelta between the start and end date.
        td_range = end_actual_date - start_actual_date
        td_range_sec = td_range.total_seconds()
        if td_range_sec < 0:
            nothing = input("You cannot have a start date later than your end "
                            "date. Please try again.\n Hit enter to continue.")
            self.clear_screen()
            SearchEntry.date_range_search(self)
        logging.debug("In function: {} {},\n\ttd_range_sec: {}".format(
                        SearchEntry.__name__,"Date_range_search",
                        td_range_sec))
        # Bring in the data from the file and check if its in range of the dates
                # send the list of results for display.
        # Try exception to handle missing file.
        try:
            with open('work_log.csv', 'r', newline='') as csv_reader:
                log_reader = csv.DictReader(csv_reader)
                lr_enum = enumerate(log_reader, start=0)
                index, row = lr_enum.__next__()
                logging.debug("In function: {} {},\n\tlr_enum.next() tuple: {}, {}"
                            .format(SearchEntry.__name__,"Date_range_search",
                                        index, row))
                while row:
                    # Try exception to handle the end of enumeration
                    try:
                        logging.debug("\trow is: {}, row type is: {}".format(
                                        row, type(row)))
                        next_row = lr_enum.__next__()
                        row_date_actual = datetime.datetime.strptime(row['Date'],
                                                            self.date_format)
                        td_row = row_date_actual - start_actual_date # modified this
                        td_row_sec = td_row.total_seconds()
                        td_calc_range = td_range_sec - td_row_sec
                        logging.debug("In function: {} {},\n\ttd_range_sec: {}\n\t"
                                    "td_row_sec: {}\n\ttd_calc_range: {}\n\t"
                                    "Date is: {}".format(
                                    SearchEntry.__name__,"Date_range_search",
                                    td_range_sec,
                                    td_row_sec,
                                    td_calc_range,
                                    row['Date']))
                        # Try expection to handle an empty row.
                        try:
                            if td_calc_range >= 0 and td_calc_range <= td_range_sec:
                                date_range_list.append({'Title' : row['Title'],
                                                    'Date' : row['Date'],
                                                    'Time' : row['Time'],
                                                    'Notes' : row['Notes']})
                                logging.debug("In function: {} {},\n\t"
                                            "date_range_list: {}".format(
                                            SearchEntry.__name__,"date_range_search",
                                            date_range_list))
                            index, row = next_row
                            logging.debug("In function: {} {},\n\tlr_enum.next() "
                                "tuple: {}, {}".format(
                                SearchEntry.__name__,"Date_range_search",
                                index, row))
                        except KeyError:
                            self.clear_screen()
                            choice = input("Could not find any data on that entry:\n"
                                            "1) [T]ry again\n"
                                            "2) Return to the [S]earch menu\n"
                                            "3) Return to the [M]ain Menu\n"
                                            ":>")
                            self.clear_screen()
                            if choice == '1' or choice.upper() == 'T' or choice == '':
                                logging.debug("In function: {} {},\n\tTry "
                                            "again: {}".format(
                                            SearchEntry.__name__,
                                            "date_range_search",
                                            "could not find"))
                                SearchEntry.regex_search(self)
                            elif choice == '2' or choice.upper() == 'S':
                                logging.debug("In function: {} {},\n\tSearch "
                                            "Menu: {}".format(
                                            SearchEntry.__name__,
                                            "date_range_search",
                                            "could not find"))
                                SearchEntry.search_menu(self)
                            elif choice == '3' or choice.upper() == 'M':
                                logging.debug("In function: {} {},\n\tReturn to "
                                            "main menu: {}".format(
                                            SearchEntry.__name__,
                                            "date_range_search",
                                            "could not find"))
                                self.main_menu()
                            # Catch all and return to main menu
                            else:
                                self.main_menu()
                    except StopIteration:
                        # Catches the end of file.
                        logging.debug("In function: {} {},\n\tlr_enum.next() "
                            "tuple: {}, {}".format(
                            SearchEntry.__name__,"date_range_search",
                            "Date_range_search",
                             index, row))
                        # Prints the last row left in the itirator/generator when done.
                        logging.debug("In function: {} {},\n\tRaw row: "
                                    "{}\n".format(
                                    SearchEntry.__name__,"date_range_search",
                                     row))
                        # Setting the row date string to a datetime object.
                        row_date_actual = datetime.datetime.strptime(row['Date'],
                                                            self.date_format)
                        td_row = row_date_actual - start_actual_date # modified this
                        td_row_sec = td_row.total_seconds()
                        td_calc_range = td_range_sec - td_row_sec
                        logging.debug("In function: {} {},\n\ttd_range_sec: {}\n\t"
                                    "td_row_sec: {}\n\ttd_calc_range: {}\n\t"
                                    "Date is: {}".format(
                                    SearchEntry.__name__,"date_range_search",
                                    td_range_sec,
                                    td_row_sec,
                                    td_calc_range,
                                    row['Date']))
                        # Try expection to handle an empty row.
                        try:
                            if td_calc_range > 0 and td_calc_range <= td_range_sec:
                                date_range_list.append({'Title' : row['Title'],
                                                    'Date' : row['Date'],
                                                    'Time' : row['Time'],
                                                    'Notes' : row['Notes']})
                                logging.debug("In function: {} {},\n\t"
                                            "date_range_list: {}".format(
                                            SearchEntry.__name__,
                                            "date_range_search",
                                            date_range_list))
                        except KeyError:
                            self.clear_screen()
                            choice = input("Could not find any data on that entry:\n"
                                            "1) [T]ry again\n"
                                            "2) Return to the [S]earch menu\n"
                                            "3) Return to the [M]ain Menu\n"
                                            ":>")
                            self.clear_screen()
                            if choice == '1' or choice.upper() == 'T' or choice == '':
                                logging.debug("In function: {} {},\n\tTry again: "
                                            "{}".format(
                                            SearchEntry.__name__,
                                            "date_range_search",
                                            "could not find"))
                                SearchEntry.regex_search(self)
                            elif choice == '2' or choice.upper() == 'S':
                                logging.debug("In function: {} {},\n\tSearch "
                                            "Menu: {}".format(
                                            SearchEntry.__name__,
                                            "date_range_search",
                                            "could not find"))
                                SearchEntry.search_menu(self)
                            elif choice == '3' or choice.upper() == 'M':
                                logging.debug("In function: {} {},\n\tReturn to "
                                            "main menu: {}".format(
                                            SearchEntry.__name__,
                                            "date_range_search",
                                            "could not find"))
                                self.main_menu()
                            # Catch all and return to main menu
                            else:
                                self.main_menu()
                        index, row = None, None
                # Importing needed libs for needed fuctions here.
                from display_entry import DisplayEntry
                from operator import itemgetter
                # Sorting the date range list by the date.
                sorted_date_range = sorted(date_range_list, key=itemgetter('Date'))
                DisplayEntry.display_entries(self, sorted_date_range)
                # When end of file is reached and no match found: choice.
                if index == None:
                    self.clear_screen()
                    choice = input("Could not find any data on that entry:\n"
                                    "1) [T]ry again\n"
                                    "2) Return to the [S]earch menu\n"
                                    "3) Return to the [M]ain Menu\n"
                                    ":>")
                    self.clear_screen()
                    if choice == '1' or choice.upper() == 'T' or choice == '':
                        logging.debug("In function: {} {},\n\tTry again: "
                                    "{}".format(
                                    SearchEntry.__name__,
                                    "date_range_search",
                                    "could not find"))
                        SearchEntry.regex_search(self)
                    elif choice == '2' or choice.upper() == 'S':
                        logging.debug("In function: {} {},\n\tSearch "
                                    "Menu: {}".format(
                                    SearchEntry.__name__,
                                    "date_range_search",
                                    "could not find"))
                        SearchEntry.search_menu(self)
                    elif choice == '3' or choice.upper() == 'M':
                        logging.debug("In function: {} {},\n\tReturn to main "
                                    "menu: {}".format(
                                    SearchEntry.__name__,"date_range_search",
                                    "could not find"))
                        self.main_menu()
                    # Catch all and return to main menu
                    else:
                        self.main_menu()
                else:
                    nothing = input("Returning to Main Menu.")
                    self.main_menu()
        # Handles exception in case the file is missing.
        except FileNotFoundError:
            nothing = input("Could not find 'work_log.csv' please check to be "
                "sure it is present and in the correct directory.\n"
                "Returning to Main Menu. Hit enter to continue.")
            self.main_menu()
            
    def search_display_all(self):
        '''
        Reads through the .csv file and readies the data for display.
        '''
        logging.debug("In function: {} {},".format(SearchEntry.__name__,
                    "search_display_all"))
        display_all_list = []
        self.clear_screen()
        # Open file and run through all entries.
        # Try exception to handle missing file.
        try:
            with open('work_log.csv', 'r', newline='') as csv_reader:
                log_reader = csv.DictReader(csv_reader)
                lr_enum = enumerate(log_reader, start=1)
                index, row = lr_enum.__next__()
                logging.debug("In function: {} {},\n\tlr_enum.next() "
                            "tuple: {}, {}".format(
                            SearchEntry.__name__,"search_display_all",
                            index, row))
                while row:
                    # Try exception to handle the end of enumeration
                    try:
                        next_row = lr_enum.__next__()
                        # Try expection to handle an empty row.
                        try:
                            if row['Title']:
                                display_all_list.append({'Title' : row['Title'],
                                                'Date' : row['Date'],
                                                'Time' : row['Time'],
                                                'Notes' : row['Notes']})
                        except KeyError:
                            self.clear_screen()
                            choice = input("Could not display entries:\n"
                                            "1) [T]ry again\n"
                                            "2) Return to the [S]earch menu\n"
                                            "3) Return to the [M]ain Menu\n"
                                            ":>")
                            if choice == '1' or choice.upper() == 'T' or choice == '':
                                logging.debug("In function: {} {},\n\tTry "
                                            "again: {}".format(
                                            SearchEntry.__name__,
                                            "search_display_all",
                                            "could not find"))
                                SearchEntry.search_display_all(self)
                            elif choice == '2' or choice.upper() == 'S':
                                logging.debug("In function: {} {},\n\tSearch "
                                            "Menu: {}".format(
                                            SearchEntry.__name__,
                                            "search_display_all",
                                            "could not find"))
                                SearchEntry.search_menu(self)
                            elif choice == '3' or choice.upper() == 'M':
                                logging.debug("In function: {} {},\n\tReturn to "
                                            "main menu: {}".format(
                                            SearchEntry.__name__,
                                            "search_display_all",
                                            "could not find"))
                                self.main_menu()
                            # Catch all and return to main menu
                            else:
                                nothing = input("Hit enter to continue to the main menu.")
                                self.main_menu()
                        index, row = next_row
                        logging.debug("In function: {} {},\n\tlr_enum.next() "
                                    "tuple: {}, {}".format(
                                    SearchEntry.__name__,"search_display_all",
                                    index, row))
                    except StopIteration:
                        # Catches the end of file.
                        logging.debug("In function: {} {},\n\tlr_enum.next() "
                            "tuple: {}, {}".format(
                                    SearchEntry.__name__,"search_display_all",
                                    index, row))
                        # Prints the last row left in the itirator/generator when done.
                        logging.debug("In function: {} {},\n\tRaw row: "
                                    "{}\n".format(
                                    SearchEntry.__name__,"search_display_all",
                                    row))
                        # Try expection to handle an empty row.
                        try:
                            if row['Title']:
                                display_all_list.append({'Title' : row['Title'],
                                                'Date' : row['Date'],
                                                'Time' : row['Time'],
                                                'Notes' : row['Notes']})
                        except KeyError:
                            self.clear_screen()
                            choice = input("Could not display entries:\n"
                                            "1) [T]ry again\n"
                                            "2) Return to the [S]earch menu\n"
                                            "3) Return to the [M]ain Menu\n"
                                            ":>")
                            if choice == '1' or choice.upper() == 'T' or choice == '':
                                logging.debug("In function: {} {},\n\tTry "
                                            "again: {}".format(
                                            SearchEntry.__name__,
                                            "search_display_all",
                                            "could not find"))
                                SearchEntry.search_display_all(self)
                            elif choice == '2' or choice.upper() == 'S':
                                logging.debug("In function: {} {},\n\tSearch "
                                            "Menu: {}".format(
                                            SearchEntry.__name__,
                                            "search_display_all",
                                            "could not find"))
                                SearchEntry.search_menu(self)
                            elif choice == '3' or choice.upper() == 'M':
                                logging.debug("In function: {} {},\n\tReturn to "
                                            "main menu: {}".format(
                                            SearchEntry.__name__,
                                            "search_display_all",
                                            "could not find"))
                                self.main_menu()
                            # Catch all and return to main menu
                            else:                            
                                nothing = input("Hit enter to continue to the main menu.")
                                self.main_menu()
                        index, row = None, None
                from display_entry import DisplayEntry
                DisplayEntry.display_entries(self, display_all_list)
                # When end of file is reached and no match found: choice.
                if index == None:
                    self.clear_screen()
                    choice = input("Could not display entries:\n"
                                    "1) [T]ry again\n"
                                    "2) Return to the [S]earch menu\n"
                                    "3) Return to the [M]ain Menu\n"
                                    "Note: Title must match exactly.\n"
                                    ":>")
                    if choice == '1' or choice.upper() == 'T' or choice == '':
                        logging.debug("In function: {} {},\n\tTry "
                                    "again: {}".format(
                                    SearchEntry.__name__,"search_display_all",
                                    "could not find"))
                        SearchEntry.search_display_all(self)
                    elif choice == '2' or choice.upper() == 'S':
                        logging.debug("In function: {} {},\n\tSearch "
                                    "Menu: {}".format(
                                    SearchEntry.__name__,"search_display_all",
                                    "could not find"))
                        SearchEntry.search_menu(self)
                    elif choice == '3' or choice.upper() == 'M':
                        logging.debug("In function: {} {},\n\tReturn to main "
                                    "menu: {}".format(
                                    SearchEntry.__name__,"search_display_all",
                                    "could not find"))
                        self.main_menu()
                    # Catch all and return to main menu
                    else:
                        self.main_menu()
        # Handles exception in case the file is missing.
        except FileNotFoundError:
            nothing = input("Could not find 'work_log.csv' please check to be "
                "sure it is present and in the correct directory.\n"
                "Returning to Main Menu. Hit enter to continue.")
            self.main_menu()
