import CarPark as CP

# creates csv file at the start of the programme and reads the csv file
CP.create_csv()
CP.get_occupied_spaces()

# Prints option menu for users


def Menu():
    print('''
        Press "1" To Enter Car Park (2 pounds/hour)
        Press "2" To Exit Car Park 
        Press "3" To Check For Available Parking Spaces
        Press "4" To Query Parking Record
        Press "5" To Quit
        Available parking space(s): {}
    '''.format(CP.available_parking_spaces())
          )


while True:
    Menu()
    User_input = input("Enter your choice here: ")

    if User_input == "1":
        if CP.available_parking_spaces() <= 0:
            print("Car Park limit exceeded!")
        else:
            # creating Vehicle as an object of the Car_park class"
            Vehicle = CP.Car_park()

            Vehicle_number = input(
                "Kindly Enter Vehicle registration number here (e.g A1234): ")
            # calling the validate function to validate vehicle registration number
            Validate = Vehicle.validate_VN(Vehicle_number)
            if Validate == False:
                print("Enter valid vehicle registration number(e.g A1234)")
            else:
                # checking if a vehicle registration number already exists in the car park
                isParked = Vehicle.enter_carpark(Vehicle_number)
                if isParked == False:
                    print("Vehicle is already parked in the car park")

                else:
                    print("Your Parking Space ID is {}:  and Your Ticket Number is {}: " .format(
                        Vehicle.parkingspace_ID, Vehicle.ticket_number))

    elif User_input == "2":
        # Creating an object of the Car_park class
        Vehicle = CP.Car_park()
        Vehicle_number = input(
            "Kindly Enter Vehicle registration number here: ")
        isSuccessful = Vehicle.exit_carpark(Vehicle_number)
        if isSuccessful:
            print('''
            
                PRICE OF PARKING £{}:
                PARKING SPACE ID  OF DEPARTING VEHICLE {}:
                AVAILABLE PARKING SPACES {}:

                GOODBYE! '''.format(
                Vehicle.cost,  Vehicle.parkingspace_ID, CP.available_parking_spaces()))
        else:
            print("Vehicle is not currently parked in the car park")
    elif User_input == "3":
        # Calling the Avaiable_Parking_space method
        Available_Parking_Spaces = CP.available_parking_spaces()
        print("The available parking space(s) are {}:".format(
            Available_Parking_Spaces))
    elif User_input == "4":
        Query_id = input("Enter Ticket Number here: ")
        # Creating Query as an object of the User_Records class
        Query = CP.User_Records(Query_id)
        # calling the query_records method of the User_Records class
        records = Query.query_records(Query_id)
        if records == None:
            print("Parking record doesnt exist")
        else:

            print("""

                Your parking record is as follows: 
                Vehicle registration Number: {}
                Entry time: {}
                Exit time: {}
                Ticket Number: {}
                Parking space ID: {}
                Cost of parking: £{}
        
        """. format(
                records[0],
                records[1],
                records[2],
                records[3],
                records[4],
                records[5]
            ))
    elif User_input == "5":
        print(" Thank You For Parking With Us. We hope You Enjoyed Your stay.")
        break
    else:
        print("INVALID INPUT! Enter inputs from 1-5")
