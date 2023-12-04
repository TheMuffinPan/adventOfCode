def main():
    """ Loop through a input file where there are digits mixed in with other
    alpha numeric characters. Need to isolate the first and last digit of the
    line, and create a single 2 digit integer. If there is only 1 digit add it
    to itself ie 1 -> 11. """

    # General initialization for total sum
    totalSum = 0

    # Prepare to read the input data
    inputFile = open("./1/inputData.txt", "r")

    # Loop over the individual lines of the input data
    for lineValue in inputFile:

        # Loop over the individual line values characters and if any are a
        # numerical digit append it to the digits array
        digits = []
        for x in lineValue:
            if (x.isdigit()):
                digits.append(x)
            
        # Get the first and last digit from the digits array
        firstDigit = digits[0]
        lastDigit = digits[len(digits)-1]

        # "Add" the first and last digit together as a string then convert to an
        # integer to ensure it is a 2 digit integer that is created
        lineSum = int(str(firstDigit) + str(lastDigit))

        # Add the 2 digit integer to the total sum
        totalSum = totalSum + lineSum

    # Close the input file since we are done with the loop
    inputFile.close()    
    
    # Print out the total sum value
    print("totalSum: " + str(totalSum))


# Main
if __name__ == "__main__":
    """ The main call to the main function """

    # Run the funtion
    main()