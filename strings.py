#Question 1: WAP to Split string every n characters but without splitting a word.
# Answer:
from textwrap import wrap
str = "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule. Python is dynamically typed and garbage-collected"
print("\n".join(wrap(str, 15)))

# Question 2: Please find the frequency of each charactor in a given string
# Answer :
str = "Hello we are using python"
str_upper = str.upper()
freq = {}
for char in str_upper:
    if char in freq:
        freq[char] = freq[char]+1
    else:
        freq[char] = 1
print(freq)


