# Write a function that return whether or not the input string has balanced parantheses
# Balanced:
#   '((()))'
#   '(()())'
#2 Not balanced:
#   '((()'
#   '())('
def count(paren):
    stack = []
    pushChars, popChars = "<({[", ">)}]"
    for c in str:
        if c in pushChars:
            stack.append(c)
        elif c in popChars:
            if not len(stack):
                return False
            else:
                stackTop = stack.pop()
                balancingBracket = pushChars[popChars.index(c)]
                if stackTop != balancingBracket:
                    return False
        else:
            return False
    return not len(stack)
