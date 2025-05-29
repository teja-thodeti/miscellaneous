class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        final=len(digits)-1
        if digits[final]!=9:
            digits[final]=digits[final]+1
        elif digits[final]==9:
            digits[final]=1
            digits.append(0)
        else:
            string_convert=int("".join(map(str,digits)))
            string_convert+=1
            result=list(map(int,str()))
            print(result)
        return digits