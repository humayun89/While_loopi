"""
#1. Make a lists of sequence from one to hundred. (using loop and range)
# 2.Multiply it by 8 using map
#3.Use lambda to multiply it.
#4. Find all of the odd and even numbers within it.
"""

#1.Solution :
seq = []
for i in range(1,101):
    seq.append(i)
print(seq)
# Again:
seq=list(range(1,101))
print(seq)
#multiply seq by 8 using map:
def times8(num): return num*8
multiple8=list(map(times8,seq))
print(multiple8)
# multiply of seq by 8 using for loop :
multiple8 = [times8(num) for num in seq]
print(multiple8)
# Use lambda function to multiply it by 7 :
x= list(map(lambda num:num*7,seq))
print(x)
# Findout all of the odd and even number within the sequence:
odd_number= list(map( lambda num: num % 2 != 0, seq))
even_number= list(map(lambda num: num% 2==0, seq))
print(even_number)
print(odd_number)