from Os_file_manipulation import Os_file_manipulation

class Comparing_values(Os_file_manipulation):
    @classmethod
    def comparing_values(cls):
        cus_outputs =  Os_file_manipulation.read_outputs(0)
        outputs =  Os_file_manipulation.read_outputs(1)
        compare_result = []
        count =0
        while count<len(outputs):
            if(cus_outputs[count]==outputs[count]):
                compare_result.append(f"TESTCASE {count+1}({cus_outputs[count]}=={outputs[count]}): PASSED!")
            else:
                compare_result.append(f"TESTCASE {count+1}({cus_outputs[count]}!={outputs[count]}): FAILED!") 
            count += 1
        Os_file_manipulation.test_result_in_txt(0,compare_result)