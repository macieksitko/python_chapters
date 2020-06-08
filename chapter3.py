def main():

    min_num = 372**2
    max_num = 809**2
   
    found = 0
    for number in range(min_num,max_num):
        ident_digits = 1
        ident_group = 0
        increased_digits = True 
        number = str(number)
        for i in range(0,len(number)-1):
            if number[i] == number[i+1]:
                ident_digits += 1
            else:
                ident_digits = 1
            if ident_digits >= 2 and number[i-1]!=number[i]:
                ident_group+=1
            if number[i] > number[i+1]: increased_digits = False
            
        if increased_digits == True and ident_group >=2: 
            found += 1 
            print(number)
    print ("The answer is: {}".format(found))

main()


                




