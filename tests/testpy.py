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


class NP:

    lib = ffi.open("""libupanda3d_c.so""")

    NP_C_reparent_to_v_p = lib.func('v','NP_C_reparent_to_v_p','p')

# variadic

    NP_C_reparent_to_v_p = {
        1 : lib.func('p','NP_C_NP_p_p','p'),
        0 : lib.func('p','NP_C_NP_p_v',''),
    }
# c++ struct
    def reparent_to(*argv,**kw):
        return self.NP_C_reparent_to_v_p(self.iptr, *argv, **kw)

    def NP(*argv,**kw):
        return variadic_call(self, NP_C_reparent_to_v_p, *argv, **kw)

class WindowFramework:

    lib = ffi.open("""libupanda3d_c.so""")

    WindowFramework_C_get_lighting_B_p = lib.func('B','WindowFramework_C_get_lighting_B_p','p')
    WindowFramework_C_set_anim_controls_v_p = lib.func('v','WindowFramework_C_set_anim_controls_v_p','p')
    WindowFramework_C_loop_animations_1_v_p = lib.func('v','WindowFramework_C_loop_animations_1_v_p','p')
    WindowFramework_C_load_default_model_p_p = lib.func('p','WindowFramework_C_load_default_model_p_p','p')
    WindowFramework_C_get_render_p_p = lib.func('p','WindowFramework_C_get_render_p_p','p')
    WindowFramework_C_get_panda_framework_p_p = lib.func('p','WindowFramework_C_get_panda_framework_p_p','p')
    WindowFramework_C_loop_animations_v_p = lib.func('v','WindowFramework_C_loop_animations_v_p','p')
    WindowFramework_C_get_class_type_i_p = lib.func('i','WindowFramework_C_get_class_type_i_p','p')
    WindowFramework_C_adjust_dimensions_v_p = lib.func('v','WindowFramework_C_adjust_dimensions_v_p','p')
    WindowFramework_C_init_type_v_p = lib.func('v','WindowFramework_C_init_type_v_p','p')
    WindowFramework_C_get_wireframe_B_p = lib.func('B','WindowFramework_C_get_wireframe_B_p','p')
    WindowFramework_C_get_aspect_2d_p_p = lib.func('p','WindowFramework_C_get_aspect_2d_p_p','p')
    WindowFramework_C_get_num_cameras_i_p = lib.func('i','WindowFramework_C_get_num_cameras_i_p','p')
    WindowFramework_C_get_camera_group_p_p = lib.func('p','WindowFramework_C_get_camera_group_p_p','p')
    WindowFramework_C_get_display_region_3d_p_p = lib.func('p','WindowFramework_C_get_display_region_3d_p_p','p')
    WindowFramework_C_stagger_animations_v_p = lib.func('v','WindowFramework_C_stagger_animations_v_p','p')
    WindowFramework_C_set_two_sided_v_p = lib.func('v','WindowFramework_C_set_two_sided_v_p','p')
    WindowFramework_C_set_one_sided_reverse_v_p = lib.func('v','WindowFramework_C_set_one_sided_reverse_v_p','p')
    WindowFramework_C_get_wireframe_filled_B_p = lib.func('B','WindowFramework_C_get_wireframe_filled_B_p','p')
    WindowFramework_C_get_pixel_2d_p_p = lib.func('p','WindowFramework_C_get_pixel_2d_p_p','p')
    WindowFramework_C_enable_keyboard_v_p = lib.func('v','WindowFramework_C_enable_keyboard_v_p','p')
    WindowFramework_C_split_window_p_p = lib.func('p','WindowFramework_C_split_window_p_p','p')
    WindowFramework_C_set_texture_v_p = lib.func('v','WindowFramework_C_set_texture_v_p','p')
    WindowFramework_C_get_anim_controls_B_p = lib.func('B','WindowFramework_C_get_anim_controls_B_p','p')
    WindowFramework_C_WindowFramework_p_p = lib.func('p','WindowFramework_C_WindowFramework_p_p','p')
    WindowFramework_C_get_shuttle_controls_font_p_v = lib.func('p','WindowFramework_C_get_shuttle_controls_font_p_v','v')
    WindowFramework_C_make_camera_p_p = lib.func('p','WindowFramework_C_make_camera_p_p','p')
    WindowFramework_C_get_graphics_window_p_p = lib.func('p','WindowFramework_C_get_graphics_window_p_p','p')
    WindowFramework_C_set_lighting_v_p = lib.func('v','WindowFramework_C_set_lighting_v_p','p')
    WindowFramework_C_center_trackball_v_p = lib.func('v','WindowFramework_C_center_trackball_v_p','p')
    WindowFramework_C_next_anim_control_v_p = lib.func('v','WindowFramework_C_next_anim_control_v_p','p')
    WindowFramework_C_get_two_sided_B_p = lib.func('B','WindowFramework_C_get_two_sided_B_p','p')
    WindowFramework_C_get_type_i_p = lib.func('i','WindowFramework_C_get_type_i_p','p')
    WindowFramework_C_get_graphics_output_p_p = lib.func('p','WindowFramework_C_get_graphics_output_p_p','p')
    WindowFramework_C_get_one_sided_reverse_B_p = lib.func('B','WindowFramework_C_get_one_sided_reverse_B_p','p')
    WindowFramework_C_set_perpixel_v_p = lib.func('v','WindowFramework_C_set_perpixel_v_p','p')
    WindowFramework_C_set_background_type_v_p = lib.func('v','WindowFramework_C_set_background_type_v_p','p')
    WindowFramework_C_get_display_region_2d_p_p = lib.func('p','WindowFramework_C_get_display_region_2d_p_p','p')
    WindowFramework_C_get_texture_B_p = lib.func('B','WindowFramework_C_get_texture_B_p','p')
    WindowFramework_C_setup_trackball_v_p = lib.func('v','WindowFramework_C_setup_trackball_v_p','p')
    WindowFramework_C_get_button_thrower_p_p = lib.func('p','WindowFramework_C_get_button_thrower_p_p','p')
    WindowFramework_C_get_background_type_p_p = lib.func('p','WindowFramework_C_get_background_type_p_p','p')
    WindowFramework_C_get_render_2d_p_p = lib.func('p','WindowFramework_C_get_render_2d_p_p','p')
    WindowFramework_C_force_init_type_i_p = lib.func('i','WindowFramework_C_force_init_type_i_p','p')
    WindowFramework_C_split_window_1_p_p = lib.func('p','WindowFramework_C_split_window_1_p_p','p')
    WindowFramework_C_get_perpixel_B_p = lib.func('B','WindowFramework_C_get_perpixel_B_p','p')
    WindowFramework_C_get_mouse_p_p = lib.func('p','WindowFramework_C_get_mouse_p_p','p')
    WindowFramework_C_get_camera_p_p = lib.func('p','WindowFramework_C_get_camera_p_p','p')

