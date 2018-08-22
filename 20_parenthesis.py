from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = deque([])

        started = False
        opening = ['[', '{', '(']
        closing = [']', '}', ')']
        pairs = {']': '[', '}': '{', ')': '('}

        opened = 0

        for x in s:
            print (x, opened)
            if not started:
                started = True
                if x in opening:
                    d.append(x)
                    opened = opened + 1
                else:
                    return False
            else:
                if x in opening:
                    d.append(x)
                    opened = opened + 1
                elif x not in closing:
                    return False
                elif len(d) == 0:
                    return False
                elif pairs[x] != d.pop():
                    return False
                else:
                    opened = opened - 1

        if opened != 0:
            return False
        
        return True
        

if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid('{()}]'))

    sol = Solution()
    print(sol.isValid('{('))

    sol = Solution()
    print(sol.isValid('{()}'))

