from posixpath import abspath, split
from Os_file_manipulation import Os_file_manipulation
import subprocess,os
import shutil,sys
class Automation_of_code:
    code_path = ""
    code_name = ""
    abs_path = ""
    @classmethod
    def get_code_path(cls,path):
        cls.code_path = path
        cls.code_name = os.path.basename(cls.code_path)
        cls.abs_path = os.path.abspath("testcodes")
        dest_path= cls.abs_path+"\\"+cls.code_name
        shutil.copyfile(cls.code_path,dest_path)
    @classmethod
    def execute_code(cls,testcasespath):
        ext = os.path.splitext(cls.code_name)[1]
        if ext==".c":
            subprocess.run("gcc -o "+cls.abs_path+"\\"+str(os.path.splitext(cls.code_name)[0])+" "+cls.abs_path+"\\"+cls.code_name,shell=True)
        elif ext==".java":
            subprocess.run("javac "+" "+cls.abs_path+"\\"+cls.code_name,shell=True)
        elif ext ==".cpp":
            subprocess.run("g++ -o "+cls.abs_path+"\\"+str(os.path.splitext(cls.code_name)[0])+" "+cls.abs_path+"\\"+cls.code_name,shell=True)
        if testcasespath!="":
            with open(testcasespath) as f:
                lines = [line.rstrip() for line in f]
        else:    
            with open('testcases.txt') as f:
                lines = [line.rstrip() for line in f]
        l = []
        l.clear()
        for testcase in lines:
            if ext==".c":
                p1 =  subprocess.run("./testcodes\\"+str(os.path.splitext(cls.code_name)[0]+" "+testcase),stdout=subprocess.PIPE,text=True)
                print(p1.stdout)
                l.append(p1.stdout)
            elif ext==".java":
                p1 =  subprocess.run("java "+" "+cls.abs_path+"\\"+cls.code_name+" "+testcase,stdout=subprocess.PIPE,text=True,shell=True)
                print(p1.stdout)
                l.append(p1.stdout)
            elif ext==".py":
                p1 =  subprocess.run("py -3.8"+" "+cls.abs_path+"\\"+cls.code_name+" "+testcase,stdout=subprocess.PIPE,text=True,shell=True)
                l.append(p1.stdout)
            elif ext==".cpp":
                p1 =  subprocess.run("./testcodes\\"+str(os.path.splitext(cls.code_name)[0]+" "+testcase),stdout=subprocess.PIPE,text=True)
                l.append(p1.stdout)
        Os_file_manipulation.test_result_in_txt(1,l)