# variadic

# c++ struct
    def get_lighting(*argv,**kw):
        return self.WindowFramework_C_get_lighting_B_p(self.iptr, *argv, **kw)

    def set_anim_controls(*argv,**kw):
        return self.WindowFramework_C_set_anim_controls_v_p(self.iptr, *argv, **kw)

    def loop_animations_1(*argv,**kw):
        return self.WindowFramework_C_loop_animations_1_v_p(self.iptr, *argv, **kw)

    def load_default_model(*argv,**kw):
        return self.WindowFramework_C_load_default_model_p_p(self.iptr, *argv, **kw)

    def get_render(*argv,**kw):
        return self.WindowFramework_C_get_render_p_p(self.iptr, *argv, **kw)

    def get_panda_framework(*argv,**kw):
        return self.WindowFramework_C_get_panda_framework_p_p(self.iptr, *argv, **kw)

    def loop_animations(*argv,**kw):
        return self.WindowFramework_C_loop_animations_v_p(self.iptr, *argv, **kw)

    def get_class_type(*argv,**kw):
        return self.WindowFramework_C_get_class_type_i_p(self.iptr, *argv, **kw)

    def adjust_dimensions(*argv,**kw):
        return self.WindowFramework_C_adjust_dimensions_v_p(self.iptr, *argv, **kw)

    def init_type(*argv,**kw):
        return self.WindowFramework_C_init_type_v_p(self.iptr, *argv, **kw)

    def get_wireframe(*argv,**kw):
        return self.WindowFramework_C_get_wireframe_B_p(self.iptr, *argv, **kw)

    def get_aspect_2d(*argv,**kw):
        return self.WindowFramework_C_get_aspect_2d_p_p(self.iptr, *argv, **kw)

    def get_num_cameras(*argv,**kw):
        return self.WindowFramework_C_get_num_cameras_i_p(self.iptr, *argv, **kw)

    def get_camera_group(*argv,**kw):
        return self.WindowFramework_C_get_camera_group_p_p(self.iptr, *argv, **kw)

    def get_display_region_3d(*argv,**kw):
        return self.WindowFramework_C_get_display_region_3d_p_p(self.iptr, *argv, **kw)

    def stagger_animations(*argv,**kw):
        return self.WindowFramework_C_stagger_animations_v_p(self.iptr, *argv, **kw)

    def set_two_sided(*argv,**kw):
        return self.WindowFramework_C_set_two_sided_v_p(self.iptr, *argv, **kw)

    def set_one_sided_reverse(*argv,**kw):
        return self.WindowFramework_C_set_one_sided_reverse_v_p(self.iptr, *argv, **kw)

    def get_wireframe_filled(*argv,**kw):
        return self.WindowFramework_C_get_wireframe_filled_B_p(self.iptr, *argv, **kw)

    def get_pixel_2d(*argv,**kw):
        return self.WindowFramework_C_get_pixel_2d_p_p(self.iptr, *argv, **kw)

    def enable_keyboard(*argv,**kw):
        return self.WindowFramework_C_enable_keyboard_v_p(self.iptr, *argv, **kw)

    def split_window(*argv,**kw):
        return self.WindowFramework_C_split_window_p_p(self.iptr, *argv, **kw)

    def set_texture(*argv,**kw):
        return self.WindowFramework_C_set_texture_v_p(self.iptr, *argv, **kw)

    def get_anim_controls(*argv,**kw):
        return self.WindowFramework_C_get_anim_controls_B_p(self.iptr, *argv, **kw)

    def WindowFramework(*argv,**kw):
        return self.WindowFramework_C_WindowFramework_p_p(self.iptr, *argv, **kw)

    def get_shuttle_controls_font(*argv,**kw):
        return self.WindowFramework_C_get_shuttle_controls_font_p_v(self.iptr, *argv, **kw)

    def make_camera(*argv,**kw):
        return self.WindowFramework_C_make_camera_p_p(self.iptr, *argv, **kw)

    def get_graphics_window(*argv,**kw):
        return self.WindowFramework_C_get_graphics_window_p_p(self.iptr, *argv, **kw)

    def set_lighting(*argv,**kw):
        return self.WindowFramework_C_set_lighting_v_p(self.iptr, *argv, **kw)

    def center_trackball(*argv,**kw):
        return self.WindowFramework_C_center_trackball_v_p(self.iptr, *argv, **kw)

    def next_anim_control(*argv,**kw):
        return self.WindowFramework_C_next_anim_control_v_p(self.iptr, *argv, **kw)

    def get_two_sided(*argv,**kw):
        return self.WindowFramework_C_get_two_sided_B_p(self.iptr, *argv, **kw)

    def get_type(*argv,**kw):
        return self.WindowFramework_C_get_type_i_p(self.iptr, *argv, **kw)

    def get_graphics_output(*argv,**kw):
        return self.WindowFramework_C_get_graphics_output_p_p(self.iptr, *argv, **kw)

    def get_one_sided_reverse(*argv,**kw):
        return self.WindowFramework_C_get_one_sided_reverse_B_p(self.iptr, *argv, **kw)

    def set_perpixel(*argv,**kw):
        return self.WindowFramework_C_set_perpixel_v_p(self.iptr, *argv, **kw)

    def set_background_type(*argv,**kw):
        return self.WindowFramework_C_set_background_type_v_p(self.iptr, *argv, **kw)

    def get_display_region_2d(*argv,**kw):
        return self.WindowFramework_C_get_display_region_2d_p_p(self.iptr, *argv, **kw)

    def get_texture(*argv,**kw):
        return self.WindowFramework_C_get_texture_B_p(self.iptr, *argv, **kw)

    def setup_trackball(*argv,**kw):
        return self.WindowFramework_C_setup_trackball_v_p(self.iptr, *argv, **kw)

    def get_button_thrower(*argv,**kw):
        return self.WindowFramework_C_get_button_thrower_p_p(self.iptr, *argv, **kw)

    def get_background_type(*argv,**kw):
        return self.WindowFramework_C_get_background_type_p_p(self.iptr, *argv, **kw)

    def get_render_2d(*argv,**kw):
        return self.WindowFramework_C_get_render_2d_p_p(self.iptr, *argv, **kw)

    def force_init_type(*argv,**kw):
        return self.WindowFramework_C_force_init_type_i_p(self.iptr, *argv, **kw)

    def split_window_1(*argv,**kw):
        return self.WindowFramework_C_split_window_1_p_p(self.iptr, *argv, **kw)

    def get_perpixel(*argv,**kw):
        return self.WindowFramework_C_get_perpixel_B_p(self.iptr, *argv, **kw)

    def get_mouse(*argv,**kw):
        return self.WindowFramework_C_get_mouse_p_p(self.iptr, *argv, **kw)

    def get_camera(*argv,**kw):
        return self.WindowFramework_C_get_camera_p_p(self.iptr, *argv, **kw)

