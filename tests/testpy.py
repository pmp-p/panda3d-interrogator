# upy
import os
import sys
import ffi
import uctypes

def variadic_call(self,ffi_name,*argv,**kw):
    func = cls.get(ffi_name,{})

    if func:
        func = func.get( len(argv) , None)

    if func:
        return func(self.iptr, *argv)

    raise TypeError("%s : wrong count of positional arguments" % ffi_name)


class Engine:

    lib = ffi.open("""libupanda3d_c.so""")

    Engine_C_get_wframe_p_p = lib.func('p','Engine_C_get_wframe_p_p','p')
    Engine_C_build_v_p = lib.func('v','Engine_C_build_v_p','p')
    Engine_C_get_version_string_p_v = lib.func('p','Engine_C_get_version_string_p_v','v')
    Engine_C_load_model_p_p = lib.func('p','Engine_C_load_model_p_p','p')
    Engine_C_attach_v_p = lib.func('v','Engine_C_attach_v_p','p')
    Engine_C_HelloEngine_i_p = lib.func('i','Engine_C_HelloEngine_i_p','p')
    Engine_C_set_framework_v_p = lib.func('v','Engine_C_set_framework_v_p','p')
    Engine_C_get_framework_p_p = lib.func('p','Engine_C_get_framework_p_p','p')
    Engine_C_step_v_p = lib.func('v','Engine_C_step_v_p','p')

# variadic

    ctor = {
        1 : lib.func('p','Engine_C_ctor_p_p','p'),
        0 : lib.func('p','Engine_C_ctor_p_v',''),
    }
# c++ ctor

    def __init__(self, *argv, **kw):
        self.iptr = variadic_call(self, 'ctor', *argv, **kw)

# c++ instance methods

    def get_wframe(self,*argv,**kw):
        return self.Engine_C_get_wframe_p_p(self.iptr, *argv, **kw)

    def build(self,*argv,**kw):
        return self.Engine_C_build_v_p(self.iptr, *argv, **kw)

    @classmethod
    def get_version_string(cls,*argv,**kw):
        return cls.Engine_C_get_version_string_p_v(*argv, **kw)

    def load_model(self,*argv,**kw):
        return self.Engine_C_load_model_p_p(self.iptr, *argv, **kw)

    def attach(self,*argv,**kw):
        return self.Engine_C_attach_v_p(self.iptr, *argv, **kw)

    def HelloEngine(self,*argv,**kw):
        return self.Engine_C_HelloEngine_i_p(self.iptr, *argv, **kw)

    def ctor(*argv,**kw):
        return variadic_call(self, Engine_C_HelloEngine_i_p, *argv, **kw)

    def set_framework(self,*argv,**kw):
        return self.Engine_C_set_framework_v_p(self.iptr, *argv, **kw)

    def get_framework(self,*argv,**kw):
        return self.Engine_C_get_framework_p_p(self.iptr, *argv, **kw)

    def step(self,*argv,**kw):
        return self.Engine_C_step_v_p(self.iptr, *argv, **kw)

