import json
import time


# Print menu functions
#-----------------------------------------------
def printMenu():
    print('\n')
    for key in menu_options:
        print(key, ' -- ', menu_options[key])


# Save and Quit functions
#-----------------------------------------------
def saveAndQuit():
    with open("remainders.json", "w") as outfile:
        outfile.write(json.dumps(remData, indent=4))

# Add new remainder
#-----------------------------------------------
def addNew():
    title = input("Enter title: ")
    label = input("Enter lanel: ")
    priority = int(input("Enter priority 1-5: "))

    if priority < 1 or priority > 5:
        print("Priority must be in range 1-5!\n")
        priority = int(input("Enter priority 1-5: "))

    
    remainder = {'Title': title, 'Label': label, 'Priority': priority}
    remData.append(remainder)


# Read all remainders
#-----------------------------------------------
def readAll():
    for k in remData:
        print(k, '\n')


# Delete remainder
#-----------------------------------------------
def delRemainder():
    print("Enter the reminder number to delete: (0 -  "  ,len(remData) -1, ")" )
    toDel = int(input())
    del remData[toDel]



# Change remainder
#-----------------------------------------------
def changeRem():
    for k in remData:
        print(k, '\n')

    remToChange = int(input("Enter remainder to change: ")) - 1
    
    new_title = input("Enter title: ")
    new_label = input("Enter lanel: ")
    new_priority = int(input("Enter priority 1-5: "))

    remData[remToChange] = {'Title': new_title, 'Label': new_label, 'Priority': new_priority}


t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)


with open("remainders.json", "r") as openfile:
    remData = json.load(openfile)



menu_options = {
    1: 'Add',
    2: 'Read All',
    3: 'Change',
    4: 'Delete',
    5: 'Quit'
}

while(True):

    printMenu()
    
    try:
        option = int(input("Enter your choice:"))
    except ValueError:
        print("\n!!! Wrong entry, try again (need to be number) !!!")
        continue

    match option:
        case 1:
            addNew()
        case 2:
            readAll()
        case 3:
            changeRem()
        case 4:
            delRemainder()
        case 5:
            saveAndQuit()
            break
