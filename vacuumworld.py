def printInformation(location): 
    print("Location " + location + " is Dirty")
    print("Cost for cleaning " + location + ": 1")
    print("Location " + location + " has been cleaned")
    
    
def vacuumCleaner(goalState, currentState, location):
    print("\nGoal State Required:\n", goalState)
    print("\nVacuum is placed in location " + location)
    totalCost = 0
    
    while(currentState != goalState):
        if(location == "A"):
            #cleaning
            if(currentState['A'] == 1):
                currentState ['A'] = 0
                totalCost += 1
                printInformation('A')
            else: 
                print("Location " + location + " is already clean")
                
            #moving    
            if(currentState['B'] == 1 or currentState['C'] == 1):
                print("-------------> Moving right to the location B.\nCost for moving Right: 1")
                location = 'B'
                totalCost += 1
                
        elif(location == "B"):
            #cleaning
            if(currentState["B"] == 1):
                currentState["B"] = 0
                totalCost += 1
                printInformation("B")
            else: 
                print("Location " + location + " is already clean")
                
            #moving    
            if(currentState['A'] == 1):
                print("<----------------- Moving left to the location A.\nCost for moving Left: 1")
                location = 'A'
                totalCost += 1
                
            if(currentState['C'] == 1): 
                print("--------------------> Moving right to the location C.\nCost for moving Right: 1")
                location = "C"
                totalCost += 1
        
        elif(location == "C"):
            #cleaning
            if(currentState["C"] == 1):
                currentState["C"] = 0
                totalCost += 1
                printInformation("C")
            else: 
                print("Location " + location + " is already clean")
                
            #moving    
            if(currentState['A'] == 1 or currentState['B'] == 1):
                print("<------------------ Moving left to the location B.\nCost for moving Left: 1")
                location = 'B' or 'A'
                totalCost += 1
                
    print("\nGoal State: ", currentState)
    return totalCost


goalState = {"A": 0, "B": 0, "C": 0}
currentState = {"A": -1, "B": -1, "C": -1}

location = input("Enter Location of Vacuum:\n")
currentState["A"] = int(input("Enter status of A: "))
currentState["B"] = int(input("Enter status of B: "))
currentState["C"] = int(input("Enter status of C: "))

totalCost = vacuumCleaner(goalState, currentState, location)
print("Performance Measurement: ", totalCost)