class Filename:

    lib = ffi.open("""libupanda3d_c.so""")

    Filename_C_get_basename_wo_extension_p_p = lib.func('p','Filename_C_get_basename_wo_extension_p_p','p')
    Filename_C_get_timestamp_p_p = lib.func('p','Filename_C_get_timestamp_p_p','p')
    Filename_C_has_hash_B_p = lib.func('B','Filename_C_has_hash_B_p','p')
    Filename_C_get_hash_i_p = lib.func('i','Filename_C_get_hash_i_p','p')
    Filename_C_make_true_case_B_p = lib.func('B','Filename_C_make_true_case_B_p','p')
    Filename_C_binary_filename_p_p = lib.func('p','Filename_C_binary_filename_p_p','p')
    Filename_C_substr_p_p = lib.func('p','Filename_C_substr_p_p','p')
    Filename_C_set_text_v_p = lib.func('v','Filename_C_set_text_v_p','p')
    Filename_C_to_os_short_name_p_p = lib.func('p','Filename_C_to_os_short_name_p_p','p')
    Filename_C_compare_to_i_p = lib.func('i','Filename_C_compare_to_i_p','p')
    Filename_C_set_extension_v_p = lib.func('v','Filename_C_set_extension_v_p','p')
    Filename_C_unlink_B_p = lib.func('B','Filename_C_unlink_B_p','p')
    Filename_C_dso_filename_p_p = lib.func('p','Filename_C_dso_filename_p_p','p')
    Filename_C_set_hash_to_end_v_p = lib.func('v','Filename_C_set_hash_to_end_v_p','p')
    Filename_C_is_directory_B_p = lib.func('B','Filename_C_is_directory_B_p','p')
    Filename_C_length_p_p = lib.func('p','Filename_C_length_p_p','p')
    Filename_C_is_local_B_p = lib.func('B','Filename_C_is_local_B_p','p')
    Filename_C_is_text_B_p = lib.func('B','Filename_C_is_text_B_p','p')
    Filename_C_binary_filename_1_p_p = lib.func('p','Filename_C_binary_filename_1_p_p','p')
    Filename_C_set_binary_v_p = lib.func('v','Filename_C_set_binary_v_p','p')
    Filename_C_set_basename_v_p = lib.func('v','Filename_C_set_basename_v_p','p')
    Filename_C_get_type_p_p = lib.func('p','Filename_C_get_type_p_p','p')
    Filename_C_find_on_searchpath_i_p = lib.func('i','Filename_C_find_on_searchpath_i_p','p')
    Filename_C_is_fully_qualified_B_p = lib.func('B','Filename_C_is_fully_qualified_B_p','p')
    Filename_C_mkdir_B_p = lib.func('B','Filename_C_mkdir_B_p','p')
    Filename_C_is_binary_B_p = lib.func('B','Filename_C_is_binary_B_p','p')
    Filename_C_set_filesystem_encoding_v_p = lib.func('v','Filename_C_set_filesystem_encoding_v_p','p')
    Filename_C_text_filename_1_p_p = lib.func('p','Filename_C_text_filename_1_p_p','p')
    Filename_C_get_home_directory_p_v = lib.func('p','Filename_C_get_home_directory_p_v','v')
    Filename_C_empty_B_p = lib.func('B','Filename_C_empty_B_p','p')
    Filename_C_extract_components_v_p = lib.func('v','Filename_C_extract_components_v_p','p')
    Filename_C_c_str_p_p = lib.func('p','Filename_C_c_str_p_p','p')
    Filename_C_is_regular_file_B_p = lib.func('B','Filename_C_is_regular_file_B_p','p')
    Filename_C_get_class_type_i_p = lib.func('i','Filename_C_get_class_type_i_p','p')
    Filename_C_to_os_generic_p_p = lib.func('p','Filename_C_to_os_generic_p_p','p')
    Filename_C_make_absolute_1_v_p = lib.func('v','Filename_C_make_absolute_1_v_p','p')
    Filename_C_open_read_1_B_p = lib.func('B','Filename_C_open_read_1_B_p','p')
    Filename_C_get_fullpath_w_p_p = lib.func('p','Filename_C_get_fullpath_w_p_p','p')
    Filename_C_make_dir_B_p = lib.func('B','Filename_C_make_dir_B_p','p')
    Filename_C_get_fullpath_p_p = lib.func('p','Filename_C_get_fullpath_p_p','p')
    Filename_C_make_canonical_B_p = lib.func('B','Filename_C_make_canonical_B_p','p')
    Filename_C_rmdir_B_p = lib.func('B','Filename_C_rmdir_B_p','p')
    Filename_C_get_filename_index_p_p = lib.func('p','Filename_C_get_filename_index_p_p','p')
    Filename_C_get_access_timestamp_p_p = lib.func('p','Filename_C_get_access_timestamp_p_p','p')
    Filename_C_set_dirname_v_p = lib.func('v','Filename_C_set_dirname_v_p','p')
    Filename_C_get_dirname_p_p = lib.func('p','Filename_C_get_dirname_p_p','p')
    Filename_C_open_append_B_p = lib.func('B','Filename_C_open_append_B_p','p')
    Filename_C_set_fullpath_wo_extension_v_p = lib.func('v','Filename_C_set_fullpath_wo_extension_v_p','p')
    Filename_C_standardize_v_p = lib.func('v','Filename_C_standardize_v_p','p')
    Filename_C_get_fullpath_wo_extension_p_p = lib.func('p','Filename_C_get_fullpath_wo_extension_p_p','p')
    Filename_C_set_pattern_v_p = lib.func('v','Filename_C_set_pattern_v_p','p')
    Filename_C_copy_to_B_p = lib.func('B','Filename_C_copy_to_B_p','p')
    Filename_C_get_common_appdata_directory_p_v = lib.func('p','Filename_C_get_common_appdata_directory_p_v','v')
    Filename_C_exists_B_p = lib.func('B','Filename_C_exists_B_p','p')
    Filename_C_chdir_B_p = lib.func('B','Filename_C_chdir_B_p','p')
    Filename_C_get_filesystem_encoding_p_p = lib.func('p','Filename_C_get_filesystem_encoding_p_p','p')
    Filename_C_scan_directory_B_p = lib.func('B','Filename_C_scan_directory_B_p','p')
    Filename_C_get_hash_to_end_p_p = lib.func('p','Filename_C_get_hash_to_end_p_p','p')
    Filename_C_init_type_v_p = lib.func('v','Filename_C_init_type_v_p','p')
    Filename_C_set_fullpath_v_p = lib.func('v','Filename_C_set_fullpath_v_p','p')
    Filename_C_text_filename_p_p = lib.func('p','Filename_C_text_filename_p_p','p')
    Filename_C_output_v_p = lib.func('v','Filename_C_output_v_p','p')
    Filename_C_make_absolute_v_p = lib.func('v','Filename_C_make_absolute_v_p','p')
    Filename_C_set_type_v_p = lib.func('v','Filename_C_set_type_v_p','p')
    Filename_C_to_os_long_name_p_p = lib.func('p','Filename_C_to_os_long_name_p_p','p')
    Filename_C_is_writable_B_p = lib.func('B','Filename_C_is_writable_B_p','p')
    Filename_C_get_extension_p_p = lib.func('p','Filename_C_get_extension_p_p','p')
    Filename_C_pattern_filename_p_p = lib.func('p','Filename_C_pattern_filename_p_p','p')
    Filename_C_set_basename_wo_extension_v_p = lib.func('v','Filename_C_set_basename_wo_extension_v_p','p')
    Filename_C_touch_B_p = lib.func('B','Filename_C_touch_B_p','p')
    Filename_C_Filename_3_p_p = lib.func('p','Filename_C_Filename_3_p_p','p')
    Filename_C_Filename_2_p_p = lib.func('p','Filename_C_Filename_2_p_p','p')
    Filename_C_Filename_1_p_p = lib.func('p','Filename_C_Filename_1_p_p','p')
    Filename_C_is_executable_B_p = lib.func('B','Filename_C_is_executable_B_p','p')
    Filename_C_open_append_1_B_p = lib.func('B','Filename_C_open_append_1_B_p','p')
    Filename_C_rename_to_B_p = lib.func('B','Filename_C_rename_to_B_p','p')
    Filename_C_get_file_size_p_p = lib.func('p','Filename_C_get_file_size_p_p','p')
    Filename_C_get_pattern_B_p = lib.func('B','Filename_C_get_pattern_B_p','p')
    Filename_C_Filename_4_p_p = lib.func('p','Filename_C_Filename_4_p_p','p')
    Filename_C_get_basename_p_p = lib.func('p','Filename_C_get_basename_p_p','p')
    Filename_C_open_read_append_1_B_p = lib.func('B','Filename_C_open_read_append_1_B_p','p')
    Filename_C_open_read_B_p = lib.func('B','Filename_C_open_read_B_p','p')
    Filename_C_is_binary_or_text_B_p = lib.func('B','Filename_C_is_binary_or_text_B_p','p')
    Filename_C_get_user_appdata_directory_p_v = lib.func('p','Filename_C_get_user_appdata_directory_p_v','v')
    Filename_C_open_read_append_B_p = lib.func('B','Filename_C_open_read_append_B_p','p')
    Filename_C_get_temp_directory_p_v = lib.func('p','Filename_C_get_temp_directory_p_v','v')
    Filename_C___nonzero___B_p = lib.func('B','Filename_C___nonzero___B_p','p')
    Filename_C_to_os_specific_p_p = lib.func('p','Filename_C_to_os_specific_p_p','p')
    Filename_C_to_os_specific_w_p_p = lib.func('p','Filename_C_to_os_specific_w_p_p','p')
    Filename_C_executable_filename_p_p = lib.func('p','Filename_C_executable_filename_p_p','p')

