import re

def main():
    """ """

    # Initializations
    colorSearchList = ["red", "green", "blue"]
    powerValues = []

    # Prepare to read the input data
    inputFile = open("./2/inputData.txt", "r")
    fileLines = inputFile.readlines()
    inputFile.close()    

    # Loop over the individual lines of the input data
    for game in fileLines:
        cubes = game.split(":")[1].strip() # Split off the : and get the second part since the first part is the Game and Index which we do not want to search through
        individualPulls = cubes.split(";")

        # Loop over the collection of pulls for this game to determine individual pull draw amounts
        cubeTotalsPerPull = [0, 0, 0]
        for ii in individualPulls:
            colorOrder = re.findall(r"(?=("+'|'.join(colorSearchList)+r"))", ii)
            valueOrder = re.findall(r"\b[0-9]+\b", ii)

            # Parse and and find the max rolled value of each color
            for jj in range(len(valueOrder)):
                currentColor = colorOrder[jj]
                currentValue = int(valueOrder[jj])
                colorIndex = colorSearchList.index(currentColor)
                if (currentValue > cubeTotalsPerPull[colorIndex]):
                    cubeTotalsPerPull[colorIndex] = currentValue

        # Multiple the minimum values needed together and store in an array
        powerValues.append((cubeTotalsPerPull[0]*cubeTotalsPerPull[1])*cubeTotalsPerPull[2])

    # Sum of the powers to determine the final sum
    total = sum(powerValues)
    print("total: " + str(total))
    

# Main
if __name__ == "__main__":
    """ """

    # Run the funtion
    main()