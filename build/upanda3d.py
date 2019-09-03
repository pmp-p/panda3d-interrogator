# upy

import sys


if not '.' in sys.path: sys.path.insert(0,'.')
import interrogator.uplusplus as cxx

cxx.cstructs.decl.extend(['vector_uchar', 'WindowFramework::BackgroundType', 'WindowFramework', 'TransparencyAttrib::Mode', 'TransformState', 'TextureStageCollection', 'TextureStage', 'TextureCollection', 'Texture', 'TextFont', 'TextEncoder::Encoding', 'ShaderInput', 'Shader', 'SamplerState', 'RenderState', 'RenderModeAttrib::Mode', 'RenderEffects', 'RenderEffect', 'RenderAttrib::TexGenMode', 'RenderAttrib', 'RecorderController', 'PandaSystem', 'PandaNode', 'PandaFramework', 'NodePathCollection', 'NodePath::ErrorType', 'NodePath', 'MaterialCollection', 'Material', 'LogicOpAttrib::Operation', 'LVector3', 'LVecBase4', 'LVecBase3f::EVector3', 'LVecBase3f', 'LVecBase3', 'LVecBase2f', 'LVecBase2', 'LQuaternion', 'LPoint3', 'LMatrix4', 'LColor', 'InternalNameCollection', 'GraphicsWindow', 'GraphicsPipe', 'GraphicsOutput', 'GraphicsEngine', 'Fog', 'Filename::Type', 'Filename', 'EventHandler', 'Engine', 'DrawMask', 'DisplayRegion', 'ConfigPage', 'ConfigDeclaration', 'CollideMask', 'Camera', 'BoundingVolume', 'AuxSceneData', 'AsyncTaskManager'])




