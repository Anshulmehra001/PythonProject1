# from PIL import Image
# import os
#
# # List of your image filenames
# files = [f"{i}.png" for i in range(2, 10)]
# cleaned_paths = []
#
# for fname in files:
#     img = Image.open(f"/mnt/data/{fname}")
#     clean_name = fname.replace(".png", "_cleaned.png")
#     clean_path = f"/mnt/data/{clean_name}"
#     img.save(clean_path, icc_profile=None)
#     cleaned_paths.append(clean_name)
#
# print(cleaned_paths)

#
# from PIL import Image
# import os
#
# def clean_images(input_dir, output_dir):
#     os.makedirs(output_dir, exist_ok=True)
#
#     for filename in os.listdir(input_dir):
#         if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
#             input_path = os.path.join(input_dir, filename)
#             output_path = os.path.join(output_dir, filename)
#
#             try:
#                 with Image.open(input_path) as img:
#                     rgb_img = img.convert("RGB")
#                     rgb_img.save(output_path, icc_profile=None)
#                     print(f"Cleaned: {filename}")
#             except Exception as e:
#                 print(f"Failed to process {filename}: {e}")
#
# # Usage
# clean_images("resources/unclean", 'resources/clean')

# from PIL import Image
#
# img0 = Image.open("resources/0_cleaned.png")
# img1= Image.open("resources/1_cleaned.png")
# img2 = Image.open("resources/2_cleaned.png")
# img3 = Image.open("resources/3_cleaned.png")
# img4 = Image.open("resources/4_cleaned.png")
# img5 = Image.open("resources/5_cleaned.png")
# img6 = Image.open("resources/6_cleaned.png")
# img7 = Image.open("resources/7_cleaned.png")
# img8= Image.open("resources/8_cleaned.png")
# img9 = Image.open("resources/9_cleaned.png")
# imgbackground = Image.open("resources/background.png")
# imgbase = Image.open("resources/base.png")
# imgpipe = Image.open("resources/pipe.png")
# imgmessage = Image.open("resources/message.png")
# imgbird = Image.open("resources/bird.png")
# print(img0.size)
# print(img1.size)
# print(img2.size)
# print(img3.size)
# print(img4.size)
# print(img5.size)
# print(img6.size)
# print(img7.size)
# print(img8.size)
# print(img9.size)
# print(imgbackground.size)
# print(imgbase.size)
# print(imgbird.size)
# print(imgpipe.size)
# print(imgmessage.size)


from PIL import Image
import os

# Define sizes for each image by filename (without extension)
resize_map = {
    '0_cleaned': (24, 36),
    '1_cleaned': (24, 36),
    '2_cleaned': (24, 36),
    '3_cleaned': (24, 36),
    '4_cleaned': (24, 36),
    '5_cleaned': (24, 36),
    '6_cleaned': (24, 36),
    '7_cleaned': (24, 36),
    '8_cleaned': (24, 36),
    '9_cleaned': (24, 36),
    'background': (289, 511),
    'base': (289, 100),
    'pipe': (52, 320),
    'message': (184, 267),
    'bird': (34, 24)
}

# Set directories
input_dir = 'resources'
output_dir = 'resources/resized'
os.makedirs(output_dir, exist_ok=True)

# Resize images in bulk
for name, size in resize_map.items():
    try:
        img_path = os.path.join(input_dir, f"{name}.png")
        output_path = os.path.join(output_dir, f"{name}.png")

        with Image.open(img_path) as img:
            img = img.resize(size, Image.LANCZOS)
            img.save(output_path)
            print(f"Resized {name}.png to {size}")
    except Exception as e:
        print(f"Failed to resize {name}.png: {e}")
