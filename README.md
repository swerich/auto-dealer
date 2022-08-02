# CarCar

# Instructions to run project

Team:

* Person 1 - John - Service
* Person 2 - Rich - Sales

## Design

## Service microservice

Explain your models and integration with the inventory
microservice, here.

## Sales microservice

Explain your models and integration with the inventory
microservice, here.

[ ] Create Inventory API that provides:
    [ ] Manufacturer
    [ ] VehicleModel
    [ ] Automobile

[ ] React based front end app where we write the components to interact with:
    [ ] Sales services
    [ ] Inventory service

[ ] Sales API: The restful API to handle sales information

[ ] Sales Poller: a poller to use to integrate with other services

Requirements:

    Inventory Front-End Requirements

    Create React componenets accessible from the navbar to do the following:
        [ ] Show list of manufacturers
        [ ] Create a manufacturer
        [ ] Show a list of vehicle models
        [ ] Create a vehicle model
        [ ] Show a list of automobiles in inventory
        [ ] Create an automobile in inventory

    Sales Requirements

        Add a sales person: 

        [ ] Create a form that allows a person to enter the name and employee number for a sales person. When the form is submitted, the sales person is created in the application.
        [ ] Create a link in the navbar to get to the Add a Sales Person form

        Add a potential customer:

        [ ] Create a form that allows a person to enter the name, address, and phone number for a potential customer. When the form is submitted, the customer is created in the application.
        [ ] Create a link in the navbar to get to the Add a potential customer form

        Create a sales recordL

        [ ] Create a form that associates an automobile that came from the inventory and has not yet been sold, a sales person, and a customer with a price to record the sale of an automobile. When the form is submitted, the sales record is stored in the application.
        [ ] Create a link in the navbar to get to the Create a sale record form
        
        List all sales:

        [ ] Show a page that lists all sales showing the sales person's first name and employee number, the purchaser's name, the automobile VIN and the price of the sale.
        [ ] Create a link in the navbar to get to the list of all sales

        List a sales person's sales history:

        [ ] Show a list of the sales for a sales person's employee number by creating a page that has a dropdown that allows someone to choose a sales person from it. WHen the dropdown selection changes,fetch all of the sales associated with the sales person selected in the dropdown. Then, show that list of sales that has the sales person, the customer, the autombile VIN, and the price of the sale.
        [ ] Create a link in the navbar to get to the page that shows a specific sales person's sales history.




