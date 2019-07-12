# AlgoExpert

## Very Hard

### Iterative In-order Traversal - Very Hard 1
Write a function that takes in a Binary Tree and traverses it using the in-order traversal technique but without using recursion. 

As the tree is being traversed, a callback function passed in as an argument to the main function should be called on each node (i.e. callback(currentNode)). 

Each Binary Tree node has a value stored in a property called "value," a parent node in a property called "parent," and two children nodes stored in properties called "left" and "right," respectively. 

Children nodes can either be Binary Tree nodes themselves or the None (null) value.

Sample input:
```
    1
   / \
   2 3
  /  /\
  4  6 7
  \
  9
```
Sample output:
```
callback(4)
callback(9)
callback(2)
callback(1)
callback(6)
callback(3)
callback(7)
```

### Max Profit With K Transactions - Very Hard 2
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
### Palindrome Partitioning Min Cuts - Very Hard 3
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
### Knuth—Morris—Pratt Algorithm - Very Hard 4
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
### LRU Cache - Very Hard 5
Implement a class for a Least Recently Used (LRU) Cache. The cache should support inserting key / value pairs (the insertKeyValuePair() method), retrieving a key's value (the getValueFromKey() method), and retrieving the most recently "active" key (the getMostRecentKey() method); each of these methods should run in constant time. 

When a key / value pair is inserted or a key's value is retrieved, the key in question should become the most recent key. 

Also, the LRUCache class should store a maxSize property set to the size of the cache, which is passed in as an argument during instantiation. 

This size represents the maximum number of key / value pairs that the cache can hold at once. 

If a key / value pair is added to the cache when it has reached maximum capacity, the least recently used ("active") key / value pair should be evicted from the cache and no longer retrievable; the newly added key / value pair should effectively replace it. 

Inserting a key / value pair with an already existing key should simply replace the key's value in the cache with the new value and should not evict a key / value pair if the cache is full. 

Attempting to retrieve a value from a key that is not in the cache should return the None (null) value.

Sample input: (for an LRU Cache of size 3)
```
insertKeyValuePair("a",1)
insertKeyValuePair("b",2)
insertKeyValuePair("c",3)
getMostRecentKey()
getValueFromKey("a")
getMostRecentKey()
insertKeyValuePair("d",4)
getValueFromKey("b")
insertKeyValuePair("a",5)
getValueFromKey("a")
```
Sample output:
```
-
-
-
"c"
1
"a"
-
None
-
5
```