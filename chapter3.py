def main():

    #min and max numbers
    min_num = 372**2
    max_num = 809**2
   
    found = 0  #found numbers counter
    for number in range(min_num,max_num):
        ident_digits = 1  #number of identical digits in a number
        ident_group = 0   #number of idenitcal digits group greater than 2
        increased_digits = True  #if digits are increasing in a number
        number = str(number)
        for i in range(0,len(number)-1):
            if number[i] == number[i+1]:  #if a digit and the next digit are the same, increase ident_digits
                ident_digits += 1
            else:
                ident_digits = 1          #else, set it on 1 again
            
            if ident_digits >= 2 and number[i-1]!=number[i]:  #if there are at least 2 indentical digits and it is the last digit from this group, increase ident_group
                ident_group+=1
            if number[i] > number[i+1]: increased_digits = False #if there is any number on the left greater than the right one, the digits are not increasing from left to the right
            
        if increased_digits == True and ident_group >=2:   #if all conditions are satisfied, increase found
            found += 1 
            print(number)
    print ("The answer is: {}".format(found))

main()


                




