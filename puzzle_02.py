#!/usr/bin/env python

frequencyArray = []
countArray = []
compairArray = []
count = 0

def populateArray():
  with open("puzzle_input.txt", "r") as puzzle_input:
	for line in puzzle_input:
  	frequencyArray.append(int(line))
  print(sum(frequencyArray))

def calculateFrequency():
  for i in frequencyArray:
	global count
	count += i
	countArray.append(count)
	compairArray.append(count)

def calibrateFrequency():
  set(countArray) & set(compairArray)


# Gather our code in a main() function
def main():
  print("Puzzle 1"), populateArray()
  print("Puzzle 2"), calculateFrequency()
  compairArray.pop(0)
  print(sum(countArray))
  print(sum(compairArray))
  calculateFrequency()
  print(sum(countArray))
  print(sum(compairArray))

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()
