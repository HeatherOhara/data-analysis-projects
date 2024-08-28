# Create the adding_practice list with the following entry: 273.15
# adding_pracice = [273.15]

# Use the append method to add the number 42 and the string "hello" to the list. Add these new items one at a time.  Print the list after each step to confirm the changes.
# adding_pracice.append(42)
# adding_pracice.append("hello")
# print(adding_pracice)
# Use list concatenation to add these three items to the list all at once: [False, -4.6, '87'].
# adding_pracice += [False, -4.6, '87']
# print(adding_pracice)
# Use the cargo_hold list for the next set of exercises.
cargo_hold = ['oxygen tanks', 'space suits', 'parrot', 'instruction manual', 'meal packs', 'slinky', 'security blanket']

# Use bracket notation to replace 'slinky' in the list with 'space tether'. Print the list to confirm the change.
# List = ['oxygen tanks', 'space suits', 'parrot', 'instruction manual', 'meal packs', 'slinky', 'security blanket']
# List[5] = 'Space tether'
# print(List)

# Remove the last item from the list with pop. Print the element removed and the updated list.
# item = cargo_hold.pop()
# print(item)
# print(cargo_hold)

# Remove the first item from the list with pop. Print the element removed and the updated list.
# item = cargo_hold.pop(0)
# print(item)
# print(cargo_hold)

# append and insert require arguments inside the (). Add the items 1138 and ‘20 meters’ to the the list - the number at the start and the string at the end. Print the updated list to confirm the changes.
# cargo_hold.insert(0,1138)
# cargo_hold.append('20 meters')
# print(cargo_hold)

# Use the remove method to take the parrot out of cargo_hold, then print the updated list.
# cargo_hold.remove('parrot')
# print(cargo_hold)

# Use .format() to print the final list and its length. "The list ___ contains ___ items."
list_length = len(cargo_hold)
print("The List{} contains{} items".format(cargo_hold, list_length))