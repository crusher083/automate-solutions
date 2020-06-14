from PIL import ImageGrab, ImageOps
from numpy import *
from os import getcwd, makedirs
from time import time, sleep
import win32api
import win32con
"""
All coordinates assume a screen resolution of 1920x1024, and Chrome 
100% scaled with the Bookmarks Toolbar disabled.
Down was pressed 2 times
x_pad = 243
y_pad = 383
Play area =  x_pad+1, y_pad+1, 1048, 987
"""
x_pad = 165
y_pad = 305


def screen_grab():
    box = (x_pad+1, y_pad+1, x_pad+893, y_pad+670)
    im = ImageGrab.grab(box)
    im.save(getcwd() + '\\snaps\\Snap__' + str(int(time())) +
            '.png', 'PNG')
    return im


def grab():
    box = (x_pad + 1, y_pad+1, x_pad+893, y_pad+670)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a


def l_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print("Click.")          # completely optional. But nice for debugging purposes.


def left_down():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(.1)
    print('left Down')


def left_up():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    sleep(.1)
    print('left release')


def mouse_pos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(f"{x}, {y}")


def start():
    # location of first menu
    mouse_pos((250, 128))
    l_click()
    sleep(.1)
    # location of second menu
    mouse_pos((261, 306))
    l_click()
    sleep(.1)
    # location of tutorial skip
    mouse_pos((533, 371))
    l_click()
    sleep(.1)
    # today's goal continue
    mouse_pos((268, 286))
    l_click()
    sleep(.1)


class Cord:
    f_shrimp = (-10, 254)
    f_rice = (43, 246)
    f_nori = (-18, 300)
    f_roe = (40, 304)
    f_salmon = (-5, 353)
    f_unagi = (36, 352)
    phone = (531, 285)
    menu_toppings = (505, 186)
    t_shrimp = (445, 134)
    t_nori = (414, 174)
    t_roe = (502, 183)
    t_salmon = (418, 239)
    t_unagi = (504, 129)
    t_exit = (547, 254)
    menu_rice = (489, 209)
    buy_rice = (466, 191)
    delivery_norm = (440, 211)


"""

Plate cords:

    40, 123
    132, 123
    233, 123
    344, 123
    439, 123
    551, 123
"""


def clear_tables():
    mouse_pos((40, 123))
    l_click()
    mouse_pos((132, 123))
    l_click()
    mouse_pos((233, 123))
    l_click()
    mouse_pos((344, 123))
    l_click()
    mouse_pos((439, 123))
    l_click()
    mouse_pos((551, 123))
    l_click()
    sleep(1)


def fold_mat():
    mouse_pos((124, 253))
    l_click()
    sleep(.1)
    
    
def make_food(food):
    '''
    Recipes:
        onigiri:
        2 rice, 1 nori
        caliroll:
        1 rice, 1 nori, 1 roe
        gunkan:
        1 rice, 1 nori, 2 roe
    '''
    if food == 'caliroll':
        print('Making a caliroll')
        food_stack['rice'] -= 1
        food_stack['nori'] -= 1
        food_stack['roe'] -= 1
        mouse_pos(Cord.f_rice)
        l_click()
        sleep(.05)
        mouse_pos(Cord.f_nori)
        l_click()
        sleep(.05)
        mouse_pos(Cord.f_roe)
        l_click()
        sleep(.1)
        fold_mat()
        sleep(1.5)
    elif food == 'onigiri':
        print('Making a onigiri')
        food_stack['rice'] -= 2
        food_stack['nori'] -= 1
        mouse_pos(Cord.f_rice)
        l_click()
        sleep(.05)
        mouse_pos(Cord.f_rice)
        l_click()
        sleep(.05)
        mouse_pos(Cord.f_nori)
        l_click()
        sleep(.1)
        fold_mat()
        sleep(.05)
        sleep(1.5)
    elif food == 'gunkan':
        print('Making a gunkan')
        food_stack['rice'] -= 1
        food_stack['nori'] -= 1
        food_stack['roe'] -= 2
        mouse_pos(Cord.f_rice)
        l_click()
        sleep(.05)
        mouse_pos(Cord.f_nori)
        l_click()
        sleep(.05)
        mouse_pos(Cord.f_roe)
        l_click()
        sleep(.05)
        mouse_pos(Cord.f_roe)
        l_click()
        sleep(.1)
        fold_mat()
        sleep(1.5)


