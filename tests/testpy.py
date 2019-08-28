# upy
import os
import sys
import ffi
import uctypes
import gc
import time


if not '.' in sys.path: sys.path.insert(0,'.')
from cplusplus import cplusplus, cstructs



class NodePath(cplusplus):
    c = cstructs()
    c.name = """NodePath@upanda3d_c"""
    c.dlopen("""libupanda3d_c.so""")


    # ctor/dtor

    c.ct['ctor'] = {
        1 : ['s','p', c.lib.func('p','NodePath_C_ctor_p_p','p')],
        0 : ['s','p', c.lib.func('p','NodePath_C_ctor_p_v','')],
    }

    # fixed pos

    c.ct['look_at'] = ['d','v', c.lib.func('v','NodePath_C_look_at_v_pfff','pfff')]
    c.ct['set_scale'] = ['d','v', c.lib.func('v','NodePath_C_set_scale_v_pp','pp')]
    c.ct['set_pos'] = ['d','v', c.lib.func('v','NodePath_C_set_pos_v_pp','pp')]
    c.ct['reparent_to'] = ['d','v', c.lib.func('v','NodePath_C_reparent_to_v_pp','pp')]

    # variadic



    # c++ instance methods

    def __getattr__(self, attr):
        return self.__call(attr)



    del c.lib