class LVecBase3f(cxx.cplusplus):
    c = cxx.cstructs().register("LVecBase3f", "upanda3d", """libupanda3d_c.so""")


    # ctor/dtor : classmethod type calls and return only raw pointer or void

    c.ct['ctor_1'] = ['s', 33, c.lib.func('p','LVecBase3f_C_ctor_1_p_p','p')]
    c.ct['ctor'] = {
        1 : ['s', 33, c.lib.func('p','LVecBase3f_C_ctor_p_f','f')],
        3 : ['s', 33, c.lib.func('p','LVecBase3f_C_ctor_p_fff','fff')],
        1 : ['s', 33, c.lib.func('p','LVecBase3f_C_ctor_p_p','p')],
        2 : ['s', 33, c.lib.func('p','LVecBase3f_C_ctor_p_pf','pf')],
        0 : ['s', 'p', c.lib.func('p','LVecBase3f_C_ctor_p_v','')],
    }

    # fixed pos : return basic types or other C++ classes

    c.ct['get_standardized_hpr'] = ['d', 33, c.lib.func('p','LVecBase3f_C_get_standardized_hpr_p_p','p')]
    c.ct['add_to_cell'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_add_to_cell_v_pif','pif')]
    c.ct['get_class_type'] = ['d', 'i', c.lib.func('i','LVecBase3f_C_get_class_type_i_v','v')]
    c.ct['fill'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_fill_v_pf','pf')]
    c.ct['normalized'] = ['d', 33, c.lib.func('p','LVecBase3f_C_normalized_p_p','p')]
    c.ct['normalize'] = ['d', 'B', c.lib.func('B','LVecBase3f_C_normalize_B_p','p')]
    c.ct['read_datagram'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_read_datagram_v_pp','pp')]
    c.ct['fmin'] = ['d', 33, c.lib.func('p','LVecBase3f_C_fmin_p_pp','pp')]
    c.ct['get_y'] = ['d', 'f', c.lib.func('f','LVecBase3f_C_get_y_f_p','p')]
    c.ct['get_z'] = ['d', 'f', c.lib.func('f','LVecBase3f_C_get_z_f_p','p')]
    c.ct['length_squared'] = ['d', 'f', c.lib.func('f','LVecBase3f_C_length_squared_f_p','p')]
    c.ct['get_cell'] = ['d', 'f', c.lib.func('f','LVecBase3f_C_get_cell_f_pi','pi')]
    c.ct['output'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_output_v_pp','pp')]
    c.ct['get_v'] = ['d', 'p', c.lib.func('p','LVecBase3f_C_get_v_p_p','p')]
    c.ct['get_yz'] = ['d', 35, c.lib.func('p','LVecBase3f_C_get_yz_p_p','p')]
    c.ct['length'] = ['d', 'f', c.lib.func('f','LVecBase3f_C_length_f_p','p')]
    c.ct['end_1'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_end_1_v_p','p')]
    c.ct['get_num_components'] = ['d', 'i', c.lib.func('i','LVecBase3f_C_get_num_components_i_v','v')]
    c.ct['end'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_end_v_p','p')]
    c.ct['read_datagram_fixed'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_read_datagram_fixed_v_pp','pp')]
    c.ct['set'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_set_v_pfff','pfff')]
    c.ct['get_data'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_get_data_v_p','p')]
    c.ct['get_x'] = ['d', 'f', c.lib.func('f','LVecBase3f_C_get_x_f_p','p')]
    c.ct['set_y'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_set_y_v_pf','pf')]
    c.ct['set_z'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_set_z_v_pf','pf')]
    c.ct['unit_x'] = ['d', 33, c.lib.func('p','LVecBase3f_C_unit_x_p_v','v')]
    c.ct['size'] = ['d', 'i', c.lib.func('i','LVecBase3f_C_size_i_v','v')]
    c.ct['dot'] = ['d', 'f', c.lib.func('f','LVecBase3f_C_dot_f_pp','pp')]
    c.ct['get_xy'] = ['d', 'p', c.lib.func('p','LVecBase3f_C_get_xy_p_p','p')]
    c.ct['get_xz'] = ['d', 35, c.lib.func('p','LVecBase3f_C_get_xz_p_p','p')]
    c.ct['unit_y'] = ['d', 33, c.lib.func('p','LVecBase3f_C_unit_y_p_v','v')]
    c.ct['unit_z'] = ['d', 33, c.lib.func('p','LVecBase3f_C_unit_z_p_v','v')]
    c.ct['write_datagram_fixed'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_write_datagram_fixed_v_pp','pp')]
    c.ct['project'] = ['d', 33, c.lib.func('p','LVecBase3f_C_project_p_pp','pp')]
    c.ct['begin'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_begin_v_p','p')]
    c.ct['write_datagram'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_write_datagram_v_pp','pp')]
    c.ct['fmax'] = ['d', 33, c.lib.func('p','LVecBase3f_C_fmax_p_pp','pp')]
    c.ct['add_z'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_add_z_v_pf','pf')]
    c.ct['add_y'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_add_y_v_pf','pf')]
    c.ct['is_nan'] = ['d', 'B', c.lib.func('B','LVecBase3f_C_is_nan_B_p','p')]
    c.ct['add_x'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_add_x_v_pf','pf')]
    c.ct['set_cell'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_set_cell_v_pif','pif')]
    c.ct['begin_1'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_begin_1_v_p','p')]
    c.ct['cross'] = ['d', 33, c.lib.func('p','LVecBase3f_C_cross_p_pp','pp')]
    c.ct['zero'] = ['d', 33, c.lib.func('p','LVecBase3f_C_zero_p_v','v')]
    c.ct['componentwise_mult'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_componentwise_mult_v_pp','pp')]
    c.ct['init_type'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_init_type_v_v','v')]
    c.ct['cross_into'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_cross_into_v_pp','pp')]
    c.ct['set_x'] = ['d', 'v', c.lib.func('v','LVecBase3f_C_set_x_v_pf','pf')]

    # variadic : return basic types or other C++ classes

    c.ct['generate_hash'] = {
        2 : ['d', 'v', c.lib.func('v','LVecBase3f_C_generate_hash_v_pp','pp')],
        3 : ['d', 'v', c.lib.func('v','LVecBase3f_C_generate_hash_v_ppf','ppf')],
    }
    c.ct['add_hash'] = {
        2 : ['d', 'p', c.lib.func('p','LVecBase3f_C_add_hash_p_pp','pp')],
        3 : ['d', 'p', c.lib.func('p','LVecBase3f_C_add_hash_p_ppf','ppf')],
    }
    c.ct['compare_to'] = {
        2 : ['d', 'i', c.lib.func('i','LVecBase3f_C_compare_to_i_pp','pp')],
        3 : ['d', 'i', c.lib.func('i','LVecBase3f_C_compare_to_i_ppf','ppf')],
    }
    c.ct['almost_equal'] = {
        2 : ['d', 'B', c.lib.func('B','LVecBase3f_C_almost_equal_B_pp','pp')],
        3 : ['d', 'B', c.lib.func('B','LVecBase3f_C_almost_equal_B_ppf','ppf')],
    }
    c.ct['get_hash'] = {
        1 : ['d', 'p', c.lib.func('p','LVecBase3f_C_get_hash_p_p','p')],
        2 : ['d', 'p', c.lib.func('p','LVecBase3f_C_get_hash_p_pf','pf')],
    }


    # c++ instance methods

    def __del__(self):
        self.__class__.destroy(self)

    def __getattr__(self, attr):
        return self.__call(attr)

LVecBase3f.c.link(LVecBase3f)



class PandaFramework(cxx.cplusplus):
    c = cxx.cstructs().register("PandaFramework", "upanda3d", """libupanda3d_c.so""")


    # ctor/dtor : classmethod type calls and return only raw pointer or void

    c.ct['ctor'] = {
        1 : ['s', 23, c.lib.func('p','PandaFramework_C_ctor_p_p','p')],
        0 : ['s', 'p', c.lib.func('p','PandaFramework_C_ctor_p_v','')],
    }

    # fixed pos : return basic types or other C++ classes

    c.ct['open_window_2'] = ['d', 2, c.lib.func('p','PandaFramework_C_open_window_2_p_ppipp','ppipp')]
    c.ct['get_texture'] = ['d', 'B', c.lib.func('B','PandaFramework_C_get_texture_B_p','p')]
    c.ct['do_frame'] = ['d', 'B', c.lib.func('B','PandaFramework_C_do_frame_B_pp','pp')]
    c.ct['get_graphics_engine'] = ['d', 'p', c.lib.func('p','PandaFramework_C_get_graphics_engine_p_p','p')]
    c.ct['has_highlight'] = ['d', 'B', c.lib.func('B','PandaFramework_C_has_highlight_B_p','p')]
    c.ct['get_wireframe'] = ['d', 'B', c.lib.func('B','PandaFramework_C_get_wireframe_B_p','p')]
    c.ct['get_data_root'] = ['d', 26, c.lib.func('p','PandaFramework_C_get_data_root_p_p','p')]
    c.ct['get_event_handler'] = ['d', 'p', c.lib.func('p','PandaFramework_C_get_event_handler_p_p','p')]
    c.ct['find_window_1'] = ['d', 'i', c.lib.func('i','PandaFramework_C_find_window_1_i_pp','pp')]
    c.ct['set_two_sided'] = ['d', 'v', c.lib.func('v','PandaFramework_C_set_two_sided_v_pB','pB')]
    c.ct['get_default_window_props'] = ['d', 'v', c.lib.func('v','PandaFramework_C_get_default_window_props_v_pp','pp')]
    c.ct['close_framework'] = ['d', 'v', c.lib.func('v','PandaFramework_C_close_framework_v_p','p')]
    c.ct['enable_default_keys'] = ['d', 'v', c.lib.func('v','PandaFramework_C_enable_default_keys_v_p','p')]
    c.ct['close_all_windows'] = ['d', 'v', c.lib.func('v','PandaFramework_C_close_all_windows_v_p','p')]
    c.ct['set_texture'] = ['d', 'v', c.lib.func('v','PandaFramework_C_set_texture_v_pB','pB')]
    c.ct['hide_collision_solids'] = ['d', 'i', c.lib.func('i','PandaFramework_C_hide_collision_solids_i_pp','pp')]
    c.ct['remove_mouse'] = ['d', 'v', c.lib.func('v','PandaFramework_C_remove_mouse_v_pp','pp')]
    c.ct['clear_highlight'] = ['d', 'v', c.lib.func('v','PandaFramework_C_clear_highlight_v_p','p')]
    c.ct['set_highlight'] = ['d', 'v', c.lib.func('v','PandaFramework_C_set_highlight_v_pp','pp')]
    c.ct['main_loop'] = ['d', 'v', c.lib.func('v','PandaFramework_C_main_loop_v_p','p')]
    c.ct['get_models'] = ['d', 26, c.lib.func('p','PandaFramework_C_get_models_p_p','p')]
    c.ct['set_lighting'] = ['d', 'v', c.lib.func('v','PandaFramework_C_set_lighting_v_pB','pB')]
    c.ct['get_window'] = ['d', 2, c.lib.func('p','PandaFramework_C_get_window_p_pi','pi')]
    c.ct['report_frame_rate'] = ['d', 'v', c.lib.func('v','PandaFramework_C_report_frame_rate_v_pp','pp')]
    c.ct['set_window_title'] = ['d', 'v', c.lib.func('v','PandaFramework_C_set_window_title_v_pp','pp')]
    c.ct['set_wireframe'] = ['d', 'v', c.lib.func('v','PandaFramework_C_set_wireframe_v_pB','pB')]
    c.ct['get_two_sided'] = ['d', 'B', c.lib.func('B','PandaFramework_C_get_two_sided_B_p','p')]
    c.ct['get_highlight'] = ['d', 26, c.lib.func('p','PandaFramework_C_get_highlight_p_p','p')]
    c.ct['get_task_mgr'] = ['d', 'p', c.lib.func('p','PandaFramework_C_get_task_mgr_p_p','p')]
    c.ct['show_collision_solids'] = ['d', 'i', c.lib.func('i','PandaFramework_C_show_collision_solids_i_pp','pp')]
    c.ct['set_perpixel'] = ['d', 'v', c.lib.func('v','PandaFramework_C_set_perpixel_v_pB','pB')]
    c.ct['set_background_type'] = ['d', 'v', c.lib.func('v','PandaFramework_C_set_background_type_v_pp','pp')]
    c.ct['set_exit_flag'] = ['d', 'v', c.lib.func('v','PandaFramework_C_set_exit_flag_v_p','p')]
    c.ct['open_framework'] = ['d', 'v', c.lib.func('v','PandaFramework_C_open_framework_v_p','p')]
    c.ct['get_default_pipe'] = ['d', 'p', c.lib.func('p','PandaFramework_C_get_default_pipe_p_p','p')]
    c.ct['reset_frame_rate'] = ['d', 'v', c.lib.func('v','PandaFramework_C_reset_frame_rate_v_p','p')]
    c.ct['set_recorder'] = ['d', 'v', c.lib.func('v','PandaFramework_C_set_recorder_v_pp','pp')]
    c.ct['clear_exit_flag'] = ['d', 'v', c.lib.func('v','PandaFramework_C_clear_exit_flag_v_p','p')]
    c.ct['all_windows_closed'] = ['d', 'B', c.lib.func('B','PandaFramework_C_all_windows_closed_B_p','p')]
    c.ct['get_background_type'] = ['d', 'p', c.lib.func('p','PandaFramework_C_get_background_type_p_p','p')]
    c.ct['get_num_windows'] = ['d', 'i', c.lib.func('i','PandaFramework_C_get_num_windows_i_p','p')]
    c.ct['find_window'] = ['d', 'i', c.lib.func('i','PandaFramework_C_find_window_i_pp','pp')]
    c.ct['get_recorder'] = ['d', 'p', c.lib.func('p','PandaFramework_C_get_recorder_p_p','p')]
    c.ct['get_perpixel'] = ['d', 'B', c.lib.func('B','PandaFramework_C_get_perpixel_B_p','p')]
    c.ct['get_mouse'] = ['d', 26, c.lib.func('p','PandaFramework_C_get_mouse_p_pp','pp')]
    c.ct['get_lighting'] = ['d', 'B', c.lib.func('B','PandaFramework_C_get_lighting_B_p','p')]

    # variadic : return basic types or other C++ classes

    c.ct['close_window'] = {
        2 : ['d', 'v', c.lib.func('v','PandaFramework_C_close_window_v_pi','pi')],
        2 : ['d', 'v', c.lib.func('v','PandaFramework_C_close_window_v_pp','pp')],
    }
    c.ct['open_window'] = {
        1 : ['d', 'p', c.lib.func('p','PandaFramework_C_open_window_p_p','p')],
        5 : ['d', 2, c.lib.func('p','PandaFramework_C_open_window_p_ppipp','ppipp')],
        3 : ['d', 2, c.lib.func('p','PandaFramework_C_open_window_p_ppp','ppp')],
    }
    c.ct['open_window_1'] = {
        5 : ['d', 2, c.lib.func('p','PandaFramework_C_open_window_1_p_ppipp','ppipp')],
        3 : ['d', 2, c.lib.func('p','PandaFramework_C_open_window_1_p_ppp','ppp')],
    }


    # c++ instance methods

    def __del__(self):
        self.__class__.destroy(self)

    def __getattr__(self, attr):
        return self.__call(attr)

PandaFramework.c.link(PandaFramework)



class Engine(cxx.cplusplus):
    c = cxx.cstructs().register("Engine", "upanda3d", """libupanda3d_c.so""")


    # ctor/dtor : classmethod type calls and return only raw pointer or void

    c.ct['ctor'] = {
        1 : ['s', 50, c.lib.func('p','Engine_C_ctor_p_p','p')],
        0 : ['s', 'p', c.lib.func('p','Engine_C_ctor_p_v','')],
    }
    c.ct['dtor'] = ['s', 'v', c.lib.func('v','Engine_C_dtor_v_p','p')]

    # fixed pos : return basic types or other C++ classes

    c.ct['get_framework'] = ['d', 23, c.lib.func('p','Engine_C_get_framework_p_p','p')]
    c.ct['casetest'] = ['d', 'i', c.lib.func('i','Engine_C_casetest_i_pipB','pipB')]
    c.ct['HelloEngine'] = ['d', 'i', c.lib.func('i','Engine_C_HelloEngine_i_p','p')]
    c.ct['load_model'] = ['d', 26, c.lib.func('p','Engine_C_load_model_p_ps','ps')]
    c.ct['attach'] = ['d', 'v', c.lib.func('v','Engine_C_attach_v_pp','pp')]
    c.ct['get_version_string'] = ['d', 's', c.lib.func('s','Engine_C_get_version_string_s_v','v')]
    c.ct['op_scale'] = ['d', 'v', c.lib.func('v','Engine_C_op_scale_v_ppp','ppp')]
    c.ct['set_framework'] = ['d', 'v', c.lib.func('v','Engine_C_set_framework_v_pp','pp')]
    c.ct['step'] = ['d', 'v', c.lib.func('v','Engine_C_step_v_p','p')]
    c.ct['stop'] = ['d', 'v', c.lib.func('v','Engine_C_stop_v_v','v')]
    c.ct['is_alive'] = ['d', 'i', c.lib.func('i','Engine_C_is_alive_i_v','v')]
    c.ct['build'] = ['d', 'v', c.lib.func('v','Engine_C_build_v_p','p')]
    c.ct['op_pos'] = ['d', 'v', c.lib.func('v','Engine_C_op_pos_v_ppp','ppp')]
    c.ct['get_wframe'] = ['d', 2, c.lib.func('p','Engine_C_get_wframe_p_p','p')]

    # variadic : return basic types or other C++ classes



    # c++ instance methods

    def __del__(self):
        self.__class__.destroy(self)

    def __getattr__(self, attr):
        return self.__call(attr)

Engine.c.link(Engine)



class PandaSystem(cxx.cplusplus):
    c = cxx.cstructs().register("PandaSystem", "upanda3d", """libupanda3d_c.so""")


    # ctor/dtor : classmethod type calls and return only raw pointer or void


    # fixed pos : return basic types or other C++ classes

    c.ct['add_system'] = ['d', 'v', c.lib.func('v','PandaSystem_C_add_system_v_pp','pp')]
    c.ct['set_system_tag'] = ['d', 'v', c.lib.func('v','PandaSystem_C_set_system_tag_v_pppp','pppp')]
    c.ct['get_global_ptr'] = ['d', 'p', c.lib.func('p','PandaSystem_C_get_global_ptr_p_v','v')]
    c.ct['get_platform'] = ['d', 's', c.lib.func('s','PandaSystem_C_get_platform_s_v','v')]
    c.ct['get_distributor'] = ['d', 's', c.lib.func('s','PandaSystem_C_get_distributor_s_v','v')]
    c.ct['get_num_systems'] = ['d', 'p', c.lib.func('p','PandaSystem_C_get_num_systems_p_p','p')]
    c.ct['output'] = ['d', 'v', c.lib.func('v','PandaSystem_C_output_v_pp','pp')]
    c.ct['write'] = ['d', 'v', c.lib.func('v','PandaSystem_C_write_v_pp','pp')]
    c.ct['get_package_version_string'] = ['d', 's', c.lib.func('s','PandaSystem_C_get_package_version_string_s_v','v')]
    c.ct['get_major_version'] = ['d', 'i', c.lib.func('i','PandaSystem_C_get_major_version_i_v','v')]
    c.ct['heap_trim'] = ['d', 'B', c.lib.func('B','PandaSystem_C_heap_trim_B_pp','pp')]
    c.ct['get_class_type'] = ['d', 'i', c.lib.func('i','PandaSystem_C_get_class_type_i_v','v')]
    c.ct['get_package_host_url'] = ['d', 's', c.lib.func('s','PandaSystem_C_get_package_host_url_s_v','v')]
    c.ct['get_p3d_coreapi_version_string'] = ['d', 's', c.lib.func('s','PandaSystem_C_get_p3d_coreapi_version_string_s_v','v')]
    c.ct['get_system'] = ['d', 's', c.lib.func('s','PandaSystem_C_get_system_s_pp','pp')]
    c.ct['is_official_version'] = ['d', 'B', c.lib.func('B','PandaSystem_C_is_official_version_B_v','v')]
    c.ct['get_system_tag'] = ['d', 's', c.lib.func('s','PandaSystem_C_get_system_tag_s_ppp','ppp')]
    c.ct['get_git_commit'] = ['d', 's', c.lib.func('s','PandaSystem_C_get_git_commit_s_v','v')]
    c.ct['has_system'] = ['d', 'B', c.lib.func('B','PandaSystem_C_has_system_B_pp','pp')]
    c.ct['get_version_string'] = ['d', 's', c.lib.func('s','PandaSystem_C_get_version_string_s_v','v')]
    c.ct['init_type'] = ['d', 'v', c.lib.func('v','PandaSystem_C_init_type_v_v','v')]
    c.ct['get_build_date'] = ['d', 's', c.lib.func('s','PandaSystem_C_get_build_date_s_v','v')]
    c.ct['get_minor_version'] = ['d', 'i', c.lib.func('i','PandaSystem_C_get_minor_version_i_v','v')]
    c.ct['get_compiler'] = ['d', 's', c.lib.func('s','PandaSystem_C_get_compiler_s_v','v')]
    c.ct['get_memory_alignment'] = ['d', 'i', c.lib.func('i','PandaSystem_C_get_memory_alignment_i_v','v')]
    c.ct['get_sequence_version'] = ['d', 'i', c.lib.func('i','PandaSystem_C_get_sequence_version_i_v','v')]

    # variadic : return basic types or other C++ classes



    # c++ instance methods

    def __del__(self):
        self.__class__.destroy(self)

    def __getattr__(self, attr):
        return self.__call(attr)

PandaSystem.c.link(PandaSystem)



class NodePath(cxx.cplusplus):
    c = cxx.cstructs().register("NodePath", "upanda3d", """libupanda3d_c.so""")


    # ctor/dtor : classmethod type calls and return only raw pointer or void

    c.ct['ctor'] = {
        1 : ['s', 26, c.lib.func('p','NodePath_C_ctor_p_p','p')],
        2 : ['s', 26, c.lib.func('p','NodePath_C_ctor_p_pp','pp')],
        3 : ['s', 26, c.lib.func('p','NodePath_C_ctor_p_ppp','ppp')],
        0 : ['s', 26, c.lib.func('p','NodePath_C_ctor_p_v','')],
    }
    c.ct['ctor_1'] = {
        1 : ['s', 26, c.lib.func('p','NodePath_C_ctor_1_p_p','p')],
        2 : ['s', 26, c.lib.func('p','NodePath_C_ctor_1_p_pp','pp')],
        3 : ['s', 26, c.lib.func('p','NodePath_C_ctor_1_p_ppp','ppp')],
    }
    c.ct['ctor_2'] = ['s', 26, c.lib.func('p','NodePath_C_ctor_2_p_pp','pp')]
    c.ct['ctor_3'] = ['s', 26, c.lib.func('p','NodePath_C_ctor_3_p_pp','pp')]

    # fixed pos : return basic types or other C++ classes

    c.ct['fillin'] = ['d', 'v', c.lib.func('v','NodePath_C_fillin_v_ppp','ppp')]
    c.ct['get_stashed_ancestor'] = ['d', 26, c.lib.func('p','NodePath_C_get_stashed_ancestor_p_pp','pp')]
    c.ct['get_ancestor'] = ['d', 26, c.lib.func('p','NodePath_C_get_ancestor_p_pip','pip')]
    c.ct['compare_to_1'] = ['d', 'i', c.lib.func('i','NodePath_C_compare_to_1_i_pp','pp')]
    c.ct['force_recompute_bounds'] = ['d', 'v', c.lib.func('v','NodePath_C_force_recompute_bounds_v_p','p')]
    c.ct['detach_node_1'] = ['d', 'v', c.lib.func('v','NodePath_C_detach_node_1_v_pp','pp')]
    c.ct['set_audio_volume'] = ['d', 'v', c.lib.func('v','NodePath_C_set_audio_volume_v_pfi','pfi')]
    c.ct['verify_complete_1'] = ['d', 'B', c.lib.func('B','NodePath_C_verify_complete_1_B_pp','pp')]
    c.ct['get_bin_name'] = ['d', 's', c.lib.func('s','NodePath_C_get_bin_name_s_p','p')]
    c.ct['set_effect'] = ['d', 'v', c.lib.func('v','NodePath_C_set_effect_v_pp','pp')]
    c.ct['has_parent_1'] = ['d', 'B', c.lib.func('B','NodePath_C_has_parent_1_B_pp','pp')]
    c.ct['is_ancestor_of'] = ['d', 'B', c.lib.func('B','NodePath_C_is_ancestor_of_B_ppp','ppp')]
    c.ct['get_net_prev_transform'] = ['d', 4, c.lib.func('p','NodePath_C_get_net_prev_transform_p_pp','pp')]
    c.ct['get_net_state_1'] = ['d', 14, c.lib.func('p','NodePath_C_get_net_state_1_p_pp','pp')]
    c.ct['set_material_off_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_material_off_1_v_pi','pi')]
    c.ct['get_shader_input'] = ['d', 'p', c.lib.func('p','NodePath_C_get_shader_input_p_pp','pp')]
    c.ct['write_bam_file'] = ['d', 'B', c.lib.func('B','NodePath_C_write_bam_file_B_pp','pp')]
    c.ct['write_bounds'] = ['d', 'v', c.lib.func('v','NodePath_C_write_bounds_v_pp','pp')]
    c.ct['show_tight_bounds'] = ['d', 'v', c.lib.func('v','NodePath_C_show_tight_bounds_v_p','p')]
    c.ct['ls_1'] = ['d', 'v', c.lib.func('v','NodePath_C_ls_1_v_ppi','ppi')]
    c.ct['clear_effect'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_effect_v_pp','pp')]
    c.ct['set_shader'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_v_ppi','ppi')]
    c.ct['get_render_mode'] = ['d', 'p', c.lib.func('p','NodePath_C_get_render_mode_p_p','p')]
    c.ct['set_depth_offset_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_depth_offset_1_v_pii','pii')]
    c.ct['set_render_mode_perspective_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_render_mode_perspective_1_v_pBi','pBi')]
    c.ct['is_singleton'] = ['d', 'B', c.lib.func('B','NodePath_C_is_singleton_B_pp','pp')]
    c.ct['set_transparency'] = ['d', 'v', c.lib.func('v','NodePath_C_set_transparency_v_ppi','ppi')]
    c.ct['calc_tight_bounds'] = ['d', 'B', c.lib.func('B','NodePath_C_calc_tight_bounds_B_ppppp','ppppp')]
    c.ct['verify_complete'] = ['d', 'B', c.lib.func('B','NodePath_C_verify_complete_B_pp','pp')]
    c.ct['get_top_node'] = ['d', 22, c.lib.func('p','NodePath_C_get_top_node_p_pp','pp')]
    c.ct['clear_bin'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_bin_v_p','p')]
    c.ct['has_audio_volume'] = ['d', 'B', c.lib.func('B','NodePath_C_has_audio_volume_B_p','p')]
    c.ct['set_render_mode_filled'] = ['d', 'v', c.lib.func('v','NodePath_C_set_render_mode_filled_v_pi','pi')]
    c.ct['is_stashed'] = ['d', 'B', c.lib.func('B','NodePath_C_is_stashed_B_p','p')]
    c.ct['find_texture_stage'] = ['d', 'p', c.lib.func('p','NodePath_C_find_texture_stage_p_pp','pp')]
    c.ct['get_shader'] = ['d', 'p', c.lib.func('p','NodePath_C_get_shader_p_p','p')]
    c.ct['clear_mat'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_mat_v_p','p')]
    c.ct['reparent_to_1'] = ['d', 'v', c.lib.func('v','NodePath_C_reparent_to_1_v_ppip','ppip')]
    c.ct['set_billboard_point_eye_2'] = ['d', 'v', c.lib.func('v','NodePath_C_set_billboard_point_eye_2_v_pfB','pfB')]
    c.ct['reparent_to_2'] = ['d', 'v', c.lib.func('v','NodePath_C_reparent_to_2_v_ppip','ppip')]
    c.ct['has_light'] = ['d', 'B', c.lib.func('B','NodePath_C_has_light_B_pp','pp')]
    c.ct['get_net_state'] = ['d', 14, c.lib.func('p','NodePath_C_get_net_state_p_pp','pp')]
    c.ct['look_at_2'] = ['d', 'v', c.lib.func('v','NodePath_C_look_at_2_v_pppp','pppp')]
    c.ct['has_texcoord'] = ['d', 'B', c.lib.func('B','NodePath_C_has_texcoord_B_pp','pp')]
    c.ct['get_stashed_children_1'] = ['d', 24, c.lib.func('p','NodePath_C_get_stashed_children_1_p_pp','pp')]
    c.ct['has_attrib'] = ['d', 'B', c.lib.func('B','NodePath_C_has_attrib_B_pp','pp')]
    c.ct['premunge_scene_1'] = ['d', 'v', c.lib.func('v','NodePath_C_premunge_scene_1_v_pp','pp')]
    c.ct['get_sr'] = ['d', 'f', c.lib.func('f','NodePath_C_get_sr_f_p','p')]
    c.ct['find_all_textures_1'] = ['d', 7, c.lib.func('p','NodePath_C_find_all_textures_1_p_pp','pp')]
    c.ct['replace_material'] = ['d', 'v', c.lib.func('v','NodePath_C_replace_material_v_ppp','ppp')]
    c.ct['instance_to'] = ['d', 26, c.lib.func('p','NodePath_C_instance_to_p_ppip','ppip')]
    c.ct['get_sg'] = ['d', 'f', c.lib.func('f','NodePath_C_get_sg_f_p','p')]
    c.ct['any_path'] = ['d', 26, c.lib.func('p','NodePath_C_any_path_p_ppp','ppp')]
    c.ct['get_common_ancestor_1'] = ['d', 26, c.lib.func('p','NodePath_C_get_common_ancestor_1_p_ppp','ppp')]
    c.ct['clear_shader_input'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_shader_input_v_pp','pp')]
    c.ct['set_material_off'] = ['d', 'v', c.lib.func('v','NodePath_C_set_material_off_v_pi','pi')]
    c.ct['get_sb'] = ['d', 'f', c.lib.func('f','NodePath_C_get_sb_f_p','p')]
    c.ct['get_sa'] = ['d', 'f', c.lib.func('f','NodePath_C_get_sa_f_p','p')]
    c.ct['get_net_transform_1'] = ['d', 4, c.lib.func('p','NodePath_C_get_net_transform_1_p_pp','pp')]
    c.ct['premunge_scene'] = ['d', 'v', c.lib.func('v','NodePath_C_premunge_scene_v_pp','pp')]
    c.ct['get_error_type'] = ['d', 'p', c.lib.func('p','NodePath_C_get_error_type_p_p','p')]
    c.ct['set_render_mode'] = ['d', 'v', c.lib.func('v','NodePath_C_set_render_mode_v_ppfi','ppfi')]
    c.ct['get_num_children_1'] = ['d', 'i', c.lib.func('i','NodePath_C_get_num_children_1_i_pp','pp')]
    c.ct['get_relative_vector'] = ['d', 30, c.lib.func('p','NodePath_C_get_relative_vector_p_ppp','ppp')]
    c.ct['count_num_descendants'] = ['d', 'i', c.lib.func('i','NodePath_C_count_num_descendants_i_p','p')]
    c.ct['get_depth_test'] = ['d', 'B', c.lib.func('B','NodePath_C_get_depth_test_B_p','p')]
    c.ct['clear_scissor'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_scissor_v_p','p')]
    c.ct['is_ancestor_of_1'] = ['d', 'B', c.lib.func('B','NodePath_C_is_ancestor_of_1_B_ppp','ppp')]
    c.ct['find_texture'] = ['d', 8, c.lib.func('p','NodePath_C_find_texture_p_pp','pp')]
    c.ct['get_tex_gen'] = ['d', 'p', c.lib.func('p','NodePath_C_get_tex_gen_p_pp','pp')]
    c.ct['clear_antialias'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_antialias_v_p','p')]
    c.ct['not_found'] = ['d', 26, c.lib.func('p','NodePath_C_not_found_p_v','v')]
    c.ct['clear_material'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_material_v_p','p')]
    c.ct['project_texture'] = ['d', 'v', c.lib.func('v','NodePath_C_project_texture_v_pppp','pppp')]
    c.ct['compare_to'] = ['d', 'i', c.lib.func('i','NodePath_C_compare_to_i_pp','pp')]
    c.ct['get_top_node_1'] = ['d', 22, c.lib.func('p','NodePath_C_get_top_node_1_p_pp','pp')]
    c.ct['get_net_audio_volume'] = ['d', 'f', c.lib.func('f','NodePath_C_get_net_audio_volume_f_p','p')]
    c.ct['has_clip_plane'] = ['d', 'B', c.lib.func('B','NodePath_C_has_clip_plane_B_pp','pp')]
    c.ct['hide_bounds'] = ['d', 'v', c.lib.func('v','NodePath_C_hide_bounds_v_p','p')]
    c.ct['attach_new_node_5'] = ['d', 26, c.lib.func('p','NodePath_C_attach_new_node_5_p_ppip','ppip')]
    c.ct['attach_new_node_4'] = ['d', 26, c.lib.func('p','NodePath_C_attach_new_node_4_p_ppip','ppip')]
    c.ct['find_net_tag'] = ['d', 26, c.lib.func('p','NodePath_C_find_net_tag_p_pp','pp')]
    c.ct['set_two_sided'] = ['d', 'v', c.lib.func('v','NodePath_C_set_two_sided_v_pBi','pBi')]
    c.ct['attach_new_node_1'] = ['d', 26, c.lib.func('p','NodePath_C_attach_new_node_1_p_ppip','ppip')]
    c.ct['attach_new_node_3'] = ['d', 26, c.lib.func('p','NodePath_C_attach_new_node_3_p_ppip','ppip')]
    c.ct['attach_new_node_2'] = ['d', 26, c.lib.func('p','NodePath_C_attach_new_node_2_p_ppip','ppip')]
    c.ct['set_attrib'] = ['d', 'v', c.lib.func('v','NodePath_C_set_attrib_v_ppi','ppi')]
    c.ct['node'] = ['d', 22, c.lib.func('p','NodePath_C_node_p_p','p')]
    c.ct['get_num_nodes'] = ['d', 'i', c.lib.func('i','NodePath_C_get_num_nodes_i_pp','pp')]
    c.ct['clear_billboard'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_billboard_v_p','p')]
    c.ct['replace_texture'] = ['d', 'v', c.lib.func('v','NodePath_C_replace_texture_v_ppp','ppp')]
    c.ct['get_tex_projector_from'] = ['d', 26, c.lib.func('p','NodePath_C_get_tex_projector_from_p_pp','pp')]
    c.ct['flatten_medium'] = ['d', 'i', c.lib.func('i','NodePath_C_flatten_medium_i_p','p')]
    c.ct['show_bounds'] = ['d', 'v', c.lib.func('v','NodePath_C_show_bounds_v_p','p')]
    c.ct['set_collide_mask'] = ['d', 'v', c.lib.func('v','NodePath_C_set_collide_mask_v_pppp','pppp')]
    c.ct['get_stashed_ancestor_1'] = ['d', 26, c.lib.func('p','NodePath_C_get_stashed_ancestor_1_p_pp','pp')]
    c.ct['copy_to_2'] = ['d', 26, c.lib.func('p','NodePath_C_copy_to_2_p_ppip','ppip')]
    c.ct['copy_to_1'] = ['d', 26, c.lib.func('p','NodePath_C_copy_to_1_p_ppip','ppip')]
    c.ct['set_name'] = ['d', 'v', c.lib.func('v','NodePath_C_set_name_v_pp','pp')]
    c.ct['get_node'] = ['d', 22, c.lib.func('p','NodePath_C_get_node_p_pip','pip')]
    c.ct['stash_2'] = ['d', 'v', c.lib.func('v','NodePath_C_stash_2_v_pip','pip')]
    c.ct['stash_1'] = ['d', 'v', c.lib.func('v','NodePath_C_stash_1_v_pip','pip')]
    c.ct['set_material'] = ['d', 'v', c.lib.func('v','NodePath_C_set_material_v_ppi','ppi')]
    c.ct['unstash_all_1'] = ['d', 'v', c.lib.func('v','NodePath_C_unstash_all_1_v_pp','pp')]
    c.ct['unstash_all'] = ['d', 'v', c.lib.func('v','NodePath_C_unstash_all_v_pp','pp')]
    c.ct['has_logic_op'] = ['d', 'B', c.lib.func('B','NodePath_C_has_logic_op_B_p','p')]
    c.ct['write_bam_stream'] = ['d', 'B', c.lib.func('B','NodePath_C_write_bam_stream_B_pp','pp')]
    c.ct['get_bounds_1'] = ['d', 57, c.lib.func('p','NodePath_C_get_bounds_1_p_pp','pp')]
    c.ct['get_render_mode_thickness'] = ['d', 'f', c.lib.func('f','NodePath_C_get_render_mode_thickness_f_p','p')]
    c.ct['set_logic_op_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_logic_op_1_v_ppi','ppi')]
    c.ct['get_bin_draw_order'] = ['d', 'i', c.lib.func('i','NodePath_C_get_bin_draw_order_i_p','p')]
    c.ct['is_empty'] = ['d', 'B', c.lib.func('B','NodePath_C_is_empty_B_p','p')]
    c.ct['heads_up_2'] = ['d', 'v', c.lib.func('v','NodePath_C_heads_up_2_v_pppp','pppp')]
    c.ct['has_depth_offset'] = ['d', 'B', c.lib.func('B','NodePath_C_has_depth_offset_B_p','p')]
    c.ct['clear_transparency'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_transparency_v_p','p')]
    c.ct['set_color_off'] = ['d', 'v', c.lib.func('v','NodePath_C_set_color_off_v_pi','pi')]
    c.ct['write_datagram'] = ['d', 'v', c.lib.func('v','NodePath_C_write_datagram_v_ppp','ppp')]
    c.ct['get_name'] = ['d', 's', c.lib.func('s','NodePath_C_get_name_s_p','p')]
    c.ct['get_distance'] = ['d', 'f', c.lib.func('f','NodePath_C_get_distance_f_pp','pp')]
    c.ct['wrt_reparent_to_1'] = ['d', 'v', c.lib.func('v','NodePath_C_wrt_reparent_to_1_v_ppip','ppip')]
    c.ct['set_depth_test'] = ['d', 'v', c.lib.func('v','NodePath_C_set_depth_test_v_pBi','pBi')]
    c.ct['has_tex_projector'] = ['d', 'B', c.lib.func('B','NodePath_C_has_tex_projector_B_pp','pp')]
    c.ct['wrt_reparent_to_2'] = ['d', 'v', c.lib.func('v','NodePath_C_wrt_reparent_to_2_v_ppip','ppip')]
    c.ct['get_tag'] = ['d', 's', c.lib.func('s','NodePath_C_get_tag_s_pp','pp')]
    c.ct['wrt_reparent_to'] = ['d', 'v', c.lib.func('v','NodePath_C_wrt_reparent_to_v_ppip','ppip')]
    c.ct['set_billboard_axis_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_billboard_axis_1_v_pf','pf')]
    c.ct['get_relative_point'] = ['d', 38, c.lib.func('p','NodePath_C_get_relative_point_p_ppp','ppp')]
    c.ct['get_common_ancestor'] = ['d', 26, c.lib.func('p','NodePath_C_get_common_ancestor_p_ppp','ppp')]
    c.ct['has_parent'] = ['d', 'B', c.lib.func('B','NodePath_C_has_parent_B_pp','pp')]
    c.ct['get_parent_1'] = ['d', 26, c.lib.func('p','NodePath_C_get_parent_1_p_pp','pp')]
    c.ct['get_audio_volume'] = ['d', 'f', c.lib.func('f','NodePath_C_get_audio_volume_f_p','p')]
    c.ct['clear_depth_test'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_depth_test_v_p','p')]
    c.ct['clear_compass'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_compass_v_p','p')]
    c.ct['has_depth_test'] = ['d', 'B', c.lib.func('B','NodePath_C_has_depth_test_B_p','p')]
    c.ct['remove_node'] = ['d', 'v', c.lib.func('v','NodePath_C_remove_node_v_pp','pp')]
    c.ct['set_light'] = ['d', 'v', c.lib.func('v','NodePath_C_set_light_v_ppi','ppi')]
    c.ct['has_two_sided'] = ['d', 'B', c.lib.func('B','NodePath_C_has_two_sided_B_p','p')]
    c.ct['flatten_light'] = ['d', 'i', c.lib.func('i','NodePath_C_flatten_light_i_p','p')]
    c.ct['flatten_strong'] = ['d', 'i', c.lib.func('i','NodePath_C_flatten_strong_i_p','p')]
    c.ct['find_material'] = ['d', 'p', c.lib.func('p','NodePath_C_find_material_p_pp','pp')]
    c.ct['list_tags'] = ['d', 'v', c.lib.func('v','NodePath_C_list_tags_v_p','p')]
    c.ct['adjust_all_priorities'] = ['d', 'v', c.lib.func('v','NodePath_C_adjust_all_priorities_v_pi','pi')]
    c.ct['add_hash'] = ['d', 'p', c.lib.func('p','NodePath_C_add_hash_p_pp','pp')]
    c.ct['clear_attrib'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_attrib_v_pp','pp')]
    c.ct['get_child'] = ['d', 26, c.lib.func('p','NodePath_C_get_child_p_pip','pip')]
    c.ct['has_color'] = ['d', 'B', c.lib.func('B','NodePath_C_has_color_B_p','p')]
    c.ct['do_billboard_point_world'] = ['d', 'v', c.lib.func('v','NodePath_C_do_billboard_point_world_v_ppf','ppf')]
    c.ct['is_singleton_1'] = ['d', 'B', c.lib.func('B','NodePath_C_is_singleton_1_B_pp','pp')]
    c.ct['get_top'] = ['d', 26, c.lib.func('p','NodePath_C_get_top_p_pp','pp')]
    c.ct['get_child_1'] = ['d', 26, c.lib.func('p','NodePath_C_get_child_1_p_pip','pip')]
    c.ct['set_render_mode_filled_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_render_mode_filled_1_v_pi','pi')]
    c.ct['get_sort_1'] = ['d', 'i', c.lib.func('i','NodePath_C_get_sort_1_i_pp','pp')]
    c.ct['set_shader_input_43'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_43_v_pppi','pppi')]
    c.ct['has_scissor'] = ['d', 'B', c.lib.func('B','NodePath_C_has_scissor_B_p','p')]
    c.ct['set_shader_input_41'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_41_v_pppi','pppi')]
    c.ct['set_shader_input_40'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_40_v_pppi','pppi')]
    c.ct['is_same_graph'] = ['d', 'B', c.lib.func('B','NodePath_C_is_same_graph_B_ppp','ppp')]
    c.ct['set_shader_input_42'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_42_v_pppi','pppi')]
    c.ct['set_two_sided_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_two_sided_1_v_pBi','pBi')]
    c.ct['stash_to_2'] = ['d', 'v', c.lib.func('v','NodePath_C_stash_to_2_v_ppip','ppip')]
    c.ct['stash_to_1'] = ['d', 'v', c.lib.func('v','NodePath_C_stash_to_1_v_ppip','ppip')]
    c.ct['clear_tag'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_tag_v_pp','pp')]
    c.ct['set_render_mode_filled_wireframe_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_render_mode_filled_wireframe_1_v_ppi','ppi')]
    c.ct['set_shader_input_7'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_7_v_pppi','pppi')]
    c.ct['set_shader_input_6'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_6_v_pppi','pppi')]
    c.ct['set_shader_input_5'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_5_v_pppi','pppi')]
    c.ct['clear_color'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_color_v_p','p')]
    c.ct['removed'] = ['d', 26, c.lib.func('p','NodePath_C_removed_p_v','v')]
    c.ct['set_sb'] = ['d', 'v', c.lib.func('v','NodePath_C_set_sb_v_pf','pf')]
    c.ct['set_sa'] = ['d', 'v', c.lib.func('v','NodePath_C_set_sa_v_pf','pf')]
    c.ct['has_material'] = ['d', 'B', c.lib.func('B','NodePath_C_has_material_B_p','p')]
    c.ct['set_all_color_scale'] = ['d', 'v', c.lib.func('v','NodePath_C_set_all_color_scale_v_pfi','pfi')]
    c.ct['set_sg'] = ['d', 'v', c.lib.func('v','NodePath_C_set_sg_v_pf','pf')]
    c.ct['clear_depth_write'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_depth_write_v_p','p')]
    c.ct['set_all_color_scale_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_all_color_scale_1_v_pfi','pfi')]
    c.ct['calc_tight_bounds_1'] = ['d', 'B', c.lib.func('B','NodePath_C_calc_tight_bounds_1_B_ppppp','ppppp')]
    c.ct['calc_tight_bounds_2'] = ['d', 'B', c.lib.func('B','NodePath_C_calc_tight_bounds_2_B_ppppp','ppppp')]
    c.ct['set_shader_input_4'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_4_v_pppi','pppi')]
    c.ct['set_shader_input_8'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_8_v_pppi','pppi')]
    c.ct['set_shader_input_9'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_9_v_pppi','pppi')]
    c.ct['set_sr'] = ['d', 'v', c.lib.func('v','NodePath_C_set_sr_v_pf','pf')]
    c.ct['set_fog_off'] = ['d', 'v', c.lib.func('v','NodePath_C_set_fog_off_v_pi','pi')]
    c.ct['set_depth_offset'] = ['d', 'v', c.lib.func('v','NodePath_C_set_depth_offset_v_pii','pii')]
    c.ct['get_ancestor_1'] = ['d', 26, c.lib.func('p','NodePath_C_get_ancestor_1_p_pip','pip')]
    c.ct['set_fog_off_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_fog_off_1_v_pi','pi')]
    c.ct['set_render_mode_wireframe'] = ['d', 'v', c.lib.func('v','NodePath_C_set_render_mode_wireframe_v_pi','pi')]
    c.ct['get_material'] = ['d', 28, c.lib.func('p','NodePath_C_get_material_p_p','p')]
    c.ct['has_fog'] = ['d', 'B', c.lib.func('B','NodePath_C_has_fog_B_p','p')]
    c.ct['get_color_scale'] = ['d', 'p', c.lib.func('p','NodePath_C_get_color_scale_p_p','p')]
    c.ct['set_shader_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_1_v_ppi','ppi')]
    c.ct['get_num_nodes_1'] = ['d', 'i', c.lib.func('i','NodePath_C_get_num_nodes_1_i_pp','pp')]
    c.ct['find'] = ['d', 26, c.lib.func('p','NodePath_C_find_p_pp','pp')]
    c.ct['set_render_mode_wireframe_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_render_mode_wireframe_1_v_pi','pi')]
    c.ct['set_shader_off_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_off_1_v_pi','pi')]
    c.ct['set_audio_volume_off'] = ['d', 'v', c.lib.func('v','NodePath_C_set_audio_volume_off_v_pi','pi')]
    c.ct['set_billboard_point_world_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_billboard_point_world_1_v_pf','pf')]
    c.ct['set_shader_input_25'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_25_v_pppi','pppi')]
    c.ct['get_color'] = ['d', 'p', c.lib.func('p','NodePath_C_get_color_p_p','p')]
    c.ct['get_two_sided'] = ['d', 'B', c.lib.func('B','NodePath_C_get_two_sided_B_p','p')]
    c.ct['find_all_paths_to'] = ['d', 24, c.lib.func('p','NodePath_C_find_all_paths_to_p_pp','pp')]
    c.ct['clear_project_texture'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_project_texture_v_pp','pp')]
    c.ct['clear_fog'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_fog_v_p','p')]
    c.ct['get_net_tag'] = ['d', 's', c.lib.func('s','NodePath_C_get_net_tag_s_pp','pp')]
    c.ct['set_shader_input_20'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_20_v_pppi','pppi')]
    c.ct['remove_node_1'] = ['d', 'v', c.lib.func('v','NodePath_C_remove_node_1_v_pp','pp')]
    c.ct['attach_new_node'] = ['d', 26, c.lib.func('p','NodePath_C_attach_new_node_p_ppip','ppip')]
    c.ct['set_shader_input_21'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_21_v_pppi','pppi')]
    c.ct['get_top_1'] = ['d', 26, c.lib.func('p','NodePath_C_get_top_1_p_pp','pp')]
    c.ct['apply_texture_colors'] = ['d', 'v', c.lib.func('v','NodePath_C_apply_texture_colors_v_p','p')]
    c.ct['has_vertex_column'] = ['d', 'B', c.lib.func('B','NodePath_C_has_vertex_column_B_pp','pp')]
    c.ct['get_max_search_depth'] = ['d', 'i', c.lib.func('i','NodePath_C_get_max_search_depth_i_v','v')]
    c.ct['set_bin'] = ['d', 'v', c.lib.func('v','NodePath_C_set_bin_v_ppii','ppii')]
    c.ct['has_occluder'] = ['d', 'B', c.lib.func('B','NodePath_C_has_occluder_B_pp','pp')]
    c.ct['set_shader_input_22'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_22_v_pppi','pppi')]
    c.ct['clear_color_scale'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_color_scale_v_p','p')]
    c.ct['set_shader_input_23'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_23_v_pppi','pppi')]
    c.ct['has_billboard'] = ['d', 'B', c.lib.func('B','NodePath_C_has_billboard_B_p','p')]
    c.ct['set_shader_input_24'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_24_v_pppi','pppi')]
    c.ct['set_shader_input_26'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_26_v_pppi','pppi')]
    c.ct['set_shader_input_27'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_27_v_pppi','pppi')]
    c.ct['set_shader_input_28'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_28_v_pppi','pppi')]
    c.ct['set_shader_input_29'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_29_v_pppi','pppi')]
    c.ct['set_shader_input_34'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_34_v_pppi','pppi')]
    c.ct['do_billboard_axis'] = ['d', 'v', c.lib.func('v','NodePath_C_do_billboard_axis_v_ppf','ppf')]
    c.ct['set_attrib_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_attrib_1_v_ppi','ppi')]
    c.ct['set_shader_input_30'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_30_v_pppi','pppi')]
    c.ct['find_path_to'] = ['d', 26, c.lib.func('p','NodePath_C_find_path_to_p_pp','pp')]
    c.ct['set_shader_input_31'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_31_v_pppi','pppi')]
    c.ct['set_shader_input_32'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_32_v_pppi','pppi')]
    c.ct['set_render_mode_thickness_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_render_mode_thickness_1_v_pfi','pfi')]
    c.ct['set_render_mode_thickness'] = ['d', 'v', c.lib.func('v','NodePath_C_set_render_mode_thickness_v_pfi','pfi')]
    c.ct['has_transparency'] = ['d', 'B', c.lib.func('B','NodePath_C_has_transparency_B_p','p')]
    c.ct['init_type'] = ['d', 'v', c.lib.func('v','NodePath_C_init_type_v_v','v')]
    c.ct['get_bounds'] = ['d', 'p', c.lib.func('p','NodePath_C_get_bounds_p_pp','pp')]
    c.ct['get_collide_mask'] = ['d', 55, c.lib.func('p','NodePath_C_get_collide_mask_p_p','p')]
    c.ct['get_net_transform'] = ['d', 4, c.lib.func('p','NodePath_C_get_net_transform_p_pp','pp')]
    c.ct['set_shader_input_33'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_33_v_pppi','pppi')]
    c.ct['set_render_mode_filled_wireframe'] = ['d', 'v', c.lib.func('v','NodePath_C_set_render_mode_filled_wireframe_v_ppi','ppi')]
    c.ct['set_shader_input_35'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_35_v_pppi','pppi')]
    c.ct['set_color_2'] = ['d', 'v', c.lib.func('v','NodePath_C_set_color_2_v_pffffi','pffffi')]
    c.ct['has_antialias'] = ['d', 'B', c.lib.func('B','NodePath_C_has_antialias_B_p','p')]
    c.ct['clear_effects'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_effects_v_p','p')]
    c.ct['get_hidden_ancestor_1'] = ['d', 26, c.lib.func('p','NodePath_C_get_hidden_ancestor_1_p_ppp','ppp')]
    c.ct['get_num_children'] = ['d', 'i', c.lib.func('i','NodePath_C_get_num_children_i_pp','pp')]
    c.ct['set_shader_input_36'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_36_v_pppi','pppi')]
    c.ct['get_hidden_ancestor_2'] = ['d', 26, c.lib.func('p','NodePath_C_get_hidden_ancestor_2_p_ppp','ppp')]
    c.ct['decode_from_bam_stream_1'] = ['d', 26, c.lib.func('p','NodePath_C_decode_from_bam_stream_1_p_ppp','ppp')]
    c.ct['set_bin_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_bin_1_v_ppii','ppii')]
    c.ct['set_audio_volume_off_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_audio_volume_off_1_v_pi','pi')]
    c.ct['get_instance_count'] = ['d', 'i', c.lib.func('i','NodePath_C_get_instance_count_i_p','p')]
    c.ct['set_shader_input_37'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_37_v_pppi','pppi')]
    c.ct['get_children'] = ['d', 'p', c.lib.func('p','NodePath_C_get_children_p_pp','pp')]
    c.ct['set_shader_input_38'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_38_v_pppi','pppi')]
    c.ct['set_shader_input_39'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_39_v_pppi','pppi')]
    c.ct['set_shader_off'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_off_v_pi','pi')]
    c.ct['reverse_ls_1'] = ['d', 'i', c.lib.func('i','NodePath_C_reverse_ls_1_i_ppi','ppi')]
    c.ct['prepare_scene'] = ['d', 'v', c.lib.func('v','NodePath_C_prepare_scene_v_pp','pp')]
    c.ct['any_path_1'] = ['d', 26, c.lib.func('p','NodePath_C_any_path_1_p_ppp','ppp')]
    c.ct['set_alpha_scale_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_alpha_scale_1_v_pfi','pfi')]
    c.ct['set_clip_plane_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_clip_plane_1_v_ppi','ppi')]
    c.ct['set_render_mode_perspective'] = ['d', 'v', c.lib.func('v','NodePath_C_set_render_mode_perspective_v_pBi','pBi')]
    c.ct['get_effects'] = ['d', 'p', c.lib.func('p','NodePath_C_get_effects_p_p','p')]
    c.ct['clear_depth_offset'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_depth_offset_v_p','p')]
    c.ct['set_logic_op'] = ['d', 'v', c.lib.func('v','NodePath_C_set_logic_op_v_ppi','ppi')]
    c.ct['has_render_mode'] = ['d', 'B', c.lib.func('B','NodePath_C_has_render_mode_B_p','p')]
    c.ct['get_antialias'] = ['d', 'p', c.lib.func('p','NodePath_C_get_antialias_p_p','p')]
    c.ct['get_attrib'] = ['d', 'p', c.lib.func('p','NodePath_C_get_attrib_p_pp','pp')]
    c.ct['get_tex_projector_to'] = ['d', 26, c.lib.func('p','NodePath_C_get_tex_projector_to_p_pp','pp')]
    c.ct['clear_model_nodes'] = ['d', 'i', c.lib.func('i','NodePath_C_clear_model_nodes_i_p','p')]
    c.ct['get_tag_keys'] = ['d', 'v', c.lib.func('v','NodePath_C_get_tag_keys_v_pp','pp')]
    c.ct['set_shader_input_12'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_12_v_pppi','pppi')]
    c.ct['set_shader_input_13'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_13_v_pppi','pppi')]
    c.ct['set_fog_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_fog_1_v_ppi','ppi')]
    c.ct['get_effect'] = ['d', 'p', c.lib.func('p','NodePath_C_get_effect_p_pp','pp')]
    c.ct['set_shader_input_10'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_10_v_pppi','pppi')]
    c.ct['get_key'] = ['d', 'i', c.lib.func('i','NodePath_C_get_key_i_p','p')]
    c.ct['set_shader_input_11'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_11_v_pppi','pppi')]
    c.ct['set_shader_input_14'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_14_v_pppi','pppi')]
    c.ct['set_shader_input_15'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_15_v_pppi','pppi')]
    c.ct['set_shader_input_16'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_16_v_pppi','pppi')]
    c.ct['has_bin'] = ['d', 'B', c.lib.func('B','NodePath_C_has_bin_B_p','p')]
    c.ct['get_net_prev_transform_1'] = ['d', 4, c.lib.func('p','NodePath_C_get_net_prev_transform_1_p_pp','pp')]
    c.ct['set_depth_write'] = ['d', 'v', c.lib.func('v','NodePath_C_set_depth_write_v_pBi','pBi')]
    c.ct['is_same_graph_1'] = ['d', 'B', c.lib.func('B','NodePath_C_is_same_graph_1_B_ppp','ppp')]
    c.ct['do_billboard_point_eye'] = ['d', 'v', c.lib.func('v','NodePath_C_do_billboard_point_eye_v_ppf','ppf')]
    c.ct['get_parent'] = ['d', 26, c.lib.func('p','NodePath_C_get_parent_p_pp','pp')]
    c.ct['has_tag'] = ['d', 'B', c.lib.func('B','NodePath_C_has_tag_B_pp','pp')]
    c.ct['set_effects'] = ['d', 'v', c.lib.func('v','NodePath_C_set_effects_v_pp','pp')]
    c.ct['instance_under_node_2'] = ['d', 26, c.lib.func('p','NodePath_C_instance_under_node_2_p_pppip','pppip')]
    c.ct['instance_under_node_1'] = ['d', 26, c.lib.func('p','NodePath_C_instance_under_node_1_p_pppip','pppip')]
    c.ct['set_instance_count'] = ['d', 'v', c.lib.func('v','NodePath_C_set_instance_count_v_pi','pi')]
    c.ct['get_sort'] = ['d', 'i', c.lib.func('i','NodePath_C_get_sort_i_pp','pp')]
    c.ct['has_tex_transform'] = ['d', 'B', c.lib.func('B','NodePath_C_has_tex_transform_B_pp','pp')]
    c.ct['set_color_off_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_color_off_1_v_pi','pi')]
    c.ct['get_class_type'] = ['d', 'i', c.lib.func('i','NodePath_C_get_class_type_i_v','v')]
    c.ct['has_tex_gen'] = ['d', 'B', c.lib.func('B','NodePath_C_has_tex_gen_B_pp','pp')]
    c.ct['set_shader_input_17'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_17_v_pppi','pppi')]
    c.ct['set_shader_input_18'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_18_v_pppi','pppi')]
    c.ct['set_shader_input_19'] = ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_19_v_pppi','pppi')]
    c.ct['set_antialias'] = ['d', 'v', c.lib.func('v','NodePath_C_set_antialias_v_ppi','ppi')]
    c.ct['get_fog'] = ['d', 'p', c.lib.func('p','NodePath_C_get_fog_p_p','p')]
    c.ct['set_fog'] = ['d', 'v', c.lib.func('v','NodePath_C_set_fog_v_ppi','ppi')]
    c.ct['set_compass_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_compass_1_v_pp','pp')]
    c.ct['set_depth_test_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_depth_test_1_v_pBi','pBi')]
    c.ct['set_tex_projector_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_tex_projector_1_v_ppppi','ppppi')]
    c.ct['get_transparency'] = ['d', 'p', c.lib.func('p','NodePath_C_get_transparency_p_p','p')]
    c.ct['clear_logic_op'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_logic_op_v_p','p')]
    c.ct['set_color_scale_off'] = ['d', 'v', c.lib.func('v','NodePath_C_set_color_scale_off_v_pi','pi')]
    c.ct['set_tex_projector'] = ['d', 'v', c.lib.func('v','NodePath_C_set_tex_projector_v_ppppi','ppppi')]
    c.ct['set_light_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_light_1_v_ppi','ppi')]
    c.ct['clear'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_v_p','p')]
    c.ct['get_children_1'] = ['d', 24, c.lib.func('p','NodePath_C_get_children_1_p_pp','pp')]
    c.ct['set_color_scale_off_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_color_scale_off_1_v_pi','pi')]
    c.ct['set_texture_2'] = ['d', 'v', c.lib.func('v','NodePath_C_set_texture_2_v_pppi','pppi')]
    c.ct['set_texture_3'] = ['d', 'v', c.lib.func('v','NodePath_C_set_texture_3_v_pppi','pppi')]
    c.ct['get_depth_offset'] = ['d', 'i', c.lib.func('i','NodePath_C_get_depth_offset_i_p','p')]
    c.ct['set_compass'] = ['d', 'v', c.lib.func('v','NodePath_C_set_compass_v_pp','pp')]
    c.ct['set_transparency_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_transparency_1_v_ppi','ppi')]
    c.ct['find_texture_1'] = ['d', 8, c.lib.func('p','NodePath_C_find_texture_1_p_pp','pp')]
    c.ct['detach_node'] = ['d', 'v', c.lib.func('v','NodePath_C_detach_node_v_pp','pp')]
    c.ct['output'] = ['d', 'v', c.lib.func('v','NodePath_C_output_v_pp','pp')]
    c.ct['get_logic_op'] = ['d', 'p', c.lib.func('p','NodePath_C_get_logic_op_p_p','p')]
    c.ct['decode_from_bam_stream'] = ['d', 26, c.lib.func('p','NodePath_C_decode_from_bam_stream_p_ppp','ppp')]
    c.ct['get_render_mode_perspective'] = ['d', 'B', c.lib.func('B','NodePath_C_get_render_mode_perspective_B_p','p')]
    c.ct['instance_to_2'] = ['d', 26, c.lib.func('p','NodePath_C_instance_to_2_p_ppip','ppip')]
    c.ct['has_color_scale'] = ['d', 'B', c.lib.func('B','NodePath_C_has_color_scale_B_p','p')]
    c.ct['instance_to_1'] = ['d', 26, c.lib.func('p','NodePath_C_instance_to_1_p_ppip','ppip')]
    c.ct['set_render_mode_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_render_mode_1_v_ppfi','ppfi')]
    c.ct['fail'] = ['d', 26, c.lib.func('p','NodePath_C_fail_p_v','v')]
    c.ct['get_depth_write'] = ['d', 'B', c.lib.func('B','NodePath_C_get_depth_write_B_p','p')]
    c.ct['get_node_1'] = ['d', 22, c.lib.func('p','NodePath_C_get_node_1_p_pip','pip')]
    c.ct['clear_shader'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_shader_v_p','p')]
    c.ct['clear_render_mode'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_render_mode_v_p','p')]
    c.ct['set_material_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_material_1_v_ppi','ppi')]
    c.ct['encode_to_bam_stream_1'] = ['d', 'B', c.lib.func('B','NodePath_C_encode_to_bam_stream_1_B_ppp','ppp')]
    c.ct['copy_to'] = ['d', 26, c.lib.func('p','NodePath_C_copy_to_p_ppip','ppip')]
    c.ct['has_effect'] = ['d', 'B', c.lib.func('B','NodePath_C_has_effect_B_pp','pp')]
    c.ct['set_antialias_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_antialias_1_v_ppi','ppi')]
    c.ct['has_compass'] = ['d', 'B', c.lib.func('B','NodePath_C_has_compass_B_p','p')]
    c.ct['set_max_search_depth'] = ['d', 'v', c.lib.func('v','NodePath_C_set_max_search_depth_v_ii','ii')]
    c.ct['get_hidden_ancestor'] = ['d', 26, c.lib.func('p','NodePath_C_get_hidden_ancestor_p_ppp','ppp')]
    c.ct['set_clip_plane'] = ['d', 'v', c.lib.func('v','NodePath_C_set_clip_plane_v_ppi','ppi')]
    c.ct['set_tag'] = ['d', 'v', c.lib.func('v','NodePath_C_set_tag_v_ppp','ppp')]
    c.ct['get_stashed_children'] = ['d', 24, c.lib.func('p','NodePath_C_get_stashed_children_p_pp','pp')]
    c.ct['clear_two_sided'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_two_sided_v_p','p')]
    c.ct['stash_to'] = ['d', 'v', c.lib.func('v','NodePath_C_stash_to_v_ppip','ppip')]
    c.ct['set_depth_write_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_depth_write_1_v_pBi','pBi')]
    c.ct['stash'] = ['d', 'v', c.lib.func('v','NodePath_C_stash_v_pip','pip')]
    c.ct['unify_texture_stages'] = ['d', 'v', c.lib.func('v','NodePath_C_unify_texture_stages_v_pp','pp')]
    c.ct['unstash_1'] = ['d', 'v', c.lib.func('v','NodePath_C_unstash_1_v_pip','pip')]
    c.ct['unstash_2'] = ['d', 'v', c.lib.func('v','NodePath_C_unstash_2_v_pip','pip')]
    c.ct['has_fog_off'] = ['d', 'B', c.lib.func('B','NodePath_C_has_fog_off_B_p','p')]
    c.ct['unstash'] = ['d', 'v', c.lib.func('v','NodePath_C_unstash_v_pip','pip')]
    c.ct['set_collide_mask_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_collide_mask_1_v_pppp','pppp')]
    c.ct['set_collide_mask_2'] = ['d', 'v', c.lib.func('v','NodePath_C_set_collide_mask_2_v_pppp','pppp')]
    c.ct['is_hidden'] = ['d', 'B', c.lib.func('B','NodePath_C_is_hidden_B_pp','pp')]
    c.ct['reparent_to'] = ['d', 'v', c.lib.func('v','NodePath_C_reparent_to_v_ppip','ppip')]
    c.ct['has_depth_write'] = ['d', 'B', c.lib.func('B','NodePath_C_has_depth_write_B_p','p')]
    c.ct['is_hidden_1'] = ['d', 'B', c.lib.func('B','NodePath_C_is_hidden_1_B_pp','pp')]
    c.ct['set_audio_volume_1'] = ['d', 'v', c.lib.func('v','NodePath_C_set_audio_volume_1_v_pfi','pfi')]
    c.ct['set_occluder'] = ['d', 'v', c.lib.func('v','NodePath_C_set_occluder_v_pp','pp')]
    c.ct['has_mat'] = ['d', 'B', c.lib.func('B','NodePath_C_has_mat_B_p','p')]
    c.ct['instance_under_node'] = ['d', 26, c.lib.func('p','NodePath_C_instance_under_node_p_pppip','pppip')]
    c.ct['find_all_matches'] = ['d', 24, c.lib.func('p','NodePath_C_find_all_matches_p_pp','pp')]
    c.ct['clear_audio_volume'] = ['d', 'v', c.lib.func('v','NodePath_C_clear_audio_volume_v_p','p')]
    c.ct['set_alpha_scale'] = ['d', 'v', c.lib.func('v','NodePath_C_set_alpha_scale_v_pfi','pfi')]
    c.ct['has_net_tag'] = ['d', 'B', c.lib.func('B','NodePath_C_has_net_tag_B_pp','pp')]

    # variadic : return basic types or other C++ classes

    c.ct['set_shxy'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_shxy_v_pf','pf')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_shxy_v_ppf','ppf')],
    }
    c.ct['set_shader_input'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_v_pp','pp')],
        7 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_v_ppffffi','ppffffi')],
        7 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_v_ppiiiii','ppiiiii')],
        8 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_v_pppBBiii','pppBBiii')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_v_pppi','pppi')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_v_ppppi','ppppi')],
    }
    c.ct['set_clip_plane_off_1'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_clip_plane_off_1_v_pi','pi')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_clip_plane_off_1_v_ppi','ppi')],
    }
    c.ct['set_clip_plane_off'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_clip_plane_off_v_pi','pi')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_clip_plane_off_v_ppi','ppi')],
    }
    c.ct['set_shxz'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_shxz_v_pf','pf')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_shxz_v_ppf','ppf')],
    }
    c.ct['has_texture_off'] = {
        1 : ['d', 'B', c.lib.func('B','NodePath_C_has_texture_off_B_p','p')],
        2 : ['d', 'B', c.lib.func('B','NodePath_C_has_texture_off_B_pp','pp')],
    }
    c.ct['set_tex_scale'] = {
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_scale_v_ppf','ppf')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_scale_v_ppff','ppff')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_scale_v_ppfff','ppfff')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_scale_v_ppp','ppp')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_scale_v_pppf','pppf')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_scale_v_pppff','pppff')],
        6 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_scale_v_pppfff','pppfff')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_scale_v_pppp','pppp')],
    }
    c.ct['set_transform'] = {
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_transform_v_ppp','ppp')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_transform_v_pppp','pppp')],
    }
    c.ct['find_all_materials'] = {
        1 : ['d', 'p', c.lib.func('p','NodePath_C_find_all_materials_p_p','p')],
        2 : ['d', 27, c.lib.func('p','NodePath_C_find_all_materials_p_pp','pp')],
    }
    c.ct['set_billboard_axis'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_billboard_axis_v_pf','pf')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_billboard_axis_v_ppf','ppf')],
    }
    c.ct['get_quat'] = {
        1 : ['d', 'p', c.lib.func('p','NodePath_C_get_quat_p_p','p')],
        2 : ['d', 37, c.lib.func('p','NodePath_C_get_quat_p_pp','pp')],
    }
    c.ct['set_pos_hpr_scale'] = {
        10 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_hpr_scale_v_pfffffffff','pfffffffff')],
        11 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_hpr_scale_v_ppfffffffff','ppfffffffff')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_hpr_scale_v_pppp','pppp')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_hpr_scale_v_ppppp','ppppp')],
    }
    c.ct['get_shxz'] = {
        1 : ['d', 'f', c.lib.func('f','NodePath_C_get_shxz_f_p','p')],
        2 : ['d', 'f', c.lib.func('f','NodePath_C_get_shxz_f_pp','pp')],
    }
    c.ct['get_shxy'] = {
        1 : ['d', 'f', c.lib.func('f','NodePath_C_get_shxy_f_p','p')],
        2 : ['d', 'f', c.lib.func('f','NodePath_C_get_shxy_f_pp','pp')],
    }
    c.ct['set_texture_off'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_texture_off_v_pi','pi')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_texture_off_v_ppi','ppi')],
    }
    c.ct['hide'] = {
        1 : ['d', 'v', c.lib.func('v','NodePath_C_hide_v_p','p')],
        2 : ['d', 'v', c.lib.func('v','NodePath_C_hide_v_pp','pp')],
    }
    c.ct['set_billboard_point_eye_1'] = {
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_billboard_point_eye_1_v_pfB','pfB')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_billboard_point_eye_1_v_ppfB','ppfB')],
    }
    c.ct['get_sz'] = {
        1 : ['d', 'f', c.lib.func('f','NodePath_C_get_sz_f_p','p')],
        2 : ['d', 'f', c.lib.func('f','NodePath_C_get_sz_f_pp','pp')],
    }
    c.ct['get_sy'] = {
        1 : ['d', 'f', c.lib.func('f','NodePath_C_get_sy_f_p','p')],
        2 : ['d', 'f', c.lib.func('f','NodePath_C_get_sy_f_pp','pp')],
    }
    c.ct['get_sx'] = {
        1 : ['d', 'f', c.lib.func('f','NodePath_C_get_sx_f_p','p')],
        2 : ['d', 'f', c.lib.func('f','NodePath_C_get_sx_f_pp','pp')],
    }
    c.ct['get_state_1'] = {
        2 : ['d', 14, c.lib.func('p','NodePath_C_get_state_1_p_pp','pp')],
        3 : ['d', 14, c.lib.func('p','NodePath_C_get_state_1_p_ppp','ppp')],
    }
    c.ct['set_pos_quat'] = {
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_quat_v_ppp','ppp')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_quat_v_pppp','pppp')],
    }
    c.ct['look_at_1'] = {
        3 : ['d', 'v', c.lib.func('v','NodePath_C_look_at_1_v_ppp','ppp')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_look_at_1_v_pppp','pppp')],
    }
    c.ct['set_prev_transform_1'] = {
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_prev_transform_1_v_ppp','ppp')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_prev_transform_1_v_pppp','pppp')],
    }
    c.ct['set_pos_quat_scale'] = {
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_quat_scale_v_pppp','pppp')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_quat_scale_v_ppppp','ppppp')],
    }
    c.ct['look_at'] = {
        4 : ['d', 'v', c.lib.func('v','NodePath_C_look_at_v_pfff','pfff')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_look_at_v_ppfff','ppfff')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_look_at_v_ppp','ppp')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_look_at_v_pppp','pppp')],
    }
    c.ct['set_scissor'] = {
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_scissor_v_pffff','pffff')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_scissor_v_ppp','ppp')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_scissor_v_pppp','pppp')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_scissor_v_ppppp','ppppp')],
        6 : ['d', 'v', c.lib.func('v','NodePath_C_set_scissor_v_pppppp','pppppp')],
    }
    c.ct['set_state_1'] = {
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_state_1_v_ppp','ppp')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_state_1_v_pppp','pppp')],
    }
    c.ct['set_tex_hpr'] = {
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_hpr_v_ppfff','ppfff')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_hpr_v_ppp','ppp')],
        6 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_hpr_v_pppfff','pppfff')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_hpr_v_pppp','pppp')],
    }
    c.ct['set_pos_quat_scale_shear'] = {
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_quat_scale_shear_v_ppppp','ppppp')],
        6 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_quat_scale_shear_v_pppppp','pppppp')],
    }
    c.ct['set_shader_auto_1'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_auto_1_v_pi','pi')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_auto_1_v_ppi','ppi')],
    }
    c.ct['set_color_scale'] = {
        6 : ['d', 'v', c.lib.func('v','NodePath_C_set_color_scale_v_pffffi','pffffi')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_color_scale_v_ppi','ppi')],
    }
    c.ct['has_clip_plane_off'] = {
        1 : ['d', 'B', c.lib.func('B','NodePath_C_has_clip_plane_off_B_p','p')],
        2 : ['d', 'B', c.lib.func('B','NodePath_C_has_clip_plane_off_B_pp','pp')],
    }
    c.ct['clear_transform_1'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_clear_transform_1_v_pp','pp')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_clear_transform_1_v_ppp','ppp')],
    }
    c.ct['has_light_off'] = {
        1 : ['d', 'B', c.lib.func('B','NodePath_C_has_light_off_B_p','p')],
        2 : ['d', 'B', c.lib.func('B','NodePath_C_has_light_off_B_pp','pp')],
    }
    c.ct['get_scale'] = {
        1 : ['d', 34, c.lib.func('p','NodePath_C_get_scale_p_p','p')],
        2 : ['d', 34, c.lib.func('p','NodePath_C_get_scale_p_pp','pp')],
    }
    c.ct['get_tex_transform'] = {
        2 : ['d', 4, c.lib.func('p','NodePath_C_get_tex_transform_p_pp','pp')],
        3 : ['d', 4, c.lib.func('p','NodePath_C_get_tex_transform_p_ppp','ppp')],
    }
    c.ct['set_state'] = {
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_state_v_ppp','ppp')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_state_v_pppp','pppp')],
    }
    c.ct['compose_color_scale'] = {
        6 : ['d', 'v', c.lib.func('v','NodePath_C_compose_color_scale_v_pffffi','pffffi')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_compose_color_scale_v_ppi','ppi')],
    }
    c.ct['set_fluid_y'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_fluid_y_v_pf','pf')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_fluid_y_v_ppf','ppf')],
    }
    c.ct['set_fluid_x'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_fluid_x_v_pf','pf')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_fluid_x_v_ppf','ppf')],
    }
    c.ct['get_tex_offset'] = {
        2 : ['d', 36, c.lib.func('p','NodePath_C_get_tex_offset_p_pp','pp')],
        3 : ['d', 'p', c.lib.func('p','NodePath_C_get_tex_offset_p_ppp','ppp')],
    }
    c.ct['set_fluid_z'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_fluid_z_v_pf','pf')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_fluid_z_v_ppf','ppf')],
    }
    c.ct['get_pos'] = {
        1 : ['d', 'p', c.lib.func('p','NodePath_C_get_pos_p_p','p')],
        2 : ['d', 38, c.lib.func('p','NodePath_C_get_pos_p_pp','pp')],
    }
    c.ct['set_tex_offset'] = {
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_offset_v_ppff','ppff')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_offset_v_ppp','ppp')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_offset_v_pppff','pppff')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_offset_v_pppp','pppp')],
    }
    c.ct['set_shear'] = {
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_shear_v_pfff','pfff')],
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_shear_v_pp','pp')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_shear_v_ppfff','ppfff')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_shear_v_ppp','ppp')],
    }
    c.ct['heads_up_1'] = {
        3 : ['d', 'v', c.lib.func('v','NodePath_C_heads_up_1_v_ppp','ppp')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_heads_up_1_v_pppp','pppp')],
    }
    c.ct['ls'] = {
        1 : ['d', 'v', c.lib.func('v','NodePath_C_ls_v_p','p')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_ls_v_ppi','ppi')],
    }
    c.ct['get_mat'] = {
        1 : ['d', 'p', c.lib.func('p','NodePath_C_get_mat_p_p','p')],
        2 : ['d', 39, c.lib.func('p','NodePath_C_get_mat_p_pp','pp')],
    }
    c.ct['set_texture'] = {
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_texture_v_ppi','ppi')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_texture_v_pppi','pppi')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_texture_v_ppppi','ppppi')],
    }
    c.ct['set_x'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_x_v_pf','pf')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_x_v_ppf','ppf')],
    }
    c.ct['set_p'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_p_v_pf','pf')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_p_v_ppf','ppf')],
    }
    c.ct['set_r'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_r_v_pf','pf')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_r_v_ppf','ppf')],
    }
    c.ct['set_hpr'] = {
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_hpr_v_pfff','pfff')],
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_hpr_v_pp','pp')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_hpr_v_ppfff','ppfff')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_hpr_v_ppp','ppp')],
    }
    c.ct['set_y'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_y_v_pf','pf')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_y_v_ppf','ppf')],
    }
    c.ct['set_z'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_z_v_pf','pf')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_z_v_ppf','ppf')],
    }
    c.ct['set_h'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_h_v_pf','pf')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_h_v_ppf','ppf')],
    }
    c.ct['set_scale'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_scale_v_pf','pf')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_scale_v_pfff','pfff')],
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_scale_v_pp','pp')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_scale_v_ppf','ppf')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_scale_v_ppfff','ppfff')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_scale_v_ppp','ppp')],
    }
    c.ct['set_prev_transform'] = {
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_prev_transform_v_ppp','ppp')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_prev_transform_v_pppp','pppp')],
    }
    c.ct['set_hpr_scale'] = {
        7 : ['d', 'v', c.lib.func('v','NodePath_C_set_hpr_scale_v_pffffff','pffffff')],
        8 : ['d', 'v', c.lib.func('v','NodePath_C_set_hpr_scale_v_ppffffff','ppffffff')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_hpr_scale_v_ppp','ppp')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_hpr_scale_v_pppp','pppp')],
    }
    c.ct['get_tex_rotate'] = {
        2 : ['d', 'f', c.lib.func('f','NodePath_C_get_tex_rotate_f_pp','pp')],
        3 : ['d', 'f', c.lib.func('f','NodePath_C_get_tex_rotate_f_ppp','ppp')],
    }
    c.ct['set_quat_scale'] = {
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_quat_scale_v_ppp','ppp')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_quat_scale_v_pppp','pppp')],
    }
    c.ct['clear_tex_projector'] = {
        1 : ['d', 'v', c.lib.func('v','NodePath_C_clear_tex_projector_v_p','p')],
        2 : ['d', 'v', c.lib.func('v','NodePath_C_clear_tex_projector_v_pp','pp')],
    }
    c.ct['set_shader_input_1'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_1_v_pp','pp')],
        7 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_1_v_ppffffi','ppffffi')],
        7 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_1_v_ppiiiii','ppiiiii')],
        8 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_1_v_pppBBiii','pppBBiii')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_1_v_pppi','pppi')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_1_v_ppppi','ppppi')],
    }
    c.ct['set_shader_input_2'] = {
        7 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_2_v_ppffffi','ppffffi')],
        7 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_2_v_ppiiiii','ppiiiii')],
        8 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_2_v_pppBBiii','pppBBiii')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_2_v_pppi','pppi')],
    }
    c.ct['set_shader_input_3'] = {
        7 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_3_v_ppffffi','ppffffi')],
        7 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_3_v_ppiiiii','ppiiiii')],
        8 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_3_v_pppBBiii','pppBBiii')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_input_3_v_pppi','pppi')],
    }
    c.ct['set_sx'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_sx_v_pf','pf')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_sx_v_ppf','ppf')],
    }
    c.ct['set_fluid_pos'] = {
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_fluid_pos_v_pfff','pfff')],
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_fluid_pos_v_pp','pp')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_fluid_pos_v_ppfff','ppfff')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_fluid_pos_v_ppp','ppp')],
    }
    c.ct['set_quat'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_quat_v_pp','pp')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_quat_v_ppp','ppp')],
    }
    c.ct['set_pos_hpr_scale_shear'] = {
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_hpr_scale_shear_v_ppppp','ppppp')],
        6 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_hpr_scale_shear_v_pppppp','pppppp')],
    }
    c.ct['clear_clip_plane'] = {
        1 : ['d', 'v', c.lib.func('v','NodePath_C_clear_clip_plane_v_p','p')],
        2 : ['d', 'v', c.lib.func('v','NodePath_C_clear_clip_plane_v_pp','pp')],
    }
    c.ct['get_prev_transform_1'] = {
        2 : ['d', 4, c.lib.func('p','NodePath_C_get_prev_transform_1_p_pp','pp')],
        3 : ['d', 4, c.lib.func('p','NodePath_C_get_prev_transform_1_p_ppp','ppp')],
    }
    c.ct['clear_light'] = {
        1 : ['d', 'v', c.lib.func('v','NodePath_C_clear_light_v_p','p')],
        2 : ['d', 'v', c.lib.func('v','NodePath_C_clear_light_v_pp','pp')],
    }
    c.ct['compose_color_scale_1'] = {
        6 : ['d', 'v', c.lib.func('v','NodePath_C_compose_color_scale_1_v_pffffi','pffffi')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_compose_color_scale_1_v_ppi','ppi')],
    }
    c.ct['set_color'] = {
        6 : ['d', 'v', c.lib.func('v','NodePath_C_set_color_v_pffffi','pffffi')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_color_v_ppi','ppi')],
    }
    c.ct['get_tex_scale'] = {
        2 : ['d', 36, c.lib.func('p','NodePath_C_get_tex_scale_p_pp','pp')],
        3 : ['d', 36, c.lib.func('p','NodePath_C_get_tex_scale_p_ppp','ppp')],
    }
    c.ct['get_tex_hpr'] = {
        2 : ['d', 34, c.lib.func('p','NodePath_C_get_tex_hpr_p_pp','pp')],
        3 : ['d', 34, c.lib.func('p','NodePath_C_get_tex_hpr_p_ppp','ppp')],
    }
    c.ct['get_texture'] = {
        1 : ['d', 'p', c.lib.func('p','NodePath_C_get_texture_p_p','p')],
        2 : ['d', 8, c.lib.func('p','NodePath_C_get_texture_p_pp','pp')],
    }
    c.ct['get_hpr'] = {
        1 : ['d', 'p', c.lib.func('p','NodePath_C_get_hpr_p_p','p')],
        2 : ['d', 34, c.lib.func('p','NodePath_C_get_hpr_p_pp','pp')],
    }
    c.ct['get_state'] = {
        2 : ['d', 14, c.lib.func('p','NodePath_C_get_state_p_pp','pp')],
        3 : ['d', 'p', c.lib.func('p','NodePath_C_get_state_p_ppp','ppp')],
    }
    c.ct['set_light_off_1'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_light_off_1_v_pi','pi')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_light_off_1_v_ppi','ppi')],
    }
    c.ct['get_texture_sampler'] = {
        1 : ['d', 'p', c.lib.func('p','NodePath_C_get_texture_sampler_p_p','p')],
        2 : ['d', 13, c.lib.func('p','NodePath_C_get_texture_sampler_p_pp','pp')],
    }
    c.ct['get_transform'] = {
        2 : ['d', 4, c.lib.func('p','NodePath_C_get_transform_p_pp','pp')],
        3 : ['d', 'p', c.lib.func('p','NodePath_C_get_transform_p_ppp','ppp')],
    }
    c.ct['get_prev_transform'] = {
        2 : ['d', 4, c.lib.func('p','NodePath_C_get_prev_transform_p_pp','pp')],
        3 : ['d', 4, c.lib.func('p','NodePath_C_get_prev_transform_p_ppp','ppp')],
    }
    c.ct['find_all_texture_stages'] = {
        1 : ['d', 'p', c.lib.func('p','NodePath_C_find_all_texture_stages_p_p','p')],
        2 : ['d', 5, c.lib.func('p','NodePath_C_find_all_texture_stages_p_pp','pp')],
    }
    c.ct['get_shyz'] = {
        1 : ['d', 'f', c.lib.func('f','NodePath_C_get_shyz_f_p','p')],
        2 : ['d', 'f', c.lib.func('f','NodePath_C_get_shyz_f_pp','pp')],
    }
    c.ct['clear_tex_transform'] = {
        1 : ['d', 'v', c.lib.func('v','NodePath_C_clear_tex_transform_v_p','p')],
        2 : ['d', 'v', c.lib.func('v','NodePath_C_clear_tex_transform_v_pp','pp')],
    }
    c.ct['set_color_1'] = {
        6 : ['d', 'v', c.lib.func('v','NodePath_C_set_color_1_v_pffffi','pffffi')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_color_1_v_ppi','ppi')],
    }
    c.ct['get_tex_pos'] = {
        2 : ['d', 34, c.lib.func('p','NodePath_C_get_tex_pos_p_pp','pp')],
        3 : ['d', 34, c.lib.func('p','NodePath_C_get_tex_pos_p_ppp','ppp')],
    }
    c.ct['get_h'] = {
        1 : ['d', 'f', c.lib.func('f','NodePath_C_get_h_f_p','p')],
        2 : ['d', 'f', c.lib.func('f','NodePath_C_get_h_f_pp','pp')],
    }
    c.ct['clear_transform'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_clear_transform_v_pp','pp')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_clear_transform_v_ppp','ppp')],
    }
    c.ct['get_pos_delta'] = {
        1 : ['d', 'p', c.lib.func('p','NodePath_C_get_pos_delta_p_p','p')],
        2 : ['d', 30, c.lib.func('p','NodePath_C_get_pos_delta_p_pp','pp')],
    }
    c.ct['get_x'] = {
        1 : ['d', 'f', c.lib.func('f','NodePath_C_get_x_f_p','p')],
        2 : ['d', 'f', c.lib.func('f','NodePath_C_get_x_f_pp','pp')],
    }
    c.ct['get_y'] = {
        1 : ['d', 'f', c.lib.func('f','NodePath_C_get_y_f_p','p')],
        2 : ['d', 'f', c.lib.func('f','NodePath_C_get_y_f_pp','pp')],
    }
    c.ct['set_light_off'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_light_off_v_pi','pi')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_light_off_v_ppi','ppi')],
    }
    c.ct['get_z'] = {
        1 : ['d', 'f', c.lib.func('f','NodePath_C_get_z_f_p','p')],
        2 : ['d', 'f', c.lib.func('f','NodePath_C_get_z_f_pp','pp')],
    }
    c.ct['set_pos'] = {
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_v_pfff','pfff')],
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_v_pp','pp')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_v_ppfff','ppfff')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_v_ppp','ppp')],
    }
    c.ct['find_all_texcoords'] = {
        1 : ['d', 41, c.lib.func('p','NodePath_C_find_all_texcoords_p_p','p')],
        2 : ['d', 41, c.lib.func('p','NodePath_C_find_all_texcoords_p_pp','pp')],
    }
    c.ct['get_p'] = {
        1 : ['d', 'f', c.lib.func('f','NodePath_C_get_p_f_p','p')],
        2 : ['d', 'f', c.lib.func('f','NodePath_C_get_p_f_pp','pp')],
    }
    c.ct['get_r'] = {
        1 : ['d', 'f', c.lib.func('f','NodePath_C_get_r_f_p','p')],
        2 : ['d', 'f', c.lib.func('f','NodePath_C_get_r_f_pp','pp')],
    }
    c.ct['has_texture'] = {
        1 : ['d', 'B', c.lib.func('B','NodePath_C_has_texture_B_p','p')],
        2 : ['d', 'B', c.lib.func('B','NodePath_C_has_texture_B_pp','pp')],
    }
    c.ct['clear_texture'] = {
        1 : ['d', 'v', c.lib.func('v','NodePath_C_clear_texture_v_p','p')],
        2 : ['d', 'v', c.lib.func('v','NodePath_C_clear_texture_v_pp','pp')],
    }
    c.ct['set_mat'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_mat_v_pp','pp')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_mat_v_ppp','ppp')],
    }
    c.ct['encode_to_bam_stream'] = {
        3 : ['d', 'B', c.lib.func('B','NodePath_C_encode_to_bam_stream_B_ppp','ppp')],
        1 : ['d', 'p', c.lib.func('p','NodePath_C_encode_to_bam_stream_p_p','p')],
    }
    c.ct['set_shyz'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_shyz_v_pf','pf')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_shyz_v_ppf','ppf')],
    }
    c.ct['set_sy'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_sy_v_pf','pf')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_sy_v_ppf','ppf')],
    }
    c.ct['set_shader_auto'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_auto_v_pi','pi')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_shader_auto_v_ppi','ppi')],
    }
    c.ct['set_sz'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_sz_v_pf','pf')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_sz_v_ppf','ppf')],
    }
    c.ct['set_tex_gen_1'] = {
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_gen_1_v_pppi','pppi')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_gen_1_v_ppppi','ppppi')],
    }
    c.ct['set_tex_gen'] = {
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_gen_v_pppi','pppi')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_gen_v_ppppi','ppppi')],
    }
    c.ct['get_shear'] = {
        1 : ['d', 34, c.lib.func('p','NodePath_C_get_shear_p_p','p')],
        2 : ['d', 34, c.lib.func('p','NodePath_C_get_shear_p_pp','pp')],
    }
    c.ct['clear_occluder'] = {
        1 : ['d', 'v', c.lib.func('v','NodePath_C_clear_occluder_v_p','p')],
        2 : ['d', 'v', c.lib.func('v','NodePath_C_clear_occluder_v_pp','pp')],
    }
    c.ct['set_tex_pos'] = {
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_pos_v_ppfff','ppfff')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_pos_v_ppp','ppp')],
        6 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_pos_v_pppfff','pppfff')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_pos_v_pppp','pppp')],
    }
    c.ct['set_tex_scale_1'] = {
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_scale_1_v_ppp','ppp')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_scale_1_v_pppp','pppp')],
    }
    c.ct['set_color_scale_1'] = {
        6 : ['d', 'v', c.lib.func('v','NodePath_C_set_color_scale_1_v_pffffi','pffffi')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_color_scale_1_v_ppi','ppi')],
    }
    c.ct['get_tex_scale_3d'] = {
        2 : ['d', 34, c.lib.func('p','NodePath_C_get_tex_scale_3d_p_pp','pp')],
        3 : ['d', 34, c.lib.func('p','NodePath_C_get_tex_scale_3d_p_ppp','ppp')],
    }
    c.ct['set_tex_transform'] = {
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_transform_v_ppp','ppp')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_transform_v_pppp','pppp')],
    }
    c.ct['set_texture_1'] = {
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_texture_1_v_ppi','ppi')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_texture_1_v_pppi','pppi')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_set_texture_1_v_ppppi','ppppi')],
    }
    c.ct['set_texture_off_1'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_texture_off_1_v_pi','pi')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_texture_off_1_v_ppi','ppi')],
    }
    c.ct['set_transform_1'] = {
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_transform_1_v_ppp','ppp')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_transform_1_v_pppp','pppp')],
    }
    c.ct['show_through'] = {
        1 : ['d', 'v', c.lib.func('v','NodePath_C_show_through_v_p','p')],
        2 : ['d', 'v', c.lib.func('v','NodePath_C_show_through_v_pp','pp')],
    }
    c.ct['set_pos_hpr'] = {
        7 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_hpr_v_pffffff','pffffff')],
        8 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_hpr_v_ppffffff','ppffffff')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_hpr_v_ppp','ppp')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_pos_hpr_v_pppp','pppp')],
    }
    c.ct['set_billboard_point_eye'] = {
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_billboard_point_eye_v_pfB','pfB')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_billboard_point_eye_v_ppfB','ppfB')],
    }
    c.ct['heads_up'] = {
        4 : ['d', 'v', c.lib.func('v','NodePath_C_heads_up_v_pfff','pfff')],
        5 : ['d', 'v', c.lib.func('v','NodePath_C_heads_up_v_ppfff','ppfff')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_heads_up_v_ppp','ppp')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_heads_up_v_pppp','pppp')],
    }
    c.ct['set_tex_rotate'] = {
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_rotate_v_ppf','ppf')],
        4 : ['d', 'v', c.lib.func('v','NodePath_C_set_tex_rotate_v_pppf','pppf')],
    }
    c.ct['find_all_textures'] = {
        1 : ['d', 'p', c.lib.func('p','NodePath_C_find_all_textures_p_p','p')],
        2 : ['d', 7, c.lib.func('p','NodePath_C_find_all_textures_p_pp','pp')],
    }
    c.ct['show'] = {
        1 : ['d', 'v', c.lib.func('v','NodePath_C_show_v_p','p')],
        2 : ['d', 'v', c.lib.func('v','NodePath_C_show_v_pp','pp')],
    }
    c.ct['clear_tex_gen'] = {
        1 : ['d', 'v', c.lib.func('v','NodePath_C_clear_tex_gen_v_p','p')],
        2 : ['d', 'v', c.lib.func('v','NodePath_C_clear_tex_gen_v_pp','pp')],
    }
    c.ct['find_all_vertex_columns'] = {
        1 : ['d', 'p', c.lib.func('p','NodePath_C_find_all_vertex_columns_p_p','p')],
        2 : ['d', 41, c.lib.func('p','NodePath_C_find_all_vertex_columns_p_pp','pp')],
    }
    c.ct['set_billboard_point_world'] = {
        2 : ['d', 'v', c.lib.func('v','NodePath_C_set_billboard_point_world_v_pf','pf')],
        3 : ['d', 'v', c.lib.func('v','NodePath_C_set_billboard_point_world_v_ppf','ppf')],
    }
    c.ct['reverse_ls'] = {
        3 : ['d', 'i', c.lib.func('i','NodePath_C_reverse_ls_i_ppi','ppi')],
        1 : ['d', 'v', c.lib.func('v','NodePath_C_reverse_ls_v_p','p')],
    }
    c.ct['get_transform_1'] = {
        2 : ['d', 4, c.lib.func('p','NodePath_C_get_transform_1_p_pp','pp')],
        3 : ['d', 4, c.lib.func('p','NodePath_C_get_transform_1_p_ppp','ppp')],
    }


    # c++ instance methods

    def __del__(self):
        self.__class__.destroy(self)

    def __getattr__(self, attr):
        return self.__call(attr)