# variadic

    Filename_C_executable_filename_p_p = {
        1 : lib.func('p','Filename_C_Filename_p_p','p'),
        0 : lib.func('p','Filename_C_Filename_p_v',''),
    }
# c++ struct
    def get_basename_wo_extension(*argv,**kw):
        return self.Filename_C_get_basename_wo_extension_p_p(self.iptr, *argv, **kw)

    def get_timestamp(*argv,**kw):
        return self.Filename_C_get_timestamp_p_p(self.iptr, *argv, **kw)

    def has_hash(*argv,**kw):
        return self.Filename_C_has_hash_B_p(self.iptr, *argv, **kw)

    def get_hash(*argv,**kw):
        return self.Filename_C_get_hash_i_p(self.iptr, *argv, **kw)

    def make_true_case(*argv,**kw):
        return self.Filename_C_make_true_case_B_p(self.iptr, *argv, **kw)

    def binary_filename(*argv,**kw):
        return self.Filename_C_binary_filename_p_p(self.iptr, *argv, **kw)

    def substr(*argv,**kw):
        return self.Filename_C_substr_p_p(self.iptr, *argv, **kw)

    def set_text(*argv,**kw):
        return self.Filename_C_set_text_v_p(self.iptr, *argv, **kw)

    def to_os_short_name(*argv,**kw):
        return self.Filename_C_to_os_short_name_p_p(self.iptr, *argv, **kw)

    def compare_to(*argv,**kw):
        return self.Filename_C_compare_to_i_p(self.iptr, *argv, **kw)

    def set_extension(*argv,**kw):
        return self.Filename_C_set_extension_v_p(self.iptr, *argv, **kw)

    def unlink(*argv,**kw):
        return self.Filename_C_unlink_B_p(self.iptr, *argv, **kw)

    def dso_filename(*argv,**kw):
        return self.Filename_C_dso_filename_p_p(self.iptr, *argv, **kw)

    def set_hash_to_end(*argv,**kw):
        return self.Filename_C_set_hash_to_end_v_p(self.iptr, *argv, **kw)

    def is_directory(*argv,**kw):
        return self.Filename_C_is_directory_B_p(self.iptr, *argv, **kw)

    def length(*argv,**kw):
        return self.Filename_C_length_p_p(self.iptr, *argv, **kw)

    def is_local(*argv,**kw):
        return self.Filename_C_is_local_B_p(self.iptr, *argv, **kw)

    def is_text(*argv,**kw):
        return self.Filename_C_is_text_B_p(self.iptr, *argv, **kw)

    def binary_filename_1(*argv,**kw):
        return self.Filename_C_binary_filename_1_p_p(self.iptr, *argv, **kw)

    def set_binary(*argv,**kw):
        return self.Filename_C_set_binary_v_p(self.iptr, *argv, **kw)

    def set_basename(*argv,**kw):
        return self.Filename_C_set_basename_v_p(self.iptr, *argv, **kw)

    def get_type(*argv,**kw):
        return self.Filename_C_get_type_p_p(self.iptr, *argv, **kw)

    def find_on_searchpath(*argv,**kw):
        return self.Filename_C_find_on_searchpath_i_p(self.iptr, *argv, **kw)

    def is_fully_qualified(*argv,**kw):
        return self.Filename_C_is_fully_qualified_B_p(self.iptr, *argv, **kw)

    def mkdir(*argv,**kw):
        return self.Filename_C_mkdir_B_p(self.iptr, *argv, **kw)

    def is_binary(*argv,**kw):
        return self.Filename_C_is_binary_B_p(self.iptr, *argv, **kw)

    def set_filesystem_encoding(*argv,**kw):
        return self.Filename_C_set_filesystem_encoding_v_p(self.iptr, *argv, **kw)

    def text_filename_1(*argv,**kw):
        return self.Filename_C_text_filename_1_p_p(self.iptr, *argv, **kw)

    def get_home_directory(*argv,**kw):
        return self.Filename_C_get_home_directory_p_v(self.iptr, *argv, **kw)

    def empty(*argv,**kw):
        return self.Filename_C_empty_B_p(self.iptr, *argv, **kw)

    def extract_components(*argv,**kw):
        return self.Filename_C_extract_components_v_p(self.iptr, *argv, **kw)

    def c_str(*argv,**kw):
        return self.Filename_C_c_str_p_p(self.iptr, *argv, **kw)

    def is_regular_file(*argv,**kw):
        return self.Filename_C_is_regular_file_B_p(self.iptr, *argv, **kw)

    def get_class_type(*argv,**kw):
        return self.Filename_C_get_class_type_i_p(self.iptr, *argv, **kw)

    def to_os_generic(*argv,**kw):
        return self.Filename_C_to_os_generic_p_p(self.iptr, *argv, **kw)

    def make_absolute_1(*argv,**kw):
        return self.Filename_C_make_absolute_1_v_p(self.iptr, *argv, **kw)

    def open_read_1(*argv,**kw):
        return self.Filename_C_open_read_1_B_p(self.iptr, *argv, **kw)

    def get_fullpath_w(*argv,**kw):
        return self.Filename_C_get_fullpath_w_p_p(self.iptr, *argv, **kw)

    def make_dir(*argv,**kw):
        return self.Filename_C_make_dir_B_p(self.iptr, *argv, **kw)

    def get_fullpath(*argv,**kw):
        return self.Filename_C_get_fullpath_p_p(self.iptr, *argv, **kw)

    def make_canonical(*argv,**kw):
        return self.Filename_C_make_canonical_B_p(self.iptr, *argv, **kw)

    def rmdir(*argv,**kw):
        return self.Filename_C_rmdir_B_p(self.iptr, *argv, **kw)

    def get_filename_index(*argv,**kw):
        return self.Filename_C_get_filename_index_p_p(self.iptr, *argv, **kw)

    def get_access_timestamp(*argv,**kw):
        return self.Filename_C_get_access_timestamp_p_p(self.iptr, *argv, **kw)

    def set_dirname(*argv,**kw):
        return self.Filename_C_set_dirname_v_p(self.iptr, *argv, **kw)

    def get_dirname(*argv,**kw):
        return self.Filename_C_get_dirname_p_p(self.iptr, *argv, **kw)

    def open_append(*argv,**kw):
        return self.Filename_C_open_append_B_p(self.iptr, *argv, **kw)

    def set_fullpath_wo_extension(*argv,**kw):
        return self.Filename_C_set_fullpath_wo_extension_v_p(self.iptr, *argv, **kw)

    def standardize(*argv,**kw):
        return self.Filename_C_standardize_v_p(self.iptr, *argv, **kw)

    def get_fullpath_wo_extension(*argv,**kw):
        return self.Filename_C_get_fullpath_wo_extension_p_p(self.iptr, *argv, **kw)

    def set_pattern(*argv,**kw):
        return self.Filename_C_set_pattern_v_p(self.iptr, *argv, **kw)

    def copy_to(*argv,**kw):
        return self.Filename_C_copy_to_B_p(self.iptr, *argv, **kw)

    def get_common_appdata_directory(*argv,**kw):
        return self.Filename_C_get_common_appdata_directory_p_v(self.iptr, *argv, **kw)

    def exists(*argv,**kw):
        return self.Filename_C_exists_B_p(self.iptr, *argv, **kw)

    def chdir(*argv,**kw):
        return self.Filename_C_chdir_B_p(self.iptr, *argv, **kw)

    def get_filesystem_encoding(*argv,**kw):
        return self.Filename_C_get_filesystem_encoding_p_p(self.iptr, *argv, **kw)

    def Filename(*argv,**kw):
        return variadic_call(self, Filename_C_get_filesystem_encoding_p_p, *argv, **kw)

    def scan_directory(*argv,**kw):
        return self.Filename_C_scan_directory_B_p(self.iptr, *argv, **kw)

    def get_hash_to_end(*argv,**kw):
        return self.Filename_C_get_hash_to_end_p_p(self.iptr, *argv, **kw)

    def init_type(*argv,**kw):
        return self.Filename_C_init_type_v_p(self.iptr, *argv, **kw)

    def set_fullpath(*argv,**kw):
        return self.Filename_C_set_fullpath_v_p(self.iptr, *argv, **kw)

    def text_filename(*argv,**kw):
        return self.Filename_C_text_filename_p_p(self.iptr, *argv, **kw)

    def output(*argv,**kw):
        return self.Filename_C_output_v_p(self.iptr, *argv, **kw)

    def make_absolute(*argv,**kw):
        return self.Filename_C_make_absolute_v_p(self.iptr, *argv, **kw)

    def set_type(*argv,**kw):
        return self.Filename_C_set_type_v_p(self.iptr, *argv, **kw)

    def to_os_long_name(*argv,**kw):
        return self.Filename_C_to_os_long_name_p_p(self.iptr, *argv, **kw)

    def is_writable(*argv,**kw):
        return self.Filename_C_is_writable_B_p(self.iptr, *argv, **kw)

    def get_extension(*argv,**kw):
        return self.Filename_C_get_extension_p_p(self.iptr, *argv, **kw)

    def pattern_filename(*argv,**kw):
        return self.Filename_C_pattern_filename_p_p(self.iptr, *argv, **kw)

    def set_basename_wo_extension(*argv,**kw):
        return self.Filename_C_set_basename_wo_extension_v_p(self.iptr, *argv, **kw)

    def touch(*argv,**kw):
        return self.Filename_C_touch_B_p(self.iptr, *argv, **kw)

    def Filename_3(*argv,**kw):
        return self.Filename_C_Filename_3_p_p(self.iptr, *argv, **kw)

    def Filename_2(*argv,**kw):
        return self.Filename_C_Filename_2_p_p(self.iptr, *argv, **kw)

    def Filename_1(*argv,**kw):
        return self.Filename_C_Filename_1_p_p(self.iptr, *argv, **kw)

    def is_executable(*argv,**kw):
        return self.Filename_C_is_executable_B_p(self.iptr, *argv, **kw)

    def open_append_1(*argv,**kw):
        return self.Filename_C_open_append_1_B_p(self.iptr, *argv, **kw)

    def rename_to(*argv,**kw):
        return self.Filename_C_rename_to_B_p(self.iptr, *argv, **kw)

    def get_file_size(*argv,**kw):
        return self.Filename_C_get_file_size_p_p(self.iptr, *argv, **kw)

    def get_pattern(*argv,**kw):
        return self.Filename_C_get_pattern_B_p(self.iptr, *argv, **kw)

    def Filename_4(*argv,**kw):
        return self.Filename_C_Filename_4_p_p(self.iptr, *argv, **kw)

    def get_basename(*argv,**kw):
        return self.Filename_C_get_basename_p_p(self.iptr, *argv, **kw)

    def open_read_append_1(*argv,**kw):
        return self.Filename_C_open_read_append_1_B_p(self.iptr, *argv, **kw)

    def open_read(*argv,**kw):
        return self.Filename_C_open_read_B_p(self.iptr, *argv, **kw)

    def is_binary_or_text(*argv,**kw):
        return self.Filename_C_is_binary_or_text_B_p(self.iptr, *argv, **kw)

    def get_user_appdata_directory(*argv,**kw):
        return self.Filename_C_get_user_appdata_directory_p_v(self.iptr, *argv, **kw)

    def open_read_append(*argv,**kw):
        return self.Filename_C_open_read_append_B_p(self.iptr, *argv, **kw)

    def get_temp_directory(*argv,**kw):
        return self.Filename_C_get_temp_directory_p_v(self.iptr, *argv, **kw)

    def __nonzero__(*argv,**kw):
        return self.Filename_C___nonzero___B_p(self.iptr, *argv, **kw)

    def to_os_specific(*argv,**kw):
        return self.Filename_C_to_os_specific_p_p(self.iptr, *argv, **kw)

    def to_os_specific_w(*argv,**kw):
        return self.Filename_C_to_os_specific_w_p_p(self.iptr, *argv, **kw)

    def executable_filename(*argv,**kw):
        return self.Filename_C_executable_filename_p_p(self.iptr, *argv, **kw)