def buy_food(food):
    if food == 'rice':
        mouse_pos(Cord.phone)
        sleep(.1)
        l_click()
        mouse_pos(Cord.menu_rice)
        sleep(.05)
        l_click()
        s = screen_grab()
        if s.getpixel(Cord.buy_rice) != (118, 83, 85):
            print('rice is available')
            mouse_pos(Cord.buy_rice)
            sleep(.1)
            l_click()
            mouse_pos(Cord.delivery_norm)
            food_stack['rice'] += 10
            sleep(.1)
            l_click()
            sleep(2.5)
        else:
            print('rice is NOT available')
            mouse_pos(Cord.t_exit)
            l_click()
            sleep(1)
            buy_food(food)
    if food == 'nori':
        mouse_pos(Cord.phone)
        sleep(.1)
        l_click()
        mouse_pos(Cord.menu_toppings)
        sleep(.05)
        l_click()
        s = screen_grab()
        print('test')
        sleep(.1)
        if s.getpixel(Cord.t_nori) != (109, 123, 127):
            print('nori is available')
            mouse_pos(Cord.t_nori)
            sleep(.1)
            l_click()
            mouse_pos(Cord.delivery_norm)
            food_stack['nori'] += 10
            sleep(.1)
            l_click()
            sleep(2.5)
        else:
            print('nori is NOT available')
            mouse_pos(Cord.t_exit)
            l_click()
            sleep(1)
            buy_food(food)
    if food == 'roe':
        mouse_pos(Cord.phone)
        sleep(.1)
        l_click()
        mouse_pos(Cord.menu_toppings)
        sleep(.05)
        l_click()
        s = screen_grab()
        sleep(.1)
        if s.getpixel(Cord.t_roe) != (109, 123, 127):
            print('roe is available')
            mouse_pos(Cord.t_roe)
            sleep(.1)
            l_click()
            mouse_pos(Cord.delivery_norm)
            food_stack['roe'] += 10
            sleep(.1)
            l_click()
            sleep(2.5)
        else:
            print('roe is NOT available')
            mouse_pos(Cord.t_exit)
            l_click()
            sleep(1)
            buy_food(food)


food_stack = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}


def check_food():
    for i, j in food_stack.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print(f'{i} is low and needs to be replenished')
                buy_food(i)


def get_seat_one(x, y, box_w, box_h):
    box = (x_pad + x, y_pad + y, x_pad + x + box_w, y_pad + y + box_h)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(getcwd() + '\\seats\\seat_1__' + str(int(time())) + '.png', 'PNG')
    return a


def get_seat_two(x, y, box_w, box_h):
    box = (x_pad + x, y_pad + y, x_pad + x + box_w, y_pad + y + box_h)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(getcwd() + '\\seats\\seat_2__' + str(int(time())) + '.png', 'PNG')
    return a


def get_seat_three(x, y, box_w, box_h):
    box = (x_pad + x, y_pad + y, x_pad + x + box_w, y_pad + y + box_h)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(getcwd() + '\\seats\\seat_3__' + str(int(time())) + '.png', 'PNG')
    return a


def get_seat_four(x, y, box_w, box_h):
    box = (x_pad + x, y_pad + y, x_pad + x + box_w, y_pad + y + box_h)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(getcwd() + '\\seats\\seat_4__' + str(int(time())) + '.png', 'PNG')
    return a


