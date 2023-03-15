def compare_strings(s1, s2):
    if len(s2.replace('*', '')) > len(s1):
        return 0
    if len(s1) == 0 and len(s2) == 0:
        return 1
    if len(s1) > 0 and len(s2) == 0:
        return 0
    if len(s1) == 0 and len(s2) > 0:
        return 0
    if s1[0] == s2[0] or s2[0] == '*':
        if compare_strings(s1[1:], s2[1:]):
            return 1
    if s2[0] == '*':
        if compare_strings(s1[1:], s2) or compare_strings(s1, s2[1:]):
            return 1
    return 0

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
if compare_strings(s1, s2):
    print("1")
else:
    print("0")
