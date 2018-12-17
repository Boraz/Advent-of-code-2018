
def main():
  with open("puzzle_input.txt", "r") as e:
    frequencyList = []
    for line in e:
      frequencyList.append(int(line))
  print(sum(frequencyList))

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()
