# Challenge-362-Intermediate-Java -- Complete!

https://www.reddit.com/r/dailyprogrammer/comments/8n8tog/20180530_challenge_362_intermediate_route/?st=ji3oz32i&sh=de1f57a2

Report:
After drawing out the problem for doing a transposition cipher, I decided to build an algorithm that functions like a car.  

For this to work properly I kept track of all visited x,y positions in a set. Since I wanted to keep track of an ordered pair, I had to write my own IntPair class.  I then implemented my own compare function for HashSet.

The car would change its heading once it reached a visited position or if it was going to run out of the bounds of the array. I then used these positions to cipher the plain text message that was stripped of all unnecessary information using regex.
