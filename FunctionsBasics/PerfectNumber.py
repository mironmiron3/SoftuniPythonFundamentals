def check_if_perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

a = int(input())
outcome = check_if_perfect_number(a)
print(outcome)