class LVecBase3f(cplusplus):
    c = cstructs()
    c.name = """LVecBase3f@upanda3d_c"""
    c.dlopen("""libupanda3d_c.so""")


    # ctor/dtor

    c.ct['ctor_1'] = ['s','p', c.lib.func('p','LVecBase3f_C_ctor_1_p_p','p')]
    c.ct['ctor'] = {
        1 : ['s','p', c.lib.func('p','LVecBase3f_C_ctor_p_f','f')],
        3 : ['s','p', c.lib.func('p','LVecBase3f_C_ctor_p_fff','fff')],
        1 : ['s','p', c.lib.func('p','LVecBase3f_C_ctor_p_p','p')],
        2 : ['s','p', c.lib.func('p','LVecBase3f_C_ctor_p_pf','pf')],
        0 : ['s','p', c.lib.func('p','LVecBase3f_C_ctor_p_v','')],
    }

    # fixed pos

    c.ct['get_standardized_hpr'] = ['d','p', c.lib.func('p','LVecBase3f_C_get_standardized_hpr_p_p','p')]
    c.ct['add_to_cell'] = ['d','v', c.lib.func('v','LVecBase3f_C_add_to_cell_v_pif','pif')]
    c.ct['get_class_type'] = ['d','i', c.lib.func('i','LVecBase3f_C_get_class_type_i_v','v')]
    c.ct['fill'] = ['d','v', c.lib.func('v','LVecBase3f_C_fill_v_pf','pf')]
    c.ct['normalized'] = ['d','p', c.lib.func('p','LVecBase3f_C_normalized_p_p','p')]
    c.ct['normalize'] = ['d','B', c.lib.func('B','LVecBase3f_C_normalize_B_p','p')]
    c.ct['read_datagram'] = ['d','v', c.lib.func('v','LVecBase3f_C_read_datagram_v_pp','pp')]
    c.ct['fmin'] = ['d','p', c.lib.func('p','LVecBase3f_C_fmin_p_pp','pp')]
    c.ct['get_y'] = ['d','f', c.lib.func('f','LVecBase3f_C_get_y_f_p','p')]
    c.ct['get_z'] = ['d','f', c.lib.func('f','LVecBase3f_C_get_z_f_p','p')]
    c.ct['length_squared'] = ['d','f', c.lib.func('f','LVecBase3f_C_length_squared_f_p','p')]
    c.ct['get_cell'] = ['d','f', c.lib.func('f','LVecBase3f_C_get_cell_f_pi','pi')]
    c.ct['output'] = ['d','v', c.lib.func('v','LVecBase3f_C_output_v_pp','pp')]
    c.ct['get_v'] = ['d','p', c.lib.func('p','LVecBase3f_C_get_v_p_p','p')]
    c.ct['get_yz'] = ['d','p', c.lib.func('p','LVecBase3f_C_get_yz_p_p','p')]
    c.ct['length'] = ['d','f', c.lib.func('f','LVecBase3f_C_length_f_p','p')]
    c.ct['end_1'] = ['d','v', c.lib.func('v','LVecBase3f_C_end_1_v_p','p')]
    c.ct['get_num_components'] = ['d','i', c.lib.func('i','LVecBase3f_C_get_num_components_i_v','v')]
    c.ct['end'] = ['d','v', c.lib.func('v','LVecBase3f_C_end_v_p','p')]
    c.ct['read_datagram_fixed'] = ['d','v', c.lib.func('v','LVecBase3f_C_read_datagram_fixed_v_pp','pp')]
    c.ct['set'] = ['d','v', c.lib.func('v','LVecBase3f_C_set_v_pfff','pfff')]
    c.ct['get_data'] = ['d','v', c.lib.func('v','LVecBase3f_C_get_data_v_p','p')]
    c.ct['get_x'] = ['d','f', c.lib.func('f','LVecBase3f_C_get_x_f_p','p')]
    c.ct['set_y'] = ['d','v', c.lib.func('v','LVecBase3f_C_set_y_v_pf','pf')]
    c.ct['set_z'] = ['d','v', c.lib.func('v','LVecBase3f_C_set_z_v_pf','pf')]
    c.ct['unit_x'] = ['d','p', c.lib.func('p','LVecBase3f_C_unit_x_p_v','v')]
    c.ct['size'] = ['d','i', c.lib.func('i','LVecBase3f_C_size_i_v','v')]
    c.ct['dot'] = ['d','f', c.lib.func('f','LVecBase3f_C_dot_f_pp','pp')]
    c.ct['get_xy'] = ['d','p', c.lib.func('p','LVecBase3f_C_get_xy_p_p','p')]
    c.ct['get_xz'] = ['d','p', c.lib.func('p','LVecBase3f_C_get_xz_p_p','p')]
    c.ct['unit_y'] = ['d','p', c.lib.func('p','LVecBase3f_C_unit_y_p_v','v')]
    c.ct['unit_z'] = ['d','p', c.lib.func('p','LVecBase3f_C_unit_z_p_v','v')]
    c.ct['write_datagram_fixed'] = ['d','v', c.lib.func('v','LVecBase3f_C_write_datagram_fixed_v_pp','pp')]
    c.ct['project'] = ['d','p', c.lib.func('p','LVecBase3f_C_project_p_pp','pp')]
    c.ct['begin'] = ['d','v', c.lib.func('v','LVecBase3f_C_begin_v_p','p')]
    c.ct['write_datagram'] = ['d','v', c.lib.func('v','LVecBase3f_C_write_datagram_v_pp','pp')]
    c.ct['fmax'] = ['d','p', c.lib.func('p','LVecBase3f_C_fmax_p_pp','pp')]
    c.ct['add_z'] = ['d','v', c.lib.func('v','LVecBase3f_C_add_z_v_pf','pf')]
    c.ct['add_y'] = ['d','v', c.lib.func('v','LVecBase3f_C_add_y_v_pf','pf')]
    c.ct['is_nan'] = ['d','B', c.lib.func('B','LVecBase3f_C_is_nan_B_p','p')]
    c.ct['add_x'] = ['d','v', c.lib.func('v','LVecBase3f_C_add_x_v_pf','pf')]
    c.ct['set_cell'] = ['d','v', c.lib.func('v','LVecBase3f_C_set_cell_v_pif','pif')]
    c.ct['begin_1'] = ['d','v', c.lib.func('v','LVecBase3f_C_begin_1_v_p','p')]
    c.ct['cross'] = ['d','p', c.lib.func('p','LVecBase3f_C_cross_p_pp','pp')]
    c.ct['zero'] = ['d','p', c.lib.func('p','LVecBase3f_C_zero_p_v','v')]
    c.ct['componentwise_mult'] = ['d','v', c.lib.func('v','LVecBase3f_C_componentwise_mult_v_pp','pp')]
    c.ct['init_type'] = ['d','v', c.lib.func('v','LVecBase3f_C_init_type_v_v','v')]
    c.ct['cross_into'] = ['d','v', c.lib.func('v','LVecBase3f_C_cross_into_v_pp','pp')]
    c.ct['set_x'] = ['d','v', c.lib.func('v','LVecBase3f_C_set_x_v_pf','pf')]

    # variadic

    c.ct['generate_hash'] = {
        2 : ['d','v', c.lib.func('v','LVecBase3f_C_generate_hash_v_pp','pp')],
        3 : ['d','v', c.lib.func('v','LVecBase3f_C_generate_hash_v_ppf','ppf')],
    }
    c.ct['add_hash'] = {
        2 : ['d','p', c.lib.func('p','LVecBase3f_C_add_hash_p_pp','pp')],
        3 : ['d','p', c.lib.func('p','LVecBase3f_C_add_hash_p_ppf','ppf')],
    }
    c.ct['compare_to'] = {
        2 : ['d','i', c.lib.func('i','LVecBase3f_C_compare_to_i_pp','pp')],
        3 : ['d','i', c.lib.func('i','LVecBase3f_C_compare_to_i_ppf','ppf')],
    }
    c.ct['almost_equal'] = {
        2 : ['d','B', c.lib.func('B','LVecBase3f_C_almost_equal_B_pp','pp')],
        3 : ['d','B', c.lib.func('B','LVecBase3f_C_almost_equal_B_ppf','ppf')],
    }
    c.ct['get_hash'] = {
        1 : ['d','p', c.lib.func('p','LVecBase3f_C_get_hash_p_p','p')],
        2 : ['d','p', c.lib.func('p','LVecBase3f_C_get_hash_p_pf','pf')],
    }


    # c++ instance methods

    def __getattr__(self, attr):
        return self.__call(attr)



    del c.lib


