class PhuongTien:
    def __init__(self, loai_xe, hang_xe, mau_sac, so_cho_ngoi, so_banh_xe, gia_tien):
        self.loai_xe = loai_xe
        self.hang_xe = hang_xe
        self.mau_sac = mau_sac
        self.so_cho_ngoi = so_cho_ngoi
        self.so_banh_xe = so_banh_xe
        self.gia_tien = gia_tien
# Hãy viết phương thức in ra một số thông tin của một phương tiện.
    def in_thong_tin(self):
        print(self.loai_xe)
        print(self.hang_xe)
        print(self.mau_sac)
        print(self.gia_tien)
# Khởi tạo đối tượng thuộc lớp PhuongTien
xe_hoi = PhuongTien("xe hơi", "Toyota", "đen", 4, 4, 5000)