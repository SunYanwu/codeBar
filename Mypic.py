#生成一个二维码
import math
import random

import cairo
def creatNumber(num):
    left_guard = "101"
    right_guard = "101"
    center_guard = "01010"
    dict_lcode = {0: "0001101", 1: "0011001", 2: "0010011", 3: "0111101", 4: "0100011", 5: "0110001", 6: "0101111",
                  7: "0111011", 8: "0110111", 9: "0001011"}
    dict_rcode = {0: "1110010", 1: "1100110", 2: "1101100", 3: "1000010", 4: "1011100",
                  5: "1001110", 6: "1010000", 7: "1000100", 8: "1001000", 9: "1110100"}
    number = num
    number_list = [0] + [int(c) for c in number]
    check1 = 3 * sum(number_list[::2]) + sum(number_list[1::2])
    check2 = 10 - check1 % 10
    if check2 == 10:
        check2 = 0
    number_list.append(check2)
    code = left_guard
    for i in range(6):
        code += dict_lcode[number_list[i]]
    code += center_guard
    for i in range(6, 12):
        code += dict_rcode[number_list[i]]
    code += right_guard
    return code;

def draw_code(ctx, code,r,g,b,x,y):
    width_per_code = 3
    height_per_code = 200
    ctx.set_source_rgb(r, g, b)
    for i, c in enumerate(code):
        xpos = x+width_per_code * i
        if c=="1":
            ctx.rectangle(xpos, y, width_per_code, height_per_code)
            ctx.fill()

if __name__ == '__main__':
    WIDTH, HEIGHT = 1600, 1600
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(1, 1, 1)
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.fill_preserve()
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()
    code = creatNumber("1234569852")
    for y in range(50,1600,400):
        r = 0
        for x in range(50,1600,400):
            Number = random.randint(1000000000,9999999999)
            code = creatNumber("1234569852")
            draw_code(ctx,code,r,r,r,x,y)
            r = r +0.3
            for k in range(15 * (y + 1)):  # 噪点添加
                ctx.arc(random.randint(x, x+300), random.randint(y, y + 200), 0.5, 0, 0.5 * math.pi)
                ctx.stroke()
    surface.write_to_png ("barcode1.png") # Output to PNG


