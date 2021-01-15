#encoding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from PIL import Image

def get_cmap(path):
    #获取图片路径

    picture = np.array(Image.open( path ).resize((500, 300)))

    Colorful_picture = np.array(Image.open( path ).resize((5, 3)))

    height = np.zeros((1, 5 * 3))
    for i in range (3):
        for j in range (5):
            r = Colorful_picture[i][j][2]
            g = Colorful_picture[i][j][1]
            b = Colorful_picture[i][j][0]
            height[0][5*i + j] = (r+g)/2 -b

    RGB_num = [[]]
    for i in range(3):
        for j in range(5):
            RGB_num[0].append(Colorful_picture[i][j])
    RGB_num = list(RGB_num)

    Cool_Warm_chaos = list((height[0][:]))
    Cool_Warm_order = sorted(Cool_Warm_chaos)

    Cool_Warm_order = list(np.array(Cool_Warm_order).reshape(3,5))

    Cool_Warm = [[]]
    for i in range(15):
        Cool_Warm[0].append([])
    for i in range(15):
        Cool_Warm[0][i] = [169, 149, 121]

    for i in range(3):
        for j in range(5):
            RGB_index = Cool_Warm_chaos.index(Cool_Warm_order[i][j])
            Cool_Warm[0][5*i+j] = RGB_num[0][RGB_index]

#绘图
    plt.style.use('dark_background')
    fig, (ax1, ax2, ax3) = plt.subplots(3,1)

    ax1.imshow(picture)
    ax1.axis('off')
    ax2.imshow(Colorful_picture)
    ax2.axis('off')
    im = ax3.imshow(Cool_Warm)
    for i in range (15):
        r = Cool_Warm[0][i][2]
        g = Cool_Warm[0][i][1]
        b = Cool_Warm[0][i][0]
        description = 'RGB:\n'+str(r)+'\n'+str(g)+'\n'+str(b)
        text = ax3.text(i, 0, description,
                        ha="center", va="center", color="w")
    ax3.axis('off')
    plt.savefig('C:/Users/hx893/Desktop/get_cmap.png')
    #plt.show()
