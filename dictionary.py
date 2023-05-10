import json

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] ) 
        

# Create new word function
# ----------------------------------------
def createNewWord ():
    word = input("Enter a word: ")
    meaning = input("Ënter meaning: ")
    
    
    if word not in dictionary:
        dictionary[word] = [meaning]
    else:
        dictionary[word].append(meaning)


menu_options = {
    1: 'Create',
    2: 'Read All',
    3: 'Delete word',
    4: 'Quit',
}

dictionary = {}


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
            with open("dictionary.json", "a") as outfile:
                outfile.write(json.dumps(dictionary, indent=2))
            break







 







