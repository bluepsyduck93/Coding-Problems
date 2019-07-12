def reverse_polish(input_arr):
    nums = []
    for i in input_arr:
        if type(i) == int:
            nums.append(i)
        else:
            if i == '+':
                nums.append(nums.pop() + nums.pop())
            elif i == '-':
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(num1 - num2)
            elif i == '/':
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(num1 / num2)
            elif i == '*':
                nums.append(nums.pop() * nums.pop())
    print(nums)


reverse_polish([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'])