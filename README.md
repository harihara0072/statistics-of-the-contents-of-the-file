# statistics-of-the-contents-of-the-file

program to request a file name from the user and calculate
the following statistics of the contents of the file:
• Number of lines
• Number of words
• Number of characters
• Average length of a word
In this problem use the following definitions:
A line is a sequence of characters that end with a newline (\n) character
A word bounded by one or more spaces (or \n) on either side of it (or both
sides)
A character is any single length string, e.g. ‘a’, ‘-‘, etc. but not a space (or
white space)

Algorithm:

1. Asking the user to enter a filename and checking if we can open the file or not. If not, then printing the user to enter a proper file name
2. Opening the file in read mode. and saving all the lines in a list where each element is a line.Then length of this list will be number of lines.
3. iterating through the lines list and for each line we will calulate the number of words by splitting it using the split function and also saves the word count and charecter count.
4. Clculating the average charecter per word by using the formulae total charecters/ total words. 

Steps to execute:
Execute the next two cells to run the program.

Expected output:

What is the file name:RobertFrost.txt

Number of lines: 4
Number of words: 27 
Number of characters: 103
Average length of a word: 3.814814814814815
