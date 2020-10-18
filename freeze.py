from flask_frozen import Freezer
from run import app
from os import rename

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    rename("build/", "docs/")
