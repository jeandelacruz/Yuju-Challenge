from re import match

def checkExpression(expression):
    for v in expression:
        if len(expression) <= 100:
            if len(v) <= 5000:
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