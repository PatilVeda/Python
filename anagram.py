def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Anagram" if is_anagram(s1, s2) else "Not anagram")
