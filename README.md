# CarCar 
    This project is a frontend/backend application that can be used by a car dealership to manage inventory, sales and service. It is useful, in that repect.

# Getting started
   Open a terminal and CD into a directory where you'd like to clone the project files, and run the following commands in your terminal:
    
        1. git clone https://gitlab.com/rich5D/project-beta.git
        2. cd project-beta
        3. docker-compose build
        4. docker-compose up
    
    In your browser, go to: localhost:3000/







# CarCar Planning

Team:

* Person 1 - John, Automobile Service
* Person 2 - Rich, Auto Sales

## Design

## Service microservice

-Keep track of service appointments for automobiles and their owners

-Technician form:
    -auto tech's name and employee number
    -when form submitted, auto tech is created in the application
    -link in navbar to get to "Enter a technician" form

-Service appointment:
    -allows service concierge to enter VIN of vehicle, date and time of appointment, assigned technician, reason for service appointment
    -when form submitted, service appointment should be saved in the application
    -link in navbar to get to "Enter a service appointment" form

-List of appointments:
    -shows list of scheduled appointments that contains details collected in the form: VIN, date and time of appointment, assigned technician, reason for service appointment
    -if VIN was for automobile that was one time in the inventory, automobile was purchased from dealership
    -list of scheduled appointments should show automobile was purchased from dealership, so concierge can give customer "VIP treatment"
    -each appointmet in list should have button that allows concierge to cancel appointment, or show that appointment has been finished
    -when appointment is cancelled or finished, should no longer show up in list of appointments
    -link in navbar to get list of appointments

-Service history
    -show a list of service appointments for specific VIN
        -create a page that allows someone to type in the VIN
        -on form submission, fetch all service appointments for automobile with VIN in input
        -show list of service appointments to include customer name, date and time of service, assigned technician's name, reason for service
    -link in navbar for service history


## Sales microservice

Explain your models and integration with the inventory
microservice, here.

[x] Create Inventory API that provides:
    [x] Manufacturer
    [x] VehicleModel
    [x] Automobile

[ ] React based front end app where we write the components to interact with:
    [x] Sales services
    [x] Inventory service

[x] Sales API: The restful API to handle sales information

[x] Sales Poller: a poller to use to integrate with other services

Requirements:

    Inventory Front-End Requirements

    Create React componenets accessible from the navbar to do the following:
        [x] Show list of manufacturers
        [x] Create a manufacturer
        [x] Show a list of vehicle models
        [x] Create a vehicle model
        [x] Show a list of automobiles in inventory
        [x] Create an automobile in inventory

    Sales Requirements

        Add a sales person: 

        [x] Create a form that allows a person to enter the name and employee number for a sales person. When the form is submitted, the sales person is created in the application.
        [x] Create a link in the navbar to get to the Add a Sales Person form

        Add a potential customer:

        [x] Create a form that allows a person to enter the name, address, and phone number for a potential customer. When the form is submitted, the customer is created in the application.
        [x] Create a link in the navbar to get to the Add a potential customer form

        Create a sales recordL

        [x] Create a form that associates an automobile that came from the inventory and has not yet been sold, a sales person, and a customer with a price to record the sale of an automobile. When the form is submitted, the sales record is stored in the application.
        [x] Create a link in the navbar to get to the Create a sale record form
        
        List all sales:

        [x] Show a page that lists all sales showing the sales person's first name and employee number, the purchaser's name, the automobile VIN and the price of the sale.
        [x] Create a link in the navbar to get to the list of all sales

        List a sales person's sales history:

        [ ] Show a list of the sales for a sales person's employee number by creating a page that has a dropdown that allows someone to choose a sales person from it. WHen the dropdown selection changes,fetch all of the sales associated with the sales person selected in the dropdown. Then, show that list of sales that has the sales person, the customer, the autombile VIN, and the price of the sale.
        [ ] Create a link in the navbar to get to the page that shows a specific sales person's sales history.

