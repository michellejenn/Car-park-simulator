import datetime
import csv
import os

# GLOBAL VARIABLES THAT CONTAIN NUMBER OF TOTAL AND OCCUPIED PARKING SPACES
occupied_spaces = set()
Total_parking_spaces = 7

# STATIC FUNCTION TO GET THE OCCUPIED PARKING SPACES AND ADD IT TO THE occupied_spaces VARIABLE


def get_occupied_spaces():

    with open('Records.csv', mode="r") as csvfile:
        csv_reader = csv.reader(csvfile)
        # next(csv_reader)
        global occupied_spaces
        for row in csv_reader:
            if row[2] == '' and row[5] == '':
                occupied_spaces.add(row[4])
        csvfile.close()
    return True

# STATIC FUNCTION TO CALCULATE THE NUMBER OF AVAILABLE PARKING SPACES IN THE CAR PARK


def available_parking_spaces():
    get_occupied_spaces()
    global Total_parking_spaces
    global occupied_spaces
    return Total_parking_spaces - len(occupied_spaces)

# CAR PARK FIRST CLASS


class Car_park:
    ''' Class Car_park. Contains instance variables/ states and instance methods of the Car_park class used to 
    instantiate the object of the class for every car that enters the car park in the CUI or GUI
      '''

    # INITIALISING STATES AND BEHAVIOURS OF THE Car_park CLASS
    def __init__(self):
        self.VN = None
        self.cost = None
        self.ticket_number = None
        self.parkingspace_ID = None
        self.Entry_Time = None
        self.Exit_Time = None

    # A METHOD USED TO ASSIGN A PARKING SPACE ID FOR USERS ENTERING THE CAR PARK WITH A TOTAL OF 7 SPACES
    def Parking_space_identifier(self):
        global occupied_spaces
        for i in range(1, 8):
            if str(i) in occupied_spaces:
                continue
            else:
                return i
    # A METHOD USED TO RECORD THE TIME A USER ENTERS OR EXITS THE CAR PARK

    def Get_Time(self):
        return datetime.datetime.now()

    # A METHOD USED TO CALCULATE THE COST OF PARKING USING THE ENTRY AND EXIT TIME AT £2 PER HOUR
    def calculate_Cost(self, Entry_time, Exit_time):
        current_entry_time = datetime.datetime.strptime(
            Entry_time, "%Y-%m-%d %H:%M:%S.%f")

        duration = Exit_time - current_entry_time
        duration_per_hr = duration.total_seconds() / 3600

        return duration_per_hr * 2

    # AN INSTANCE METHOD TO GENERATE A TICKET NUMBER BY APPENDING  "ABC" TO THE VEHICLE NUMBER
    def Ticket_number(self, VN):
        return VN + "ABC"

    # AN INSTANCE METHOD FOR VALIDATING THE VEHICLE REGISTRATION NUMBER ENTERED BY THE USER
    # SO THAT ONLY A PATTERN OF 5 CHARACTERS, STARTING WITH AN ALPHABET IS ENTERED
    def validate_VN(self, VN):
        if len(VN) != 5:
            return False
        if not VN[0].isalpha():
            return False
        if not VN[1:].isdigit():
            return False
        return True

    # AN INSTANCE METHOD CALLED WHEN A VEHICLE USER WANTS TO ENTER THE CAR PARK
    def enter_carpark(self, VN):
        rows = Read_from_csv()
        for row in rows:
            if row[0] == VN and row[5] == "":

                return False
    # ASSIGNING VALUES GOTTEN FROM THE FUNCTIONS TO VARIABLES
        self.VN = VN
        self.Entry_Time = self.Get_Time()
        self.ticket_number = self.Ticket_number(VN)
        self.parkingspace_ID = self.Parking_space_identifier()

    # PLACING THE OBJECTS GOTTEN IN A LIST OF OBJECTS
        list_of_objects = [self.VN, self.Entry_Time, "",
                           self.ticket_number, self.parkingspace_ID, ""]

        write_to_csv(list_of_objects)
        return True

    # AN INSTANCE METHOD CALLED WHEN A CAR WANTS TO LEAVE THE CAR PARK
    def exit_carpark(self, VN):
        get_occupied_spaces()
        global occupied_spaces
        rows = Read_from_csv()
        try:
            for row in rows:
                if VN == row[0]:
                    self.VN = VN
                    self.Entry_Time = row[1]
                    self.Exit_Time = self.Get_Time()
                    row[2] = self.Exit_Time
                    self.ticket_number = row[3]
                    self.parkingspace_ID = row[4]
                    self.cost = self.calculate_Cost(
                        self.Entry_Time, self.Exit_Time)
                    row[5] = self.cost
                    # break
            occupied_spaces.remove(self.parkingspace_ID)

            with open('Records.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(rows)
            csvfile.close()
            get_occupied_spaces()

            return True
        except:
            return False

# CREATES A CSV FILE WHEN CALLED


def create_csv():
    if not os.path.isfile("Records.csv"):
        with open('Records.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Vehicle_Registration_no', 'Entry_Time', 'Exit_Time',
                            'TicketNumber', 'Parking_space_ID',  'Cost_of_Parking'])
            csvfile.close()
    else:
        return

# WRITES LIST OBJECTS INTO THE CSV


def write_to_csv(list_of_objects):
    with open('Records.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(list_of_objects)
        csvfile.close()

# READS FROM THE CSV FILE TO APPEND A NEW ROW CALLED


def Read_from_csv():
    rows = []
    with open("Records.csv", mode='r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            rows.append(row)
    return rows


class User_Records:
    ''' Contains the state and method that gets the record from the CSV'''

    # initialising Ticket numer
    def __init__(self, Ticketnumber):
        self.Ticketnumber = Ticketnumber

    # method that reads the csv file to get the record for the using the user's ticket number
    def query_records(self, Ticketnumber):
        try:
            with open('Records.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)

                for row in reader:
                    if Ticketnumber == row[3]:

                        return list(row)
        except:
            return None