NodePath.c.link(NodePath)



class ConfigPage(cxx.cplusplus):
    c = cxx.cstructs().register("ConfigPage", "upanda3d", """libupanda3d_c.so""")


    # ctor/dtor : classmethod type calls and return only raw pointer or void


    # fixed pos : return basic types or other C++ classes

    c.ct['make_declaration_1'] = ['d', 54, c.lib.func('p','ConfigPage_C_make_declaration_1_p_ppp','ppp')]
    c.ct['modify_declaration'] = ['d', 54, c.lib.func('p','ConfigPage_C_modify_declaration_p_pp','pp')]
    c.ct['delete_declaration'] = ['d', 'B', c.lib.func('B','ConfigPage_C_delete_declaration_B_pp','pp')]
    c.ct['read_prc'] = ['d', 'B', c.lib.func('B','ConfigPage_C_read_prc_B_pp','pp')]
    c.ct['get_local_page'] = ['d', 53, c.lib.func('p','ConfigPage_C_get_local_page_p_v','v')]
    c.ct['get_signature'] = ['d', 's', c.lib.func('s','ConfigPage_C_get_signature_s_p','p')]
    c.ct['get_string_value'] = ['d', 's', c.lib.func('s','ConfigPage_C_get_string_value_s_pp','pp')]
    c.ct['get_default_page'] = ['d', 'p', c.lib.func('p','ConfigPage_C_get_default_page_p_v','v')]
    c.ct['get_trust_level'] = ['d', 'i', c.lib.func('i','ConfigPage_C_get_trust_level_i_p','p')]
    c.ct['output_brief_signature'] = ['d', 'v', c.lib.func('v','ConfigPage_C_output_brief_signature_v_pp','pp')]
    c.ct['output'] = ['d', 'v', c.lib.func('v','ConfigPage_C_output_v_pp','pp')]
    c.ct['set_trust_level'] = ['d', 'v', c.lib.func('v','ConfigPage_C_set_trust_level_v_pi','pi')]
    c.ct['write'] = ['d', 'v', c.lib.func('v','ConfigPage_C_write_v_pp','pp')]
    c.ct['get_num_declarations'] = ['d', 'p', c.lib.func('p','ConfigPage_C_get_num_declarations_p_p','p')]
    c.ct['set_sort'] = ['d', 'v', c.lib.func('v','ConfigPage_C_set_sort_v_pi','pi')]
    c.ct['make_declaration'] = ['d', 'p', c.lib.func('p','ConfigPage_C_make_declaration_p_ppp','ppp')]
    c.ct['is_implicit'] = ['d', 'B', c.lib.func('B','ConfigPage_C_is_implicit_B_p','p')]
    c.ct['read_encrypted_prc'] = ['d', 'B', c.lib.func('B','ConfigPage_C_read_encrypted_prc_B_ppp','ppp')]
    c.ct['clear'] = ['d', 'v', c.lib.func('v','ConfigPage_C_clear_v_p','p')]
    c.ct['is_variable_used'] = ['d', 'B', c.lib.func('B','ConfigPage_C_is_variable_used_B_pp','pp')]
    c.ct['is_special'] = ['d', 'B', c.lib.func('B','ConfigPage_C_is_special_B_p','p')]
    c.ct['get_variable_name'] = ['d', 's', c.lib.func('s','ConfigPage_C_get_variable_name_s_pp','pp')]
    c.ct['get_sort'] = ['d', 'i', c.lib.func('i','ConfigPage_C_get_sort_i_p','p')]
    c.ct['get_name'] = ['d', 's', c.lib.func('s','ConfigPage_C_get_name_s_p','p')]
    c.ct['get_declaration'] = ['d', 54, c.lib.func('p','ConfigPage_C_get_declaration_p_pp','pp')]
    c.ct['get_page_seq'] = ['d', 'i', c.lib.func('i','ConfigPage_C_get_page_seq_i_p','p')]

    # variadic : return basic types or other C++ classes



    # c++ instance methods

    def __del__(self):
        self.__class__.destroy(self)

    def __getattr__(self, attr):
        return self.__call(attr)

