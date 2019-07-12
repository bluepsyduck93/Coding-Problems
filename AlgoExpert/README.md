# AlgoExpert

## Iterative In-order Traversal - Very Hard 1
Write a function that takes in a Binary Tree and traverses it using the in-order traversal technique but without using recursion. 

As the tree is being traversed, a callback function passed in as an argument to the main function should be called on each node (i.e. callback(currentNode)). 

Each Binary Tree node has a value stored in a property called "value," a parent node in a property called "parent," and two children nodes stored in properties called "left" and "right," respectively. 

Children nodes can either be Binary Tree nodes themselves or the None (null) value.

Sample Input:
```
    1
   / \
   2 3
  /  /\
  4  6 7
  \
  9
```
Sample Output:
```
callback(4)
callback(9)
callback(2)
callback(1)
callback(6)
callback(3)
callback(7)
```

## Max Profit With K Transactions - Very Hard 2
You are given an array of integers representing the prices of a single stock on various days (each index in the array represents a different day). 

You are also given an integer k, which represents the number of transactions you are allowed to make. One transaction consists of buying the stock on a given day and selling it on another, later day. 

Write a function that returns the maximum profit that you can make buying and selling the stock, given k transactions. 

Note that you can only hold 1 share of the stock at a time; in other words, you cannot buy more than 1 share of the stock on any given day, and you cannot buy a share of the stock if you are still holding another share.

Sample input: 
```
[5, 11, 3, 50, 60, 90], 2
```
Sample output: 
```
93 (Buy: 5, Sell: 11; Buy: 3, Sell: 90)
```
## Palindrome Partitioning Min Cuts - Very Hard 3
Given a non-empty string, write a function that returns the minimum number of cuts needed to perform on the string such that each remaining substring is a palindrome. 

A palindrome is defined as a string that is written the same forward as backward. Note that single-character strings are palindromes.

Sample input: 
```
"noonabbad"
```
Sample output: 
```
2 ("noon | abba | d")
```
## Knuth—Morris—Pratt Algorithm - Very Hard 4
Write a function that takes in two strings and checks if the first string contains the second one using the Knuth—Morris—Pratt algorithm. 

The function should return a boolean.

Sample input: 
```
"aefoaefcdaefcdaed", "aefcdaed"
```
Sample output: 
```
true
```
