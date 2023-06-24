def check(string):
    stack = []
    for char in string:
        if char in ("(", "[", "{"):
            stack.append(char)
        elif char in (")", "]", "}"):
            if not stack or stack.pop() != char:
                return False
    return not stack


string = input("Enter the Sequence:--")
print(check(string))
