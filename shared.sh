INC="-I. -Ilib -I/usr/local/include/panda3d/include -I/usr/include/eigen3"

LIBS="-L/usr/local/lib/x86_64-linux-gnu/panda3d -lp3framework -lpanda -lpandafx -lpandaexpress -lp3dtoolconfig -lp3dtool -lp3interrogatedb -lpthread"
INT="-S/usr/include/panda3d/parser-inc -S/usr/include/"


glib="g++ -shared -std=gnu++11 -O3 ${INC} -fPIC -shared -Wno-ignored-attributes -fpermissive"


if echo "$@"|grep -q fast
then
    echo "skipping c++ build+test"
else
    rm libupanda3d_cpp.so libupanda3d_c.so mview_cpp mview_c

    $glib -o libupanda3d_cpp.so  mview.cxx ${LIBS}

    g++ -o mview_cpp -L. -lupanda3d_cpp ${LIBS}
    if [ -f mview_cpp ]
    then
        LD_LIBRARY_PATH=. ./mview_cpp &
    else
        echo "can't run c++ test program"
    fi
fi
stty sane
echo
echo "================================================"
echo

if [ -f libupanda3d_cpp.so ]
then
    reset
    if $glib -fmax-errors=1 -Ilib -o libupanda3d_c.so lib/interrogate_wrapper.cpp ${LIBS} -L . -lupanda3d_cpp
    then
        cmd="gcc -fmax-errors=1 -I. -Ilib -o mview_c mview.c ${LIBS} -L. -lupanda3d_cpp -lupanda3d_c"
        echo $cmd
        $cmd
        LD_LIBRARY_PATH=/data/cross/panda3d ./mview_c
    else
        echo "build C lib failed"
    fi
fi
