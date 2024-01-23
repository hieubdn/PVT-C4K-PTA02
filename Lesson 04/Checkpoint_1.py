# *****Tự luận*****
# câu1
# class Hinhvuong:
#     def __init__(self, canh):
#         self.canh = canh

#     def tinh_chu_vi(self):
#         chu_vi = 4 * self.canh
#         return chu_vi


# canh_hinh_vuong = 5
# hinh_vuong = Hinhvuong(canh_hinh_vuong)
# chu_vi_hinh_vuong = hinh_vuong.tinh_chu_vi()
# print(f"Chu vi hình vuông có cạnh bằng {canh_hinh_vuong} là: {chu_vi_hinh_vuong}")

# Câu 2
class HocSinh:
    def __init__(self, ten, dia_chi, chieu_cao, can_nang, hoc_luc=""):
        self.ten = ten
        self.dia_chi = dia_chi
        self.chieu_cao = chieu_cao
        self.can_nang = can_nang
        self.hoc_luc = hoc_luc

    def cap_nhat_dia_chi(self, dia_chi_moi):
        self.dia_chi = dia_chi_moi
        print(f"Địa chỉ của học sinh {self.ten} đã được cập nhật thành {dia_chi_moi}.")

    def cap_nhat_suc_khoe(self, chieu_cao_moi, can_nang_moi):
        self.chieu_cao = chieu_cao_moi
        self.can_nang = can_nang_moi
        print(f"Thông tin sức khỏe của học sinh {self.ten} đã được cập nhật.")

    def xuat_thong_tin(self):
        print(
            f"Thông tin học sinh:\nTên: {self.ten}\nĐịa chỉ: {self.dia_chi}\nChiều cao: {self.chieu_cao} cm\nCân nặng: {self.can_nang} kg\nHọc lực: {self.hoc_luc}"
        )


# Ví dụ sử dụng lớp HocSinh
hoc_sinh1 = HocSinh("Nguyen Van A", "123 Duong ABC, TP.HCM", 160, 50, "Giỏi")
hoc_sinh1.xuat_thong_tin()

hoc_sinh1.cap_nhat_dia_chi("456 Duong XYZ, TP.HCM")
hoc_sinh1.cap_nhat_suc_khoe(165, 55)

hoc_sinh1.xuat_thong_tin()