class Engine(cplusplus):
    c = cstructs()
    c.name = """Engine@upanda3d_c"""
    c.dlopen("""libupanda3d_c.so""")


    # ctor/dtor

    c.ct['ctor'] = {
        1 : ['s','p', c.lib.func('p','Engine_C_ctor_p_p','p')],
        0 : ['s','p', c.lib.func('p','Engine_C_ctor_p_v','')],
    }
    c.ct['dtor'] = ['s','v', c.lib.func('v','Engine_C_dtor_v_p','p')]

    # fixed pos

    c.ct['get_framework'] = ['d','p', c.lib.func('p','Engine_C_get_framework_p_p','p')]
    c.ct['casetest'] = ['d','i', c.lib.func('i','Engine_C_casetest_i_pipB','pipB')]
    c.ct['HelloEngine'] = ['d','i', c.lib.func('i','Engine_C_HelloEngine_i_p','p')]
    c.ct['load_model'] = ['d','p', c.lib.func('p','Engine_C_load_model_p_ps','ps')]
    c.ct['attach'] = ['d','v', c.lib.func('v','Engine_C_attach_v_pp','pp')]
    c.ct['get_version_string'] = ['d','s', c.lib.func('s','Engine_C_get_version_string_s_v','v')]
    c.ct['op_scale'] = ['d','v', c.lib.func('v','Engine_C_op_scale_v_ppp','ppp')]
    c.ct['set_framework'] = ['d','v', c.lib.func('v','Engine_C_set_framework_v_pp','pp')]
    c.ct['step'] = ['d','v', c.lib.func('v','Engine_C_step_v_p','p')]
    c.ct['stop'] = ['d','v', c.lib.func('v','Engine_C_stop_v_v','v')]
    c.ct['is_alive'] = ['d','i', c.lib.func('i','Engine_C_is_alive_i_v','v')]
    c.ct['build'] = ['d','v', c.lib.func('v','Engine_C_build_v_p','p')]
    c.ct['op_pos'] = ['d','v', c.lib.func('v','Engine_C_op_pos_v_ppp','ppp')]
    c.ct['get_wframe'] = ['d','p', c.lib.func('p','Engine_C_get_wframe_p_p','p')]

    # variadic



    # c++ instance methods

    def __getattr__(self, attr):
        return self.__call(attr)



    del c.lib


def test():
    print("C++ class constructor", Engine.c.ct['ctor'])
    E = Engine()
    print('engine      ',E)
    C = E.__class__( iptr=E )
    print('engine(copy)',C)

    # a dumb test that should say 42
    print('hello',E.HelloEngine())

    print('version','=', E.get_version_string())

    E.build()

    np = E.load_model( "model.bam" )

    print("np","=",np)

    E.attach(np)

    np = NodePath(cptr=np)

    v3 = LVecBase3f(0.01, 42.01, 0.01)
    print( v3, v3.get_x() , v3.get_y(), v3.get_z() )
    np.set_pos( v3 )

    v3 = LVecBase3f(2.0, 2.0, 2.0)
    print( v3, v3.get_x() , v3.get_y(), v3.get_z() )

    np.set_scale( v3 )




    while E.is_alive():
        E.step()

    print("C++ engine requested exit")
    del E
    print("deleting copy")
    del C

print("--- test3 with refcounting ----")
test()
del test
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


