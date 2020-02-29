import sys 




def counting_sheep(num):
    if num == 0:
        return 'INSOMNIA'
    else:
        
            


        return None


if __name__ == "__main__":
    print("Enter number of test cases:")
    num_test_cases = int(input())
    for i in range(num_test_cases):
        print("Enter number:")
        num = int(input())
        ret = counting_sheep(num)
        print("CASE #"+num+":"+"    "+ret)
