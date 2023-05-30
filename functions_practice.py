def hello():
    print('Hello user!')

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

def eat_lunch(food_list):
    if len(food_list) == 0:
        print("My lunch box is empty!")
    else:
        print("first I eat ", food_list[0])
        for food in food_list[1:]:
            print("Next I eat ", food)
    
