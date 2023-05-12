import json


# Print menu function
#----------------------------------------
def print_menu():
    print('\n')
    for key in menu_options.keys():
        print (key, '--', menu_options[key] ) 
        

# Create new word function
# ----------------------------------------
def createNewWord ():
    word = input("Enter a word: ")
    meaning = input("Ënter meaning:")
    
    
    if word not in dictionary:
        dictionary[word] = [meaning]
    else:
        dictionary[word].append(meaning)


#Change function
#----------------------------------------
def changeWord():
    wordToChange = input("Enter the word you want to change: ")
    if wordToChange in dictionary:
        newMeaning = input("Enter a new value: ")
        dictionary[wordToChange] = [newMeaning]
    else:
        print("\nNo such word!\n")


#Find function
#----------------------------------------
def find ():
    findWord = input("Enter the word: ")
    for x in dictionary.keys():
        if findWord in x:
            print('\n', x , ': ' ,  dictionary[x])


#Delete function
#----------------------------------------
def delWord ():
    word_toDel = input("Enter the word you want to delete: ")
    if word_toDel in dictionary:
        dictionary.pop(word_toDel)
        print("\n Successfully deleted \n")


# Save and Quit function
#-----------------------------------------
def saveAndQuit ():
    with open("dictionary.json", "w") as outfile:
        outfile.write(json.dumps(dictionary, indent=4))
        outfile.close()
        

            

with open('dictionary.json', 'r') as openfile:
    dictionary = json.load(openfile)
    openfile.close()

menu_options = {
    1: 'Create',
    2: 'Read All',
    3: 'Change',
    4: 'Find words',
    5: 'Delete word',
    6: 'Quit',
}


while(True):

    print_menu()

    try:
        option = int(input('\nEnter your choice: '))
    except ValueError:
        print("\n!!! Wrong entry, try again (need to be number) !!! \n")
        continue
    
    match option:
        case 1:
            createNewWord()        
        case 2:
            print(dictionary, '\n')
        case 3:
            changeWord()
        case 4:
            find()
        case 5:
            delWord()
        case 6:
            saveAndQuit()
            break







 







