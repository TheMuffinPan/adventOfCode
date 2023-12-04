import re

def main():
    """ """

    # Initializations
    maxRed = 12
    maxGreen = 13
    maxBlue = 14
    validGames = [True]*100
    colorSearchList = ["red", "green", "blue"]

    # Prepare to read the input data
    inputFile = open("./2/inputData.txt", "r")
    fileLines = inputFile.readlines()
    games = enumerate(fileLines)

    # Loop over the individual lines of the input data
    for index, game in games:
        index = index + 1 # Need to add by 1 since the game values start at 1
        cubes = game.split(":")[1].strip() # Split off the : and get the second part since the first part is the Game and Index which we do not want to search through
        individualPulls = cubes.split(";")

        # Loop over the collection of pulls for this game to determine individual pull draw amounts
        for ii in individualPulls:
            colorOrder = re.findall(r"(?=("+'|'.join(colorSearchList)+r"))", ii)
            valueOrder = re.findall(r"\b[0-9]+\b", ii)

            # Parse and total the draw amounts for each individual pull
            cubeTotalsPerPull = [0, 0, 0]
            for jj in range(len(colorOrder)):
                currentColor = colorOrder[jj]
                currentValue = valueOrder[jj]
                colorIndex = colorSearchList.index(currentColor)
                cubeTotalsPerPull[colorIndex] = int(cubeTotalsPerPull[colorIndex]) + int(currentValue)

            # Determine if any pull in this game is invalid or not
            if (cubeTotalsPerPull[0] > maxRed) or (cubeTotalsPerPull[1] > maxGreen) or (cubeTotalsPerPull[2] > maxBlue):
                validGames[index-1] = False

        # Find all the valid games
        validGameIndex = [ii for ii, x in enumerate(validGames) if x]

    # Sum of the indicies of the valid games and add the length of the arrary to adjust for the Games index starting at 1 vs 0
    total = sum(validGameIndex) + len(validGameIndex)
    print("total: " + str(total))

    # Close the input file since we are done with the loop
    inputFile.close()    
    

# Main
if __name__ == "__main__":
    """ """

    # Run the funtion
    main()