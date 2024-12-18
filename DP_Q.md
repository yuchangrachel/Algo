### Greedy
45. Jump Game II
55. Jump Game
605. Can Place Flowers


### Template
Pseducode
create dp list, size (+1 or not)
base dp case dp[0] dp[1]
return dp[-1]

Think:
Goal: max/min/ways of combinations
Choice: 1step/2step, +/-, true/false
Rule: how to handle dp[i]


### When use DP
Ask accumulated wayss for combination
Ask max/min accumulated profit for many combinations(ways, add)
Ask if can get result from combination
choices + optimal substructure + overlap subproblems


### DP 1D
70. Climbing Stairs
198. House Robber
714. Best Time to Buy and Sell Stock with Transaction Fee
746. Min Cost Climbing Stairs
### DP 1D Bottom-Up 
start from base case
139. Word Break
300. Longest Increasing Subsequence
322. Coin Change
1137. N-th Tribonacci Number
### DP top-down memorization/recursion
63. Unique Paths II (dfs memo)
494. Target Sum


### DP 2D
#### bottomup
62. Unique Paths
64. Minimum Path Sum
1143. Longest Common Subsequence
#### memorization
def dfs return memo[i][j]
72. Edit Distance


### Tricky DP
790. Domino and Tromino Tiling