speeds = "../data/train.txt"


def line_reader(file_name):
    for row in open(file_name, "r"):
        yield row


line = line_reader(speeds)

speed = next(line)

while speed:
    print(speed)
