#all immport
import random
import time

#Set up command
class Player():
    def __init__(self):
        self.player_hungry = 2
        self.player_health = 10
        self.inventory = {}

    def has_item(self,item):
        item_count = self.inventory.get(item, 0)
        if item_count > 0:
            return True
        else:
            return False
    def item_count(self):
        pass
    
    def add_item(self, item, count=1):
        item_count = self.inventory.get(item, 0)
        self.inventory[item] = item_count + count
        
    def remove_item(self, item):
        if self.has_item(item):
            item_count = self.inventory.get(item, 0)
            self.inventory[item] = item_count - 1
    def show_inv(self):
        print("Your item is-----")

        
class Event():
    def main_event(player):
        rand_num = random.randint(7)
#Not finish        
    
    def explore(player):
        rand_num = random.randint(0,100)
        if rand_num < 10:
            "rare_event"
        elif rand_num < 30:
            "common_event"
        else:
            "normal__event"
#Not finish             

def intro_user_choice():
    print("you hve to pick 3 item out of 7")
    print("which is food, video game, cat, gun, first aid kit, radio , bird")
    
def get_user_choice () :
#input1
        start_item1 = input("What 1 item you want to choose?")
         
        if start_item1 in ['food','video game','cat','gun','first aid kit','radio','bird']:
            valid_choice = True
        else:
            print("That is not an option...Plz try again")
            get_user_choice()
#input2      
        start_item2 = input("What 2 item you want to choose?")
        
        if start_item2 in ['food','video game','cat','gun','first aid kit','radio','bird']:
            valid_choice = True
        else:
            print("That is not an option...Plz try again")
            get_user_choice()
#input3        
        start_item3 = input("What 3 item you want to choose?")
        
        if start_item3 in ['food','video game','cat','gun','first aid kit','radio','bird']:
            valid_choice = True
        else:
            print("That is not an option...Plz try again")
            get_user_choice()
#out put123            
        print(start_item1,start_item2,start_item3)
    
        
       
            

def test_change()
    pass

intro_user_choice()
get_user_choice()
