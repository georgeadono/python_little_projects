Exercise 1

Implement a program in Python 3 that reads a text and creates a histogram of the frequency of characters and symbols it contains. At the end, the program should display the character that appeared the most and the corresponding one that appeared the least, along with their respective counts.

The program should ignore whether the characters are lowercase or uppercase and count them uniformly, meaning, for example, the letter 'a' and 'A' should be counted as 'A'.

Example histogram:
A: *********
T: *****
#: **
...
&: ***
Most frequent: A, 9 time(s).
Least frequent: #, 2 time(s).

If the program is executed with a parameter being the name of a text file located in the same directory (see Exercise 9 of Lab04), it should read the contents of the file. Otherwise, it should prompt the user to type the text.

Exercise 2

Implement a program in Python 3 that implements a word-finding game as follows:
From a text file containing words (provided as a sample in the assignment folder, words.txt), randomly select a word. The user should then find this word. For help, the program should display one-third of the letters that make up the word (consider how you would select which positions to display in the word).

Then, the user should propose letters, and the program should fill in the word accordingly, otherwise, it should inform accordingly. The user should have N chances to find a word (define a value or ask for it at the beginning as a difficulty level).

If the user writes a word instead of a character, the program should check if they found it; otherwise, it should decrease the chances by one.

Exercise 3

Implement a program in Python 3 that implements a game between 2 players. The game is played on a 5x5 grid, and the players fill in the cells with O and X, respectively. The aim is for one of the two players to complete a row of five symbols either vertically, horizontally, or diagonally. Players take turns giving coordinates (row, column with a range [1-5]) where they wish to place their symbol. The program should make some checks:
a. If the cell a player wants to place is already occupied,
b. If with their last move a player won,
c. If it reaches a point where neither of the two players can win, it should terminate the game and announce a draw.

Implement at least one function within the above checks.

The program should display the grid (two-dimensional array) after each move.





