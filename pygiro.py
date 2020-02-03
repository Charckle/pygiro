from modules import pylavor
import logging
from simple_term_menu import TerminalMenu


logging.basicConfig(level=logging.DEBUG)  #filename='upTimer.log',level=logging.INFO, filemode='w')

class Location():
    def __init__(self, data):
        self.name = data["name"]
        self.type = data["type"]
        self.tags = data["tags"]
        self.rating = data["rating"]
        self.tts = data["tts"]
        self.l_coordinates = data["l_coordinates"]
        self.mtld = data["mtld"]
        self.short_d = data["short_d"]
        self.long_d = data["long_d"]
        self.contact = data["contact"]
        self.timetable = data["timetable"]
        self.fee = data["fee"]
        self.child = data["child"]    
        self.season = data["season"]    

    def __str__(self):
        print(f"Location name: {self.name}")
        print(f"Type: {type_to_name(self.type)}")
        print(f"Tags: {self.tags}")
        print(f"Location rating: {self.rating}")
        print(f"Time to spend: {self.tts}")
        print(f"Latitude: {self.l_coordinates[0]}, Longitude: {self.l_coordinates[1]}")
        print(f"Maximum to location difficulty: P{self.mtld}")
        print(f"Description: {self.short_d}")
        print(f"Long description: {self.long_d}")
        print(f"Webpage: {self.contact[0]}\nTel: {self.contact[1]}\nEmail: {self.contact[2]}")
        print(f"Timetable: {self.timetable}")
        print(f"Fee: {no_dep_yes(self.fee)}")
        print(f"Suitable for children: {no_dep_yes(self.child)}")
        print(f"Season dependant: {no_yes(self.season)}")

    def to_database(self):
        new_location = {}

        logging.debug(f"Writting {new_location["name"]} to main database.")
        new_location["name"] = self.name
        new_location["type"] = self.type
        new_location["tags"] = self.tags
        new_location["rating"] = self.rating
        new_location["tts"] = self.tts
        new_location["l_coordinates"] = self.l_coordinates
        new_location["mtld"] = self.mtld
        new_location["short_d"] = self.short_d
        new_location["long_d"] = self.long_d
        new_location["contact"] = self.contact
        new_location["timetable"] = self.timetable
        new_location["fee"] = self.fee
        new_location["child"] = self.child
        new_location["season"] = self.season


        all_locations = pylavor.json_read("data/databases", "all_places.json")
        all_locations[new_location["name"]] = new_location
        pylavor.json_write("data/databases", "all_places.json", all_locations)

 
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
    terminal_menu = TerminalMenu(["0", "1", "2", "3", "4", "5"], title="Give the location a rating from 0 to 5: ")

def no_dep_yes(ndy):
    if ndy == 0:
        return "No"

    elif ndy == 1:
        return "Depends"

    else:
        return "Yes"

def no_yes(ndy):
    if ndy == 0:
        return "No"

    else:
        return "Yes"

def type_to_name(l_type):
    if l_type == 0:
        return "History"

    elif l_type == 1:
        return "Nature"

    elif l_type == 2:
        return "Fun"

    elif l_type == 3:
        return "Castle"

    elif l_type == 4:
        return "Cave"
    
    elif l_type == 5:
        return "Waterfall"

    elif l_type == 6:
        return "Hilltop/Mountain"
    
    elif l_type == 7:
        return "Food place"
   
    elif l_type == 8:
        return "Museum"

    else:
        return "ERROR"


def get_l_type():
    terminal_menu = TerminalMenu(["History", "Nature", "Fun", "Castle", "Cave", "Waterfall", "Hilltop/Mountain", "Food place", "Museum"], title="What type will the new location be?")
    
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
        logging.debug(f"Waterfall selected")

    elif l_type == 6:
        logging.debug(f"Hilltop/Mountain selected.")
    
    elif l_type == 7:
        logging.debug(f"Food place selected.")

    elif l_type == 8:
        logging.debug(f" selected.")


    else:
        logging.debug(f"Nothing selected. Fun selected.")
        l_type = 2

    return l_type

def get_l_coordinates():
    latitude = input("Give the latitude of the location: ")
    longitude = input("Give the longitude of the location: ")

    #return {"latitude": latitude, "longitude": longitude}
    return [latitude, longitude]

def get_tts():
    tts = None
    while True:
        tts = input("Give the time you can spend on the location in minutes: ")
        try:
            if isinstance(int(tts), int):
                break
        except:
            pass

    logging.debug(f"Selected time to stay {tts}")

    return int(tts)

