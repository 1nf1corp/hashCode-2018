print("Pizzaparser")

print "Values:"
pizzaMatrix = []
numberOfRows = 0
numberOfCols = 0
minNumberOfToppings = 0
maxNumberOfTiles = 0

# Create matrix
f = open('sampledata', 'r')
for idx,line in enumerate(f):
    pizzaMatrix.append(line)
f.close()

# Get values
valueLine = pizzaMatrix.pop(0)
valueList = [int(i) for i in valueLine.split()]
print valueList
numberOfRows = valueList[0]
print("numberOfRows " + str(numberOfRows))
numberOfCols = valueList[1]
print("numberOfCols " + str(numberOfCols))
minNumberOfToppings = valueList[2]
print("minNumberOfToppings " + str(minNumberOfToppings))
maxNumberOfTiles = valueList[3]
print("maxNumberOfTiles " + str(maxNumberOfTiles))

# Print pizza
print "Pizza:"
print(pizzaMatrix)
for row in pizzaMatrix:
	print(row),