ConfigPage.c.link(ConfigPage)



class Camera(cxx.cplusplus):
    c = cxx.cstructs().register("Camera", "upanda3d", """libupanda3d_c.so""")


    # ctor/dtor : classmethod type calls and return only raw pointer or void

    c.ct['ctor_1'] = ['s', 56, c.lib.func('p','Camera_C_ctor_1_p_pp','pp')]
    c.ct['ctor'] = {
        1 : ['s', 'p', c.lib.func('p','Camera_C_ctor_p_p','p')],
        2 : ['s', 56, c.lib.func('p','Camera_C_ctor_p_pp','pp')],
    }

    # fixed pos : return basic types or other C++ classes

    c.ct['get_display_region'] = ['d', 'p', c.lib.func('p','Camera_C_get_display_region_p_pp','pp')]
    c.ct['clear_tag_states'] = ['d', 'v', c.lib.func('v','Camera_C_clear_tag_states_v_p','p')]
    c.ct['safe_to_flatten'] = ['d', 'B', c.lib.func('B','Camera_C_safe_to_flatten_B_p','p')]
    c.ct['make_copy'] = ['d', 'p', c.lib.func('p','Camera_C_make_copy_p_p','p')]
    c.ct['get_cull_center'] = ['d', 26, c.lib.func('p','Camera_C_get_cull_center_p_p','p')]
    c.ct['list_aux_scene_data'] = ['d', 'v', c.lib.func('v','Camera_C_list_aux_scene_data_v_pp','pp')]
    c.ct['set_tag_state_key'] = ['d', 'v', c.lib.func('v','Camera_C_set_tag_state_key_v_pp','pp')]
    c.ct['clear_tag_state'] = ['d', 'v', c.lib.func('v','Camera_C_clear_tag_state_v_pp','pp')]
    c.ct['get_scene'] = ['d', 'p', c.lib.func('p','Camera_C_get_scene_p_p','p')]
    c.ct['clear_aux_scene_data'] = ['d', 'B', c.lib.func('B','Camera_C_clear_aux_scene_data_B_pp','pp')]
    c.ct['set_camera_mask'] = ['d', 'v', c.lib.func('v','Camera_C_set_camera_mask_v_pp','pp')]
    c.ct['get_camera_mask'] = ['d', 'p', c.lib.func('p','Camera_C_get_camera_mask_p_p','p')]
    c.ct['get_num_display_regions'] = ['d', 'p', c.lib.func('p','Camera_C_get_num_display_regions_p_p','p')]
    c.ct['register_with_read_factory'] = ['d', 'v', c.lib.func('v','Camera_C_register_with_read_factory_v_v','v')]
    c.ct['cleanup_aux_scene_data'] = ['d', 'i', c.lib.func('i','Camera_C_cleanup_aux_scene_data_i_pp','pp')]
    c.ct['set_aux_scene_data'] = ['d', 'v', c.lib.func('v','Camera_C_set_aux_scene_data_v_ppp','ppp')]
    c.ct['set_scene'] = ['d', 'v', c.lib.func('v','Camera_C_set_scene_v_pp','pp')]
    c.ct['set_cull_bounds'] = ['d', 'v', c.lib.func('v','Camera_C_set_cull_bounds_v_pp','pp')]
    c.ct['set_tag_state'] = ['d', 'v', c.lib.func('v','Camera_C_set_tag_state_v_ppp','ppp')]
    c.ct['set_lod_scale'] = ['d', 'v', c.lib.func('v','Camera_C_set_lod_scale_v_pf','pf')]
    c.ct['set_lod_center'] = ['d', 'v', c.lib.func('v','Camera_C_set_lod_center_v_pp','pp')]
    c.ct['get_class_type'] = ['d', 'i', c.lib.func('i','Camera_C_get_class_type_i_v','v')]
    c.ct['get_aux_scene_data'] = ['d', 'p', c.lib.func('p','Camera_C_get_aux_scene_data_p_pp','pp')]
    c.ct['force_init_type'] = ['d', 'i', c.lib.func('i','Camera_C_force_init_type_i_p','p')]
    c.ct['safe_to_transform'] = ['d', 'B', c.lib.func('B','Camera_C_safe_to_transform_B_p','p')]
    c.ct['init_type'] = ['d', 'v', c.lib.func('v','Camera_C_init_type_v_v','v')]
    c.ct['set_cull_center'] = ['d', 'v', c.lib.func('v','Camera_C_set_cull_center_v_pp','pp')]
    c.ct['set_initial_state'] = ['d', 'v', c.lib.func('v','Camera_C_set_initial_state_v_pp','pp')]
    c.ct['get_tag_state_key'] = ['d', 's', c.lib.func('s','Camera_C_get_tag_state_key_s_p','p')]
    c.ct['get_cull_bounds'] = ['d', 57, c.lib.func('p','Camera_C_get_cull_bounds_p_p','p')]
    c.ct['get_tag_state'] = ['d', 14, c.lib.func('p','Camera_C_get_tag_state_p_pp','pp')]
    c.ct['cleanup_aux_scene_data_1'] = ['d', 'i', c.lib.func('i','Camera_C_cleanup_aux_scene_data_1_i_pp','pp')]
    c.ct['get_initial_state'] = ['d', 14, c.lib.func('p','Camera_C_get_initial_state_p_p','p')]
    c.ct['write_datagram'] = ['d', 'v', c.lib.func('v','Camera_C_write_datagram_v_ppp','ppp')]
    c.ct['get_lod_scale'] = ['d', 'f', c.lib.func('f','Camera_C_get_lod_scale_f_p','p')]
    c.ct['set_active'] = ['d', 'v', c.lib.func('v','Camera_C_set_active_v_pB','pB')]
    c.ct['get_lod_center'] = ['d', 26, c.lib.func('p','Camera_C_get_lod_center_p_p','p')]
    c.ct['is_active'] = ['d', 'B', c.lib.func('B','Camera_C_is_active_B_p','p')]
    c.ct['has_tag_state'] = ['d', 'B', c.lib.func('B','Camera_C_has_tag_state_B_pp','pp')]
    c.ct['get_type'] = ['d', 'i', c.lib.func('i','Camera_C_get_type_i_p','p')]

    # variadic : return basic types or other C++ classes



    # c++ instance methods

    def __del__(self):
        self.__class__.destroy(self)

    def __getattr__(self, attr):
        return self.__call(attr)

