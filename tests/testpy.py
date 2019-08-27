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
    def variadic_call(self, ffi_name, *argv, **kw):
        func = getattr(self, ffi_name, {})
        try:
            if func:
                func = func.get(len(argv), None)

            if func:
                return func(self.iptr, *argv)
        except Exception as e:
            print(e, ffi_name, len(argv), func, 'argv=',argv)
            raise
        raise TypeError("%s : wrong count of positional arguments" % ffi_name)

    # c++ ctor/dtor

    def __init__(self, *argv, **kw):
        global GCBAD, REFC
        iref = kw.pop('iptr',None)
        if iref:
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

    NodePath_C_look_at_v_pfff = lib.func('v','NodePath_C_look_at_v_pfff','pfff')
    NodePath_C_set_scale_v_pp = lib.func('v','NodePath_C_set_scale_v_pp','pp')
    NodePath_C_set_pos_v_pp = lib.func('v','NodePath_C_set_pos_v_pp','pp')
    NodePath_C_reparent_to_v_pp = lib.func('v','NodePath_C_reparent_to_v_pp','pp')

    # variadic

    ctor = {
        1 : lib.func('p','NodePath_C_ctor_p_p','p'),
        0 : lib.func('p','NodePath_C_ctor_p_v',''),
    }


    # c++ instance methods



    def look_at(self, *argv, **kw):
        return self.NodePath_C_look_at_v_pfff(self.iptr, *argv, **kw)

    def set_scale(self, *argv, **kw):
        return self.NodePath_C_set_scale_v_pp(self.iptr, *argv, **kw)

    def set_pos(self, *argv, **kw):
        return self.NodePath_C_set_pos_v_pp(self.iptr, *argv, **kw)

    def reparent_to(self, *argv, **kw):
        return self.NodePath_C_reparent_to_v_pp(self.iptr, *argv, **kw)

