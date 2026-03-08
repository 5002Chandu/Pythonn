num = int(input("Enter any Number: "))
org = num
rev = 0

# Reverse the number
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

print("The reverse of", org, "is", rev)

# Check palindrome
if rev == org:
    print("The number", org, "is Palindrome")
else:
    print("The number", org, "is not a Palindrome")

# Count digit occurrences
print("Digit\tNumber of Occurrences")
for i in range(0, 10):
    count = 0
    temp = org   # use the original number, not 'number'
    while temp > 0:
        digit = temp % 10
        if digit == i:
            count += 1
        temp = temp // 10
    if count > 0:
        print(i, "\t", count)