Camera.c.link(Camera)



class Filename(cxx.cplusplus):
    c = cxx.cstructs().register("Filename", "upanda3d", """libupanda3d_c.so""")


    # ctor/dtor : classmethod type calls and return only raw pointer or void

    c.ct['ctor'] = {
        1 : ['s', 48, c.lib.func('p','Filename_C_ctor_p_p','p')],
        2 : ['s', 48, c.lib.func('p','Filename_C_ctor_p_pp','pp')],
        1 : ['s', 48, c.lib.func('p','Filename_C_ctor_p_s','s')],
        0 : ['s', 'p', c.lib.func('p','Filename_C_ctor_p_v','')],
    }
    c.ct['ctor_1'] = ['s', 48, c.lib.func('p','Filename_C_ctor_1_p_p','p')]
    c.ct['ctor_2'] = ['s', 48, c.lib.func('p','Filename_C_ctor_2_p_p','p')]
    c.ct['ctor_3'] = ['s', 48, c.lib.func('p','Filename_C_ctor_3_p_p','p')]

    # fixed pos : return basic types or other C++ classes

    c.ct['find_on_searchpath'] = ['d', 'i', c.lib.func('i','Filename_C_find_on_searchpath_i_pp','pp')]
    c.ct['is_text'] = ['d', 'B', c.lib.func('B','Filename_C_is_text_B_p','p')]
    c.ct['init_type'] = ['d', 'v', c.lib.func('v','Filename_C_init_type_v_v','v')]
    c.ct['set_type'] = ['d', 'v', c.lib.func('v','Filename_C_set_type_v_pp','pp')]
    c.ct['open_read_append_1'] = ['d', 'B', c.lib.func('B','Filename_C_open_read_append_1_B_pp','pp')]
    c.ct['to_os_short_name'] = ['d', 's', c.lib.func('s','Filename_C_to_os_short_name_s_p','p')]
    c.ct['get_access_timestamp'] = ['d', 'p', c.lib.func('p','Filename_C_get_access_timestamp_p_p','p')]
    c.ct['get_basename_wo_extension'] = ['d', 's', c.lib.func('s','Filename_C_get_basename_wo_extension_s_p','p')]
    c.ct['make_true_case'] = ['d', 'B', c.lib.func('B','Filename_C_make_true_case_B_p','p')]
    c.ct['mkdir'] = ['d', 'B', c.lib.func('B','Filename_C_mkdir_B_p','p')]
    c.ct['is_regular_file'] = ['d', 'B', c.lib.func('B','Filename_C_is_regular_file_B_p','p')]
    c.ct['make_dir'] = ['d', 'B', c.lib.func('B','Filename_C_make_dir_B_p','p')]
    c.ct['resolve_filename_1'] = ['d', 'B', c.lib.func('B','Filename_C_resolve_filename_1_B_ppp','ppp')]
    c.ct['open_read_write_1'] = ['d', 'B', c.lib.func('B','Filename_C_open_read_write_1_B_ppB','ppB')]
    c.ct['open_write'] = ['d', 'B', c.lib.func('B','Filename_C_open_write_B_ppB','ppB')]
    c.ct['open_read_write_3'] = ['d', 'B', c.lib.func('B','Filename_C_open_read_write_3_B_ppB','ppB')]
    c.ct['open_read_write_2'] = ['d', 'B', c.lib.func('B','Filename_C_open_read_write_2_B_ppB','ppB')]
    c.ct['get_dirname'] = ['d', 's', c.lib.func('s','Filename_C_get_dirname_s_p','p')]
    c.ct['is_binary'] = ['d', 'B', c.lib.func('B','Filename_C_is_binary_B_p','p')]
    c.ct['rmdir'] = ['d', 'B', c.lib.func('B','Filename_C_rmdir_B_p','p')]
    c.ct['chdir'] = ['d', 'B', c.lib.func('B','Filename_C_chdir_B_p','p')]
    c.ct['from_os_specific'] = ['d', 48, c.lib.func('p','Filename_C_from_os_specific_p_spp','spp')]
    c.ct['standardize'] = ['d', 'v', c.lib.func('v','Filename_C_standardize_v_p','p')]
    c.ct['unlink'] = ['d', 'B', c.lib.func('B','Filename_C_unlink_B_p','p')]
    c.ct['set_basename'] = ['d', 'v', c.lib.func('v','Filename_C_set_basename_v_pp','pp')]
    c.ct['get_timestamp'] = ['d', 'p', c.lib.func('p','Filename_C_get_timestamp_p_p','p')]
    c.ct['set_text'] = ['d', 'v', c.lib.func('v','Filename_C_set_text_v_p','p')]
    c.ct['get_filename_index'] = ['d', 48, c.lib.func('p','Filename_C_get_filename_index_p_pi','pi')]
    c.ct['expand_from_1'] = ['d', 48, c.lib.func('p','Filename_C_expand_from_1_p_spp','spp')]
    c.ct['is_binary_or_text'] = ['d', 'B', c.lib.func('B','Filename_C_is_binary_or_text_B_p','p')]
    c.ct['set_filesystem_encoding'] = ['d', 'v', c.lib.func('v','Filename_C_set_filesystem_encoding_v_pp','pp')]
    c.ct['get_fullpath_w'] = ['d', 'p', c.lib.func('p','Filename_C_get_fullpath_w_p_p','p')]
    c.ct['get_common_appdata_directory'] = ['d', 48, c.lib.func('p','Filename_C_get_common_appdata_directory_p_v','v')]
    c.ct['get_user_appdata_directory'] = ['d', 48, c.lib.func('p','Filename_C_get_user_appdata_directory_p_v','v')]
    c.ct['from_os_specific_1'] = ['d', 48, c.lib.func('p','Filename_C_from_os_specific_1_p_spp','spp')]
    c.ct['open_read_append'] = ['d', 'B', c.lib.func('B','Filename_C_open_read_append_B_pp','pp')]
    c.ct['set_binary'] = ['d', 'v', c.lib.func('v','Filename_C_set_binary_v_p','p')]
    c.ct['resolve_filename'] = ['d', 'B', c.lib.func('B','Filename_C_resolve_filename_B_ppp','ppp')]
    c.ct['c_str'] = ['d', 's', c.lib.func('s','Filename_C_c_str_s_p','p')]
    c.ct['get_hash'] = ['d', 'i', c.lib.func('i','Filename_C_get_hash_i_p','p')]
    c.ct['get_class_type'] = ['d', 'i', c.lib.func('i','Filename_C_get_class_type_i_v','v')]
    c.ct['compare_to'] = ['d', 'i', c.lib.func('i','Filename_C_compare_to_i_pp','pp')]
    c.ct['temporary_1'] = ['d', 48, c.lib.func('p','Filename_C_temporary_1_p_spppp','spppp')]
    c.ct['is_directory'] = ['d', 'B', c.lib.func('B','Filename_C_is_directory_B_p','p')]
    c.ct['get_file_size'] = ['d', 'p', c.lib.func('p','Filename_C_get_file_size_p_p','p')]
    c.ct['temporary_2'] = ['d', 48, c.lib.func('p','Filename_C_temporary_2_p_spppp','spppp')]
    c.ct['to_os_specific_w'] = ['d', 'p', c.lib.func('p','Filename_C_to_os_specific_w_p_p','p')]
    c.ct['set_extension'] = ['d', 'v', c.lib.func('v','Filename_C_set_extension_v_pp','pp')]
    c.ct['is_local'] = ['d', 'B', c.lib.func('B','Filename_C_is_local_B_p','p')]
    c.ct['copy_to'] = ['d', 'B', c.lib.func('B','Filename_C_copy_to_B_pp','pp')]
    c.ct['scan_directory'] = ['d', 'B', c.lib.func('B','Filename_C_scan_directory_B_pp','pp')]
    c.ct['open_read_1'] = ['d', 'B', c.lib.func('B','Filename_C_open_read_1_B_pp','pp')]
    c.ct['temporary'] = ['d', 48, c.lib.func('p','Filename_C_temporary_p_spppp','spppp')]
    c.ct['has_hash'] = ['d', 'B', c.lib.func('B','Filename_C_has_hash_B_p','p')]
    c.ct['get_extension'] = ['d', 's', c.lib.func('s','Filename_C_get_extension_s_p','p')]
    c.ct['dso_filename'] = ['d', 48, c.lib.func('p','Filename_C_dso_filename_p_sp','sp')]
    c.ct['get_home_directory'] = ['d', 48, c.lib.func('p','Filename_C_get_home_directory_p_v','v')]
    c.ct['open_append'] = ['d', 'B', c.lib.func('B','Filename_C_open_append_B_pp','pp')]
    c.ct['touch'] = ['d', 'B', c.lib.func('B','Filename_C_touch_B_p','p')]
    c.ct['from_os_specific_w_1'] = ['d', 48, c.lib.func('p','Filename_C_from_os_specific_w_1_p_ppp','ppp')]
    c.ct['exists'] = ['d', 'B', c.lib.func('B','Filename_C_exists_B_p','p')]
    c.ct['make_relative_to_1'] = ['d', 'B', c.lib.func('B','Filename_C_make_relative_to_1_B_ppB','ppB')]
    c.ct['get_filesystem_encoding'] = ['d', 'p', c.lib.func('p','Filename_C_get_filesystem_encoding_p_v','v')]
    c.ct['is_executable'] = ['d', 'B', c.lib.func('B','Filename_C_is_executable_B_p','p')]
    c.ct['__nonzero__'] = ['d', 'B', c.lib.func('B','Filename_C___nonzero___B_p','p')]
    c.ct['expand_from'] = ['d', 48, c.lib.func('p','Filename_C_expand_from_p_spp','spp')]
    c.ct['get_hash_to_end'] = ['d', 's', c.lib.func('s','Filename_C_get_hash_to_end_s_p','p')]
    c.ct['open_read'] = ['d', 'B', c.lib.func('B','Filename_C_open_read_B_pp','pp')]
    c.ct['get_fullpath'] = ['d', 's', c.lib.func('s','Filename_C_get_fullpath_s_p','p')]
    c.ct['set_hash_to_end'] = ['d', 'v', c.lib.func('v','Filename_C_set_hash_to_end_v_pp','pp')]
    c.ct['set_fullpath_wo_extension'] = ['d', 'v', c.lib.func('v','Filename_C_set_fullpath_wo_extension_v_pp','pp')]
    c.ct['get_basename'] = ['d', 's', c.lib.func('s','Filename_C_get_basename_s_p','p')]
    c.ct['compare_timestamps_2'] = ['d', 'i', c.lib.func('i','Filename_C_compare_timestamps_2_i_ppBB','ppBB')]
    c.ct['compare_timestamps_1'] = ['d', 'i', c.lib.func('i','Filename_C_compare_timestamps_1_i_ppBB','ppBB')]
    c.ct['to_os_generic'] = ['d', 's', c.lib.func('s','Filename_C_to_os_generic_s_p','p')]
    c.ct['to_os_long_name'] = ['d', 's', c.lib.func('s','Filename_C_to_os_long_name_s_p','p')]
    c.ct['rename_to'] = ['d', 'B', c.lib.func('B','Filename_C_rename_to_B_pp','pp')]
    c.ct['set_dirname'] = ['d', 'v', c.lib.func('v','Filename_C_set_dirname_v_pp','pp')]
    c.ct['to_os_specific'] = ['d', 's', c.lib.func('s','Filename_C_to_os_specific_s_p','p')]
    c.ct['extract_components'] = ['d', 'v', c.lib.func('v','Filename_C_extract_components_v_pp','pp')]
    c.ct['get_fullpath_wo_extension'] = ['d', 's', c.lib.func('s','Filename_C_get_fullpath_wo_extension_s_p','p')]
    c.ct['length'] = ['d', 'p', c.lib.func('p','Filename_C_length_p_p','p')]
    c.ct['is_writable'] = ['d', 'B', c.lib.func('B','Filename_C_is_writable_B_p','p')]
    c.ct['is_fully_qualified'] = ['d', 'B', c.lib.func('B','Filename_C_is_fully_qualified_B_p','p')]
    c.ct['make_relative_to'] = ['d', 'B', c.lib.func('B','Filename_C_make_relative_to_B_ppB','ppB')]
    c.ct['make_canonical'] = ['d', 'B', c.lib.func('B','Filename_C_make_canonical_B_p','p')]
    c.ct['open_write_1'] = ['d', 'B', c.lib.func('B','Filename_C_open_write_1_B_ppB','ppB')]
    c.ct['get_type'] = ['d', 'p', c.lib.func('p','Filename_C_get_type_p_p','p')]
    c.ct['open_write_2'] = ['d', 'B', c.lib.func('B','Filename_C_open_write_2_B_ppB','ppB')]
    c.ct['open_write_3'] = ['d', 'B', c.lib.func('B','Filename_C_open_write_3_B_ppB','ppB')]
    c.ct['empty'] = ['d', 'B', c.lib.func('B','Filename_C_empty_B_p','p')]
    c.ct['from_os_specific_w'] = ['d', 48, c.lib.func('p','Filename_C_from_os_specific_w_p_ppp','ppp')]
    c.ct['output'] = ['d', 'v', c.lib.func('v','Filename_C_output_v_pp','pp')]
    c.ct['set_fullpath'] = ['d', 'v', c.lib.func('v','Filename_C_set_fullpath_v_pp','pp')]
    c.ct['pattern_filename'] = ['d', 48, c.lib.func('p','Filename_C_pattern_filename_p_sp','sp')]
    c.ct['open_read_write'] = ['d', 'B', c.lib.func('B','Filename_C_open_read_write_B_ppB','ppB')]
    c.ct['set_basename_wo_extension'] = ['d', 'v', c.lib.func('v','Filename_C_set_basename_wo_extension_v_pp','pp')]
    c.ct['open_append_1'] = ['d', 'B', c.lib.func('B','Filename_C_open_append_1_B_pp','pp')]
    c.ct['set_pattern'] = ['d', 'v', c.lib.func('v','Filename_C_set_pattern_v_pB','pB')]
    c.ct['get_pattern'] = ['d', 'B', c.lib.func('B','Filename_C_get_pattern_B_p','p')]
    c.ct['compare_timestamps'] = ['d', 'i', c.lib.func('i','Filename_C_compare_timestamps_i_ppBB','ppBB')]
    c.ct['get_temp_directory'] = ['d', 48, c.lib.func('p','Filename_C_get_temp_directory_p_v','v')]
    c.ct['executable_filename'] = ['d', 48, c.lib.func('p','Filename_C_executable_filename_p_sp','sp')]

    # variadic : return basic types or other C++ classes

    c.ct['text_filename'] = {
        2 : ['d', 48, c.lib.func('p','Filename_C_text_filename_p_pp','pp')],
        2 : ['d', 48, c.lib.func('p','Filename_C_text_filename_p_sp','sp')],
    }
    c.ct['substr'] = {
        2 : ['d', 's', c.lib.func('s','Filename_C_substr_s_pp','pp')],
        3 : ['d', 's', c.lib.func('s','Filename_C_substr_s_ppp','ppp')],
    }
    c.ct['binary_filename'] = {
        2 : ['d', 48, c.lib.func('p','Filename_C_binary_filename_p_pp','pp')],
        2 : ['d', 48, c.lib.func('p','Filename_C_binary_filename_p_sp','sp')],
    }
    c.ct['make_absolute'] = {
        1 : ['d', 'v', c.lib.func('v','Filename_C_make_absolute_v_p','p')],
        2 : ['d', 'v', c.lib.func('v','Filename_C_make_absolute_v_pp','pp')],
    }


    # c++ instance methods

    def __del__(self):
        self.__class__.destroy(self)

    def __getattr__(self, attr):
        return self.__call(attr)

