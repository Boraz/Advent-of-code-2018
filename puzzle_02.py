#!/usr/bin/env python

# Iterate over the characters in a line and count duplicates and triplicates
def set_match():
  double = False
  doubles = 0
  tripple = False
  tripples = 0
  seen = set()
  with open("puzzle_input_02.txt") as f:
    while True:
      c = f.read(1)
      if not c:
        print("End of file")
        break
      while c not in seen:
        if c == '\n':
          break
        seen.add(c)
      #if letter in set:
       # if double is True:
        #  tripple = True
         # double = False
      #if double:
       # doubles += 1
        #double = False
      #if tripple:
       # tripples += 1
        #tripple = False
  #print(doubles * tripples)
  print(seen)


# Gather our code in a main() function
def main():

  print("Puzzle 2")
  set_match()

# Standard boilerplate to call the main() function
if __name__ == '__main__':
  main()
