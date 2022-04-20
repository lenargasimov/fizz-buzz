def fizz_buzz():
    for number in range(1, 101):
        divisible3 = number % 3
        divisible5 = number % 5

        match (divisible3, divisible5):
            case (0, 0):
                print("FizzBuzz")
            case (0, _):
                print("Fizz")
            case (_, 0):
                print("Buzz")
            case _:
                print(number)


fizz_buzz()