Filename.c.link(Filename)



class WindowFramework(cxx.cplusplus):
    c = cxx.cstructs().register("WindowFramework", "upanda3d", """libupanda3d_c.so""")


    # ctor/dtor : classmethod type calls and return only raw pointer or void

    c.ct['ctor'] = ['s', 2, c.lib.func('p','WindowFramework_C_ctor_p_p','p')]

    # fixed pos : return basic types or other C++ classes

    c.ct['get_lighting'] = ['d', 'B', c.lib.func('B','WindowFramework_C_get_lighting_B_p','p')]
    c.ct['set_anim_controls'] = ['d', 'v', c.lib.func('v','WindowFramework_C_set_anim_controls_v_pB','pB')]
    c.ct['loop_animations_1'] = ['d', 'v', c.lib.func('v','WindowFramework_C_loop_animations_1_v_pi','pi')]
    c.ct['load_default_model'] = ['d', 26, c.lib.func('p','WindowFramework_C_load_default_model_p_pp','pp')]
    c.ct['get_render'] = ['d', 26, c.lib.func('p','WindowFramework_C_get_render_p_p','p')]
    c.ct['get_panda_framework'] = ['d', 23, c.lib.func('p','WindowFramework_C_get_panda_framework_p_p','p')]
    c.ct['loop_animations'] = ['d', 'v', c.lib.func('v','WindowFramework_C_loop_animations_v_pi','pi')]
    c.ct['load_model'] = ['d', 26, c.lib.func('p','WindowFramework_C_load_model_p_ppp','ppp')]
    c.ct['get_class_type'] = ['d', 'i', c.lib.func('i','WindowFramework_C_get_class_type_i_v','v')]
    c.ct['adjust_dimensions'] = ['d', 'v', c.lib.func('v','WindowFramework_C_adjust_dimensions_v_p','p')]
    c.ct['get_wireframe'] = ['d', 'B', c.lib.func('B','WindowFramework_C_get_wireframe_B_p','p')]
    c.ct['get_aspect_2d'] = ['d', 26, c.lib.func('p','WindowFramework_C_get_aspect_2d_p_p','p')]
    c.ct['get_num_cameras'] = ['d', 'i', c.lib.func('i','WindowFramework_C_get_num_cameras_i_p','p')]
    c.ct['get_camera_group'] = ['d', 26, c.lib.func('p','WindowFramework_C_get_camera_group_p_p','p')]
    c.ct['get_display_region_3d'] = ['d', 52, c.lib.func('p','WindowFramework_C_get_display_region_3d_p_p','p')]
    c.ct['split_window_1'] = ['d', 2, c.lib.func('p','WindowFramework_C_split_window_1_p_pp','pp')]
    c.ct['set_two_sided'] = ['d', 'v', c.lib.func('v','WindowFramework_C_set_two_sided_v_pB','pB')]
    c.ct['set_one_sided_reverse'] = ['d', 'v', c.lib.func('v','WindowFramework_C_set_one_sided_reverse_v_pB','pB')]
    c.ct['get_wireframe_filled'] = ['d', 'B', c.lib.func('B','WindowFramework_C_get_wireframe_filled_B_p','p')]
    c.ct['get_pixel_2d'] = ['d', 26, c.lib.func('p','WindowFramework_C_get_pixel_2d_p_p','p')]
    c.ct['enable_keyboard'] = ['d', 'v', c.lib.func('v','WindowFramework_C_enable_keyboard_v_p','p')]
    c.ct['get_anim_controls'] = ['d', 'B', c.lib.func('B','WindowFramework_C_get_anim_controls_B_p','p')]
    c.ct['set_texture'] = ['d', 'v', c.lib.func('v','WindowFramework_C_set_texture_v_pB','pB')]
    c.ct['load_models'] = ['d', 'B', c.lib.func('B','WindowFramework_C_load_models_B_ppp','ppp')]
    c.ct['set_wireframe_1'] = ['d', 'v', c.lib.func('v','WindowFramework_C_set_wireframe_1_v_pBB','pBB')]
    c.ct['get_shuttle_controls_font'] = ['d', 'p', c.lib.func('p','WindowFramework_C_get_shuttle_controls_font_p_v','v')]
    c.ct['set_wireframe'] = ['d', 'v', c.lib.func('v','WindowFramework_C_set_wireframe_v_pBB','pBB')]
    c.ct['make_camera'] = ['d', 26, c.lib.func('p','WindowFramework_C_make_camera_p_p','p')]
    c.ct['split_window'] = ['d', 2, c.lib.func('p','WindowFramework_C_split_window_p_pp','pp')]
    c.ct['get_graphics_window'] = ['d', 'p', c.lib.func('p','WindowFramework_C_get_graphics_window_p_p','p')]
    c.ct['set_lighting'] = ['d', 'v', c.lib.func('v','WindowFramework_C_set_lighting_v_pB','pB')]
    c.ct['center_trackball'] = ['d', 'v', c.lib.func('v','WindowFramework_C_center_trackball_v_pp','pp')]
    c.ct['stagger_animations'] = ['d', 'v', c.lib.func('v','WindowFramework_C_stagger_animations_v_p','p')]
    c.ct['next_anim_control'] = ['d', 'v', c.lib.func('v','WindowFramework_C_next_anim_control_v_p','p')]
    c.ct['get_two_sided'] = ['d', 'B', c.lib.func('B','WindowFramework_C_get_two_sided_B_p','p')]
    c.ct['get_type'] = ['d', 'i', c.lib.func('i','WindowFramework_C_get_type_i_p','p')]
    c.ct['get_graphics_output'] = ['d', 'p', c.lib.func('p','WindowFramework_C_get_graphics_output_p_p','p')]
    c.ct['get_one_sided_reverse'] = ['d', 'B', c.lib.func('B','WindowFramework_C_get_one_sided_reverse_B_p','p')]
    c.ct['set_perpixel'] = ['d', 'v', c.lib.func('v','WindowFramework_C_set_perpixel_v_pB','pB')]
    c.ct['set_background_type'] = ['d', 'v', c.lib.func('v','WindowFramework_C_set_background_type_v_pp','pp')]
    c.ct['get_display_region_2d'] = ['d', 52, c.lib.func('p','WindowFramework_C_get_display_region_2d_p_p','p')]
    c.ct['get_texture'] = ['d', 'B', c.lib.func('B','WindowFramework_C_get_texture_B_p','p')]
    c.ct['setup_trackball'] = ['d', 'v', c.lib.func('v','WindowFramework_C_setup_trackball_v_p','p')]
    c.ct['get_button_thrower'] = ['d', 26, c.lib.func('p','WindowFramework_C_get_button_thrower_p_p','p')]
    c.ct['get_background_type'] = ['d', 1, c.lib.func('p','WindowFramework_C_get_background_type_p_p','p')]
    c.ct['get_render_2d'] = ['d', 26, c.lib.func('p','WindowFramework_C_get_render_2d_p_p','p')]
    c.ct['force_init_type'] = ['d', 'i', c.lib.func('i','WindowFramework_C_force_init_type_i_p','p')]
    c.ct['init_type'] = ['d', 'v', c.lib.func('v','WindowFramework_C_init_type_v_v','v')]
    c.ct['get_perpixel'] = ['d', 'B', c.lib.func('B','WindowFramework_C_get_perpixel_B_p','p')]
    c.ct['get_mouse'] = ['d', 26, c.lib.func('p','WindowFramework_C_get_mouse_p_p','p')]
    c.ct['get_camera'] = ['d', 56, c.lib.func('p','WindowFramework_C_get_camera_p_pi','pi')]

    # variadic : return basic types or other C++ classes



    # c++ instance methods

    def __del__(self):
        self.__class__.destroy(self)

    def __getattr__(self, attr):
        return self.__call(attr)

