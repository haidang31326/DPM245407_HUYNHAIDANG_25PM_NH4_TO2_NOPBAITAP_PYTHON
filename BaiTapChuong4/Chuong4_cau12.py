def oscillate(start, stop):

  for i in range(start, stop):
    yield i
    yield -i


print("Kết quả chạy chương trình:")
for n in oscillate(-3, 5):
    print(n, end=' ')
print()

