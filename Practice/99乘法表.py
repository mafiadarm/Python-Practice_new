# version 3.6
# 99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%2d ' % (j, i, i * j), end='')
    print()

for i in range(9, 0, -1):
    for j in range(1, i + 1):
        print('%d*%d=%2d ' % (j, i, i * j), end='')
    print()
