# panda3d-interrogator
ffi experiment with interrogate C bindings

first target :

    MicroPython  https://github.com/micropython/micropython



requires cpython 3.7+  ( 3.6 NOT TESTED )

requires Panda3D , not the "pip" version, as it won't work because you need C++ part of sdk

see :

 https://www.panda3d.org/download/sdk-1-10-4-1/ [other downloads]

 but better build from source locally  <= preferred : match current test conditions

 full sdk installed to /usr/local should be ok too if you create a config.env


requires https://github.com/pmp-p/fstrings_helper for MicroPython f-strings support
or old cpython targets


```
# run interrogator.sh to get the lib/interrogate_wrapper.cpp from lib/lib.*
# .cxx and .h of your lib must be already in ./lib/
# forced exports of extern classes is made by adding them to lib.N

CONFIG=linux-x64.env ./interrogator.sh

# a lib for linking a Panda3D C interface is used for demo
# link the c++ libupanda_cpp.so then build its C only interface libupanda_c.so
# there a test for both give it a model.bam to display

./build_c_interface.sh


#test micropython build ( need uctypes and ffi modules enabled on unix port )
./test_upy.sh

# enjoy micropython bindings in build/upanda3d.py
# and write your own game in place of the test
# ( kidding there is not whole Panda3D API in there ! -yet- )
```

Thanks thetestgame for teasing with C bindings.

Thanks rdb and C​FSworks for help on implementation.

Thanks to pfalcon for micropython-ffigen inspiration.
