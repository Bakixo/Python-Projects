"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        yeni_liste = int(''.join(map(str, digits))) + 1

        sonuc = [int(digit) for digit in str(yeni_liste)]
        return sonuc
"""
