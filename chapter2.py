import sys
import argparse
from datetime import date


myList=[]

def main():

    #creating a main parser and subparser
    my_parser = argparse.ArgumentParser()
    subparsers = my_parser.add_subparsers(title="subcommands")

    #add parsers and its arguments
    parser_a = subparsers.add_parser('add', help='add item')
    parser_a.set_defaults(func=add)

    parser_a.add_argument('-n','--name',action="store")
    parser_a.add_argument('-d','--deadline',action="store")
    parser_a.add_argument('-s','--description',action="store")

    #update parsers and its arguments
    parser_b = subparsers.add_parser('update', help='update item')
    parser_b.set_defaults(func=update)

    parser_b.add_argument('-n','--name',action="store")
    parser_b.add_argument('-d','--deadline',action="store")
    parser_b.add_argument('-s','--description',action="store")
    parser_b.add_argument('hash_to_update', action='store')

    #remove parsers and its arguments
    parser_c = subparsers.add_parser('remove',help='remove item')
    parser_c.add_argument('hash_to_remove',action='store')
    parser_c.set_defaults(func=remove)

    #list parsers and its arguments
    parser_d = subparsers.add_parser('list',help='show list')
    parser_d.set_defaults(func=show_list)
    parser_d.add_argument('-a','--all',action="store_true")
    parser_d.add_argument('-t','--today',action="store_true")


    args = my_parser.parse_args() #parsing all args

    args.func(args) #invoking functions

def add(args):
    
    #searching for the last line of a file to check if there is \n
    with open("tasklist.txt", "r") as file:
        for last_line in file:
            pass
    
    with open("tasklist.txt","a+") as f:
        element = []
        hash_str = "{}{}{}".format(args.name,args.deadline,args.description) 
        hash_id = hash(hash_str)    #hashing contents of a task

        #appending all arguments to 'element' list

        element.append(str(hash_id)) 
        element.append(args.name)
        element.append(args.deadline)
        element.append(args.description)
        
        data = f.read()

        #condition statemnt that adds element to the file, but if that is not the first item, it adds \n sign before
        if len(data) > 0 :
            f.seek(0,2)
            if not "\n" in last_line: f.write("\n")
            f.write(', '.join(element))
        else:
            f.write(', '.join(element))
        f.close()
def update(args):
    element = []
    element.append(args.name)
    element.append(args.deadline)
    element.append(args.description)

    #hash_to_update variable stores a hash given by the user as the last argument in the command line
    hash_to_update = sys.argv[-1]

    i = 0

    #searching for index of a record that contains hash_to_update
    with open('tasklist.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if hash_to_update in line:
                index = i
            i=i+1

    #editing line where hash was found
    lines[index] = "{}, {}, {}, {}\n".format(hash_to_update,args.name,args.deadline,args.description)

    #overwriting a file with changed line
    with open('tasklist.txt', 'w') as f:
        f.writelines(lines)
    
        f.close()
def remove(args):

    #hash_to_remove contains a hash given by user to remove from a list
    hash_to_remove = sys.argv[-1]

    with open('tasklist.txt', 'r') as f:
        lines = f.readlines()
    with open('tasklist.txt', 'w') as f:
        for line in lines:
            if line.find(hash_to_remove):
                f.write(line)
        f.close()

def show_list(args):
    any_today = False       #boolean variable to check if there is any today date in a file
    now = str(date.today()) #now stores today date

    print("Today is: {}".format(now))

    #condition statement checks if user typed -t command amd if so, show the tasks only for today
    if (sys.argv[-1] == '--today' or sys.argv[-1] == '-t' ):
        with open('tasklist.txt', 'r') as f:
            lines = f.readlines()
            print("------------TASK LIST-----------")
            print("hash--------name-----deadline-----description")

            #searching for today date in a file line by line
            for line in lines:
                #if found, rstrip \n sign and print the line
                if now in line:
                    line = line.rstrip("\n")
                    print(line)

                else: any_today = True #if not found, set any_today to True and print a communicate after that
        if any_today : print("Found no tasks today")
    else:
        with open('tasklist.txt', 'r') as f:
            lines = f.readlines()
            print("------------TASK LIST-----------")
            print("hash--------name-----deadline-----description")
            for line in lines:
                line = line.rstrip("\n")
                line = line.replace(',', '')
                print(line)
                print("--------------------------------")
    f.close()
if __name__ == '__main__':
    main()

    