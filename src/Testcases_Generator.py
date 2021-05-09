import random
class TestcasesGenerator():
    a = []
    @classmethod
    def generate(cls,Limit,type):
        for i in range(0,Limit):
            cls.a.append(random.randint(0,Limit))
        return cls.a    