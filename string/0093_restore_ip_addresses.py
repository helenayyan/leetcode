"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

"""


class Solution:
    def restoreIpAddresses(self, s: str):
        res = [s]
        for _ in range(3):
            curr_res = []
            for si in res:
                curr = si.split('.')[-1]
                n = len(si) - len(curr)  # length of prev splited string

                for i in range(1, len(curr) + 1):
                    if i > 3:
                        break
                    if int(curr[:i]) <= 255:
                        curr_res.append(si[: n + i] + '.' + si[n + i:])
                    if curr[0] == '0':
                        # only consider 0 but not 01 / 012 etc
                        break
            res = curr_res

        res_now = []

        def valid(num_s):
            # check if the string if valid as one sector of the address
            if num_s and int(num_s) < 256:
                if num_s[0] != '0' or num_s == '0':
                    return True
            return False

        for si in res:
            end = si.split('.')[-1]
            if valid(end):
                res_now.append(si)

        return res_now
