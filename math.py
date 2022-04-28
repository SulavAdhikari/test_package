class Calculator:
    def sum(self,*args):
        sum = 0
        for i in args:    sum +=i
        return sum

    def divide(self, num1, num2):
        result = num1/num2
        return result

    def multiply(self, *args):
        result = 1
        for i in args: result *= i
        return result

    

            
                
            

                

        