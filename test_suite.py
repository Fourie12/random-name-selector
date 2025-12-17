#!/usr/bin/env python3
"""
Test suite for the random name selector program.
Tests the distribution of random selections over multiple runs.
"""

import sys
import subprocess
from collections import Counter


def run_selection(filepath, num_runs):
	"""
	Run the name selector multiple times and collect results.
	
	Args:
		filepath: Path to the file with names
		num_runs: Number of times to run the selector
		
	Returns:
		Counter: Dictionary with name counts
	"""
	results = []
	
	for i in range(num_runs):
		try:
			# Run the main program as a subprocess
			result = subprocess.run(
				['python3', 'rns.py', filepath],
				capture_output=True,
				text=True,
				timeout=10
			)
			
			if result.returncode == 0:
				name = result.stdout.strip()
				results.append(name)
				print(f"Run {i+1}/{num_runs}: {name}")
			else:
				print(f"Error on run {i+1}: {result.stderr}")
				
		except subprocess.TimeoutExpired:
			print(f"Run {i+1} timed out")
		except Exception as e:
			print(f"Error on run {i+1}: {e}")
	
	return Counter(results)


def display_statistics(counts, num_runs):
	"""
	Display statistics about the name selection distribution.
	
	Args:
		counts: Counter object with name frequencies
		num_runs: Total number of runs
	"""
	print("\n" + "="*60)
	print("DISTRIBUTION STATISTICS")
	print("="*60)
	print(f"Total runs: {num_runs}")
	print(f"Successful runs: {sum(counts.values())}")
	print()
	
	# Sort by count (descending) then by name
	sorted_names = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
	
	print(f"{'Name':<30} {'Count':<10} {'Percentage':<10}")
	print("-"*60)
	
	for name, count in sorted_names:
		percentage = (count / num_runs) * 100
		print(f"{name:<30} {count:<10} {percentage:.2f}%")
	
	print("-"*60)
	
	# Calculate expected percentage (assuming equal distribution)
	if len(counts) > 0:
		expected_pct = 100 / len(counts)
		print(f"\nExpected percentage per name (equal distribution): {expected_pct:.2f}%")
		
		# Calculate chi-square-like deviation
		print("\nDeviation from expected:")
		for name, count in sorted_names:
			actual_pct = (count / num_runs) * 100
			deviation = actual_pct - expected_pct
			print(f"{name:<30} {deviation:+.2f}%")


def main():
	"""Main test function."""
	if len(sys.argv) != 3:
		print("Usage: python test_suite.py <filename> <num_runs>")
		print("Example: python test_suite.py names.txt 100")
		sys.exit(1)
	
	filepath = sys.argv[1]
	
	try:
		num_runs = int(sys.argv[2])
		if num_runs <= 0:
			print("Error: Number of runs must be positive")
			sys.exit(1)
	except ValueError:
		print("Error: Number of runs must be an integer")
		sys.exit(1)
	
	print(f"Testing random name selector with {num_runs} runs...\n")
	
	# Run the tests
	counts = run_selection(filepath, num_runs)
	
	# Display results
	display_statistics(counts, num_runs)


if __name__ == "__main__":
	main()
