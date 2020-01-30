from modules import pylavor
import logging
from simple_term_menu import TerminalMenu


logging.basicConfig(level=logging.DEBUG)  #filename='upTimer.log',level=logging.INFO, filemode='w')

def check_for_files():
    logging.debug(f"Checking if all needed files are present.")
    proceed = False

    main_db = pylavor.check_file_exists("data/databases/all_places.json")
    if main_db == False:
        logging.debug(f"The main places database was not found, creating one.")
        pylavor.json_write("data/databases", "all_places.json", {})
        logging.debug(f"Database created.")
    
    if main_db == True:
        proceed = True
        logging.info(f"All files were located, the program can proceed.")

    else:
        proceed = False
        logging.info(f"Not all files were found, starting the program in create mode.")

    return proceed

def main_menu():
    terminal_menu = TerminalMenu(["Insert Location", "Browse Mode", "Alter Mode", "Itinerary Mode", "Help", "Exit"], title="What would you like to do?")
    #print(terminal_menu.show())
    return terminal_menu.show()

def get_rating():
    terminal_menu = TerminalMenu(["0", "1", "2", "3", "4", "5"], title="Give the location a rating from 1 to 5")


def get_l_type():
    terminal_menu = TerminalMenu(["History", "Nature", "Fun", "Castle", "Cave", "Waterfall", "Hilltop/Mountain", "Food place"], title="What type will the new location be?")
    
    l_type =  terminal_menu.show()
    if l_type == 0:
        logging.debug(f"History selected.")

    elif l_type == 1:
        logging.debug(f"Nature selected.")

    elif l_type == 2:
        logging.debug(f"Fun selected.")

    elif l_type == 3:
        logging.debug(f"Castle selected.")

    elif l_type == 4:
        logging.debug(f"Cave selected.")
    
    elif l_type == 5:
        logging.debug(f"Waterfall selected.")

    elif l_type == 6:
        logging.debug(f"Hilltop/Mountain selected.")
    
    elif l_type == 7:
        logging.debug(f"Food place selected.")

    else:
        logging.debug(f"Nothing selected. Fun selected.")
        l_type = 2

    return l_type

def get_l_coordinates():
    latitude = input("Give the latitude of the location.")
    longitude = input("Give the longitude of the location.")

    return {"latitude": latitude, "longitude": longitude}

def get_tts():
    tts = None
    while True:
        tts = input("Give the time you can spend on the location.")
        try:
            if int(tts) in range(1,6):
                 break


    return int(tts)

def create_mode():
    new_location = {}
    logging.info(f"Getting the locations name.")
    new_location["name"] = input("What is the name of the new location? ")
    
    logging.info(f"Selecting the location type.")
    new_location["type"] = get_l_type()
    logging.debug(f"Selecting tags.")
    new_location["tags"] = input("Write the tags for the location, separate them with ',': ")
    logging.debug(f"Selecting rating.")
    new_location["rating"] = input("Give the location a rating from 1 to 5: ")
    logging.debug(f"Selecting TTS.")
    new_location["tts"] = get_tts()
    logging.debug(f"Selecting coordinates.")
    new_location["l_coordinates"] = get_l_coordinates()



def browse_mode():
    pass

def alter_mode():
    pass

def itinerary_mode():
    pass

def help():
    pass

def exit():
    pass

def startup(create=False):
    if create == True:
        create_mode()

    while True:
        command = main_menu()
        print(command)
        #command = input("What would you like to do? Press 1 to insert a new location, 2 for Browse mode, 3 for Alter mode, 4 for Itinerary mode, 5 for help, q to exit the program: ").strip()
        print("------------------")

        if command == 0:
            logging.info(f"Entering Create mode.")
            create_mode()

        elif command == 1:
            logging.info(f"Entering Browse mode.")
            browse_mode()

        elif command == 2:
            logging.info(f"Entering Alter mode.")
            alter_mode()

        elif command == 3:
            logging.info(f"Entering Itinerary mode.")
            itinerary_mode()

        elif command == 4:
            logging.info(f"Entering Help mode.")
            help()


        elif command == None or 5:
            logging.info(f"Quiting.")
            exit()
            break

        
if __name__ == "__main__":
    if check_for_files() == True:
        startup()

    else:
        print("Not all files were present. Files were created. Starting the program in Create mode, so you can populate the locations.")
        print("--------------------")
        startup(create=True)

