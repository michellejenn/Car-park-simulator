# Car-park-simulator
##  CarPark Simulator


Welcome to the CarPark Simulator project! This comprehensive software application is designed to simulate the dynamics and management of a car park environment. Whether you're a developer exploring parking system algorithms or a student learning about simulation techniques, this project provides a versatile solution.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Command Line Interface (CUI)](#command-line-interface-cui)
  - [Graphical User Interface (GUI)](#graphical-user-interface-gui)
- [Main Functionality](#main-functionality)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The CarPark Simulator is a powerful software application that replicates real-world car park operations. It enables users to create and manage a virtual car park, control vehicle entry and exit, monitor parking space availability, and analyze traffic patterns. This simulator serves as an educational tool, a testing environment for parking algorithms, and a visual aid for presentations on parking management systems.

## Features

- **Realistic Simulation**: Experience lifelike car park scenarios, including vehicles entering, searching for parking spots, and exiting the car park.

- **Billing System**: Implement a billing system that calculates parking costs based on the duration of stay. Each hour of parking incurs a predefined cost (e.g., £2), ensuring fair billing for users.


- **Interactive Interfaces**: Choose between using a command line interface (CUI) or a graphical user interface (GUI) to interact with the simulation.
  
- **Dynamic Status Updates**: Receive live updates on parking space availability and occupied spaces as vehicles enter and exit the car park. This dynamic status tracking provides an accurate representation of the changing conditions.

- **Data Collection**: Gather insights with data on parking durations, occupancy rates, and more for analysis.

## Installation

1. **Clone the Repository**: `git clone https://github.com/michellejenn/carpark-simulator.git`
2. **Navigate to the Project Directory**: `cd carpark-simulator`

## Usage

### Command Line Interface (CUI)

1. Run the main functionality script using the following command:
   ```bash
   python main_script.py

The CUI presents options to enter the car park, exit, check available parking spaces, query records, and quit the simulation.

Follow the on-screen instructions to perform actions within the car park simulation.

### Graphical User Interface (GUI)
Run the GUI script using the following command:

bash
Copy code
python gui_script.py
The GUI window provides options for entering, exiting, checking available parking spaces, querying records, and quitting the simulation.

Interact with the graphical interface to simulate car park activities and observe the results.

## Main Functionality
The main functionality of the CarPark Simulator includes the core features required for the simulation:

Car entry and exit: Simulate vehicle entry and exit with real-time parking space occupancy updates.
Ticketing system: Generate ticket numbers for vehicles, calculate parking costs, and record parking durations.
Data management: Store parking records in a CSV file, allowing for querying and data analysis.

## Configuration
The config.json file allows customization of the simulation parameters:

car_park_size: Set the car park dimensions.
entry_rate: Adjust the rate at which vehicles enter the car park.
exit_rate: Configure the rate at which vehicles exit the car park.
vehicle_preferences: Define parking spot preferences for vehicles (e.g., closer to exits).

## Contributing
Contributions are welcome! Enhance the CarPark Simulator by following these steps:

Fork the repository.
Create a new branch: git checkout -b feature-new-feature.
Implement your changes and commit them: git commit -m 'Add new feature'.
Push your changes to your fork: git push origin feature-new-feature.
Submit a pull request explaining your changes and improvements.

## License
This project is licensed under the MIT License.

We invite you to explore the CarPark Simulator for educational, testing, and visualization purposes. If you encounter issues or have suggestions for improvements, feel free to create issues or contribute to the project. Enjoy simulating car park dynamics and management!
