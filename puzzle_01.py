frequencyArray = []

def main():
  with open("puzzle_input.txt", "r") as puzzle_input:
	frequencyArray = []
	for line in puzzle_input:
  	frequencyArray.append(int(line))
  print(sum(frequencyArray))

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()
