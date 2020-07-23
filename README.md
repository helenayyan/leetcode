# LeetCode
 This is a place to store and categorize all the past coding practices, mainly leetcode practice. 

###### User name: yy452
***
## Navigator
- [My Personal Blog](#my-personal-blog)
- [Useful Resources](#useful-resources)
- [My Coding Challenge Diary (2020)](#my-coding-challenge-diary--2020)
- [Coding Style](#coding-style)
- [Questions by Category](#questions-by-category)
  * [Array](#array)
  * [Binary Search](#binary-search)
    + [General solutions for binary search:](#general-solutions-for-binary-search)
  * [Binary Search Tree](#binary-search-tree)
  * [Graph](#graph)
  * [Hash Table](#hash-table)
  * [Linked List](#linked-list)
  * [Math](#math)
  * [Stack](#stack)
  * [String](#string)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>
***
## My Personal Blog
####[helenayy.tech](http://helenayy.tech)
Welcome to visit my personal blog page. You can find my documentations of data structures and other interesting articles onto it. :)

***
## Useful Resources
- [Leetcode 常见题型代码模版](https://blog.csdn.net/fuxuemingzhu/article/details/101900729)
 （整理的非常细致的一些可以通用的算法框架，可以适当背下来。）
***
## My Coding Challenge Diary (2020)

| Date       | Title        |
| ------------- |:-------------|
| 04/05/2020 | [0098 Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
| 06/05/2020 | [0572 Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)
| 09/05/2020 | [0069 Square root of x](https://leetcode.com/problems/sqrtx/)
| 10/05/2020 | [0236 Lowest Common Ancestor of A Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
| 11/05/2020 | [0050 Pow(x, n) ](https://leetcode.com/problems/powx-n/)
| 12/05/2020 | [0155 Min Stack](https://leetcode.com/problems/min-stack/)
| 13/05/2020 | [0102 Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
| 10/06/2020 | [0009 Palindrome Number](https://leetcode.com/problems/palindrome-number/)
| 11/06/2020 | [0739 Daily Temperatures](https://leetcode.com/problems/daily_temperatures/)
| 12/06/2020 | [0015 3Sum](https://leetcode.com/problems/3sum/)
| 16/06/2020 | [0297 Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
| 17/06/2020 | [1014 Best Sightseeing Pair ](https://leetcode.com/problems/best-sightseeing-pair/)
| 18/06/2020 | [1028 Recover a Tree from Preorder Traversal](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/)
| 21/06/2020 | [0124 Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
| 01/07/2020 | [0718 Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)
| 02/07/2020 | [0378 kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
| 03/07/2020 | [0108 Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
| 04/07/2020 | [0032 Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)
| 08/07/2020 | [0112 Path Sum](https://leetcode.com/problems/path-sum/)
| 10/07/2020 | [0309 Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
| 11/07/2020 | [0315 Count of Smaller Numbers after Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
| 12/07/2020 | [0174 Dungeon Game](https://leetcode.com/problems/dungeon-game/)
| 13/07/2020 | [0350 Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)
| 14/07/2020 | [0120 Triangle](https://leetcode.com/problems/triangle/)
| 15/07/2020 | [0096 Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/)
| 16/07/2020 | [0785 Is Graph Bipartite](https://leetcode.com/problems/is-graph-bipartite/)
| 18/07/2020 | [0097 Interleaving String](https://leetcode.com/problems/interleaving-string/)
| 19/07/2020 | [0312 Burst Balloons](https://leetcode.com/problems/burst-balloons/)
| 20/07/2020 | [0167 Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
| 21/07/2020 | [0044 Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)
| 23/07/2020 | [0064 Minimum Path Sum](https://leetcode.com/problems/wminimum-path-sum/)

***
## Coding Style
| Language       | Style        |
| ------------- |:-------------:|
| Python     | [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) |
***

## Questions by Category
######I use both the US and Chinese website of Leetcode, therefore there are questions uploaded to both version.
######The number and title of each questions is consistent and the web pages of the original question are linked below as well.

### Array
| Number | Title       |
| -------|:-------------:|
|  0014  | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)|
|  0088  | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)|

***
### Binary Search
| Number | Title       |Note|
| -------|:-------------:|:----------------------:|
|  0035  | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Extension of 0704|
|  0069  | [Square root of x](https://leetcode.com/problems/sqrtx/) | This question can also use *f(x)= x^2 - a* (牛顿迭代法）|
|  0378  | [kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | Binary Search (first method) is faster than using stack and makes full use of the characteristic of matrix|
|  0704  | [Binary Search](https://leetcode.com/problems/binary-search/)

#### General solutions for binary search:
- 知识点讲解(by @liweiwei1419)：
['用「排除法」（减治思想）写二分查找问题、与其它二分查找模板的比较'](https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/)
###### 重点：根据实际情况判断mid的归属， 不要死套模版
***
### Binary Search Tree
| Number | Title       | Note|
| -------|:-------------:|:-----:|
|  0094  | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
|  0098  | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
|  0102  | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)| BFS model applied using queue
|  0108  | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)| recursion with reversed inorder traversal
|  0112  | [Path Sum](https://leetcode.com/problems/path-sum/)| easy recursion
|  0124  | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)| DFS recursion method model
|  0144  | [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)| DFS model, here stack is used to iterate
|  0145  | [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)| similar code as 'preorder' with reversed stacking order
|  0236  | [Lowest Common Ancestor of A Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
|  0297  | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Extension of [0102](binary_search_tree/0102_binary_tree_level_order_traversal.py) (iteration)
|  0315  | [Count of Smaller Numbers after Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | Extended exercise of binary search tree, need to record count and position
|  0572  | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)
|  1028  | [Recover a Tree from Preorder Traversal](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/)| deserialize Binary Tree from a Preorder Traversal string (Serialize: [0144](binary_search_tree/0144_binary_tree_preorder_traversal.py)

#### Documentation:
- [Binary Tree Traversal](binary_search_tree/binary_tree.md): Four different methods to traverse a binary search tree
***

### Dynamic Programming
| Number | Title       | Note|
| -------|:-------------:|:------:|
|  0044  | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)|classic
|  0063  | [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)|similar as 0064, matrix dp
|  0064  | [Minimum Path Sum](https://leetcode.com/problems/wminimum-path-sum/)|easier version of Dungeon Game
|  0095  | [Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/)| further extension of [0096](dynamic_programming/0096_unique_binary_search_trees)
|  0096  | [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/)| Counting DP/ Math: Catalan Num
|  0097  | [Interleaving String](https://leetcode.com/problems/interleaving-string/)| linear DP 
|  0120  | [triangle](https://leetcode.com/problems/triangle/)| Linear DP classic problems: Four different methods
|  0174  | [Dungeon Game](https://leetcode.com/problems/dungeon-game/)| reversed dp from end to start
|  0309  | [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)|
|  0312  | [Burst Balloons](https://leetcode.com/problems/burst-balloons/)|
|  0718  | [Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)|
#### Documentation:
- [DP Classify and Summarize](https://zhuanlan.zhihu.com/p/126546914?utm_source=wechat_session&utm_medium=social&utm_oi=27134168924160%E3%80%82)
***
### Graph
| Number | Title       | Note|
| -------|:-------------:|:------:|
|  0785  | [Is Graph Bipartite](https://leetcode.com/problems/is-graph-bipartite/)| bfs method applied
***

### Hash Table
| Number | Title       | Note|
| -------|:-------------:|:------:|
|  0001  | [Two Sum](https://leetcode.com/problems/two-sum/)| similar as threeSum but different method|
|  0349  | [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)|similar as 0350 with set() used to print same element only once|
|  0350  | [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)|collections.Counter() and & used to print also duplicate elements|


***

### Linked List
| Number | Title       | Note|
| -------|:-------------:|:------:|
|  0092  | [Reversed Linked List II](https://leetcode.com/problems/reversed-linked-list-ii/)| Integrated with the method in 0206 reversed linked list|
|  0206  | [Reversed Linked List](https://leetcode.com/problems/reversed-linked-list/)|


***
### Math
| Number | Title       | Note|
| -------|:-------------:|:------:|
|  0007  | [Reverse Integer](https://leetcode.com/problems/reverse-integer/)
|  0009  | [Palindrome Number](https://leetcode.com/problems/palindrome-number/)
|  0050  | [Pow(x, n) ](https://leetcode.com/problems/powx-n/)|[Using merge sort / binary (@krahets)](https://leetcode-cn.com/problems/powx-n/solution/50-powx-n-kuai-su-mi-qing-xi-tu-jie-by-jyd/)
|  1014  | [Best Sightseeing Pair ](https://leetcode.com/problems/best-sightseeing-pair/)| O(n^2) will exceed time limit, O(n) method used here

***
### Stack
| Number | Title       |
| -------|:-------------:|
|  0032  | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)
|  0155  | [Min Stack](https://leetcode.com/problems/min-stack/)
|  0739  | [Daily Temperatures](https://leetcode.com/problems/daily_temperatures/)


***
### String
| Number | Title       |
| -------|:-------------:|
|  0003  | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
|  0005  | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
|  0008  | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

***
### Two Pointers
| Number | Title       |
| -------|:-------------:|
|  0015  | [3Sum](https://leetcode.com/problems/3sum/)
|  0167  | [Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

