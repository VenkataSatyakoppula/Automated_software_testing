from Testcases_Generator import TestcasesGenerator
import os
class Os_file_manipulation(TestcasesGenerator):
    testcases = open("testcases.txt","r+")
    a = []
    @classmethod
    def append_in_txt(cls,limit,typee):
        cls.testcases = open("testcases.txt","r+")
        cls.testcases.truncate(0)
        cls.a= TestcasesGenerator.generate(limit,typee).copy()
        for line in cls.a:
            cls.testcases.write(str(line))
            cls.testcases.write("\n")
        cls.testcases.close()
        os.startfile("testcases.txt")
