# Sudoku 

## Overview
This script allows for any sudoku puzzle to be solved using an almost human-like approach first before using the traditional backtracking approach to finish the puzzle allowing it to be in the 85th percentile of all solutions on [Leetcode](https://leetcode.com/problems/sudoku-solver/submissions/902197912/) in terms of runtime.  

Time Complexity = `O(n^2)` for Part 1 and `O(9^m)` for Part 2 where `m` is the number of empty cells left

<p>&nbsp;</p>

### Part 1 - The Human Like Approach
The way I approached this problem was to think back on how I used to solve sudoku as a kid. I was taught to first identify all the possible numbers that can go into the empty squares and from there fill in squares that can only hold one number.  

As a result, I first started by creating two lists  `columns` and `boxes` and using a simple `for` and `while` loop respectively, ordered the sudoku puzzle into the respective lists. 

From there I created an `empty_cells` dictionary and iterated through the board finding empty cells and checking the cell with the row, column and box it was in and finding all possible values the cell could have. It was them appended to the dictionary with the key being the position of the empty cell in the format `row_num col_num box_num` and the value being a list of all possible values the empty cell could have.

The following function `one_value` thereafter iterated through the `empty_cells` dictionary, finding cells which can only hold one possible value. Since the key of the empty cell is based on the location of the cell in the board, the board as well as the `columns` and `boxes` lists can be updated rather easily.  
The  function proceeds to update the `empty_cells` dictionary. This is as once an empty cell is filled in, it is not possible for the other empty cells in the same row, column or box to have the same number. Hence, the possible values of each affected empty cell needs to be updated. 

Subsequently, a check is done to see whether or not empty cells exist with only one possible value and if that is the case, the `one_value` function is called again.

<p>&nbsp;</p>

### Part 2 - Brute Force
A list `remaining_cells` is created from the `empty_cells` dictionary to hold all the locations of the empty cells which will be used later.

After Part 1, the remaining empty cells all should have two or more possible values.  
Hence it is not possible to continue using the same method as before. Although I did spend a considerable amount of time researching how professional sudoku solvers solve such puzzles, advance techiques such as `The X-Wing` and `The Swordfish` seemed too reliant on finding patterns that do not rely on a strict set of instructions which makes it hard to code.  
Therefore, I decided to brute force the rest of the puzzle.

This method utlizes two function, a main function `brute` which guesses numbers in empty cells and a helper function `valid` which checks the guess against the row, column and box the empty cell is in to ensure that the cell can hold the guess.  
To make the solution more efficient and to prevent the `brute` function from iterating through the whole board, the `brute` function takes in a `pointer` variable that points to the `remaining_cells` which allows it to guess immediately and not have to find empty cells.

<p>&nbsp;</p>

### Time and Space Complexity
I would just like to preface this by saying that I am in no means good at analyzing the time and space complexities of a given algorithm but given my limited understanding I thought I would give it a try for the sake of learning. For this algorithm, I am not really sure of how to even begin estimating the space complexity as there are simply too many variables used.  
As such please feel free to correct me or even provide me with more insight as to how I can improve. Any help is greatly appreaciated. Thank you :) 

<p>&nbsp;</p>

#### Part 1
As there are two areas where the algorithm iterates through the board (firstly to find `columns` and `boxes` and secondly to find `empty_cells`) in a nested `for` loop, I belive the total time complexity would be `n^2 + n^2 = 2n^2` which in Big O notation would simply be `O(n^2)`. 

#### Part 2
As this part is a brute force solution, and the function iterates through each possible value the empty cell could have from 1-9, I believe the time complexity to be `O(9^m)` where `m` is the number of empty cells remaining after Part 1. Upon further research, I learned that a general Sudoku solution is generally thought to be `NP complete` as the solution to a sudoku puzzle can be easily verified and a brute force algorithm can rather easily find the solution by trying all possible solutions.


<p>&nbsp;</p>
 
## Things to Improve
- Find a solution without brute forcing
    - Be smarter with guesses (eg. Guessing empty cells with only two possible values)
    - Trying to implement some of the more advanced sudoku methods that sudoku players use in real life
