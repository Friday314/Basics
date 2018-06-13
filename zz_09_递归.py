
# 循环递归
i = 1
result = 1
while i <= 4:
    result *= i
    i += 1

print(result)


# 方法递归
def getNums(num):

    if num > 1:
        return num * getNums(num - 1)
    else:
        return num


print(getNums(4))