def get_rating():
    terminal_menu = TerminalMenu(["0 - If you have time, go see it once", "1 - Nothing special, but nice to see", "2 - Worth seeing if you can spare the time", "3 - Check it out, you wont regret it", "4 - Really good, top and see it", "5 - A must every time!"], title="How would you rate the location, where 5 is the best?")
    
    l_type =  terminal_menu.show()
    
    logging.debug(f"Selected rating {l_type}")

    return l_type

def get_l_ttl():
    ttl = None
    while True:
        ttl = input("Give the time you need to get to the location in minutes.")
        try:
            if isinstance(int(ttl), int):
                break
        except:
            pass

    logging.debug(f"Selected time to location {ttl}")

    return int(ttl)

def get_mtld():
    terminal_menu = TerminalMenu(["PP0 - Easy, do not bother to mention", "PP1 - Peacefull walk", "PP2 - Can have some climbing protections", "PP3 - Climbing protections, but not exposed, phisical strenght needed", "PP4 - Vertical, exposed route", "PP5 - Basicaly rock climbing with steel cables.",  "PP6 - Like 5 but harder and more vertica"], title="Select the max to location difficulty. 0 is for parking the car and walking to the location on a paved road.")
    
    l_mtld =  terminal_menu.show()
    
    logging.debug(f"Selected max to location difficulty {l_mtld}")

    return l_mtld

def get_contacts():
    web = input("Webpage of the location, (no https://): ")
    tel = input("Telephone number of the location: ")
    email = input("Email address of the location: ")

    contacts = [web, tel, email]
    
    logging.debug(f"Selected the contacts {contacts}")

    return contacts

def get_fee():
    terminal_menu = TerminalMenu(["No", "Depends", "Yes"], title="Does the location have a fee?")
    
    l_fee =  terminal_menu.show()
    
    logging.debug(f"Selected fee status {l_fee}")

    return l_fee

def get_child():
    terminal_menu = TerminalMenu(["No", "Depends", "Yes"], title="Is the location suitable for children?")
    
    l_child =  terminal_menu.show()
    
    logging.debug(f"Selected fee status {l_child}")

    return l_child

def get_season():
    terminal_menu = TerminalMenu(["No", "Yes"], title="Is the location season dependand?")
    
    l_season =  terminal_menu.show()
    
    if l_season == 1:
        comment =  input("How is it dependant?: ")
    else:
        comment = "" 

    logging.debug(f"Selected season dependant {l_season}")

    return [l_season, comment]


def location_need_changes():
    terminal_menu = TerminalMenu(["Yes", "No"], title="Do you agree with the inserted data?")
    
    l_ok =  terminal_menu.show()
    
    logging.debug(f"Selected is OK changes: {l_ok}")

    return l_ok


def create_mode():
    new_location = {}

    logging.debug(f"Getting the locations name.")
    new_location["name"] = input("What is the name of the new location? ")
    logging.debug(f"Selected {new_location['name']}")
    
    logging.debug(f"Selecting the location type.")
    new_location["type"] = get_l_type()

    logging.debug(f"Selecting tags.")
    new_location["tags"] = input("Write the tags for the location, separate them with ',': ")
    logging.debug(f"Selected tags: {new_location['tags']}")
    
    logging.debug(f"Selecting rating.")
    new_location["rating"] = get_rating()
    
    logging.debug(f"Selecting TTS.")
    new_location["tts"] = get_tts()
    
    logging.debug(f"Selecting coordinates.")
    new_location["l_coordinates"] = get_l_coordinates()
    
    logging.debug(f"Selecting max to location difficulty.")
    new_location["mtld"] =  get_mtld()
    
    logging.debug(f"Selecting short description.")
    new_location["short_d"] = input("Write a short description of the location: ")
    logging.debug(f"Selected short description: {new_location['short_d']}")
    
    logging.debug(f"Selecting long description.")
    new_location["long_d"] = input("Write a long description of the location: ")
    logging.debug(f"Selected long description: {new_location['long_d']}")
    
    logging.debug(f"Selecting contact details.")
    new_location["contact"] =  get_contacts()
    
    logging.debug(f"Selecting a timetable.")
    new_location["timetable"] = input("Write the timetable: ")
    logging.debug(f"Selected long description: {new_location['timetable']}")
    
    logging.debug(f"Selecting fee status.")
    new_location["fee"] = get_fee()

    logging.debug(f"Selecting child status.")
    new_location["child"] = get_child()
    
    logging.debug(f"Selecting season")
    new_location["season"] = get_season()


    new_location_created = Location(new_location)
    new_location_created.__str__()

    change_data_l = location_need_changes()
    if change_data_l == 0:
        alter_mode(new_location_created)

    else:



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

