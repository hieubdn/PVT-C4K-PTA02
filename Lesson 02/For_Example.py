# Tạo một class thông tin về con chó
class dog:
    name = ""
    age = 0
    color = ""
name_1 = dog()
name_1.name = "Bella"
print(name_1.name)

# Tạo hàm __init__
class ThuCung:
    def __init__(self, ten, tuoi, mau):
        self.ten = ten
        self.tuoi = tuoi
        self.mau = mau
