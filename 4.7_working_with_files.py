filename = "import_exercises.py"
with open(filename, "r") as f:
    contents = f.readlines()
    for i, line in enumerate(contents, start = 1):
        print(i,": ", line)

grocery_list = ["lettuce", "oranges", "beans"]


def make_grocery_list(grocery_list):
    filename = "my_grocery_list.txt"
    with open(filename, "w") as f:
        for item in grocery_list:
            f.write(item + "\n")
            
make_grocery_list(grocery_list)


def show_grocery_list():
    with open("my_grocery_list.txt") as f:
        contents = f.readlines()
        for item in contents:
            print(item)
show_grocery_list()

def buy_item(item):
    remaining_items = grocery_list.remove(item)
    make_grocery_list(remaining_items)
buy_item("spinach")