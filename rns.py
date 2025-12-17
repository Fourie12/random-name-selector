#!/usr/bin/env python3
"""
This program will take in a file with a bunch of names in them and then using a random number and mod string, it will give one of those names back
It will use true random numbers
"""
import sys
import requests

def read_file(filepath):
	"""
	Read and return the contents of a file.
	
	Args:
		filepath: Path to the file to read
		
	Returns:
		str: Contents of the file
		
	Raises:
		FileNotFoundError: If the file doesn't exist
		IOError: If there's an error reading the file
	"""
	try:
		with open(filepath, 'r', encoding='utf-8') as f:
			return f.read()
	except FileNotFoundError:
		print(f"Error: File '{filepath}' not found.")
		sys.exit(1)
	except IOError as e:
		print(f"Error reading file: {e}")
		sys.exit(1)

def select_random(all_names):
	names_arr = all_names.split('\n')
	url = "https://www.random.org/integers/?num=1&min=1&max=100&col=1&base=10&format=plain&rnd=new"
	response = requests.get(url)
	rand = int(response.text.strip())
	selected = rand%(len(names_arr) - 1)
	return(names_arr[selected])

def main():
	"""Main function to orchestrate the program."""
	# Check if filename was provided as command-line argument
	if len(sys.argv) != 2:
		print("Usage: python rns.py <filename>")
		sys.exit(1)
	
	filepath = sys.argv[1]
	
	# Read and print file contents
	all_names = read_file(filepath)
	name = select_random(all_names)
	print(name)


if __name__ == "__main__":
	main()
