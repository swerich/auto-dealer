# CarCar

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

Add one more line
