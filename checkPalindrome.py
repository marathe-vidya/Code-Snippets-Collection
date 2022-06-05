def isPalindrome(string: str, start: int, end: int):
    # Returns True if String is Palindrome

    while start < end:
        if string[start] != string[end]:
            return False
        start += 1      # Move +1 element from left
        end -= 1        # Move -1 element from right
    return True

def getAllParts(partitions: list, current: list, start: int, n: int, string: str):
    # Gets all palindrome partitions.

    if start >= n:
        listCopy = current.copy()       # Making local copy of current list passed by ref.
        partitions.append(listCopy)
        return

    for i in range(start, n):
        if isPalindrome(string, start, i):
            current.append(string[start:i + 1])
            getAllParts(partitions, current, i + 1, n, string)   # Recursive call
            current.pop()

def prettyPrint(elements:str, actualString:str):

    # The desired output contains capital letters to..
    # We had considered lowercase alphabets for palindrome comparisons (as per the question)

    for elem in elements:
        if isPalindrome(elem, 0, len(elem)-1):
            index = 0
            element = ""
            for char in elem :
                if char != " ":
                    element += actualString[index]
                    index += 1
                else:
                    element += char
            print(element)

def palindromePartitions(string: str):

    partitions = []      # List of all possible partitions
    current = []         # Current partition

    #Recursive call to get all partitions
    getAllParts(partitions, current, 0, len(string), string.lower())

    # Getting required strings from partition lists.
    elements = []
    for i in range(len(partitions)):
        element = ""
        for j in range(len(partitions[i])):
            element += partitions[i][j]
            element += " "
        elements.append(element[:-1])

    # Pretty print to get output in required format.
    prettyPrint(elements, string)

#----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    string = "BorrowOrRob"       # String for partition
    palindromePartitions(string)

