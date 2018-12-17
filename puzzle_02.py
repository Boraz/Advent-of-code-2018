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

# Gather our code in a main() function
def main():

  print("Puzzle 1")
  populateArray()

  print("Puzzle 2")
  print("Result found: {0} at iteration {1}".format(*sol_p2()))
  

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
