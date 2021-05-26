from Testcases_Generator import TestcasesGenerator
import os
class Os_file_manipulation(TestcasesGenerator):
    cus_out_path = ""
    cus_test_path = ""
    testcases = open("testcases.txt","w")
    # executed_outputs = open("output.txt","r")
    a = []
    @classmethod
    def append_in_txt(cls,limit,typee):
        cls.testcases = open("testcases.txt","w")
        print(typee)
        cls.a= TestcasesGenerator.generate_random_values(limit,typee).copy()
        for line in cls.a:
            cls.testcases.write(str(line))
            cls.testcases.write("\n")
        cls.testcases.close()
        if limit!=0:
            os.startfile("testcases.txt")
    @classmethod
    def getpath(cls,testcases,outputs):
        cls.cus_out_path = outputs
        cls.cus_test_path = testcases
    @classmethod    
    def read_outputs(cls,key):
        temp=[]
        count=0
        temp.clear()
        if key==0:
            # print(cls.cus_out_path)
            outputs = open(cls.cus_out_path,"r")
        elif key==1:
            outputs = open("outputs.txt","r")    
        # os.startfile("C:/Users/VENKATA SATYA/Desktop/custom_outputs.txt")
        while True:
            count +=1
            line = outputs.readline()
            if not line:
                break
            print(line.strip())
            temp.append(line.strip())
        outputs.close()
        return temp
    @staticmethod
    def test_result_in_txt(mode,result):
        if mode==0:
            testresult = open("TestResult.txt","w")
            for line in result:
                testresult.write(str(line))
                testresult.write("\n")
            os.startfile("TestResult.txt")
            testresult.close()
        elif(mode==1):
            testresult = open("outputs.txt","w")
            for line in result:
                    testresult.write(str(line))
                    testresult.write("\n")
            os.startfile("outputs.txt")
            testresult.close()
            

        