WindowFramework.c.link(WindowFramework)



class NodePathCollection(cxx.cplusplus):
    c = cxx.cstructs().register("NodePathCollection", "upanda3d", """libupanda3d_c.so""")


    # ctor/dtor : classmethod type calls and return only raw pointer or void

    c.ct['ctor'] = {
        1 : ['s', 24, c.lib.func('p','NodePathCollection_C_ctor_p_p','p')],
        0 : ['s', 24, c.lib.func('p','NodePathCollection_C_ctor_p_v','')],
    }

    # fixed pos : return basic types or other C++ classes

    c.ct['set_attrib'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_set_attrib_v_ppi','ppi')]
    c.ct['set_attrib_1'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_set_attrib_1_v_ppi','ppi')]
    c.ct['append'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_append_v_pp','pp')]
    c.ct['remove_path'] = ['d', 'B', c.lib.func('B','NodePathCollection_C_remove_path_B_pp','pp')]
    c.ct['set_collide_mask'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_set_collide_mask_v_pppp','pppp')]
    c.ct['remove_paths_from'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_remove_paths_from_v_pp','pp')]
    c.ct['stash'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_stash_v_p','p')]
    c.ct['write_1'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_write_1_v_ppi','ppi')]
    c.ct['output'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_output_v_pp','pp')]
    c.ct['detach'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_detach_v_p','p')]
    c.ct['remove_duplicate_paths'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_remove_duplicate_paths_v_p','p')]
    c.ct['get_path'] = ['d', 26, c.lib.func('p','NodePathCollection_C_get_path_p_pi','pi')]
    c.ct['extend'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_extend_v_pp','pp')]
    c.ct['clear'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_clear_v_p','p')]
    c.ct['is_empty'] = ['d', 'B', c.lib.func('B','NodePathCollection_C_is_empty_B_p','p')]
    c.ct['set_color_scale_2'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_set_color_scale_2_v_pffffi','pffffi')]
    c.ct['reserve'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_reserve_v_pp','pp')]
    c.ct['add_path'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_add_path_v_pp','pp')]
    c.ct['compose_color_scale_2'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_compose_color_scale_2_v_pffffi','pffffi')]
    c.ct['size'] = ['d', 'p', c.lib.func('p','NodePathCollection_C_size_p_p','p')]
    c.ct['write'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_write_v_ppi','ppi')]
    c.ct['get_num_paths'] = ['d', 'i', c.lib.func('i','NodePathCollection_C_get_num_paths_i_p','p')]
    c.ct['add_paths_from'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_add_paths_from_v_pp','pp')]
    c.ct['unstash'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_unstash_v_p','p')]
    c.ct['set_collide_mask_1'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_set_collide_mask_1_v_pppp','pppp')]
    c.ct['set_collide_mask_2'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_set_collide_mask_2_v_pppp','pppp')]
    c.ct['find_all_matches'] = ['d', 24, c.lib.func('p','NodePathCollection_C_find_all_matches_p_pp','pp')]
    c.ct['hide'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_hide_v_p','p')]
    c.ct['has_path'] = ['d', 'B', c.lib.func('B','NodePathCollection_C_has_path_B_pp','pp')]
    c.ct['reparent_to'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_reparent_to_v_pp','pp')]
    c.ct['get_collide_mask'] = ['d', 'p', c.lib.func('p','NodePathCollection_C_get_collide_mask_p_p','p')]
    c.ct['calc_tight_bounds'] = ['d', 'B', c.lib.func('B','NodePathCollection_C_calc_tight_bounds_B_ppp','ppp')]
    c.ct['set_color_2'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_set_color_2_v_pffffi','pffffi')]
    c.ct['wrt_reparent_to'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_wrt_reparent_to_v_pp','pp')]
    c.ct['show'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_show_v_p','p')]
    c.ct['ls_1'] = ['d', 'v', c.lib.func('v','NodePathCollection_C_ls_1_v_ppi','ppi')]

    # variadic : return basic types or other C++ classes

    c.ct['set_texture_off'] = {
        2 : ['d', 'v', c.lib.func('v','NodePathCollection_C_set_texture_off_v_pi','pi')],
        3 : ['d', 'v', c.lib.func('v','NodePathCollection_C_set_texture_off_v_ppi','ppi')],
    }
    c.ct['set_texture_off_1'] = {
        2 : ['d', 'v', c.lib.func('v','NodePathCollection_C_set_texture_off_1_v_pi','pi')],
        3 : ['d', 'v', c.lib.func('v','NodePathCollection_C_set_texture_off_1_v_ppi','ppi')],
    }
    c.ct['set_color_scale_1'] = {
        6 : ['d', 'v', c.lib.func('v','NodePathCollection_C_set_color_scale_1_v_pffffi','pffffi')],
        3 : ['d', 'v', c.lib.func('v','NodePathCollection_C_set_color_scale_1_v_ppi','ppi')],
    }
    c.ct['set_texture'] = {
        3 : ['d', 'v', c.lib.func('v','NodePathCollection_C_set_texture_v_ppi','ppi')],
        4 : ['d', 'v', c.lib.func('v','NodePathCollection_C_set_texture_v_pppi','pppi')],
    }
    c.ct['compose_color_scale_1'] = {
        6 : ['d', 'v', c.lib.func('v','NodePathCollection_C_compose_color_scale_1_v_pffffi','pffffi')],
        3 : ['d', 'v', c.lib.func('v','NodePathCollection_C_compose_color_scale_1_v_ppi','ppi')],
    }
    c.ct['set_color_scale'] = {
        6 : ['d', 'v', c.lib.func('v','NodePathCollection_C_set_color_scale_v_pffffi','pffffi')],
        3 : ['d', 'v', c.lib.func('v','NodePathCollection_C_set_color_scale_v_ppi','ppi')],
    }
    c.ct['compose_color_scale'] = {
        6 : ['d', 'v', c.lib.func('v','NodePathCollection_C_compose_color_scale_v_pffffi','pffffi')],
        3 : ['d', 'v', c.lib.func('v','NodePathCollection_C_compose_color_scale_v_ppi','ppi')],
    }
    c.ct['set_color_1'] = {
        6 : ['d', 'v', c.lib.func('v','NodePathCollection_C_set_color_1_v_pffffi','pffffi')],
        3 : ['d', 'v', c.lib.func('v','NodePathCollection_C_set_color_1_v_ppi','ppi')],
    }
    c.ct['set_texture_1'] = {
        3 : ['d', 'v', c.lib.func('v','NodePathCollection_C_set_texture_1_v_ppi','ppi')],
        4 : ['d', 'v', c.lib.func('v','NodePathCollection_C_set_texture_1_v_pppi','pppi')],
    }
    c.ct['ls'] = {
        1 : ['d', 'v', c.lib.func('v','NodePathCollection_C_ls_v_p','p')],
        3 : ['d', 'v', c.lib.func('v','NodePathCollection_C_ls_v_ppi','ppi')],
    }
    c.ct['set_color'] = {
        6 : ['d', 'v', c.lib.func('v','NodePathCollection_C_set_color_v_pffffi','pffffi')],
        3 : ['d', 'v', c.lib.func('v','NodePathCollection_C_set_color_v_ppi','ppi')],
    }


    # c++ instance methods

    def __del__(self):
        self.__class__.destroy(self)

    def __getattr__(self, attr):
        return self.__call(attr)

NodePathCollection.c.link(NodePathCollection)



if __name__ == '__main__':
    import os
    import gc
    import time
    REFC = cxx.REFC

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

        print('framework=', E.get_wframe() )


        np = E.load_model( "model.bam" )

        print("np","=",np)


        cxx.TRACE = 0
        E.attach(np)

        if 1:
            v3 = LVecBase3f()
            v3.set_x(0.01)
            v3.set_y(42.01)
            v3.set_z(0.01)

            print( v3, v3.get_x() , v3.get_y(), v3.get_z() )

            np.set_pos( v3 )

        if 1:
            v3 = LVecBase3f(0.01, 42.01, 0.01)

            np.set_pos( v3 )
            #E.op_pos(v3)

            v3 = LVecBase3f(2.0, 2.0, 2.0)
            print( v3, v3.get_x() , v3.get_y(), v3.get_z() )
            np.set_scale( v3 )
            #E.op_scale(v3)


        while E.is_alive():
            E.step()
            gc.collect()
            time.sleep(.016)

        print("C++ engine requested exit")
        del E
        print("deleting copy")
        del C

    print("--- test3 with refcounting ----")
    test()
    del test
    gc.collect()
    gc.collect()

    cxx.gc()


