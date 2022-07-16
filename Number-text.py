	
# Global Array storing word for each digit
arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
 
def number_2_word(n):
 
    # If all the digits are encountered return blank string
    if(n==0):
        return ""
     
    else:
        # compute spelling for the last digit
        small_ans = arr[n%10]
 
        # keep computing for the previous digits and add the spelling for the last digit
        ans = number_2_word(int(n/10)) + small_ans + " "
     
    # Return the final answer
    return ans
 
n = int(input("Enter the number: "))
print("Number Entered was : ", n)
print(f"Converted to word it becomes: {number_2_word(n)}")



# from num2words import num2words

# Number = int(input("enter the number: "))
# print(num2words(Number, lang="es") )