import os
import time
import matplotlib.pyplot as plt
import PIL.Image as image


def get_count():
    return len([x for x in os.listdir(
        os.path.dirname(__file__) + '\\images\\')])


def visualization():
    count = get_count()
    counteddata = data[get_count():]

    plt.rcParams['font.sans-serif'] = ['SimHei']
    for day, dailydata in enumerate(counteddata):
        plt.barh(range(6), (100000,) + dailydata + (100000,), tick_label=[
            '', '确诊', '疑似', '治愈', '死亡', ''], color='wrygkw')
        plt.savefig(f'images\\{day + count}.png', dpi=100)
        plt.clf()


def make_gif():
    gif_frames = [image.open(os.path.dirname(__file__)
                             + f'\\images\\{day}.png')
                  for day in range(get_count())]

    gif_frames[0].save("nCoV.gif", save_all=True,
                       append_images=gif_frames[1:], duration=30)


# print('Starting request...')
# startrequest = time.time()
from request import *
# endrequest = time.time()
# print('Ending request...')
# print(f'Done request in {endrequest - startrequest}s.')

print()

print('Starting visualization...')
startvis = time.time()
visualization()
endvis = time.time()
print('Ending visualization...')
print(f'Done visualization in {endvis - startvis}s.')

print()

print('Starting making GIF...')
start_making_gif = time.time()
make_gif()
end_making_gif = time.time()
print('Ending making GIF...')
print(f'Done making GIF in {end_making_gif - start_making_gif}s.')

print()

print('All done!')
