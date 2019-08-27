INC="-I. -Ilib -I/usr/local/include/panda3d/include -I/usr/include/eigen3"

LIBS="-L/usr/local/lib/x86_64-linux-gnu/panda3d -lp3framework -lpanda -lpandafx -lpandaexpress -lp3dtoolconfig -lp3dtool -lp3interrogatedb -lpthread -ldl -lm -lc"
INT="-S/usr/include/panda3d/parser-inc -S/usr/include/"

# ubuntu gcc7 workaround -fuse-ld=gold see https://stackoverflow.com/questions/50024731/ld-unrecognized-option-push-state-no-as-needed

COPT="-fuse-ld=gold -fsanitize=bool -std=gnu++11 -O3 ${INC} -fPIC -Wno-ignored-attributes -fpermissive"

glib="g++ ${COPT} -shared"


if echo "$@"|grep -q fast
then
    echo "skipping c++ build+test"
else
    rm libupanda3d_cpp.so libupanda3d_c.so mview_cpp mview_c

    $glib -o libupanda3d_cpp.so  mview.cxx ${LIBS}

    g++  -fPIE $COPT -o mview_cpp -L. -lupanda3d_cpp ${LIBS}
    if [ -f mview_cpp ]
    then
        if echo "$@" | grep -q dev
        then
            echo "skipping c++ test program"
        else
            LD_LIBRARY_PATH=. ./mview_cpp &
        fi
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

