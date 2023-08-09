import tkinter as tk
import CarPark as CP
import tkinter.simpledialog as sd


class Car_Park_GUI:
    """ This is the class that houses the widgets and its functionalities"""

    def __init__(self):
        # initialising the root window, frames and widgets of the Class
        self.root = tk.Tk()
        self.root.geometry("850x300")
        self.root.title("My Car Park")
        self.label = tk.Label(
            self.root, text="YOU ARE WELCOME!", font=("Arial", 15))
        self.label.pack(padx=15, pady=15)

        # creating two frames for the buttons and the outputlabel
        self.buttonframe = tk.Frame(self.root)
        self.outputframe = tk.Frame(self.root)

        # setting the frame for the buttons into 5 columns
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)
        self.buttonframe.columnconfigure(4, weight=1)

        # placing the output label in the  output frame
        self.outputlabel = tk.Label(
            self.outputframe, text="",  font=('Arial', 13))
        self.outputlabel.pack(pady=15)

        # defining the buttons, placing them into the buttonframe and inserting the button functions
        enter_button = tk.Button(
            self.buttonframe, text="Enter", font=('Arial', 13), borderwidth=10, padx=10, command=self.enter)
        enter_button.grid(row=1, column=0)
        exit_button = tk.Button(
            self.buttonframe, text="Exit", font=('Arial', 13), borderwidth=10, padx=10, command=self.exit)
        exit_button.grid(row=1, column=1)
        Available_button = tk.Button(
            self.buttonframe, text="Available Spaces", font=('Arial', 13), borderwidth=10, padx=10, command=self.available)
        Available_button.grid(row=1, column=2)
        Query_button = tk.Button(
            self.buttonframe, text="Query Records", font=('Arial', 13), borderwidth=10, padx=10, command=self.Query)
        Query_button.grid(row=1, column=3)
        Quit_button = tk.Button(
            self.buttonframe, text="Quit", font=('Arial', 13), borderwidth=10, padx=10, fg="red", command=self.Quit)
        Quit_button.grid(row=1, column=4)

        # setting the putton frame in the pack layout
        self.buttonframe.pack(fill='x')
        self.outputframe.pack(fill="x")

    # running the root window

    def run(self):

        CP.create_csv()
        CP.get_occupied_spaces()
        self.root.mainloop()

    # defining the function to enter car park, passed when the enter button is clicked
    def enter(self):
        if CP.available_parking_spaces() <= 0:
            self.outputlabel.config(text="Car Park limit exceeded!")

        else:
            Car = CP.Car_park()

        Vehicle_number = sd.askstring(
            "E.g A1234", "Please enter your vehicle registration number:")
        Validate = Car.validate_VN(Vehicle_number)
        if Validate == False:
            self.outputlabel.config(
                text="Enter valid vehicle registration number(e.g A1234)")
        else:
            isParked = Car.enter_carpark(Vehicle_number)
            if isParked == False:
                self.outputlabel.config(
                    text="Vehicle is already parked in the car park")
            else:
                self.outputlabel.config(text="Your Parking Space ID is: {}  and Your Ticket Number is: {} " .format(
                    Car.parkingspace_ID, Car.ticket_number))

    # defines the exit function to be passed when the exit button is clicked

    def exit(self):
        Car = CP.Car_park()
        Vehicle_number = sd.askstring(
            "Vehicle Registration", "Kindly Enter Vehicle registration number here: ")
        isSuccessful = Car.exit_carpark(Vehicle_number)
        if isSuccessful:
            self.outputlabel.config(text='''
                PRICE OF PARKING: £{}
                PARKING SPACE ID  OF DEPARTING VEHICLE: {}
                AVAILABLE PARKING SPACES: {}

                GOODBYE! '''.format(
                Car.cost,  Car.parkingspace_ID, CP.available_parking_spaces()))
        else:
            self.outputlabel.config(
                text="Vehicle is not currently parked in the car park")

    # defining the avialble spaces function to be called when the available button is clicked

    def available(self):
        Available_Parking_Spaces = CP.available_parking_spaces()
        self.outputlabel.config(text="The available parking space(s) are: {}".format(
            Available_Parking_Spaces))

    # defining the Query records function to be called when the query button is clicked

    def Query(self):
        Query_id = sd.askstring("Ticket Number", "Enter Ticket Number here: ")
        Query = CP.User_Records(Query_id)
        records = Query.query_records(Query_id)
        if records == None:
            self.outputlabel.config(text="Parking record doesnt exist")
        else:

            self.outputlabel.config(text="""

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

    # defining the quit function to close the window when the quit button is called

    def Quit(self):
        self.root.quit()


# Creating Car as an object of the Car_Park_GUI class and calling the run function to start the GUI window
Car = Car_Park_GUI()
Car.run()
