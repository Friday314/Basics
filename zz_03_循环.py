"""

while 条件:
    循环体

手动死循环
while True:
    循环体

"""

i = 1

while i <= 10:
    print(i)
    i += 1


"""

for 循环

for item in iterable:
    do
    
item        表示元素
iterable    是集合

"""
for i in range(1, 11):
    print(i)


names = ["xiaoming", "wangwu", "peter"]
ages = [22, 15, 19]

# 多重循环，通过zip
for name, age in zip(names, ages):
    print(name, age)


urls = ["www.baidu.com/pdf{}".format(number)
        for number in range(1, 11)]

for url in urls:
    print(url)

