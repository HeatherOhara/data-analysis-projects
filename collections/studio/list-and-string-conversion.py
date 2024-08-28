proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.


# Define a function to check for delimiters
def check_delimiters(lst):
    has_comma = any(',' in item for item in lst)
    has_semicolon = any(';' in item for item in lst)
    has_space = any(' ' in item for item in lst)
    return has_comma, has_semicolon, has_space
lists = [proto_list1, proto_list2, proto_list3, proto_list4]
results = {}

for i, lst in enumerate(lists, start=1):
    has_comma, has_semicolon, has_space = check_delimiters(lst)
    results[f"list{i}"] = {
        "contains_comma": has_comma,
        "contains_semicolon": has_semicolon,
        "contains_space": has_space
    }
for list_name, result in results.items():
    print(f"{list_name}:")
    print(f"  Contains comma: {result['contains_comma']}")
    print(f"  Contains semicolon: {result['contains_semicolon']}")
    print(f"  Contains space: {result['contains_space']}")

# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.
# numbers = proto_list1.split(',')
# numbers.reverse()
# reversed_string = ','.join(numbers)
# print("proto_list1", proto_list1)
# print("Reversed_string", reversed_string)
# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
# letters = proto_list2.split(';')
# letters.sort()
# comma_seperated_string = ','.join(letters)
# print("proto_list2", proto_list2)
# print("comma_seperated+_string", comma_seperated_string)


# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.
# words = proto_list3.split(' ')
# words.sort(reverse=True)
# space_seperated_string = ','.join(words)
# print("proto_list3", proto_list3)
# print("space_seperated_string", space_seperated_string)


# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the finawords = proto_list3.split(' ')
Finalwords = proto_list4.split(', ')
Finalwords.sort()
Nospace_seperated_string = ','.join(Finalwords)
print("proto_list4", proto_list4)
print("Nospace_seperated_string", Nospace_seperated_string)