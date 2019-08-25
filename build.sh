INC="-I/usr/local/include/panda3d -I/usr/include/eigen3"

LIBS="-L/usr/local/lib/x86_64-linux-gnu/panda3d -lp3framework -lpanda -lpandafx -lpandaexpress -lp3dtoolconfig -lp3dtool -lp3pystub"
INT="-S/usr/include/panda3d/parser-inc -S/usr/include/"

#g++ -c -std=gnu++11 -O2 ${INC} -fPIC  -o pview.o pview.cxx -Wno-ignored-attributes -fpermissive
#g++ pview.o -o ptest  ${LIBS} -lpthread
IOPTS="-DCPPPARSER -D__STDC__=1 -D__cplusplus=201103L -fnames -string -refcount -assert"
interrogate -c ${INC} ${INT} ${IOPTS} -oc test.c -library p3framework pview.cxx
#/usr/local/include/panda3d/include/pandaFramework.h
interrogate  ${INC} ${INT} ${IOPTS} -DEXPCL_DTOOLCONFIG= -nodb -c -promiscuous -module panda3d.interrogatedb -library interrogatedb -string -true-names -oc test.c pview.cxx
