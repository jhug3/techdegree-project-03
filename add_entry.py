# add_entry.py created by John Hughes on 4/9/18

import logging, datetime

from worklog import WorkLog
from menus import Menu
                    
class AddEntry(WorkLog):
    '''
    Class Name: AddEntry
    Class Type: Child of WorkLog
    Adds a time log entry and creats all the relevent menus and ueser input and
    out put needed.
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
        logging.debug("In function: {} {}".format(AddEntry.__name__,
                        "__init__"))
        
    def entry_title(self):
            '''
            Menu choices for a new entry.
            '''
            logging.debug("In function: {} {}".format(AddEntry.__name__,
                            "entry_title"))
            # Getting the title of the task
            self.clear_screen()
            self.user_title = input(
                            "Enter a title/name you wish to give to this task:\n"
                            ":>")
            # This makes the first letter in each word a capital, like a title.
            self.user_title = self.user_title.title()
            logging.debug("In function: {} {},\n\ttask title, user "
                            "input: {}".format(
                            AddEntry.__name__,"entry_title",
                            self.user_title))
            if self.user_title == '':
                nothing = input("That is not a valid Title, please try again.")
                AddEntry.entry_title(self)
            self.task_title = self.user_title
            # Moving on to the next setp: entry_date()
            AddEntry.entry_date(self)
            
    def entry_date(self):
        '''
        Getting the date of the task
        '''
        logging.debug("In function: {} {}".format(AddEntry.__name__,"entry_date"))
        today = datetime.datetime.today()
        self.clear_screen()
        print("Enter the date of the task:\n")
        self.user_date = input(
                            "Please use the following format: MM/DD/YYYY:\n"
                            "Note: hit enter to use today's date!\n"
                            ":>")
        logging.debug("In function: {} {},\n\tdate input: {}".format(
                    AddEntry.__name__,"entry_date",
                    self.user_date,))
        # Entering todays date if user hits enter, empty string.
        if self.user_date == '':
            # Setting the user input attribute to todays date.
            self.user_date = '{0:%m/%d/%Y}'.format(today)
            logging.debug("In function: {} {},\n\tdefault date input formated:"
                        "{}".format(
                        AddEntry.__name__,"entry_date",
                        self.user_date))
        # Checking for a valid date entry:
        try:
            self.task_date = datetime.datetime.strptime(
                        self.user_date, self.date_format)
            logging.debug("In function: {} {},\n\ttry block: {}".format(
                            AddEntry.__name__,"entry_date",
                            self.task_date))
        except ValueError:
            nothing = input("That was not a valid date. Please try again.")
            logging.debug("In function: {} {},\n\texception: ValueError, Not a "
                            "valid date. Please try again.".format(
                            AddEntry.__name__,"entry_date"))
            AddEntry.entry_date(self)
        # Checking to be sure the entered date is not in the future.
        td = self.task_date - today
        logging.debug("In function: {} {},\n\ttd is: {}".format(
                    AddEntry.__name__,"entry_date",
                    td))
        if td.total_seconds() >= 0:
            logging.debug("In function: {} {},\n\ttimedelta is greater "
                            "than or = zero this entry is in the "
                            "future.".format(
                            AddEntry.__name__,"entry_date"))
            nothing = input("Invalid entry, this date is in the future!\n"
                            "Unless you have a TARDIS there is no way you can "
                            "do work in the future.\n"
                            "Please enter a valid date, try again.\n")
            AddEntry.entry_date(self)
        # Setting the format to a str.
        self.task_date = self.task_date.strftime(self.date_format)
        # Moving on to the next step: entry_time()
        AddEntry.entry_time(self)
        
    def entry_time(self):
        '''
        Getting the time spent on the task
        '''
        logging.debug("In function {} {}".format(AddEntry.__name__,"entry_time"))
        self.clear_screen()
        # ** May want diffrent formats for diffrent amounts of time.
        # example ww/dd/hh/mm or dd/hh/mm or hh/mm or mm for now just go with mm
        print("Time spent on task:\n")
        self.user_time = input(
                    "Please use the following formats:\n"
                    " _____________________________________\n"
                    "|MM     |For minutes                  |\n"
                    "|HH:MM  |For hours(24) and minutes    |\n"
                    "|_____________________________________|\n"
                    ":>")
        logging.debug("In function: {} {},\n\ttime input: {}".format(
                    AddEntry.__name__,"entry_time",
                    self.user_time))
        # Checking for minute only input:
        if len(self.user_time) == 2:
            # Checking for out of bound input on minues.
            try:
                self.task_time = datetime.datetime.strptime(self.user_time, '%M')
                logging.debug("In function: {} {},\n\ttime input: {}, "
                        "task_time is: {}".format(
                        AddEntry.__name__,"entry_time",
                        self.user_time,
                        self.task_time))
            except ValueError:
                nothing = input("Not a valid time entry. Please try again.")
                AddEntry.entry_time(self)
            else:
                # Converting to a str for formating.
                self.task_time = self.task_time.strftime('%H:%M')
        # Checking for hour and minute input:
        elif len(self.user_time) == 5:
            # Checking of out of bound hour or minute input.
            try:
                self.task_time = datetime.datetime.strptime(
                                                    self.user_time, '%H:%M')
                logging.debug("In function: {} {},\n\ttime input: {}, "
                        "task_time is: {}".format(
                        AddEntry.__name__,"entry_time",
                        self.user_time,
                        self.task_time))
            except ValueError:
                nothing = input("Not a valid time entry. Please try again.")
                AddEntry.entry_time(self)
            else:
                # Converting to a str for formating.
                self.task_time = self.task_time.strftime('%H:%M')
        # If user does not input anything valid this catches it.
        else:
            nothing = input("Not valid input. Please try again.\n")
            AddEntry.entry_time(self)
        # Moving on to the next step: entry_note()            
        AddEntry.entry_note(self)
              
    def entry_note(self):
        '''
        Getting the optional note for the task
        '''
        logging.debug("In function: {} {}".format(AddEntry.__name__,
                        "entry_notes"))
        self.clear_screen()
        print("Enter a note for the task.\n"
                "Note: (this is optional) hit enter to skip.")
        self.user_notes = input(":>")
        logging.debug("In function: {} {},\n\ttask notes, user input: {}".format(
                        AddEntry.__name__,"entry_notes",
                        self.user_notes))
        task_note_split = self.user_notes.split()
        logging.debug("In function: {} {},\n\ttask notes: {} task note "
                "split: {}".format(
                AddEntry.__name__,"entry_notes", 
                self.user_notes,
                 task_note_split))
        # Handeling the exeption for when the string is blank.
        try:
            task_note_split_title = task_note_split[0]
        except IndexError:
            logging.warning("In function: {} {},\n\ttry block: handeled "
                            "exception: IndexError for a default entry of "
                            "zero len string.".format(
                            AddEntry.__name__,"entry_notes"))
        # Handeling the exeption for when the string is blank.
        try:
            task_note_split[0] = task_note_split_title.title()
        except UnboundLocalError:
            logging.warning("In function: {} {},\n\ttry block: handeled exception:"
                            "UnboundLocalError for a default entry of zero len "
                            "string.".format(
                            AddEntry.__name__,"entry_notes"))
        logging.debug("In function: {} {}\n\ttask notes: {}\n\ttask note "
                "split,title: {}".format(
                AddEntry.__name__,"entry_notes", 
                self.user_notes,
                 task_note_split))
        self.task_notes = ' '.join(task_note_split)
        # Move to next step: entry_review()
        AddEntry.entry_review(self)
        
    def entry_review(self):
        '''
        Show users the entry and allows them to edit the entry before 
        returning to main menu. 
        '''
        logging.debug("In function: {}".format(AddEntry.__name__,"entry_review"))
        # Allowing user to skip this part.
        self.clear_screen()
        print("Review your entry? Y/N:")
        choice = input(":>")
        if choice.upper() == 'Y':
            self.clear_screen()
            print("Your task entry:\n\n"
                    "_________________________________________\n"
                    "Title: {}\n"
                    "Date: {}\n"
                    "Time: {}\n"
                    "Note: {}\n"
                    "_________________________________________\n"
                    .format(
                            self.task_title,
                            self.task_date,
                            self.task_time,
                            self.task_notes))
            logging.debug("In function: {} {},\n\tReview is:\n\t"
                            "Title: {},\n\t"
                            "Date: {},\n\t"
                            "Time: {},\n\t"
                            "Note: {},\n".format(
                            AddEntry.__name__,"entry_review",
                            self.task_title,
                            self.task_date,
                            self.task_time,
                            self.task_notes))
            AddEntry.edit_entry(self)
        else:
            AddEntry.write_file(self)
                            
    def edit_entry(self):
        '''
        Allowing user to edit their entry.
        '''
        logging.debug("In function: {} {}".format(AddEntry.__name__,
                        "entry_entry"))
        choice = input("Do you wish to edit your entry?\n"
                    "You may start at: [T]itle, [D]ate, Ti[m]e, or [N]ote.\n\n"
                    "You can [S]kip saving your entry and return to the"
                    " main menu.\n\tNOTE:\n\tIf you are editing a saved entry and "
                    "skip\n\tit this is the same as deleting it.\n"
                    "Hit enter to save your data and go to the main menu."
                    "\n:>"
                    )
        if choice.upper() == 'T':
            logging.debug("In function: {} {},\n\tUser chose to edit {}"
                            .format(AddEntry.__name__,"entry_entry",
                            "Title"))
            AddEntry.entry_title(self)
        elif choice.upper() == 'D':
            logging.debug("In function: {} {},\n\tUser chose to edit {}"
                            .format(AddEntry.__name__,"entry_entry",
                            "Date"))
            AddEntry.entry_date(self)
        elif choice.upper() == 'M':
            logging.debug("In function: {} {},\n\tUser chose to edit {}"
                            .format(AddEntry.__name__,"entry_entry",
                            "Time"))
            AddEntry.entry_time(self)
        elif choice.upper() == 'N':
            logging.debug("In function: {} {},\n\tUser chose to edit {}"
                            .format(AddEntry.__name__,"entry_entry",
                            "Notes"))
            AddEntry.entry_note(self)
        elif choice.upper() == 'S':
            logging.debug("In function: {} {},\n\tUser chose {}"
                            .format(AddEntry.__name__,"entry_entry",
                            "not to save"))
            self.main_menu()
        elif choice == '':
            logging.debug("In function: {} {},\n\tUser chose {}"
                            .format(AddEntry.__name__,"entry_entry",
                            "to save."))
            AddEntry.write_file(self)
        # input error handeling.
        else:
            nothing = input("That was not a recognized input,"
                            "please try again.\n:>")
            AddEntry.entry_review(self)
        # Moving to next step add_entry() 
        AddEntry.write_file(self)
        
    def write_file(self):
        '''
        Writes the dict style entry to the .csv file.
        '''
        logging.debug("In fuction: {} {}".format(
                        AddEntry.__name__,"write_file"))
        try:
            with open('work_log.csv', 'a') as log_writer:
                line = (self.task_title + ',' + 
                        self.task_date + ',' +
                        self.task_time + ',' + 
                        self.task_notes + '\n')
                log_writer.write(line)
        except PermissionError:
            self.clear_screen()
            logging.warning("In fuction: {} {},\n\tFile Permission Error [Errno 13]"
                            "Permission denied: 'work_log.csv' file may be open,"
                            "or cannot find file.".format(
                            AddEntry.__name__,"write_file"))
            nothing = input("Warning!\nThere was an problem writing to the file."
                            "\nPlease check the file and be sure it\nis not"
                            " open and that it is in the correct direcotry.\n"
                            "Hit Enter to return to the Main menu.\n:>")
            self.main_menu()
        # Moveing back to the main menu
        nothing = input("File saved successfully. Hit enter to continue to the "
                        "main menu.")
        self.main_menu()
