flavors = {
  'chocolate' : 0.35,
  'vanilla' : 0.35,
  'strawberry' : 0.42,
  'cookies and cream' : 0.45,
  'mint chocolate chip' : 0.42,
  'fudge chunk' : 0.45,
  'saffron' : 2.25,
  'garlic' : 0.05
}

## Set a variable called choice to the flavor you want to search for.
# flavors['choice'] = 'cookies and cream'
## Use an if statement to check if choice is in the flavors dictionary.
# if 'choice' in flavors:
#   print("Key 'choice' is in the dictionary")
# else:
#   print("Key'choice' is not in the dictionary")
## If it is, set another variable called cost to the value associated with choice.
flavors['cost'] = 0.45

## If it isn’t, set cost to 0.

## Print the cost.
# if 'choice' in flavors:
#     print("Key 'choice'  is in dictionary")
#     cost = flavors['cost']
# print('cost', cost)
### Search a Dictionary Part 2:

## Initialize two variables: highest_cost to 0 and fanciest to an empty string.
highest_cost = 0.0
fanciest = ''
## Loop through the flavors dictionary using a for loop.
# for key, value in flavors.items():
#     print(f"Key: {key}, value: {value}")
## For each flavor, check if its price is higher than highest_cost.
# for flavor, cost in flavors.items():
#     if cost > highest_cost:
#         highest_cost = cost
#         fanciest = flavor
# print(flavors)
## If it is, update fanciest to this flavor and highest_cost to its price.
for flavor, cost in flavors.items():
    if cost > highest_cost:
        highest_cost = cost
        fanciest = flavor
flavors['highest_cost'] = highest_cost
flavors['fanciest'] = fanciest
print(flavors)

## After the loop, print the most expensive flavor.
