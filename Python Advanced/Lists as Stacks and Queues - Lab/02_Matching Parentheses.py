s = input()
stack = []
for el in range(len(s)):
    if s[el] == "(":
        stack.append(el)
    elif s[el] == ")":
        
        last = stack.pop()
        print(s[last:el + 1])
