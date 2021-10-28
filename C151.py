months = ('January','Feburary','March','April','May','June','July','August','September','October','November','December')

profits = (11000,17000,25000,42000,68000,97000,123000,147000,162000,171000,183000,190000)

maxProfits = max(profits)
maxIndexProfit = profits.index(maxProfits)
print(maxIndexProfit)
indexMonth = months[maxIndexProfit]
print(indexMonth)

print('Maximum Profit was ' + str(maxProfits) + ', in ' + str(indexMonth))

minimumProfits = min(profits)
minIndexProfit = profits.index(minimumProfits)
print(minIndexProfit)
indexMinMonth = months[minIndexProfit]
print(indexMinMonth)

print('Minimum Profit was ' + str(minimumProfits) + ', in ' + str(indexMinMonth))