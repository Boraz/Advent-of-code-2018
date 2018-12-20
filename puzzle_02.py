#!/usr/bin/env python

def populateArray():
  with open("puzzle_input.txt", "r") as e:
    frequencyList = []
    for line in e:
      frequencyList.append(int(line))
  print(sum(frequencyList))

def sol_p2():
    with open("puzzle_input.txt", "r") as f:
      lines = [int(x) for x in f.readlines()]
    freq = 0
    index = 0
    seen = set()
    while freq not in seen:
      seen.add(freq)
      freq += lines[index % len(lines)]
      index += 1
    return freq, index

def Rabin_Karp():
  double = false
  doubles = 0

  tripple = false
  tripples = 0

  seen = set()
  with open("puzzle_input_02.txt", "r") as f:
    lines = [int(x) for x in f.read()]
  while letter not in seen:
      seen.add()
      if letter in set:
        if double is true:
          tripple = true
          double = false
      if double:
        doubles += 1
        double = false
      if tripple:
        tripples += 1
        tripple = false
  print(doubles * tripples)


# Gather our code in a main() function
def main():

  print("Puzzle 2")

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
