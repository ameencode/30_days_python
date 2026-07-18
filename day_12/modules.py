import random
import string

def random_user_id():
    alphanumeric = string.ascii_letters + string.digits
    for _ in range(6):
        return "".join(random.choices(alphanumeric, k=6))
    
print(random_user_id())

def user_id_gen_by_user():
    alpha_num = string.ascii_letters + string.digits
    num_char = int(input('How many characters do you want? '))
    num_id = int(input('How many ID would you like to generate? '))

    for _ in range(num_id):
        new_id = "".join(random.choices(alpha_num, k= num_char))
        print(new_id)
       
user_id_gen_by_user()   
#print(user_id_gen_by_user())

'''
def rgb_color_gen():

    rgb_num = range(0, 256)
    #rgb = ()

    for num in rgb_num:
        if num >= 100:
            value = (random.choices(rgb_num, k=3))
    return value 
print(rgb_color_gen())
'''

# A better method
def rgb_color_gene():
    color_list = random.choices(range(0, 256), k=3)
    return tuple(color_list)

print(rgb_color_gene())

# formatting to :03d
def rgb_color_gene():
    color_list = random.choices(range(0, 256), k=3)

    r = f"{color_list[0]:03d}"
    g = f"{color_list[1]:03d}"
    b = f"{color_list[2]:03d}"

    return f"rgb({r}, {g}, {b})"

print(rgb_color_gene())