#!/bin/bash

CONFIG=${CONFIG:-config.env}
. $CONFIG


PDIR="./build/$PDIR"

echo "PDIR=$PDIR"


INC="-I. -Ilib -Ibuild -I${PDIR}/include -I/usr/include/eigen3"

#-lpandafx
PANDA="-lp3framework -lpanda -lpandaexpress -lp3dtoolconfig -lp3dtool -lp3interrogatedb"

LIBS="-Lbuild -L${ROOT}/lib ${PANDA} -lpthread -ldl -lm -lc"

# ubuntu gcc7 workaround -fuse-ld=gold to get sanitize=bool
# see https://stackoverflow.com/questions/50024731/ld-unrecognized-option-push-state-no-as-needed


if false
then
    COPT="-fmax-errors=1 -fuse-ld=gold -fextended-identifiers -fsanitize=bool -O3 ${INC} -fPIC -Wno-ignored-attributes"
    cxx="g++ ${COPT} -std=gnu++11"
    link="$cxx -shared"
    cc="gcc $COPT"
else
#    COPT="-fextended-identifiers -fsanitize=bool -O2 ${INC} -fPIC -Wno-ignored-attributes"
# -fsanitize=bool not supported on clang10 pclinuxos
    COPT="-fextended-identifiers -O0 -g3 ${INC} -fPIC -Wno-ignored-attributes"
    cxx="clang++ ${COPT} -fno-vectorize -fno-slp-vectorize -std=gnu++11"
    link="$cxx -shared"
    cc="clang ${COPT}"
fi

# -fpermissive
LIB=upanda3d

if echo "$@"|grep -q fast
then
    echo "skipping c++ build+test"
    rm build/lib${LIB}_c.so
else
    rm build/lib${LIB}_*.so mview_cpp mview_c

    echo "building c++ interface"
    $link -o build/lib${LIB}_cpp.so lib/lib.cxx ${LIBS}

    echo "building c++ test"
    $cxx  -fPIE $COPT -o mview_cpp -L./build -l${LIB}_cpp ${LIBS}
    if [ -f mview_cpp ]
    then
        if echo "$@" | grep -q dev
        then
            echo "skipping c++ test program"
        else
            ./mview_cpp &
        fi
    else
        echo "can't run c++ test program"
    fi
fi




if echo "$@" |grep -q cpponly
then
    echo skipping C test
else

    stty sane
    echo
    echo "================================================"
    echo

    mkdir -p build

    if [ -f build/lib${LIB}_cpp.so ]
    then
        echo "building CNI interface"
        if $link -o build/lib${LIB}_cni.so build/interrogate_cni.cpp ${LIBS} -l${LIB}_cpp
        then
            echo "C native ffi interface for C++ built"
        fi


        echo "building C indexed interface"
        if $link -o build/lib${LIB}_c.so build/interrogate_wrapper.cpp ${LIBS} -l${LIB}_cpp
        then
            /bin/mv -vf build/interrogate_wrapper.h build/${LIB}.h
            /bin/mv -vf build/interrogate_wrapper.json build/${LIB}.json
            cmd="$cc -o mview_c mview.c ${LIBS} -l${LIB}_cpp -l${LIB}_cni"
            echo $cmd
            $cmd
            ./mview_c

            cmd="$cc -DINDEX=1 -o mview_c_idx mview.c ${LIBS} -l${LIB}_cpp -l${LIB}_c"
            echo $cmd
            $cmd
            ./mview_c_idx
        else
            echo "build C lib failed"
        fi
    fi
fi
