# LeetCode
 This is a place to store and categorize all the past coding practices, mainly leetcode practice. 

###### User name: yy452
***
## Navigator
- [Useful Resources](#useful-resources)
- [My Coding Challenge Diary (2020)](#my-coding-challenge-diary--2020-)
- [Coding Style](#coding-style)
- [Questions by Category](#questions-by-category)
  * [Array](#array)
  * [Binary Search](#binary-search)
    + [General solutions for binary search:](#general-solutions-for-binary-search-)
  * [Binary Search Tree](#binary-search-tree)
  * [Hash Table](#hash-table)
  * [Linked List](#linked-list)
  * [Math](#math)
  * [Stack](#stack)
  * [String](#string)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>
***
## Useful Resources
- [Leetcode 常见题型代码模版](https://blog.csdn.net/fuxuemingzhu/article/details/101900729)
 （整理的非常细致的一些可以通用的算法框架，可以适当背下来。）
***
## My Coding Challenge Diary (2020)
| Date       | Title        |
| ------------- |:-------------:|
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
|  0704  | [Binary Search](https://leetcode.com/problems/binary-search/)

#### General solutions for binary search:
- 知识点讲解(by @liweiwei1419)：
['用「排除法」（减治思想）写二分查找问题、与其它二分查找模板的比较'](https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/)
###### 重点：根据实际情况判断mid的归属， 不要死套模版
***
### Binary Search Tree
| Number | Title       | Note|
| -------|:-------------:|:-----:|
|  0098  | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
|  0102  | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)| BFS model applied using queue
|  0236  | [Lowest Common Ancestor of A Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
|  0297  | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Extension of 0102 (BFS applied)
|  0572  | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)

***
### Hash Table
| Number | Title       | Note|
| -------|:-------------:|:------:|
|  0001  | [Two Sum](https://leetcode.com/problems/two-sum/)| similar as threeSum but different method|


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

