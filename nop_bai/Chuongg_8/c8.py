#bai 1 va 2
class TuDien:
    def __init__(self):
        self.dictionary = {}

    def NhapTu(self, tu, dong_nghia=None, trai_nghia=None):
        key = tu[0].lower()  # Hàm băm dựa trên ký tự đầu
        if key not in self.dictionary:
            self.dictionary[key] = {}
        self.dictionary[key][tu] = {'dong_nghia': dong_nghia or [], 'trai_nghia': trai_nghia or []}

    def TraTu(self, tu):
        key = tu[0].lower()
        if key in self.dictionary and tu in self.dictionary[key]:
            return self.dictionary[key][tu]
        else:
            return "Không tìm thấy từ trong từ điển"

    def DongNghia(self, tu):
        key = tu[0].lower()
        if key in self.dictionary and tu in self.dictionary[key]:
            return self.dictionary[key][tu]['dong_nghia']
        else:
            return "Không tìm thấy từ trong từ điển"

    def TraiNghia(self, tu):
        key = tu[0].lower()
        if key in self.dictionary and tu in self.dictionary[key]:
            return self.dictionary[key][tu]['trai_nghia']
        else:
            return "Không tìm thấy từ trong từ điển"

# Sử dụng lớp TuDien
td = TuDien()
td.NhapTu("bánh", ["cake"], ["bread"])
print(td.TraTu("bánh"))  # Trả về từ đồng nghĩa và trái nghĩa
print(td.DongNghia("bánh"))  # Trả về các từ đồng nghĩa
print(td.TraiNghia("bánh"))  # Trả về các từ trái nghĩa
