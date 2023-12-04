# Import regex
import re

# Main Function
def main():
    """ Loop through a input file where there are digits mixed in with other
    alpha numeric characters. Need to isolate the first and last digit of the
    line, and create a single 2 digit integer. If there is only 1 digit add it
    to itself ie 1 -> 11. There are also digits values of one, two, three, etc
    through to nine. These are valid digits and need to be considered. However
    something like oneight means one and eight not 1ight. This edge case needs
    to be considered as well. """

    # General initializations for the total sum
    totalSum = 0

    # Create a string list of all valid digits to regex on and an according conversion array for what that digit should be converted to. 
    stringList = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    valueList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Prepare to read the input data
    inputFile = open("./1/inputData.txt", "r")

    # Loop over the individual lines of the input data
    for lineValue in inputFile:
        lineValue = lineValue.strip()

        # Find all the instances of a valid digit even if some of the characters
        # overlap like oneight ie one and eight then
        digits = re.findall(r"(?=("+'|'.join(stringList)+r"))", lineValue)

        # Now that we have an array of all the digits from the line, convert
        # each individial digit to the according value without impacting the
        # characters of the other valid digits
        for x in digits:
            newValue = str(valueList[stringList.index(x)])
            index = int(digits.index(x))
            digits[index] = newValue

        # Get the first digit and last digit out of the digits array
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
    """ The main with the call to the main function"""

    # Run the funtion
    main()