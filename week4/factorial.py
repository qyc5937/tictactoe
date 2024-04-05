def factorial (num):
    if num == 1:
        return 1
    if num == 0:
        return 0
    answer = num * factorial(num - 1)
    return answer

print(factorial(5))