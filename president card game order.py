import time

players= int(input("How many people are playing? (2-14) "))

oddoreven= players % 2

#if there are an even number of people
if oddoreven== 0:
    numofworkers=2

#if there are an odd number of people
else:
    numofworkers= 1

numofgov= int(((players- numofworkers)/2))
numofpleb= int(numofgov)

while True:
    print()
    print("There are",numofgov,"goverment roles")
    time.sleep(1)
    if numofworkers== 1:
        print("There is 1 worker")
    else:
        print("There are 2 workers")
    time.sleep(1)
    print("There are",numofpleb,"plebs")
    time.sleep(1)
    print()


    allnames=[]

    #goverment roles
    govroles=["President: ","Vice-President: ","Speaker of the House: ","Office: ","Prime Ministor: ","MP: "]
    govnames=[]
    for i in range(numofgov):
        name=input(govroles[i])
        govnames.append(name)
        allnames.append(name)
    #print(govnames)
    print()

    #workers
    workernames=[]
    for i in range(numofworkers):
        name= input("Worker: ")
        workernames.append(name)
        allnames.append(name)
    #print(workernames)
    print()

    #pleb roles
    plebroles=["Pleb: ","Super-Pleb: ","Mega-Pleb: ","Tramp: ","Super-Tramp: ","Illegal Immigrant: "]
    plebnames=[]
    for i in range(numofpleb):
        name=input(plebroles[i])
        plebnames.append(name)
        allnames.append(name)
    #print(plebnames)

    #~~~~~~~~~~~~~~~~~~   adding/removing players   ~~~~~~~~~~~~~~~~~~~~~~~~#
    while True:
        print()
        print("Press [r] to remove a player")
        print("Press [a] to add a new player")
        print("Press Enter to continue")
        choice= input()

        if choice== "r":
            print()
            print(allnames)
            print("Whos name do youwant to remove?")
            removename=input()
            allnames.remove(removename)
        elif choice == "a":
            print()
            name= input("What is their name? ")
            allnames.append(name)
        else:
            break
    print(allnames)
    print()

    numofplayers=(len(allnames))#how many people are now playing
    print(numofplayers)

    ### ~~~~~~~~~~  reordering who is what role when new players are added  ~~~~~~~~~~~~~~~~~~~~#
    oddoreven= numofplayers % 2
    #if there are an even number of people
    if oddoreven== 0:
        numofworkers=2
    #if there are an odd number of people
    else:
        numofworkers= 1

    numofgov= int(((numofplayers- numofworkers)/2))
    numofpleb= int(numofgov)

    '''print(numofgov)
    print(numofworkers)
    print(numofpleb)

    print(allnames)'''
    print()

    govnames=[]
    workernames=[]
    plebnames=[]
    #presidents
    for i in range(numofgov):
        govnames.append(allnames[i])
        #print(allnames[i])
    print()
    #workers
    for i in range(numofworkers):
        a= i+numofgov
        workernames.append(allnames[a])
        #print(allnames[a])
    #plebs
    print()
    for i in range(numofpleb):
        b =i+numofworkers+ numofgov
        plebnames.append(allnames[b])
        #print(allnames[b])
    print()

    '''print(govnames)
    print(workernames)
    print(plebnames)
    print()'''
    ### ~~~~~~~~~~~~~~~  how many cards they give/get (eg. +2)  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    howmanycards= numofgov
    for i in range(numofgov):
        print(govnames[i],"   +",howmanycards)
        howmanycards -= 1
    print()

    for i in range(numofworkers):
        print(workernames[i],"   +",0)
    print()

    howmanycards= 1
    for i in range(numofpleb):
        print(plebnames[i],"   -",howmanycards)
        howmanycards +=1

    print()
    continueon =input("Press enter to continue")
    print()












