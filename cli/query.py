from data import stock, personnel
from datetime import datetime

# Initial Variables
# Sumary
search_history = list()
listed_categories = list()
listed_items = 0
# Item Variable
item = ''

# User Validator


def validator(func):
    def wrapper(*args, **kwargs):
        print("Autentication required.")
        user = username
        passwd = input("Provide your Password: ")

        # autentication
        if authenticate(user, passwd):
            return func(*args, **kwargs)
        else:
            print("Invalid Username or Password, Access Denied")
            farewell(username, total_listed)
    return wrapper


# user autenticator


def authenticate(user, password, users=personnel):
    for user_info in users:
        if user_info["user_name"] == user and user_info.get("password") == password:
            return True
        if "head_of" in user_info:
            if authenticate(user, password, user_info["head_of"]):
                return True
    return False


# Getting user


def get_user():
    username = input("Introduce your name: ")
    return username


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
        order_sel(order_request)
    elif sel == "3":
        category_list(stock)
    elif sel == "4":
        summary(username)
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


# Expanded categories


def category_expand(categories, items):
    cat_selection = int(input("Type the number of the category to browse: "))
    listed_categories.append(categories[cat_selection][0])
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
    search_history.append(selected_item)
    selected_item = selected_item.title()
    global item
    item = selected_item
    return selected_item


# Print all the items of both Warehouses


def print_all():
    warehouse_count = dict()

    print("Items available are:\n")
    for item in stock:
        print(item)
        if item["warehouse"] in warehouse_count:
            warehouse_count[item["warehouse"]] += 1
        else:
            warehouse_count[item["warehouse"]] = 1
    print("\n")
    for key, val in warehouse_count.items():

        print(f"Items in Warehouse {key}: {val}")
    global total_listed
    total_listed += sum(warehouse_count.values())
    farewell(username)


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
    result = dict()
    for item in result_dict:
        if item["location"] in result:
            result[item["location"]] += 1
        else:
            result[item["location"]] = 1
    result_ord = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))

    # print total amount
    print("Amount available: ", sum(result_ord.values()))
    # print list of items
    print("Location:")
    for item in result_dict:
        print(
            f"""- Warehouse {item["location"]} (in stock for {item["days"]}) days""")
    # evaluationg warehouses availability
    total = sum(result_ord.values())
    if total == 0:
        print(f"""Location: Not in stock
""")
        {farewell(username)}

    else:
        max_avail = list(result_ord.keys())[0]
        print(
            f"Maximum availability: {result_ord[max_avail]} in Warehouse {max_avail}")
    return total


# Order processing


def order_sel(val: int):
    order_sel = input("Would you like to order this item?(y/n): ")
    if order_sel == "n":
        farewell(username)
    elif order_sel == "y":
        order(val)


@validator
def order(val: int):
    order_count = int(input("How many would you like?: "))
    if order_count > val:
        print(
            f"There are not this many available. The maximum amount that can be ordered is {val}")
        max_available_sel = input(
            "Would you like to order the maximum available?(y/n): ")
        if max_available_sel == "n":
            {farewell(username)}
        elif max_available_sel == "y":
            print(f"{val} {item} have been ordered.")
            {farewell(username)}
    elif order_count < val:
        print(f"{order_count} {item} have been ordered.")
        {farewell(username)}


# Farewell


def farewell(name):
    continue_interaction = input(
        f"{name} do you want to perform another operation?(y/n): ")
    if continue_interaction == "y":
        initial_interaction(username)
    else:
        summary(name)
        exit()


def summary(name):
    print(f"Thank you for your visit, {name}!")
    print("In this session you have: ")
    print(f"1. Listed for {total_listed} items")
    print(f"2. Searched for: ")
    for items in search_history:
        print("     -", items)
    print(f"3. Browsed the category: ")
    for items in listed_categories:
        print("     -", items)


total_listed = 0
# Username
username = get_user()
# Caling the initial interaction
initial_interaction(username)