def get_seat_five(x, y, box_w, box_h):
    box = (x_pad + x, y_pad + y, x_pad + x + box_w, y_pad + y + box_h)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(getcwd() + '\\seats\\seat_5__' + str(int(time())) + '.png', 'PNG')
    return a


def get_seat_six(x, y, box_w, box_h):
    box = (x_pad + x, y_pad + y, x_pad + x + box_w, y_pad + y + box_h)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)

    im.save(getcwd() + '\\seats\\seat_6__' + str(int(time())) + '.png', 'PNG')
    return a


def get_all_seats():
    box_w = 79
    box_h = 18
    get_seat_one(38, 85, box_w, box_h)
    get_seat_two(179, 85, box_w, box_h)
    get_seat_three(321, 85, box_w, box_h)
    get_seat_four(461, 85, box_w, box_h)
    get_seat_five(602, 85, box_w, box_h)
    get_seat_six(743, 85, box_w, box_h)


class RangeDict(dict):
    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)


sushi_type = RangeDict({range(6000, 7400): 'onigiri',
             range(8400, 9800) : 'caliroll',
            range(4400, 5500): 'gunkan'})


class Blank:
    seat_1 = 11876
    seat_2 = 11423
    seat_3 = 15335
    seat_4 = 16732
    seat_5 = 12158
    seat_6 = 15226


def check_bubs():
    box_w = 79
    box_h = 18
    check_food()
    s1 = get_seat_one(38, 85, box_w, box_h)
    if s1 != Blank.seat_1:
        for key in sushi_type.keys():
            if s1 in key:
                print(f'table 1 is occupied and needs {sushi_type[s1]}')
                make_food(sushi_type[s1])
        else:
            print('sushi not found!\n sushiType = %i' % s1)
    else:
        print('Table 1 unoccupied')

    clear_tables()
    check_food()
    s2 = get_seat_two(179, 85, box_w, box_h)
    if s2 != Blank.seat_2:
        for key in sushi_type.keys():
            if s2 in key:
                print('table 2 is occupied and needs %s' % sushi_type[s2])
                make_food(sushi_type[s2])
        else:
            print('sushi not found!\n sushiType = %i' % s2)
    else:
        print('Table 2 unoccupied')

    check_food()
    s3 = get_seat_three(321, 85, box_w, box_h)
    if s3 != Blank.seat_3:
        for key in sushi_type.keys():
            if s3 in key:
                print('table 3 is occupied and needs %s' % sushi_type[s3])
                make_food(sushi_type[s3])
        else:
            print('sushi not found!\n sushiType = %i' % s3)
    else:
        print('Table 3 unoccupied')

    check_food()
    s4 = get_seat_four(461, 85, box_w, box_h)
    if s4 != Blank.seat_4:
        for key in sushi_type.keys():
            if s4 in key:
                print('table 4 is occupied and needs %s' % sushi_type[s4])
                make_food(sushi_type[s4])
        else:
            print('sushi not found!\n sushiType = %i' % s4)
    else:
        print('Table 4 unoccupied')

    clear_tables()
    check_food()
    s5 = get_seat_five(602, 85, box_w, box_h)
    if s5 != Blank.seat_5:
        for key in sushi_type.keys():
            if s5 in key:
                print('table 5 is occupied and needs %s' % sushi_type[s5])
                make_food(sushi_type[s5])
        else:
            print('sushi not found!\n sushiType = %i' % s5)
    else:
        print('Table 5 unoccupied')

    check_food()
    s6 = get_seat_six(743, 85, box_w, box_h)
    if s6 != Blank.seat_6:
        for key in sushi_type.keys():
            if s5 in key:
                print('table 1 is occupied and needs %s' % sushi_type[s6])
                make_food(sushi_type[s6])
        else:
            print('sushi not found!\n sushiType = %i' % s6)
    else:
        print('Table 6 unoccupied')
    clear_tables()


def main():
    try:
        makedirs('seats', exist_ok=True)
        makedirs('snaps', exist_ok=True)
        start()
        while True:
            check_bubs()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
