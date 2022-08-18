# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# dejam,220816,Modified code to complete assignment 06
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
#import libraries and modules
from os.path import exists

# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection

# Processing  --------------------------------------------------------------- #
class Processor():
    """Performs Processing tasks"""
    
    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ 
        Reads data from a file into a list of dictionary rows
        
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        
        #check if file exists
        file_exists = exists(file_name)
        
        #if file exists, load data
        if(file_exists == True):
            list_of_rows.clear()  #clear current data
            file = open(file_name, "r")
            for line in file:
                task, priority = line.split(",")
                row = {"Task": task.strip(), "Priority": priority.strip()}
                list_of_rows.append(row)
            file.close()
            print("Data loaded from file!")
            return list_of_rows
        
        #if file does not exist, alert user and return to main menu
        else:
            print("No data to load from file!")  
            
    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ 
        Adds data to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        
        #add user input items to dictionary row
        row = {"Task": str(task).strip(), "Priority": str(priority).strip()}
        
        #add dictionary row to python list/table
        list_of_rows.append(row)

        return list_of_rows

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ 
        Removes data from a list of dictionary rows
        
        :param task: (string) with name of task:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        
        #cycle through entries in list_of_rows until the user input item 
        #matches an item in the list of dictionary rows
        list_of_rows_position = 0
        for row in list_of_rows:
            #if user input item is found on the to-do list, it is removed from the to-do list
            if(row["Task"].lower() == task.lower()):   
                #removes user input item from list
                del list_of_rows[list_of_rows_position]

                #alert user the item was removed from the list and return to main menu
                print(task + " has been removed from the to-do list.")
                break

            #if the list has been cycled through, and the user input item is not 
            #the last item on the list: alert user the item was not found and return to main menu
            if(str(list_of_rows_position) == str(len(list_of_rows)-1) and row["Task"].lower() != task.lower()):
                print(task + " was not found on the to-do list!")
                break

            #if user input item has not been found, but there are more items on the list,
            #then continue to cycle through the list
            else:
                list_of_rows_position = list_of_rows_position+1 
        
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """
        Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        
        #ToDoFile.txt is identified as file_obj
        file_obj = open(file_name_str, "w")
        
        #write user input to-do items to ToDoFile.txt
        for row in list_of_rows:
            file_obj.write(row["Task"] + "," + row["Priority"] + "\n")
        
        #ToDoFile.txt is closed
        file_obj.close()
        
        #user is alerted that their data has successfully been saved
        print("Data has been saved!")
        
        return list_of_rows

# Presentation (Input/Output)  -------------------------------------------- #
class IO():
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  
        Display a menu of choices to the user
        
        :return: nothing
        """
        
        print("""
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Exit Program
        """)
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ 
        Gets the menu choice from a user
        
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4]: ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ 
        Shows the current Tasks in the list of dictionaries rows
        
        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        
        print("Here is your current to-do list: ")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print()  # Add an extra line for looks
    
    @staticmethod
    def input_new_task_and_priority():
        """  
        Gets task and priority values to be added to the list
        
        return: (string, string) with task and priority
        """
    
        #task: (string) with name of task:
        task = input("Enter a Task for the to-do list: ")
        
        #priority: (string) with name of priority:
        priority = input("Enter the Priority of this Task: ")
        
        #return user input task and priority
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """  
        Gets the task name to be removed from the list
        
        :return: (string) with task
        """
        
        #identify item to remove from to-do list
        str_task_remove = input("Which task do you want to remove from the to-do list? ")
        
        return str_task_remove

### Main Body of Script  ------------------------------------------------------ #
"""Step 1: When the program starts, load data from ToDoFile.txt"""
Processor.read_data_from_file(file_name=file_name_str, list_of_rows=table_lst)  # read data from file

"""Step 2: Display a menu of choices to the user"""
while (True):
    """Step 3: show current data"""
    #shows current data in the to-do list if there are items in the to-do list
    if(table_lst != []):
        IO.output_current_tasks_in_list(list_of_rows=table_lst)
        
    #shows main menu to user, returns user's choice from main menu
    IO.output_menu_tasks()
    choice_str = IO.input_menu_choice()
    
    """Step 4: Process user's menu choice"""
    #add a new Task to the to-do list
    if(choice_str.strip() == '1'):
        task, priority = IO.input_new_task_and_priority()
        table_lst = Processor.add_data_to_list(task=task, priority=priority, list_of_rows=table_lst)
        continue #return to main menu
        
    #remove an existing Task from the to-do list
    elif(choice_str == '2'):
        #if the to-do list is empty, alert the user and return to main menu
        if(table_lst == []):
            print("There are no tasks on the to-do list! Please choose a different option:")
        
        #if there are tasks on the to-do list, allow the user to remove a task from the to-do list
        else:
            task = IO.input_task_to_remove()
            table_lst = Processor.remove_data_from_list(task=task, list_of_rows=table_lst)
        continue #return to main menu
     
    #save data to file
    elif(choice_str == '3'):
        table_lst = Processor.write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)
        continue #return to main menu
     
    #exit script
    elif(choice_str == '4'):
        print("Goodbye!")
        break #break loop to exit script