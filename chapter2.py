import sys
import argparse
from datetime import date


myList=[]

def main():


    my_parser = argparse.ArgumentParser()
    subparsers = my_parser.add_subparsers(title="subcommands")

    #add parsers
    parser_a = subparsers.add_parser('add', help='add item')
    parser_a.set_defaults(func=add)

    parser_a.add_argument('-n','--name',action="store")
    parser_a.add_argument('-d','--deadline',action="store")
    parser_a.add_argument('-s','--description',action="store")

    #update parsers
    parser_b = subparsers.add_parser('update', help='update item')
    parser_b.set_defaults(func=update)

    parser_b.add_argument('-n','--name',action="store")
    parser_b.add_argument('-d','--deadline',action="store")
    parser_b.add_argument('-s','--description',action="store")
    parser_b.add_argument('hash_to_update', action='store')

    #remove parsers
    parser_c = subparsers.add_parser('remove',help='remove item')
    parser_c.add_argument('hash_to_remove',action='store')
    parser_c.set_defaults(func=remove)
    #list parsers
    parser_d = subparsers.add_parser('list',help='show list')
    parser_d.set_defaults(func=show_list)
    parser_d.add_argument('-a','--all',action="store_true")
    parser_d.add_argument('-t','--today',action="store_true")


    args = my_parser.parse_args()
    args.func(args)

def add(args):
    with open("tasklist.txt","a+") as f:
        element = []
        hash_str = "{}{}{}".format(args.name,args.deadline,args.description)
        hash_id = hash(hash_str)
        element.append(str(hash_id))
        element.append(args.name)
        element.append(args.deadline)
        element.append(args.description)
        
        data = f.read()
        print(len(data))
        if len(data) > 0 :
            f.seek(0,2)
            f.write("\n")
            f.write(', '.join(element))
        else:
            f.write(', '.join(element))
        f.close()
def update(args):
    element = []
    element.append(args.name)
    element.append(args.deadline)
    element.append(args.description)


    hash_to_update = sys.argv[-1]
    print(hash_to_update)
    i = 0
    with open('tasklist.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if hash_to_update in line:
                index = i
            i=i+1


    lines[index] = "{}, {}, {}, {}".format(hash_to_update,args.name,args.deadline,args.description)

    with open('tasklist.txt', 'w') as f:
        f.writelines(lines)
    
        f.close()
def remove(args):
    hash_to_remove = sys.argv[2]
    print(sys.argv[2])

    with open('tasklist.txt', 'r') as f:
        lines = f.readlines()
    with open('tasklist.txt', 'w') as f:
        for line in lines:
            if line.find(hash_to_remove):
                f.write(line)
        f.close()
def show_list(args):
    now = str(date.today())
    print("Today is: {}".format(now))
    if (sys.argv[-1] == '--today' or sys.argv[-1] == '-t' ):
        with open('tasklist.txt', 'r') as f:
            lines = f.readlines()
            print("------------TASK LIST-----------")
            print("hash------name-----deadline-----description")
            print("\n")
            for line in lines:
                if now in line:
                    line = line.rstrip("\n")

                    print(line)
    else:
        with open('tasklist.txt', 'r') as f:
            lines = f.readlines()
            print("------------TASK LIST-----------")
            print("hash------name-----deadline-----description")
            print("\n")
            for line in lines:
                line = line.rstrip("\n")
                line = line.replace(',', '')
                print(line)
                print("--------------------------------")

if __name__ == '__main__':
    main()

    