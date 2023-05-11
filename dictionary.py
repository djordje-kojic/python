import json


# Print menu function
#----------------------------------------
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] ) 
        

# Create and Save new word into JSON
# ----------------------------------------
def createNewWord ():
    word = input("Enter a word: ")
    meaning = input("Ënter meaning: ")
    
    
    if word not in dictionary:
        dictionary[word] = [meaning]
    else:
        dictionary[word].append(meaning)


# Save and Quit
#-----------------------------------------
def saveAndQuit ():
    with open("dictionary.json", "w") as outfile:
        outfile.write(json.dumps(dictionary, indent=4))
        outfile.close()
        

with open('dictionary.json', 'r') as openfile:
    dictionary = json.load(openfile)

menu_options = {
    1: 'Create',
    2: 'Read All',
    3: 'Delete word',
    4: 'Quit',
}

 

while(True):
    print_menu()
    option = int(input('Enter your choice: '))

    match option:
        case 1:
            createNewWord()        
        case 2:
             print(dictionary)
        case 3:
            print("test Delete word")
        case 4:
            saveAndQuit()
            break







 







