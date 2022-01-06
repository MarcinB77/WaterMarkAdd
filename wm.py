from PIL import Image, ImageDraw, ImageFont

# get an image


class WM:
    def __init__(self, file_path, text, positions, font, fnt_size, opacity):
        with Image.open(file_path).convert("RGBA") as base:
            # get image size
            self.size = base.size
            # make a blank image for the text, initialized to transparent text color
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

            # get a font
            fnt = ImageFont.truetype(font, fnt_size)
            # get a drawing context
            d = ImageDraw.Draw(txt)

            # draw text for each position, half opacity
            positions = self.get_positions(positions)
            for position in positions:
                d.text(position, text, font=fnt, fill=(255, 255, 255, opacity))

            # add '_wm' to file name
            new_name = str(file_path).split(".")[0] + "_wm." + str(file_path).split(".")[1]
            # create new image
            self.out = Image.alpha_composite(base, txt).convert('RGB')
            # save
            self.out.save(new_name)

    def get_positions(self, positions):
        size = self.size
        pos_dict = {"lt": (10, 20),
                    "lb": (10, size[1]-250),
                    "rt": (size[0] - 700, 20),
                    "rb": (size[0] - 700, size[1] - 250),
                    "ct": (size[0] / 2 - 170, size[1] / 2 - 170)
                    }
        pos_list = []
        for pos in positions:
            if pos in pos_dict:
                pos_list.append(pos_dict[pos])
        return pos_list
