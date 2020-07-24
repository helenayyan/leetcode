# Dynamic Programming

Dynamic programming is a method which solves problems by combining the solutions to subproblems. We typically apply this method to optimization problems and when the subproblems overlap to avoid recomputing the answer. 

## Steps

- Define the state of the optimal solution
- Define the state transition function
- Initialization of the table
- recursively define the value of solutions for each subproblems
- Construct the optimal solution from the computed tabular solutions

## Recursive Manners

- **Top-down implementation**:

  Memoization (recording a value for later look-up), result for each subproblem usually stored in an array or hash table.

- **Bottom-up method (recommanded for most DP problems):**

  Sovle the smaller problems whose result is required when computing larger subproblems.

## DP Models

### Linear DP

#### Example Question:

[Leetcode 0120 - Triangle](https://leetcode.com/problems/triangle/)
> Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
>
> For example, given the following triangle:
>
>[
>      [2],
>     [3,4],
>    [6,5,7],
>   [4,1,8,3]
> ]
> The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

##### Top-down method：
**Step 1: Define the state**
`dp[i][j]` is the path sum from top to `triangle[i][j]`.

**Step 2: Define the state transition function**
The optimal result for subproblem, minimum path sum to the current position, can be calculated as follow
`dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]`

**Step 3: Initialization of the table**
Top: `dp[0][0] = triangle[0][0]`
Left Edge: `dp[i][0] = dp[i - 1][0] + triangle[i][0]`
Right Edge: `dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]`

**Step 4: Recursion range**
For each level, recurse within the range(1, i) to avoid boarder exception.

**Step 5: Construct optimal solution**
