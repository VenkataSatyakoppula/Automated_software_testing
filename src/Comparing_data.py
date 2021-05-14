from Os_file_manipulation import Os_file_manipulation

class Compare(Os_file_manipulation):
    @classmethod
    def comparing_values(cls):
        cus_outputs =  Os_file_manipulation.read_outputs(0)
        outputs =  Os_file_manipulation.read_outputs(1)
        result = []
        count =0
        while count<len(outputs):
            if(cus_outputs[count]==outputs[count]):
                result.append(f"TESTCASE {count+1}: PASSED!")
            else:
                result.append(f"TESTCASE {count+1}: FAILED!") 
            count += 1
        Os_file_manipulation.test_result_in_txt(0,result)