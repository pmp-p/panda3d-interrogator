# panda3d-interrogator
ffi experiment with interrogate C bindings

requires cpython 3.7+  ( 3.6 NOT TESTED )

requires Panda3D , not that "pip"version won't work as you need C++ part of sdk

requires https://github.com/pmp-p/fstrings_helper


```
# run interrogate to get the lib/interrogate_wrapper.cpp from lib/lib.*
./test_i.sh

# link the c++ libupanda_cpp.so then build its C only interface libupanda_c.so
# there a test for both
./shared.sh


#test micropython build ( need uctypes and ffi modules enabled on unix port )
./test_upy.sh

# enjoy micropython bindinds in tests/testpy.py
# and write your own game in place of the test
# ( kidding there is not whole Panda3D API in there ! -yet- )
```

Thanks thetestgame for teasing with C bindings.
Thanks rdb and C​FSworks for help on implementation.


