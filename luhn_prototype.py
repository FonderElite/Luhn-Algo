import random,math
from colorama import Fore as fg
global key 
values = [] 
second_val = []
squared = []
greater_than_9 = []
added_values = []
res = []
generated = []
bold_color = '\033[1m'

class LuhnAlgo(object):
    def __init__(self,digits):
        self.digits = digits
    def generate(self):
     for i in range(self.digits):
         gen = lambda x : random.randint(0,x)
         values.append(gen(9))
     for index in range(1,len(values),2):
         second_val.append(values[index])
     for i in second_val:
         squared.append(i * 2)
     get_val9 = [x for x in squared if x > 9]
     greater_than_9.append(get_val9)
    
    @staticmethod
    def two_digit_sum():
        for i in squared:
            sum = 0
            for digit in str(i):
                sum+=int(digit)
            res.append(sum)

    @staticmethod
    def validate():
        values[1::2] = res
        generated.append(values)
        flattened = []
        for sublist in generated:
            for val in sublist:
                flattened.append(val)
        validity = sum(flattened)
        new_lst = str(flattened)[1:-1]
        remove_comma = new_lst.replace(',','')
        remove_whitespace = remove_comma.replace(' ','')
        print(values)
        if validity % 10 == 0:
            print(bold_color + fg.GREEN +  "Valid: " + "".join(str(remove_whitespace).strip()) +fg.WHITE)
        else:
            print(bold_color + fg.RED + "Invalid: " + "".join(str(remove_whitespace).strip()) + fg.WHITE)

if __name__ == "__main__":
    luhnclass = LuhnAlgo(13)
    generate_valid = luhnclass.generate()
    twodigitsum = luhnclass.two_digit_sum()
    remove_secondel = luhnclass.validate()

