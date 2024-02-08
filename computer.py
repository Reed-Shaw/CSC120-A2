# Import a few useful containers from the typing module
from typing import Dict, Optional

class Computer:

    # What attributes will it need?
    Description: str
    #^Ex. "2019 Macbook Pro"
    Price: float
    Operating_System: str
    Updates: str
    Year_Made: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, price, operating_sys, updates, year_made):
        self.Description = description
        self.Price = price
        self.Operating_System = operating_sys
        self.Updates = updates
        self.Year_Made = year_made

    # What methods will you need?
    #Method that will return a description of the computer
    def show_desc(self):
        return self.Description
    
    #Method that will update the price of the computer and print out the new price
    def update_price(self, new_price: float):
        self.Price = new_price
        print(new_price)

    #Method that will return the computer's price
    def show_price(self):
        return self.Price
    
    #Method that will return the operating system
    def show_op_sys(self):
        return self.Operating_System
    
    #Method that will update the computer and print the new update
    def update_comp(self, new_update: str):
        self.Updates = new_update
        return self.Updates
    
    #Refurbish the computer automatically
    def refurbish(self, new_os: Optional[str] = None):
        if self.Year_Made < 2000:
            self.Price = 0 # too old to sell, donation only
        elif self.Year_Made < 2012:
            self.Price = 250 # heavily-discounted price on machines 10+ years old
        elif self.Year_Made < 2018:
            self.Price = 550 # discounted price on machines 4-to-10 year old machines
        else:
            self.Price = 1000 # recent stuff
        if new_os is not None:
           self.Operating_System = new_os # update details after installing new OS



def main():
    #Make computer
    myComputer = Computer("2019 MacBook Pro", 100, "Windows", "Windows 12.1", 2019)
    #Test computer methods  
    print(myComputer.show_desc())
    print(myComputer.show_op_sys())
    myComputer.refurbish("Windows 13")
    print(myComputer.show_price())
    print(myComputer.show_op_sys())

main()
