import random
import string
class TestcasesGenerator():
    a = []
    @classmethod
    def generate(cls,Limit,typee):
        cls.a.clear()
        if(typee == 0):
            for i in range(0,Limit):
                cls.a.append(random.randint(0,Limit))
            return cls.a   
        else:
            for i in range(0,Limit):
                cls.a.append(''.join(random.choices(string.ascii_letters, k = 6)))
            return cls.a 
