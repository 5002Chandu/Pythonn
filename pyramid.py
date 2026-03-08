print("\nExact Center Pyramid")

rows = 5
for i in range(1, rows + 1):
    stars = '*' * (2 * i - 1)   # odd number of stars per row
    print(stars.center(2 * rows))  # center align within max width
