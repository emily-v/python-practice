# DNA

Prompt and test cases taken from [CS50x](https://www.edx.org/course/cs50s-introduction-to-computer-science) problem set 6.

## Requirements
- The program should require as its first command-line argument the name of a CSV file containing the STR counts for a list of individuals and should require as its second command-line argument the name of a text file containing the DNA sequence to identify.
    - If your program is executed with the incorrect number of command-line arguments, your program should print an error message of your choice (with print). If the correct number of arguments are provided, you may assume that the first argument is indeed the filename of a valid CSV file, and that the second argument is the filename of a valid text file.
- Your program should open the CSV file and read its contents into memory.
    - You may assume that the first row of the CSV file will be the column names. The first column will be the word name and the remaining columns will be the STR sequences themselves.
- Your program should open the DNA sequence and read its contents into memory.
- For each of the STRs (from the first line of the CSV file), your program should compute the longest run of consecutive repeats of the STR in the DNA sequence to identify.
- If the STR counts match exactly with any of the individuals in the CSV file, your program should print out the name of the matching individual.
    - You may assume that the STR counts will not match more than one individual.
    - If the STR counts do not match exactly with any of the individuals in the CSV file, your program should print "No match".

Your program should behave per the example below:

`$ python dna.py databases/large.csv sequences/5.txt`  
`Lavender`

## Manual Test Cases
- Run your program as python `dna.py databases/small.csv sequences/1.txt.` Your program should output `Bob`.
- Run your program as python `dna.py databases/small.csv sequences/2.txt.` Your program should output `No match`.
- Run your program as python `dna.py databases/small.csv sequences/3.txt.` Your program should output `No match`.
- Run your program as python `dna.py databases/small.csv sequences/4.txt.` Your program should output `Alice`.
- Run your program as python `dna.py databases/large.csv sequences/5.txt.` Your program should output `Lavender`.
- Run your program as python `dna.py databases/large.csv sequences/6.txt.` Your program should output `Luna`.
- Run your program as python `dna.py databases/large.csv sequences/7.txt.` Your program should output `Ron``.
- Run your program as python `dna.py databases/large.csv sequences/8.txt.` Your program should output `Ginny`.
- Run your program as python `dna.py databases/large.csv sequences/9.txt.` Your program should output `Draco`.
- Run your program as python `dna.py databases/large.csv sequences/10.txt.` Your program should output `Albus`.
- Run your program as python `dna.py databases/large.csv sequences/11.txt.` Your program should output `Hermione`.
- Run your program as python `dna.py databases/large.csv sequences/12.txt.` Your program should output `Lily`.
- Run your program as python `dna.py databases/large.csv sequences/13.txt.` Your program should output `No match`.
- Run your program as python `dna.py databases/large.csv sequences/14.txt.` Your program should output `Severus`.
- Run your program as python `dna.py databases/large.csv sequences/15.txt.` Your program should output `Sirius`.
- Run your program as python `dna.py databases/large.csv sequences/16.txt.` Your program should output `No match`.
- Run your program as python `dna.py databases/large.csv sequences/17.txt.` Your program should output `Harry`.
- Run your program as python `dna.py databases/large.csv sequences/18.txt.` Your program should output `No match`.
- Run your program as python `dna.py databases/large.csv sequences/19.txt.` Your program should output `Fred`.
- Run your program as python `dna.py databases/large.csv sequences/20.txt.` Your program should output `No match`.
