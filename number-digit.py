number = int(input("Enter number"))
number_copy = number
length = 1
zeros = 1
remain = number
if number_copy >= 0 and number_copy < 10:
    length += 1
else:
    while number_copy > 9:
        number_copy = number_copy//10
        zeros *= 10
        length += 1
while zeros > 1:
    print(int(remain // zeros))
    remain = remain % zeros
    zeros /= 10
print(int(remain))
