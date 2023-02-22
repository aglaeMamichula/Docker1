
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost= cost
        self.quantity=quantity
        
    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return float(self.cost)

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return int(self.quantity)
        
    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return "{}\n{}\n{}\n{}\n{}".format(self.country,self.code,self.product,self.cost,self.quantity)

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    with open ("inventory.txt","r") as f:
        for i,x in enumerate(f):
            if i > 0:
                shoe_contents = x.split(",")
                shoe_object = Shoe(country= shoe_contents[0], code = shoe_contents[1], product= shoe_contents[2], cost= shoe_contents[3], quantity= shoe_contents[4].replace("\n", ""))
                shoe_list.append(shoe_object)
        
def update_shoe_data():
    with open("inventory.txt","w") as f:
        f.write("Country,Code,Product,Cost,Quantity\n")
        for each in shoe_list:
            f.write("{},{},{},{},{}\n".format(each.country, each.code, each.product, each.cost, each.quantity))
        
def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    country = input("please add the country of your shoe")
    code = input("please add the code of you new shoe")
    product = input("please add the name of your new shoe")
    cost = int(input("please add the cost of your new shoe")) 
    quantity= int(input("please add the quantity of your new shoe"))
    
    new_shoe= Shoe(country=country,code=code, product=product,cost=cost,quantity=quantity)
    shoe_list.append(new_shoe)
    

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    for each in shoe_list:
        print(each.__str__())
    

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    quantity_dictionary = {}
    for each in shoe_list:
        current_quantity = each.get_quantity()
        if current_quantity in quantity_dictionary:
            quantity_dictionary [current_quantity].append(each)
        else:
            quantity_dictionary [current_quantity]=[each]
    
    quantity= list(quantity_dictionary.keys())
    quantity.sort()
    lowest_shoes = quantity_dictionary[quantity[0]]
    print("Lowest quantity shoes are:")
    for lowest_shoe in lowest_shoes:
        #option to re-stock dependign on what the user choose yes/no and how many
        print("{}: {}".format(lowest_shoe.product, lowest_shoe.quantity))
        
    for lowest_shoe in lowest_shoes:
        add_to_shoes = input("would you like to re-stock {}? (yes or no) ".format(lowest_shoe.product))
        if add_to_shoes.lower() == "yes":
            add_quantity = int(input("how many shoes would you like to add: "))
            new_quantity = lowest_shoe.get_quantity() + add_quantity
            lowest_shoe.quantity = str(new_quantity)
            update_shoe_data()
            
            
def seach_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    search_code= input("please enter the code")
    for each in shoe_list:
        if each.code == search_code:
            return each

def value_per_item():   
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    for each in shoe_list:
        current_value = each.get_cost() * each.get_quantity()
        print("{}: {}".format (each.product, current_value))

def highest_qty():  
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    quantity_dictionary = {}
    for each in shoe_list:
        current_quantity = each.get_quantity()
        if current_quantity in quantity_dictionary:
            quantity_dictionary [current_quantity].append (each)
        else:
            quantity_dictionary [current_quantity]=[each]
    
    quantity= list(quantity_dictionary.keys())
    quantity.sort()
    return quantity_dictionary[quantity[-1]]
    
#==========Main Menue=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

while True:
    read_shoes_data()
    menu=int(input("""    1. add shoe.
    2. details.
    3. view all.
    4. low stock.
    5. search shoe.
    6. value of the item
    7. full stock.
    0. exit
    """))
    # 1. add shoe.
    if menu==1:
        capture_shoes()
        print("new shoe added")
    # 2. details. 
    elif menu==2:
        view_all()
    #3. view all.    
    elif menu==3:
        view_all()
    #4. low stock.    
    elif menu==4:
        re_stock()
    # 5. search shoe    
    elif menu==5:
        found_shoe=seach_shoe()
        if found_shoe:
            print(found_shoe.__str__())
        else:
            print("shoe not found")
    #6. value of the item    
    elif menu==6:
        value_per_item()
    #7. full stock    
    elif menu==7:
        highest_quantities = highest_qty()
        for each_highest in highest_quantities:
            print((each_highest.product))
    #0. exit
    elif menu==0:
        print('Goodbye!!!')
        exit() 