# Day 4
## Part 1
I essentially compared the actual numbers found in the ids. I would compare the starting and ending numbers with the other ID and determine if it fell within the bounds of the ID. 
This is easier than creating strings to represent the ranges and then checking if at least one of the strings was in the other.

## Part 2
Before I start, I know that there was a way to do this by comparing numbers again. Instead, I chose to use lists because I found it fun to play with them.

I used the same variables from part 1 because it was easy to copy and paste those. I used list comprehension to add all of the numbers in the range of numbers to a list. Then I used the 
```any``` keyword to check if there were any elements from the first ID contained within the second ID.