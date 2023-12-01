from itertools import permutations
import re

def makeExpressionbySeperator(seperator,expression,pr):
    expArr=re.split(seperator,expression)
    exp=''
    for s in expArr:
        if pr in s:
            arr=s.split(pr)
            if len(arr)>=2:
                exp+=str(eval(s))
            else:
                num=arr[0]
                exp+=num
        else:
            exp+=s
    return exp
  
def solution(expression):
    answer = 0
    operators=["-","*","+"]
    for pr1,pr2,pr3 in list(permutations(operators,3)):
        seperator1="("+"["+pr2+pr3+"]"+")"
        exp1=makeExpressionbySeperator(seperator1,expression,pr1)
        seperator2="("+"["+pr3+"]"+")"
        exp2=makeExpressionbySeperator(seperator2,exp1,pr2)
        answer=max(answer,abs(eval(exp2)))
    return answer