from word_color.ImageLoader import ImageLoader as IL
import word_color.get_image_color as get_ic
import shutil


def get_word_color(what_to: str) -> tuple[int, int, int]:
    loader = IL(what_to)
    loader.download()

    count, red, green, blue = len(loader.files), 0, 0, 0
    for item in loader.files:
        color = get_ic.get_color(item)
        red += color[0]
        green += color[1]
        blue += color[2]

    shutil.rmtree('Downloads')

    return red // count, green // count, blue // count
