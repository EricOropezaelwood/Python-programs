# Eric Oropezaelwood
# 26 Aug 2015
# Assignment #1 Part1
# Calculate the U.S. population in one year taking into account
# births/deaths/immigrants.

uspop = 318892103
secsinyear = (60*60*24*365)
# seconds in minute * minutes in hour * hours in day * days in year

births = (secsinyear/8)
deaths = (secsinyear/13)
immigrants = (secsinyear/40)

uspop = (uspop + births - deaths + immigrants)
uspop = round(uspop, 0)

print("The population will be ", int(uspop))
