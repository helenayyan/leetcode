# The Knuth-Morris-Pratt Algorithm
> The Knuth-Morris-Pratt Algorithm (KMP) is widly applied in matching substrings problems.
It was introduced by D.E.Knuth、J,H,Morris and V.R.Pratt. 
>
## Partial Match Table
The key to KMP Algorithm is the partial match table, usually stored as a list named `next` or `fail`. 
With its help, we could then avoid moving the pointers back to the beginning once fail matching.

### Proper Prefix and Suffix
- Proper Prefixes:
    All the substrings with one or more cut off the end.
- Proper Suffixes:
    All the substrings with one or more cut off the beginning.
    
Eg: `abcde` has prefixes: `a`,`ab`,`abc`,`abcd`; suffixes:`e`,`de`,`cde`,`bcde`

### Partial Match Value
> The length of the longest proper prefix that matches a proper suffix in the same substring.
>

#### Sample partial match table
String: `s = abababca`, `next = [0,0,1,2,3,4,0,1]`

    string: a b a b a b c a
    index:  0 1 2 3 4 5 6 7
    value:  0 0 1 2 3 4 0 1

##### Notes:
1. For substrings `a` and `ab`, they don't have any matching proper prefix and proper suffix.
2. Examining the first three characters `aba`, we see that proper prefix `a`and proper suffix `a`. Thus, the partial match value, which is the lenght of the longest proper matching prefix and suffix, is `1`.
3. Similarly:
    - `abab` has longest match `ab`;
    - `ababa`: `aba`
    - `ababab`: `abab`
    - `abababc` does not have any match
    - `abababca` only has match `a` of length 1
  
##### Code:
```python
def pmv_match(sub_string):
    """
        return: the length of the longest matching proper prefix and suffix
    """
    n = len(sub_string) - 1
    for i in range(n):
        # start from the longest proper prefix
        if sub_string[:n - i] == sub_string[i + 1:]:
            return n - i
    return 0
```

### Code Implementation of Partial Match Table
#### Using `pmv_match()` function:
```python
def get_pmt(s):
    """
        return: the list containing all the partial match values of the substrings
    """
    n = len(s)
    next = [0 for _ in range(n)]
    for i in range(n):
        next[i] = pmv_match(s[:i])
    return next
```
#### Fast Implementation
```python
def get_pmt(s):
    n = len(s)
    next = [0 for _ in range(n)]
    for i in range(1, n):
        j = next[i-1]
        while j != 0 and s[j] != s[i]:
            j = next[j]
        if s[j] == s[i]:
            next[i] = j + 1
    return next
```

## Apply Partial Match Table in KMP
With the help of the Partial Match Table `next`, we can then easily match the strings.

### Violent Algorithm
Let' s first take a look at the violent algorithm when matching two strings.

Suppose we’re matching the pattern `p = abababca` against the text `s = bacbababaabcbab`
For violent match, we use two pointers `i` and `j` and move them each along `s` and `p`, 
- if current character match, i.e. `s[i] == p[j]`, `i` and `j` move along the string,
- else, move `i` to the next search starting point `i - (j - 1)` and reset `j = 0`

1. i = 0, j = 0

    s = bacbababaabcbab  (i = 0)
        | (unmatch)
    p = abababca (j = 0)

i = i - j + 1 = 1, j = 0

2. i = 1, j = 0

    s = bacbababaabcbab  (i = 2)
         || 
    p =  abababca (j = 1)
    
3. i = 2, j = 0
    ...
    
```python
def violent_match(s:str, p:str):
    s_len = len(s)
    p_len = len(p)
    
    # set two pointers
    i = 0
    j = 0

    while i < s_len and j < p_len:
        if s[i] == p[j]:
            # ①s[i] == p[j], i++, j++    
            i+=1
            j+=1
        else:
            # ②s[i]! = p[j], i = i - (j - 1)，j = 0    
            i = i - j + 1
            j = 0

    # if successfully match, return the location of start，otherwise return -1
    if j == p_len:
        return i - j
    else:
        return -1

```
However, it is easily to notice that once unmatched, 
if we move back both `i` and `j`, some known unmatched character need to be reconsider again.

Therefore, the partial match table is introduced to skip these step and move the pointer to the next possible starting position.

### KMP Algorithm
Recall the Partial Match table of `p = abababca` ：

    string: a b a b a b c a
    index:  0 1 2 3 4 5 6 7
    value:  0 0 1 2 3 4 0 1
    
Similarly, we use two pointers `i` and `j` and move them each along `s` and `p`.
When moving the pointers, we use the values in the partial match table to skip ahead 
rather than redoing unnecessary old comparisons following the formula:

`position to be skipped = partial matched length - table[partial matched length - 1]` (`table[partial matched length] > 1`)

1. The first partial match: i = 1, j = 0

    s = bacbababaabcbab  (i = 2)
         | 
    p =  abababca (j = 1)

`partial matched lenght = 1`, `table[partial matched length - 1]` (or `table[0]`) is `0`, so we don’t get to skip ahead any. 

2. The next partial match:
    
    s = bacbababaabcbab  (i = 2)
            ||||| 
    p =     abababca (j = 1)
    
`partial matched lenght = 5`, `table[partial_match_length - 1]` (or `table[4]`) is `3`, 
That means we get to skip ahead `partial matched length - table[partial matched length - 1]` (or `5 - table[4] = 2`) characters.

3. Skip ahead 2 characters:

    // x denotes a skip
    s = bacbababaabcbab
            xx|||
    p =       abababca
    
This is a `partial matched length` of `3`. 
The value at `table[partial_match_length - 1]` (or `table[2]`) is `1`. 
That means we get to skip ahead `partial matched length - table[partial matched length - 1]` (or `3 - table[2]` or `2`) characters:

3. Skip ahead again 2 characters:

    // x denotes a skip
    
    s = bacbababaabcbab
              xx|
    p =         abababca
    
`j + len(p) > len(s)`, given no match.

#### Code implementation

```python
def kmp_search(s: str, p: str, next: [int]):
	i = 0
	j = 0
	s_len = len(s)
	p_len = len(p)
	while i < s_len and j < p_len:
		# ①if j = -1, or s[i] == p[j], i++，j++    
		if j == -1 or s[i] == p[j]:
			i += 1
			j += 1
        else:
            # ② if j != -1 and s[i] != p[j], i unchange and j = next[j]      
            j = next[j]
    if j == p_len:
        return i - j
    else:
        return -1
```
  
## Reference
> 1. http://jakeboxer.com/blog/2009/12/13/the-knuth-morris-pratt-algorithm-in-my-own-words/
> 2. https://blog.csdn.net/v_JULY_v/article/details/7041827
> 