class LVecBase3f(cplusplus):

    lib = ffi.open("""libupanda3d_c.so""")

    LVecBase3f_C_get_standardized_hpr_p_p = lib.func('p','LVecBase3f_C_get_standardized_hpr_p_p','p')
    LVecBase3f_C_add_to_cell_v_pif = lib.func('v','LVecBase3f_C_add_to_cell_v_pif','pif')
    LVecBase3f_C_get_class_type_i_v = lib.func('i','LVecBase3f_C_get_class_type_i_v','v')
    LVecBase3f_C_fill_v_pf = lib.func('v','LVecBase3f_C_fill_v_pf','pf')
    LVecBase3f_C_normalized_p_p = lib.func('p','LVecBase3f_C_normalized_p_p','p')
    LVecBase3f_C_normalize_B_p = lib.func('B','LVecBase3f_C_normalize_B_p','p')
    LVecBase3f_C_read_datagram_v_pp = lib.func('v','LVecBase3f_C_read_datagram_v_pp','pp')
    LVecBase3f_C_fmin_p_pp = lib.func('p','LVecBase3f_C_fmin_p_pp','pp')
    LVecBase3f_C_get_y_f_p = lib.func('f','LVecBase3f_C_get_y_f_p','p')
    LVecBase3f_C_get_z_f_p = lib.func('f','LVecBase3f_C_get_z_f_p','p')
    LVecBase3f_C_length_squared_f_p = lib.func('f','LVecBase3f_C_length_squared_f_p','p')
    LVecBase3f_C_get_cell_f_pi = lib.func('f','LVecBase3f_C_get_cell_f_pi','pi')
    LVecBase3f_C_output_v_pp = lib.func('v','LVecBase3f_C_output_v_pp','pp')
    LVecBase3f_C_get_v_p_p = lib.func('p','LVecBase3f_C_get_v_p_p','p')
    LVecBase3f_C_get_yz_p_p = lib.func('p','LVecBase3f_C_get_yz_p_p','p')
    LVecBase3f_C_ctor_1_p_p = lib.func('p','LVecBase3f_C_ctor_1_p_p','p')
    LVecBase3f_C_length_f_p = lib.func('f','LVecBase3f_C_length_f_p','p')
    LVecBase3f_C_end_1_v_p = lib.func('v','LVecBase3f_C_end_1_v_p','p')
    LVecBase3f_C_get_num_components_i_v = lib.func('i','LVecBase3f_C_get_num_components_i_v','v')
    LVecBase3f_C_end_v_p = lib.func('v','LVecBase3f_C_end_v_p','p')
    LVecBase3f_C_read_datagram_fixed_v_pp = lib.func('v','LVecBase3f_C_read_datagram_fixed_v_pp','pp')
    LVecBase3f_C_set_v_pfff = lib.func('v','LVecBase3f_C_set_v_pfff','pfff')
    LVecBase3f_C_get_data_v_p = lib.func('v','LVecBase3f_C_get_data_v_p','p')
    LVecBase3f_C_get_x_f_p = lib.func('f','LVecBase3f_C_get_x_f_p','p')
    LVecBase3f_C_set_y_v_pf = lib.func('v','LVecBase3f_C_set_y_v_pf','pf')
    LVecBase3f_C_set_z_v_pf = lib.func('v','LVecBase3f_C_set_z_v_pf','pf')
    LVecBase3f_C_unit_x_p_v = lib.func('p','LVecBase3f_C_unit_x_p_v','v')
    LVecBase3f_C_size_i_v = lib.func('i','LVecBase3f_C_size_i_v','v')
    LVecBase3f_C_dot_f_pp = lib.func('f','LVecBase3f_C_dot_f_pp','pp')
    LVecBase3f_C_get_xy_p_p = lib.func('p','LVecBase3f_C_get_xy_p_p','p')
    LVecBase3f_C_get_xz_p_p = lib.func('p','LVecBase3f_C_get_xz_p_p','p')
    LVecBase3f_C_unit_y_p_v = lib.func('p','LVecBase3f_C_unit_y_p_v','v')
    LVecBase3f_C_unit_z_p_v = lib.func('p','LVecBase3f_C_unit_z_p_v','v')
    LVecBase3f_C_write_datagram_fixed_v_pp = lib.func('v','LVecBase3f_C_write_datagram_fixed_v_pp','pp')
    LVecBase3f_C_project_p_pp = lib.func('p','LVecBase3f_C_project_p_pp','pp')
    LVecBase3f_C_begin_v_p = lib.func('v','LVecBase3f_C_begin_v_p','p')
    LVecBase3f_C_write_datagram_v_pp = lib.func('v','LVecBase3f_C_write_datagram_v_pp','pp')
    LVecBase3f_C_fmax_p_pp = lib.func('p','LVecBase3f_C_fmax_p_pp','pp')
    LVecBase3f_C_add_z_v_pf = lib.func('v','LVecBase3f_C_add_z_v_pf','pf')
    LVecBase3f_C_add_y_v_pf = lib.func('v','LVecBase3f_C_add_y_v_pf','pf')
    LVecBase3f_C_is_nan_B_p = lib.func('B','LVecBase3f_C_is_nan_B_p','p')
    LVecBase3f_C_add_x_v_pf = lib.func('v','LVecBase3f_C_add_x_v_pf','pf')
    LVecBase3f_C_set_cell_v_pif = lib.func('v','LVecBase3f_C_set_cell_v_pif','pif')
    LVecBase3f_C_begin_1_v_p = lib.func('v','LVecBase3f_C_begin_1_v_p','p')
    LVecBase3f_C_cross_p_pp = lib.func('p','LVecBase3f_C_cross_p_pp','pp')
    LVecBase3f_C_zero_p_v = lib.func('p','LVecBase3f_C_zero_p_v','v')
    LVecBase3f_C_componentwise_mult_v_pp = lib.func('v','LVecBase3f_C_componentwise_mult_v_pp','pp')
    LVecBase3f_C_init_type_v_v = lib.func('v','LVecBase3f_C_init_type_v_v','v')
    LVecBase3f_C_cross_into_v_pp = lib.func('v','LVecBase3f_C_cross_into_v_pp','pp')
    LVecBase3f_C_set_x_v_pf = lib.func('v','LVecBase3f_C_set_x_v_pf','pf')

    # variadic

    generate_hash = {
        2 : lib.func('v','LVecBase3f_C_generate_hash_v_pp','pp'),
        3 : lib.func('v','LVecBase3f_C_generate_hash_v_ppf','ppf'),
    }
    ctor = {
        1 : lib.func('p','LVecBase3f_C_ctor_p_f','f'),
        3 : lib.func('p','LVecBase3f_C_ctor_p_fff','fff'),
        1 : lib.func('p','LVecBase3f_C_ctor_p_p','p'),
        2 : lib.func('p','LVecBase3f_C_ctor_p_pf','pf'),
        0 : lib.func('p','LVecBase3f_C_ctor_p_v',''),
    }
    add_hash = {
        2 : lib.func('p','LVecBase3f_C_add_hash_p_pp','pp'),
        3 : lib.func('p','LVecBase3f_C_add_hash_p_ppf','ppf'),
    }
    compare_to = {
        2 : lib.func('i','LVecBase3f_C_compare_to_i_pp','pp'),
        3 : lib.func('i','LVecBase3f_C_compare_to_i_ppf','ppf'),
    }
    almost_equal = {
        2 : lib.func('B','LVecBase3f_C_almost_equal_B_pp','pp'),
        3 : lib.func('B','LVecBase3f_C_almost_equal_B_ppf','ppf'),
    }
    get_hash = {
        1 : lib.func('p','LVecBase3f_C_get_hash_p_p','p'),
        2 : lib.func('p','LVecBase3f_C_get_hash_p_pf','pf'),
    }


    # c++ instance methods



    def get_standardized_hpr(self, *argv, **kw):
        return self.LVecBase3f_C_get_standardized_hpr_p_p(self.iptr, *argv, **kw)

    def add_to_cell(self, *argv, **kw):
        return self.LVecBase3f_C_add_to_cell_v_pif(self.iptr, *argv, **kw)

    @classmethod
    def get_class_type(cls, *argv, **kw):
        return cls.LVecBase3f_C_get_class_type_i_v(*argv, **kw)

    def fill(self, *argv, **kw):
        return self.LVecBase3f_C_fill_v_pf(self.iptr, *argv, **kw)

    def normalized(self, *argv, **kw):
        return self.LVecBase3f_C_normalized_p_p(self.iptr, *argv, **kw)

    def normalize(self, *argv, **kw):
        return self.LVecBase3f_C_normalize_B_p(self.iptr, *argv, **kw)

    def read_datagram(self, *argv, **kw):
        return self.LVecBase3f_C_read_datagram_v_pp(self.iptr, *argv, **kw)

    def fmin(self, *argv, **kw):
        return self.LVecBase3f_C_fmin_p_pp(self.iptr, *argv, **kw)

    def get_y(self, *argv, **kw):
        return self.LVecBase3f_C_get_y_f_p(self.iptr, *argv, **kw)

    def get_z(self, *argv, **kw):
        return self.LVecBase3f_C_get_z_f_p(self.iptr, *argv, **kw)

    def length_squared(self, *argv, **kw):
        return self.LVecBase3f_C_length_squared_f_p(self.iptr, *argv, **kw)

    def get_cell(self, *argv, **kw):
        return self.LVecBase3f_C_get_cell_f_pi(self.iptr, *argv, **kw)

    def output(self, *argv, **kw):
        return self.LVecBase3f_C_output_v_pp(self.iptr, *argv, **kw)

    def get_v(self, *argv, **kw):
        return self.LVecBase3f_C_get_v_p_p(self.iptr, *argv, **kw)

    def get_yz(self, *argv, **kw):
        return self.LVecBase3f_C_get_yz_p_p(self.iptr, *argv, **kw)

    def ctor_1(self, *argv, **kw):
        return self.LVecBase3f_C_ctor_1_p_p(self.iptr, *argv, **kw)

    def length(self, *argv, **kw):
        return self.LVecBase3f_C_length_f_p(self.iptr, *argv, **kw)

    def end_1(self, *argv, **kw):
        return self.LVecBase3f_C_end_1_v_p(self.iptr, *argv, **kw)

    @classmethod
    def get_num_components(cls, *argv, **kw):
        return cls.LVecBase3f_C_get_num_components_i_v(*argv, **kw)

    def end(self, *argv, **kw):
        return self.LVecBase3f_C_end_v_p(self.iptr, *argv, **kw)

    def generate_hash(self, *argv, **kw):
        return self.variadic_call("LVecBase3f_C_end_v_p", *argv, **kw)

    def read_datagram_fixed(self, *argv, **kw):
        return self.LVecBase3f_C_read_datagram_fixed_v_pp(self.iptr, *argv, **kw)

    def set(self, *argv, **kw):
        return self.LVecBase3f_C_set_v_pfff(self.iptr, *argv, **kw)

    def get_data(self, *argv, **kw):
        return self.LVecBase3f_C_get_data_v_p(self.iptr, *argv, **kw)

    def get_x(self, *argv, **kw):
        return self.LVecBase3f_C_get_x_f_p(self.iptr, *argv, **kw)

    def set_y(self, *argv, **kw):
        return self.LVecBase3f_C_set_y_v_pf(self.iptr, *argv, **kw)

    def set_z(self, *argv, **kw):
        return self.LVecBase3f_C_set_z_v_pf(self.iptr, *argv, **kw)

    @classmethod
    def unit_x(cls, *argv, **kw):
        return cls.LVecBase3f_C_unit_x_p_v(*argv, **kw)

    @classmethod
    def size(cls, *argv, **kw):
        return cls.LVecBase3f_C_size_i_v(*argv, **kw)

    def dot(self, *argv, **kw):
        return self.LVecBase3f_C_dot_f_pp(self.iptr, *argv, **kw)

    def get_xy(self, *argv, **kw):
        return self.LVecBase3f_C_get_xy_p_p(self.iptr, *argv, **kw)

    def get_xz(self, *argv, **kw):
        return self.LVecBase3f_C_get_xz_p_p(self.iptr, *argv, **kw)

    @classmethod
    def unit_y(cls, *argv, **kw):
        return cls.LVecBase3f_C_unit_y_p_v(*argv, **kw)

    @classmethod
    def unit_z(cls, *argv, **kw):
        return cls.LVecBase3f_C_unit_z_p_v(*argv, **kw)

    def write_datagram_fixed(self, *argv, **kw):
        return self.LVecBase3f_C_write_datagram_fixed_v_pp(self.iptr, *argv, **kw)

    def project(self, *argv, **kw):
        return self.LVecBase3f_C_project_p_pp(self.iptr, *argv, **kw)

    def begin(self, *argv, **kw):
        return self.LVecBase3f_C_begin_v_p(self.iptr, *argv, **kw)

    def write_datagram(self, *argv, **kw):
        return self.LVecBase3f_C_write_datagram_v_pp(self.iptr, *argv, **kw)

    def fmax(self, *argv, **kw):
        return self.LVecBase3f_C_fmax_p_pp(self.iptr, *argv, **kw)

    def add_z(self, *argv, **kw):
        return self.LVecBase3f_C_add_z_v_pf(self.iptr, *argv, **kw)

    def add_y(self, *argv, **kw):
        return self.LVecBase3f_C_add_y_v_pf(self.iptr, *argv, **kw)

    def is_nan(self, *argv, **kw):
        return self.LVecBase3f_C_is_nan_B_p(self.iptr, *argv, **kw)

    def add_x(self, *argv, **kw):
        return self.LVecBase3f_C_add_x_v_pf(self.iptr, *argv, **kw)

    def set_cell(self, *argv, **kw):
        return self.LVecBase3f_C_set_cell_v_pif(self.iptr, *argv, **kw)

    def begin_1(self, *argv, **kw):
        return self.LVecBase3f_C_begin_1_v_p(self.iptr, *argv, **kw)

    def cross(self, *argv, **kw):
        return self.LVecBase3f_C_cross_p_pp(self.iptr, *argv, **kw)

    def add_hash(self, *argv, **kw):
        return self.variadic_call("LVecBase3f_C_cross_p_pp", *argv, **kw)

    @classmethod
    def zero(cls, *argv, **kw):
        return cls.LVecBase3f_C_zero_p_v(*argv, **kw)

    def compare_to(self, *argv, **kw):
        return self.variadic_call("LVecBase3f_C_zero_p_v", *argv, **kw)

    def componentwise_mult(self, *argv, **kw):
        return self.LVecBase3f_C_componentwise_mult_v_pp(self.iptr, *argv, **kw)

    def almost_equal(self, *argv, **kw):
        return self.variadic_call("LVecBase3f_C_componentwise_mult_v_pp", *argv, **kw)

    @classmethod
    def init_type(cls, *argv, **kw):
        return cls.LVecBase3f_C_init_type_v_v(*argv, **kw)

    def get_hash(self, *argv, **kw):
        return self.variadic_call("LVecBase3f_C_init_type_v_v", *argv, **kw)

    def cross_into(self, *argv, **kw):
        return self.LVecBase3f_C_cross_into_v_pp(self.iptr, *argv, **kw)

    def set_x(self, *argv, **kw):
        return self.LVecBase3f_C_set_x_v_pf(self.iptr, *argv, **kw)

