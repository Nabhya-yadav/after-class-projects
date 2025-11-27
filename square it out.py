def square_even_odd(start, end):
    squares = []
    even_squares = []
    odd_squares = []

    for num in range(start, end + 1):
        squares.append(num * num)

    for sq in squares:
        if sq % 2 == 0:
            even_squares.append(sq)
        else:
            odd_squares.append(sq)

    print("All squares:", squares)
    print("Even squares:", even_squares)
    print("Odd squares:", odd_squares)


square_even_odd(1, 10)
