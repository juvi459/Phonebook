import sys

def initial_phonebook():
    rows,cols = int(input("Please enter initial number of contacts")),5
    phone_book =[]
    print(phone_book)

    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):"% (i+1))
        print("NOTE: * indicates mandatory fields")
        print("....................................................................")

        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter Name*: *")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit(
                        "Name is a mandatory field. Process exiting due to blank field...")