class Engine(cplusplus):

    lib = ffi.open("""libupanda3d_c.so""")

    Engine_C_get_framework_p_p = lib.func('p','Engine_C_get_framework_p_p','p')
    Engine_C_casetest_i_pipB = lib.func('i','Engine_C_casetest_i_pipB','pipB')
    Engine_C_HelloEngine_i_p = lib.func('i','Engine_C_HelloEngine_i_p','p')
    Engine_C_load_model_p_ps = lib.func('p','Engine_C_load_model_p_ps','ps')
    Engine_C_attach_v_pp = lib.func('v','Engine_C_attach_v_pp','pp')
    Engine_C_dtor_v_p = lib.func('v','Engine_C_dtor_v_p','p')
    Engine_C_get_version_string_s_v = lib.func('s','Engine_C_get_version_string_s_v','v')
    Engine_C_op_scale_v_ppp = lib.func('v','Engine_C_op_scale_v_ppp','ppp')
    Engine_C_set_framework_v_pp = lib.func('v','Engine_C_set_framework_v_pp','pp')
    Engine_C_step_v_p = lib.func('v','Engine_C_step_v_p','p')
    Engine_C_stop_v_v = lib.func('v','Engine_C_stop_v_v','v')
    Engine_C_is_alive_i_v = lib.func('i','Engine_C_is_alive_i_v','v')
    Engine_C_build_v_p = lib.func('v','Engine_C_build_v_p','p')
    Engine_C_op_pos_v_ppp = lib.func('v','Engine_C_op_pos_v_ppp','ppp')
    Engine_C_get_wframe_p_p = lib.func('p','Engine_C_get_wframe_p_p','p')

    # variadic

    ctor = {
        1 : lib.func('p','Engine_C_ctor_p_p','p'),
        0 : lib.func('p','Engine_C_ctor_p_v',''),
    }


    # c++ instance methods



    def get_framework(self, *argv, **kw):
        return self.Engine_C_get_framework_p_p(self.iptr, *argv, **kw)

    def casetest(self, *argv, **kw):
        return self.Engine_C_casetest_i_pipB(self.iptr, *argv, **kw)

    def HelloEngine(self, *argv, **kw):
        return self.Engine_C_HelloEngine_i_p(self.iptr, *argv, **kw)

    def load_model(self, *argv, **kw):
        return self.Engine_C_load_model_p_ps(self.iptr, *argv, **kw)

    def attach(self, *argv, **kw):
        return self.Engine_C_attach_v_pp(self.iptr, *argv, **kw)

    def dtor(self, *argv, **kw):
        return self.Engine_C_dtor_v_p(self.iptr, *argv, **kw)

    @classmethod
    def get_version_string(cls, *argv, **kw):
        return cls.Engine_C_get_version_string_s_v(*argv, **kw)

    def op_scale(self, *argv, **kw):
        return self.Engine_C_op_scale_v_ppp(self.iptr, *argv, **kw)

    def set_framework(self, *argv, **kw):
        return self.Engine_C_set_framework_v_pp(self.iptr, *argv, **kw)

    def step(self, *argv, **kw):
        return self.Engine_C_step_v_p(self.iptr, *argv, **kw)

    @classmethod
    def stop(cls, *argv, **kw):
        return cls.Engine_C_stop_v_v(*argv, **kw)

    @classmethod
    def is_alive(cls, *argv, **kw):
        return cls.Engine_C_is_alive_i_v(*argv, **kw)

    def build(self, *argv, **kw):
        return self.Engine_C_build_v_p(self.iptr, *argv, **kw)

    def op_pos(self, *argv, **kw):
        return self.Engine_C_op_pos_v_ppp(self.iptr, *argv, **kw)

    def get_wframe(self, *argv, **kw):
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

