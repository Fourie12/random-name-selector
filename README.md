# Random Name Selector

A Python program that randomly selects a name from a file using truly random numbers from Random.org.

## Description

This program reads a list of names from a text file (one name per line) and uses a true random number generator to select one name. Unlike pseudo-random number generators, this uses Random.org's atmospheric noise-based randomness for genuine unpredictability.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone or download this repository
2. Install the required dependency:

```bash
pip install requests
```

## Usage

### Running the Name Selector

```bash
python rns.py <filename>
```

**Example:**
```bash
python rns.py names.txt
```

### Input File Format

Create a text file with one name per line:

```
Alice
Bob
Charlie
David
```

### Running the Test Suite

To test the distribution of random selections:

```bash
python test_suite.py <filename> <num_runs>
```

**Example:**
```bash
python test_suite.py names.txt 100
```

This will run the selector 100 times and display statistics showing how many times each name was selected.

## Files

- `rns.py` - Main program that selects a random name
- `test_suite.py` - Test suite for analyzing selection distribution
- `names.txt` - Example input file (create your own)

## How It Works

1. Reads all names from the specified file
2. Fetches a true random number from Random.org (1-100)
3. Uses modulo operation to map the random number to a name index
4. Returns the selected name

## Example Output

```bash
$ python rns.py names.txt
Charlie
```

## Test Suite Output Example

```
============================================================
DISTRIBUTION STATISTICS
============================================================
Total runs: 100
Successful runs: 100

Name                           Count      Percentage
------------------------------------------------------------
Alice                          28         28.00%
Bob                            26         26.00%
Charlie                        24         24.00%
David                          22         22.00%
------------------------------------------------------------

Expected percentage per name (equal distribution): 25.00%
```

## Notes

- Requires internet connection to access Random.org API
- Each API call may take 1-2 seconds
- Random.org has rate limits for free usage
- For offline use, consider switching to Python's built-in `random` module (pseudo-random)

## License

Free to use and modify.

## Contributing

Feel free to submit issues or pull requests for improvements!
