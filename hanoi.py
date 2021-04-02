# 汉诺塔问题
index = 1

def hanoi(n, A, B, C):
    if n > 0:
        hanoi(n - 1, A, C, B)
        global index
        print("第%d步：%s moving to %s" % (index, A, C))
        index += 1
        hanoi(n - 1, B, A, C)

hanoi(3, 'A', 'B', 'C')

