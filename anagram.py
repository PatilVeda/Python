# def is_anagram(s1, s2):
#     return sorted(s1) == sorted(s2)

# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")
# print("Anagram" if is_anagram(s1, s2) else "Not anagram")

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# n = int(input("Enter a number: "))
# total = 0
# for i in range(2, n + 1):
#     if is_prime(i):
#         total += i
# print("Sum of primes:", total)
# lst = list(map(int, input("Enter numbers: ").split()))
# rev = []
# for i in range(len(lst)-1, -1, -1):
#     rev.append(lst[i])
# print("Reversed list:", rev)
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
print(squares)  # Output: [1, 4, 9, 16]
