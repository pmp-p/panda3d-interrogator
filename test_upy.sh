reset;
clear >> /tmp/log
rm tests/testpy.py

if black -S -l 132 cpanda3d.py
then

    if python3.8 -m fstrings_helper cpanda3d.py > upanda3d.py
    then
        LD_LIBRARY_PATH=$(pwd) micropython upanda3d.py
        LD_LIBRARY_PATH=$(pwd) micropython tests/testpy.py
    fi
fi
