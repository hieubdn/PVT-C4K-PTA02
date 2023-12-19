# Bài tập
class VatNuoi:
    def __init__(self, ten, giong, mau_sac, tuoi, can_nang):
        self.ten = ten
        self.giong = giong
        self.mau_sac = mau_sac
        self.tuoi = tuoi
        self.can_nang = can_nang
thu_cung1 = VatNuoi("Milu", "Chihuahua", "Vàng", 2, 15)
thu_cung2 = VatNuoi("misa", "Mặt xệ", "trăng- đen", 5, 15)

print("Thông tin về: ", thu_cung1.ten)
print("Giống loài: ", thu_cung1.giong)
print("Màu sắc: ", thu_cung1.mau_sac)
print("Tuổi: ", thu_cung1.tuoi)
print("Cân nặng: ", thu_cung1.can_nang)