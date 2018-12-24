#!/usr/bin/env python

#  iterate over the characters in a line and count duplicates and triplicates
def set_match():
  doubleBool = False
  trippleBool = False
  doubles = 0
  tripples = 0
  seen = set()
  doubleSet = set()
  trippleSet = set()
  with open("puzzle_input_02.txt") as f:
    while True:
      c = f.read(1)
      if not c:
        print("End of file")
        break
      #  do all the calculations at the end of each line
      if c == '\n':
        if len(doubleSet) > 0:
          doubleBool = True
        if len(trippleSet) > 0:
          trippleBool = True
        if doubleBool is True:
          doubles += 1
        if trippleBool is True:
          tripples += 1
        doubleSet.clear()
        trippleSet.clear()
        seen.clear()
        trippleBool = False
        doubleBool = False
        continue
      #  no code for removing quad or greater
      #  if c exists in double, add it to tripple and remove it from double
      elif c in doubleSet:
        trippleSet.add(c)
        doubleSet.discard(c)
      #  if c exists in the line already, add it to double
      elif c in seen:
        doubleSet.add(c)
      #  if we have not seen c add it to the set
      else:
        seen.add(c)

  print("doubles ", doubles)
  print("tripples ", tripples)
  print(doubles * tripples)

#  gather our code in a main() function
def main():

  print("Puzzle 2")
  set_match()

#  standard boilerplate to call the main() function
if __name__ == '__main__':
  main()
