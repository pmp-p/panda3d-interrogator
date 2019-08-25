reset;
black -S -l 132 cpanda3d.py

python3.8 -m fstrings_helper cpanda3d.py > upanda3d.py &&  upy upanda3d.py
