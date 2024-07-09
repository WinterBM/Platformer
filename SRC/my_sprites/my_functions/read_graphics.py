from my_sprites.my_sprites import Platform

# Read graphics
def level_reader(path:str, all_sprites, object_sprites):
    """
    Reads level txt file and adds to aproriate sprite groups

    :param path str: path to level txt file
    :param all_sprites : sprite group for all sprites
    :param object_sprites : sprite group for platform sprites
    """
    with open(path, "r") as f:
        lines = f.readlines()
        for y, line in enumerate(lines):
            for x, pos in enumerate(line):
                if pos =="x":
                    PT = Platform((x*50,y*50))
                    all_sprites.add(PT)
                    object_sprites.add(PT)
