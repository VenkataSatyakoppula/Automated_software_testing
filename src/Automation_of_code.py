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
    def execute_code(cls,n):
        if n==1:
            subprocess.run("gcc -o "+cls.abs_path+"\\"+str(os.path.splitext(cls.code_name)[0])+" "+cls.abs_path+"\\"+cls.code_name,shell=True)
        elif n==2:
            subprocess.run("javac "+" "+cls.abs_path+"\\"+cls.code_name,shell=True)
        with open('testcases.txt') as f:
            lines = [line.rstrip() for line in f]
        l = []
        for testcase in lines:
            if n==1:
                p1 =  subprocess.run("./testcodes\\"+str(os.path.splitext(cls.code_name)[0]+" "+testcase),stdout=subprocess.PIPE,text=True)
                print(p1.stdout)
            elif n==2:
                p1 =  subprocess.run("java "+" "+cls.abs_path+"\\"+cls.code_name+" "+testcase,stdout=subprocess.PIPE,text=True,shell=True)
                l.append(p1.stdout)
        print(l)


