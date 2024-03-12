class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = int(a, 2)
        num_b = int(b, 2)

        toplam = num_a + num_b
        sonuc = bin(toplam)[2:]

        return sonuc
    