class Engine:

    lib = ffi.open("""libupanda3d_c.so""")

    Engine_C_set_framework_v_p = lib.func('v','Engine_C_set_framework_v_p','p')
    Engine_C_build_v_p = lib.func('v','Engine_C_build_v_p','p')
    Engine_C_get_wframe_p_p = lib.func('p','Engine_C_get_wframe_p_p','p')
    Engine_C_load_model_p_p = lib.func('p','Engine_C_load_model_p_p','p')
    Engine_C_attach_v_p = lib.func('v','Engine_C_attach_v_p','p')
    Engine_C_HelloEngine_i_p = lib.func('i','Engine_C_HelloEngine_i_p','p')
    Engine_C_step_v_p = lib.func('v','Engine_C_step_v_p','p')
    Engine_C_get_framework_p_p = lib.func('p','Engine_C_get_framework_p_p','p')

# variadic

    Engine_C_get_framework_p_p = {
        1 : lib.func('p','Engine_C_Engine_p_p','p'),
        0 : lib.func('p','Engine_C_Engine_p_v',''),
    }
# c++ struct
    def set_framework(*argv,**kw):
        return self.Engine_C_set_framework_v_p(self.iptr, *argv, **kw)

    def build(*argv,**kw):
        return self.Engine_C_build_v_p(self.iptr, *argv, **kw)

    def get_wframe(*argv,**kw):
        return self.Engine_C_get_wframe_p_p(self.iptr, *argv, **kw)

    def load_model(*argv,**kw):
        return self.Engine_C_load_model_p_p(self.iptr, *argv, **kw)

    def attach(*argv,**kw):
        return self.Engine_C_attach_v_p(self.iptr, *argv, **kw)

    def HelloEngine(*argv,**kw):
        return self.Engine_C_HelloEngine_i_p(self.iptr, *argv, **kw)

    def step(*argv,**kw):
        return self.Engine_C_step_v_p(self.iptr, *argv, **kw)

    def Engine(*argv,**kw):
        return variadic_call(self, Engine_C_step_v_p, *argv, **kw)

    def get_framework(*argv,**kw):
        return self.Engine_C_get_framework_p_p(self.iptr, *argv, **kw)

