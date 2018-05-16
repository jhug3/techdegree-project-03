# display_entry.py created by John Hughes on 4/10/18

import logging, csv

from worklog import WorkLog


class DisplayEntry(WorkLog):
    '''
    Class Name: DisplayEntry
    Class Type: Child of WorkLog
    Displays the results of any searches.
    '''
    def __init__(self):
        '''
        Enables the logger if self.loggin_bool is set to True.
        '''
        if self.logging_bool:
            logging.basicConfig(filename='work_log.log', 
                    filemode = 'a', 
                    level = logging.DEBUG
                    )
        logging.bebug("In function: {} {}".format(DisplayEntry.__name__,
                        "__init__"))
    
    def display_entry(self):
        '''
        Displays the entry from the atribues.
        '''
        logging.debug("In function: {} {},".format(DisplayEntry.__name__,
                        "display_entry"))
        self.clear_screen()
        print("Your task entry:\n\n"
                "_________________________________________\n"
                "Title: {}\n"
                "Date: {}\n"
                "Time: {}\n"
                "Note: {}\n"
                "_________________________________________\n"
                .format(self.task_title,
                        self.task_date,
                        self.task_time,
                        self.task_notes))
        logging.debug("In function: {} {}\n\t"
                            "Variables for display:\n"
                            "\tTitle: {}\n\t"
                            "\tDate: {}\n\t"
                            "\tTime: {}\n\t"
                            "\tNotes: {}\n".format(
                            DisplayEntry.__name__,"display_entry",
                            self.task_title,
                            self.task_date,
                            self.task_time,
                            self.task_notes))
                            
    def entry_data(self, search_list, list_index):
        '''
        Inputs data to class attribues, only called from display_entries.
        '''
        logging.debug("In fuction: {} {}".format(DisplayEntry.__name__,
                        "entry_data"))
        logging.debug("In fuction: {} {}\n\tsearch_list: {} \n\t"
                        "list_index: {}".format(
                        DisplayEntry.__name__,"entry_data",
                        search_list, list_index))
        try:
            dict_entry = search_list[list_index]
            for key, value in dict_entry.items():
                if key == 'Title':
                    self.task_title = value
                    logging.debug("In function: {} {}\n\tin if statement: Title,"
                                    "key: {} value: {} Class var: {}".format(
                                    DisplayEntry.__name__,"entry_data", 
                                    key,
                                    value,
                                    self.task_title))
                if key == 'Date':
                    self.task_date = value
                    logging.debug("In function: {} {}tin if statement: Date,"
                                    "key: {} value: {} Class var: {}".format(
                                    DisplayEntry.__name__,"entry_data",  
                                    key,
                                    value,
                                    self.task_date))
                if key == 'Time':
                    self.task_time = value
                    logging.debug("In function: {} {} \n\tin if statement: Time,"
                                    "key: {} value: {} Class var: {}".format(
                                    DisplayEntry.__name__,"entry_data",  
                                    key,
                                    value,
                                    self.task_time))
                if key == 'Notes':
                    self.task_notes = value
                    logging.debug("In function: {} {}\n\tin if statement: Notes,"
                                    "key: {} value: {} Class var: {}".format(
                                    DisplayEntry.__name__,"entry_data",  
                                    key,
                                    value,
                                    self.task_notes))
        except IndexError:
            self.clear_screen()
            nothing = input("You have reached the end of your search. "
                            "Returning to the Main Menu.")
            self.main_menu()
        
    def display_entries(self, search_list):
        '''
        Displays entries from the passed in list.
        '''
        logging.debug("In function: {} {}".format(DisplayEntry.__name__,
                        "display_entries"))
        logging.debug("In function: {} {},\n\tSearch_dict: {}".format(
                        DisplayEntry.__name__,"display_entries",
                        search_list))
        list_index = 0
        logging.debug("In fuction: {} {},\n\tfirst call, call to DisplayEntry.entry_data, "
                            "search_list: {}, list_index: {}".format(
                            DisplayEntry.__name__,"display_entries",
                            search_list, list_index))
        # Call entry_data to put data into the class atribues from the list.
        DisplayEntry.entry_data(self, search_list, list_index)
        # Get user input choice while index is less than the list len.
        while list_index < len(search_list):
            DisplayEntry.display_entry(self)        
            choice = input("Hit Enter to go to the [N]ext entry\n"
                            "Go [B]ack to the previous entry\n"
                            "[E]dit your entry\n"
                            "[D]elete your entry\n:>")
            if choice.upper() == 'N' or choice == '':
                logging.debug("In fuction: {} {},\n\tcall to DisplayEntry.entry_data, "
                                "search_list: {}, list_index: {}".format(
                                DisplayEntry.__name__,"display_entries",
                                search_list, list_index))
                # Call entry_data to put data into the class atribues from the list.
                
                list_index += 1
                DisplayEntry.entry_data(self, search_list, list_index)
            elif choice.upper() == 'B':
                list_index -= 1
                if list_index < 0:
                    list_index = 0
                    nothing = input("Cannot go back any further. Displaying last "
                                    "entry. Hit entry to continu.")
                logging.debug("In fuction: {} {},\n\tcall to DisplayEntry.entry_data, "
                                "search_list: {}, list_index: {}".format(
                                DisplayEntry.__name__,"display_entries",
                                search_list, list_index))
                # Call entry_data to put data into the class atribues from the list.
                DisplayEntry.entry_data(self, search_list, list_index)
            elif choice.upper() == 'E':
                logging.debug("In fuction: {} {},\n\tcall to "
                                "DisplayEntry.edit_entry".format(
                                DisplayEntry.__name__,"display_entries"))
                DisplayEntry.edit_entry(self)
            elif choice.upper() == 'D':
                logging.debug("In fuction: {} {},\n\tcall to "
                                "DisplayEntry.delete_entry".format(
                                DisplayEntry.__name__,"display_entries"))
                DisplayEntry.delete_entry(self)
                print("Your file has been deleted\n")
                nothing = input("File Saved successfully!\nHit "
                                "enter to continue to Main Menu.")
                self.main_menu()
            else:
                nothing = ("Input not recognized. Returning to Main Menu.")
                self.main_menu()

    def delete_entry(self, delete=True):
        '''
        Deletes the entry the user has chossen. Note: this method of deleting
            would not be best for very large files.
        '''
        logging.debug("In function: {} {}".format(DisplayEntry.__name__,
                                                    "delete_entry"))
        self.clear_screen()
        DisplayEntry.display_entry(self)
        # Displays a warning if delete is True, used when deleting an entry.
        if delete:
            print("WARNING!! You cannot undo this delete.\n"
                "Are you sure you wish to continue?\n")
            choice = input("Y/N\n:>")
        # Sets to 'Y', used for when editing an entry.
        else:
            choice = 'Y'
        if choice.upper() == 'Y' or choice == '':
            file_list = DisplayEntry.get_file(self)
            logging.debug("In function: {} {},\n\tfile_list: {}".format(
                        DisplayEntry.__name__,
                        "delete_entry",
                        file_list))
            index = 0
            truth_value = 0
            for entry in file_list:
                logging.debug("In function: {} {}\n\t"
                                        "file_list: {}\n\t"
                                        "entry: {}".format(
                                        DisplayEntry.__name__,
                                        "delete_entry",
                                        file_list,
                                        entry))
                for key, value in entry.items():
                    if key == 'Title':
                        if value == self.task_title:
                            truth_value += 1
                            logging.debug("In function: {} {}\n\t"
                                        "Key: {}\n\t"
                                        "Value: {}\n\t"
                                        "self.task_tile: {}\n\t"
                                        "truth_value: {}".format(
                                        DisplayEntry.__name__,
                                        "delete_entry",
                                        key,
                                        value,
                                        self.task_title,
                                        truth_value))
                            logging.debug("\tTitle Key: {}\n"
                                            "\tTruth_value: {}".format(
                                            value, truth_value))
                    # Making sure all the values of the entry match the enty to
                        # be deleted.
                    if key == 'Date':
                        if value == self.task_date:
                            truth_value += 1
                            logging.debug("\tDate Key: {}\n"
                                            "\tTruth_value: {}".format(
                                            value, truth_value))
                    if key == 'Time':
                        if value == self.task_time:
                            truth_value += 1
                            logging.debug("\tTime Key: {}\n"
                                            "\tTruth_value: {}".format(
                                            value, truth_value))
                    if key == 'Notes':
                        if value == self.task_notes:
                            truth_value += 1
                            logging.debug("\tNotes Key: {}\n"
                                            "\tTruth_value: {}".format(
                                            value, truth_value))
                    if truth_value == 4:
                        logging.debug("\t Total truth_value: {}".format(
                                        truth_value))
                        del file_list[index]
                        # Copying file_list after editing it, so there are no
                            # issues with list errors.
                        new_file_list = file_list[:]
                        try:
                            # Writing new list with entry deleted to the file,
                                # overwriting the data in the file.
                            with open('work_log.csv', 'w') as log_writer:
                                # Header for the CSV, reason for no spaces.
                                log_writer.write("Title,Date,Time,Notes\n")
                                for entry in new_file_list:
                                    for key, value in entry.items():
                                        if key == 'Title':
                                            self.task_title = value
                                        if key == 'Date':
                                            self.task_date = value
                                        if key == 'Time':
                                            self.task_time = value
                                        if key == 'Notes':
                                            self.task_notes = value
                                    line = (self.task_title + ',' + 
                                            self.task_date + ',' +
                                            self.task_time + ',' + 
                                            self.task_notes + '\n')
                                    log_writer.write(line)
                            return
                        except PermissionError:
                            self.clear_screen()
                            logging.warning("In fuction: {} {}, File Permission "
                                            "Error [Errno 13] Permission denied: " "'work_log.csv' file may be open,"
                                            " or cannot find file.".format(
                                            DisplayEntry.__name__,
                                            "display_entries"))
                            nothing = input("Warning!\nThere was an problem "
                                            "writing to the file.\nPlease check "
                                            "the file and be sure it\nis not"
                                            " open and that it is in the "
                                            "correct direcotry.\nHit Enter to "
                                            "return to the Main menu.\n:>")
                            self.main_menu()
                index += 1
                truth_value = 0
        else:
            self.main_menu()
    
    def edit_entry(self):
        '''
        Deletes entry, then edits entry, then will write users edit back to the
            file.
        '''
        logging.debug("In function: {} {}".format(DisplayEntry.__name__,
                        "edit_entry"))
        # Holding the original entry for later.
        temp_title = self.task_title
        temp_date = self.task_date
        temp_time = self.task_time
        temp_notes = self.task_notes
        # Deleting entry from file.
        DisplayEntry.delete_entry(self, False)
        # Putting entry back into class attribues.
        self.task_title = temp_title
        self.task_date = temp_date
        self.task_time = temp_time
        self.task_notes = temp_notes
        # Calling edit functions from add entry.
        from add_entry import AddEntry
        AddEntry.edit_entry(self)
        
    def get_file(self):
        '''
        Reads the .csv file and puts the contents into a list so it can be
        manipulated.
        '''
        file_list = []
        logging.debug("In function: {} {}".format(
                            DisplayEntry.__name__,"get_file"))
        try:
            with open('work_log.csv', 'r', newline='') as csv_reader:
                log_reader = csv.DictReader(csv_reader)
                lr_enum = enumerate(log_reader, start=0)
                index, row = lr_enum.__next__()
                logging.debug("In function: {} {},\n\tlr_enum.next() tuple: {}, {}"
                            .format(DisplayEntry.__name__,"get_file",
                            index, row))
                while row:
                    try:
                        logging.debug("\trow is: {}, row type is: {}".format(
                                        row, type(row)))
                        next_row = lr_enum.__next__()
                        if row:
                            file_list.append({'Title' : row['Title'],
                                                'Date' : row['Date'],
                                                'Time' : row['Time'],
                                                'Notes' : row['Notes']})
                            logging.debug("In function: {} {},\n\tfile_list is: {}"
                                        .format(DisplayEntry.__name__,"get_file",
                                        file_list))
                        index, row = next_row
                        logging.debug("In function: {} {},\n\tlr_enum.next() "
                                    "tuple: {}, {}".format(
                                    DisplayEntry.__name__,"get_file",
                                    index, row))
                    except StopIteration:
                        # Catches the end of file.
                        logging.debug("In function: {} {},\n\tlr_enum.next() "
                                    "tuple: {}, {}".format(
                                    DisplayEntry.__name__,"get_file",
                                    index, row))
                        # Prints the last row left in the itirator/generator when done.
                        logging.debug("In function: {} {},\n\tRaw row: {}\n".format(
                                    DisplayEntry.__name__,"get_file",row))
                        if row:
                            file_list.append({'Title' : row['Title'],
                                                'Date' : row['Date'],
                                                'Time' : row['Time'],
                                                'Notes' : row['Notes']})
                            logging.debug("In function: {} {},\n\tfile_list is: {}"
                                        .format(DisplayEntry.__name__,"get_file",
                                        file_list))
                        index, row = None, None
                        return file_list
        # Handles exception in case the file is missing.
        except FileNotFoundError:
            nothing = input("Could not find 'work_log.csv' please check to be "
                "sure it is present and in the correct directory.\n"
                "Returning to Main Menu. Hit enter to continue.")
            self.main_menu()
