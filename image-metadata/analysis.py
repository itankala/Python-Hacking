from PIL import Image, ExifTags
from helper.files import get_path_to_file, get_filename

def analysis(image_file):
    output_path = get_path_to_file(image_file) + "output-from-" + get_filename(image_file) + ".txt"

    img = Image.open(image_file)
    file = open(output_path, "w")
    file.write("===== " + get_filename(image_file) + " =====\n")
    for i, j in img._getexif().items():
        if i in ExifTags.TAGS:
            try:
                data = ExifTags.TAGS[i] + " - " + j.decode("utf-8")
            except:
                data = ExifTags.TAGS[i] + " - " + str(j)
            file.write(data + "\n")
    file.close()


analysis("files/picture.jpg")
