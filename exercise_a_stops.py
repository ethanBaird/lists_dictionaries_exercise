stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list

stops.append("Edinburgh Waverley")

#2. Add "Glasgow Queen St" to the start of the list

stops.insert(0, "Glasgow Queen Street")

#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")

# note: list has changed! remember indexes have changed as a result
stops.insert(4, "Polmont")

#4. Print out the index position of "Linlithgow"

print(stops)
print(stops.index("Linlithgow"))

#5. Remove "Livingston" from the list using its name

stops.remove("Linlithgow")
print(stops)

#6. Delete "Cumbernauld" from the list by index

stops.pop(2)
print(stops)

#7. Print the number of stops there are in the list

print(len(stops))

#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop

