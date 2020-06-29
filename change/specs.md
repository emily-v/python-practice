# Change

Prompt and test cases taken from [CS50x](https://www.edx.org/course/cs50s-introduction-to-computer-science) problem set 6.

## Requirements
- Write a program that first asks the user how much change is owed and then spits out the minimum number of coins with which said change can be made.
- Assume that the only coins available are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢).
- If the user fails to provide a non-negative value, your program should re-prompt the user for a valid amount again and again until the user complies.

Your program should behave per the example below:

`$ python change.py`  
`Change owed: 0.41`  
`4`

## Manual Test Cases
- Input: `0.41` Expected Output: `4`
- Input: `1.60` Expected Output: `7`
- Input: `23` Expected Output: `92`
- Input: `-1` Expected Output: n/a - program re-prompts for valid input.
