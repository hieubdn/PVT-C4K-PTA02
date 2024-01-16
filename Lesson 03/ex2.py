class ThuCung:
    def __init__(self, ten, giong, mau_sac, tuoi, can_nang):
        self.ten = ten
        self.giong = giong
        self.mau_sac = mau_sac
        self.tuoi = tuoi
        self.can_nang = can_nang

    def xuat_thong_tin(self):
        print("=Thông tin về thú cưng=")
        print("Tên", self.ten)
        print("Giống", self.giong)
        print("Màu sắc", self.mau_sac)
        print("Tuổi", self.tuoi)
        print("Cân nặng",self.can_nang)

    def doi_mau_long (self, mau_moi):
        self.mau_sac = mau_moi
        print("Đổi màu lông của thú cưng thành: ", mau_moi)
# Gán giá trị dữu liệu cho class
thu_cung1 = ThuCung("MiLu", "Chó Labrador", "Vàng", 2, 15)
thu_cung2= ThuCung("Mèo", "dog", "đỏ", 3, 30)
# Xuất thông tin
thu_cung1.xuat_thong_tin()
thu_cung2.xuat_thong_tin()
# Đổi màu và xuất
thu_cung2.doi_mau_long("vàng")
thu_cung2.xuat_thong_tin()