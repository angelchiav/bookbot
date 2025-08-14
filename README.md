# BookBot 
BookBot is a simple tool that analyzes text books and provides statistics about the content.
## What does it do?
BookBot reads a text file and shows you:
- **Word count**: How many words there are in total
- **Character count**: Frequency of each letter of the alphabet (sorted from highest to lowest)
## Installation
1. Clone or download this repository
2. Make sure you have Python 3 installed
3. No additional dependencies required
## Usage
```bash
python3 main.py <path_to_text_file>
```
### Example:
```bash
python3 main.py books/frankenstein.txt
```
## Project structure
```
bookbot/
├── main.py        # Main file
├── stats.py       # Analysis functions
├── books/         # Directory for your books (gitignored)
└── README.md
```
## Sample output
```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 77986 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24367
s: 21155
h: 19725
...
============= END ===============
```
## Notes
- Only analyzes alphabetic characters (ignores numbers and symbols)
- Analysis is case-insensitive
- Place your text files in the `books/` directory to keep the project organized
