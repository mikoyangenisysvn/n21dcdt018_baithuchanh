class SoHang:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None

    def __repr__(self):
        return f"{self.HeSo}x^{self.SoMu}"
class DaThuc:
    def __init__(self):
        self.Head = None

    def Them(self, heso, somu):
        new_term = SoHang(heso, somu)
        if not self.Head:
            self.Head = new_term
        else:
            current = self.Head
            while current.KeTiep:
                current = current.KeTiep
            current.KeTiep = new_term

    def RutGon(self):
        if not self.Head:
            return
        powers = {}
        current = self.Head
        while current:
            if current.SoMu in powers:
                powers[current.SoMu] += current.HeSo
            else:
                powers[current.SoMu] = current.HeSo
            current = current.KeTiep
        
        self.Head = None
        for p in sorted(powers.keys(), reverse=True):
            if powers[p] != 0:
                self.Them(powers[p], p)

    def Cong(self, other):
        result = DaThuc()
        current = self.Head
        while current:
            result.Them(current.HeSo, current.SoMu)
            current = current.KeTiep
        current = other.Head
        while current:
            result.Them(current.HeSo, current.SoMu)
            current = current.KeTiep
        result.RutGon()
        return result

    def DoiDau(self):
        current = self.Head
        while current:
            current.HeSo = -current.HeSo
            current = current.KeTiep

    def Tich(self, other):
        result = DaThuc()
        a = self.Head
        while a:
            b = other.Head
            while b:
                result.Them(a.HeSo * b.HeSo, a.SoMu + b.SoMu)
                b = b.KeTiep
            a = a.KeTiep
        result.RutGon()
        return result

    def Chep(self):
        copy = DaThuc()
        current = self.Head
        while current:
            copy.Them(current.HeSo, current.SoMu)
            current = current.KeTiep
        return copy

    def __repr__(self):
        if not self.Head:
            return "0"
        terms = []
        current = self.Head
        while current:
            terms.append(f"{current.HeSo}x^{current.SoMu}")
            current = current.KeTiep
        return " + ".join(terms)

# Sử dụng các phương thức
dt = DaThuc()
dt.Them(3, 2)
dt.Them(5, 1)
dt.Them(-2, 2)
dt.RutGon()
print(dt)

dt1 = DaThuc()
dt1.Them(1, 2)
dt1.Them(2, 1)

dt2 = DaThuc()
dt2.Them(3, 2)
dt2.Them(1, 1)

dt3 = dt1.Cong(dt2)
print(dt3)

dt1.DoiDau()
print(dt1)

dt4 = dt1.Tich(dt2)
print(dt4)
