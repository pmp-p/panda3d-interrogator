reset;
clear >> /tmp/log
rm build/upanda3d.py

if black -S -l 132 cxxbuilder_cpy.py
then

    if python3.8 -m fstrings_helper cxxbuilder_cpy.py > cxxbuilder_upy.py
    then
        LD_LIBRARY_PATH=$(pwd)/build micropython cxxbuilder_upy.py
        LD_LIBRARY_PATH=$(pwd)/build micropython  -X heapsize=256K build/upanda3d.py
    fi
fi
