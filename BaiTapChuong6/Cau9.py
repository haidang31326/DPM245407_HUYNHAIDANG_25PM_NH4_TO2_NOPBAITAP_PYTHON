
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


M = list(map(int, input("Nhập mảng số tự nhiên (cách nhau bằng dấu cách): ").split()))

so_le = [x for x in M if x % 2 != 0]
so_chan = [x for x in M if x % 2 == 0]
so_nguyen_to = [x for x in M if la_so_nguyen_to(x)]
so_khong_nt = [x for x in M if not la_so_nguyen_to(x)]

print("Dòng 1 - Số lẻ:", so_le, f"→ Có {len(so_le)} số lẻ")
print("Dòng 2 - Số chẵn:", so_chan, f"→ Có {len(so_chan)} số chẵn")
print("Dòng 3 - Số nguyên tố:", so_nguyen_to)
print("Dòng 4 - Không phải số nguyên tố:", so_khong_nt)
