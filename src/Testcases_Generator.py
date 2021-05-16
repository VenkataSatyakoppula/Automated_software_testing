import random
import string
class TestcasesGenerator():
    arr_result = []
    @classmethod
    def generate_random_values(cls,Limit,typee):
        cls.arr_result.clear()
        if(typee == 0):
            for _ in range(0,Limit):
                cls.arr_result.append(random.randint(0,Limit))
            return cls.arr_result   
        else:
            for _ in range(0,Limit):
                cls.arr_result.append(''.join(random.choices(string.ascii_letters, k = 6)))
            return cls.arr_result 
