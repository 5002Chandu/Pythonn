rows = 5
# Upper pyramid
for i in range(1, rows + 1):
    stars = '*' * (2 * i - 1)
    print(stars.center(2 * rows))

# Lower pyramid
for i in range(rows - 1, 0, -1):
    stars = '*' * (2 * i - 1)
    print(stars.center(2 * rows))
