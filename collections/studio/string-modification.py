my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
# firstThree = my_string[:3]
# lastthree = my_string[3:]
# NewString = lastthree + firstThree
# print(NewString)

# # Use a template literal to print the original and modified string in a descriptive phrase.
# firstThree = my_string[:3]
# lastthree = my_string[3:]
# NewString = lastthree + firstThree
# print(NewString, 'just looks silly')


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
# numletters = int(input("Enter the number of letters to move:"))
# if numletters>len(my_string):
#     print("Rhe number of letters exceeds the length of the string")

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
# numletters = int(input("Enter the number of letters to move:"))
# if numletters>len(my_string):
#     print("Rhe number of letters exceeds the length of the string")
# elif numletters>0:
#     print(f"ERROR Number of letters cannot be negative, Default to three characters")
#     numletters = 3
# first =  my_string[:numletters]
# last = my_string[numletters:]
# NewString = last + first
# print(f"ModString:'{NewString}' just looks silly. ")

    