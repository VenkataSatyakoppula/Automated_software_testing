from posixpath import split
from Os_file_manipulation import Os_file_manipulation
import subprocess,os
import shutil,sys
class Automation_of_code:
    code_path = ""
    code_name = "c_program.c"
    @classmethod
    def get_code_path(cls,path):
        cls.code_path = path
        cls.code_name = os.path.basename(cls.code_path)
        dest_path= "E:\\Projects\\Automated_software_testing\\testcodes\\"+cls.code_name
        shutil.copyfile(cls.code_path,dest_path)
    @classmethod
    def execute_code(cls):
        subprocess.run("gcc -o "+"E:\\Projects\\Automated_software_testing\\testcodes\\"+str(os.path.splitext(cls.code_name)[0])+" E:\\Projects\\Automated_software_testing\\testcodes\\"+cls.code_name,shell=True)
        subprocess.run("./testcodes\\"+str(os.path.splitext(cls.code_name)[0]))
        subprocess.run("py -3.8 Automation_of_code.py)") 
a = Automation_of_code()

a.execute_code()