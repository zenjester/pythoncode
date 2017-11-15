#pizza3.py pizza house without classes
#andyp 13.09.13
#TODO needs error checking

def num_enter(num_value, num_list):
    if num_value not in num_list:
        print('Enter a valid number')
    return


def enter_pizza(num_of_pizza):  #TODO combine these two and use pizza
    print('Pablos Pizza Palace')
    print('===================')
    print('')
    print('How many pizza you want ?')
    while num_of_pizza not in five:
        num_of_pizza = int(input('enter a number'))
        print(num_of_pizza)  # TODO better dialog
        num_enter(num_of_pizza, five)
    return num_of_pizza


def create_pizza(pizza_siza):
    print('Enter your size of pizza')
    print('Enter 1 for small, 2 for medium or 3 for large')
    while pizza_siza not in three:
        pizza_siza = int(input('enter a number'))
        print(pizza_siza)  # TODO better dialog
        num_enter(pizza_siza, three)
    return pizza_siza


def choose_toppings():
    print('Choose up to 3 toppings')
    print('=======================')
    print_toppings()
    print('How many toppings do you want')
    num_tops = 9
    top_count = 0
    while num_tops not in five:
        num_tops = int(input('Enter Number of toppings'))
        num_enter(num_tops, five)
        print('')
    while top_count < num_tops:
        print('Choose a topping')
        print_toppings()
        top_choice = int(input('Enter a topping choice'))
        num_enter(top_choice, five)
        tops[top_count] = top_choice - 1
        top_count += 1
    return ()


def print_toppings():  # only works because I only have five toppings
    for n in range(0, 5):
        print(n + 1 , topping[n])
    print('')
    return


def print_pizza():
    print('This is your order')
    print('==================\n')
    count=0
    while choice[count][0] != 0:
        print('your', cardinal[0], 'pizza is')
        print('a', size[choice[count][0]-1], topping[choice[count][1]], topping[choice[count][2]], topping[choice[count][2]])
        print(choice[count])  #test prnt
        count+=1
    return

#variable declaration
#tuples and lists


three = (1, 2, 3)
five = (1, 2, 3, 4, 5)
pizza = [0,5,5,5]
psize = 0
choice = [pizza, pizza, pizza, pizza, pizza]
cardinal = ['first','second','third','fourth','fifth']
topping = ('chicken', 'beef', 'pepperoni', 'ham', 'sweetcorn','none')
size = ('small', 'medium', 'large')
tops = [5, 5, 5]  #TODO think about a dictionary

#global variables
in_pizza = 9
in_siza = 9
count = 0
#main_loop
# TODO display each pizza
# TODO claculate bill
ordered_pizzas = enter_pizza(in_pizza)
while count < ordered_pizzas:
    psize = create_pizza(in_pizza)
    choose_toppings()
    choice[count] = [psize, tops[0], tops[1], tops[2]]
    count += 1

print_pizza()

