kratz_deli = ["Tom", "Paul", "Mike"]

def line(kratz_deli):
    if len(kratz_deli) == 0:
        print("The line is currently empty.")
    else:
        print("The line is currently: ", end = "")
        for name in kratz_deli:
            if name != kratz_deli[-1]:
                print(f"{(kratz_deli.index(name) + 1)}. {name}", end = " ")
            else:
                print(f"{(kratz_deli.index(name) + 1)}. {name}", end = "\n")

def take_a_number(kratz_deli, name):
    kratz_deli.append(name)
    print(f"Welcome, {name}. You are number {kratz_deli.index(name) + 1} in line.")

def now_serving(kratz_deli):
    if len(kratz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {kratz_deli[0]}.")
        kratz_deli.pop(0)
        
    return None
