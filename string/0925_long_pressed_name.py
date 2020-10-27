"""
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

"""


class Solution:
    def isLongPressedName(self, name, typed):
        i, j = 0, 0
        n, m = len(name), len(typed)
        # Fist character must be same
        if name[i] != typed[j]:
            return False

        while i < n and j < m:
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if typed[j] == name[i - 1]:
                    j += 1
                else:
                    return False

        # quit loop at the same time
        if i == n and j == m:
            return True
        # if typed quit first, more characters in name
        if i < n:
            return False
        # if name quit first, check what's left in typed all equals the last character in name
        if j < m:
            if ''.join(set(typed[j:])) == typed[j]:
                return True
            return False
