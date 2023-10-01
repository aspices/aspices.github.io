import os

import numpy as np
from PIL import Image

IMG_PATH = '/Users/tincya/Desktop/space-play/expd/images/asp-about'
IMG_DST_PATH = '/Users/tincya/Desktop/space-play/expd/images/asp_brand'


# imageObject = Image.open(os.path.join(IMG_PATH, 'barn.gif'))
#
# for frame in range(0, imageObject.n_frames):
#     imageObject.seek(frame)
#     imageObject.show()

def process_image(src_folder, file_name, dst_folder):
    original = Image.open(os.path.join(src_folder, file_name))

    new_gif = []
    new_gif_duration = []
    for frame_num in range(original.n_frames):
        original.seek(frame_num)

        new_frame = Image.new('RGBA', original.size)
        new_frame.paste(original)

        # new_frame_px = new_frame.load()
        # for y in range(original.size[1]):
        #     for x in range(original.size[0]):
        #         crn_color = new_frame_px[x, y]
        #         if crn_color == (51, 204, 204, 255):
        #             new_frame.putpixel((x, y), (148, 101, 41, 255))

        # START
        data = np.array(new_frame)
        r1, g1, b1 = 51, 204, 204  # Original value
        r2, g2, b2, a2 = 148, 101, 41, 255  # Value that we want to replace it with

        red, green, blue, alpha = data[:, :, 0], data[:, :, 1], data[:, :, 2], data[:, :, 3]
        mask = ((red <= r1 + 50) | (r1 <= red + 50)) \
               & ((green - g1 <= 50) | (g1 - green <= 50)) \
               & ((blue <= b1 + 50) | (b1 <= blue + 50))
        data[:, :, :4][mask] = [r2, g2, b2, a2]
        # END

        # new_gif.append(new_frame)
        new_gif.append(Image.fromarray(data))
        new_gif_duration.append(original.info['duration'])

    new_gif[0].save(
        os.path.join(dst_folder, file_name),
        append_images=new_gif[1:], save_all=True,
        duration=new_gif_duration, loop=0, optimize=False, disposal=original.disposal_method
    )


for fl in os.listdir(IMG_PATH):
    process_image(IMG_PATH, fl, IMG_DST_PATH)
