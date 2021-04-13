from re import match

def checkExpression(expression):
    for v in expression:
        if len(expression) <= 100:
            if len(expression) <= 5000:
                print(v)
                if match("\{([^()]|())*\}|^\{\(\{\}\[]\)\}$", v):
                    print(1)
                else:
                    print(0)

expressions = [
    "{(})([]}", 
    "{}()[]",
    "{({}[])}"
]

checkExpression(expressions)