"""Question :Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation(See example).

Valid operators are +, -, *, and /.

Note that division between two integers should truncate toward zero. It is guaranteed that the given RPN expression is always valid. 
That means the expression would always evaluate to a result, and there will not be any division by zero operation. 
The Input is an array of strings where each element is either a valid operator or an integer. E.g.[“1”,”2”,”+”]"""

def rev_pol_not(tokens):
    # Time Complexity Explanation:
    # We are iterating through all the tokens once, hence the time complexity is O(n), 
    # where n is the number of tokens.
    
    stack = []
    valid_operator = {
        '+': lambda n1, n2: n1 + n2,
        '-': lambda n1, n2: n1 - n2,
        '*': lambda n1, n2: n1 * n2,
        '/': lambda n1, n2: int(n1 / n2)  # integer division in Python
    }
 
    for token in tokens:
        if token in valid_operator:
            n2 = stack.pop()
            n1 = stack.pop()
            result = valid_operator[token](n1, n2)
            stack.append(result)
        else:
            stack.append(int(token))
 
    return stack.pop()
 
# Final Time Complexity: The time complexity for this function is O(n), where n is the number of tokens.

print(rev_pol_not(["1", "2", "+"]))          # 3
print(rev_pol_not(["2", "3", "4", "*", "+"])) # 2 + (3*4) = 14
print(rev_pol_not(["4", "13", "5", "/", "+"]))# 4 + (13/5) = 4 + 2 = 6
print(rev_pol_not(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
# famous LeetCode example → 22
