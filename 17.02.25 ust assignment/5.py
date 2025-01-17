class Numbers:
    def __init__(self, value):
        self.value = value

    def ChkPrime(self):
        if self.value == 0 or self.value == 1:
            return False
        elif self.value == 2:
            return True
        for i in range(2, int(self.value ** 0.5)):
            if self.value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        fact_sum = Numbers.SumFactors(self)
        if fact_sum == self.value:
            return True
        else:
            return False

    def SumFactors(self):
        fact_sum = 0
        for i in range(1, self.value):
            if self.value % i == 0:
                fact_sum += i
        return fact_sum

    def Factors(self):
        lst = []
        for i in range(1, self.value):
            if self.value % i == 0:
                lst.append(i)
        return lst


o = Numbers(6)

print("Prime Check: ", o.ChkPrime())
print("*" * 20)

print("Perfect Check: ", o.ChkPerfect())
print("*" * 20)

print("Factors:", o.Factors())
print("*" * 20)

print("Sum of Factor:", o.SumFactors())
print("*"*20)