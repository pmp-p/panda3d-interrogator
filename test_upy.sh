reset;
black -S -l 132 cpanda3d.py

python3.8 -m fstrings_helper cpanda3d.py > upanda3d.py && LD_LIBRARY_PATH=/data/cross/panda3d upy upanda3d.py
