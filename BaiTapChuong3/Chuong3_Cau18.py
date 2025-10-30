''' Với n là chiều cao của hình, hãy dựa vào n để Vẽ các hình dưới đây  '''
n = int(input("Nhập chiều cao n: "))
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()

n = int(input("Nhập chiều cao n: "))
for i in range(1, n + 1):
    print('  ' * (n - i), end='') 
    print('* ' * i)

n = int(input("Nhập chiều cao n (số lẻ): "))

for i in range(n):
    for j in range(n):
        if i == n // 2:
            print('*', end=' ')
        elif i < n // 2 and (j == 0 or j == i):
            print('*', end=' ')
        elif i > n // 2 and (j == n - 1 or j == i):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

