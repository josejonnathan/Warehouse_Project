from data import stock
from datetime import datetime, timedelta

# Gretting and Menu


def initial_interaction(username):
    print(f"""
Welcome {username}, 

Please select one of the following options

1. List items by warehouse
2. Search an item and place an order
3. Browse by category
4. Quit
""")
    user_selection = str(input("Write your selection: "))
    user_interaction(user_selection)

# Choose the path to follow based on user_selection


def user_interaction(sel):
    if sel == "1":
        print_all()
    elif sel == "2":
        search_result = search_item(retrive_item())
        order_request = result_eval(search_result)
        order(order_request)
    elif sel == "3":
        category_list(stock)
    elif sel == "4":
        farewell(username)
        exit()
    else:
        print(f"{sel} is not a valid operation.")
        farewell(username)

# Printing categories


def category_list(items):
    category = dict()
    category_menu = list()
    for item in stock:
        if item["category"] not in category:
            category[item["category"]] = 1
        else:
            category[item["category"]] += 1
    for count, item in enumerate(category):
        category_menu.append([item, category[item]])
        print(f"{count}. {item} ({category[item]})")
    print("*" * 30)
    category_expand(category_menu, items)


def category_expand(categories, items):
    cat_selection = int(input("Type the number of the category to browse: "))
    print(f'List of {categories[cat_selection][0]} available:\n')
    for item in items:
        if item["category"] == categories[cat_selection][0]:
            print(
                f"{item['state']} {item['category']}, Warehouse {item['warehouse']}")
        else:
            pass
    print("*" * 30)
    farewell(username)

# Getting the item from user


def retrive_item():
    selected_item = input("Please introduce the item you are looking for: ")
    selected_item = selected_item.title()
    return selected_item

# Print all the items of both Warehouses


def print_all():
    warehouse1_count = 0
    warehouse2_count = 0
    print("Items available are:\n")
    for item in stock:
        print(item,)
        if item["warehouse"] == 1:
            warehouse1_count += 1
        elif item["warehouse"] == 2:
            warehouse2_count += 1
    print("\n")
    print("Total items in warehouse 1: ", warehouse1_count, "\n")
    print("Total items in warehouse 2: ", warehouse2_count, "\n")


# Search the number of ocurrences of the item
def search_item(item):
    print(f"Searching for {item}...")
    search_result = list()
    for items in stock:
        item_name = items["state"] + " " + items["category"]
        if item in item_name:
            search_result.append(
                {"location": items["warehouse"], "days": time_delta(items["date_of_stock"])})

        else:
            pass
    return (search_result)

# Timedelta


def time_delta(d1):
    stock_time = datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")
    today = datetime.today()
    delta = today - stock_time
    return delta.days


# returning info of location and total items

def result_eval(result_dict):
    # counting availability by warehouse
    result = [0, 0]
    for item in result_dict:
        if item["location"] == 1:
            result[0] += 1
        else:
            result[1] += 1
    # print total amount
    print("Amount available: ", result[0] + result[1])
    # print list of items
    print("Location:")
    for item in result_dict:
        print(
            f"""- Warehouse {item["location"]} (in stock for {item["days"]})""")
    # evaluationg warehouses availability
    total = result[0] + result[1]
    if result[0] == 0 and result[1] == 0:
        print(f"""Location: Not in stock
""")
        {farewell(username)}
        exit()
    elif result[0] == 0 and result[1] > 0:
        print(f"""Location: Warehouse 2
""")
        return total
    elif result[0] > 0 and result[1] == 0:
        print(f"""Location: Warehouse 1""")
        return total
    elif result[0] > 0 and result[1] > 0:
        print(f"""Location: Both warehouses""")
        if result[0] > result[1]:
            print(f"Maximum availability: {result[0]} in Warehouse 1")
        elif result[0] == result[1]:
            print(f"Maximum availability: {result[1]} in both Warehouses")
        else:
            print(f"Maximum availability: {result[1]} in Warehouse 2")
        return total

# Order processing


def order(val):
    order_sel = input("Would you like to order this item?(y/n): ")
    if order_sel == "n":
        print(f"Thank you for your visit, {username}!")
    elif order_sel == "y":
        order_count = int(input("How many would you like?: "))
        if order_count > val:
            print(
                f"There are not this many available. The maximum amount that can be ordered is {val}")
            max_available_sel = input(
                "Would you like to order the maximum available?(y/n): ")
            if max_available_sel == "n":
                {farewell(username)}
            elif max_available_sel == "y":
                print(f"{val} Almost new router have been ordered.")
        elif order_count < val:
            print(f"{order_count} Almost new router have been ordered.")
            {farewell(username)}

# Farewell


def farewell(name):
    print(f"Thank you for your visit, {name}!")


# Getting username
username = input("Introduce your name: ")
# Caling the initial interaction
initial_interaction(username)
