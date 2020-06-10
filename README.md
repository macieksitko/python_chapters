# python_chapters
3 chapters of Python code

1. [Chapter 1](#chapter-1)
2. [Chapter 2](#chapter-2)
3. [Chapter 3](#chapter-3)

## Chapter 1

This program contains 2 classes, Car and InvalidCarExeption. 

Car class receives 3 arguments: pax_count, car_mass, gear_count.
Creating an object or assiging values to existing object is constrainted by some circumstances (pax_count c (1,5), car_mass <= 2000)
Car class has got attribute total_mass, which returns car_mass. 

Example:

c = Car(3,2000,1)

Result: Car added successfully!



wrongcar = Car(5,2100,1)

Result: Error: Car_mass out of range InvalidCarMassError



c.pax_count = 6

Result: Error: Pax_count out of range InvalidPaxCountError



c = Car(3,2000,1)

print(c.total_mass())

Result: 2210


## Chapter 2

This is command-line script to manage a task list. 

### Guide to use this script.

Below are all commands you can put in your commanand-line. In case of any problem, use --help command.

NAME is a task name

DEADLINE is a ultimate date of finishing a task

DESPRIPTION is a short additional information about your task

All tasks have got unique HASH required to update or remove specific task.

usage: chapter2.py [-h] {add,update,remove,list} ...

chapter2.py -h

optional arguments:
  -h, --help            show this help message and exit

subcommands:

  {add,update,remove,list}

    add                 add item

    update              update item

    remove              remove item

    list                show list

- chapter2.py add -h

  usage: chapter2.py add [-h] [-n NAME] [-d DEADLINE] [-s DESCRIPTION]
  optional arguments:

    -h, --help            show this help message and exit

    -n NAME, --name NAME

    -d DEADLINE, --deadline DEADLINE

    -s DESCRIPTION, --description DESCRIPTION

- chapter2.py update -h

  usage: chapter2.py update [-h] [-n NAME] [-d DEADLINE] [-s DESCRIPTION]
                            hash_to_update

  positional arguments:
    hash_to_update

  optional arguments:

    -h, --help            show this help message and exit

    -n NAME, --name NAME

    -d DEADLINE, --deadline DEADLINE

    -s DESCRIPTION, --description DESCRIPTION

- chapter2.py remove -h
  usage: chapter2.py remove [-h] hash_to_remove

  positional arguments:
    hash_to_remove

- chapter2.py list -h  
  usage: chapter2.py list [-h] [-a] [-t]

  optional arguments:

    -h, --help   show this help message and exit

    -a, --all

    -t, --today 


## Chapter 3

This program finds amount of solutions for given problem. 

A number that is a solution fulfills following rules:

1. There are at least two groups of identical adjacent digits
2. Going from left to right, the digits never decrease
3. It is a number in the range between 372^2 and 809^2 (both ends inclusive).
