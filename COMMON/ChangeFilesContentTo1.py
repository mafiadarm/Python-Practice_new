import hashlib
import os
import random
from multiprocessing.dummy import Pool
from tqdm import tqdm


def changeTo1(file):
    mm = hashlib.md5(file.encode()).hexdigest()
    with open(file, "a") as cc:
        cc.seek(random.randint(1000, 10000))
        cc.write(mm)

    # os.remove(file)  # delete files


if __name__ == '__main__':
    folder = input("The folder path: ")
    p = Pool()

    for folder, _, files in os.walk(folder):
        for file in tqdm(files):
            path = os.path.join(folder, file)
            p.apply_async(changeTo1, args=(path,))

    p.close()
    p.join()