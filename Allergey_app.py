#Now just beautify in the free time you have
from tkinter import *
import requests

def click(key):
    # print the key that was pressed
    print(key.char)

def apiingredients(barcode):


    # Define the API endpoint URL
    url = 'https://trackapi.nutritionix.com/v2/search/item/?upc='+barcode

    try:
        headers = {'content-type': 'application/json','x-app-id':'c404e551','x-app-key':'485514be9b95df5d7818d16da81cb93b'}
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url,headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None



# create root window
root = Tk()

# root window title and dimension
root.title("Allergy Checker")
# Set geometry(widthxheight)
root.geometry('1200x1200')
root.configure(bg="#ffffff")
barcode_frame = Frame(root, bg="#ffffff",relief="sunken")
barcode_frame.grid(row=0, column=0, pady=10)
lbl = Label(barcode_frame, text="Enter barcode number:", font=("Comfortaa", 17), bg="white",fg="black") #center this and change font color
lbl.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=3)



# adding Entry Field
txt = Entry(barcode_frame, width=10, font=("Comfortaa",17))
txt.grid(row=1, column=0, padx=10, pady=10, sticky="ew", columnspan=3)
txt.focus_set()
txt.bind("<Key>", click)

table_frame = Frame(root,bg="#ffffff")
table_frame.grid(row=1, column=0, padx=10, pady=10)

def typed():
    barcode=txt.get()

def del_info():
    for x in table_frame.grid_slaves():
        x.grid_forget()
def clicked():
    barcode=txt.get()
    print(len(barcode))
    txt.delete(0, END)
    del_info()
    allist = ["Milk", "Cream", "Cheese", "Eggs", "Egg", "Fish", " Anchovy", "Salmon", "Herring", "Mackerel",
              "Sardine", "Tuna", "Cod", "Trout", "Pollock", "Seafood", "Fish sauce", "Fish oil", "Surimi", "Gelatin",
              "Omega-3", "fatty acids", "Seaweed", "Caviar", "Fish meal", "Anchovy paste", "Fish protein", "Fumet",
              "Shellfish", "Shrimp", "Prawns", "Crab", "Lobster", "Scallops", "Clams", "Mussels", "Oysters", "Squid",
              "Octopus", "Cuttlefish", "Abalone", "Krill", "Cockles", "Nuts", "Peanut", "Wheat", "Soy", "Soybean",
              "Sesame","Cashews","Almonds"]
    firstlist = []
    lastlist = []
    #txt.delete(0, 'end')

    json=apiingredients(barcode)
    print(json)  # Debugging line

    if json and 'foods' in json and len(json['foods']) > 0:
        # Check if 'nf_ingredient_statement' exists in the first item
        if 'nf_ingredient_statement' in json['foods'][0]:
            ingredients = json['foods'][0]['nf_ingredient_statement'].split(',')
        else:
            print('Ingredient statement not found.')
            ingredients = []  # Empty list if no ingredients found
        foodname= json['foods'][0]['food_name']

    else:
        print('No food data found for the barcode.')
        ingredients = []
    if ingredients:
        for x in allist:
            for i in ingredients:
                if x.lower() in i.lower():  # Check case-insensitively
                    firstlist.append(x)
                    break
    for y in firstlist:
        if y == "Milk" or y == "Cream" or y == "Cheese":
            lastlist.append("Dairy allergen")
        elif y == "Egg" or y == "Eggs":
            lastlist.append("Egg allergen")
        elif y == "Fish" or y == " Anchovy" or y == "Salmon" or y == "Herring" or y == "Mackerel" or y == "Sardine" or y == "Tuna" or y == "Cod" or y == "Trout" or y == "Pollock" or y == "Seafood" or y == "Fish sauce" or y == "Fish oil" or y == "Surimi" or y == "Gelatin" or y == "Omega-3" or y == "Fatty Acids" or y == "Seaweed" or y == "Caviar" or y == "Fish meal" or y == "Anchovy Paste" or y == "Fish protein" or y == "Fumet":
            lastlist.append("Fish allergen")
        elif y == "Shellfish" or y == "Shrimp" or y == "Prawns" or y == "Crab" or y == "Lobster" or y == "Scallops" or y == "Clams" or y == "Mussels" or y == "Oysters" or y == "Squid" or y == "Octopus" or y == "Cuttlefish" or y == "Abalone" or y == "Krill" or y == "Cockles":
            lastlist.append("Shellfish allergen")
        elif y == "Almonds" or y == "Nuts" or y == "Cashew" or y=="Cashews" or y == "Nut":
            lastlist.append("Tree nut allergen")
        elif y == "Peanut" or y == "Peanuts":
            lastlist.append("peanut allergen")
        elif y == "Soy" or y == "Soybean":
            lastlist.append("Soy allergen")
        elif y == "Sesame":
            lastlist.append("Sesame allergen")


    if(len(firstlist))==0:
            lastlist.append("No potential allergens found")

    lastlist = list(set(lastlist))

    class Table:
        def __init__(self, root):
            header_font = ('Comfortta', 15,)
            food = Label(root,text=foodname, fg="black", font=("Quicksand", 22),
                         bg="white", )
            food.grid(row=1, column=0, padx=10, pady=10, sticky="ew", columnspan=3)
            # Add header row
            for j in range(total_columns):
                header = Label(root, width=50, text=lst[0][j], font=header_font, justify='center', wraplength=400,bg="#ffffff", fg="blue")
                header.grid(row=2, column=j)

            # Add data rows
            for i in range(1, total_rows):
                for j in range(total_columns):
                    label = Label(root, width=50, text=lst[i][j], font=('Comfortaa', 15, 'bold'), justify='center',wraplength=400,bg="#ffffff", fg="#ed1b24")
                    label.grid(row=i + 3, column=j)

    # take the data
    lst = [('Found key words in Ingredients:', "\n".join(firstlist)), ('Allergies', "\n".join(lastlist))]
    total_rows = len(lst)
    total_columns = len(lst[0])


    t = Table(table_frame)
btn = Button(barcode_frame, text = "Find allergens" ,fg = "#ffffff", command=clicked,font=("Comfortaa", 17), bg="red",)
btn.grid(row=2, column=0, padx=10, pady=10, sticky="ew", columnspan=3)

root.mainloop()