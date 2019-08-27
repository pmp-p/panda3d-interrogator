# upy
import os
import sys
import ffi
import uctypes

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


class Engine:

    lib = ffi.open("""libupanda3d_c.so""")

    Engine_C_attach_v_pp = lib.func('v','Engine_C_attach_v_pp','pp')
    Engine_C_casetest_i_pppp = lib.func('i','Engine_C_casetest_i_pppp','pppp')
    Engine_C_get_framework_p_p = lib.func('p','Engine_C_get_framework_p_p','p')
    Engine_C_is_alive_i_v = lib.func('i','Engine_C_is_alive_i_v','v')
    Engine_C_load_model_p_ps = lib.func('p','Engine_C_load_model_p_ps','ps')
    Engine_C_set_framework_v_pp = lib.func('v','Engine_C_set_framework_v_pp','pp')
    Engine_C_step_v_p = lib.func('v','Engine_C_step_v_p','p')
    Engine_C_get_version_string_s_v = lib.func('s','Engine_C_get_version_string_s_v','v')
    Engine_C_HelloEngine_i_p = lib.func('i','Engine_C_HelloEngine_i_p','p')
    Engine_C_get_wframe_p_p = lib.func('p','Engine_C_get_wframe_p_p','p')
    Engine_C_build_v_p = lib.func('v','Engine_C_build_v_p','p')

# variadic

    ctor = {
        1 : lib.func('p','Engine_C_ctor_p_p','p'),
        0 : lib.func('p','Engine_C_ctor_p_v',''),
    }
# c++ ctor

    def __init__(self, *argv, **kw):
        self.iptr = self.ctor[len(argv)](*argv, **kw)

# c++ instance methods

    def attach(self,*argv,**kw):
        return self.Engine_C_attach_v_pp(self.iptr, *argv, **kw)

    def casetest(self,*argv,**kw):
        return self.Engine_C_casetest_i_pppp(self.iptr, *argv, **kw)

    def get_framework(self,*argv,**kw):
        return self.Engine_C_get_framework_p_p(self.iptr, *argv, **kw)

    @classmethod
    def is_alive(cls,*argv,**kw):
        return cls.Engine_C_is_alive_i_v(*argv, **kw)

    def load_model(self,*argv,**kw):
        return self.Engine_C_load_model_p_ps(self.iptr, *argv, **kw)

    def set_framework(self,*argv,**kw):
        return self.Engine_C_set_framework_v_pp(self.iptr, *argv, **kw)

    def step(self,*argv,**kw):
        return self.Engine_C_step_v_p(self.iptr, *argv, **kw)

    @classmethod
    def get_version_string(cls,*argv,**kw):
        return cls.Engine_C_get_version_string_s_v(*argv, **kw)

    def HelloEngine(self,*argv,**kw):
        return self.Engine_C_HelloEngine_i_p(self.iptr, *argv, **kw)

    def get_wframe(self,*argv,**kw):
        return self.Engine_C_get_wframe_p_p(self.iptr, *argv, **kw)

    def build(self,*argv,**kw):
        return self.Engine_C_build_v_p(self.iptr, *argv, **kw)


def std_string(addr):
    max_str = 255
    mem = uctypes.struct(addr, { "cstr": (uctypes.ARRAY | 0, uctypes.UINT8 | max_str),})
    for sz in range(0,max_str):
        if not mem.cstr[sz]:
            break
    mem = uctypes.struct(addr, { "cstr": (uctypes.ARRAY | 0, uctypes.UINT8 | sz),})
    return bytes(mem.cstr).decode('utf-8')

print(Engine.ctor)
E = Engine()
print('engine',E)
print('hello',E.HelloEngine())

print('versionP','=', E.get_version_string())

#print('versionS','=', std_string( E.get_version_string() ) )



E.build()

#ba = bytearray(b"boris.bam")
#print( memoryview(ba)[0:len(ba)] )

np = E.load_model( "boris.bam" )

print("np","=",np)

E.attach(np)



while E.is_alive():
    E.step()



