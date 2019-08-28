INC="-I. -Ilib -I/usr/local/include/panda3d/include -I/usr/include/eigen3"

LIBS="-L/usr/local/lib/x86_64-linux-gnu/panda3d -lp3framework -lpanda -lpandafx -lpandaexpress -lp3dtoolconfig -lp3dtool -lp3interrogatedb -lpthread -ldl -lm -lc"
INT="-S/usr/include/panda3d/parser-inc -S/usr/include/"

# ubuntu gcc7 workaround -fuse-ld=gold see https://stackoverflow.com/questions/50024731/ld-unrecognized-option-push-state-no-as-needed

COPT="-fuse-ld=gold -fsanitize=bool -std=gnu++11 -O3 ${INC} -fPIC -Wno-ignored-attributes -fpermissive"

glib="g++ ${COPT} -shared"



LIB=upanda3d

if echo "$@"|grep -q fast
then
    echo "skipping c++ build+test"
else
    rm lib${LIB}_cpp.so lib${LIB}_c.so mview_cpp mview_c

    $glib -o build/lib${LIB}_cpp.so  mview.cxx ${LIBS}

    g++  -fPIE $COPT -o mview_cpp -L./build -l${LIB}_cpp ${LIBS}
    if [ -f mview_cpp ]
    then
        if echo "$@" | grep -q dev
        then
            echo "skipping c++ test program"
        else
            LD_LIBRARY_PATH=./build ./mview_cpp &
        fi
    else
        echo "can't run c++ test program"
    fi
fi

stty sane
echo
echo "================================================"
echo


mkdir -p build

if [ -f build/lib${LIB}_cpp.so ]
then
    if $glib -fmax-errors=1 -Ilib -o build/lib${LIB}_c.so lib/interrogate_wrapper.cpp ${LIBS} -L./build -l${LIB}_cpp
    then
        cp -f lib/interrogate_wrapper.h build/${LIB}.h
        cmd="gcc -fmax-errors=1 -I. -Ilib -o mview_c mview.c ${LIBS} -L./build -lupanda3d_cpp -lupanda3d_c"
        echo $cmd
        $cmd
        LD_LIBRARY_PATH=/data/cross/panda3d/build ./mview_c
    else
        echo "build C lib failed"
    fi
fi

