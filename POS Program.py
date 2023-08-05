import datetime
def letA():
    print("= = = = =")
    print("<Add a Product>")
    f = open("Products.txt", "a")
    name = input("Product Name: ")
    price = input("Product Price: ")
    try:
        if price is float or int:
            float(price)
            f.write(f"Product Name: {name}\n")
            f.write(f"    Product Price: {price}\n")
            f.close()
            print("! Product added to the system.")
            task()
        else:
            try:
                print("! Product not added. Invalid Price.")
                f.close()
                task()
            except ValueError:
                print("! Product not added. Invalid Price.")
                f.close()
                task()
    except ValueError:
        print("! Product not added. Invalid Price.")
        f.close()
        task()
def letV():
    f = open("Products.txt", "r")
    print("<View Products>")
    print(f.read())
    f.close()
    task()
def letD():
    print("<Delete a Product>")
    rmv = input("Product Name: ")
    f = open("Products.txt", "r")
    found = False
    lines = f.readlines()
    f = open("Products.txt", "w")
    i = 0
    while i < len(lines):
        if rmv in lines[i]:
            found = True
            i += 2
        else:
            f.write(lines[i])
            i += 1
    f.close()
    if found:
        print("! Product removed from the inventory.")
        task()
    else:
        print("! Product does not exist.")
        task()


def letT():
    print("= = = = =\n")
    print("<Transact Sales>")
    def getprice(product):
        for line in products_data:
            if product in line:
                price_index = products_data.index(line)+1
                try:
                    product_price = float(products_data[price_index].strip().split(": ")[1])
                    return product_price
                except (IndexError, ValueError):
                    print("! Product does not exist.")
                    return None
        return None
    nf = open("LOGBOOK.txt", "a")
    nf.write("\n= = = = =\n")
    dt = datetime.datetime.now()
    nf.write(f"""Date: {dt}
Products Transacted:\n""")
    user_inputs = []
    total_price = 0

    f = open("Products.txt", "r")
    products_data = f.readlines()

    while True:
        x = input("Product Name (type 'x' to stop the transaction): ")
        if x == "x":
            print("Total Cost: ", total_price)
            print("See LOGBOOK for the transaction details")
            nf.write(f"Total Cost: {total_price}")
            f.close()
            nf.close()
            task()
        else:
            product_price = getprice(x)
            if product_price is not None:
                user_inputs.append(x)
                total_price += product_price
                nf.write(f"{x} - {product_price}\n")
            else:
                print("! Product does not exist.")

def task():
    pick = input("""= = = = =
Tasks:
    A - Add a Product
    V - View Products
    D - Delete a Product
    T - Transact Sales
    [ANY KEY] - Exit
Chosen task is: """)
    if pick.upper() == "A":
        letA()
    elif pick.upper() == "V":
        letV()
    elif pick.upper() == "D":
        letD()
    elif pick.upper() == "T":
        letT()
    else:
        quit()


print("POS - PYTHON")
task()