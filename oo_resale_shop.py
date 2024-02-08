# Import a few useful containers from the typing module
from typing import Dict, Optional
from computer import *

class ResaleShop:

    # What attributes will it need?
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = {}
        self.itemID = 0
        
    # What methods will you need?
    #Buys a computer and adds it to the inventory and assigns an itemID
    def buy(self, computer: Computer):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer
        return self.itemID
        
    #Sells a computer and removes it from the inventory
    def sell(self, itemID: int):
        if self.itemID in self.inventory:
            del self.inventory[self.itemID]
            print("Item", self.itemID, "sold!")
        else: 
            print("Item", self.itemID, "not found. Please select another item to sell.")

    #Shows the shop's inventory 
    def print_inventory(self):
        #If there's computers in the inventory...
        if self.inventory:
        # For each item
            for self.itemID in self.inventory:
                # Print item details
                print(f'Item ID: {self.itemID} : {self.inventory[self.itemID]}')
        #If theres no computers in the inventory...
        else:
            print("No inventory to display.")
            print("stuff")
    
    #Refurbish a computer using it's itemID using the refurbish method in the Computer class. 
    def refurb(self, itemID: int):
        return self.inventory[self.itemID].refurbish()
    


def main():
    #Make a shop
    myShop = ResaleShop()
    #buy computers 
    print(myShop.buy(Computer("2019 MacBook Pro", 150, "Windows", "Windows 12.1", 2019)))
    print(myShop.buy(Computer("2020 MacBook", 200, "Intel", "Intel 1.3", 2020)))
    #Show the shop inventory
    myShop.print_inventory()
    #Sell a computer
    myShop.sell(2)
    #Show new shop inventory
    myShop.print_inventory()
    


main()