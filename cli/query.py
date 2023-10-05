from data import warehouse1, warehouse2

#Gretting and Menu
def initial_interaction(username):
    print (f"""
Welcome {username}, 

Please select one of the following options

1. List items by warehouse
2. Search an item and place an order
3. Quit
""")
    user_selection= str(input("Write your selection: "))
    user_interaction(user_selection)

# Choose the path to follow based on user_selection
def user_interaction (sel):
    if sel == "1":
        print_all()
    elif sel == "2":   
        search_result = search_item(retrive_item())
        order_request = result_eval(search_result)
        order(order_request)
    elif sel == "3":
        farewell(username)
        exit()
    else:
        print (f"{sel} is not a valid operation.")
        farewell(username)

#Getting the item from user       
def retrive_item():
    selected_item=input("Please introduce the item you are looking for: ")
    return selected_item

# Print all the items of both Warehouses    
def print_all():
    print ("Items available in warehouse 1 are:\n")
    for item in warehouse1:
        print (item)
    print ("Items available in warehouse 2 are:\n")
    for item in warehouse2:
        print (item)

#Search the number of ocurrences of the item
def search_item(item):
    print (f"Searching for {item}...")
    item_qty_wh1 = 0
    item_qty_wh2 = 0
    for items in warehouse1:
        if item in items:
            item_qty_wh1 += 1
        else:
            pass
    for items in warehouse2:
        if item in items:
            item_qty_wh2 += 1
        else:
            pass
    return [item_qty_wh1, item_qty_wh2]

# returning info of location and total items
def result_eval(result):
    total = result[0]+result[1]
    if result[0] == 0 and result[1]==0:
        print (f"""Amount available: 0
Location: Not in stock
""")
        {farewell(username)}
        exit()
    elif result[0] == 0 and result[1] > 0:
        print (f"""Amount available: {total}
Location: Warehouse 2
""")
        return total
    elif result[0] > 0 and result[1] == 0:
        print (f"""Amount available: {total}
Location: Warehouse 1""")
        return total
    elif result[0] > 0 and result[1] > 0:
        print (f"""Amount available: {total}
Location: Both warehouses""")
        if result[0] > result[1]:
            print (f"Maximum availability: {result[0]} in Warehouse 1")
        elif result[0] == result[1]:
            print (f"Maximum availability: {result[1]} in both Warehouses")
        else: 
            print (f"Maximum availability: {result[1]} in Warehouse 2")
        return total

# Order processing      
def order(val):
    order_sel = input("Would you like to order this item?(y/n): ")
    if order_sel == "n":
        print (f"Thank you for your visit, {username}!")
    elif order_sel == "y":
        order_count = int(input("How many would you like?: "))
        if order_count>val:
            print (f"There are not this many available. The maximum amount that can be ordered is {val}")
            max_available_sel = input("Would you like to order the maximum available?(y/n): ")
            if max_available_sel == "n":
                {farewell(username)}
            elif max_available_sel == "y":
                print (f"{val} Almost new router have been ordered.")
        elif order_count<val:
            print (f"{order_count} Almost new router have been ordered.")
            {farewell(username)}

# Farewell
def farewell(name):
    print (f"Thank you for your visit, {name}!")
        



# Getting username
username=input("Introduce your name: ")
# Caling the initial interaction
initial_interaction(username)

