
import math
import os
import random
import re
import sys

def isBalanced(s):
    stack=[]
    open_brackets=['(', '{', '[']
    close_brackets=[')', '}', ']']
    
    for i in s:
        if i in open_brackets:
            stack.append(i)
        elif i in close_brackets: 
            if not stack:  
                return "NO"
            
            if stack.pop() != open_brackets[close_brackets.index(i)]:
                return "NO"
    return "YES" if not stack else "NO"

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

#test case as given in hackerrank
6
}][}}(}][))]
[](){()}
()
({}([][]))[]()
{)[](}]}]}))}(())(
([[)

#output
NO
YES
YES
YES
NO
NO
