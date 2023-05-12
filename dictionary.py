import json


# Print menu function
#----------------------------------------
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] ) 
        

# Create new word function
# ----------------------------------------
def createNewWord ():
    word = input("Enter a word: ")
    meaning = input("Ënter meaning: \n")
    
    
    if word not in dictionary:
        dictionary[word] = [meaning]
    else:
        dictionary[word].append(meaning)


# Save and Quit function
#-----------------------------------------
def saveAndQuit ():
    with open("dictionary.json", "w") as outfile:
        outfile.write(json.dumps(dictionary, indent=4))
        outfile.close()
        

#Delete function
#----------------------------------------
def delWord ():
    word_toDel = input("Enter the word you want to delete: ")
    if word_toDel in dictionary:
        dictionary.pop(word_toDel)
        print("\n Successfully deleted \n")

    
#Change function
#----------------------------------------
def changeWord():
    wordToChange = input("Enter the word you want to change: ")
    newMeaning = input("Enter a new value:")
    if wordToChange in dictionary:
        dictionary[wordToChange] = [newMeaning]

#Find function
#----------------------------------------
def find ():
    findWord = input("Enter the word: ")
    """ if findWord in dictionary:
        print(findWord , ': ' ,  dictionary[findWord]) """
    for x in dictionary.keys():
        if findWord in x:
            print(x , ': ' ,  dictionary[x])

            

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
    option = int(input('\nEnter your choice: '))

    match option:
        case 1:
            createNewWord()        
        case 2:
            print(dictionary)
        case 3:
            changeWord()
        case 4:
            find()
        case 5:
            delWord()
        case 6:
            saveAndQuit()
            break







 







