# *****Tự luận*****
# câu1
class Hinhvuong:
    def __init__(self, canh):
        self.canh = canh
    
    def tinh_chu_vi (self):
        chu_vi = 4 * self.canh
        return chu_vi
    
canh_hinh_vuong = 5
hinh_vuong = Hinhvuong(canh_hinh_vuong)
chu_vi_hinh_vuong = hinh_vuong.tinh_chu_vi()
print(f"Chu vi hình vuông có cạnh bằng {canh_hinh_vuong} là: {chu_vi_hinh_vuong}") 
# Câu 2
