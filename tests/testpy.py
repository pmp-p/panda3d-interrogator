# upy
import os
import sys
import ffi
import uctypes
import gc
import time

GCBAD = 0
REFC = {}

class cplusplus:
    def variadic_call(self,ffi_name,*argv,**kw):
        func = getattr(self, ffi_name, {})
        try:
            if func:
                func = func.get(len(argv), None)

            if func:
                return func(self.iptr, *argv)
        except Exception as e:
            print(e,ffi_name,len(argv),func,'argv=',argv)
            raise
        raise TypeError("%s : wrong count of positional arguments" % ffi_name)

    # c++ ctor/dtor

    def __init__(self, *argv, **kw):
        global GCBAD, REFC
        iref = kw.get('iptr',None)
        if iref:
            iref = iref.iptr
            self.iptr = iref
            REFC.setdefault(iref,1)
            REFC[iref]+=1
        else:
            GCBAD += 1
            self.iptr = self.ctor[len(argv)](*argv, **kw)

    def refcount(self):
        global REFC
        return REFC.get( id(self.iptr) , 1 )

    def __del__(self):
        global GCBAD
        nref= REFC.get( self.iptr , 1)
        if nref > 1:
            REFC[self.iptr] -= 1
            print("still",nref-1,"ref. on",self.iptr)
            del self.iptr, self.dtor
            return
        print("__del__",self.iptr)
        GCBAD -= 1
        try:
            self.dtor(self.iptr)
        finally:
            self.iptr = None

    def __enter__(self,*argv,**kw):
        return self

    #self.__del__() is not called ...
    def __exit__(self,*argv,**kw):
        global REFC

        for attr in dir(self):
            try:
                if (not attr in ['dtor','iptr','__del__']):
                    delattr(E,attr)
            except:
                pass

        self.__del__()


class NodePath(cplusplus):

    lib = ffi.open("""libupanda3d_c.so""")

    NodePath_C_look_at_v_pppp = lib.func('v','NodePath_C_look_at_v_pppp','pppp')
    NodePath_C_set_scale_v_pppp = lib.func('v','NodePath_C_set_scale_v_pppp','pppp')
    NodePath_C_set_pos_v_pppp = lib.func('v','NodePath_C_set_pos_v_pppp','pppp')
    NodePath_C_reparent_to_v_pp = lib.func('v','NodePath_C_reparent_to_v_pp','pp')

# variadic

    ctor = {
        1 : lib.func('p','NodePath_C_ctor_p_p','p'),
        0 : lib.func('p','NodePath_C_ctor_p_v',''),
    }


    # c++ instance methods



    def look_at(self,*argv,**kw):
        return self.NodePath_C_look_at_v_pppp(self.iptr, *argv, **kw)

    def set_scale(self,*argv,**kw):
        return self.NodePath_C_set_scale_v_pppp(self.iptr, *argv, **kw)

    def set_pos(self,*argv,**kw):
        return self.NodePath_C_set_pos_v_pppp(self.iptr, *argv, **kw)

    def reparent_to(self,*argv,**kw):
        return self.NodePath_C_reparent_to_v_pp(self.iptr, *argv, **kw)

class Engine(cplusplus):

    lib = ffi.open("""libupanda3d_c.so""")

    Engine_C_get_framework_p_p = lib.func('p','Engine_C_get_framework_p_p','p')
    Engine_C_casetest_i_pppp = lib.func('i','Engine_C_casetest_i_pppp','pppp')
    Engine_C_HelloEngine_i_p = lib.func('i','Engine_C_HelloEngine_i_p','p')
    Engine_C_load_model_p_ps = lib.func('p','Engine_C_load_model_p_ps','ps')
    Engine_C_attach_v_pp = lib.func('v','Engine_C_attach_v_pp','pp')
    Engine_C_set_framework_v_pp = lib.func('v','Engine_C_set_framework_v_pp','pp')
    Engine_C_dtor_v_p = lib.func('v','Engine_C_dtor_v_p','p')
    Engine_C_get_version_string_s_v = lib.func('s','Engine_C_get_version_string_s_v','v')
    Engine_C_step_v_p = lib.func('v','Engine_C_step_v_p','p')
    Engine_C_is_alive_i_v = lib.func('i','Engine_C_is_alive_i_v','v')
    Engine_C_build_v_p = lib.func('v','Engine_C_build_v_p','p')
    Engine_C_get_wframe_p_p = lib.func('p','Engine_C_get_wframe_p_p','p')

# variadic

    ctor = {
        1 : lib.func('p','Engine_C_ctor_p_p','p'),
        0 : lib.func('p','Engine_C_ctor_p_v',''),
    }


    # c++ instance methods



    def get_framework(self,*argv,**kw):
        return self.Engine_C_get_framework_p_p(self.iptr, *argv, **kw)

    def casetest(self,*argv,**kw):
        return self.Engine_C_casetest_i_pppp(self.iptr, *argv, **kw)

    def HelloEngine(self,*argv,**kw):
        return self.Engine_C_HelloEngine_i_p(self.iptr, *argv, **kw)

    def load_model(self,*argv,**kw):
        return self.Engine_C_load_model_p_ps(self.iptr, *argv, **kw)

    def attach(self,*argv,**kw):
        return self.Engine_C_attach_v_pp(self.iptr, *argv, **kw)

    def set_framework(self,*argv,**kw):
        return self.Engine_C_set_framework_v_pp(self.iptr, *argv, **kw)

    def dtor(self,*argv,**kw):
        return self.Engine_C_dtor_v_p(self.iptr, *argv, **kw)

    @classmethod
    def get_version_string(cls,*argv,**kw):
        return cls.Engine_C_get_version_string_s_v(*argv, **kw)

    def step(self,*argv,**kw):
        return self.Engine_C_step_v_p(self.iptr, *argv, **kw)

    @classmethod
    def is_alive(cls,*argv,**kw):
        return cls.Engine_C_is_alive_i_v(*argv, **kw)

    def build(self,*argv,**kw):
        return self.Engine_C_build_v_p(self.iptr, *argv, **kw)

    def get_wframe(self,*argv,**kw):
        return self.Engine_C_get_wframe_p_p(self.iptr, *argv, **kw)


def test1():
    print("C++ class constructor",Engine.ctor)
    with Engine() as E:
        print('engine',E)

        # a dumb test that should say 42
        print('hello',E.HelloEngine())

        print('version','=', E.get_version_string())

        E.build()

        np = E.load_model( "model.bam" )

        print("np","=",np)

        E.attach(np)


        while E.is_alive():
            E.step()

        print("C++ engine requested exit")
    #E.__del__() # <== should not have to be called manually, cpython would do it itself.

def test2():
    print("C++ class constructor",Engine.ctor)
    with Engine() as E:
        print('engine      ',E, E.iptr)
        C = E.__class__( iptr=E )
        print('engine(copy)',C, C.iptr)

        # a dumb test that should say 42
        print('hello',E.HelloEngine())

        print('version','=', E.get_version_string())

        E.build()

        np = E.load_model( "model.bam" )

        print("np","=",np)

        E.attach(np)


        while E.is_alive():
            E.step()

        print("C++ engine requested exit")

    print("deleting copy")
    del C #C.__del__() # <== should not have to be called manually, cpython would do it itself.


if 0:
    print("--- test1 with forced del ----")
    test1()
    del test1
    gc.collect()

if 1:
    print("--- test2 with refcounting ----")
    test2()
    del test2
    gc.collect()
    gc.collect()

print(REFC)
if GCBAD:print("Bad GC")

