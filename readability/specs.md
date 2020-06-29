# Readability

Prompt and test cases taken from [CS50x](https://www.edx.org/course/cs50s-introduction-to-computer-science) problem set 6.

## Requirements
- Write a program that first asks the user to type in some text, and then outputs the grade level for the text, according to the Coleman-Liau formula, exactly as you did in Problem Set 2, except that your program this time should be written in Python.
    - Recall that the Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8, where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.
- Your program should count the number of letters, words, and sentences in the text. You may assume that a letter is any lowercase character from a to z or any uppercase character from A to Z, any sequence of characters separated by spaces should count as a word, and that any occurrence of a period, exclamation point, or question mark indicates the end of a sentence.
- Your program should print as output "Grade X" where X is the grade level computed by the Coleman-Liau formula, rounded to the nearest integer.
- If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level), your program should output "Grade 16+" instead of giving the exact index number. If the index number is less than 1, your program should output "Before Grade 1".

Your program should behave per the example below:

`$ python readability.py  
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!  
Grade 3`

## Manual Test Cases
- Input: `One fish. Two fish. Red fish. Blue fish.` Expected Output: `Before Grade 1.`
- Input: `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` Expected Output: `Grade 2.`
- Input: `Congratulations! Today is your day. You're off to Great Places! You're off and away!` Expected Output: `Grade 3.`
- Input: `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.` Expected Output: `Grade 5.`
- Input: `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` Expected Output: `Grade 7.`
- Input: `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"` Expected Output: `Grade 8.`
- Input: `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.` Expected Output: `Grade 8.`
- Input: `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.` Expected Output: `Grade 9.`
- Input: `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.` Expected Output: `Grade 10.`
- Input: `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` Expected Output: `Grade 16+.`