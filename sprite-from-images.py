import glob
import sys
from os.path import join

from PIL import Image

_, path, size_x_str, size_y_str, output_file_name, rotation_str = sys.argv

print("Target size: (", size_x_str, ",", size_y_str, ")")
size_x = int(size_x_str)
size_y = int(size_y_str)
rotation = int(rotation_str)

images = [file for file in sorted(glob.glob(path))]
images_pil = [Image.open(join(path, image)).rotate(rotation, expand=True)
              .resize((size_x, size_y)) for image in images]

sprite = Image.new('RGBA', (len(images_pil) * size_x, size_y))

for index, tile in enumerate(images_pil):
    sprite.paste(tile, (index*size_x, 0))

sprite.save(output_file_name)
sprite.show()