def test3():
    print("C++ class constructor",Engine.ctor)
    E = Engine()
    print('engine      ',E, E.iptr)
    C = E.__class__( iptr=E.iptr )
    print('engine(copy)',C, C.iptr)

    # a dumb test that should say 42
    print('hello',E.HelloEngine())

    print('version','=', E.get_version_string())

    E.build()

    np = E.load_model( "model.bam" )

    print("np","=",np)

    E.attach(np)

    np = NodePath(iptr=np)

    v3 = LVecBase3f(0.01, 42.01, 0.01)
    print( v3, v3.get_x() , v3.get_y(), v3.get_z() )
    np.set_pos( uctypes.bytearray_at(v3.iptr, 12) )

    v3 = LVecBase3f(2.0, 2.0, 2.0)
    print( v3, v3.get_x() , v3.get_y(), v3.get_z() )
    np.set_scale( uctypes.bytearray_at(v3.iptr, 12) )


    while E.is_alive():
        E.step()

    print("C++ engine requested exit")
    del E
    print("deleting copy")
    del C


if 0:
    print("--- test1 with forced del ----")
    test1()
    del test1
    gc.collect()
    gc.collect()

if 0:
    print("--- test2 with refcounting ----")
    test2()
    del test1,test2
    gc.collect()
    gc.collect()

if 1:
    print("--- test3 with refcounting ----")
    test3()
    del test1,test2,test3
    gc.collect()
    gc.collect()

gc.collect()
gc.collect()  # one more it's free !
print(REFC)
if GCBAD:print(" ----------- Bad GC ------------") # who said free ?

#luckily we have 1 pointer left
REFC = list(REFC.keys())
while REFC:
    Engine.Engine_C_dtor_v_p(REFC.pop())




