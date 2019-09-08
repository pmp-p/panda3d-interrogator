reset;
rm build/upanda3d.py

CONFIG=${CONFIG:-config.env}
. $CONFIG

for py in 8 7 6
do
    if which python3.${py}
    then
        export PYTHON=python3.${py}
        break
    fi
done
echo Will use python $PYTHON
echo

if [ -d fstrings_helper ]
then
    echo found fstrings_helper
else
    git clone https://github.com/pmp-p/fstrings_helper.git
fi

echo LD_LIBRARY_PATH=$LD_LIBRARY_PATH

if black -S -l 132 cxxbuilder_cpy.py
then

    if $PYTHON -m fstrings_helper cxxbuilder_cpy.py > cxxbuilder_upy.py
    then
        micropython -X heapsize=16384K cxxbuilder_upy.py
        LOG=nolog micropython -X heapsize=2048K build/upanda3d.py
    fi
fi
