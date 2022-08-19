"""

01
KG
123
ABC

"""


import re


class ValidCarNumber:
    def is_valid(self, number):
        self.number = number
        is_valid = re.search(r'.+01KG([0-9]{3})([A-Z]{3})', number)
        print(is_valid)
        try:
            if self.number[is_valid.start():is_valid.end()] == number:
                print('Car Number is valid!')

        except:
            print('Car Number is invalid!')



num = ValidCarNumber()
print(num.is_valid(input()))
