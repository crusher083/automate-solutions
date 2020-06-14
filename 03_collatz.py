def collatz():
    while True:
        try:
            num = int(input('Please enter the number: '))
            if num % 2 == 0:
                result = (num // 2)
            else:
                result = (num * 3) + 1
        except ValueError:
            print('Please enter integer!')
        else:
            return result
