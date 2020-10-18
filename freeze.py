from flask_frozen import Freezer
from run import app
import os

freezer = Freezer(app)

if __name__ == '__main__':
    os.system("rm -rf build docs")

    freezer.freeze()

    os.system("mv build docs")
