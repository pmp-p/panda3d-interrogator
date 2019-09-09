# upy

import sys


if not '.' in sys.path: sys.path.insert(0,'.')
import interrogator.uplusplus as cxx

extern = cxx.cstructs.decl.append
extern('ConfigPage') # 
extern('Engine') # 
extern('Filename') # 
extern('GeomEnums') # 
extern('LVecBase3f') # 
extern('LinkedListNode') # 
extern('MemoryBase') # 
extern('NodePath') # 
extern('NodePathCollection') # 
extern('PandaFramework') # 
extern('PandaSystem') # 
extern('GeomVertexWriter') # GeomEnums
extern('Namable') # MemoryBase
extern('ReferenceCount') # MemoryBase
extern('TypedObject') # MemoryBase
extern('TypedWritable') # TypedObject
extern('TypedReferenceCount') # TypedObject, ReferenceCount
extern('Thread') # TypedReferenceCount, Namable
extern('TypedWritableReferenceCount') # TypedWritable, ReferenceCount
extern('GeomVertexFormat') # TypedWritableReferenceCount, GeomEnums
extern('WindowFramework') # TypedWritableReferenceCount
extern('InternalName') # TypedWritableReferenceCount
extern('CachedTypedWritableReferenceCount') # TypedWritableReferenceCount
extern('CopyOnWriteObject') # CachedTypedWritableReferenceCount
extern('GeomVertexData') # CopyOnWriteObject, GeomEnums
extern('GeomPrimitive') # CopyOnWriteObject, GeomEnums
extern('GeomTriangles') # GeomPrimitive
extern('GeomT') # GeomTriangles
extern('Geom') # CopyOnWriteObject, GeomEnums
extern('PandaNode') # TypedWritableReferenceCount, Namable, LinkedListNode
extern('LensNode') # PandaNode
extern('Camera') # LensNode
extern('GeomNode') # PandaNode
del extern

# enum NotifySeverity

NS_debug = const(2)
NS_error = const(5)
NS_fatal = const(6)
NS_info = const(3)
NS_spam = const(1)
NS_unspecified = const(0)
NS_warning = const(4)


# enum AutoTextureScale

ATS_down = const(1)
ATS_none = const(0)
ATS_pad = const(3)
ATS_unspecified = const(4)
ATS_up = const(2)


# enum TiXmlEncoding

TIXML_ENCODING_LEGACY = const(2)
TIXML_ENCODING_UNKNOWN = const(0)
TIXML_ENCODING_UTF8 = const(1)


# enum LODNodeType

LNT_fade = const(1)
LNT_pop = const(0)


# enum ThreadPriority

TP_high = const(2)
TP_low = const(0)
TP_normal = const(1)
TP_urgent = const(3)


# enum PointerType

eraser = const(4)
finger = const(2)
mouse = const(1)
stylus = const(3)
unknown = const(0)


# enum CoordinateSystem

CS_default = const(0)
CS_invalid = const(5)
CS_yup_left = const(4)
CS_yup_right = const(2)
CS_zup_left = const(3)
CS_zup_right = const(1)


# enum ColorSpace

CS_linear = const(1)
CS_sRGB = const(2)
CS_scRGB = const(3)
CS_unspecified = const(0)


# enum ErrorUtilCode

EU_eof = const(6)
EU_error_abort = const(-1)
EU_error_file_empty = const(-2)
EU_error_file_invalid = const(-3)
EU_error_http_gateway_timeout = const(-71)
EU_error_http_proxy_authentication = const(-73)
EU_error_http_server_timeout = const(-70)
EU_error_http_service_unavailable = const(-72)
EU_error_invalid_checksum = const(-4)
EU_error_network_buffer_overflow = const(-41)
EU_error_network_dead = const(-30)
EU_error_network_disconnected = const(-32)
EU_error_network_disconnected_locally = const(-40)
EU_error_network_disk_quota_exceeded = const(-42)
EU_error_network_no_data = const(-34)
EU_error_network_remote_host_disconnected = const(-50)
EU_error_network_remote_host_down = const(-51)
EU_error_network_remote_host_no_response = const(-54)
EU_error_network_remote_host_not_found = const(-53)
EU_error_network_remote_host_unreachable = const(-52)
EU_error_network_timeout = const(-33)
EU_error_network_unreachable = const(-31)
EU_error_write_disk_fault = const(-66)
EU_error_write_disk_full = const(-63)
EU_error_write_disk_not_found = const(-64)
EU_error_write_disk_sector_not_found = const(-65)
EU_error_write_file_rename = const(-67)
EU_error_write_out_of_files = const(-60)
EU_error_write_out_of_memory = const(-61)
EU_error_write_sharing_violation = const(-62)
EU_error_zlib = const(-80)
EU_http_redirect = const(7)
EU_network_no_data = const(5)
EU_ok = const(2)
EU_success = const(1)
EU_write = const(3)
EU_write_ram = const(4)



class ConfigPage(cxx.cplusplus):

    c = cxx.cstructs()
    c.register("ConfigPage", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['get_default_page'] = [
        ('s', 0, 0, ('p', 'ConfigPage_C_get_default_page_p_v', ''), []),
    ]
    c.ct['get_local_page'] = [
        ('s', 0, 0, ('p', 'ConfigPage_C_get_local_page_p_v', ''), []),
    ]

    @classmethod
    def get_default_page(cls, *args,**kw):
        return ( cls.c.get('get_default_page', None) or cls.c.call(ConfigPage, 'get_default_page', None) )(*args,**kw)

    @classmethod
    def get_local_page(cls, *args,**kw):
        return ( cls.c.get('get_local_page', None) or cls.c.call(ConfigPage, 'get_local_page', None) )(*args,**kw)

    # instance method type calls

    c.ct['clear'] = [
        ('d', 'v', 0, ('v', 'ConfigPage_C_clear_v_p', 'p'), []),
    ]
    c.ct['delete_declaration'] = [
        ('d', 'B', 1, ('B', 'ConfigPage_C_delete_declaration_B_pp', 'pp'), ['ConfigDeclaration*']),
    ]
    c.ct['get_declaration'] = [
        ('d', 'p', 1, ('p', 'ConfigPage_C_get_declaration_p_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['get_name'] = [
        ('d', 's', 0, ('s', 'ConfigPage_C_get_name_s_p', 'p'), []),
    ]
    c.ct['get_num_declarations'] = [
        ('d', 'p', 0, ('p', 'ConfigPage_C_get_num_declarations_p_p', 'p'), []),
    ]
    c.ct['get_page_seq'] = [
        ('d', 'i', 0, ('i', 'ConfigPage_C_get_page_seq_i_p', 'p'), []),
    ]
    c.ct['get_signature'] = [
        ('d', 's', 0, ('s', 'ConfigPage_C_get_signature_s_p', 'p'), []),
    ]
    c.ct['get_sort'] = [
        ('d', 'i', 0, ('i', 'ConfigPage_C_get_sort_i_p', 'p'), []),
    ]
    c.ct['get_string_value'] = [
        ('d', 's', 1, ('s', 'ConfigPage_C_get_string_value_s_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['get_trust_level'] = [
        ('d', 'i', 0, ('i', 'ConfigPage_C_get_trust_level_i_p', 'p'), []),
    ]
    c.ct['get_variable_name'] = [
        ('d', 's', 1, ('s', 'ConfigPage_C_get_variable_name_s_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['is_implicit'] = [
        ('d', 'B', 0, ('B', 'ConfigPage_C_is_implicit_B_p', 'p'), []),
    ]
    c.ct['is_special'] = [
        ('d', 'B', 0, ('B', 'ConfigPage_C_is_special_B_p', 'p'), []),
    ]
    c.ct['is_variable_used'] = [
        ('d', 'B', 1, ('B', 'ConfigPage_C_is_variable_used_B_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['make_declaration'] = [
        ('d', 'p', 2, ('p', 'ConfigPage_C_make_declaration_p_pps', 'pps'), ['ConfigVariableCore*', 'std::string const&']),
        ('d', 'p', 2, ('p', 'ConfigPage_C_make_declaration_p_pss', 'pss'), ['std::string const&', 'std::string const&']),
    ]
    c.ct['modify_declaration'] = [
        ('d', 'p', 1, ('p', 'ConfigPage_C_modify_declaration_p_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'ConfigPage_C_output_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['output_brief_signature'] = [
        ('d', 'v', 1, ('v', 'ConfigPage_C_output_brief_signature_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['read_encrypted_prc'] = [
        ('d', 'B', 2, ('B', 'ConfigPage_C_read_encrypted_prc_B_pps', 'pps'), ['std::istream&', 'std::string const&']),
    ]
    c.ct['read_prc'] = [
        ('d', 'B', 1, ('B', 'ConfigPage_C_read_prc_B_pp', 'pp'), ['std::istream&']),
    ]
    c.ct['set_sort'] = [
        ('d', 'v', 1, ('v', 'ConfigPage_C_set_sort_v_pi', 'pi'), ['int']),
    ]
    c.ct['set_trust_level'] = [
        ('d', 'v', 1, ('v', 'ConfigPage_C_set_trust_level_v_pi', 'pi'), ['int']),
    ]
    c.ct['write'] = [
        ('d', 'v', 1, ('v', 'ConfigPage_C_write_v_pp', 'pp'), ['std::ostream&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(ConfigPage, attr, self)

ConfigPage.c.link(ConfigPage)



class Engine(cxx.cplusplus):

    c = cxx.cstructs()
    c.register("Engine", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 1, 0, ('p', 'Engine_C_ctor_p_v', ''), []),
        ('s', 1, 1, ('p', 'Engine_C_ctor_p_p', 'p'), ['Engine const&']),
    ]

    # classmethod type calls

    c.ct['get_version_string'] = [
        ('s', 's', 0, ('s', 'Engine_C_get_version_string_s_v', ''), []),
    ]
    c.ct['is_alive'] = [
        ('s', 'i', 0, ('i', 'Engine_C_is_alive_i_v', ''), []),
    ]
    c.ct['stop'] = [
        ('s', 'v', 0, ('v', 'Engine_C_stop_v_v', ''), []),
    ]

    @classmethod
    def get_version_string(cls, *args,**kw):
        return ( cls.c.get('get_version_string', None) or cls.c.call(Engine, 'get_version_string', None) )(*args,**kw)

    @classmethod
    def is_alive(cls, *args,**kw):
        return ( cls.c.get('is_alive', None) or cls.c.call(Engine, 'is_alive', None) )(*args,**kw)

    @classmethod
    def stop(cls, *args,**kw):
        return ( cls.c.get('stop', None) or cls.c.call(Engine, 'stop', None) )(*args,**kw)

    # instance method type calls

    c.ct['HelloEngine'] = [
        ('d', 'i', 0, ('i', 'Engine_C_HelloEngine_i_p', 'p'), []),
    ]
    c.ct['add_primitive'] = [
        ('d', 'v', 2, ('v', 'Engine_C_add_primitive_v_ppp', 'ppp'), ['Geom*', 'GeomTriangles*']),
    ]
    c.ct['attach'] = [
        ('d', 'v', 1, ('v', 'Engine_C_attach_v_pp', 'pp'), ['NodePath*']),
    ]
    c.ct['build'] = [
        ('d', 'v', 0, ('v', 'Engine_C_build_v_p', 'p'), []),
    ]
    c.ct['casetest'] = [
        ('d', 'i', 3, ('i', 'Engine_C_casetest_i_pisB', 'pisB'), ['int', 'std::string', 'bool']),
    ]
    c.ct['close_primitive'] = [
        ('d', 'v', 1, ('v', 'Engine_C_close_primitive_v_pp', 'pp'), ['GeomTriangles*']),
    ]
    c.ct['dtor'] = [
        ('d', 'v', 0, ('v', 'Engine_C_dtor_v_p', 'p'), []),
    ]
    c.ct['get_framework'] = [
        ('d', 9, 0, ('p', 'Engine_C_get_framework_p_p', 'p'), []),
    ]
    c.ct['get_wframe'] = [
        ('d', 20, 0, ('p', 'Engine_C_get_wframe_p_p', 'p'), []),
    ]
    c.ct['load_model'] = [
        ('d', 7, 1, ('p', 'Engine_C_load_model_p_ps', 'ps'), ['char const*']),
    ]
    c.ct['new_GeomTriangles'] = [
        ('d', 26, 0, ('p', 'Engine_C_new_GeomTriangles_p_p', 'p'), []),
    ]
    c.ct['new_GeomVertexWriter'] = [
        ('d', 11, 2, ('p', 'Engine_C_new_GeomVertexWriter_p_pps', 'pps'), ['GeomVertexData*', 'char const*']),
    ]
    c.ct['set_framework'] = [
        ('d', 'v', 1, ('v', 'Engine_C_set_framework_v_pp', 'pp'), ['PandaFramework*']),
    ]
    c.ct['step'] = [
        ('d', 'v', 0, ('v', 'Engine_C_step_v_p', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(Engine, attr, self)

Engine.c.link(Engine)



class Filename(cxx.cplusplus):

    c = cxx.cstructs()
    c.register("Filename", "upanda3d", """libupanda3d_cni.so""")

    # enum Flags

    F_binary = const(16)
    F_pattern = const(64)
    F_text = const(32)
    F_type = const(15)


    # enum Type

    T_dso = const(1)
    T_executable = const(2)
    T_general = const(0)


    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 2, 0, ('p', 'Filename_C_ctor_p_v', ''), []),
        ('s', 2, 1, ('p', 'Filename_C_ctor_p_p', 'p'), ['Filename&&']),
        ('s', 2, 1, ('p', 'Filename_C_ctor_p_p_1_p_p', 'p'), ['Filename const&']),
        ('s', 2, 2, ('p', 'Filename_C_ctor_p_pp', 'pp'), ['Filename const&', 'Filename const&']),
        ('s', 2, 1, ('p', 'Filename_C_ctor_p_s', 's'), ['char const*']),
        ('s', 2, 1, ('p', 'Filename_C_ctor_p_s_1_p_s', 's'), ['std::string const&']),
        ('s', 2, 1, ('p', 'Filename_C_ctor_p_p_1_p_p_2_p_p', 'p'), ['std::wstring const&']),
    ]

    # classmethod type calls

    c.ct['binary_filename'] = [
        ('s', 2, 1, ('p', 'Filename_C_binary_filename_p_p', 'p'), ['Filename const&']),
        ('s', 2, 1, ('p', 'Filename_C_binary_filename_p_s', 's'), ['std::string const&']),
    ]
    c.ct['dso_filename'] = [
        ('s', 2, 1, ('p', 'Filename_C_dso_filename_p_s', 's'), ['std::string const&']),
    ]
    c.ct['executable_filename'] = [
        ('s', 2, 1, ('p', 'Filename_C_executable_filename_p_s', 's'), ['std::string const&']),
    ]
    c.ct['expand_from'] = [
        ('s', 2, 2, ('p', 'Filename_C_expand_from_p_sp', 'sp'), ['std::string const&', 'Filename::Type']),
        ('s', 2, 1, ('p', 'Filename_C_expand_from_p_s', 's'), ['std::string const&']),
    ]
    c.ct['from_os_specific'] = [
        ('s', 2, 2, ('p', 'Filename_C_from_os_specific_p_sp', 'sp'), ['std::string const&', 'Filename::Type']),
        ('s', 2, 1, ('p', 'Filename_C_from_os_specific_p_s', 's'), ['std::string const&']),
    ]
    c.ct['from_os_specific_w'] = [
        ('s', 2, 2, ('p', 'Filename_C_from_os_specific_w_p_pp', 'pp'), ['std::wstring const&', 'Filename::Type']),
        ('s', 2, 1, ('p', 'Filename_C_from_os_specific_w_p_p', 'p'), ['std::wstring const&']),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'Filename_C_get_class_type_i_v', ''), []),
    ]
    c.ct['get_common_appdata_directory'] = [
        ('s', 2, 0, ('p', 'Filename_C_get_common_appdata_directory_p_v', ''), []),
    ]
    c.ct['get_filesystem_encoding'] = [
        ('s', 'p', 0, ('p', 'Filename_C_get_filesystem_encoding_p_v', ''), []),
    ]
    c.ct['get_home_directory'] = [
        ('s', 2, 0, ('p', 'Filename_C_get_home_directory_p_v', ''), []),
    ]
    c.ct['get_temp_directory'] = [
        ('s', 2, 0, ('p', 'Filename_C_get_temp_directory_p_v', ''), []),
    ]
    c.ct['get_user_appdata_directory'] = [
        ('s', 2, 0, ('p', 'Filename_C_get_user_appdata_directory_p_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'Filename_C_init_type_v_v', ''), []),
    ]
    c.ct['pattern_filename'] = [
        ('s', 2, 1, ('p', 'Filename_C_pattern_filename_p_s', 's'), ['std::string const&']),
    ]
    c.ct['set_filesystem_encoding'] = [
        ('s', 'v', 1, ('v', 'Filename_C_set_filesystem_encoding_v_p', 'p'), ['TextEncoder::Encoding']),
    ]
    c.ct['temporary'] = [
        ('s', 2, 4, ('p', 'Filename_C_temporary_p_sssp', 'sssp'), ['std::string const&', 'std::string const&', 'std::string const&', 'Filename::Type']),
        ('s', 2, 3, ('p', 'Filename_C_temporary_p_sss', 'sss'), ['std::string const&', 'std::string const&', 'std::string const&']),
        ('s', 2, 2, ('p', 'Filename_C_temporary_p_ss', 'ss'), ['std::string const&', 'std::string const&']),
    ]
    c.ct['text_filename'] = [
        ('s', 2, 1, ('p', 'Filename_C_text_filename_p_p', 'p'), ['Filename const&']),
        ('s', 2, 1, ('p', 'Filename_C_text_filename_p_s', 's'), ['std::string const&']),
    ]

    @classmethod
    def binary_filename(cls, *args,**kw):
        return ( cls.c.get('binary_filename', None) or cls.c.call(Filename, 'binary_filename', None) )(*args,**kw)

    @classmethod
    def dso_filename(cls, *args,**kw):
        return ( cls.c.get('dso_filename', None) or cls.c.call(Filename, 'dso_filename', None) )(*args,**kw)

    @classmethod
    def executable_filename(cls, *args,**kw):
        return ( cls.c.get('executable_filename', None) or cls.c.call(Filename, 'executable_filename', None) )(*args,**kw)

    @classmethod
    def expand_from(cls, *args,**kw):
        return ( cls.c.get('expand_from', None) or cls.c.call(Filename, 'expand_from', None) )(*args,**kw)

    @classmethod
    def from_os_specific(cls, *args,**kw):
        return ( cls.c.get('from_os_specific', None) or cls.c.call(Filename, 'from_os_specific', None) )(*args,**kw)

    @classmethod
    def from_os_specific_w(cls, *args,**kw):
        return ( cls.c.get('from_os_specific_w', None) or cls.c.call(Filename, 'from_os_specific_w', None) )(*args,**kw)

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(Filename, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_common_appdata_directory(cls, *args,**kw):
        return ( cls.c.get('get_common_appdata_directory', None) or cls.c.call(Filename, 'get_common_appdata_directory', None) )(*args,**kw)

    @classmethod
    def get_filesystem_encoding(cls, *args,**kw):
        return ( cls.c.get('get_filesystem_encoding', None) or cls.c.call(Filename, 'get_filesystem_encoding', None) )(*args,**kw)

    @classmethod
    def get_home_directory(cls, *args,**kw):
        return ( cls.c.get('get_home_directory', None) or cls.c.call(Filename, 'get_home_directory', None) )(*args,**kw)

    @classmethod
    def get_temp_directory(cls, *args,**kw):
        return ( cls.c.get('get_temp_directory', None) or cls.c.call(Filename, 'get_temp_directory', None) )(*args,**kw)

    @classmethod
    def get_user_appdata_directory(cls, *args,**kw):
        return ( cls.c.get('get_user_appdata_directory', None) or cls.c.call(Filename, 'get_user_appdata_directory', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(Filename, 'init_type', None) )(*args,**kw)

    @classmethod
    def pattern_filename(cls, *args,**kw):
        return ( cls.c.get('pattern_filename', None) or cls.c.call(Filename, 'pattern_filename', None) )(*args,**kw)

    @classmethod
    def set_filesystem_encoding(cls, *args,**kw):
        return ( cls.c.get('set_filesystem_encoding', None) or cls.c.call(Filename, 'set_filesystem_encoding', None) )(*args,**kw)

    @classmethod
    def temporary(cls, *args,**kw):
        return ( cls.c.get('temporary', None) or cls.c.call(Filename, 'temporary', None) )(*args,**kw)

    @classmethod
    def text_filename(cls, *args,**kw):
        return ( cls.c.get('text_filename', None) or cls.c.call(Filename, 'text_filename', None) )(*args,**kw)

    # instance method type calls

    c.ct['__nonzero__'] = [
        ('d', 'B', 0, ('B', 'Filename_C___nonzero___B_p', 'p'), []),
    ]
    c.ct['c_str'] = [
        ('d', 's', 0, ('s', 'Filename_C_c_str_s_p', 'p'), []),
    ]
    c.ct['chdir'] = [
        ('d', 'B', 0, ('B', 'Filename_C_chdir_B_p', 'p'), []),
    ]
    c.ct['compare_timestamps'] = [
        ('d', 'i', 3, ('i', 'Filename_C_compare_timestamps_i_ppBB', 'ppBB'), ['Filename const&', 'bool', 'bool']),
        ('d', 'i', 2, ('i', 'Filename_C_compare_timestamps_i_ppB', 'ppB'), ['Filename const&', 'bool']),
        ('d', 'i', 1, ('i', 'Filename_C_compare_timestamps_i_pp', 'pp'), ['Filename const&']),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'Filename_C_compare_to_i_pp', 'pp'), ['Filename const&']),
    ]
    c.ct['copy_to'] = [
        ('d', 'B', 1, ('B', 'Filename_C_copy_to_B_pp', 'pp'), ['Filename const&']),
    ]
    c.ct['empty'] = [
        ('d', 'B', 0, ('B', 'Filename_C_empty_B_p', 'p'), []),
    ]
    c.ct['exists'] = [
        ('d', 'B', 0, ('B', 'Filename_C_exists_B_p', 'p'), []),
    ]
    c.ct['extract_components'] = [
        ('d', 'v', 1, ('v', 'Filename_C_extract_components_v_pp', 'pp'), ['vector_string&']),
    ]
    c.ct['find_on_searchpath'] = [
        ('d', 'i', 1, ('i', 'Filename_C_find_on_searchpath_i_pp', 'pp'), ['DSearchPath const&']),
    ]
    c.ct['get_access_timestamp'] = [
        ('d', 'p', 0, ('p', 'Filename_C_get_access_timestamp_p_p', 'p'), []),
    ]
    c.ct['get_basename'] = [
        ('d', 's', 0, ('s', 'Filename_C_get_basename_s_p', 'p'), []),
    ]
    c.ct['get_basename_wo_extension'] = [
        ('d', 's', 0, ('s', 'Filename_C_get_basename_wo_extension_s_p', 'p'), []),
    ]
    c.ct['get_dirname'] = [
        ('d', 's', 0, ('s', 'Filename_C_get_dirname_s_p', 'p'), []),
    ]
    c.ct['get_extension'] = [
        ('d', 's', 0, ('s', 'Filename_C_get_extension_s_p', 'p'), []),
    ]
    c.ct['get_file_size'] = [
        ('d', 'p', 0, ('p', 'Filename_C_get_file_size_p_p', 'p'), []),
    ]
    c.ct['get_filename_index'] = [
        ('d', 2, 1, ('p', 'Filename_C_get_filename_index_p_pi', 'pi'), ['int']),
    ]
    c.ct['get_fullpath'] = [
        ('d', 's', 0, ('s', 'Filename_C_get_fullpath_s_p', 'p'), []),
    ]
    c.ct['get_fullpath_w'] = [
        ('d', 'p', 0, ('p', 'Filename_C_get_fullpath_w_p_p', 'p'), []),
    ]
    c.ct['get_fullpath_wo_extension'] = [
        ('d', 's', 0, ('s', 'Filename_C_get_fullpath_wo_extension_s_p', 'p'), []),
    ]
    c.ct['get_hash'] = [
        ('d', 'i', 0, ('i', 'Filename_C_get_hash_i_p', 'p'), []),
    ]
    c.ct['get_hash_to_end'] = [
        ('d', 's', 0, ('s', 'Filename_C_get_hash_to_end_s_p', 'p'), []),
    ]
    c.ct['get_pattern'] = [
        ('d', 'B', 0, ('B', 'Filename_C_get_pattern_B_p', 'p'), []),
    ]
    c.ct['get_timestamp'] = [
        ('d', 'p', 0, ('p', 'Filename_C_get_timestamp_p_p', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'p', 0, ('p', 'Filename_C_get_type_p_p', 'p'), []),
    ]
    c.ct['has_hash'] = [
        ('d', 'B', 0, ('B', 'Filename_C_has_hash_B_p', 'p'), []),
    ]
    c.ct['is_binary'] = [
        ('d', 'B', 0, ('B', 'Filename_C_is_binary_B_p', 'p'), []),
    ]
    c.ct['is_binary_or_text'] = [
        ('d', 'B', 0, ('B', 'Filename_C_is_binary_or_text_B_p', 'p'), []),
    ]
    c.ct['is_directory'] = [
        ('d', 'B', 0, ('B', 'Filename_C_is_directory_B_p', 'p'), []),
    ]
    c.ct['is_executable'] = [
        ('d', 'B', 0, ('B', 'Filename_C_is_executable_B_p', 'p'), []),
    ]
    c.ct['is_fully_qualified'] = [
        ('d', 'B', 0, ('B', 'Filename_C_is_fully_qualified_B_p', 'p'), []),
    ]
    c.ct['is_local'] = [
        ('d', 'B', 0, ('B', 'Filename_C_is_local_B_p', 'p'), []),
    ]
    c.ct['is_regular_file'] = [
        ('d', 'B', 0, ('B', 'Filename_C_is_regular_file_B_p', 'p'), []),
    ]
    c.ct['is_text'] = [
        ('d', 'B', 0, ('B', 'Filename_C_is_text_B_p', 'p'), []),
    ]
    c.ct['is_writable'] = [
        ('d', 'B', 0, ('B', 'Filename_C_is_writable_B_p', 'p'), []),
    ]
    c.ct['length'] = [
        ('d', 'p', 0, ('p', 'Filename_C_length_p_p', 'p'), []),
    ]
    c.ct['make_absolute'] = [
        ('d', 'v', 0, ('v', 'Filename_C_make_absolute_v_p', 'p'), []),
        ('d', 'v', 1, ('v', 'Filename_C_make_absolute_v_pp', 'pp'), ['Filename const&']),
    ]
    c.ct['make_canonical'] = [
        ('d', 'B', 0, ('B', 'Filename_C_make_canonical_B_p', 'p'), []),
    ]
    c.ct['make_dir'] = [
        ('d', 'B', 0, ('B', 'Filename_C_make_dir_B_p', 'p'), []),
    ]
    c.ct['make_relative_to'] = [
        ('d', 'B', 2, ('B', 'Filename_C_make_relative_to_B_ppB', 'ppB'), ['Filename', 'bool']),
        ('d', 'B', 1, ('B', 'Filename_C_make_relative_to_B_pp', 'pp'), ['Filename']),
    ]
    c.ct['make_true_case'] = [
        ('d', 'B', 0, ('B', 'Filename_C_make_true_case_B_p', 'p'), []),
    ]
    c.ct['mkdir'] = [
        ('d', 'B', 0, ('B', 'Filename_C_mkdir_B_p', 'p'), []),
    ]
    c.ct['open_append'] = [
        ('d', 'B', 1, ('B', 'Filename_C_open_append_B_pp', 'pp'), ['pofstream&']),
        ('d', 'B', 1, ('B', 'Filename_C_open_append_B_pp_1_B_pp', 'pp'), ['std::ofstream&']),
    ]
    c.ct['open_read'] = [
        ('d', 'B', 1, ('B', 'Filename_C_open_read_B_pp', 'pp'), ['pifstream&']),
        ('d', 'B', 1, ('B', 'Filename_C_open_read_B_pp_1_B_pp', 'pp'), ['std::ifstream&']),
    ]
    c.ct['open_read_append'] = [
        ('d', 'B', 1, ('B', 'Filename_C_open_read_append_B_pp', 'pp'), ['pfstream&']),
        ('d', 'B', 1, ('B', 'Filename_C_open_read_append_B_pp_1_B_pp', 'pp'), ['std::fstream&']),
    ]
    c.ct['open_read_write'] = [
        ('d', 'B', 2, ('B', 'Filename_C_open_read_write_B_ppB', 'ppB'), ['pfstream&', 'bool']),
        ('d', 'B', 1, ('B', 'Filename_C_open_read_write_B_pp', 'pp'), ['pfstream&']),
        ('d', 'B', 2, ('B', 'Filename_C_open_read_write_B_ppB_1_B_ppB', 'ppB'), ['std::fstream&', 'bool']),
        ('d', 'B', 1, ('B', 'Filename_C_open_read_write_B_pp_1_B_pp', 'pp'), ['std::fstream&']),
    ]
    c.ct['open_write'] = [
        ('d', 'B', 2, ('B', 'Filename_C_open_write_B_ppB', 'ppB'), ['pofstream&', 'bool']),
        ('d', 'B', 1, ('B', 'Filename_C_open_write_B_pp', 'pp'), ['pofstream&']),
        ('d', 'B', 2, ('B', 'Filename_C_open_write_B_ppB_1_B_ppB', 'ppB'), ['std::ofstream&', 'bool']),
        ('d', 'B', 1, ('B', 'Filename_C_open_write_B_pp_1_B_pp', 'pp'), ['std::ofstream&']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'Filename_C_output_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['rename_to'] = [
        ('d', 'B', 1, ('B', 'Filename_C_rename_to_B_pp', 'pp'), ['Filename const&']),
    ]
    c.ct['resolve_filename'] = [
        ('d', 'B', 2, ('B', 'Filename_C_resolve_filename_B_pps', 'pps'), ['DSearchPath const&', 'std::string const&']),
        ('d', 'B', 1, ('B', 'Filename_C_resolve_filename_B_pp', 'pp'), ['DSearchPath const&']),
    ]
    c.ct['rmdir'] = [
        ('d', 'B', 0, ('B', 'Filename_C_rmdir_B_p', 'p'), []),
    ]
    c.ct['scan_directory'] = [
        ('d', 'B', 1, ('B', 'Filename_C_scan_directory_B_pp', 'pp'), ['vector_string&']),
    ]
    c.ct['set_basename'] = [
        ('d', 'v', 1, ('v', 'Filename_C_set_basename_v_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['set_basename_wo_extension'] = [
        ('d', 'v', 1, ('v', 'Filename_C_set_basename_wo_extension_v_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['set_binary'] = [
        ('d', 'v', 0, ('v', 'Filename_C_set_binary_v_p', 'p'), []),
    ]
    c.ct['set_dirname'] = [
        ('d', 'v', 1, ('v', 'Filename_C_set_dirname_v_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['set_extension'] = [
        ('d', 'v', 1, ('v', 'Filename_C_set_extension_v_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['set_fullpath'] = [
        ('d', 'v', 1, ('v', 'Filename_C_set_fullpath_v_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['set_fullpath_wo_extension'] = [
        ('d', 'v', 1, ('v', 'Filename_C_set_fullpath_wo_extension_v_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['set_hash_to_end'] = [
        ('d', 'v', 1, ('v', 'Filename_C_set_hash_to_end_v_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['set_pattern'] = [
        ('d', 'v', 1, ('v', 'Filename_C_set_pattern_v_pB', 'pB'), ['bool']),
    ]
    c.ct['set_text'] = [
        ('d', 'v', 0, ('v', 'Filename_C_set_text_v_p', 'p'), []),
    ]
    c.ct['set_type'] = [
        ('d', 'v', 1, ('v', 'Filename_C_set_type_v_pp', 'pp'), ['Filename::Type']),
    ]
    c.ct['standardize'] = [
        ('d', 'v', 0, ('v', 'Filename_C_standardize_v_p', 'p'), []),
    ]
    c.ct['substr'] = [
        ('d', 's', 1, ('s', 'Filename_C_substr_s_pp', 'pp'), ['std::size_t']),
        ('d', 's', 2, ('s', 'Filename_C_substr_s_ppp', 'ppp'), ['std::size_t', 'std::size_t']),
    ]
    c.ct['to_os_generic'] = [
        ('d', 's', 0, ('s', 'Filename_C_to_os_generic_s_p', 'p'), []),
    ]
    c.ct['to_os_long_name'] = [
        ('d', 's', 0, ('s', 'Filename_C_to_os_long_name_s_p', 'p'), []),
    ]
    c.ct['to_os_short_name'] = [
        ('d', 's', 0, ('s', 'Filename_C_to_os_short_name_s_p', 'p'), []),
    ]
    c.ct['to_os_specific'] = [
        ('d', 's', 0, ('s', 'Filename_C_to_os_specific_s_p', 'p'), []),
    ]
    c.ct['to_os_specific_w'] = [
        ('d', 'p', 0, ('p', 'Filename_C_to_os_specific_w_p_p', 'p'), []),
    ]
    c.ct['touch'] = [
        ('d', 'B', 0, ('B', 'Filename_C_touch_B_p', 'p'), []),
    ]
    c.ct['unlink'] = [
        ('d', 'B', 0, ('B', 'Filename_C_unlink_B_p', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(Filename, attr, self)

Filename.c.link(Filename)



class GeomEnums(cxx.cplusplus):

    c = cxx.cstructs()
    c.register("GeomEnums", "upanda3d", """libupanda3d_cni.so""")

    # enum Contents

    C_clip_point = const(2)
    C_color = const(5)
    C_index = const(6)
    C_matrix = const(8)
    C_morph_delta = const(7)
    C_normal = const(9)
    C_other = const(0)
    C_point = const(1)
    C_texcoord = const(4)
    C_vector = const(3)


    # enum ShadeModel

    SM_flat_first_vertex = const(2)
    SM_flat_last_vertex = const(3)
    SM_smooth = const(1)
    SM_uniform = const(0)


    # enum AnimationType

    AT_hardware = const(2)
    AT_none = const(0)
    AT_panda = const(1)


    # enum PrimitiveType

    PT_lines = const(2)
    PT_none = const(0)
    PT_patches = const(4)
    PT_points = const(3)
    PT_polygons = const(1)


    # enum UsageHint

    UH_client = const(0)
    UH_dynamic = const(2)
    UH_static = const(3)
    UH_stream = const(1)
    UH_unspecified = const(4)


    # enum NumericType

    NT_float32 = const(5)
    NT_float64 = const(6)
    NT_int16 = const(9)
    NT_int32 = const(10)
    NT_int8 = const(8)
    NT_packed_dabc = const(4)
    NT_packed_dcba = const(3)
    NT_packed_ufloat = const(11)
    NT_stdfloat = const(7)
    NT_uint16 = const(1)
    NT_uint32 = const(2)
    NT_uint8 = const(0)


    # enum GeomRendering

    GR_adjacency = const(1048576)
    GR_composite_bits = const(7168)
    GR_flat_first_vertex = const(8192)
    GR_flat_last_vertex = const(16384)
    GR_indexed_bits = const(65537)
    GR_indexed_other = const(65536)
    GR_indexed_point = const(1)
    GR_line_strip = const(4096)
    GR_per_point_size = const(8)
    GR_point = const(2)
    GR_point_aspect_ratio = const(32)
    GR_point_bits = const(1022)
    GR_point_perspective = const(16)
    GR_point_rotate = const(128)
    GR_point_scale = const(64)
    GR_point_sprite = const(256)
    GR_point_sprite_tex_matrix = const(512)
    GR_point_uniform_size = const(4)
    GR_render_mode_point = const(524288)
    GR_render_mode_wireframe = const(262144)
    GR_shade_model_bits = const(24576)
    GR_strip_cut_index = const(131072)
    GR_triangle_fan = const(2048)
    GR_triangle_strip = const(1024)


    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 3, 0, ('p', 'GeomEnums_C_ctor_p_v', ''), []),
        ('s', 3, 1, ('p', 'GeomEnums_C_ctor_p_p', 'p'), ['GeomEnums const&']),
    ]

    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_Geom'] = [
        ('d', 28, 0, ('p', 'GeomEnums_C_downcast_to_Geom_p_p', 'p'), []),
    ]
    c.ct['downcast_to_GeomPrimitive'] = [
        ('d', 25, 0, ('p', 'GeomEnums_C_downcast_to_GeomPrimitive_p_p', 'p'), []),
    ]
    c.ct['downcast_to_GeomVertexData'] = [
        ('d', 24, 0, ('p', 'GeomEnums_C_downcast_to_GeomVertexData_p_p', 'p'), []),
    ]
    c.ct['downcast_to_GeomVertexFormat'] = [
        ('d', 19, 0, ('p', 'GeomEnums_C_downcast_to_GeomVertexFormat_p_p', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomEnums, attr, self)

GeomEnums.c.link(GeomEnums)



class LVecBase3f(cxx.cplusplus):

    c = cxx.cstructs()
    c.register("LVecBase3f", "upanda3d", """libupanda3d_cni.so""")

    # enum 

    is_int = const(0)
    num_components = const(3)


    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 4, 0, ('p', 'LVecBase3f_C_ctor_p_v', ''), []),
        ('s', 4, 2, ('p', 'LVecBase3f_C_ctor_p_pf', 'pf'), ['LVecBase2f const&', 'float']),
        ('s', 4, 1, ('p', 'LVecBase3f_C_ctor_p_p', 'p'), ['LVecBase3f const&']),
        ('s', 4, 1, ('p', 'LVecBase3f_C_ctor_p_p_1_p_p', 'p'), ['LVecBase3f::EVector3 const&']),
        ('s', 4, 1, ('p', 'LVecBase3f_C_ctor_p_f', 'f'), ['float']),
        ('s', 4, 3, ('p', 'LVecBase3f_C_ctor_p_fff', 'fff'), ['float', 'float', 'float']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVecBase3f_C_get_class_type_i_v', ''), []),
    ]
    c.ct['get_num_components'] = [
        ('s', 'i', 0, ('i', 'LVecBase3f_C_get_num_components_i_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVecBase3f_C_init_type_v_v', ''), []),
    ]
    c.ct['size'] = [
        ('s', 'i', 0, ('i', 'LVecBase3f_C_size_i_v', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 4, 0, ('p', 'LVecBase3f_C_unit_x_p_v', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 4, 0, ('p', 'LVecBase3f_C_unit_y_p_v', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 4, 0, ('p', 'LVecBase3f_C_unit_z_p_v', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 4, 0, ('p', 'LVecBase3f_C_zero_p_v', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LVecBase3f, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_num_components(cls, *args,**kw):
        return ( cls.c.get('get_num_components', None) or cls.c.call(LVecBase3f, 'get_num_components', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LVecBase3f, 'init_type', None) )(*args,**kw)

    @classmethod
    def size(cls, *args,**kw):
        return ( cls.c.get('size', None) or cls.c.call(LVecBase3f, 'size', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LVecBase3f, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LVecBase3f, 'unit_y', None) )(*args,**kw)

    @classmethod
    def unit_z(cls, *args,**kw):
        return ( cls.c.get('unit_z', None) or cls.c.call(LVecBase3f, 'unit_z', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LVecBase3f, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_hash'] = [
        ('d', 'p', 1, ('p', 'LVecBase3f_C_add_hash_p_pp', 'pp'), ['std::size_t']),
        ('d', 'p', 2, ('p', 'LVecBase3f_C_add_hash_p_ppf', 'ppf'), ['std::size_t', 'float']),
    ]
    c.ct['add_to_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase3f_C_add_to_cell_v_pif', 'pif'), ['int', 'float']),
    ]
    c.ct['add_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f_C_add_x_v_pf', 'pf'), ['float']),
    ]
    c.ct['add_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f_C_add_y_v_pf', 'pf'), ['float']),
    ]
    c.ct['add_z'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f_C_add_z_v_pf', 'pf'), ['float']),
    ]
    c.ct['almost_equal'] = [
        ('d', 'B', 1, ('B', 'LVecBase3f_C_almost_equal_B_pp', 'pp'), ['LVecBase3f const&']),
        ('d', 'B', 2, ('B', 'LVecBase3f_C_almost_equal_B_ppf', 'ppf'), ['LVecBase3f const&', 'float']),
    ]
    c.ct['begin'] = [
        ('d', 'v', 0, ('v', 'LVecBase3f_C_begin_v_p', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase3f_C_begin_v_p_1_v_p', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'LVecBase3f_C_compare_to_i_pp', 'pp'), ['LVecBase3f const&']),
        ('d', 'i', 2, ('i', 'LVecBase3f_C_compare_to_i_ppf', 'ppf'), ['LVecBase3f const&', 'float']),
    ]
    c.ct['componentwise_mult'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f_C_componentwise_mult_v_pp', 'pp'), ['LVecBase3f const&']),
    ]
    c.ct['cross'] = [
        ('d', 4, 1, ('p', 'LVecBase3f_C_cross_p_pp', 'pp'), ['LVecBase3f const&']),
    ]
    c.ct['cross_into'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f_C_cross_into_v_pp', 'pp'), ['LVecBase3f const&']),
    ]
    c.ct['dot'] = [
        ('d', 'f', 1, ('f', 'LVecBase3f_C_dot_f_pp', 'pp'), ['LVecBase3f const&']),
    ]
    c.ct['end'] = [
        ('d', 'v', 0, ('v', 'LVecBase3f_C_end_v_p', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase3f_C_end_v_p_1_v_p', 'p'), []),
    ]
    c.ct['fill'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f_C_fill_v_pf', 'pf'), ['float']),
    ]
    c.ct['fmax'] = [
        ('d', 4, 1, ('p', 'LVecBase3f_C_fmax_p_pp', 'pp'), ['LVecBase3f const&']),
    ]
    c.ct['fmin'] = [
        ('d', 4, 1, ('p', 'LVecBase3f_C_fmin_p_pp', 'pp'), ['LVecBase3f const&']),
    ]
    c.ct['generate_hash'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f_C_generate_hash_v_pp', 'pp'), ['ChecksumHashGenerator&']),
        ('d', 'v', 2, ('v', 'LVecBase3f_C_generate_hash_v_ppf', 'ppf'), ['ChecksumHashGenerator&', 'float']),
    ]
    c.ct['get_cell'] = [
        ('d', 'f', 1, ('f', 'LVecBase3f_C_get_cell_f_pi', 'pi'), ['int']),
    ]
    c.ct['get_data'] = [
        ('d', 'v', 0, ('v', 'LVecBase3f_C_get_data_v_p', 'p'), []),
    ]
    c.ct['get_hash'] = [
        ('d', 'p', 0, ('p', 'LVecBase3f_C_get_hash_p_p', 'p'), []),
        ('d', 'p', 1, ('p', 'LVecBase3f_C_get_hash_p_pf', 'pf'), ['float']),
    ]
    c.ct['get_standardized_hpr'] = [
        ('d', 4, 0, ('p', 'LVecBase3f_C_get_standardized_hpr_p_p', 'p'), []),
    ]
    c.ct['get_v'] = [
        ('d', 'p', 0, ('p', 'LVecBase3f_C_get_v_p_p', 'p'), []),
    ]
    c.ct['get_x'] = [
        ('d', 'f', 0, ('f', 'LVecBase3f_C_get_x_f_p', 'p'), []),
    ]
    c.ct['get_xy'] = [
        ('d', 'p', 0, ('p', 'LVecBase3f_C_get_xy_p_p', 'p'), []),
    ]
    c.ct['get_xz'] = [
        ('d', 'p', 0, ('p', 'LVecBase3f_C_get_xz_p_p', 'p'), []),
    ]
    c.ct['get_y'] = [
        ('d', 'f', 0, ('f', 'LVecBase3f_C_get_y_f_p', 'p'), []),
    ]
    c.ct['get_yz'] = [
        ('d', 'p', 0, ('p', 'LVecBase3f_C_get_yz_p_p', 'p'), []),
    ]
    c.ct['get_z'] = [
        ('d', 'f', 0, ('f', 'LVecBase3f_C_get_z_f_p', 'p'), []),
    ]
    c.ct['is_nan'] = [
        ('d', 'B', 0, ('B', 'LVecBase3f_C_is_nan_B_p', 'p'), []),
    ]
    c.ct['length'] = [
        ('d', 'f', 0, ('f', 'LVecBase3f_C_length_f_p', 'p'), []),
    ]
    c.ct['length_squared'] = [
        ('d', 'f', 0, ('f', 'LVecBase3f_C_length_squared_f_p', 'p'), []),
    ]
    c.ct['normalize'] = [
        ('d', 'B', 0, ('B', 'LVecBase3f_C_normalize_B_p', 'p'), []),
    ]
    c.ct['normalized'] = [
        ('d', 4, 0, ('p', 'LVecBase3f_C_normalized_p_p', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f_C_output_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['project'] = [
        ('d', 4, 1, ('p', 'LVecBase3f_C_project_p_pp', 'pp'), ['LVecBase3f const&']),
    ]
    c.ct['read_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f_C_read_datagram_v_pp', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['read_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f_C_read_datagram_fixed_v_pp', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['set'] = [
        ('d', 'v', 3, ('v', 'LVecBase3f_C_set_v_pfff', 'pfff'), ['float', 'float', 'float']),
    ]
    c.ct['set_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase3f_C_set_cell_v_pif', 'pif'), ['int', 'float']),
    ]
    c.ct['set_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f_C_set_x_v_pf', 'pf'), ['float']),
    ]
    c.ct['set_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f_C_set_y_v_pf', 'pf'), ['float']),
    ]
    c.ct['set_z'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f_C_set_z_v_pf', 'pf'), ['float']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f_C_write_datagram_v_pp', 'pp'), ['Datagram&']),
    ]
    c.ct['write_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f_C_write_datagram_fixed_v_pp', 'pp'), ['Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVecBase3f, attr, self)

LVecBase3f.c.link(LVecBase3f)



class LinkedListNode(cxx.cplusplus):

    c = cxx.cstructs()
    c.register("LinkedListNode", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_PandaNode'] = [
        ('d', 29, 0, ('p', 'LinkedListNode_C_downcast_to_PandaNode_p_p', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LinkedListNode, attr, self)

LinkedListNode.c.link(LinkedListNode)



class MemoryBase(cxx.cplusplus):

    c = cxx.cstructs()
    c.register("MemoryBase", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 6, 0, ('p', 'MemoryBase_C_ctor_p_v', ''), []),
        ('s', 6, 1, ('p', 'MemoryBase_C_ctor_p_p', 'p'), ['MemoryBase const&']),
    ]

    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_ReferenceCount'] = [
        ('d', 13, 0, ('p', 'MemoryBase_C_downcast_to_ReferenceCount_p_p', 'p'), []),
    ]
    c.ct['downcast_to_TypedObject'] = [
        ('d', 14, 0, ('p', 'MemoryBase_C_downcast_to_TypedObject_p_p', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(MemoryBase, attr, self)

MemoryBase.c.link(MemoryBase)



class NodePath(cxx.cplusplus):

    c = cxx.cstructs()
    c.register("NodePath", "upanda3d", """libupanda3d_cni.so""")

    # enum ErrorType

    ET_fail = const(3)
    ET_not_found = const(1)
    ET_ok = const(0)
    ET_removed = const(2)


    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 7, 0, ('p', 'NodePath_C_ctor_p_v', ''), []),
        ('s', 7, 1, ('p', 'NodePath_C_ctor_p_p', 'p'), ['NodePath&&']),
        ('s', 7, 1, ('p', 'NodePath_C_ctor_p_p_1_p_p', 'p'), ['NodePath const&']),
        ('s', 7, 3, ('p', 'NodePath_C_ctor_p_ppp', 'ppp'), ['NodePath const&', 'PandaNode*', 'Thread*']),
        ('s', 7, 2, ('p', 'NodePath_C_ctor_p_pp', 'pp'), ['NodePath const&', 'PandaNode*']),
        ('s', 7, 2, ('p', 'NodePath_C_ctor_p_pp_1_p_pp', 'pp'), ['PandaNode*', 'Thread*']),
        ('s', 7, 1, ('p', 'NodePath_C_ctor_p_p_1_p_p_2_p_p', 'p'), ['PandaNode*']),
        ('s', 7, 2, ('p', 'NodePath_C_ctor_p_sp', 'sp'), ['std::string const&', 'Thread*']),
        ('s', 7, 1, ('p', 'NodePath_C_ctor_p_s', 's'), ['std::string const&']),
    ]

    # classmethod type calls

    c.ct['any_path'] = [
        ('s', 7, 2, ('p', 'NodePath_C_any_path_p_pp', 'pp'), ['PandaNode*', 'Thread*']),
        ('s', 7, 1, ('p', 'NodePath_C_any_path_p_p', 'p'), ['PandaNode*']),
    ]
    c.ct['decode_from_bam_stream'] = [
        ('s', 7, 2, ('p', 'NodePath_C_decode_from_bam_stream_p_pp', 'pp'), ['vector_uchar', 'BamReader*']),
        ('s', 7, 1, ('p', 'NodePath_C_decode_from_bam_stream_p_p', 'p'), ['vector_uchar']),
    ]
    c.ct['fail'] = [
        ('s', 7, 0, ('p', 'NodePath_C_fail_p_v', ''), []),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'NodePath_C_get_class_type_i_v', ''), []),
    ]
    c.ct['get_max_search_depth'] = [
        ('s', 'i', 0, ('i', 'NodePath_C_get_max_search_depth_i_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'NodePath_C_init_type_v_v', ''), []),
    ]
    c.ct['not_found'] = [
        ('s', 7, 0, ('p', 'NodePath_C_not_found_p_v', ''), []),
    ]
    c.ct['removed'] = [
        ('s', 7, 0, ('p', 'NodePath_C_removed_p_v', ''), []),
    ]
    c.ct['set_max_search_depth'] = [
        ('s', 'v', 1, ('v', 'NodePath_C_set_max_search_depth_v_i', 'i'), ['int']),
    ]

    @classmethod
    def any_path(cls, *args,**kw):
        return ( cls.c.get('any_path', None) or cls.c.call(NodePath, 'any_path', None) )(*args,**kw)

    @classmethod
    def decode_from_bam_stream(cls, *args,**kw):
        return ( cls.c.get('decode_from_bam_stream', None) or cls.c.call(NodePath, 'decode_from_bam_stream', None) )(*args,**kw)

    @classmethod
    def fail(cls, *args,**kw):
        return ( cls.c.get('fail', None) or cls.c.call(NodePath, 'fail', None) )(*args,**kw)

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(NodePath, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_max_search_depth(cls, *args,**kw):
        return ( cls.c.get('get_max_search_depth', None) or cls.c.call(NodePath, 'get_max_search_depth', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(NodePath, 'init_type', None) )(*args,**kw)

    @classmethod
    def not_found(cls, *args,**kw):
        return ( cls.c.get('not_found', None) or cls.c.call(NodePath, 'not_found', None) )(*args,**kw)

    @classmethod
    def removed(cls, *args,**kw):
        return ( cls.c.get('removed', None) or cls.c.call(NodePath, 'removed', None) )(*args,**kw)

    @classmethod
    def set_max_search_depth(cls, *args,**kw):
        return ( cls.c.get('set_max_search_depth', None) or cls.c.call(NodePath, 'set_max_search_depth', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_hash'] = [
        ('d', 'p', 1, ('p', 'NodePath_C_add_hash_p_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['adjust_all_priorities'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_adjust_all_priorities_v_pi', 'pi'), ['int']),
    ]
    c.ct['apply_texture_colors'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_apply_texture_colors_v_p', 'p'), []),
    ]
    c.ct['attach_new_node'] = [
        ('d', 7, 3, ('p', 'NodePath_C_attach_new_node_p_ppip', 'ppip'), ['PandaNode*', 'int', 'Thread*']),
        ('d', 7, 2, ('p', 'NodePath_C_attach_new_node_p_ppi', 'ppi'), ['PandaNode*', 'int']),
        ('d', 7, 1, ('p', 'NodePath_C_attach_new_node_p_pp', 'pp'), ['PandaNode*']),
        ('d', 7, 3, ('p', 'NodePath_C_attach_new_node_p_psip', 'psip'), ['std::string const&', 'int', 'Thread*']),
        ('d', 7, 2, ('p', 'NodePath_C_attach_new_node_p_psi', 'psi'), ['std::string const&', 'int']),
        ('d', 7, 1, ('p', 'NodePath_C_attach_new_node_p_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['calc_tight_bounds'] = [
        ('d', 'B', 4, ('B', 'NodePath_C_calc_tight_bounds_B_ppppp', 'ppppp'), ['LPoint3&', 'LPoint3&', 'NodePath const&', 'Thread*']),
        ('d', 'B', 3, ('B', 'NodePath_C_calc_tight_bounds_B_pppp', 'pppp'), ['LPoint3&', 'LPoint3&', 'NodePath const&']),
        ('d', 'B', 2, ('B', 'NodePath_C_calc_tight_bounds_B_ppp', 'ppp'), ['LPoint3&', 'LPoint3&']),
    ]
    c.ct['clear'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_v_p', 'p'), []),
    ]
    c.ct['clear_antialias'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_antialias_v_p', 'p'), []),
    ]
    c.ct['clear_attrib'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_clear_attrib_v_pi', 'pi'), ['TypeHandle']),
    ]
    c.ct['clear_audio_volume'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_audio_volume_v_p', 'p'), []),
    ]
    c.ct['clear_billboard'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_billboard_v_p', 'p'), []),
    ]
    c.ct['clear_bin'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_bin_v_p', 'p'), []),
    ]
    c.ct['clear_clip_plane'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_clip_plane_v_p', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath_C_clear_clip_plane_v_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['clear_color'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_color_v_p', 'p'), []),
    ]
    c.ct['clear_color_scale'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_color_scale_v_p', 'p'), []),
    ]
    c.ct['clear_compass'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_compass_v_p', 'p'), []),
    ]
    c.ct['clear_depth_offset'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_depth_offset_v_p', 'p'), []),
    ]
    c.ct['clear_depth_test'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_depth_test_v_p', 'p'), []),
    ]
    c.ct['clear_depth_write'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_depth_write_v_p', 'p'), []),
    ]
    c.ct['clear_effect'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_clear_effect_v_pi', 'pi'), ['TypeHandle']),
    ]
    c.ct['clear_effects'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_effects_v_p', 'p'), []),
    ]
    c.ct['clear_fog'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_fog_v_p', 'p'), []),
    ]
    c.ct['clear_light'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_light_v_p', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath_C_clear_light_v_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['clear_logic_op'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_logic_op_v_p', 'p'), []),
    ]
    c.ct['clear_mat'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_mat_v_p', 'p'), []),
    ]
    c.ct['clear_material'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_material_v_p', 'p'), []),
    ]
    c.ct['clear_model_nodes'] = [
        ('d', 'i', 0, ('i', 'NodePath_C_clear_model_nodes_i_p', 'p'), []),
    ]
    c.ct['clear_occluder'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_occluder_v_p', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath_C_clear_occluder_v_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['clear_project_texture'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_clear_project_texture_v_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['clear_render_mode'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_render_mode_v_p', 'p'), []),
    ]
    c.ct['clear_scissor'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_scissor_v_p', 'p'), []),
    ]
    c.ct['clear_shader'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_shader_v_p', 'p'), []),
    ]
    c.ct['clear_shader_input'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_clear_shader_input_v_ps', 'ps'), ['CPT_InternalName']),
    ]
    c.ct['clear_tag'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_clear_tag_v_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['clear_tex_gen'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_tex_gen_v_p', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath_C_clear_tex_gen_v_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['clear_tex_projector'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_tex_projector_v_p', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath_C_clear_tex_projector_v_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['clear_tex_transform'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_tex_transform_v_p', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath_C_clear_tex_transform_v_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['clear_texture'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_texture_v_p', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath_C_clear_texture_v_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['clear_transform'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_clear_transform_v_ppp', 'ppp'), ['NodePath const&', 'Thread*']),
        ('d', 'v', 1, ('v', 'NodePath_C_clear_transform_v_pp', 'pp'), ['NodePath const&']),
        ('d', 'v', 1, ('v', 'NodePath_C_clear_transform_v_pp_1_v_pp', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'NodePath_C_clear_transform_v_p', 'p'), []),
    ]
    c.ct['clear_transparency'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_transparency_v_p', 'p'), []),
    ]
    c.ct['clear_two_sided'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_clear_two_sided_v_p', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'NodePath_C_compare_to_i_pp', 'pp'), ['NodePath const&']),
        ('d', 'i', 1, ('i', 'NodePath_C_compare_to_i_pp_1_i_pp', 'pp'), ['WeakNodePath const&']),
    ]
    c.ct['compose_color_scale'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_compose_color_scale_v_ppi', 'ppi'), ['LVecBase4 const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_compose_color_scale_v_pp', 'pp'), ['LVecBase4 const&']),
        ('d', 'v', 5, ('v', 'NodePath_C_compose_color_scale_v_pffffi', 'pffffi'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'int']),
        ('d', 'v', 4, ('v', 'NodePath_C_compose_color_scale_v_pffff', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['copy_to'] = [
        ('d', 7, 3, ('p', 'NodePath_C_copy_to_p_ppip', 'ppip'), ['NodePath const&', 'int', 'Thread*']),
        ('d', 7, 2, ('p', 'NodePath_C_copy_to_p_ppi', 'ppi'), ['NodePath const&', 'int']),
        ('d', 7, 1, ('p', 'NodePath_C_copy_to_p_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['count_num_descendants'] = [
        ('d', 'i', 0, ('i', 'NodePath_C_count_num_descendants_i_p', 'p'), []),
    ]
    c.ct['detach_node'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_detach_node_v_pp', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'NodePath_C_detach_node_v_p', 'p'), []),
    ]
    c.ct['do_billboard_axis'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_do_billboard_axis_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
    ]
    c.ct['do_billboard_point_eye'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_do_billboard_point_eye_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
    ]
    c.ct['do_billboard_point_world'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_do_billboard_point_world_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
    ]
    c.ct['encode_to_bam_stream'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_encode_to_bam_stream_p_p', 'p'), []),
        ('d', 'B', 2, ('B', 'NodePath_C_encode_to_bam_stream_B_ppp', 'ppp'), ['vector_uchar&', 'BamWriter*']),
        ('d', 'B', 1, ('B', 'NodePath_C_encode_to_bam_stream_B_pp', 'pp'), ['vector_uchar&']),
    ]
    c.ct['fillin'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_fillin_v_ppp', 'ppp'), ['DatagramIterator&', 'BamReader*']),
    ]
    c.ct['find'] = [
        ('d', 7, 1, ('p', 'NodePath_C_find_p_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['find_all_matches'] = [
        ('d', 8, 1, ('p', 'NodePath_C_find_all_matches_p_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['find_all_materials'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_find_all_materials_p_p', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath_C_find_all_materials_p_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['find_all_paths_to'] = [
        ('d', 8, 1, ('p', 'NodePath_C_find_all_paths_to_p_pp', 'pp'), ['PandaNode*']),
    ]
    c.ct['find_all_texcoords'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_find_all_texcoords_p_p', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath_C_find_all_texcoords_p_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['find_all_texture_stages'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_find_all_texture_stages_p_p', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath_C_find_all_texture_stages_p_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['find_all_textures'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_find_all_textures_p_p', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath_C_find_all_textures_p_pp', 'pp'), ['TextureStage*']),
        ('d', 'p', 1, ('p', 'NodePath_C_find_all_textures_p_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['find_all_vertex_columns'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_find_all_vertex_columns_p_p', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath_C_find_all_vertex_columns_p_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['find_material'] = [
        ('d', 'p', 1, ('p', 'NodePath_C_find_material_p_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['find_net_tag'] = [
        ('d', 7, 1, ('p', 'NodePath_C_find_net_tag_p_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['find_path_to'] = [
        ('d', 7, 1, ('p', 'NodePath_C_find_path_to_p_pp', 'pp'), ['PandaNode*']),
    ]
    c.ct['find_texture'] = [
        ('d', 'p', 1, ('p', 'NodePath_C_find_texture_p_pp', 'pp'), ['TextureStage*']),
        ('d', 'p', 1, ('p', 'NodePath_C_find_texture_p_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['find_texture_stage'] = [
        ('d', 'p', 1, ('p', 'NodePath_C_find_texture_stage_p_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['flatten_light'] = [
        ('d', 'i', 0, ('i', 'NodePath_C_flatten_light_i_p', 'p'), []),
    ]
    c.ct['flatten_medium'] = [
        ('d', 'i', 0, ('i', 'NodePath_C_flatten_medium_i_p', 'p'), []),
    ]
    c.ct['flatten_strong'] = [
        ('d', 'i', 0, ('i', 'NodePath_C_flatten_strong_i_p', 'p'), []),
    ]
    c.ct['force_recompute_bounds'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_force_recompute_bounds_v_p', 'p'), []),
    ]
    c.ct['get_ancestor'] = [
        ('d', 7, 2, ('p', 'NodePath_C_get_ancestor_p_pip', 'pip'), ['int', 'Thread*']),
        ('d', 7, 1, ('p', 'NodePath_C_get_ancestor_p_pi', 'pi'), ['int']),
    ]
    c.ct['get_antialias'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_antialias_p_p', 'p'), []),
    ]
    c.ct['get_attrib'] = [
        ('d', 'p', 1, ('p', 'NodePath_C_get_attrib_p_pi', 'pi'), ['TypeHandle']),
    ]
    c.ct['get_audio_volume'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_audio_volume_f_p', 'p'), []),
    ]
    c.ct['get_bin_draw_order'] = [
        ('d', 'i', 0, ('i', 'NodePath_C_get_bin_draw_order_i_p', 'p'), []),
    ]
    c.ct['get_bin_name'] = [
        ('d', 's', 0, ('s', 'NodePath_C_get_bin_name_s_p', 'p'), []),
    ]
    c.ct['get_bounds'] = [
        ('d', 'p', 1, ('p', 'NodePath_C_get_bounds_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'NodePath_C_get_bounds_p_p', 'p'), []),
    ]
    c.ct['get_child'] = [
        ('d', 7, 2, ('p', 'NodePath_C_get_child_p_pip', 'pip'), ['int', 'Thread*']),
        ('d', 7, 1, ('p', 'NodePath_C_get_child_p_pi', 'pi'), ['int']),
    ]
    c.ct['get_children'] = [
        ('d', 8, 1, ('p', 'NodePath_C_get_children_p_pp', 'pp'), ['Thread*']),
        ('d', 8, 0, ('p', 'NodePath_C_get_children_p_p', 'p'), []),
    ]
    c.ct['get_collide_mask'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_collide_mask_p_p', 'p'), []),
    ]
    c.ct['get_color'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_color_p_p', 'p'), []),
    ]
    c.ct['get_color_scale'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_color_scale_p_p', 'p'), []),
    ]
    c.ct['get_common_ancestor'] = [
        ('d', 7, 2, ('p', 'NodePath_C_get_common_ancestor_p_ppp', 'ppp'), ['NodePath const&', 'Thread*']),
        ('d', 7, 1, ('p', 'NodePath_C_get_common_ancestor_p_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_depth_offset'] = [
        ('d', 'i', 0, ('i', 'NodePath_C_get_depth_offset_i_p', 'p'), []),
    ]
    c.ct['get_depth_test'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_get_depth_test_B_p', 'p'), []),
    ]
    c.ct['get_depth_write'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_get_depth_write_B_p', 'p'), []),
    ]
    c.ct['get_distance'] = [
        ('d', 'f', 1, ('f', 'NodePath_C_get_distance_f_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_effect'] = [
        ('d', 'p', 1, ('p', 'NodePath_C_get_effect_p_pi', 'pi'), ['TypeHandle']),
    ]
    c.ct['get_effects'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_effects_p_p', 'p'), []),
    ]
    c.ct['get_error_type'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_error_type_p_p', 'p'), []),
    ]
    c.ct['get_fog'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_fog_p_p', 'p'), []),
    ]
    c.ct['get_h'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_h_f_p', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath_C_get_h_f_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_hidden_ancestor'] = [
        ('d', 7, 2, ('p', 'NodePath_C_get_hidden_ancestor_p_ppp', 'ppp'), ['DrawMask', 'Thread*']),
        ('d', 7, 1, ('p', 'NodePath_C_get_hidden_ancestor_p_pp', 'pp'), ['DrawMask']),
        ('d', 7, 0, ('p', 'NodePath_C_get_hidden_ancestor_p_p', 'p'), []),
    ]
    c.ct['get_hpr'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_hpr_p_p', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath_C_get_hpr_p_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_instance_count'] = [
        ('d', 'i', 0, ('i', 'NodePath_C_get_instance_count_i_p', 'p'), []),
    ]
    c.ct['get_key'] = [
        ('d', 'i', 0, ('i', 'NodePath_C_get_key_i_p', 'p'), []),
    ]
    c.ct['get_logic_op'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_logic_op_p_p', 'p'), []),
    ]
    c.ct['get_mat'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_mat_p_p', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath_C_get_mat_p_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_material'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_material_p_p', 'p'), []),
    ]
    c.ct['get_name'] = [
        ('d', 's', 0, ('s', 'NodePath_C_get_name_s_p', 'p'), []),
    ]
    c.ct['get_net_audio_volume'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_net_audio_volume_f_p', 'p'), []),
    ]
    c.ct['get_net_prev_transform'] = [
        ('d', 'p', 1, ('p', 'NodePath_C_get_net_prev_transform_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'NodePath_C_get_net_prev_transform_p_p', 'p'), []),
    ]
    c.ct['get_net_state'] = [
        ('d', 'p', 1, ('p', 'NodePath_C_get_net_state_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'NodePath_C_get_net_state_p_p', 'p'), []),
    ]
    c.ct['get_net_tag'] = [
        ('d', 's', 1, ('s', 'NodePath_C_get_net_tag_s_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['get_net_transform'] = [
        ('d', 'p', 1, ('p', 'NodePath_C_get_net_transform_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'NodePath_C_get_net_transform_p_p', 'p'), []),
    ]
    c.ct['get_node'] = [
        ('d', 29, 2, ('p', 'NodePath_C_get_node_p_pip', 'pip'), ['int', 'Thread*']),
        ('d', 29, 1, ('p', 'NodePath_C_get_node_p_pi', 'pi'), ['int']),
    ]
    c.ct['get_num_children'] = [
        ('d', 'i', 1, ('i', 'NodePath_C_get_num_children_i_pp', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'NodePath_C_get_num_children_i_p', 'p'), []),
    ]
    c.ct['get_num_nodes'] = [
        ('d', 'i', 1, ('i', 'NodePath_C_get_num_nodes_i_pp', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'NodePath_C_get_num_nodes_i_p', 'p'), []),
    ]
    c.ct['get_p'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_p_f_p', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath_C_get_p_f_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_parent'] = [
        ('d', 7, 1, ('p', 'NodePath_C_get_parent_p_pp', 'pp'), ['Thread*']),
        ('d', 7, 0, ('p', 'NodePath_C_get_parent_p_p', 'p'), []),
    ]
    c.ct['get_pos'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_pos_p_p', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath_C_get_pos_p_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_pos_delta'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_pos_delta_p_p', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath_C_get_pos_delta_p_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_prev_transform'] = [
        ('d', 'p', 2, ('p', 'NodePath_C_get_prev_transform_p_ppp', 'ppp'), ['NodePath const&', 'Thread*']),
        ('d', 'p', 1, ('p', 'NodePath_C_get_prev_transform_p_pp', 'pp'), ['NodePath const&']),
        ('d', 'p', 1, ('p', 'NodePath_C_get_prev_transform_p_pp_1_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'NodePath_C_get_prev_transform_p_p', 'p'), []),
    ]
    c.ct['get_quat'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_quat_p_p', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath_C_get_quat_p_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_r'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_r_f_p', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath_C_get_r_f_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_relative_point'] = [
        ('d', 'p', 2, ('p', 'NodePath_C_get_relative_point_p_ppp', 'ppp'), ['NodePath const&', 'LVecBase3 const&']),
    ]
    c.ct['get_relative_vector'] = [
        ('d', 'p', 2, ('p', 'NodePath_C_get_relative_vector_p_ppp', 'ppp'), ['NodePath const&', 'LVecBase3 const&']),
    ]
    c.ct['get_render_mode'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_render_mode_p_p', 'p'), []),
    ]
    c.ct['get_render_mode_perspective'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_get_render_mode_perspective_B_p', 'p'), []),
    ]
    c.ct['get_render_mode_thickness'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_render_mode_thickness_f_p', 'p'), []),
    ]
    c.ct['get_sa'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_sa_f_p', 'p'), []),
    ]
    c.ct['get_sb'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_sb_f_p', 'p'), []),
    ]
    c.ct['get_scale'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_scale_p_p', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath_C_get_scale_p_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_sg'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_sg_f_p', 'p'), []),
    ]
    c.ct['get_shader'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_shader_p_p', 'p'), []),
    ]
    c.ct['get_shader_input'] = [
        ('d', 'p', 1, ('p', 'NodePath_C_get_shader_input_p_ps', 'ps'), ['CPT_InternalName']),
    ]
    c.ct['get_shear'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_shear_p_p', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath_C_get_shear_p_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_shxy'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_shxy_f_p', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath_C_get_shxy_f_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_shxz'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_shxz_f_p', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath_C_get_shxz_f_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_shyz'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_shyz_f_p', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath_C_get_shyz_f_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_sort'] = [
        ('d', 'i', 1, ('i', 'NodePath_C_get_sort_i_pp', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'NodePath_C_get_sort_i_p', 'p'), []),
    ]
    c.ct['get_sr'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_sr_f_p', 'p'), []),
    ]
    c.ct['get_stashed_ancestor'] = [
        ('d', 7, 1, ('p', 'NodePath_C_get_stashed_ancestor_p_pp', 'pp'), ['Thread*']),
        ('d', 7, 0, ('p', 'NodePath_C_get_stashed_ancestor_p_p', 'p'), []),
    ]
    c.ct['get_stashed_children'] = [
        ('d', 8, 1, ('p', 'NodePath_C_get_stashed_children_p_pp', 'pp'), ['Thread*']),
        ('d', 8, 0, ('p', 'NodePath_C_get_stashed_children_p_p', 'p'), []),
    ]
    c.ct['get_state'] = [
        ('d', 'p', 2, ('p', 'NodePath_C_get_state_p_ppp', 'ppp'), ['NodePath const&', 'Thread*']),
        ('d', 'p', 1, ('p', 'NodePath_C_get_state_p_pp', 'pp'), ['NodePath const&']),
        ('d', 'p', 1, ('p', 'NodePath_C_get_state_p_pp_1_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'NodePath_C_get_state_p_p', 'p'), []),
    ]
    c.ct['get_sx'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_sx_f_p', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath_C_get_sx_f_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_sy'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_sy_f_p', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath_C_get_sy_f_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_sz'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_sz_f_p', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath_C_get_sz_f_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_tag'] = [
        ('d', 's', 1, ('s', 'NodePath_C_get_tag_s_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['get_tag_keys'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_get_tag_keys_v_pp', 'pp'), ['vector_string&']),
    ]
    c.ct['get_tex_gen'] = [
        ('d', 'p', 1, ('p', 'NodePath_C_get_tex_gen_p_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_hpr'] = [
        ('d', 'p', 2, ('p', 'NodePath_C_get_tex_hpr_p_ppp', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 'p', 1, ('p', 'NodePath_C_get_tex_hpr_p_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_offset'] = [
        ('d', 'p', 2, ('p', 'NodePath_C_get_tex_offset_p_ppp', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 'p', 1, ('p', 'NodePath_C_get_tex_offset_p_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_pos'] = [
        ('d', 'p', 2, ('p', 'NodePath_C_get_tex_pos_p_ppp', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 'p', 1, ('p', 'NodePath_C_get_tex_pos_p_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_projector_from'] = [
        ('d', 7, 1, ('p', 'NodePath_C_get_tex_projector_from_p_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_projector_to'] = [
        ('d', 7, 1, ('p', 'NodePath_C_get_tex_projector_to_p_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_rotate'] = [
        ('d', 'f', 2, ('f', 'NodePath_C_get_tex_rotate_f_ppp', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 'f', 1, ('f', 'NodePath_C_get_tex_rotate_f_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_scale'] = [
        ('d', 'p', 2, ('p', 'NodePath_C_get_tex_scale_p_ppp', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 'p', 1, ('p', 'NodePath_C_get_tex_scale_p_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_scale_3d'] = [
        ('d', 'p', 2, ('p', 'NodePath_C_get_tex_scale_3d_p_ppp', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 'p', 1, ('p', 'NodePath_C_get_tex_scale_3d_p_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_transform'] = [
        ('d', 'p', 2, ('p', 'NodePath_C_get_tex_transform_p_ppp', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 'p', 1, ('p', 'NodePath_C_get_tex_transform_p_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_texture'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_texture_p_p', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath_C_get_texture_p_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_texture_sampler'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_texture_sampler_p_p', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath_C_get_texture_sampler_p_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_top'] = [
        ('d', 7, 1, ('p', 'NodePath_C_get_top_p_pp', 'pp'), ['Thread*']),
        ('d', 7, 0, ('p', 'NodePath_C_get_top_p_p', 'p'), []),
    ]
    c.ct['get_top_node'] = [
        ('d', 29, 1, ('p', 'NodePath_C_get_top_node_p_pp', 'pp'), ['Thread*']),
        ('d', 29, 0, ('p', 'NodePath_C_get_top_node_p_p', 'p'), []),
    ]
    c.ct['get_transform'] = [
        ('d', 'p', 2, ('p', 'NodePath_C_get_transform_p_ppp', 'ppp'), ['NodePath const&', 'Thread*']),
        ('d', 'p', 1, ('p', 'NodePath_C_get_transform_p_pp', 'pp'), ['NodePath const&']),
        ('d', 'p', 1, ('p', 'NodePath_C_get_transform_p_pp_1_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'NodePath_C_get_transform_p_p', 'p'), []),
    ]
    c.ct['get_transparency'] = [
        ('d', 'p', 0, ('p', 'NodePath_C_get_transparency_p_p', 'p'), []),
    ]
    c.ct['get_two_sided'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_get_two_sided_B_p', 'p'), []),
    ]
    c.ct['get_x'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_x_f_p', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath_C_get_x_f_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_y'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_y_f_p', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath_C_get_y_f_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_z'] = [
        ('d', 'f', 0, ('f', 'NodePath_C_get_z_f_p', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath_C_get_z_f_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['has_antialias'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_antialias_B_p', 'p'), []),
    ]
    c.ct['has_attrib'] = [
        ('d', 'B', 1, ('B', 'NodePath_C_has_attrib_B_pi', 'pi'), ['TypeHandle']),
    ]
    c.ct['has_audio_volume'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_audio_volume_B_p', 'p'), []),
    ]
    c.ct['has_billboard'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_billboard_B_p', 'p'), []),
    ]
    c.ct['has_bin'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_bin_B_p', 'p'), []),
    ]
    c.ct['has_clip_plane'] = [
        ('d', 'B', 1, ('B', 'NodePath_C_has_clip_plane_B_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['has_clip_plane_off'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_clip_plane_off_B_p', 'p'), []),
        ('d', 'B', 1, ('B', 'NodePath_C_has_clip_plane_off_B_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['has_color'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_color_B_p', 'p'), []),
    ]
    c.ct['has_color_scale'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_color_scale_B_p', 'p'), []),
    ]
    c.ct['has_compass'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_compass_B_p', 'p'), []),
    ]
    c.ct['has_depth_offset'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_depth_offset_B_p', 'p'), []),
    ]
    c.ct['has_depth_test'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_depth_test_B_p', 'p'), []),
    ]
    c.ct['has_depth_write'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_depth_write_B_p', 'p'), []),
    ]
    c.ct['has_effect'] = [
        ('d', 'B', 1, ('B', 'NodePath_C_has_effect_B_pi', 'pi'), ['TypeHandle']),
    ]
    c.ct['has_fog'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_fog_B_p', 'p'), []),
    ]
    c.ct['has_fog_off'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_fog_off_B_p', 'p'), []),
    ]
    c.ct['has_light'] = [
        ('d', 'B', 1, ('B', 'NodePath_C_has_light_B_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['has_light_off'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_light_off_B_p', 'p'), []),
        ('d', 'B', 1, ('B', 'NodePath_C_has_light_off_B_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['has_logic_op'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_logic_op_B_p', 'p'), []),
    ]
    c.ct['has_mat'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_mat_B_p', 'p'), []),
    ]
    c.ct['has_material'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_material_B_p', 'p'), []),
    ]
    c.ct['has_net_tag'] = [
        ('d', 'B', 1, ('B', 'NodePath_C_has_net_tag_B_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['has_occluder'] = [
        ('d', 'B', 1, ('B', 'NodePath_C_has_occluder_B_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['has_parent'] = [
        ('d', 'B', 1, ('B', 'NodePath_C_has_parent_B_pp', 'pp'), ['Thread*']),
        ('d', 'B', 0, ('B', 'NodePath_C_has_parent_B_p', 'p'), []),
    ]
    c.ct['has_render_mode'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_render_mode_B_p', 'p'), []),
    ]
    c.ct['has_scissor'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_scissor_B_p', 'p'), []),
    ]
    c.ct['has_tag'] = [
        ('d', 'B', 1, ('B', 'NodePath_C_has_tag_B_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['has_tex_gen'] = [
        ('d', 'B', 1, ('B', 'NodePath_C_has_tex_gen_B_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['has_tex_projector'] = [
        ('d', 'B', 1, ('B', 'NodePath_C_has_tex_projector_B_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['has_tex_transform'] = [
        ('d', 'B', 1, ('B', 'NodePath_C_has_tex_transform_B_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['has_texcoord'] = [
        ('d', 'B', 1, ('B', 'NodePath_C_has_texcoord_B_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['has_texture'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_texture_B_p', 'p'), []),
        ('d', 'B', 1, ('B', 'NodePath_C_has_texture_B_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['has_texture_off'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_texture_off_B_p', 'p'), []),
        ('d', 'B', 1, ('B', 'NodePath_C_has_texture_off_B_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['has_transparency'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_transparency_B_p', 'p'), []),
    ]
    c.ct['has_two_sided'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_has_two_sided_B_p', 'p'), []),
    ]
    c.ct['has_vertex_column'] = [
        ('d', 'B', 1, ('B', 'NodePath_C_has_vertex_column_B_ps', 'ps'), ['InternalName const*']),
    ]
    c.ct['heads_up'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_heads_up_v_ppp', 'ppp'), ['LPoint3 const&', 'LVector3 const&']),
        ('d', 'v', 1, ('v', 'NodePath_C_heads_up_v_pp', 'pp'), ['LPoint3 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_heads_up_v_pppp', 'pppp'), ['NodePath const&', 'LPoint3 const&', 'LVector3 const&']),
        ('d', 'v', 2, ('v', 'NodePath_C_heads_up_v_ppp_1_v_ppp', 'ppp'), ['NodePath const&', 'LPoint3 const&']),
        ('d', 'v', 1, ('v', 'NodePath_C_heads_up_v_pp_1_v_pp', 'pp'), ['NodePath const&']),
        ('d', 'v', 4, ('v', 'NodePath_C_heads_up_v_ppfff', 'ppfff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath_C_heads_up_v_pfff', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['hide'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_hide_v_p', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath_C_hide_v_pp', 'pp'), ['DrawMask']),
    ]
    c.ct['hide_bounds'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_hide_bounds_v_p', 'p'), []),
    ]
    c.ct['instance_to'] = [
        ('d', 7, 3, ('p', 'NodePath_C_instance_to_p_ppip', 'ppip'), ['NodePath const&', 'int', 'Thread*']),
        ('d', 7, 2, ('p', 'NodePath_C_instance_to_p_ppi', 'ppi'), ['NodePath const&', 'int']),
        ('d', 7, 1, ('p', 'NodePath_C_instance_to_p_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['instance_under_node'] = [
        ('d', 7, 4, ('p', 'NodePath_C_instance_under_node_p_ppsip', 'ppsip'), ['NodePath const&', 'std::string const&', 'int', 'Thread*']),
        ('d', 7, 3, ('p', 'NodePath_C_instance_under_node_p_ppsi', 'ppsi'), ['NodePath const&', 'std::string const&', 'int']),
        ('d', 7, 2, ('p', 'NodePath_C_instance_under_node_p_pps', 'pps'), ['NodePath const&', 'std::string const&']),
    ]
    c.ct['is_ancestor_of'] = [
        ('d', 'B', 2, ('B', 'NodePath_C_is_ancestor_of_B_ppp', 'ppp'), ['NodePath const&', 'Thread*']),
        ('d', 'B', 1, ('B', 'NodePath_C_is_ancestor_of_B_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['is_empty'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_is_empty_B_p', 'p'), []),
    ]
    c.ct['is_hidden'] = [
        ('d', 'B', 1, ('B', 'NodePath_C_is_hidden_B_pp', 'pp'), ['DrawMask']),
        ('d', 'B', 0, ('B', 'NodePath_C_is_hidden_B_p', 'p'), []),
    ]
    c.ct['is_same_graph'] = [
        ('d', 'B', 2, ('B', 'NodePath_C_is_same_graph_B_ppp', 'ppp'), ['NodePath const&', 'Thread*']),
        ('d', 'B', 1, ('B', 'NodePath_C_is_same_graph_B_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['is_singleton'] = [
        ('d', 'B', 1, ('B', 'NodePath_C_is_singleton_B_pp', 'pp'), ['Thread*']),
        ('d', 'B', 0, ('B', 'NodePath_C_is_singleton_B_p', 'p'), []),
    ]
    c.ct['is_stashed'] = [
        ('d', 'B', 0, ('B', 'NodePath_C_is_stashed_B_p', 'p'), []),
    ]
    c.ct['list_tags'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_list_tags_v_p', 'p'), []),
    ]
    c.ct['look_at'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_look_at_v_ppp', 'ppp'), ['LPoint3 const&', 'LVector3 const&']),
        ('d', 'v', 1, ('v', 'NodePath_C_look_at_v_pp', 'pp'), ['LPoint3 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_look_at_v_pppp', 'pppp'), ['NodePath const&', 'LPoint3 const&', 'LVector3 const&']),
        ('d', 'v', 2, ('v', 'NodePath_C_look_at_v_ppp_1_v_ppp', 'ppp'), ['NodePath const&', 'LPoint3 const&']),
        ('d', 'v', 1, ('v', 'NodePath_C_look_at_v_pp_1_v_pp', 'pp'), ['NodePath const&']),
        ('d', 'v', 4, ('v', 'NodePath_C_look_at_v_ppfff', 'ppfff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath_C_look_at_v_pfff', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['ls'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_ls_v_p', 'p'), []),
        ('d', 'v', 2, ('v', 'NodePath_C_ls_v_ppi', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_ls_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['node'] = [
        ('d', 29, 0, ('p', 'NodePath_C_node_p_p', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_output_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['premunge_scene'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_premunge_scene_v_pp', 'pp'), ['GraphicsStateGuardianBase*']),
        ('d', 'v', 0, ('v', 'NodePath_C_premunge_scene_v_p', 'p'), []),
    ]
    c.ct['prepare_scene'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_prepare_scene_v_pp', 'pp'), ['GraphicsStateGuardianBase*']),
    ]
    c.ct['project_texture'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_project_texture_v_pppp', 'pppp'), ['TextureStage*', 'Texture*', 'NodePath const&']),
    ]
    c.ct['remove_node'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_remove_node_v_pp', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'NodePath_C_remove_node_v_p', 'p'), []),
    ]
    c.ct['reparent_to'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_reparent_to_v_ppip', 'ppip'), ['NodePath const&', 'int', 'Thread*']),
        ('d', 'v', 2, ('v', 'NodePath_C_reparent_to_v_ppi', 'ppi'), ['NodePath const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_reparent_to_v_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['replace_material'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_replace_material_v_ppp', 'ppp'), ['Material*', 'Material*']),
    ]
    c.ct['replace_texture'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_replace_texture_v_ppp', 'ppp'), ['Texture*', 'Texture*']),
    ]
    c.ct['reverse_ls'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_reverse_ls_v_p', 'p'), []),
        ('d', 'i', 2, ('i', 'NodePath_C_reverse_ls_i_ppi', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'i', 1, ('i', 'NodePath_C_reverse_ls_i_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['set_all_color_scale'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_all_color_scale_v_pfi', 'pfi'), ['PN_stdfloat', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_all_color_scale_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_alpha_scale'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_alpha_scale_v_pfi', 'pfi'), ['PN_stdfloat', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_alpha_scale_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_antialias'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_antialias_v_ppi', 'ppi'), ['unsigned short int', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_antialias_v_pp', 'pp'), ['unsigned short int']),
    ]
    c.ct['set_attrib'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_attrib_v_ppi', 'ppi'), ['RenderAttrib const*', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_attrib_v_pp', 'pp'), ['RenderAttrib const*']),
    ]
    c.ct['set_audio_volume'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_audio_volume_v_pfi', 'pfi'), ['PN_stdfloat', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_audio_volume_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_audio_volume_off'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_audio_volume_off_v_pi', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath_C_set_audio_volume_off_v_p', 'p'), []),
    ]
    c.ct['set_billboard_axis'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_billboard_axis_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_billboard_axis_v_pf', 'pf'), ['PN_stdfloat']),
        ('d', 'v', 0, ('v', 'NodePath_C_set_billboard_axis_v_p', 'p'), []),
    ]
    c.ct['set_billboard_point_eye'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_set_billboard_point_eye_v_ppfB', 'ppfB'), ['NodePath const&', 'PN_stdfloat', 'bool']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_billboard_point_eye_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_billboard_point_eye_v_pfB', 'pfB'), ['PN_stdfloat', 'bool']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_billboard_point_eye_v_pf', 'pf'), ['PN_stdfloat']),
        ('d', 'v', 0, ('v', 'NodePath_C_set_billboard_point_eye_v_p', 'p'), []),
    ]
    c.ct['set_billboard_point_world'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_billboard_point_world_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_billboard_point_world_v_pf', 'pf'), ['PN_stdfloat']),
        ('d', 'v', 0, ('v', 'NodePath_C_set_billboard_point_world_v_p', 'p'), []),
    ]
    c.ct['set_bin'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_set_bin_v_psii', 'psii'), ['std::string const&', 'int', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_bin_v_psi', 'psi'), ['std::string const&', 'int']),
    ]
    c.ct['set_clip_plane'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_clip_plane_v_ppi', 'ppi'), ['NodePath const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_clip_plane_v_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['set_clip_plane_off'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_clip_plane_off_v_ppi', 'ppi'), ['NodePath const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_clip_plane_off_v_pp', 'pp'), ['NodePath const&']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_clip_plane_off_v_pi', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath_C_set_clip_plane_off_v_p', 'p'), []),
    ]
    c.ct['set_collide_mask'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_set_collide_mask_v_pppi', 'pppi'), ['CollideMask', 'CollideMask', 'TypeHandle']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_collide_mask_v_ppp', 'ppp'), ['CollideMask', 'CollideMask']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_collide_mask_v_pp', 'pp'), ['CollideMask']),
    ]
    c.ct['set_color'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_color_v_ppi', 'ppi'), ['LColor const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_color_v_pp', 'pp'), ['LColor const&']),
        ('d', 'v', 5, ('v', 'NodePath_C_set_color_v_pffffi', 'pffffi'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'int']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_color_v_pffff', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_color_v_pfff', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_color_off'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_color_off_v_pi', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath_C_set_color_off_v_p', 'p'), []),
    ]
    c.ct['set_color_scale'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_color_scale_v_ppi', 'ppi'), ['LVecBase4 const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_color_scale_v_pp', 'pp'), ['LVecBase4 const&']),
        ('d', 'v', 5, ('v', 'NodePath_C_set_color_scale_v_pffffi', 'pffffi'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'int']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_color_scale_v_pffff', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_color_scale_off'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_color_scale_off_v_pi', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath_C_set_color_scale_off_v_p', 'p'), []),
    ]
    c.ct['set_compass'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_compass_v_pp', 'pp'), ['NodePath const&']),
        ('d', 'v', 0, ('v', 'NodePath_C_set_compass_v_p', 'p'), []),
    ]
    c.ct['set_depth_offset'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_depth_offset_v_pii', 'pii'), ['int', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_depth_offset_v_pi', 'pi'), ['int']),
    ]
    c.ct['set_depth_test'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_depth_test_v_pBi', 'pBi'), ['bool', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_depth_test_v_pB', 'pB'), ['bool']),
    ]
    c.ct['set_depth_write'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_depth_write_v_pBi', 'pBi'), ['bool', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_depth_write_v_pB', 'pB'), ['bool']),
    ]
    c.ct['set_effect'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_effect_v_pp', 'pp'), ['RenderEffect const*']),
    ]
    c.ct['set_effects'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_effects_v_pp', 'pp'), ['RenderEffects const*']),
    ]
    c.ct['set_fluid_pos'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_fluid_pos_v_pp', 'pp'), ['LVecBase3 const&']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_fluid_pos_v_ppp', 'ppp'), ['NodePath const&', 'LVecBase3 const&']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_fluid_pos_v_ppfff', 'ppfff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_fluid_pos_v_pfff', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_fluid_x'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_fluid_x_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_fluid_x_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_fluid_y'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_fluid_y_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_fluid_y_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_fluid_z'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_fluid_z_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_fluid_z_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_fog'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_fog_v_ppi', 'ppi'), ['Fog*', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_fog_v_pp', 'pp'), ['Fog*']),
    ]
    c.ct['set_fog_off'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_fog_off_v_pi', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath_C_set_fog_off_v_p', 'p'), []),
    ]
    c.ct['set_h'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_h_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_h_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_hpr'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_hpr_v_pp', 'pp'), ['LVecBase3 const&']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_hpr_v_ppp', 'ppp'), ['NodePath const&', 'LVecBase3 const&']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_hpr_v_ppfff', 'ppfff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_hpr_v_pfff', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_hpr_scale'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_hpr_scale_v_ppp', 'ppp'), ['LVecBase3 const&', 'LVecBase3 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_hpr_scale_v_pppp', 'pppp'), ['NodePath const&', 'LVecBase3 const&', 'LVecBase3 const&']),
        ('d', 'v', 7, ('v', 'NodePath_C_set_hpr_scale_v_ppffffff', 'ppffffff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 6, ('v', 'NodePath_C_set_hpr_scale_v_pffffff', 'pffffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_instance_count'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_instance_count_v_pi', 'pi'), ['int']),
    ]
    c.ct['set_light'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_light_v_ppi', 'ppi'), ['NodePath const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_light_v_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['set_light_off'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_light_off_v_ppi', 'ppi'), ['NodePath const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_light_off_v_pp', 'pp'), ['NodePath const&']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_light_off_v_pi', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath_C_set_light_off_v_p', 'p'), []),
    ]
    c.ct['set_logic_op'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_logic_op_v_ppi', 'ppi'), ['LogicOpAttrib::Operation', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_logic_op_v_pp', 'pp'), ['LogicOpAttrib::Operation']),
    ]
    c.ct['set_mat'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_mat_v_pp', 'pp'), ['LMatrix4 const&']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_mat_v_ppp', 'ppp'), ['NodePath const&', 'LMatrix4 const&']),
    ]
    c.ct['set_material'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_material_v_ppi', 'ppi'), ['Material*', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_material_v_pp', 'pp'), ['Material*']),
    ]
    c.ct['set_material_off'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_material_off_v_pi', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath_C_set_material_off_v_p', 'p'), []),
    ]
    c.ct['set_name'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_name_v_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['set_occluder'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_occluder_v_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['set_p'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_p_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_p_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_pos'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_pos_v_pp', 'pp'), ['LVecBase3 const&']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_pos_v_ppp', 'ppp'), ['NodePath const&', 'LVecBase3 const&']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_pos_v_ppfff', 'ppfff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_pos_v_pfff', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_pos_hpr'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_pos_hpr_v_ppp', 'ppp'), ['LVecBase3 const&', 'LVecBase3 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_pos_hpr_v_pppp', 'pppp'), ['NodePath const&', 'LVecBase3 const&', 'LVecBase3 const&']),
        ('d', 'v', 7, ('v', 'NodePath_C_set_pos_hpr_v_ppffffff', 'ppffffff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 6, ('v', 'NodePath_C_set_pos_hpr_v_pffffff', 'pffffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_pos_hpr_scale'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_set_pos_hpr_scale_v_pppp', 'pppp'), ['LVecBase3 const&', 'LVecBase3 const&', 'LVecBase3 const&']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_pos_hpr_scale_v_ppppp', 'ppppp'), ['NodePath const&', 'LVecBase3 const&', 'LVecBase3 const&', 'LVecBase3 const&']),
        ('d', 'v', 10, ('v', 'NodePath_C_set_pos_hpr_scale_v_ppfffffffff', 'ppfffffffff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 9, ('v', 'NodePath_C_set_pos_hpr_scale_v_pfffffffff', 'pfffffffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_pos_hpr_scale_shear'] = [
        ('d', 'v', 4, ('v', 'NodePath_C_set_pos_hpr_scale_shear_v_ppppp', 'ppppp'), ['LVecBase3 const&', 'LVecBase3 const&', 'LVecBase3 const&', 'LVecBase3 const&']),
        ('d', 'v', 5, ('v', 'NodePath_C_set_pos_hpr_scale_shear_v_pppppp', 'pppppp'), ['NodePath const&', 'LVecBase3 const&', 'LVecBase3 const&', 'LVecBase3 const&', 'LVecBase3 const&']),
    ]
    c.ct['set_pos_quat'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_pos_quat_v_ppp', 'ppp'), ['LVecBase3 const&', 'LQuaternion const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_pos_quat_v_pppp', 'pppp'), ['NodePath const&', 'LVecBase3 const&', 'LQuaternion const&']),
    ]
    c.ct['set_pos_quat_scale'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_set_pos_quat_scale_v_pppp', 'pppp'), ['LVecBase3 const&', 'LQuaternion const&', 'LVecBase3 const&']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_pos_quat_scale_v_ppppp', 'ppppp'), ['NodePath const&', 'LVecBase3 const&', 'LQuaternion const&', 'LVecBase3 const&']),
    ]
    c.ct['set_pos_quat_scale_shear'] = [
        ('d', 'v', 4, ('v', 'NodePath_C_set_pos_quat_scale_shear_v_ppppp', 'ppppp'), ['LVecBase3 const&', 'LQuaternion const&', 'LVecBase3 const&', 'LVecBase3 const&']),
        ('d', 'v', 5, ('v', 'NodePath_C_set_pos_quat_scale_shear_v_pppppp', 'pppppp'), ['NodePath const&', 'LVecBase3 const&', 'LQuaternion const&', 'LVecBase3 const&', 'LVecBase3 const&']),
    ]
    c.ct['set_prev_transform'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_set_prev_transform_v_pppp', 'pppp'), ['NodePath const&', 'TransformState const*', 'Thread*']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_prev_transform_v_ppp', 'ppp'), ['NodePath const&', 'TransformState const*']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_prev_transform_v_ppp_1_v_ppp', 'ppp'), ['TransformState const*', 'Thread*']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_prev_transform_v_pp', 'pp'), ['TransformState const*']),
    ]
    c.ct['set_quat'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_quat_v_pp', 'pp'), ['LQuaternion const&']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_quat_v_ppp', 'ppp'), ['NodePath const&', 'LQuaternion const&']),
    ]
    c.ct['set_quat_scale'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_quat_scale_v_ppp', 'ppp'), ['LQuaternion const&', 'LVecBase3 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_quat_scale_v_pppp', 'pppp'), ['NodePath const&', 'LQuaternion const&', 'LVecBase3 const&']),
    ]
    c.ct['set_r'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_r_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_r_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_render_mode'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_set_render_mode_v_ppfi', 'ppfi'), ['RenderModeAttrib::Mode', 'PN_stdfloat', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_render_mode_v_ppf', 'ppf'), ['RenderModeAttrib::Mode', 'PN_stdfloat']),
    ]
    c.ct['set_render_mode_filled'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_render_mode_filled_v_pi', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath_C_set_render_mode_filled_v_p', 'p'), []),
    ]
    c.ct['set_render_mode_filled_wireframe'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_render_mode_filled_wireframe_v_ppi', 'ppi'), ['LColor const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_render_mode_filled_wireframe_v_pp', 'pp'), ['LColor const&']),
    ]
    c.ct['set_render_mode_perspective'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_render_mode_perspective_v_pBi', 'pBi'), ['bool', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_render_mode_perspective_v_pB', 'pB'), ['bool']),
    ]
    c.ct['set_render_mode_thickness'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_render_mode_thickness_v_pfi', 'pfi'), ['PN_stdfloat', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_render_mode_thickness_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_render_mode_wireframe'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_render_mode_wireframe_v_pi', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath_C_set_render_mode_wireframe_v_p', 'p'), []),
    ]
    c.ct['set_sa'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_sa_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_sb'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_sb_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_scale'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_scale_v_pp', 'pp'), ['LVecBase3 const&']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_scale_v_ppp', 'ppp'), ['NodePath const&', 'LVecBase3 const&']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_scale_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_scale_v_ppfff', 'ppfff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_scale_v_pf', 'pf'), ['PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_scale_v_pfff', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_scissor'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_scissor_v_ppp', 'ppp'), ['LPoint3 const&', 'LPoint3 const&']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_scissor_v_ppppp', 'ppppp'), ['LPoint3 const&', 'LPoint3 const&', 'LPoint3 const&', 'LPoint3 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_scissor_v_pppp', 'pppp'), ['NodePath const&', 'LPoint3 const&', 'LPoint3 const&']),
        ('d', 'v', 5, ('v', 'NodePath_C_set_scissor_v_pppppp', 'pppppp'), ['NodePath const&', 'LPoint3 const&', 'LPoint3 const&', 'LPoint3 const&', 'LPoint3 const&']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_scissor_v_pffff', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_sg'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_sg_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_shader'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_v_ppi', 'ppi'), ['Shader const*', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_shader_v_pp', 'pp'), ['Shader const*']),
    ]
    c.ct['set_shader_auto'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_auto_v_ppi', 'ppi'), ['BitMask32', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_shader_auto_v_pp', 'pp'), ['BitMask32']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_shader_auto_v_pi', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath_C_set_shader_auto_v_p', 'p'), []),
    ]
    c.ct['set_shader_input'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi', 'pspi'), ['CPT_InternalName', 'LMatrix3 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp', 'psp'), ['CPT_InternalName', 'LMatrix3 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi', 'pspi'), ['CPT_InternalName', 'LMatrix4 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp', 'psp'), ['CPT_InternalName', 'LMatrix4 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi', 'pspi'), ['CPT_InternalName', 'LVecBase2 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp', 'psp'), ['CPT_InternalName', 'LVecBase2 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi', 'pspi'), ['CPT_InternalName', 'LVecBase2i const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp', 'psp'), ['CPT_InternalName', 'LVecBase2i const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi_4_v_pspi', 'pspi'), ['CPT_InternalName', 'LVecBase3 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp_4_v_psp', 'psp'), ['CPT_InternalName', 'LVecBase3 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi_4_v_pspi_5_v_pspi', 'pspi'), ['CPT_InternalName', 'LVecBase3i const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp_4_v_psp_5_v_psp', 'psp'), ['CPT_InternalName', 'LVecBase3i const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi_4_v_pspi_5_v_pspi_6_v_pspi', 'pspi'), ['CPT_InternalName', 'LVecBase4 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp_4_v_psp_5_v_psp_6_v_psp', 'psp'), ['CPT_InternalName', 'LVecBase4 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi_4_v_pspi_5_v_pspi_6_v_pspi_7_v_pspi', 'pspi'), ['CPT_InternalName', 'LVecBase4i const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp_4_v_psp_5_v_psp_6_v_psp_7_v_psp', 'psp'), ['CPT_InternalName', 'LVecBase4i const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi_4_v_pspi_5_v_pspi_6_v_pspi_7_v_pspi_8_v_pspi', 'pspi'), ['CPT_InternalName', 'NodePath const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp_4_v_psp_5_v_psp_6_v_psp_7_v_psp_8_v_psp', 'psp'), ['CPT_InternalName', 'NodePath const&']),
        ('d', 'v', 6, ('v', 'NodePath_C_set_shader_input_v_psffffi', 'psffffi'), ['CPT_InternalName', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'int']),
        ('d', 'v', 5, ('v', 'NodePath_C_set_shader_input_v_psffff', 'psffff'), ['CPT_InternalName', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_shader_input_v_psfff', 'psfff'), ['CPT_InternalName', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_psff', 'psff'), ['CPT_InternalName', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi_4_v_pspi_5_v_pspi_6_v_pspi_7_v_pspi_8_v_pspi_9_v_pspi', 'pspi'), ['CPT_InternalName', 'PTA_LMatrix3 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp_4_v_psp_5_v_psp_6_v_psp_7_v_psp_8_v_psp_9_v_psp', 'psp'), ['CPT_InternalName', 'PTA_LMatrix3 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi_4_v_pspi_5_v_pspi_6_v_pspi_7_v_pspi_8_v_pspi_9_v_pspi_10_v_pspi', 'pspi'), ['CPT_InternalName', 'PTA_LMatrix4 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp_4_v_psp_5_v_psp_6_v_psp_7_v_psp_8_v_psp_9_v_psp_10_v_psp', 'psp'), ['CPT_InternalName', 'PTA_LMatrix4 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi_4_v_pspi_5_v_pspi_6_v_pspi_7_v_pspi_8_v_pspi_9_v_pspi_10_v_pspi_11_v_pspi', 'pspi'), ['CPT_InternalName', 'PTA_LVecBase2 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp_4_v_psp_5_v_psp_6_v_psp_7_v_psp_8_v_psp_9_v_psp_10_v_psp_11_v_psp', 'psp'), ['CPT_InternalName', 'PTA_LVecBase2 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi_4_v_pspi_5_v_pspi_6_v_pspi_7_v_pspi_8_v_pspi_9_v_pspi_10_v_pspi_11_v_pspi_12_v_pspi', 'pspi'), ['CPT_InternalName', 'PTA_LVecBase2i const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp_4_v_psp_5_v_psp_6_v_psp_7_v_psp_8_v_psp_9_v_psp_10_v_psp_11_v_psp_12_v_psp', 'psp'), ['CPT_InternalName', 'PTA_LVecBase2i const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi_4_v_pspi_5_v_pspi_6_v_pspi_7_v_pspi_8_v_pspi_9_v_pspi_10_v_pspi_11_v_pspi_12_v_pspi_13_v_pspi', 'pspi'), ['CPT_InternalName', 'PTA_LVecBase3 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp_4_v_psp_5_v_psp_6_v_psp_7_v_psp_8_v_psp_9_v_psp_10_v_psp_11_v_psp_12_v_psp_13_v_psp', 'psp'), ['CPT_InternalName', 'PTA_LVecBase3 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi_4_v_pspi_5_v_pspi_6_v_pspi_7_v_pspi_8_v_pspi_9_v_pspi_10_v_pspi_11_v_pspi_12_v_pspi_13_v_pspi_14_v_pspi', 'pspi'), ['CPT_InternalName', 'PTA_LVecBase3i const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp_4_v_psp_5_v_psp_6_v_psp_7_v_psp_8_v_psp_9_v_psp_10_v_psp_11_v_psp_12_v_psp_13_v_psp_14_v_psp', 'psp'), ['CPT_InternalName', 'PTA_LVecBase3i const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi_4_v_pspi_5_v_pspi_6_v_pspi_7_v_pspi_8_v_pspi_9_v_pspi_10_v_pspi_11_v_pspi_12_v_pspi_13_v_pspi_14_v_pspi_15_v_pspi', 'pspi'), ['CPT_InternalName', 'PTA_LVecBase4 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp_4_v_psp_5_v_psp_6_v_psp_7_v_psp_8_v_psp_9_v_psp_10_v_psp_11_v_psp_12_v_psp_13_v_psp_14_v_psp_15_v_psp', 'psp'), ['CPT_InternalName', 'PTA_LVecBase4 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi_4_v_pspi_5_v_pspi_6_v_pspi_7_v_pspi_8_v_pspi_9_v_pspi_10_v_pspi_11_v_pspi_12_v_pspi_13_v_pspi_14_v_pspi_15_v_pspi_16_v_pspi', 'pspi'), ['CPT_InternalName', 'PTA_LVecBase4i const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp_4_v_psp_5_v_psp_6_v_psp_7_v_psp_8_v_psp_9_v_psp_10_v_psp_11_v_psp_12_v_psp_13_v_psp_14_v_psp_15_v_psp_16_v_psp', 'psp'), ['CPT_InternalName', 'PTA_LVecBase4i const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi_4_v_pspi_5_v_pspi_6_v_pspi_7_v_pspi_8_v_pspi_9_v_pspi_10_v_pspi_11_v_pspi_12_v_pspi_13_v_pspi_14_v_pspi_15_v_pspi_16_v_pspi_17_v_pspi', 'pspi'), ['CPT_InternalName', 'PTA_double const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp_4_v_psp_5_v_psp_6_v_psp_7_v_psp_8_v_psp_9_v_psp_10_v_psp_11_v_psp_12_v_psp_13_v_psp_14_v_psp_15_v_psp_16_v_psp_17_v_psp', 'psp'), ['CPT_InternalName', 'PTA_double const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi_4_v_pspi_5_v_pspi_6_v_pspi_7_v_pspi_8_v_pspi_9_v_pspi_10_v_pspi_11_v_pspi_12_v_pspi_13_v_pspi_14_v_pspi_15_v_pspi_16_v_pspi_17_v_pspi_18_v_pspi', 'pspi'), ['CPT_InternalName', 'PTA_float const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp_4_v_psp_5_v_psp_6_v_psp_7_v_psp_8_v_psp_9_v_psp_10_v_psp_11_v_psp_12_v_psp_13_v_psp_14_v_psp_15_v_psp_16_v_psp_17_v_psp_18_v_psp', 'psp'), ['CPT_InternalName', 'PTA_float const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi_4_v_pspi_5_v_pspi_6_v_pspi_7_v_pspi_8_v_pspi_9_v_pspi_10_v_pspi_11_v_pspi_12_v_pspi_13_v_pspi_14_v_pspi_15_v_pspi_16_v_pspi_17_v_pspi_18_v_pspi_19_v_pspi', 'pspi'), ['CPT_InternalName', 'PTA_int const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp_4_v_psp_5_v_psp_6_v_psp_7_v_psp_8_v_psp_9_v_psp_10_v_psp_11_v_psp_12_v_psp_13_v_psp_14_v_psp_15_v_psp_16_v_psp_17_v_psp_18_v_psp_19_v_psp', 'psp'), ['CPT_InternalName', 'PTA_int const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi_4_v_pspi_5_v_pspi_6_v_pspi_7_v_pspi_8_v_pspi_9_v_pspi_10_v_pspi_11_v_pspi_12_v_pspi_13_v_pspi_14_v_pspi_15_v_pspi_16_v_pspi_17_v_pspi_18_v_pspi_19_v_pspi_20_v_pspi', 'pspi'), ['CPT_InternalName', 'ShaderBuffer*', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp_4_v_psp_5_v_psp_6_v_psp_7_v_psp_8_v_psp_9_v_psp_10_v_psp_11_v_psp_12_v_psp_13_v_psp_14_v_psp_15_v_psp_16_v_psp_17_v_psp_18_v_psp_19_v_psp_20_v_psp', 'psp'), ['CPT_InternalName', 'ShaderBuffer*']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_shader_input_v_psppi', 'psppi'), ['CPT_InternalName', 'Texture*', 'SamplerState const&', 'int']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspp', 'pspp'), ['CPT_InternalName', 'Texture*', 'SamplerState const&']),
        ('d', 'v', 7, ('v', 'NodePath_C_set_shader_input_v_pspBBiii', 'pspBBiii'), ['CPT_InternalName', 'Texture*', 'bool', 'bool', 'int', 'int', 'int']),
        ('d', 'v', 6, ('v', 'NodePath_C_set_shader_input_v_pspBBii', 'pspBBii'), ['CPT_InternalName', 'Texture*', 'bool', 'bool', 'int', 'int']),
        ('d', 'v', 5, ('v', 'NodePath_C_set_shader_input_v_pspBBi', 'pspBBi'), ['CPT_InternalName', 'Texture*', 'bool', 'bool', 'int']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_shader_input_v_pspBB', 'pspBB'), ['CPT_InternalName', 'Texture*', 'bool', 'bool']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_pspi_1_v_pspi_2_v_pspi_3_v_pspi_4_v_pspi_5_v_pspi_6_v_pspi_7_v_pspi_8_v_pspi_9_v_pspi_10_v_pspi_11_v_pspi_12_v_pspi_13_v_pspi_14_v_pspi_15_v_pspi_16_v_pspi_17_v_pspi_18_v_pspi_19_v_pspi_20_v_pspi_21_v_pspi', 'pspi'), ['CPT_InternalName', 'Texture*', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shader_input_v_psp_1_v_psp_2_v_psp_3_v_psp_4_v_psp_5_v_psp_6_v_psp_7_v_psp_8_v_psp_9_v_psp_10_v_psp_11_v_psp_12_v_psp_13_v_psp_14_v_psp_15_v_psp_16_v_psp_17_v_psp_18_v_psp_19_v_psp_20_v_psp_21_v_psp', 'psp'), ['CPT_InternalName', 'Texture*']),
        ('d', 'v', 6, ('v', 'NodePath_C_set_shader_input_v_psiiiii', 'psiiiii'), ['CPT_InternalName', 'int', 'int', 'int', 'int', 'int']),
        ('d', 'v', 5, ('v', 'NodePath_C_set_shader_input_v_psiiii', 'psiiii'), ['CPT_InternalName', 'int', 'int', 'int', 'int']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_shader_input_v_psiii', 'psiii'), ['CPT_InternalName', 'int', 'int', 'int']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shader_input_v_psii', 'psii'), ['CPT_InternalName', 'int', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_shader_input_v_pp', 'pp'), ['ShaderInput&&']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_shader_input_v_pp_1_v_pp', 'pp'), ['ShaderInput const&']),
    ]
    c.ct['set_shader_off'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_shader_off_v_pi', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath_C_set_shader_off_v_p', 'p'), []),
    ]
    c.ct['set_shear'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_shear_v_pp', 'pp'), ['LVecBase3 const&']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_shear_v_ppp', 'ppp'), ['NodePath const&', 'LVecBase3 const&']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_shear_v_ppfff', 'ppfff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_shear_v_pfff', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_shxy'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_shxy_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_shxy_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_shxz'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_shxz_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_shxz_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_shyz'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_shyz_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_shyz_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_sr'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_set_sr_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_state'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_set_state_v_pppp', 'pppp'), ['NodePath const&', 'RenderState const*', 'Thread*']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_state_v_ppp', 'ppp'), ['NodePath const&', 'RenderState const*']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_state_v_ppp_1_v_ppp', 'ppp'), ['RenderState const*', 'Thread*']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_state_v_pp', 'pp'), ['RenderState const*']),
    ]
    c.ct['set_sx'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_sx_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_sx_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_sy'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_sy_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_sy_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_sz'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_sz_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_sz_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_tag'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_tag_v_pss', 'pss'), ['std::string const&', 'std::string const&']),
    ]
    c.ct['set_tex_gen'] = [
        ('d', 'v', 4, ('v', 'NodePath_C_set_tex_gen_v_ppppi', 'ppppi'), ['TextureStage*', 'RenderAttrib::TexGenMode', 'LTexCoord3 const&', 'int']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_tex_gen_v_pppp', 'pppp'), ['TextureStage*', 'RenderAttrib::TexGenMode', 'LTexCoord3 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_tex_gen_v_pppi', 'pppi'), ['TextureStage*', 'RenderAttrib::TexGenMode', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_tex_gen_v_ppp', 'ppp'), ['TextureStage*', 'RenderAttrib::TexGenMode']),
    ]
    c.ct['set_tex_hpr'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_set_tex_hpr_v_pppp', 'pppp'), ['NodePath const&', 'TextureStage*', 'LVecBase3 const&']),
        ('d', 'v', 5, ('v', 'NodePath_C_set_tex_hpr_v_pppfff', 'pppfff'), ['NodePath const&', 'TextureStage*', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_tex_hpr_v_ppp', 'ppp'), ['TextureStage*', 'LVecBase3 const&']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_tex_hpr_v_ppfff', 'ppfff'), ['TextureStage*', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_tex_offset'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_set_tex_offset_v_pppp', 'pppp'), ['NodePath const&', 'TextureStage*', 'LVecBase2 const&']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_tex_offset_v_pppff', 'pppff'), ['NodePath const&', 'TextureStage*', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_tex_offset_v_ppp', 'ppp'), ['TextureStage*', 'LVecBase2 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_tex_offset_v_ppff', 'ppff'), ['TextureStage*', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_tex_pos'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_set_tex_pos_v_pppp', 'pppp'), ['NodePath const&', 'TextureStage*', 'LVecBase3 const&']),
        ('d', 'v', 5, ('v', 'NodePath_C_set_tex_pos_v_pppfff', 'pppfff'), ['NodePath const&', 'TextureStage*', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_tex_pos_v_ppp', 'ppp'), ['TextureStage*', 'LVecBase3 const&']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_tex_pos_v_ppfff', 'ppfff'), ['TextureStage*', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_tex_projector'] = [
        ('d', 'v', 4, ('v', 'NodePath_C_set_tex_projector_v_ppppi', 'ppppi'), ['TextureStage*', 'NodePath const&', 'NodePath const&', 'int']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_tex_projector_v_pppp', 'pppp'), ['TextureStage*', 'NodePath const&', 'NodePath const&']),
    ]
    c.ct['set_tex_rotate'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_set_tex_rotate_v_pppf', 'pppf'), ['NodePath const&', 'TextureStage*', 'PN_stdfloat']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_tex_rotate_v_ppf', 'ppf'), ['TextureStage*', 'PN_stdfloat']),
    ]
    c.ct['set_tex_scale'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_set_tex_scale_v_pppp', 'pppp'), ['NodePath const&', 'TextureStage*', 'LVecBase2 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_tex_scale_v_pppp_1_v_pppp', 'pppp'), ['NodePath const&', 'TextureStage*', 'LVecBase3 const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_tex_scale_v_pppf', 'pppf'), ['NodePath const&', 'TextureStage*', 'PN_stdfloat']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_tex_scale_v_pppff', 'pppff'), ['NodePath const&', 'TextureStage*', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 5, ('v', 'NodePath_C_set_tex_scale_v_pppfff', 'pppfff'), ['NodePath const&', 'TextureStage*', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_tex_scale_v_ppp', 'ppp'), ['TextureStage*', 'LVecBase2 const&']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_tex_scale_v_ppp_1_v_ppp', 'ppp'), ['TextureStage*', 'LVecBase3 const&']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_tex_scale_v_ppf', 'ppf'), ['TextureStage*', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_tex_scale_v_ppff', 'ppff'), ['TextureStage*', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_tex_scale_v_ppfff', 'ppfff'), ['TextureStage*', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_tex_transform'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_set_tex_transform_v_pppp', 'pppp'), ['NodePath const&', 'TextureStage*', 'TransformState const*']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_tex_transform_v_ppp', 'ppp'), ['TextureStage*', 'TransformState const*']),
    ]
    c.ct['set_texture'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_set_texture_v_pppi', 'pppi'), ['Texture*', 'SamplerState const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_texture_v_ppp', 'ppp'), ['Texture*', 'SamplerState const&']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_texture_v_ppi', 'ppi'), ['Texture*', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_texture_v_pp', 'pp'), ['Texture*']),
        ('d', 'v', 4, ('v', 'NodePath_C_set_texture_v_ppppi', 'ppppi'), ['TextureStage*', 'Texture*', 'SamplerState const&', 'int']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_texture_v_pppp', 'pppp'), ['TextureStage*', 'Texture*', 'SamplerState const&']),
        ('d', 'v', 3, ('v', 'NodePath_C_set_texture_v_pppi_1_v_pppi', 'pppi'), ['TextureStage*', 'Texture*', 'int']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_texture_v_ppp_1_v_ppp', 'ppp'), ['TextureStage*', 'Texture*']),
    ]
    c.ct['set_texture_off'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_texture_off_v_ppi', 'ppi'), ['TextureStage*', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_texture_off_v_pp', 'pp'), ['TextureStage*']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_texture_off_v_pi', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath_C_set_texture_off_v_p', 'p'), []),
    ]
    c.ct['set_transform'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_set_transform_v_pppp', 'pppp'), ['NodePath const&', 'TransformState const*', 'Thread*']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_transform_v_ppp', 'ppp'), ['NodePath const&', 'TransformState const*']),
        ('d', 'v', 2, ('v', 'NodePath_C_set_transform_v_ppp_1_v_ppp', 'ppp'), ['TransformState const*', 'Thread*']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_transform_v_pp', 'pp'), ['TransformState const*']),
    ]
    c.ct['set_transparency'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_transparency_v_ppi', 'ppi'), ['TransparencyAttrib::Mode', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_transparency_v_pp', 'pp'), ['TransparencyAttrib::Mode']),
    ]
    c.ct['set_two_sided'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_two_sided_v_pBi', 'pBi'), ['bool', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_two_sided_v_pB', 'pB'), ['bool']),
    ]
    c.ct['set_x'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_x_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_x_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_y'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_y_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_y_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_z'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_set_z_v_ppf', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath_C_set_z_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['show'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_show_v_p', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath_C_show_v_pp', 'pp'), ['DrawMask']),
    ]
    c.ct['show_bounds'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_show_bounds_v_p', 'p'), []),
    ]
    c.ct['show_through'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_show_through_v_p', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath_C_show_through_v_pp', 'pp'), ['DrawMask']),
    ]
    c.ct['show_tight_bounds'] = [
        ('d', 'v', 0, ('v', 'NodePath_C_show_tight_bounds_v_p', 'p'), []),
    ]
    c.ct['stash'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_stash_v_pip', 'pip'), ['int', 'Thread*']),
        ('d', 'v', 1, ('v', 'NodePath_C_stash_v_pi', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath_C_stash_v_p', 'p'), []),
    ]
    c.ct['stash_to'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_stash_to_v_ppip', 'ppip'), ['NodePath const&', 'int', 'Thread*']),
        ('d', 'v', 2, ('v', 'NodePath_C_stash_to_v_ppi', 'ppi'), ['NodePath const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_stash_to_v_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['unify_texture_stages'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_unify_texture_stages_v_pp', 'pp'), ['TextureStage*']),
    ]
    c.ct['unstash'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_unstash_v_pip', 'pip'), ['int', 'Thread*']),
        ('d', 'v', 1, ('v', 'NodePath_C_unstash_v_pi', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath_C_unstash_v_p', 'p'), []),
    ]
    c.ct['unstash_all'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_unstash_all_v_pp', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'NodePath_C_unstash_all_v_p', 'p'), []),
    ]
    c.ct['verify_complete'] = [
        ('d', 'B', 1, ('B', 'NodePath_C_verify_complete_B_pp', 'pp'), ['Thread*']),
        ('d', 'B', 0, ('B', 'NodePath_C_verify_complete_B_p', 'p'), []),
    ]
    c.ct['write_bam_file'] = [
        ('d', 'B', 1, ('B', 'NodePath_C_write_bam_file_B_pp', 'pp'), ['Filename const&']),
    ]
    c.ct['write_bam_stream'] = [
        ('d', 'B', 1, ('B', 'NodePath_C_write_bam_stream_B_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['write_bounds'] = [
        ('d', 'v', 1, ('v', 'NodePath_C_write_bounds_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'NodePath_C_write_datagram_v_ppp', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]
    c.ct['wrt_reparent_to'] = [
        ('d', 'v', 3, ('v', 'NodePath_C_wrt_reparent_to_v_ppip', 'ppip'), ['NodePath const&', 'int', 'Thread*']),
        ('d', 'v', 2, ('v', 'NodePath_C_wrt_reparent_to_v_ppi', 'ppi'), ['NodePath const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath_C_wrt_reparent_to_v_pp', 'pp'), ['NodePath const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(NodePath, attr, self)

NodePath.c.link(NodePath)



class NodePathCollection(cxx.cplusplus):

    c = cxx.cstructs()
    c.register("NodePathCollection", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 8, 0, ('p', 'NodePathCollection_C_ctor_p_v', ''), []),
        ('s', 8, 1, ('p', 'NodePathCollection_C_ctor_p_p', 'p'), ['NodePathCollection const&']),
    ]

    # classmethod type calls


    # instance method type calls

    c.ct['add_path'] = [
        ('d', 'v', 1, ('v', 'NodePathCollection_C_add_path_v_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['add_paths_from'] = [
        ('d', 'v', 1, ('v', 'NodePathCollection_C_add_paths_from_v_pp', 'pp'), ['NodePathCollection const&']),
    ]
    c.ct['append'] = [
        ('d', 'v', 1, ('v', 'NodePathCollection_C_append_v_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['calc_tight_bounds'] = [
        ('d', 'B', 2, ('B', 'NodePathCollection_C_calc_tight_bounds_B_ppp', 'ppp'), ['LPoint3&', 'LPoint3&']),
    ]
    c.ct['clear'] = [
        ('d', 'v', 0, ('v', 'NodePathCollection_C_clear_v_p', 'p'), []),
    ]
    c.ct['compose_color_scale'] = [
        ('d', 'v', 2, ('v', 'NodePathCollection_C_compose_color_scale_v_ppi', 'ppi'), ['LVecBase4 const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePathCollection_C_compose_color_scale_v_pp', 'pp'), ['LVecBase4 const&']),
        ('d', 'v', 5, ('v', 'NodePathCollection_C_compose_color_scale_v_pffffi', 'pffffi'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'int']),
        ('d', 'v', 4, ('v', 'NodePathCollection_C_compose_color_scale_v_pffff', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePathCollection_C_compose_color_scale_v_pfff', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['detach'] = [
        ('d', 'v', 0, ('v', 'NodePathCollection_C_detach_v_p', 'p'), []),
    ]
    c.ct['extend'] = [
        ('d', 'v', 1, ('v', 'NodePathCollection_C_extend_v_pp', 'pp'), ['NodePathCollection const&']),
    ]
    c.ct['find_all_matches'] = [
        ('d', 8, 1, ('p', 'NodePathCollection_C_find_all_matches_p_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['get_collide_mask'] = [
        ('d', 'p', 0, ('p', 'NodePathCollection_C_get_collide_mask_p_p', 'p'), []),
    ]
    c.ct['get_num_paths'] = [
        ('d', 'i', 0, ('i', 'NodePathCollection_C_get_num_paths_i_p', 'p'), []),
    ]
    c.ct['get_path'] = [
        ('d', 7, 1, ('p', 'NodePathCollection_C_get_path_p_pi', 'pi'), ['int']),
    ]
    c.ct['has_path'] = [
        ('d', 'B', 1, ('B', 'NodePathCollection_C_has_path_B_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['hide'] = [
        ('d', 'v', 0, ('v', 'NodePathCollection_C_hide_v_p', 'p'), []),
    ]
    c.ct['is_empty'] = [
        ('d', 'B', 0, ('B', 'NodePathCollection_C_is_empty_B_p', 'p'), []),
    ]
    c.ct['ls'] = [
        ('d', 'v', 0, ('v', 'NodePathCollection_C_ls_v_p', 'p'), []),
        ('d', 'v', 2, ('v', 'NodePathCollection_C_ls_v_ppi', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'v', 1, ('v', 'NodePathCollection_C_ls_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'NodePathCollection_C_output_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['remove_duplicate_paths'] = [
        ('d', 'v', 0, ('v', 'NodePathCollection_C_remove_duplicate_paths_v_p', 'p'), []),
    ]
    c.ct['remove_path'] = [
        ('d', 'B', 1, ('B', 'NodePathCollection_C_remove_path_B_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['remove_paths_from'] = [
        ('d', 'v', 1, ('v', 'NodePathCollection_C_remove_paths_from_v_pp', 'pp'), ['NodePathCollection const&']),
    ]
    c.ct['reparent_to'] = [
        ('d', 'v', 1, ('v', 'NodePathCollection_C_reparent_to_v_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['reserve'] = [
        ('d', 'v', 1, ('v', 'NodePathCollection_C_reserve_v_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['set_attrib'] = [
        ('d', 'v', 2, ('v', 'NodePathCollection_C_set_attrib_v_ppi', 'ppi'), ['RenderAttrib const*', 'int']),
        ('d', 'v', 1, ('v', 'NodePathCollection_C_set_attrib_v_pp', 'pp'), ['RenderAttrib const*']),
    ]
    c.ct['set_collide_mask'] = [
        ('d', 'v', 3, ('v', 'NodePathCollection_C_set_collide_mask_v_pppi', 'pppi'), ['CollideMask', 'CollideMask', 'TypeHandle']),
        ('d', 'v', 2, ('v', 'NodePathCollection_C_set_collide_mask_v_ppp', 'ppp'), ['CollideMask', 'CollideMask']),
        ('d', 'v', 1, ('v', 'NodePathCollection_C_set_collide_mask_v_pp', 'pp'), ['CollideMask']),
    ]
    c.ct['set_color'] = [
        ('d', 'v', 2, ('v', 'NodePathCollection_C_set_color_v_ppi', 'ppi'), ['LColor const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePathCollection_C_set_color_v_pp', 'pp'), ['LColor const&']),
        ('d', 'v', 5, ('v', 'NodePathCollection_C_set_color_v_pffffi', 'pffffi'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'int']),
        ('d', 'v', 4, ('v', 'NodePathCollection_C_set_color_v_pffff', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePathCollection_C_set_color_v_pfff', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_color_scale'] = [
        ('d', 'v', 2, ('v', 'NodePathCollection_C_set_color_scale_v_ppi', 'ppi'), ['LVecBase4 const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePathCollection_C_set_color_scale_v_pp', 'pp'), ['LVecBase4 const&']),
        ('d', 'v', 5, ('v', 'NodePathCollection_C_set_color_scale_v_pffffi', 'pffffi'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'int']),
        ('d', 'v', 4, ('v', 'NodePathCollection_C_set_color_scale_v_pffff', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePathCollection_C_set_color_scale_v_pfff', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_texture'] = [
        ('d', 'v', 2, ('v', 'NodePathCollection_C_set_texture_v_ppi', 'ppi'), ['Texture*', 'int']),
        ('d', 'v', 1, ('v', 'NodePathCollection_C_set_texture_v_pp', 'pp'), ['Texture*']),
        ('d', 'v', 3, ('v', 'NodePathCollection_C_set_texture_v_pppi', 'pppi'), ['TextureStage*', 'Texture*', 'int']),
        ('d', 'v', 2, ('v', 'NodePathCollection_C_set_texture_v_ppp', 'ppp'), ['TextureStage*', 'Texture*']),
    ]
    c.ct['set_texture_off'] = [
        ('d', 'v', 2, ('v', 'NodePathCollection_C_set_texture_off_v_ppi', 'ppi'), ['TextureStage*', 'int']),
        ('d', 'v', 1, ('v', 'NodePathCollection_C_set_texture_off_v_pp', 'pp'), ['TextureStage*']),
        ('d', 'v', 1, ('v', 'NodePathCollection_C_set_texture_off_v_pi', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePathCollection_C_set_texture_off_v_p', 'p'), []),
    ]
    c.ct['show'] = [
        ('d', 'v', 0, ('v', 'NodePathCollection_C_show_v_p', 'p'), []),
    ]
    c.ct['size'] = [
        ('d', 'p', 0, ('p', 'NodePathCollection_C_size_p_p', 'p'), []),
    ]
    c.ct['stash'] = [
        ('d', 'v', 0, ('v', 'NodePathCollection_C_stash_v_p', 'p'), []),
    ]
    c.ct['unstash'] = [
        ('d', 'v', 0, ('v', 'NodePathCollection_C_unstash_v_p', 'p'), []),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'NodePathCollection_C_write_v_ppi', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'v', 1, ('v', 'NodePathCollection_C_write_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['wrt_reparent_to'] = [
        ('d', 'v', 1, ('v', 'NodePathCollection_C_wrt_reparent_to_v_pp', 'pp'), ['NodePath const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(NodePathCollection, attr, self)

NodePathCollection.c.link(NodePathCollection)



class PandaFramework(cxx.cplusplus):

    c = cxx.cstructs()
    c.register("PandaFramework", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 9, 0, ('p', 'PandaFramework_C_ctor_p_v', ''), []),
        ('s', 9, 1, ('p', 'PandaFramework_C_ctor_p_p', 'p'), ['PandaFramework const&']),
    ]

    # classmethod type calls

    c.ct['hide_collision_solids'] = [
        ('s', 'i', 1, ('i', 'PandaFramework_C_hide_collision_solids_i_p', 'p'), ['NodePath']),
    ]
    c.ct['show_collision_solids'] = [
        ('s', 'i', 1, ('i', 'PandaFramework_C_show_collision_solids_i_p', 'p'), ['NodePath']),
    ]

    @classmethod
    def hide_collision_solids(cls, *args,**kw):
        return ( cls.c.get('hide_collision_solids', None) or cls.c.call(PandaFramework, 'hide_collision_solids', None) )(*args,**kw)

    @classmethod
    def show_collision_solids(cls, *args,**kw):
        return ( cls.c.get('show_collision_solids', None) or cls.c.call(PandaFramework, 'show_collision_solids', None) )(*args,**kw)

    # instance method type calls

    c.ct['all_windows_closed'] = [
        ('d', 'B', 0, ('B', 'PandaFramework_C_all_windows_closed_B_p', 'p'), []),
    ]
    c.ct['clear_exit_flag'] = [
        ('d', 'v', 0, ('v', 'PandaFramework_C_clear_exit_flag_v_p', 'p'), []),
    ]
    c.ct['clear_highlight'] = [
        ('d', 'v', 0, ('v', 'PandaFramework_C_clear_highlight_v_p', 'p'), []),
    ]
    c.ct['close_all_windows'] = [
        ('d', 'v', 0, ('v', 'PandaFramework_C_close_all_windows_v_p', 'p'), []),
    ]
    c.ct['close_framework'] = [
        ('d', 'v', 0, ('v', 'PandaFramework_C_close_framework_v_p', 'p'), []),
    ]
    c.ct['close_window'] = [
        ('d', 'v', 1, ('v', 'PandaFramework_C_close_window_v_pp', 'pp'), ['WindowFramework*']),
        ('d', 'v', 1, ('v', 'PandaFramework_C_close_window_v_pi', 'pi'), ['int']),
    ]
    c.ct['do_frame'] = [
        ('d', 'B', 1, ('B', 'PandaFramework_C_do_frame_B_pp', 'pp'), ['Thread*']),
    ]
    c.ct['enable_default_keys'] = [
        ('d', 'v', 0, ('v', 'PandaFramework_C_enable_default_keys_v_p', 'p'), []),
    ]
    c.ct['find_window'] = [
        ('d', 'i', 1, ('i', 'PandaFramework_C_find_window_i_pp', 'pp'), ['GraphicsOutput const*']),
        ('d', 'i', 1, ('i', 'PandaFramework_C_find_window_i_pp_1_i_pp', 'pp'), ['WindowFramework const*']),
    ]
    c.ct['get_background_type'] = [
        ('d', 'p', 0, ('p', 'PandaFramework_C_get_background_type_p_p', 'p'), []),
    ]
    c.ct['get_data_root'] = [
        ('d', 7, 0, ('p', 'PandaFramework_C_get_data_root_p_p', 'p'), []),
    ]
    c.ct['get_default_pipe'] = [
        ('d', 'p', 0, ('p', 'PandaFramework_C_get_default_pipe_p_p', 'p'), []),
    ]
    c.ct['get_default_window_props'] = [
        ('d', 'v', 1, ('v', 'PandaFramework_C_get_default_window_props_v_pp', 'pp'), ['WindowProperties&']),
    ]
    c.ct['get_event_handler'] = [
        ('d', 'p', 0, ('p', 'PandaFramework_C_get_event_handler_p_p', 'p'), []),
    ]
    c.ct['get_graphics_engine'] = [
        ('d', 'p', 0, ('p', 'PandaFramework_C_get_graphics_engine_p_p', 'p'), []),
    ]
    c.ct['get_highlight'] = [
        ('d', 7, 0, ('p', 'PandaFramework_C_get_highlight_p_p', 'p'), []),
    ]
    c.ct['get_lighting'] = [
        ('d', 'B', 0, ('B', 'PandaFramework_C_get_lighting_B_p', 'p'), []),
    ]
    c.ct['get_models'] = [
        ('d', 7, 0, ('p', 'PandaFramework_C_get_models_p_p', 'p'), []),
    ]
    c.ct['get_mouse'] = [
        ('d', 7, 1, ('p', 'PandaFramework_C_get_mouse_p_pp', 'pp'), ['GraphicsOutput*']),
    ]
    c.ct['get_num_windows'] = [
        ('d', 'i', 0, ('i', 'PandaFramework_C_get_num_windows_i_p', 'p'), []),
    ]
    c.ct['get_perpixel'] = [
        ('d', 'B', 0, ('B', 'PandaFramework_C_get_perpixel_B_p', 'p'), []),
    ]
    c.ct['get_recorder'] = [
        ('d', 'p', 0, ('p', 'PandaFramework_C_get_recorder_p_p', 'p'), []),
    ]
    c.ct['get_task_mgr'] = [
        ('d', 'p', 0, ('p', 'PandaFramework_C_get_task_mgr_p_p', 'p'), []),
    ]
    c.ct['get_texture'] = [
        ('d', 'B', 0, ('B', 'PandaFramework_C_get_texture_B_p', 'p'), []),
    ]
    c.ct['get_two_sided'] = [
        ('d', 'B', 0, ('B', 'PandaFramework_C_get_two_sided_B_p', 'p'), []),
    ]
    c.ct['get_window'] = [
        ('d', 20, 1, ('p', 'PandaFramework_C_get_window_p_pi', 'pi'), ['int']),
    ]
    c.ct['get_wireframe'] = [
        ('d', 'B', 0, ('B', 'PandaFramework_C_get_wireframe_B_p', 'p'), []),
    ]
    c.ct['has_highlight'] = [
        ('d', 'B', 0, ('B', 'PandaFramework_C_has_highlight_B_p', 'p'), []),
    ]
    c.ct['main_loop'] = [
        ('d', 'v', 0, ('v', 'PandaFramework_C_main_loop_v_p', 'p'), []),
    ]
    c.ct['open_framework'] = [
        ('d', 'v', 0, ('v', 'PandaFramework_C_open_framework_v_p', 'p'), []),
    ]
    c.ct['open_window'] = [
        ('d', 20, 0, ('p', 'PandaFramework_C_open_window_p_p', 'p'), []),
        ('d', 20, 2, ('p', 'PandaFramework_C_open_window_p_ppp', 'ppp'), ['GraphicsPipe*', 'GraphicsStateGuardian*']),
        ('d', 20, 1, ('p', 'PandaFramework_C_open_window_p_pp', 'pp'), ['GraphicsPipe*']),
        ('d', 20, 4, ('p', 'PandaFramework_C_open_window_p_ppipp', 'ppipp'), ['WindowProperties const&', 'int', 'GraphicsPipe*', 'GraphicsStateGuardian*']),
        ('d', 20, 3, ('p', 'PandaFramework_C_open_window_p_ppip', 'ppip'), ['WindowProperties const&', 'int', 'GraphicsPipe*']),
        ('d', 20, 2, ('p', 'PandaFramework_C_open_window_p_ppi', 'ppi'), ['WindowProperties const&', 'int']),
    ]
    c.ct['remove_mouse'] = [
        ('d', 'v', 1, ('v', 'PandaFramework_C_remove_mouse_v_pp', 'pp'), ['GraphicsOutput const*']),
    ]
    c.ct['report_frame_rate'] = [
        ('d', 'v', 1, ('v', 'PandaFramework_C_report_frame_rate_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['reset_frame_rate'] = [
        ('d', 'v', 0, ('v', 'PandaFramework_C_reset_frame_rate_v_p', 'p'), []),
    ]
    c.ct['set_background_type'] = [
        ('d', 'v', 1, ('v', 'PandaFramework_C_set_background_type_v_pp', 'pp'), ['WindowFramework::BackgroundType']),
    ]
    c.ct['set_exit_flag'] = [
        ('d', 'v', 0, ('v', 'PandaFramework_C_set_exit_flag_v_p', 'p'), []),
    ]
    c.ct['set_highlight'] = [
        ('d', 'v', 1, ('v', 'PandaFramework_C_set_highlight_v_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['set_lighting'] = [
        ('d', 'v', 1, ('v', 'PandaFramework_C_set_lighting_v_pB', 'pB'), ['bool']),
    ]
    c.ct['set_perpixel'] = [
        ('d', 'v', 1, ('v', 'PandaFramework_C_set_perpixel_v_pB', 'pB'), ['bool']),
    ]
    c.ct['set_recorder'] = [
        ('d', 'v', 1, ('v', 'PandaFramework_C_set_recorder_v_pp', 'pp'), ['RecorderController*']),
    ]
    c.ct['set_texture'] = [
        ('d', 'v', 1, ('v', 'PandaFramework_C_set_texture_v_pB', 'pB'), ['bool']),
    ]
    c.ct['set_two_sided'] = [
        ('d', 'v', 1, ('v', 'PandaFramework_C_set_two_sided_v_pB', 'pB'), ['bool']),
    ]
    c.ct['set_window_title'] = [
        ('d', 'v', 1, ('v', 'PandaFramework_C_set_window_title_v_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['set_wireframe'] = [
        ('d', 'v', 1, ('v', 'PandaFramework_C_set_wireframe_v_pB', 'pB'), ['bool']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(PandaFramework, attr, self)

PandaFramework.c.link(PandaFramework)



class PandaSystem(cxx.cplusplus):

    c = cxx.cstructs()
    c.register("PandaSystem", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['get_build_date'] = [
        ('s', 's', 0, ('s', 'PandaSystem_C_get_build_date_s_v', ''), []),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'PandaSystem_C_get_class_type_i_v', ''), []),
    ]
    c.ct['get_compiler'] = [
        ('s', 's', 0, ('s', 'PandaSystem_C_get_compiler_s_v', ''), []),
    ]
    c.ct['get_distributor'] = [
        ('s', 's', 0, ('s', 'PandaSystem_C_get_distributor_s_v', ''), []),
    ]
    c.ct['get_git_commit'] = [
        ('s', 's', 0, ('s', 'PandaSystem_C_get_git_commit_s_v', ''), []),
    ]
    c.ct['get_global_ptr'] = [
        ('s', 10, 0, ('p', 'PandaSystem_C_get_global_ptr_p_v', ''), []),
    ]
    c.ct['get_major_version'] = [
        ('s', 'i', 0, ('i', 'PandaSystem_C_get_major_version_i_v', ''), []),
    ]
    c.ct['get_memory_alignment'] = [
        ('s', 'i', 0, ('i', 'PandaSystem_C_get_memory_alignment_i_v', ''), []),
    ]
    c.ct['get_minor_version'] = [
        ('s', 'i', 0, ('i', 'PandaSystem_C_get_minor_version_i_v', ''), []),
    ]
    c.ct['get_p3d_coreapi_version_string'] = [
        ('s', 's', 0, ('s', 'PandaSystem_C_get_p3d_coreapi_version_string_s_v', ''), []),
    ]
    c.ct['get_package_host_url'] = [
        ('s', 's', 0, ('s', 'PandaSystem_C_get_package_host_url_s_v', ''), []),
    ]
    c.ct['get_package_version_string'] = [
        ('s', 's', 0, ('s', 'PandaSystem_C_get_package_version_string_s_v', ''), []),
    ]
    c.ct['get_platform'] = [
        ('s', 's', 0, ('s', 'PandaSystem_C_get_platform_s_v', ''), []),
    ]
    c.ct['get_sequence_version'] = [
        ('s', 'i', 0, ('i', 'PandaSystem_C_get_sequence_version_i_v', ''), []),
    ]
    c.ct['get_version_string'] = [
        ('s', 's', 0, ('s', 'PandaSystem_C_get_version_string_s_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'PandaSystem_C_init_type_v_v', ''), []),
    ]
    c.ct['is_official_version'] = [
        ('s', 'B', 0, ('B', 'PandaSystem_C_is_official_version_B_v', ''), []),
    ]

    @classmethod
    def get_build_date(cls, *args,**kw):
        return ( cls.c.get('get_build_date', None) or cls.c.call(PandaSystem, 'get_build_date', None) )(*args,**kw)

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(PandaSystem, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_compiler(cls, *args,**kw):
        return ( cls.c.get('get_compiler', None) or cls.c.call(PandaSystem, 'get_compiler', None) )(*args,**kw)

    @classmethod
    def get_distributor(cls, *args,**kw):
        return ( cls.c.get('get_distributor', None) or cls.c.call(PandaSystem, 'get_distributor', None) )(*args,**kw)

    @classmethod
    def get_git_commit(cls, *args,**kw):
        return ( cls.c.get('get_git_commit', None) or cls.c.call(PandaSystem, 'get_git_commit', None) )(*args,**kw)

    @classmethod
    def get_global_ptr(cls, *args,**kw):
        return ( cls.c.get('get_global_ptr', None) or cls.c.call(PandaSystem, 'get_global_ptr', None) )(*args,**kw)

    @classmethod
    def get_major_version(cls, *args,**kw):
        return ( cls.c.get('get_major_version', None) or cls.c.call(PandaSystem, 'get_major_version', None) )(*args,**kw)

    @classmethod
    def get_memory_alignment(cls, *args,**kw):
        return ( cls.c.get('get_memory_alignment', None) or cls.c.call(PandaSystem, 'get_memory_alignment', None) )(*args,**kw)

    @classmethod
    def get_minor_version(cls, *args,**kw):
        return ( cls.c.get('get_minor_version', None) or cls.c.call(PandaSystem, 'get_minor_version', None) )(*args,**kw)

    @classmethod
    def get_p3d_coreapi_version_string(cls, *args,**kw):
        return ( cls.c.get('get_p3d_coreapi_version_string', None) or cls.c.call(PandaSystem, 'get_p3d_coreapi_version_string', None) )(*args,**kw)

    @classmethod
    def get_package_host_url(cls, *args,**kw):
        return ( cls.c.get('get_package_host_url', None) or cls.c.call(PandaSystem, 'get_package_host_url', None) )(*args,**kw)

    @classmethod
    def get_package_version_string(cls, *args,**kw):
        return ( cls.c.get('get_package_version_string', None) or cls.c.call(PandaSystem, 'get_package_version_string', None) )(*args,**kw)

    @classmethod
    def get_platform(cls, *args,**kw):
        return ( cls.c.get('get_platform', None) or cls.c.call(PandaSystem, 'get_platform', None) )(*args,**kw)

    @classmethod
    def get_sequence_version(cls, *args,**kw):
        return ( cls.c.get('get_sequence_version', None) or cls.c.call(PandaSystem, 'get_sequence_version', None) )(*args,**kw)

    @classmethod
    def get_version_string(cls, *args,**kw):
        return ( cls.c.get('get_version_string', None) or cls.c.call(PandaSystem, 'get_version_string', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(PandaSystem, 'init_type', None) )(*args,**kw)

    @classmethod
    def is_official_version(cls, *args,**kw):
        return ( cls.c.get('is_official_version', None) or cls.c.call(PandaSystem, 'is_official_version', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_system'] = [
        ('d', 'v', 1, ('v', 'PandaSystem_C_add_system_v_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['get_num_systems'] = [
        ('d', 'p', 0, ('p', 'PandaSystem_C_get_num_systems_p_p', 'p'), []),
    ]
    c.ct['get_system'] = [
        ('d', 's', 1, ('s', 'PandaSystem_C_get_system_s_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['get_system_tag'] = [
        ('d', 's', 2, ('s', 'PandaSystem_C_get_system_tag_s_pss', 'pss'), ['std::string const&', 'std::string const&']),
    ]
    c.ct['has_system'] = [
        ('d', 'B', 1, ('B', 'PandaSystem_C_has_system_B_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['heap_trim'] = [
        ('d', 'B', 1, ('B', 'PandaSystem_C_heap_trim_B_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'PandaSystem_C_output_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['set_system_tag'] = [
        ('d', 'v', 3, ('v', 'PandaSystem_C_set_system_tag_v_psss', 'psss'), ['std::string const&', 'std::string const&', 'std::string const&']),
    ]
    c.ct['write'] = [
        ('d', 'v', 1, ('v', 'PandaSystem_C_write_v_pp', 'pp'), ['std::ostream&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(PandaSystem, attr, self)

PandaSystem.c.link(PandaSystem)



class GeomVertexWriter(GeomEnums):

    c = cxx.cstructs()
    c.register("GeomVertexWriter", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 11, 2, ('p', 'GeomVertexWriter_C_ctor_p_pp', 'pp'), ['GeomVertexArrayData*', 'Thread*']),
        ('s', 11, 1, ('p', 'GeomVertexWriter_C_ctor_p_p', 'p'), ['GeomVertexArrayData*']),
        ('s', 11, 3, ('p', 'GeomVertexWriter_C_ctor_p_pip', 'pip'), ['GeomVertexArrayData*', 'int', 'Thread*']),
        ('s', 11, 2, ('p', 'GeomVertexWriter_C_ctor_p_pi', 'pi'), ['GeomVertexArrayData*', 'int']),
        ('s', 11, 3, ('p', 'GeomVertexWriter_C_ctor_p_psp', 'psp'), ['GeomVertexData*', 'CPT_InternalName', 'Thread*']),
        ('s', 11, 2, ('p', 'GeomVertexWriter_C_ctor_p_ps', 'ps'), ['GeomVertexData*', 'CPT_InternalName']),
        ('s', 11, 2, ('p', 'GeomVertexWriter_C_ctor_p_pp_1_p_pp', 'pp'), ['GeomVertexData*', 'Thread*']),
        ('s', 11, 1, ('p', 'GeomVertexWriter_C_ctor_p_p_1_p_p', 'p'), ['GeomVertexData*']),
        ('s', 11, 2, ('p', 'GeomVertexWriter_C_ctor_p_ps_1_p_ps', 'ps'), ['GeomVertexDataPipelineWriter*', 'InternalName const*']),
        ('s', 11, 1, ('p', 'GeomVertexWriter_C_ctor_p_p_1_p_p_2_p_p', 'p'), ['GeomVertexWriter const&']),
        ('s', 11, 1, ('p', 'GeomVertexWriter_C_ctor_p_p_1_p_p_2_p_p_3_p_p', 'p'), ['Thread*']),
        ('s', 11, 0, ('p', 'GeomVertexWriter_C_ctor_p_v', ''), []),
    ]

    # classmethod type calls


    # instance method type calls

    c.ct['add_data1'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_data1_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['add_data1d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_data1d_v_pd', 'pd'), ['double']),
    ]
    c.ct['add_data1f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_data1f_v_pf', 'pf'), ['float']),
    ]
    c.ct['add_data1i'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_data1i_v_pi', 'pi'), ['int']),
    ]
    c.ct['add_data2'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_data2_v_pp', 'pp'), ['LVecBase2 const&']),
        ('d', 'v', 2, ('v', 'GeomVertexWriter_C_add_data2_v_pff', 'pff'), ['PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['add_data2d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_data2d_v_pp', 'pp'), ['LVecBase2d const&']),
        ('d', 'v', 2, ('v', 'GeomVertexWriter_C_add_data2d_v_pdd', 'pdd'), ['double', 'double']),
    ]
    c.ct['add_data2f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_data2f_v_pp', 'pp'), ['LVecBase2f const&']),
        ('d', 'v', 2, ('v', 'GeomVertexWriter_C_add_data2f_v_pff', 'pff'), ['float', 'float']),
    ]
    c.ct['add_data2i'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_data2i_v_pp', 'pp'), ['LVecBase2i const&']),
        ('d', 'v', 2, ('v', 'GeomVertexWriter_C_add_data2i_v_pii', 'pii'), ['int', 'int']),
    ]
    c.ct['add_data3'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_data3_v_pp', 'pp'), ['LVecBase3 const&']),
        ('d', 'v', 3, ('v', 'GeomVertexWriter_C_add_data3_v_pfff', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['add_data3d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_data3d_v_pp', 'pp'), ['LVecBase3d const&']),
        ('d', 'v', 3, ('v', 'GeomVertexWriter_C_add_data3d_v_pddd', 'pddd'), ['double', 'double', 'double']),
    ]
    c.ct['add_data3f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_data3f_v_pp', 'pp'), ['LVecBase3f const&']),
        ('d', 'v', 3, ('v', 'GeomVertexWriter_C_add_data3f_v_pfff', 'pfff'), ['float', 'float', 'float']),
    ]
    c.ct['add_data3i'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_data3i_v_pp', 'pp'), ['LVecBase3i const&']),
        ('d', 'v', 3, ('v', 'GeomVertexWriter_C_add_data3i_v_piii', 'piii'), ['int', 'int', 'int']),
    ]
    c.ct['add_data4'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_data4_v_pp', 'pp'), ['LVecBase4 const&']),
        ('d', 'v', 4, ('v', 'GeomVertexWriter_C_add_data4_v_pffff', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['add_data4d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_data4d_v_pp', 'pp'), ['LVecBase4d const&']),
        ('d', 'v', 4, ('v', 'GeomVertexWriter_C_add_data4d_v_pdddd', 'pdddd'), ['double', 'double', 'double', 'double']),
    ]
    c.ct['add_data4f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_data4f_v_pp', 'pp'), ['LVecBase4f const&']),
        ('d', 'v', 4, ('v', 'GeomVertexWriter_C_add_data4f_v_pffff', 'pffff'), ['float', 'float', 'float', 'float']),
    ]
    c.ct['add_data4i'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_data4i_v_pp', 'pp'), ['LVecBase4i const&']),
        ('d', 'v', 4, ('v', 'GeomVertexWriter_C_add_data4i_v_piiii', 'piiii'), ['int', 'int', 'int', 'int']),
    ]
    c.ct['add_matrix3'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_matrix3_v_pp', 'pp'), ['LMatrix3 const&']),
    ]
    c.ct['add_matrix3d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_matrix3d_v_pp', 'pp'), ['LMatrix3d const&']),
    ]
    c.ct['add_matrix3f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_matrix3f_v_pp', 'pp'), ['LMatrix3f const&']),
    ]
    c.ct['add_matrix4'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_matrix4_v_pp', 'pp'), ['LMatrix4 const&']),
    ]
    c.ct['add_matrix4d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_matrix4d_v_pp', 'pp'), ['LMatrix4d const&']),
    ]
    c.ct['add_matrix4f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_add_matrix4f_v_pp', 'pp'), ['LMatrix4f const&']),
    ]
    c.ct['clear'] = [
        ('d', 'v', 0, ('v', 'GeomVertexWriter_C_clear_v_p', 'p'), []),
    ]
    c.ct['get_array'] = [
        ('d', 'i', 0, ('i', 'GeomVertexWriter_C_get_array_i_p', 'p'), []),
    ]
    c.ct['get_array_data'] = [
        ('d', 'p', 0, ('p', 'GeomVertexWriter_C_get_array_data_p_p', 'p'), []),
    ]
    c.ct['get_array_handle'] = [
        ('d', 'p', 0, ('p', 'GeomVertexWriter_C_get_array_handle_p_p', 'p'), []),
    ]
    c.ct['get_column'] = [
        ('d', 'p', 0, ('p', 'GeomVertexWriter_C_get_column_p_p', 'p'), []),
    ]
    c.ct['get_current_thread'] = [
        ('d', 17, 0, ('p', 'GeomVertexWriter_C_get_current_thread_p_p', 'p'), []),
    ]
    c.ct['get_start_row'] = [
        ('d', 'i', 0, ('i', 'GeomVertexWriter_C_get_start_row_i_p', 'p'), []),
    ]
    c.ct['get_stride'] = [
        ('d', 'p', 0, ('p', 'GeomVertexWriter_C_get_stride_p_p', 'p'), []),
    ]
    c.ct['get_vertex_data'] = [
        ('d', 24, 0, ('p', 'GeomVertexWriter_C_get_vertex_data_p_p', 'p'), []),
    ]
    c.ct['get_write_row'] = [
        ('d', 'i', 0, ('i', 'GeomVertexWriter_C_get_write_row_i_p', 'p'), []),
    ]
    c.ct['has_column'] = [
        ('d', 'B', 0, ('B', 'GeomVertexWriter_C_has_column_B_p', 'p'), []),
    ]
    c.ct['is_at_end'] = [
        ('d', 'B', 0, ('B', 'GeomVertexWriter_C_is_at_end_B_p', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_output_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['reserve_num_rows'] = [
        ('d', 'B', 1, ('B', 'GeomVertexWriter_C_reserve_num_rows_B_pi', 'pi'), ['int']),
    ]
    c.ct['set_column'] = [
        ('d', 'B', 1, ('B', 'GeomVertexWriter_C_set_column_B_ps', 'ps'), ['CPT_InternalName']),
        ('d', 'B', 1, ('B', 'GeomVertexWriter_C_set_column_B_pi', 'pi'), ['int']),
        ('d', 'B', 2, ('B', 'GeomVertexWriter_C_set_column_B_pip', 'pip'), ['int', 'GeomVertexColumn const*']),
    ]
    c.ct['set_data1'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_data1_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_data1d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_data1d_v_pd', 'pd'), ['double']),
    ]
    c.ct['set_data1f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_data1f_v_pf', 'pf'), ['float']),
    ]
    c.ct['set_data1i'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_data1i_v_pi', 'pi'), ['int']),
    ]
    c.ct['set_data2'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_data2_v_pp', 'pp'), ['LVecBase2 const&']),
        ('d', 'v', 2, ('v', 'GeomVertexWriter_C_set_data2_v_pff', 'pff'), ['PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_data2d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_data2d_v_pp', 'pp'), ['LVecBase2d const&']),
        ('d', 'v', 2, ('v', 'GeomVertexWriter_C_set_data2d_v_pdd', 'pdd'), ['double', 'double']),
    ]
    c.ct['set_data2f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_data2f_v_pp', 'pp'), ['LVecBase2f const&']),
        ('d', 'v', 2, ('v', 'GeomVertexWriter_C_set_data2f_v_pff', 'pff'), ['float', 'float']),
    ]
    c.ct['set_data2i'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_data2i_v_pp', 'pp'), ['LVecBase2i const&']),
        ('d', 'v', 2, ('v', 'GeomVertexWriter_C_set_data2i_v_pii', 'pii'), ['int', 'int']),
    ]
    c.ct['set_data3'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_data3_v_pp', 'pp'), ['LVecBase3 const&']),
        ('d', 'v', 3, ('v', 'GeomVertexWriter_C_set_data3_v_pfff', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_data3d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_data3d_v_pp', 'pp'), ['LVecBase3d const&']),
        ('d', 'v', 3, ('v', 'GeomVertexWriter_C_set_data3d_v_pddd', 'pddd'), ['double', 'double', 'double']),
    ]
    c.ct['set_data3f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_data3f_v_pp', 'pp'), ['LVecBase3f const&']),
        ('d', 'v', 3, ('v', 'GeomVertexWriter_C_set_data3f_v_pfff', 'pfff'), ['float', 'float', 'float']),
    ]
    c.ct['set_data3i'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_data3i_v_pp', 'pp'), ['LVecBase3i const&']),
        ('d', 'v', 3, ('v', 'GeomVertexWriter_C_set_data3i_v_piii', 'piii'), ['int', 'int', 'int']),
    ]
    c.ct['set_data4'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_data4_v_pp', 'pp'), ['LVecBase4 const&']),
        ('d', 'v', 4, ('v', 'GeomVertexWriter_C_set_data4_v_pffff', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_data4d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_data4d_v_pp', 'pp'), ['LVecBase4d const&']),
        ('d', 'v', 4, ('v', 'GeomVertexWriter_C_set_data4d_v_pdddd', 'pdddd'), ['double', 'double', 'double', 'double']),
    ]
    c.ct['set_data4f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_data4f_v_pp', 'pp'), ['LVecBase4f const&']),
        ('d', 'v', 4, ('v', 'GeomVertexWriter_C_set_data4f_v_pffff', 'pffff'), ['float', 'float', 'float', 'float']),
    ]
    c.ct['set_data4i'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_data4i_v_pp', 'pp'), ['LVecBase4i const&']),
        ('d', 'v', 4, ('v', 'GeomVertexWriter_C_set_data4i_v_piiii', 'piiii'), ['int', 'int', 'int', 'int']),
    ]
    c.ct['set_matrix3'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_matrix3_v_pp', 'pp'), ['LMatrix3 const&']),
    ]
    c.ct['set_matrix3d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_matrix3d_v_pp', 'pp'), ['LMatrix3d const&']),
    ]
    c.ct['set_matrix3f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_matrix3f_v_pp', 'pp'), ['LMatrix3f const&']),
    ]
    c.ct['set_matrix4'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_matrix4_v_pp', 'pp'), ['LMatrix4 const&']),
    ]
    c.ct['set_matrix4d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_matrix4d_v_pp', 'pp'), ['LMatrix4d const&']),
    ]
    c.ct['set_matrix4f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_matrix4f_v_pp', 'pp'), ['LMatrix4f const&']),
    ]
    c.ct['set_row'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_row_v_pi', 'pi'), ['int']),
    ]
    c.ct['set_row_unsafe'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter_C_set_row_unsafe_v_pi', 'pi'), ['int']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomVertexWriter, attr, self)

GeomVertexWriter.c.link(GeomVertexWriter)



class Namable(MemoryBase):

    c = cxx.cstructs()
    c.register("Namable", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_PandaNode'] = [
        ('d', 29, 0, ('p', 'Namable_C_downcast_to_PandaNode_p_p', 'p'), []),
    ]
    c.ct['downcast_to_Thread'] = [
        ('d', 17, 0, ('p', 'Namable_C_downcast_to_Thread_p_p', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(Namable, attr, self)

Namable.c.link(Namable)



class ReferenceCount(MemoryBase):

    c = cxx.cstructs()
    c.register("ReferenceCount", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'ReferenceCount_C_get_class_type_i_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'ReferenceCount_C_init_type_v_v', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(ReferenceCount, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(ReferenceCount, 'init_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['get_ref_count'] = [
        ('d', 'i', 0, ('i', 'ReferenceCount_C_get_ref_count_i_p', 'p'), []),
    ]
    c.ct['get_weak_list'] = [
        ('d', 'p', 0, ('p', 'ReferenceCount_C_get_weak_list_p_p', 'p'), []),
    ]
    c.ct['has_weak_list'] = [
        ('d', 'B', 0, ('B', 'ReferenceCount_C_has_weak_list_B_p', 'p'), []),
    ]
    c.ct['local_object'] = [
        ('d', 'v', 0, ('v', 'ReferenceCount_C_local_object_v_p', 'p'), []),
    ]
    c.ct['ref'] = [
        ('d', 'v', 0, ('v', 'ReferenceCount_C_ref_v_p', 'p'), []),
    ]
    c.ct['ref_if_nonzero'] = [
        ('d', 'B', 0, ('B', 'ReferenceCount_C_ref_if_nonzero_B_p', 'p'), []),
    ]
    c.ct['test_ref_count_integrity'] = [
        ('d', 'B', 0, ('B', 'ReferenceCount_C_test_ref_count_integrity_B_p', 'p'), []),
    ]
    c.ct['test_ref_count_nonzero'] = [
        ('d', 'B', 0, ('B', 'ReferenceCount_C_test_ref_count_nonzero_B_p', 'p'), []),
    ]
    c.ct['unref'] = [
        ('d', 'B', 0, ('B', 'ReferenceCount_C_unref_B_p', 'p'), []),
    ]
    c.ct['upcast_to_MemoryBase'] = [
        ('d', 6, 0, ('p', 'ReferenceCount_C_upcast_to_MemoryBase_p_p', 'p'), []),
    ]
    c.ct['weak_ref'] = [
        ('d', 'p', 0, ('p', 'ReferenceCount_C_weak_ref_p_p', 'p'), []),
    ]
    c.ct['weak_unref'] = [
        ('d', 'v', 0, ('v', 'ReferenceCount_C_weak_unref_v_p', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(ReferenceCount, attr, self)

ReferenceCount.c.link(ReferenceCount)



class TypedObject(MemoryBase):

    c = cxx.cstructs()
    c.register("TypedObject", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'TypedObject_C_get_class_type_i_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'TypedObject_C_init_type_v_v', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(TypedObject, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(TypedObject, 'init_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['as_typed_object'] = [
        ('d', 14, 0, ('p', 'TypedObject_C_as_typed_object_p_p', 'p'), []),
        ('d', 14, 0, ('p', 'TypedObject_C_as_typed_object_p_p_1_p_p', 'p'), []),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'TypedObject_C_force_init_type_i_p', 'p'), []),
    ]
    c.ct['get_best_parent_from_Set'] = [
        ('d', 'i', 1, ('i', 'TypedObject_C_get_best_parent_from_Set_i_pp', 'pp'), ['set< int > const&']),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'TypedObject_C_get_type_i_p', 'p'), []),
    ]
    c.ct['get_type_index'] = [
        ('d', 'i', 0, ('i', 'TypedObject_C_get_type_index_i_p', 'p'), []),
    ]
    c.ct['is_exact_type'] = [
        ('d', 'B', 1, ('B', 'TypedObject_C_is_exact_type_B_pi', 'pi'), ['TypeHandle']),
    ]
    c.ct['is_of_type'] = [
        ('d', 'B', 1, ('B', 'TypedObject_C_is_of_type_B_pi', 'pi'), ['TypeHandle']),
    ]
    c.ct['upcast_to_MemoryBase'] = [
        ('d', 6, 0, ('p', 'TypedObject_C_upcast_to_MemoryBase_p_p', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TypedObject, attr, self)

TypedObject.c.link(TypedObject)



class TypedWritable(TypedObject):

    c = cxx.cstructs()
    c.register("TypedWritable", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 15, 0, ('p', 'TypedWritable_C_ctor_p_v', ''), []),
        ('s', 15, 1, ('p', 'TypedWritable_C_ctor_p_p', 'p'), ['TypedWritable const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'TypedWritable_C_get_class_type_i_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'TypedWritable_C_init_type_v_v', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(TypedWritable, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(TypedWritable, 'init_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['as_reference_count'] = [
        ('d', 13, 0, ('p', 'TypedWritable_C_as_reference_count_p_p', 'p'), []),
    ]
    c.ct['encode_to_bam_stream'] = [
        ('d', 'p', 0, ('p', 'TypedWritable_C_encode_to_bam_stream_p_p', 'p'), []),
        ('d', 'B', 2, ('B', 'TypedWritable_C_encode_to_bam_stream_B_ppp', 'ppp'), ['vector_uchar&', 'BamWriter*']),
        ('d', 'B', 1, ('B', 'TypedWritable_C_encode_to_bam_stream_B_pp', 'pp'), ['vector_uchar&']),
    ]
    c.ct['fillin'] = [
        ('d', 'v', 2, ('v', 'TypedWritable_C_fillin_v_ppp', 'ppp'), ['DatagramIterator&', 'BamReader*']),
    ]
    c.ct['finalize'] = [
        ('d', 'v', 1, ('v', 'TypedWritable_C_finalize_v_pp', 'pp'), ['BamReader*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'TypedWritable_C_force_init_type_i_p', 'p'), []),
    ]
    c.ct['get_bam_modified'] = [
        ('d', 'p', 0, ('p', 'TypedWritable_C_get_bam_modified_p_p', 'p'), []),
    ]
    c.ct['mark_bam_modified'] = [
        ('d', 'v', 0, ('v', 'TypedWritable_C_mark_bam_modified_v_p', 'p'), []),
    ]
    c.ct['require_fully_complete'] = [
        ('d', 'B', 0, ('B', 'TypedWritable_C_require_fully_complete_B_p', 'p'), []),
    ]
    c.ct['update_bam_nested'] = [
        ('d', 'v', 1, ('v', 'TypedWritable_C_update_bam_nested_v_pp', 'pp'), ['BamWriter*']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'TypedWritable_C_write_datagram_v_ppp', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TypedWritable, attr, self)

TypedWritable.c.link(TypedWritable)



class TypedReferenceCount(TypedObject, ReferenceCount):

    c = cxx.cstructs()
    c.register("TypedReferenceCount", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_Thread'] = [
        ('d', 17, 0, ('p', 'TypedReferenceCount_C_downcast_to_Thread_p_p', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TypedReferenceCount, attr, self)

TypedReferenceCount.c.link(TypedReferenceCount)



class Thread(TypedReferenceCount, Namable):

    c = cxx.cstructs()
    c.register("Thread", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['bind_thread'] = [
        ('s', 17, 2, ('p', 'Thread_C_bind_thread_p_ss', 'ss'), ['std::string const&', 'std::string const&']),
    ]
    c.ct['consider_yield'] = [
        ('s', 'v', 0, ('v', 'Thread_C_consider_yield_v_v', ''), []),
    ]
    c.ct['force_yield'] = [
        ('s', 'v', 0, ('v', 'Thread_C_force_yield_v_v', ''), []),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'Thread_C_get_class_type_i_v', ''), []),
    ]
    c.ct['get_current_pipeline_stage'] = [
        ('s', 'i', 0, ('i', 'Thread_C_get_current_pipeline_stage_i_v', ''), []),
    ]
    c.ct['get_current_thread'] = [
        ('s', 17, 0, ('p', 'Thread_C_get_current_thread_p_v', ''), []),
    ]
    c.ct['get_external_thread'] = [
        ('s', 17, 0, ('p', 'Thread_C_get_external_thread_p_v', ''), []),
    ]
    c.ct['get_main_thread'] = [
        ('s', 17, 0, ('p', 'Thread_C_get_main_thread_p_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'Thread_C_init_type_v_v', ''), []),
    ]
    c.ct['is_simple_threads'] = [
        ('s', 'B', 0, ('B', 'Thread_C_is_simple_threads_B_v', ''), []),
    ]
    c.ct['is_threading_supported'] = [
        ('s', 'B', 0, ('B', 'Thread_C_is_threading_supported_B_v', ''), []),
    ]
    c.ct['is_true_threads'] = [
        ('s', 'B', 0, ('B', 'Thread_C_is_true_threads_B_v', ''), []),
    ]
    c.ct['prepare_for_exit'] = [
        ('s', 'v', 0, ('v', 'Thread_C_prepare_for_exit_v_v', ''), []),
    ]
    c.ct['sleep'] = [
        ('s', 'v', 1, ('v', 'Thread_C_sleep_v_d', 'd'), ['double']),
    ]
    c.ct['write_status'] = [
        ('s', 'v', 1, ('v', 'Thread_C_write_status_v_p', 'p'), ['std::ostream&']),
    ]

    @classmethod
    def bind_thread(cls, *args,**kw):
        return ( cls.c.get('bind_thread', None) or cls.c.call(Thread, 'bind_thread', None) )(*args,**kw)

    @classmethod
    def consider_yield(cls, *args,**kw):
        return ( cls.c.get('consider_yield', None) or cls.c.call(Thread, 'consider_yield', None) )(*args,**kw)

    @classmethod
    def force_yield(cls, *args,**kw):
        return ( cls.c.get('force_yield', None) or cls.c.call(Thread, 'force_yield', None) )(*args,**kw)

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(Thread, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_current_pipeline_stage(cls, *args,**kw):
        return ( cls.c.get('get_current_pipeline_stage', None) or cls.c.call(Thread, 'get_current_pipeline_stage', None) )(*args,**kw)

    @classmethod
    def get_current_thread(cls, *args,**kw):
        return ( cls.c.get('get_current_thread', None) or cls.c.call(Thread, 'get_current_thread', None) )(*args,**kw)

    @classmethod
    def get_external_thread(cls, *args,**kw):
        return ( cls.c.get('get_external_thread', None) or cls.c.call(Thread, 'get_external_thread', None) )(*args,**kw)

    @classmethod
    def get_main_thread(cls, *args,**kw):
        return ( cls.c.get('get_main_thread', None) or cls.c.call(Thread, 'get_main_thread', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(Thread, 'init_type', None) )(*args,**kw)

    @classmethod
    def is_simple_threads(cls, *args,**kw):
        return ( cls.c.get('is_simple_threads', None) or cls.c.call(Thread, 'is_simple_threads', None) )(*args,**kw)

    @classmethod
    def is_threading_supported(cls, *args,**kw):
        return ( cls.c.get('is_threading_supported', None) or cls.c.call(Thread, 'is_threading_supported', None) )(*args,**kw)

    @classmethod
    def is_true_threads(cls, *args,**kw):
        return ( cls.c.get('is_true_threads', None) or cls.c.call(Thread, 'is_true_threads', None) )(*args,**kw)

    @classmethod
    def prepare_for_exit(cls, *args,**kw):
        return ( cls.c.get('prepare_for_exit', None) or cls.c.call(Thread, 'prepare_for_exit', None) )(*args,**kw)

    @classmethod
    def sleep(cls, *args,**kw):
        return ( cls.c.get('sleep', None) or cls.c.call(Thread, 'sleep', None) )(*args,**kw)

    @classmethod
    def write_status(cls, *args,**kw):
        return ( cls.c.get('write_status', None) or cls.c.call(Thread, 'write_status', None) )(*args,**kw)

    # instance method type calls

    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'Thread_C_force_init_type_i_p', 'p'), []),
    ]
    c.ct['get_current_task'] = [
        ('d', 16, 0, ('p', 'Thread_C_get_current_task_p_p', 'p'), []),
    ]
    c.ct['get_pipeline_stage'] = [
        ('d', 'i', 0, ('i', 'Thread_C_get_pipeline_stage_i_p', 'p'), []),
    ]
    c.ct['get_pstats_callback'] = [
        ('d', 'p', 0, ('p', 'Thread_C_get_pstats_callback_p_p', 'p'), []),
    ]
    c.ct['get_pstats_index'] = [
        ('d', 'i', 0, ('i', 'Thread_C_get_pstats_index_i_p', 'p'), []),
    ]
    c.ct['get_python_index'] = [
        ('d', 'i', 0, ('i', 'Thread_C_get_python_index_i_p', 'p'), []),
    ]
    c.ct['get_sync_name'] = [
        ('d', 's', 0, ('s', 'Thread_C_get_sync_name_s_p', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'Thread_C_get_type_i_p', 'p'), []),
    ]
    c.ct['get_unique_id'] = [
        ('d', 's', 0, ('s', 'Thread_C_get_unique_id_s_p', 'p'), []),
    ]
    c.ct['is_joinable'] = [
        ('d', 'B', 0, ('B', 'Thread_C_is_joinable_B_p', 'p'), []),
    ]
    c.ct['is_started'] = [
        ('d', 'B', 0, ('B', 'Thread_C_is_started_B_p', 'p'), []),
    ]
    c.ct['join'] = [
        ('d', 'v', 0, ('v', 'Thread_C_join_v_p', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'Thread_C_output_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['output_blocker'] = [
        ('d', 'v', 1, ('v', 'Thread_C_output_blocker_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['preempt'] = [
        ('d', 'v', 0, ('v', 'Thread_C_preempt_v_p', 'p'), []),
    ]
    c.ct['set_min_pipeline_stage'] = [
        ('d', 'v', 1, ('v', 'Thread_C_set_min_pipeline_stage_v_pi', 'pi'), ['int']),
    ]
    c.ct['set_pipeline_stage'] = [
        ('d', 'v', 1, ('v', 'Thread_C_set_pipeline_stage_v_pi', 'pi'), ['int']),
    ]
    c.ct['set_pstats_callback'] = [
        ('d', 'v', 1, ('v', 'Thread_C_set_pstats_callback_v_pp', 'pp'), ['Thread::PStatsCallback*']),
    ]
    c.ct['set_pstats_index'] = [
        ('d', 'v', 1, ('v', 'Thread_C_set_pstats_index_v_pi', 'pi'), ['int']),
    ]
    c.ct['set_python_index'] = [
        ('d', 'v', 1, ('v', 'Thread_C_set_python_index_v_pi', 'pi'), ['int']),
    ]
    c.ct['start'] = [
        ('d', 'B', 2, ('B', 'Thread_C_start_B_ppB', 'ppB'), ['ThreadPriority', 'bool']),
    ]
    c.ct['upcast_to_Namable'] = [
        ('d', 12, 0, ('p', 'Thread_C_upcast_to_Namable_p_p', 'p'), []),
    ]
    c.ct['upcast_to_TypedReferenceCount'] = [
        ('d', 16, 0, ('p', 'Thread_C_upcast_to_TypedReferenceCount_p_p', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(Thread, attr, self)

Thread.c.link(Thread)



class TypedWritableReferenceCount(TypedWritable, ReferenceCount):

    c = cxx.cstructs()
    c.register("TypedWritableReferenceCount", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_GeomVertexFormat'] = [
        ('d', 19, 0, ('p', 'TypedWritableReferenceCount_C_downcast_to_GeomVertexFormat_p_p', 'p'), []),
    ]
    c.ct['downcast_to_PandaNode'] = [
        ('d', 29, 0, ('p', 'TypedWritableReferenceCount_C_downcast_to_PandaNode_p_p', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TypedWritableReferenceCount, attr, self)

TypedWritableReferenceCount.c.link(TypedWritableReferenceCount)



class GeomVertexFormat(TypedWritableReferenceCount, GeomEnums):

    c = cxx.cstructs()
    c.register("GeomVertexFormat", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat_C_ctor_p_v', ''), []),
        ('s', 19, 1, ('p', 'GeomVertexFormat_C_ctor_p_p', 'p'), ['GeomVertexArrayFormat const*']),
        ('s', 19, 1, ('p', 'GeomVertexFormat_C_ctor_p_p_1_p_p', 'p'), ['GeomVertexFormat const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'GeomVertexFormat_C_get_class_type_i_v', ''), []),
    ]
    c.ct['get_empty'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat_C_get_empty_p_v', ''), []),
    ]
    c.ct['get_v3'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat_C_get_v3_p_v', ''), []),
    ]
    c.ct['get_v3c4'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat_C_get_v3c4_p_v', ''), []),
    ]
    c.ct['get_v3c4t2'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat_C_get_v3c4t2_p_v', ''), []),
    ]
    c.ct['get_v3cp'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat_C_get_v3cp_p_v', ''), []),
    ]
    c.ct['get_v3cpt2'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat_C_get_v3cpt2_p_v', ''), []),
    ]
    c.ct['get_v3n3'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat_C_get_v3n3_p_v', ''), []),
    ]
    c.ct['get_v3n3c4'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat_C_get_v3n3c4_p_v', ''), []),
    ]
    c.ct['get_v3n3c4t2'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat_C_get_v3n3c4t2_p_v', ''), []),
    ]
    c.ct['get_v3n3cp'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat_C_get_v3n3cp_p_v', ''), []),
    ]
    c.ct['get_v3n3cpt2'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat_C_get_v3n3cpt2_p_v', ''), []),
    ]
    c.ct['get_v3n3t2'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat_C_get_v3n3t2_p_v', ''), []),
    ]
    c.ct['get_v3t2'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat_C_get_v3t2_p_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'GeomVertexFormat_C_init_type_v_v', ''), []),
    ]
    c.ct['register_format'] = [
        ('s', 19, 1, ('p', 'GeomVertexFormat_C_register_format_p_p', 'p'), ['GeomVertexArrayFormat const*']),
        ('s', 19, 1, ('p', 'GeomVertexFormat_C_register_format_p_p_1_p_p', 'p'), ['GeomVertexFormat const*']),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'GeomVertexFormat_C_register_with_read_factory_v_v', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(GeomVertexFormat, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_empty(cls, *args,**kw):
        return ( cls.c.get('get_empty', None) or cls.c.call(GeomVertexFormat, 'get_empty', None) )(*args,**kw)

    @classmethod
    def get_v3(cls, *args,**kw):
        return ( cls.c.get('get_v3', None) or cls.c.call(GeomVertexFormat, 'get_v3', None) )(*args,**kw)

    @classmethod
    def get_v3c4(cls, *args,**kw):
        return ( cls.c.get('get_v3c4', None) or cls.c.call(GeomVertexFormat, 'get_v3c4', None) )(*args,**kw)

    @classmethod
    def get_v3c4t2(cls, *args,**kw):
        return ( cls.c.get('get_v3c4t2', None) or cls.c.call(GeomVertexFormat, 'get_v3c4t2', None) )(*args,**kw)

    @classmethod
    def get_v3cp(cls, *args,**kw):
        return ( cls.c.get('get_v3cp', None) or cls.c.call(GeomVertexFormat, 'get_v3cp', None) )(*args,**kw)

    @classmethod
    def get_v3cpt2(cls, *args,**kw):
        return ( cls.c.get('get_v3cpt2', None) or cls.c.call(GeomVertexFormat, 'get_v3cpt2', None) )(*args,**kw)

    @classmethod
    def get_v3n3(cls, *args,**kw):
        return ( cls.c.get('get_v3n3', None) or cls.c.call(GeomVertexFormat, 'get_v3n3', None) )(*args,**kw)

    @classmethod
    def get_v3n3c4(cls, *args,**kw):
        return ( cls.c.get('get_v3n3c4', None) or cls.c.call(GeomVertexFormat, 'get_v3n3c4', None) )(*args,**kw)

    @classmethod
    def get_v3n3c4t2(cls, *args,**kw):
        return ( cls.c.get('get_v3n3c4t2', None) or cls.c.call(GeomVertexFormat, 'get_v3n3c4t2', None) )(*args,**kw)

    @classmethod
    def get_v3n3cp(cls, *args,**kw):
        return ( cls.c.get('get_v3n3cp', None) or cls.c.call(GeomVertexFormat, 'get_v3n3cp', None) )(*args,**kw)

    @classmethod
    def get_v3n3cpt2(cls, *args,**kw):
        return ( cls.c.get('get_v3n3cpt2', None) or cls.c.call(GeomVertexFormat, 'get_v3n3cpt2', None) )(*args,**kw)

    @classmethod
    def get_v3n3t2(cls, *args,**kw):
        return ( cls.c.get('get_v3n3t2', None) or cls.c.call(GeomVertexFormat, 'get_v3n3t2', None) )(*args,**kw)

    @classmethod
    def get_v3t2(cls, *args,**kw):
        return ( cls.c.get('get_v3t2', None) or cls.c.call(GeomVertexFormat, 'get_v3t2', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(GeomVertexFormat, 'init_type', None) )(*args,**kw)

    @classmethod
    def register_format(cls, *args,**kw):
        return ( cls.c.get('register_format', None) or cls.c.call(GeomVertexFormat, 'register_format', None) )(*args,**kw)

    @classmethod
    def register_with_read_factory(cls, *args,**kw):
        return ( cls.c.get('register_with_read_factory', None) or cls.c.call(GeomVertexFormat, 'register_with_read_factory', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_array'] = [
        ('d', 'p', 1, ('p', 'GeomVertexFormat_C_add_array_p_pp', 'pp'), ['GeomVertexArrayFormat const*']),
    ]
    c.ct['align_columns_for_animation'] = [
        ('d', 'v', 0, ('v', 'GeomVertexFormat_C_align_columns_for_animation_v_p', 'p'), []),
    ]
    c.ct['clear_arrays'] = [
        ('d', 'v', 0, ('v', 'GeomVertexFormat_C_clear_arrays_v_p', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'GeomVertexFormat_C_compare_to_i_pp', 'pp'), ['GeomVertexFormat const&']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'GeomVertexFormat_C_force_init_type_i_p', 'p'), []),
    ]
    c.ct['get_animation'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat_C_get_animation_p_p', 'p'), []),
    ]
    c.ct['get_array'] = [
        ('d', 'p', 1, ('p', 'GeomVertexFormat_C_get_array_p_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['get_array_with'] = [
        ('d', 'i', 1, ('i', 'GeomVertexFormat_C_get_array_with_i_ps', 'ps'), ['InternalName const*']),
        ('d', 'i', 1, ('i', 'GeomVertexFormat_C_get_array_with_i_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['get_color_array_index'] = [
        ('d', 'i', 0, ('i', 'GeomVertexFormat_C_get_color_array_index_i_p', 'p'), []),
    ]
    c.ct['get_color_column'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat_C_get_color_column_p_p', 'p'), []),
    ]
    c.ct['get_column'] = [
        ('d', 'p', 1, ('p', 'GeomVertexFormat_C_get_column_p_ps', 'ps'), ['InternalName const*']),
        ('d', 'p', 1, ('p', 'GeomVertexFormat_C_get_column_p_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['get_column_name'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat_C_get_column_name_s_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['get_morph_base'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat_C_get_morph_base_s_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['get_morph_delta'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat_C_get_morph_delta_s_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['get_morph_slider'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat_C_get_morph_slider_s_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['get_normal_array_index'] = [
        ('d', 'i', 0, ('i', 'GeomVertexFormat_C_get_normal_array_index_i_p', 'p'), []),
    ]
    c.ct['get_normal_column'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat_C_get_normal_column_p_p', 'p'), []),
    ]
    c.ct['get_num_arrays'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat_C_get_num_arrays_p_p', 'p'), []),
    ]
    c.ct['get_num_columns'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat_C_get_num_columns_p_p', 'p'), []),
    ]
    c.ct['get_num_morphs'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat_C_get_num_morphs_p_p', 'p'), []),
    ]
    c.ct['get_num_points'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat_C_get_num_points_p_p', 'p'), []),
    ]
    c.ct['get_num_texcoords'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat_C_get_num_texcoords_p_p', 'p'), []),
    ]
    c.ct['get_num_vectors'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat_C_get_num_vectors_p_p', 'p'), []),
    ]
    c.ct['get_point'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat_C_get_point_s_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['get_post_animated_format'] = [
        ('d', 19, 0, ('p', 'GeomVertexFormat_C_get_post_animated_format_p_p', 'p'), []),
    ]
    c.ct['get_texcoord'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat_C_get_texcoord_s_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'GeomVertexFormat_C_get_type_i_p', 'p'), []),
    ]
    c.ct['get_union_format'] = [
        ('d', 19, 1, ('p', 'GeomVertexFormat_C_get_union_format_p_pp', 'pp'), ['GeomVertexFormat const*']),
    ]
    c.ct['get_vector'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat_C_get_vector_s_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['get_vertex_array_index'] = [
        ('d', 'i', 0, ('i', 'GeomVertexFormat_C_get_vertex_array_index_i_p', 'p'), []),
    ]
    c.ct['get_vertex_column'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat_C_get_vertex_column_p_p', 'p'), []),
    ]
    c.ct['has_column'] = [
        ('d', 'B', 1, ('B', 'GeomVertexFormat_C_has_column_B_ps', 'ps'), ['InternalName const*']),
    ]
    c.ct['insert_array'] = [
        ('d', 'v', 2, ('v', 'GeomVertexFormat_C_insert_array_v_ppp', 'ppp'), ['std::size_t', 'GeomVertexArrayFormat const*']),
    ]
    c.ct['is_registered'] = [
        ('d', 'B', 0, ('B', 'GeomVertexFormat_C_is_registered_B_p', 'p'), []),
    ]
    c.ct['maybe_align_columns_for_animation'] = [
        ('d', 'v', 0, ('v', 'GeomVertexFormat_C_maybe_align_columns_for_animation_v_p', 'p'), []),
    ]
    c.ct['modify_array'] = [
        ('d', 'p', 1, ('p', 'GeomVertexFormat_C_modify_array_p_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'GeomVertexFormat_C_output_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['pack_columns'] = [
        ('d', 'v', 0, ('v', 'GeomVertexFormat_C_pack_columns_v_p', 'p'), []),
    ]
    c.ct['remove_array'] = [
        ('d', 'v', 1, ('v', 'GeomVertexFormat_C_remove_array_v_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['remove_column'] = [
        ('d', 'v', 2, ('v', 'GeomVertexFormat_C_remove_column_v_psB', 'psB'), ['InternalName const*', 'bool']),
        ('d', 'v', 1, ('v', 'GeomVertexFormat_C_remove_column_v_ps', 'ps'), ['InternalName const*']),
    ]
    c.ct['remove_empty_arrays'] = [
        ('d', 'v', 0, ('v', 'GeomVertexFormat_C_remove_empty_arrays_v_p', 'p'), []),
    ]
    c.ct['set_animation'] = [
        ('d', 'v', 1, ('v', 'GeomVertexFormat_C_set_animation_v_pp', 'pp'), ['GeomVertexAnimationSpec const&']),
    ]
    c.ct['set_array'] = [
        ('d', 'v', 2, ('v', 'GeomVertexFormat_C_set_array_v_ppp', 'ppp'), ['std::size_t', 'GeomVertexArrayFormat const*']),
    ]
    c.ct['unref'] = [
        ('d', 'B', 0, ('B', 'GeomVertexFormat_C_unref_B_p', 'p'), []),
    ]
    c.ct['upcast_to_GeomEnums'] = [
        ('d', 3, 0, ('p', 'GeomVertexFormat_C_upcast_to_GeomEnums_p_p', 'p'), []),
    ]
    c.ct['upcast_to_TypedWritableReferenceCount'] = [
        ('d', 18, 0, ('p', 'GeomVertexFormat_C_upcast_to_TypedWritableReferenceCount_p_p', 'p'), []),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'GeomVertexFormat_C_write_v_ppi', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'v', 1, ('v', 'GeomVertexFormat_C_write_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'GeomVertexFormat_C_write_datagram_v_ppp', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]
    c.ct['write_with_data'] = [
        ('d', 'v', 3, ('v', 'GeomVertexFormat_C_write_with_data_v_ppip', 'ppip'), ['std::ostream&', 'int', 'GeomVertexData const*']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomVertexFormat, attr, self)

GeomVertexFormat.c.link(GeomVertexFormat)



class WindowFramework(TypedWritableReferenceCount):

    c = cxx.cstructs()
    c.register("WindowFramework", "upanda3d", """libupanda3d_cni.so""")

    # enum SplitType

    ST_default = const(0)
    ST_horizontal = const(1)
    ST_vertical = const(2)


    # enum BackgroundType

    BT_black = const(2)
    BT_default = const(1)
    BT_gray = const(3)
    BT_none = const(5)
    BT_other = const(0)
    BT_white = const(4)


    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 20, 1, ('p', 'WindowFramework_C_ctor_p_p', 'p'), ['WindowFramework const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'WindowFramework_C_get_class_type_i_v', ''), []),
    ]
    c.ct['get_shuttle_controls_font'] = [
        ('s', 'p', 0, ('p', 'WindowFramework_C_get_shuttle_controls_font_p_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'WindowFramework_C_init_type_v_v', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(WindowFramework, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_shuttle_controls_font(cls, *args,**kw):
        return ( cls.c.get('get_shuttle_controls_font', None) or cls.c.call(WindowFramework, 'get_shuttle_controls_font', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(WindowFramework, 'init_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['adjust_dimensions'] = [
        ('d', 'v', 0, ('v', 'WindowFramework_C_adjust_dimensions_v_p', 'p'), []),
    ]
    c.ct['center_trackball'] = [
        ('d', 'v', 1, ('v', 'WindowFramework_C_center_trackball_v_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['enable_keyboard'] = [
        ('d', 'v', 0, ('v', 'WindowFramework_C_enable_keyboard_v_p', 'p'), []),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'WindowFramework_C_force_init_type_i_p', 'p'), []),
    ]
    c.ct['get_anim_controls'] = [
        ('d', 'B', 0, ('B', 'WindowFramework_C_get_anim_controls_B_p', 'p'), []),
    ]
    c.ct['get_aspect_2d'] = [
        ('d', 7, 0, ('p', 'WindowFramework_C_get_aspect_2d_p_p', 'p'), []),
    ]
    c.ct['get_background_type'] = [
        ('d', 'p', 0, ('p', 'WindowFramework_C_get_background_type_p_p', 'p'), []),
    ]
    c.ct['get_button_thrower'] = [
        ('d', 7, 0, ('p', 'WindowFramework_C_get_button_thrower_p_p', 'p'), []),
    ]
    c.ct['get_camera'] = [
        ('d', 31, 1, ('p', 'WindowFramework_C_get_camera_p_pi', 'pi'), ['int']),
    ]
    c.ct['get_camera_group'] = [
        ('d', 7, 0, ('p', 'WindowFramework_C_get_camera_group_p_p', 'p'), []),
    ]
    c.ct['get_display_region_2d'] = [
        ('d', 'p', 0, ('p', 'WindowFramework_C_get_display_region_2d_p_p', 'p'), []),
    ]
    c.ct['get_display_region_3d'] = [
        ('d', 'p', 0, ('p', 'WindowFramework_C_get_display_region_3d_p_p', 'p'), []),
    ]
    c.ct['get_graphics_output'] = [
        ('d', 'p', 0, ('p', 'WindowFramework_C_get_graphics_output_p_p', 'p'), []),
    ]
    c.ct['get_graphics_window'] = [
        ('d', 'p', 0, ('p', 'WindowFramework_C_get_graphics_window_p_p', 'p'), []),
    ]
    c.ct['get_lighting'] = [
        ('d', 'B', 0, ('B', 'WindowFramework_C_get_lighting_B_p', 'p'), []),
    ]
    c.ct['get_mouse'] = [
        ('d', 7, 0, ('p', 'WindowFramework_C_get_mouse_p_p', 'p'), []),
    ]
    c.ct['get_num_cameras'] = [
        ('d', 'i', 0, ('i', 'WindowFramework_C_get_num_cameras_i_p', 'p'), []),
    ]
    c.ct['get_one_sided_reverse'] = [
        ('d', 'B', 0, ('B', 'WindowFramework_C_get_one_sided_reverse_B_p', 'p'), []),
    ]
    c.ct['get_panda_framework'] = [
        ('d', 9, 0, ('p', 'WindowFramework_C_get_panda_framework_p_p', 'p'), []),
    ]
    c.ct['get_perpixel'] = [
        ('d', 'B', 0, ('B', 'WindowFramework_C_get_perpixel_B_p', 'p'), []),
    ]
    c.ct['get_pixel_2d'] = [
        ('d', 7, 0, ('p', 'WindowFramework_C_get_pixel_2d_p_p', 'p'), []),
    ]
    c.ct['get_render'] = [
        ('d', 7, 0, ('p', 'WindowFramework_C_get_render_p_p', 'p'), []),
    ]
    c.ct['get_render_2d'] = [
        ('d', 7, 0, ('p', 'WindowFramework_C_get_render_2d_p_p', 'p'), []),
    ]
    c.ct['get_texture'] = [
        ('d', 'B', 0, ('B', 'WindowFramework_C_get_texture_B_p', 'p'), []),
    ]
    c.ct['get_two_sided'] = [
        ('d', 'B', 0, ('B', 'WindowFramework_C_get_two_sided_B_p', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'WindowFramework_C_get_type_i_p', 'p'), []),
    ]
    c.ct['get_wireframe'] = [
        ('d', 'B', 0, ('B', 'WindowFramework_C_get_wireframe_B_p', 'p'), []),
    ]
    c.ct['get_wireframe_filled'] = [
        ('d', 'B', 0, ('B', 'WindowFramework_C_get_wireframe_filled_B_p', 'p'), []),
    ]
    c.ct['load_default_model'] = [
        ('d', 7, 1, ('p', 'WindowFramework_C_load_default_model_p_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['load_model'] = [
        ('d', 7, 2, ('p', 'WindowFramework_C_load_model_p_ppp', 'ppp'), ['NodePath const&', 'Filename']),
    ]
    c.ct['load_models'] = [
        ('d', 'B', 2, ('B', 'WindowFramework_C_load_models_B_ppp', 'ppp'), ['NodePath const&', 'pvector< Filename > const&']),
    ]
    c.ct['loop_animations'] = [
        ('d', 'v', 1, ('v', 'WindowFramework_C_loop_animations_v_pi', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'WindowFramework_C_loop_animations_v_p', 'p'), []),
    ]
    c.ct['make_camera'] = [
        ('d', 7, 0, ('p', 'WindowFramework_C_make_camera_p_p', 'p'), []),
    ]
    c.ct['next_anim_control'] = [
        ('d', 'v', 0, ('v', 'WindowFramework_C_next_anim_control_v_p', 'p'), []),
    ]
    c.ct['set_anim_controls'] = [
        ('d', 'v', 1, ('v', 'WindowFramework_C_set_anim_controls_v_pB', 'pB'), ['bool']),
    ]
    c.ct['set_background_type'] = [
        ('d', 'v', 1, ('v', 'WindowFramework_C_set_background_type_v_pp', 'pp'), ['WindowFramework::BackgroundType']),
    ]
    c.ct['set_lighting'] = [
        ('d', 'v', 1, ('v', 'WindowFramework_C_set_lighting_v_pB', 'pB'), ['bool']),
    ]
    c.ct['set_one_sided_reverse'] = [
        ('d', 'v', 1, ('v', 'WindowFramework_C_set_one_sided_reverse_v_pB', 'pB'), ['bool']),
    ]
    c.ct['set_perpixel'] = [
        ('d', 'v', 1, ('v', 'WindowFramework_C_set_perpixel_v_pB', 'pB'), ['bool']),
    ]
    c.ct['set_texture'] = [
        ('d', 'v', 1, ('v', 'WindowFramework_C_set_texture_v_pB', 'pB'), ['bool']),
    ]
    c.ct['set_two_sided'] = [
        ('d', 'v', 1, ('v', 'WindowFramework_C_set_two_sided_v_pB', 'pB'), ['bool']),
    ]
    c.ct['set_wireframe'] = [
        ('d', 'v', 2, ('v', 'WindowFramework_C_set_wireframe_v_pBB', 'pBB'), ['bool', 'bool']),
        ('d', 'v', 1, ('v', 'WindowFramework_C_set_wireframe_v_pB', 'pB'), ['bool']),
    ]
    c.ct['setup_trackball'] = [
        ('d', 'v', 0, ('v', 'WindowFramework_C_setup_trackball_v_p', 'p'), []),
    ]
    c.ct['split_window'] = [
        ('d', 20, 1, ('p', 'WindowFramework_C_split_window_p_pp', 'pp'), ['WindowFramework::SplitType']),
        ('d', 20, 0, ('p', 'WindowFramework_C_split_window_p_p', 'p'), []),
    ]
    c.ct['stagger_animations'] = [
        ('d', 'v', 0, ('v', 'WindowFramework_C_stagger_animations_v_p', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(WindowFramework, attr, self)

WindowFramework.c.link(WindowFramework)



class InternalName(TypedWritableReferenceCount):

    c = cxx.cstructs()
    c.register("InternalName", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['get_aspect_ratio'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_aspect_ratio_p_v', ''), []),
    ]
    c.ct['get_binormal'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_binormal_p_v', ''), []),
    ]
    c.ct['get_binormal_name'] = [
        ('s', 'p', 1, ('p', 'InternalName_C_get_binormal_name_p_s', 's'), ['std::string const&']),
    ]
    c.ct['get_camera'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_camera_p_v', ''), []),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'InternalName_C_get_class_type_i_v', ''), []),
    ]
    c.ct['get_color'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_color_p_v', ''), []),
    ]
    c.ct['get_error'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_error_p_v', ''), []),
    ]
    c.ct['get_index'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_index_p_v', ''), []),
    ]
    c.ct['get_model'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_model_p_v', ''), []),
    ]
    c.ct['get_morph'] = [
        ('s', 'p', 2, ('p', 'InternalName_C_get_morph_p_ps', 'ps'), ['InternalName*', 'std::string const&']),
    ]
    c.ct['get_normal'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_normal_p_v', ''), []),
    ]
    c.ct['get_root'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_root_p_v', ''), []),
    ]
    c.ct['get_rotate'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_rotate_p_v', ''), []),
    ]
    c.ct['get_size'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_size_p_v', ''), []),
    ]
    c.ct['get_tangent'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_tangent_p_v', ''), []),
    ]
    c.ct['get_tangent_name'] = [
        ('s', 'p', 1, ('p', 'InternalName_C_get_tangent_name_p_s', 's'), ['std::string const&']),
    ]
    c.ct['get_texcoord'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_texcoord_p_v', ''), []),
    ]
    c.ct['get_texcoord_name'] = [
        ('s', 'p', 1, ('p', 'InternalName_C_get_texcoord_name_p_s', 's'), ['std::string const&']),
    ]
    c.ct['get_transform_blend'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_transform_blend_p_v', ''), []),
    ]
    c.ct['get_transform_index'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_transform_index_p_v', ''), []),
    ]
    c.ct['get_transform_weight'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_transform_weight_p_v', ''), []),
    ]
    c.ct['get_vertex'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_vertex_p_v', ''), []),
    ]
    c.ct['get_view'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_view_p_v', ''), []),
    ]
    c.ct['get_world'] = [
        ('s', 'p', 0, ('p', 'InternalName_C_get_world_p_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'InternalName_C_init_type_v_v', ''), []),
    ]
    c.ct['make'] = [
        ('s', 'p', 1, ('p', 'InternalName_C_make_p_s', 's'), ['std::string const&']),
        ('s', 'p', 2, ('p', 'InternalName_C_make_p_si', 'si'), ['std::string const&', 'int']),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'InternalName_C_register_with_read_factory_v_v', ''), []),
    ]

    @classmethod
    def get_aspect_ratio(cls, *args,**kw):
        return ( cls.c.get('get_aspect_ratio', None) or cls.c.call(InternalName, 'get_aspect_ratio', None) )(*args,**kw)

    @classmethod
    def get_binormal(cls, *args,**kw):
        return ( cls.c.get('get_binormal', None) or cls.c.call(InternalName, 'get_binormal', None) )(*args,**kw)

    @classmethod
    def get_binormal_name(cls, *args,**kw):
        return ( cls.c.get('get_binormal_name', None) or cls.c.call(InternalName, 'get_binormal_name', None) )(*args,**kw)

    @classmethod
    def get_camera(cls, *args,**kw):
        return ( cls.c.get('get_camera', None) or cls.c.call(InternalName, 'get_camera', None) )(*args,**kw)

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(InternalName, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_color(cls, *args,**kw):
        return ( cls.c.get('get_color', None) or cls.c.call(InternalName, 'get_color', None) )(*args,**kw)

    @classmethod
    def get_error(cls, *args,**kw):
        return ( cls.c.get('get_error', None) or cls.c.call(InternalName, 'get_error', None) )(*args,**kw)

    @classmethod
    def get_index(cls, *args,**kw):
        return ( cls.c.get('get_index', None) or cls.c.call(InternalName, 'get_index', None) )(*args,**kw)

    @classmethod
    def get_model(cls, *args,**kw):
        return ( cls.c.get('get_model', None) or cls.c.call(InternalName, 'get_model', None) )(*args,**kw)

    @classmethod
    def get_morph(cls, *args,**kw):
        return ( cls.c.get('get_morph', None) or cls.c.call(InternalName, 'get_morph', None) )(*args,**kw)

    @classmethod
    def get_normal(cls, *args,**kw):
        return ( cls.c.get('get_normal', None) or cls.c.call(InternalName, 'get_normal', None) )(*args,**kw)

    @classmethod
    def get_root(cls, *args,**kw):
        return ( cls.c.get('get_root', None) or cls.c.call(InternalName, 'get_root', None) )(*args,**kw)

    @classmethod
    def get_rotate(cls, *args,**kw):
        return ( cls.c.get('get_rotate', None) or cls.c.call(InternalName, 'get_rotate', None) )(*args,**kw)

    @classmethod
    def get_size(cls, *args,**kw):
        return ( cls.c.get('get_size', None) or cls.c.call(InternalName, 'get_size', None) )(*args,**kw)

    @classmethod
    def get_tangent(cls, *args,**kw):
        return ( cls.c.get('get_tangent', None) or cls.c.call(InternalName, 'get_tangent', None) )(*args,**kw)

    @classmethod
    def get_tangent_name(cls, *args,**kw):
        return ( cls.c.get('get_tangent_name', None) or cls.c.call(InternalName, 'get_tangent_name', None) )(*args,**kw)

    @classmethod
    def get_texcoord(cls, *args,**kw):
        return ( cls.c.get('get_texcoord', None) or cls.c.call(InternalName, 'get_texcoord', None) )(*args,**kw)

    @classmethod
    def get_texcoord_name(cls, *args,**kw):
        return ( cls.c.get('get_texcoord_name', None) or cls.c.call(InternalName, 'get_texcoord_name', None) )(*args,**kw)

    @classmethod
    def get_transform_blend(cls, *args,**kw):
        return ( cls.c.get('get_transform_blend', None) or cls.c.call(InternalName, 'get_transform_blend', None) )(*args,**kw)

    @classmethod
    def get_transform_index(cls, *args,**kw):
        return ( cls.c.get('get_transform_index', None) or cls.c.call(InternalName, 'get_transform_index', None) )(*args,**kw)

    @classmethod
    def get_transform_weight(cls, *args,**kw):
        return ( cls.c.get('get_transform_weight', None) or cls.c.call(InternalName, 'get_transform_weight', None) )(*args,**kw)

    @classmethod
    def get_vertex(cls, *args,**kw):
        return ( cls.c.get('get_vertex', None) or cls.c.call(InternalName, 'get_vertex', None) )(*args,**kw)

    @classmethod
    def get_view(cls, *args,**kw):
        return ( cls.c.get('get_view', None) or cls.c.call(InternalName, 'get_view', None) )(*args,**kw)

    @classmethod
    def get_world(cls, *args,**kw):
        return ( cls.c.get('get_world', None) or cls.c.call(InternalName, 'get_world', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(InternalName, 'init_type', None) )(*args,**kw)

    @classmethod
    def make(cls, *args,**kw):
        return ( cls.c.get('make', None) or cls.c.call(InternalName, 'make', None) )(*args,**kw)

    @classmethod
    def register_with_read_factory(cls, *args,**kw):
        return ( cls.c.get('register_with_read_factory', None) or cls.c.call(InternalName, 'register_with_read_factory', None) )(*args,**kw)

    # instance method type calls

    c.ct['append'] = [
        ('d', 'p', 1, ('p', 'InternalName_C_append_p_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['finalize'] = [
        ('d', 'v', 1, ('v', 'InternalName_C_finalize_v_pp', 'pp'), ['BamReader*']),
    ]
    c.ct['find_ancestor'] = [
        ('d', 'i', 1, ('i', 'InternalName_C_find_ancestor_i_ss', 'ss'), ['std::string const&']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'InternalName_C_force_init_type_i_p', 'p'), []),
    ]
    c.ct['get_ancestor'] = [
        ('d', 's', 1, ('s', 'InternalName_C_get_ancestor_s_si', 'si'), ['int']),
    ]
    c.ct['get_basename'] = [
        ('d', 's', 0, ('s', 'InternalName_C_get_basename_s_p', 'p'), []),
    ]
    c.ct['get_name'] = [
        ('d', 's', 0, ('s', 'InternalName_C_get_name_s_p', 'p'), []),
    ]
    c.ct['get_net_basename'] = [
        ('d', 's', 1, ('s', 'InternalName_C_get_net_basename_s_si', 'si'), ['int']),
    ]
    c.ct['get_parent'] = [
        ('d', 21, 0, ('p', 'InternalName_C_get_parent_p_p', 'p'), []),
    ]
    c.ct['get_top'] = [
        ('d', 's', 0, ('s', 'InternalName_C_get_top_s_p', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'InternalName_C_get_type_i_p', 'p'), []),
    ]
    c.ct['join'] = [
        ('d', 's', 1, ('s', 'InternalName_C_join_s_ss', 'ss'), ['std::string const&']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'InternalName_C_output_v_sp', 'sp'), ['std::ostream&']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'InternalName_C_write_datagram_v_ppp', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(InternalName, attr, self)

InternalName.c.link(InternalName)



class CachedTypedWritableReferenceCount(TypedWritableReferenceCount):

    c = cxx.cstructs()
    c.register("CachedTypedWritableReferenceCount", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'CachedTypedWritableReferenceCount_C_get_class_type_i_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'CachedTypedWritableReferenceCount_C_init_type_v_v', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(CachedTypedWritableReferenceCount, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(CachedTypedWritableReferenceCount, 'init_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['cache_ref'] = [
        ('d', 'v', 0, ('v', 'CachedTypedWritableReferenceCount_C_cache_ref_v_p', 'p'), []),
    ]
    c.ct['cache_ref_only'] = [
        ('d', 'v', 0, ('v', 'CachedTypedWritableReferenceCount_C_cache_ref_only_v_p', 'p'), []),
    ]
    c.ct['cache_unref'] = [
        ('d', 'B', 0, ('B', 'CachedTypedWritableReferenceCount_C_cache_unref_B_p', 'p'), []),
    ]
    c.ct['get_cache_ref_count'] = [
        ('d', 'i', 0, ('i', 'CachedTypedWritableReferenceCount_C_get_cache_ref_count_i_p', 'p'), []),
    ]
    c.ct['test_ref_count_integrity'] = [
        ('d', 'B', 0, ('B', 'CachedTypedWritableReferenceCount_C_test_ref_count_integrity_B_p', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(CachedTypedWritableReferenceCount, attr, self)

CachedTypedWritableReferenceCount.c.link(CachedTypedWritableReferenceCount)



class CopyOnWriteObject(CachedTypedWritableReferenceCount):

    c = cxx.cstructs()
    c.register("CopyOnWriteObject", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_Geom'] = [
        ('d', 28, 0, ('p', 'CopyOnWriteObject_C_downcast_to_Geom_p_p', 'p'), []),
    ]
    c.ct['downcast_to_GeomPrimitive'] = [
        ('d', 25, 0, ('p', 'CopyOnWriteObject_C_downcast_to_GeomPrimitive_p_p', 'p'), []),
    ]
    c.ct['downcast_to_GeomVertexData'] = [
        ('d', 24, 0, ('p', 'CopyOnWriteObject_C_downcast_to_GeomVertexData_p_p', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(CopyOnWriteObject, attr, self)

CopyOnWriteObject.c.link(CopyOnWriteObject)



class GeomVertexData(CopyOnWriteObject, GeomEnums):

    c = cxx.cstructs()
    c.register("GeomVertexData", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 24, 1, ('p', 'GeomVertexData_C_ctor_p_p', 'p'), ['GeomVertexData const&']),
        ('s', 24, 2, ('p', 'GeomVertexData_C_ctor_p_pp', 'pp'), ['GeomVertexData const&', 'GeomVertexFormat const*']),
        ('s', 24, 3, ('p', 'GeomVertexData_C_ctor_p_spp', 'spp'), ['std::string const&', 'GeomVertexFormat const*', 'GeomEnums::UsageHint']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'GeomVertexData_C_get_class_type_i_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'GeomVertexData_C_init_type_v_v', ''), []),
    ]
    c.ct['pack_abcd'] = [
        ('s', 'I', 4, ('I', 'GeomVertexData_C_pack_abcd_I_IIII', 'IIII'), ['unsigned int', 'unsigned int', 'unsigned int', 'unsigned int']),
    ]
    c.ct['pack_ufloat'] = [
        ('s', 'I', 3, ('I', 'GeomVertexData_C_pack_ufloat_I_fff', 'fff'), ['float', 'float', 'float']),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'GeomVertexData_C_register_with_read_factory_v_v', ''), []),
    ]
    c.ct['unpack_abcd_a'] = [
        ('s', 'I', 1, ('I', 'GeomVertexData_C_unpack_abcd_a_I_I', 'I'), ['uint32_t']),
    ]
    c.ct['unpack_abcd_b'] = [
        ('s', 'I', 1, ('I', 'GeomVertexData_C_unpack_abcd_b_I_I', 'I'), ['uint32_t']),
    ]
    c.ct['unpack_abcd_c'] = [
        ('s', 'I', 1, ('I', 'GeomVertexData_C_unpack_abcd_c_I_I', 'I'), ['uint32_t']),
    ]
    c.ct['unpack_abcd_d'] = [
        ('s', 'I', 1, ('I', 'GeomVertexData_C_unpack_abcd_d_I_I', 'I'), ['uint32_t']),
    ]
    c.ct['unpack_ufloat_a'] = [
        ('s', 'f', 1, ('f', 'GeomVertexData_C_unpack_ufloat_a_f_I', 'I'), ['uint32_t']),
    ]
    c.ct['unpack_ufloat_b'] = [
        ('s', 'f', 1, ('f', 'GeomVertexData_C_unpack_ufloat_b_f_I', 'I'), ['uint32_t']),
    ]
    c.ct['unpack_ufloat_c'] = [
        ('s', 'f', 1, ('f', 'GeomVertexData_C_unpack_ufloat_c_f_I', 'I'), ['uint32_t']),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(GeomVertexData, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(GeomVertexData, 'init_type', None) )(*args,**kw)

    @classmethod
    def pack_abcd(cls, *args,**kw):
        return ( cls.c.get('pack_abcd', None) or cls.c.call(GeomVertexData, 'pack_abcd', None) )(*args,**kw)

    @classmethod
    def pack_ufloat(cls, *args,**kw):
        return ( cls.c.get('pack_ufloat', None) or cls.c.call(GeomVertexData, 'pack_ufloat', None) )(*args,**kw)

    @classmethod
    def register_with_read_factory(cls, *args,**kw):
        return ( cls.c.get('register_with_read_factory', None) or cls.c.call(GeomVertexData, 'register_with_read_factory', None) )(*args,**kw)

    @classmethod
    def unpack_abcd_a(cls, *args,**kw):
        return ( cls.c.get('unpack_abcd_a', None) or cls.c.call(GeomVertexData, 'unpack_abcd_a', None) )(*args,**kw)

    @classmethod
    def unpack_abcd_b(cls, *args,**kw):
        return ( cls.c.get('unpack_abcd_b', None) or cls.c.call(GeomVertexData, 'unpack_abcd_b', None) )(*args,**kw)

    @classmethod
    def unpack_abcd_c(cls, *args,**kw):
        return ( cls.c.get('unpack_abcd_c', None) or cls.c.call(GeomVertexData, 'unpack_abcd_c', None) )(*args,**kw)

    @classmethod
    def unpack_abcd_d(cls, *args,**kw):
        return ( cls.c.get('unpack_abcd_d', None) or cls.c.call(GeomVertexData, 'unpack_abcd_d', None) )(*args,**kw)

    @classmethod
    def unpack_ufloat_a(cls, *args,**kw):
        return ( cls.c.get('unpack_ufloat_a', None) or cls.c.call(GeomVertexData, 'unpack_ufloat_a', None) )(*args,**kw)

    @classmethod
    def unpack_ufloat_b(cls, *args,**kw):
        return ( cls.c.get('unpack_ufloat_b', None) or cls.c.call(GeomVertexData, 'unpack_ufloat_b', None) )(*args,**kw)

    @classmethod
    def unpack_ufloat_c(cls, *args,**kw):
        return ( cls.c.get('unpack_ufloat_c', None) or cls.c.call(GeomVertexData, 'unpack_ufloat_c', None) )(*args,**kw)

    # instance method type calls

    c.ct['animate_vertices'] = [
        ('d', 24, 2, ('p', 'GeomVertexData_C_animate_vertices_p_pBp', 'pBp'), ['bool', 'Thread*']),
    ]
    c.ct['clear_animated_vertices'] = [
        ('d', 'v', 0, ('v', 'GeomVertexData_C_clear_animated_vertices_v_p', 'p'), []),
    ]
    c.ct['clear_cache'] = [
        ('d', 'v', 0, ('v', 'GeomVertexData_C_clear_cache_v_p', 'p'), []),
    ]
    c.ct['clear_cache_stage'] = [
        ('d', 'v', 0, ('v', 'GeomVertexData_C_clear_cache_stage_v_p', 'p'), []),
    ]
    c.ct['clear_rows'] = [
        ('d', 'v', 0, ('v', 'GeomVertexData_C_clear_rows_v_p', 'p'), []),
    ]
    c.ct['clear_slider_table'] = [
        ('d', 'v', 0, ('v', 'GeomVertexData_C_clear_slider_table_v_p', 'p'), []),
    ]
    c.ct['clear_transform_blend_table'] = [
        ('d', 'v', 0, ('v', 'GeomVertexData_C_clear_transform_blend_table_v_p', 'p'), []),
    ]
    c.ct['clear_transform_table'] = [
        ('d', 'v', 0, ('v', 'GeomVertexData_C_clear_transform_table_v_p', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'GeomVertexData_C_compare_to_i_pp', 'pp'), ['GeomVertexData const&']),
    ]
    c.ct['convert_to'] = [
        ('d', 24, 1, ('p', 'GeomVertexData_C_convert_to_p_pp', 'pp'), ['GeomVertexFormat const*']),
    ]
    c.ct['copy_from'] = [
        ('d', 'v', 3, ('v', 'GeomVertexData_C_copy_from_v_ppBp', 'ppBp'), ['GeomVertexData const*', 'bool', 'Thread*']),
        ('d', 'v', 2, ('v', 'GeomVertexData_C_copy_from_v_ppB', 'ppB'), ['GeomVertexData const*', 'bool']),
    ]
    c.ct['copy_row_from'] = [
        ('d', 'v', 4, ('v', 'GeomVertexData_C_copy_row_from_v_pipip', 'pipip'), ['int', 'GeomVertexData const*', 'int', 'Thread*']),
    ]
    c.ct['describe_vertex'] = [
        ('d', 'v', 2, ('v', 'GeomVertexData_C_describe_vertex_v_ppi', 'ppi'), ['std::ostream&', 'int']),
    ]
    c.ct['finalize'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData_C_finalize_v_pp', 'pp'), ['BamReader*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'GeomVertexData_C_force_init_type_i_p', 'p'), []),
    ]
    c.ct['get_array'] = [
        ('d', 'p', 1, ('p', 'GeomVertexData_C_get_array_p_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['get_array_handle'] = [
        ('d', 'p', 1, ('p', 'GeomVertexData_C_get_array_handle_p_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['get_format'] = [
        ('d', 19, 0, ('p', 'GeomVertexData_C_get_format_p_p', 'p'), []),
    ]
    c.ct['get_modified'] = [
        ('d', 'p', 1, ('p', 'GeomVertexData_C_get_modified_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'GeomVertexData_C_get_modified_p_p', 'p'), []),
    ]
    c.ct['get_name'] = [
        ('d', 's', 0, ('s', 'GeomVertexData_C_get_name_s_p', 'p'), []),
    ]
    c.ct['get_num_arrays'] = [
        ('d', 'p', 0, ('p', 'GeomVertexData_C_get_num_arrays_p_p', 'p'), []),
    ]
    c.ct['get_num_bytes'] = [
        ('d', 'i', 0, ('i', 'GeomVertexData_C_get_num_bytes_i_p', 'p'), []),
    ]
    c.ct['get_num_rows'] = [
        ('d', 'i', 0, ('i', 'GeomVertexData_C_get_num_rows_i_p', 'p'), []),
    ]
    c.ct['get_slider_table'] = [
        ('d', 'p', 0, ('p', 'GeomVertexData_C_get_slider_table_p_p', 'p'), []),
    ]
    c.ct['get_transform_blend_table'] = [
        ('d', 'p', 0, ('p', 'GeomVertexData_C_get_transform_blend_table_p_p', 'p'), []),
    ]
    c.ct['get_transform_table'] = [
        ('d', 'p', 0, ('p', 'GeomVertexData_C_get_transform_table_p_p', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'GeomVertexData_C_get_type_i_p', 'p'), []),
    ]
    c.ct['get_usage_hint'] = [
        ('d', 'p', 0, ('p', 'GeomVertexData_C_get_usage_hint_p_p', 'p'), []),
    ]
    c.ct['has_column'] = [
        ('d', 'B', 1, ('B', 'GeomVertexData_C_has_column_B_ps', 'ps'), ['InternalName const*']),
    ]
    c.ct['modify_array'] = [
        ('d', 'p', 1, ('p', 'GeomVertexData_C_modify_array_p_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['modify_array_handle'] = [
        ('d', 'p', 1, ('p', 'GeomVertexData_C_modify_array_handle_p_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['modify_transform_blend_table'] = [
        ('d', 'p', 0, ('p', 'GeomVertexData_C_modify_transform_blend_table_p_p', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData_C_output_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['replace_column'] = [
        ('d', 24, 4, ('p', 'GeomVertexData_C_replace_column_p_ppipp', 'ppipp'), ['InternalName*', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents']),
    ]
    c.ct['request_resident'] = [
        ('d', 'B', 0, ('B', 'GeomVertexData_C_request_resident_B_p', 'p'), []),
    ]
    c.ct['require_fully_complete'] = [
        ('d', 'B', 0, ('B', 'GeomVertexData_C_require_fully_complete_B_p', 'p'), []),
    ]
    c.ct['reserve_num_rows'] = [
        ('d', 'B', 1, ('B', 'GeomVertexData_C_reserve_num_rows_B_pi', 'pi'), ['int']),
    ]
    c.ct['reverse_normals'] = [
        ('d', 24, 0, ('p', 'GeomVertexData_C_reverse_normals_p_p', 'p'), []),
    ]
    c.ct['scale_color'] = [
        ('d', 24, 1, ('p', 'GeomVertexData_C_scale_color_p_pp', 'pp'), ['LVecBase4 const&']),
        ('d', 24, 4, ('p', 'GeomVertexData_C_scale_color_p_ppipp', 'ppipp'), ['LVecBase4 const&', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents']),
    ]
    c.ct['set_array'] = [
        ('d', 'v', 2, ('v', 'GeomVertexData_C_set_array_v_ppp', 'ppp'), ['std::size_t', 'GeomVertexArrayData const*']),
    ]
    c.ct['set_color'] = [
        ('d', 24, 1, ('p', 'GeomVertexData_C_set_color_p_pp', 'pp'), ['LColor const&']),
        ('d', 24, 4, ('p', 'GeomVertexData_C_set_color_p_ppipp', 'ppipp'), ['LColor const&', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents']),
    ]
    c.ct['set_format'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData_C_set_format_v_pp', 'pp'), ['GeomVertexFormat const*']),
    ]
    c.ct['set_name'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData_C_set_name_v_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['set_num_rows'] = [
        ('d', 'B', 1, ('B', 'GeomVertexData_C_set_num_rows_B_pi', 'pi'), ['int']),
    ]
    c.ct['set_slider_table'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData_C_set_slider_table_v_pp', 'pp'), ['SliderTable const*']),
    ]
    c.ct['set_transform_blend_table'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData_C_set_transform_blend_table_v_pp', 'pp'), ['TransformBlendTable const*']),
    ]
    c.ct['set_transform_table'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData_C_set_transform_table_v_pp', 'pp'), ['TransformTable const*']),
    ]
    c.ct['set_usage_hint'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData_C_set_usage_hint_v_pp', 'pp'), ['GeomEnums::UsageHint']),
    ]
    c.ct['transform_vertices'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData_C_transform_vertices_v_pp', 'pp'), ['LMatrix4 const&']),
        ('d', 'v', 2, ('v', 'GeomVertexData_C_transform_vertices_v_ppp', 'ppp'), ['LMatrix4 const&', 'SparseArray const&']),
        ('d', 'v', 3, ('v', 'GeomVertexData_C_transform_vertices_v_ppii', 'ppii'), ['LMatrix4 const&', 'int', 'int']),
    ]
    c.ct['unclean_set_format'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData_C_unclean_set_format_v_pp', 'pp'), ['GeomVertexFormat const*']),
    ]
    c.ct['unclean_set_num_rows'] = [
        ('d', 'B', 1, ('B', 'GeomVertexData_C_unclean_set_num_rows_B_pi', 'pi'), ['int']),
    ]
    c.ct['upcast_to_CopyOnWriteObject'] = [
        ('d', 23, 0, ('p', 'GeomVertexData_C_upcast_to_CopyOnWriteObject_p_p', 'p'), []),
    ]
    c.ct['upcast_to_GeomEnums'] = [
        ('d', 3, 0, ('p', 'GeomVertexData_C_upcast_to_GeomEnums_p_p', 'p'), []),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'GeomVertexData_C_write_v_ppi', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'v', 1, ('v', 'GeomVertexData_C_write_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'GeomVertexData_C_write_datagram_v_ppp', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomVertexData, attr, self)

GeomVertexData.c.link(GeomVertexData)



class GeomPrimitive(CopyOnWriteObject, GeomEnums):

    c = cxx.cstructs()
    c.register("GeomPrimitive", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'GeomPrimitive_C_get_class_type_i_v', ''), []),
    ]
    c.ct['get_index_format'] = [
        ('s', 'p', 0, ('p', 'GeomPrimitive_C_get_index_format_p_p', 'p'), []),
        ('s', 'p', 1, ('p', 'GeomPrimitive_C_get_index_format_p_p_1_p_p', 'p'), ['GeomEnums::NumericType']),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'GeomPrimitive_C_init_type_v_v', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(GeomPrimitive, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_index_format(cls, *args,**kw):
        return ( cls.c.get('get_index_format', None) or cls.c.call(GeomPrimitive, 'get_index_format', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(GeomPrimitive, 'init_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_consecutive_vertices'] = [
        ('d', 'v', 2, ('v', 'GeomPrimitive_C_add_consecutive_vertices_v_pii', 'pii'), ['int', 'int']),
    ]
    c.ct['add_next_vertices'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive_C_add_next_vertices_v_pi', 'pi'), ['int']),
    ]
    c.ct['add_vertex'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive_C_add_vertex_v_pi', 'pi'), ['int']),
    ]
    c.ct['add_vertices'] = [
        ('d', 'v', 2, ('v', 'GeomPrimitive_C_add_vertices_v_pii', 'pii'), ['int', 'int']),
        ('d', 'v', 3, ('v', 'GeomPrimitive_C_add_vertices_v_piii', 'piii'), ['int', 'int', 'int']),
        ('d', 'v', 4, ('v', 'GeomPrimitive_C_add_vertices_v_piiii', 'piiii'), ['int', 'int', 'int', 'int']),
    ]
    c.ct['check_valid'] = [
        ('d', 'B', 1, ('B', 'GeomPrimitive_C_check_valid_B_pp', 'pp'), ['GeomVertexData const*']),
        ('d', 'B', 1, ('B', 'GeomPrimitive_C_check_valid_B_pp_1_B_pp', 'pp'), ['GeomVertexDataPipelineReader const*']),
    ]
    c.ct['clear_minmax'] = [
        ('d', 'v', 0, ('v', 'GeomPrimitive_C_clear_minmax_v_p', 'p'), []),
    ]
    c.ct['clear_vertices'] = [
        ('d', 'v', 0, ('v', 'GeomPrimitive_C_clear_vertices_v_p', 'p'), []),
    ]
    c.ct['close_primitive'] = [
        ('d', 'B', 0, ('B', 'GeomPrimitive_C_close_primitive_B_p', 'p'), []),
    ]
    c.ct['decompose'] = [
        ('d', 25, 0, ('p', 'GeomPrimitive_C_decompose_p_p', 'p'), []),
    ]
    c.ct['doubleside'] = [
        ('d', 25, 0, ('p', 'GeomPrimitive_C_doubleside_p_p', 'p'), []),
    ]
    c.ct['draw'] = [
        ('d', 'B', 3, ('B', 'GeomPrimitive_C_draw_B_pppB', 'pppB'), ['GraphicsStateGuardianBase*', 'GeomPrimitivePipelineReader const*', 'bool']),
    ]
    c.ct['finalize'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive_C_finalize_v_pp', 'pp'), ['BamReader*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive_C_force_init_type_i_p', 'p'), []),
    ]
    c.ct['get_data_size_bytes'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive_C_get_data_size_bytes_i_p', 'p'), []),
    ]
    c.ct['get_ends'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive_C_get_ends_p_p', 'p'), []),
    ]
    c.ct['get_first_vertex'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive_C_get_first_vertex_i_p', 'p'), []),
    ]
    c.ct['get_geom_rendering'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive_C_get_geom_rendering_i_p', 'p'), []),
    ]
    c.ct['get_index_format'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive_C_get_index_format_p_p', 'p'), []),
        ('d', 'p', 1, ('p', 'GeomPrimitive_C_get_index_format_p_p_1_p_p', 'p'), ['GeomEnums::NumericType']),
    ]
    c.ct['get_index_stride'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive_C_get_index_stride_i_p', 'p'), []),
    ]
    c.ct['get_index_type'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive_C_get_index_type_p_p', 'p'), []),
    ]
    c.ct['get_max_vertex'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive_C_get_max_vertex_i_p', 'p'), []),
    ]
    c.ct['get_maxs'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive_C_get_maxs_p_p', 'p'), []),
    ]
    c.ct['get_min_num_vertices_per_primitive'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive_C_get_min_num_vertices_per_primitive_i_p', 'p'), []),
    ]
    c.ct['get_min_vertex'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive_C_get_min_vertex_i_p', 'p'), []),
    ]
    c.ct['get_mins'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive_C_get_mins_p_p', 'p'), []),
    ]
    c.ct['get_modified'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive_C_get_modified_p_p', 'p'), []),
    ]
    c.ct['get_num_bytes'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive_C_get_num_bytes_i_p', 'p'), []),
    ]
    c.ct['get_num_faces'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive_C_get_num_faces_i_p', 'p'), []),
    ]
    c.ct['get_num_primitives'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive_C_get_num_primitives_i_p', 'p'), []),
    ]
    c.ct['get_num_unused_vertices_per_primitive'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive_C_get_num_unused_vertices_per_primitive_i_p', 'p'), []),
    ]
    c.ct['get_num_used_vertices'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive_C_get_num_used_vertices_i_p', 'p'), []),
    ]
    c.ct['get_num_vertices'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive_C_get_num_vertices_i_p', 'p'), []),
    ]
    c.ct['get_num_vertices_per_primitive'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive_C_get_num_vertices_per_primitive_i_p', 'p'), []),
    ]
    c.ct['get_primitive_end'] = [
        ('d', 'i', 1, ('i', 'GeomPrimitive_C_get_primitive_end_i_pi', 'pi'), ['int']),
    ]
    c.ct['get_primitive_max_vertex'] = [
        ('d', 'i', 1, ('i', 'GeomPrimitive_C_get_primitive_max_vertex_i_pi', 'pi'), ['int']),
    ]
    c.ct['get_primitive_min_vertex'] = [
        ('d', 'i', 1, ('i', 'GeomPrimitive_C_get_primitive_min_vertex_i_pi', 'pi'), ['int']),
    ]
    c.ct['get_primitive_num_faces'] = [
        ('d', 'i', 1, ('i', 'GeomPrimitive_C_get_primitive_num_faces_i_pi', 'pi'), ['int']),
    ]
    c.ct['get_primitive_num_vertices'] = [
        ('d', 'i', 1, ('i', 'GeomPrimitive_C_get_primitive_num_vertices_i_pi', 'pi'), ['int']),
    ]
    c.ct['get_primitive_start'] = [
        ('d', 'i', 1, ('i', 'GeomPrimitive_C_get_primitive_start_i_pi', 'pi'), ['int']),
    ]
    c.ct['get_primitive_type'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive_C_get_primitive_type_p_p', 'p'), []),
    ]
    c.ct['get_shade_model'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive_C_get_shade_model_p_p', 'p'), []),
    ]
    c.ct['get_strip_cut_index'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive_C_get_strip_cut_index_i_p', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive_C_get_type_i_p', 'p'), []),
    ]
    c.ct['get_usage_hint'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive_C_get_usage_hint_p_p', 'p'), []),
    ]
    c.ct['get_vertex'] = [
        ('d', 'i', 1, ('i', 'GeomPrimitive_C_get_vertex_i_pi', 'pi'), ['int']),
    ]
    c.ct['get_vertices'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive_C_get_vertices_p_p', 'p'), []),
    ]
    c.ct['get_vertices_handle'] = [
        ('d', 'p', 1, ('p', 'GeomPrimitive_C_get_vertices_handle_p_pp', 'pp'), ['Thread*']),
    ]
    c.ct['is_composite'] = [
        ('d', 'B', 0, ('B', 'GeomPrimitive_C_is_composite_B_p', 'p'), []),
    ]
    c.ct['is_indexed'] = [
        ('d', 'B', 0, ('B', 'GeomPrimitive_C_is_indexed_B_p', 'p'), []),
    ]
    c.ct['is_prepared'] = [
        ('d', 'B', 1, ('B', 'GeomPrimitive_C_is_prepared_B_pp', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['make_adjacency'] = [
        ('d', 25, 0, ('p', 'GeomPrimitive_C_make_adjacency_p_p', 'p'), []),
    ]
    c.ct['make_copy'] = [
        ('d', 25, 0, ('p', 'GeomPrimitive_C_make_copy_p_p', 'p'), []),
    ]
    c.ct['make_index_data'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive_C_make_index_data_p_p', 'p'), []),
    ]
    c.ct['make_indexed'] = [
        ('d', 'v', 0, ('v', 'GeomPrimitive_C_make_indexed_v_p', 'p'), []),
    ]
    c.ct['make_lines'] = [
        ('d', 25, 0, ('p', 'GeomPrimitive_C_make_lines_p_p', 'p'), []),
    ]
    c.ct['make_nonindexed'] = [
        ('d', 'v', 2, ('v', 'GeomPrimitive_C_make_nonindexed_v_ppp', 'ppp'), ['GeomVertexData*', 'GeomVertexData const*']),
    ]
    c.ct['make_patches'] = [
        ('d', 25, 0, ('p', 'GeomPrimitive_C_make_patches_p_p', 'p'), []),
    ]
    c.ct['make_points'] = [
        ('d', 25, 0, ('p', 'GeomPrimitive_C_make_points_p_p', 'p'), []),
    ]
    c.ct['match_shade_model'] = [
        ('d', 25, 1, ('p', 'GeomPrimitive_C_match_shade_model_p_pp', 'pp'), ['GeomEnums::ShadeModel']),
    ]
    c.ct['modify_ends'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive_C_modify_ends_p_p', 'p'), []),
    ]
    c.ct['modify_vertices'] = [
        ('d', 'p', 1, ('p', 'GeomPrimitive_C_modify_vertices_p_pi', 'pi'), ['int']),
        ('d', 'p', 0, ('p', 'GeomPrimitive_C_modify_vertices_p_p', 'p'), []),
    ]
    c.ct['modify_vertices_handle'] = [
        ('d', 'p', 1, ('p', 'GeomPrimitive_C_modify_vertices_handle_p_pp', 'pp'), ['Thread*']),
    ]
    c.ct['offset_vertices'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive_C_offset_vertices_v_pi', 'pi'), ['int']),
        ('d', 'v', 3, ('v', 'GeomPrimitive_C_offset_vertices_v_piii', 'piii'), ['int', 'int', 'int']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive_C_output_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['pack_vertices'] = [
        ('d', 'v', 2, ('v', 'GeomPrimitive_C_pack_vertices_v_ppp', 'ppp'), ['GeomVertexData*', 'GeomVertexData const*']),
    ]
    c.ct['prepare'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive_C_prepare_v_pp', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['prepare_now'] = [
        ('d', 'p', 2, ('p', 'GeomPrimitive_C_prepare_now_p_ppp', 'ppp'), ['PreparedGraphicsObjects*', 'GraphicsStateGuardianBase*']),
    ]
    c.ct['release'] = [
        ('d', 'B', 1, ('B', 'GeomPrimitive_C_release_B_pp', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['release_all'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive_C_release_all_i_p', 'p'), []),
    ]
    c.ct['request_resident'] = [
        ('d', 'B', 1, ('B', 'GeomPrimitive_C_request_resident_B_pp', 'pp'), ['Thread*']),
        ('d', 'B', 0, ('B', 'GeomPrimitive_C_request_resident_B_p', 'p'), []),
    ]
    c.ct['reserve_num_vertices'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive_C_reserve_num_vertices_v_pi', 'pi'), ['int']),
    ]
    c.ct['reverse'] = [
        ('d', 25, 0, ('p', 'GeomPrimitive_C_reverse_p_p', 'p'), []),
    ]
    c.ct['rotate'] = [
        ('d', 25, 0, ('p', 'GeomPrimitive_C_rotate_p_p', 'p'), []),
    ]
    c.ct['set_ends'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive_C_set_ends_v_pp', 'pp'), ['PTA_int']),
    ]
    c.ct['set_index_type'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive_C_set_index_type_v_pp', 'pp'), ['GeomEnums::NumericType']),
    ]
    c.ct['set_minmax'] = [
        ('d', 'v', 4, ('v', 'GeomPrimitive_C_set_minmax_v_piipp', 'piipp'), ['int', 'int', 'GeomVertexArrayData*', 'GeomVertexArrayData*']),
    ]
    c.ct['set_nonindexed_vertices'] = [
        ('d', 'v', 2, ('v', 'GeomPrimitive_C_set_nonindexed_vertices_v_pii', 'pii'), ['int', 'int']),
    ]
    c.ct['set_shade_model'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive_C_set_shade_model_v_pp', 'pp'), ['GeomEnums::ShadeModel']),
    ]
    c.ct['set_usage_hint'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive_C_set_usage_hint_v_pp', 'pp'), ['GeomEnums::UsageHint']),
    ]
    c.ct['set_vertices'] = [
        ('d', 'v', 2, ('v', 'GeomPrimitive_C_set_vertices_v_ppi', 'ppi'), ['GeomVertexArrayData const*', 'int']),
        ('d', 'v', 1, ('v', 'GeomPrimitive_C_set_vertices_v_pp', 'pp'), ['GeomVertexArrayData const*']),
    ]
    c.ct['upcast_to_CopyOnWriteObject'] = [
        ('d', 23, 0, ('p', 'GeomPrimitive_C_upcast_to_CopyOnWriteObject_p_p', 'p'), []),
    ]
    c.ct['upcast_to_GeomEnums'] = [
        ('d', 3, 0, ('p', 'GeomPrimitive_C_upcast_to_GeomEnums_p_p', 'p'), []),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'GeomPrimitive_C_write_v_ppi', 'ppi'), ['std::ostream&', 'int']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'GeomPrimitive_C_write_datagram_v_ppp', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomPrimitive, attr, self)

GeomPrimitive.c.link(GeomPrimitive)



class GeomTriangles(GeomPrimitive):

    c = cxx.cstructs()
    c.register("GeomTriangles", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 26, 1, ('p', 'GeomTriangles_C_ctor_p_p', 'p'), ['GeomEnums::UsageHint']),
        ('s', 26, 1, ('p', 'GeomTriangles_C_ctor_p_p_1_p_p', 'p'), ['GeomTriangles const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'GeomTriangles_C_get_class_type_i_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'GeomTriangles_C_init_type_v_v', ''), []),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'GeomTriangles_C_register_with_read_factory_v_v', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(GeomTriangles, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(GeomTriangles, 'init_type', None) )(*args,**kw)

    @classmethod
    def register_with_read_factory(cls, *args,**kw):
        return ( cls.c.get('register_with_read_factory', None) or cls.c.call(GeomTriangles, 'register_with_read_factory', None) )(*args,**kw)

    # instance method type calls

    c.ct['draw'] = [
        ('d', 'B', 3, ('B', 'GeomTriangles_C_draw_B_pppB', 'pppB'), ['GraphicsStateGuardianBase*', 'GeomPrimitivePipelineReader const*', 'bool']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'GeomTriangles_C_force_init_type_i_p', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'GeomTriangles_C_get_type_i_p', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomTriangles, attr, self)

GeomTriangles.c.link(GeomTriangles)



class GeomT(GeomTriangles):

    c = cxx.cstructs()
    c.register("GeomT", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 27, 1, ('p', 'GeomT_C_ctor_p_p', 'p'), ['GeomT const&']),
    ]

    # classmethod type calls


    # instance method type calls



    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomT, attr, self)

GeomT.c.link(GeomT)



class Geom(CopyOnWriteObject, GeomEnums):

    c = cxx.cstructs()
    c.register("Geom", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 28, 1, ('p', 'Geom_C_ctor_p_p', 'p'), ['GeomVertexData const*']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'Geom_C_get_class_type_i_v', ''), []),
    ]
    c.ct['get_next_modified'] = [
        ('s', 'p', 0, ('p', 'Geom_C_get_next_modified_p_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'Geom_C_init_type_v_v', ''), []),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'Geom_C_register_with_read_factory_v_v', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(Geom, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_next_modified(cls, *args,**kw):
        return ( cls.c.get('get_next_modified', None) or cls.c.call(Geom, 'get_next_modified', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(Geom, 'init_type', None) )(*args,**kw)

    @classmethod
    def register_with_read_factory(cls, *args,**kw):
        return ( cls.c.get('register_with_read_factory', None) or cls.c.call(Geom, 'register_with_read_factory', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_primitive'] = [
        ('d', 'v', 1, ('v', 'Geom_C_add_primitive_v_pp', 'pp'), ['GeomPrimitive const*']),
    ]
    c.ct['check_valid'] = [
        ('d', 'B', 0, ('B', 'Geom_C_check_valid_B_p', 'p'), []),
        ('d', 'B', 1, ('B', 'Geom_C_check_valid_B_pp', 'pp'), ['GeomVertexData const*']),
    ]
    c.ct['clear_bounds'] = [
        ('d', 'v', 0, ('v', 'Geom_C_clear_bounds_v_p', 'p'), []),
    ]
    c.ct['clear_cache'] = [
        ('d', 'v', 0, ('v', 'Geom_C_clear_cache_v_p', 'p'), []),
    ]
    c.ct['clear_cache_stage'] = [
        ('d', 'v', 1, ('v', 'Geom_C_clear_cache_stage_v_pp', 'pp'), ['Thread*']),
    ]
    c.ct['clear_primitives'] = [
        ('d', 'v', 0, ('v', 'Geom_C_clear_primitives_v_p', 'p'), []),
    ]
    c.ct['copy_primitives_from'] = [
        ('d', 'B', 1, ('B', 'Geom_C_copy_primitives_from_B_pp', 'pp'), ['Geom const*']),
    ]
    c.ct['decompose'] = [
        ('d', 28, 0, ('p', 'Geom_C_decompose_p_p', 'p'), []),
    ]
    c.ct['decompose_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom_C_decompose_in_place_v_p', 'p'), []),
    ]
    c.ct['doubleside'] = [
        ('d', 28, 0, ('p', 'Geom_C_doubleside_p_p', 'p'), []),
    ]
    c.ct['doubleside_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom_C_doubleside_in_place_v_p', 'p'), []),
    ]
    c.ct['draw'] = [
        ('d', 'B', 4, ('B', 'Geom_C_draw_B_pppBp', 'pppBp'), ['GraphicsStateGuardianBase*', 'GeomVertexData const*', 'bool', 'Thread*']),
    ]
    c.ct['finalize'] = [
        ('d', 'v', 1, ('v', 'Geom_C_finalize_v_pp', 'pp'), ['BamReader*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'Geom_C_force_init_type_i_p', 'p'), []),
    ]
    c.ct['get_animated_vertex_data'] = [
        ('d', 24, 2, ('p', 'Geom_C_get_animated_vertex_data_p_pBp', 'pBp'), ['bool', 'Thread*']),
        ('d', 24, 1, ('p', 'Geom_C_get_animated_vertex_data_p_pB', 'pB'), ['bool']),
    ]
    c.ct['get_bounds'] = [
        ('d', 'p', 1, ('p', 'Geom_C_get_bounds_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'Geom_C_get_bounds_p_p', 'p'), []),
    ]
    c.ct['get_bounds_type'] = [
        ('d', 'p', 0, ('p', 'Geom_C_get_bounds_type_p_p', 'p'), []),
    ]
    c.ct['get_geom_rendering'] = [
        ('d', 'i', 0, ('i', 'Geom_C_get_geom_rendering_i_p', 'p'), []),
    ]
    c.ct['get_modified'] = [
        ('d', 'p', 1, ('p', 'Geom_C_get_modified_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'Geom_C_get_modified_p_p', 'p'), []),
    ]
    c.ct['get_nested_vertices'] = [
        ('d', 'i', 1, ('i', 'Geom_C_get_nested_vertices_i_pp', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'Geom_C_get_nested_vertices_i_p', 'p'), []),
    ]
    c.ct['get_num_bytes'] = [
        ('d', 'i', 0, ('i', 'Geom_C_get_num_bytes_i_p', 'p'), []),
    ]
    c.ct['get_num_primitives'] = [
        ('d', 'p', 0, ('p', 'Geom_C_get_num_primitives_p_p', 'p'), []),
    ]
    c.ct['get_primitive'] = [
        ('d', 25, 1, ('p', 'Geom_C_get_primitive_p_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['get_primitive_type'] = [
        ('d', 'p', 0, ('p', 'Geom_C_get_primitive_type_p_p', 'p'), []),
    ]
    c.ct['get_shade_model'] = [
        ('d', 'p', 0, ('p', 'Geom_C_get_shade_model_p_p', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'Geom_C_get_type_i_p', 'p'), []),
    ]
    c.ct['get_usage_hint'] = [
        ('d', 'p', 0, ('p', 'Geom_C_get_usage_hint_p_p', 'p'), []),
    ]
    c.ct['get_vertex_data'] = [
        ('d', 24, 1, ('p', 'Geom_C_get_vertex_data_p_pp', 'pp'), ['Thread*']),
        ('d', 24, 0, ('p', 'Geom_C_get_vertex_data_p_p', 'p'), []),
    ]
    c.ct['insert_primitive'] = [
        ('d', 'v', 2, ('v', 'Geom_C_insert_primitive_v_ppp', 'ppp'), ['std::size_t', 'GeomPrimitive const*']),
    ]
    c.ct['is_empty'] = [
        ('d', 'B', 0, ('B', 'Geom_C_is_empty_B_p', 'p'), []),
    ]
    c.ct['is_prepared'] = [
        ('d', 'B', 1, ('B', 'Geom_C_is_prepared_B_pp', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['make_adjacency'] = [
        ('d', 28, 0, ('p', 'Geom_C_make_adjacency_p_p', 'p'), []),
    ]
    c.ct['make_adjacency_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom_C_make_adjacency_in_place_v_p', 'p'), []),
    ]
    c.ct['make_copy'] = [
        ('d', 28, 0, ('p', 'Geom_C_make_copy_p_p', 'p'), []),
    ]
    c.ct['make_lines'] = [
        ('d', 28, 0, ('p', 'Geom_C_make_lines_p_p', 'p'), []),
    ]
    c.ct['make_lines_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom_C_make_lines_in_place_v_p', 'p'), []),
    ]
    c.ct['make_nonindexed'] = [
        ('d', 'i', 1, ('i', 'Geom_C_make_nonindexed_i_pB', 'pB'), ['bool']),
    ]
    c.ct['make_patches'] = [
        ('d', 28, 0, ('p', 'Geom_C_make_patches_p_p', 'p'), []),
    ]
    c.ct['make_patches_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom_C_make_patches_in_place_v_p', 'p'), []),
    ]
    c.ct['make_points'] = [
        ('d', 28, 0, ('p', 'Geom_C_make_points_p_p', 'p'), []),
    ]
    c.ct['make_points_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom_C_make_points_in_place_v_p', 'p'), []),
    ]
    c.ct['mark_bounds_stale'] = [
        ('d', 'v', 0, ('v', 'Geom_C_mark_bounds_stale_v_p', 'p'), []),
    ]
    c.ct['modify_primitive'] = [
        ('d', 25, 1, ('p', 'Geom_C_modify_primitive_p_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['modify_vertex_data'] = [
        ('d', 24, 0, ('p', 'Geom_C_modify_vertex_data_p_p', 'p'), []),
    ]
    c.ct['offset_vertices'] = [
        ('d', 'v', 2, ('v', 'Geom_C_offset_vertices_v_ppi', 'ppi'), ['GeomVertexData const*', 'int']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'Geom_C_output_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['prepare'] = [
        ('d', 'v', 1, ('v', 'Geom_C_prepare_v_pp', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['prepare_now'] = [
        ('d', 'p', 2, ('p', 'Geom_C_prepare_now_p_ppp', 'ppp'), ['PreparedGraphicsObjects*', 'GraphicsStateGuardianBase*']),
    ]
    c.ct['release'] = [
        ('d', 'B', 1, ('B', 'Geom_C_release_B_pp', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['release_all'] = [
        ('d', 'i', 0, ('i', 'Geom_C_release_all_i_p', 'p'), []),
    ]
    c.ct['remove_primitive'] = [
        ('d', 'v', 1, ('v', 'Geom_C_remove_primitive_v_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['request_resident'] = [
        ('d', 'B', 0, ('B', 'Geom_C_request_resident_B_p', 'p'), []),
    ]
    c.ct['reverse'] = [
        ('d', 28, 0, ('p', 'Geom_C_reverse_p_p', 'p'), []),
    ]
    c.ct['reverse_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom_C_reverse_in_place_v_p', 'p'), []),
    ]
    c.ct['rotate'] = [
        ('d', 28, 0, ('p', 'Geom_C_rotate_p_p', 'p'), []),
    ]
    c.ct['rotate_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom_C_rotate_in_place_v_p', 'p'), []),
    ]
    c.ct['set_bounds'] = [
        ('d', 'v', 1, ('v', 'Geom_C_set_bounds_v_pp', 'pp'), ['BoundingVolume const*']),
    ]
    c.ct['set_bounds_type'] = [
        ('d', 'v', 1, ('v', 'Geom_C_set_bounds_type_v_pp', 'pp'), ['BoundingVolume::BoundsType']),
    ]
    c.ct['set_primitive'] = [
        ('d', 'v', 2, ('v', 'Geom_C_set_primitive_v_ppp', 'ppp'), ['std::size_t', 'GeomPrimitive const*']),
    ]
    c.ct['set_usage_hint'] = [
        ('d', 'v', 1, ('v', 'Geom_C_set_usage_hint_v_pp', 'pp'), ['GeomEnums::UsageHint']),
    ]
    c.ct['set_vertex_data'] = [
        ('d', 'v', 1, ('v', 'Geom_C_set_vertex_data_v_pp', 'pp'), ['GeomVertexData const*']),
    ]
    c.ct['transform_vertices'] = [
        ('d', 'v', 1, ('v', 'Geom_C_transform_vertices_v_pp', 'pp'), ['LMatrix4 const&']),
    ]
    c.ct['unify'] = [
        ('d', 28, 2, ('p', 'Geom_C_unify_p_piB', 'piB'), ['int', 'bool']),
    ]
    c.ct['unify_in_place'] = [
        ('d', 'v', 2, ('v', 'Geom_C_unify_in_place_v_piB', 'piB'), ['int', 'bool']),
    ]
    c.ct['upcast_to_CopyOnWriteObject'] = [
        ('d', 23, 0, ('p', 'Geom_C_upcast_to_CopyOnWriteObject_p_p', 'p'), []),
    ]
    c.ct['upcast_to_GeomEnums'] = [
        ('d', 3, 0, ('p', 'Geom_C_upcast_to_GeomEnums_p_p', 'p'), []),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'Geom_C_write_v_ppi', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'v', 1, ('v', 'Geom_C_write_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'Geom_C_write_datagram_v_ppp', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(Geom, attr, self)

Geom.c.link(Geom)



class PandaNode(TypedWritableReferenceCount, Namable, LinkedListNode):

    c = cxx.cstructs()
    c.register("PandaNode", "upanda3d", """libupanda3d_cni.so""")

    # enum FancyBits

    FB_cull_callback = const(64)
    FB_draw_mask = const(32)
    FB_effects = const(4)
    FB_state = const(2)
    FB_tag = const(16)
    FB_transform = const(1)


    # enum UnexpectedChange

    UC_children = const(2)
    UC_draw_mask = const(16)
    UC_parents = const(1)
    UC_state = const(8)
    UC_transform = const(4)


    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 29, 1, ('p', 'PandaNode_C_ctor_p_s', 's'), ['std::string const&']),
    ]

    # classmethod type calls

    c.ct['decode_from_bam_stream'] = [
        ('s', 29, 2, ('p', 'PandaNode_C_decode_from_bam_stream_p_pp', 'pp'), ['vector_uchar', 'BamReader*']),
        ('s', 29, 1, ('p', 'PandaNode_C_decode_from_bam_stream_p_p', 'p'), ['vector_uchar']),
    ]
    c.ct['get_all_camera_mask'] = [
        ('s', 'p', 0, ('p', 'PandaNode_C_get_all_camera_mask_p_v', ''), []),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'PandaNode_C_get_class_type_i_v', ''), []),
    ]
    c.ct['get_overall_bit'] = [
        ('s', 'p', 0, ('p', 'PandaNode_C_get_overall_bit_p_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'PandaNode_C_init_type_v_v', ''), []),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'PandaNode_C_register_with_read_factory_v_v', ''), []),
    ]
    c.ct['reset_all_prev_transform'] = [
        ('s', 'v', 1, ('v', 'PandaNode_C_reset_all_prev_transform_v_p', 'p'), ['Thread*']),
        ('s', 'v', 0, ('v', 'PandaNode_C_reset_all_prev_transform_v_v', ''), []),
    ]

    @classmethod
    def decode_from_bam_stream(cls, *args,**kw):
        return ( cls.c.get('decode_from_bam_stream', None) or cls.c.call(PandaNode, 'decode_from_bam_stream', None) )(*args,**kw)

    @classmethod
    def get_all_camera_mask(cls, *args,**kw):
        return ( cls.c.get('get_all_camera_mask', None) or cls.c.call(PandaNode, 'get_all_camera_mask', None) )(*args,**kw)

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(PandaNode, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_overall_bit(cls, *args,**kw):
        return ( cls.c.get('get_overall_bit', None) or cls.c.call(PandaNode, 'get_overall_bit', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(PandaNode, 'init_type', None) )(*args,**kw)

    @classmethod
    def register_with_read_factory(cls, *args,**kw):
        return ( cls.c.get('register_with_read_factory', None) or cls.c.call(PandaNode, 'register_with_read_factory', None) )(*args,**kw)

    @classmethod
    def reset_all_prev_transform(cls, *args,**kw):
        return ( cls.c.get('reset_all_prev_transform', None) or cls.c.call(PandaNode, 'reset_all_prev_transform', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_child'] = [
        ('d', 'v', 3, ('v', 'PandaNode_C_add_child_v_ppip', 'ppip'), ['PandaNode*', 'int', 'Thread*']),
        ('d', 'v', 2, ('v', 'PandaNode_C_add_child_v_ppi', 'ppi'), ['PandaNode*', 'int']),
        ('d', 'v', 1, ('v', 'PandaNode_C_add_child_v_pp', 'pp'), ['PandaNode*']),
    ]
    c.ct['add_for_draw'] = [
        ('d', 'v', 2, ('v', 'PandaNode_C_add_for_draw_v_ppp', 'ppp'), ['CullTraverser*', 'CullTraverserData&']),
    ]
    c.ct['add_stashed'] = [
        ('d', 'v', 3, ('v', 'PandaNode_C_add_stashed_v_ppip', 'ppip'), ['PandaNode*', 'int', 'Thread*']),
        ('d', 'v', 2, ('v', 'PandaNode_C_add_stashed_v_ppi', 'ppi'), ['PandaNode*', 'int']),
        ('d', 'v', 1, ('v', 'PandaNode_C_add_stashed_v_pp', 'pp'), ['PandaNode*']),
    ]
    c.ct['adjust_draw_mask'] = [
        ('d', 'v', 3, ('v', 'PandaNode_C_adjust_draw_mask_v_pppp', 'pppp'), ['DrawMask', 'DrawMask', 'DrawMask']),
    ]
    c.ct['apply_attribs_to_vertices'] = [
        ('d', 'v', 3, ('v', 'PandaNode_C_apply_attribs_to_vertices_v_ppip', 'ppip'), ['AccumulatedAttribs const&', 'int', 'GeomTransformer&']),
    ]
    c.ct['as_light'] = [
        ('d', 'p', 0, ('p', 'PandaNode_C_as_light_p_p', 'p'), []),
    ]
    c.ct['clear_attrib'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_clear_attrib_v_pi', 'pi'), ['TypeHandle']),
        ('d', 'v', 1, ('v', 'PandaNode_C_clear_attrib_v_pi_1_v_pi', 'pi'), ['int']),
    ]
    c.ct['clear_bounds'] = [
        ('d', 'v', 0, ('v', 'PandaNode_C_clear_bounds_v_p', 'p'), []),
    ]
    c.ct['clear_effect'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_clear_effect_v_pi', 'pi'), ['TypeHandle']),
    ]
    c.ct['clear_effects'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_clear_effects_v_pp', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'PandaNode_C_clear_effects_v_p', 'p'), []),
    ]
    c.ct['clear_state'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_clear_state_v_pp', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'PandaNode_C_clear_state_v_p', 'p'), []),
    ]
    c.ct['clear_tag'] = [
        ('d', 'v', 2, ('v', 'PandaNode_C_clear_tag_v_psp', 'psp'), ['std::string const&', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode_C_clear_tag_v_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['clear_transform'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_clear_transform_v_pp', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'PandaNode_C_clear_transform_v_p', 'p'), []),
    ]
    c.ct['clear_unexpected_change'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_clear_unexpected_change_v_pI', 'pI'), ['unsigned int']),
    ]
    c.ct['combine_with'] = [
        ('d', 29, 1, ('p', 'PandaNode_C_combine_with_p_pp', 'pp'), ['PandaNode*']),
    ]
    c.ct['compare_tags'] = [
        ('d', 'i', 1, ('i', 'PandaNode_C_compare_tags_i_pp', 'pp'), ['PandaNode const*']),
    ]
    c.ct['copy_all_properties'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_copy_all_properties_v_pp', 'pp'), ['PandaNode*']),
    ]
    c.ct['copy_children'] = [
        ('d', 'v', 2, ('v', 'PandaNode_C_copy_children_v_ppp', 'ppp'), ['PandaNode*', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode_C_copy_children_v_pp', 'pp'), ['PandaNode*']),
    ]
    c.ct['copy_subgraph'] = [
        ('d', 29, 1, ('p', 'PandaNode_C_copy_subgraph_p_pp', 'pp'), ['Thread*']),
        ('d', 29, 0, ('p', 'PandaNode_C_copy_subgraph_p_p', 'p'), []),
    ]
    c.ct['copy_tags'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_copy_tags_v_pp', 'pp'), ['PandaNode*']),
    ]
    c.ct['count_num_descendants'] = [
        ('d', 'i', 0, ('i', 'PandaNode_C_count_num_descendants_i_p', 'p'), []),
    ]
    c.ct['cull_callback'] = [
        ('d', 'B', 2, ('B', 'PandaNode_C_cull_callback_B_ppp', 'ppp'), ['CullTraverser*', 'CullTraverserData&']),
    ]
    c.ct['dupe_for_flatten'] = [
        ('d', 29, 0, ('p', 'PandaNode_C_dupe_for_flatten_p_p', 'p'), []),
    ]
    c.ct['find_child'] = [
        ('d', 'i', 2, ('i', 'PandaNode_C_find_child_i_ppp', 'ppp'), ['PandaNode*', 'Thread*']),
        ('d', 'i', 1, ('i', 'PandaNode_C_find_child_i_pp', 'pp'), ['PandaNode*']),
    ]
    c.ct['find_parent'] = [
        ('d', 'i', 2, ('i', 'PandaNode_C_find_parent_i_ppp', 'ppp'), ['PandaNode*', 'Thread*']),
        ('d', 'i', 1, ('i', 'PandaNode_C_find_parent_i_pp', 'pp'), ['PandaNode*']),
    ]
    c.ct['find_stashed'] = [
        ('d', 'i', 2, ('i', 'PandaNode_C_find_stashed_i_ppp', 'ppp'), ['PandaNode*', 'Thread*']),
        ('d', 'i', 1, ('i', 'PandaNode_C_find_stashed_i_pp', 'pp'), ['PandaNode*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'PandaNode_C_force_init_type_i_p', 'p'), []),
    ]
    c.ct['get_attrib'] = [
        ('d', 'p', 1, ('p', 'PandaNode_C_get_attrib_p_pi', 'pi'), ['TypeHandle']),
        ('d', 'p', 1, ('p', 'PandaNode_C_get_attrib_p_pi_1_p_pi', 'pi'), ['int']),
    ]
    c.ct['get_bounds'] = [
        ('d', 'p', 1, ('p', 'PandaNode_C_get_bounds_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode_C_get_bounds_p_p', 'p'), []),
        ('d', 'p', 2, ('p', 'PandaNode_C_get_bounds_p_ppp', 'ppp'), ['UpdateSeq&', 'Thread*']),
        ('d', 'p', 1, ('p', 'PandaNode_C_get_bounds_p_pp_1_p_pp', 'pp'), ['UpdateSeq&']),
    ]
    c.ct['get_bounds_type'] = [
        ('d', 'p', 0, ('p', 'PandaNode_C_get_bounds_type_p_p', 'p'), []),
    ]
    c.ct['get_child'] = [
        ('d', 29, 2, ('p', 'PandaNode_C_get_child_p_pip', 'pip'), ['int', 'Thread*']),
        ('d', 29, 1, ('p', 'PandaNode_C_get_child_p_pi', 'pi'), ['int']),
    ]
    c.ct['get_child_sort'] = [
        ('d', 'i', 2, ('i', 'PandaNode_C_get_child_sort_i_pip', 'pip'), ['int', 'Thread*']),
        ('d', 'i', 1, ('i', 'PandaNode_C_get_child_sort_i_pi', 'pi'), ['int']),
    ]
    c.ct['get_children'] = [
        ('d', 'p', 1, ('p', 'PandaNode_C_get_children_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode_C_get_children_p_p', 'p'), []),
    ]
    c.ct['get_draw_control_mask'] = [
        ('d', 'p', 0, ('p', 'PandaNode_C_get_draw_control_mask_p_p', 'p'), []),
    ]
    c.ct['get_draw_show_mask'] = [
        ('d', 'p', 0, ('p', 'PandaNode_C_get_draw_show_mask_p_p', 'p'), []),
    ]
    c.ct['get_effect'] = [
        ('d', 'p', 1, ('p', 'PandaNode_C_get_effect_p_pi', 'pi'), ['TypeHandle']),
    ]
    c.ct['get_effects'] = [
        ('d', 'p', 1, ('p', 'PandaNode_C_get_effects_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode_C_get_effects_p_p', 'p'), []),
    ]
    c.ct['get_fancy_bits'] = [
        ('d', 'i', 1, ('i', 'PandaNode_C_get_fancy_bits_i_pp', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'PandaNode_C_get_fancy_bits_i_p', 'p'), []),
    ]
    c.ct['get_first_visible_child'] = [
        ('d', 'i', 0, ('i', 'PandaNode_C_get_first_visible_child_i_p', 'p'), []),
    ]
    c.ct['get_internal_bounds'] = [
        ('d', 'p', 1, ('p', 'PandaNode_C_get_internal_bounds_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode_C_get_internal_bounds_p_p', 'p'), []),
    ]
    c.ct['get_internal_vertices'] = [
        ('d', 'i', 1, ('i', 'PandaNode_C_get_internal_vertices_i_pp', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'PandaNode_C_get_internal_vertices_i_p', 'p'), []),
    ]
    c.ct['get_into_collide_mask'] = [
        ('d', 'p', 0, ('p', 'PandaNode_C_get_into_collide_mask_p_p', 'p'), []),
    ]
    c.ct['get_legal_collide_mask'] = [
        ('d', 'p', 0, ('p', 'PandaNode_C_get_legal_collide_mask_p_p', 'p'), []),
    ]
    c.ct['get_nested_vertices'] = [
        ('d', 'i', 1, ('i', 'PandaNode_C_get_nested_vertices_i_pp', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'PandaNode_C_get_nested_vertices_i_p', 'p'), []),
    ]
    c.ct['get_net_collide_mask'] = [
        ('d', 'p', 1, ('p', 'PandaNode_C_get_net_collide_mask_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode_C_get_net_collide_mask_p_p', 'p'), []),
    ]
    c.ct['get_net_draw_control_mask'] = [
        ('d', 'p', 0, ('p', 'PandaNode_C_get_net_draw_control_mask_p_p', 'p'), []),
    ]
    c.ct['get_net_draw_show_mask'] = [
        ('d', 'p', 0, ('p', 'PandaNode_C_get_net_draw_show_mask_p_p', 'p'), []),
    ]
    c.ct['get_next_visible_child'] = [
        ('d', 'i', 1, ('i', 'PandaNode_C_get_next_visible_child_i_pi', 'pi'), ['int']),
    ]
    c.ct['get_num_children'] = [
        ('d', 'i', 1, ('i', 'PandaNode_C_get_num_children_i_pp', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'PandaNode_C_get_num_children_i_p', 'p'), []),
    ]
    c.ct['get_num_parents'] = [
        ('d', 'i', 1, ('i', 'PandaNode_C_get_num_parents_i_pp', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'PandaNode_C_get_num_parents_i_p', 'p'), []),
    ]
    c.ct['get_num_stashed'] = [
        ('d', 'i', 1, ('i', 'PandaNode_C_get_num_stashed_i_pp', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'PandaNode_C_get_num_stashed_i_p', 'p'), []),
    ]
    c.ct['get_num_tags'] = [
        ('d', 'p', 0, ('p', 'PandaNode_C_get_num_tags_p_p', 'p'), []),
    ]
    c.ct['get_off_clip_planes'] = [
        ('d', 'p', 1, ('p', 'PandaNode_C_get_off_clip_planes_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode_C_get_off_clip_planes_p_p', 'p'), []),
    ]
    c.ct['get_parent'] = [
        ('d', 29, 2, ('p', 'PandaNode_C_get_parent_p_pip', 'pip'), ['int', 'Thread*']),
        ('d', 29, 1, ('p', 'PandaNode_C_get_parent_p_pi', 'pi'), ['int']),
    ]
    c.ct['get_parents'] = [
        ('d', 'p', 1, ('p', 'PandaNode_C_get_parents_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode_C_get_parents_p_p', 'p'), []),
    ]
    c.ct['get_prev_transform'] = [
        ('d', 'p', 1, ('p', 'PandaNode_C_get_prev_transform_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode_C_get_prev_transform_p_p', 'p'), []),
    ]
    c.ct['get_stashed'] = [
        ('d', 'p', 1, ('p', 'PandaNode_C_get_stashed_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode_C_get_stashed_p_p', 'p'), []),
        ('d', 29, 2, ('p', 'PandaNode_C_get_stashed_p_pip', 'pip'), ['int', 'Thread*']),
        ('d', 29, 1, ('p', 'PandaNode_C_get_stashed_p_pi', 'pi'), ['int']),
    ]
    c.ct['get_stashed_sort'] = [
        ('d', 'i', 2, ('i', 'PandaNode_C_get_stashed_sort_i_pip', 'pip'), ['int', 'Thread*']),
        ('d', 'i', 1, ('i', 'PandaNode_C_get_stashed_sort_i_pi', 'pi'), ['int']),
    ]
    c.ct['get_state'] = [
        ('d', 'p', 1, ('p', 'PandaNode_C_get_state_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode_C_get_state_p_p', 'p'), []),
    ]
    c.ct['get_tag'] = [
        ('d', 's', 2, ('s', 'PandaNode_C_get_tag_s_psp', 'psp'), ['std::string const&', 'Thread*']),
        ('d', 's', 1, ('s', 'PandaNode_C_get_tag_s_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['get_tag_key'] = [
        ('d', 's', 1, ('s', 'PandaNode_C_get_tag_key_s_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['get_tag_keys'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_get_tag_keys_v_pp', 'pp'), ['vector_string&']),
    ]
    c.ct['get_transform'] = [
        ('d', 'p', 1, ('p', 'PandaNode_C_get_transform_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode_C_get_transform_p_p', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'PandaNode_C_get_type_i_p', 'p'), []),
    ]
    c.ct['get_unexpected_change'] = [
        ('d', 'I', 1, ('I', 'PandaNode_C_get_unexpected_change_I_pI', 'pI'), ['unsigned int']),
    ]
    c.ct['get_unsafe_to_apply_attribs'] = [
        ('d', 'i', 0, ('i', 'PandaNode_C_get_unsafe_to_apply_attribs_i_p', 'p'), []),
    ]
    c.ct['get_visible_child'] = [
        ('d', 'i', 0, ('i', 'PandaNode_C_get_visible_child_i_p', 'p'), []),
    ]
    c.ct['has_attrib'] = [
        ('d', 'B', 1, ('B', 'PandaNode_C_has_attrib_B_pi', 'pi'), ['TypeHandle']),
        ('d', 'B', 1, ('B', 'PandaNode_C_has_attrib_B_pi_1_B_pi', 'pi'), ['int']),
    ]
    c.ct['has_dirty_prev_transform'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_has_dirty_prev_transform_B_p', 'p'), []),
    ]
    c.ct['has_effect'] = [
        ('d', 'B', 1, ('B', 'PandaNode_C_has_effect_B_pi', 'pi'), ['TypeHandle']),
    ]
    c.ct['has_selective_visibility'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_has_selective_visibility_B_p', 'p'), []),
    ]
    c.ct['has_single_child_visibility'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_has_single_child_visibility_B_p', 'p'), []),
    ]
    c.ct['has_tag'] = [
        ('d', 'B', 2, ('B', 'PandaNode_C_has_tag_B_psp', 'psp'), ['std::string const&', 'Thread*']),
        ('d', 'B', 1, ('B', 'PandaNode_C_has_tag_B_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['has_tags'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_has_tags_B_p', 'p'), []),
    ]
    c.ct['is_ambient_light'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_is_ambient_light_B_p', 'p'), []),
    ]
    c.ct['is_bounds_stale'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_is_bounds_stale_B_p', 'p'), []),
    ]
    c.ct['is_collision_node'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_is_collision_node_B_p', 'p'), []),
    ]
    c.ct['is_final'] = [
        ('d', 'B', 1, ('B', 'PandaNode_C_is_final_B_pp', 'pp'), ['Thread*']),
        ('d', 'B', 0, ('B', 'PandaNode_C_is_final_B_p', 'p'), []),
    ]
    c.ct['is_geom_node'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_is_geom_node_B_p', 'p'), []),
    ]
    c.ct['is_lod_node'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_is_lod_node_B_p', 'p'), []),
    ]
    c.ct['is_overall_hidden'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_is_overall_hidden_B_p', 'p'), []),
    ]
    c.ct['is_renderable'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_is_renderable_B_p', 'p'), []),
    ]
    c.ct['is_scene_root'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_is_scene_root_B_p', 'p'), []),
    ]
    c.ct['is_under_scene_root'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_is_under_scene_root_B_p', 'p'), []),
    ]
    c.ct['list_tags'] = [
        ('d', 'v', 2, ('v', 'PandaNode_C_list_tags_v_pps', 'pps'), ['std::ostream&', 'std::string const&']),
        ('d', 'v', 1, ('v', 'PandaNode_C_list_tags_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['ls'] = [
        ('d', 'v', 2, ('v', 'PandaNode_C_ls_v_ppi', 'ppi'), ['std::ostream&', 'int']),
    ]
    c.ct['make_copy'] = [
        ('d', 29, 0, ('p', 'PandaNode_C_make_copy_p_p', 'p'), []),
    ]
    c.ct['mark_bounds_stale'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_mark_bounds_stale_v_pp', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'PandaNode_C_mark_bounds_stale_v_p', 'p'), []),
    ]
    c.ct['mark_internal_bounds_stale'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_mark_internal_bounds_stale_v_pp', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'PandaNode_C_mark_internal_bounds_stale_v_p', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_output_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['prepare_scene'] = [
        ('d', 'v', 2, ('v', 'PandaNode_C_prepare_scene_v_ppp', 'ppp'), ['GraphicsStateGuardianBase*', 'RenderState const*']),
    ]
    c.ct['preserve_name'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_preserve_name_B_p', 'p'), []),
    ]
    c.ct['r_prepare_scene'] = [
        ('d', 'v', 4, ('v', 'PandaNode_C_r_prepare_scene_v_ppppp', 'ppppp'), ['GraphicsStateGuardianBase*', 'RenderState const*', 'GeomTransformer&', 'Thread*']),
    ]
    c.ct['remove_all_children'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_remove_all_children_v_pp', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'PandaNode_C_remove_all_children_v_p', 'p'), []),
    ]
    c.ct['remove_child'] = [
        ('d', 'B', 2, ('B', 'PandaNode_C_remove_child_B_ppp', 'ppp'), ['PandaNode*', 'Thread*']),
        ('d', 'B', 1, ('B', 'PandaNode_C_remove_child_B_pp', 'pp'), ['PandaNode*']),
        ('d', 'v', 2, ('v', 'PandaNode_C_remove_child_v_pip', 'pip'), ['int', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode_C_remove_child_v_pi', 'pi'), ['int']),
    ]
    c.ct['remove_stashed'] = [
        ('d', 'v', 2, ('v', 'PandaNode_C_remove_stashed_v_pip', 'pip'), ['int', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode_C_remove_stashed_v_pi', 'pi'), ['int']),
    ]
    c.ct['replace_child'] = [
        ('d', 'B', 3, ('B', 'PandaNode_C_replace_child_B_pppp', 'pppp'), ['PandaNode*', 'PandaNode*', 'Thread*']),
        ('d', 'B', 2, ('B', 'PandaNode_C_replace_child_B_ppp', 'ppp'), ['PandaNode*', 'PandaNode*']),
    ]
    c.ct['replace_node'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_replace_node_v_pp', 'pp'), ['PandaNode*']),
    ]
    c.ct['reset_prev_transform'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_reset_prev_transform_v_pp', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'PandaNode_C_reset_prev_transform_v_p', 'p'), []),
    ]
    c.ct['safe_to_combine'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_safe_to_combine_B_p', 'p'), []),
    ]
    c.ct['safe_to_combine_children'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_safe_to_combine_children_B_p', 'p'), []),
    ]
    c.ct['safe_to_flatten'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_safe_to_flatten_B_p', 'p'), []),
    ]
    c.ct['safe_to_flatten_below'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_safe_to_flatten_below_B_p', 'p'), []),
    ]
    c.ct['safe_to_modify_transform'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_safe_to_modify_transform_B_p', 'p'), []),
    ]
    c.ct['safe_to_transform'] = [
        ('d', 'B', 0, ('B', 'PandaNode_C_safe_to_transform_B_p', 'p'), []),
    ]
    c.ct['set_attrib'] = [
        ('d', 'v', 2, ('v', 'PandaNode_C_set_attrib_v_ppi', 'ppi'), ['RenderAttrib const*', 'int']),
        ('d', 'v', 1, ('v', 'PandaNode_C_set_attrib_v_pp', 'pp'), ['RenderAttrib const*']),
    ]
    c.ct['set_bound'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_set_bound_v_pp', 'pp'), ['BoundingVolume const*']),
    ]
    c.ct['set_bounds'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_set_bounds_v_pp', 'pp'), ['BoundingVolume const*']),
    ]
    c.ct['set_bounds_type'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_set_bounds_type_v_pp', 'pp'), ['BoundingVolume::BoundsType']),
    ]
    c.ct['set_effect'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_set_effect_v_pp', 'pp'), ['RenderEffect const*']),
    ]
    c.ct['set_effects'] = [
        ('d', 'v', 2, ('v', 'PandaNode_C_set_effects_v_ppp', 'ppp'), ['RenderEffects const*', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode_C_set_effects_v_pp', 'pp'), ['RenderEffects const*']),
    ]
    c.ct['set_final'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_set_final_v_pB', 'pB'), ['bool']),
    ]
    c.ct['set_into_collide_mask'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_set_into_collide_mask_v_pp', 'pp'), ['CollideMask']),
    ]
    c.ct['set_overall_hidden'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_set_overall_hidden_v_pB', 'pB'), ['bool']),
    ]
    c.ct['set_prev_transform'] = [
        ('d', 'v', 2, ('v', 'PandaNode_C_set_prev_transform_v_ppp', 'ppp'), ['TransformState const*', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode_C_set_prev_transform_v_pp', 'pp'), ['TransformState const*']),
    ]
    c.ct['set_state'] = [
        ('d', 'v', 2, ('v', 'PandaNode_C_set_state_v_ppp', 'ppp'), ['RenderState const*', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode_C_set_state_v_pp', 'pp'), ['RenderState const*']),
    ]
    c.ct['set_tag'] = [
        ('d', 'v', 3, ('v', 'PandaNode_C_set_tag_v_pssp', 'pssp'), ['std::string const&', 'std::string const&', 'Thread*']),
        ('d', 'v', 2, ('v', 'PandaNode_C_set_tag_v_pss', 'pss'), ['std::string const&', 'std::string const&']),
    ]
    c.ct['set_transform'] = [
        ('d', 'v', 2, ('v', 'PandaNode_C_set_transform_v_ppp', 'ppp'), ['TransformState const*', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode_C_set_transform_v_pp', 'pp'), ['TransformState const*']),
    ]
    c.ct['set_unexpected_change'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_set_unexpected_change_v_pI', 'pI'), ['unsigned int']),
    ]
    c.ct['stash_child'] = [
        ('d', 'B', 2, ('B', 'PandaNode_C_stash_child_B_ppp', 'ppp'), ['PandaNode*', 'Thread*']),
        ('d', 'B', 1, ('B', 'PandaNode_C_stash_child_B_pp', 'pp'), ['PandaNode*']),
        ('d', 'v', 2, ('v', 'PandaNode_C_stash_child_v_pip', 'pip'), ['int', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode_C_stash_child_v_pi', 'pi'), ['int']),
    ]
    c.ct['steal_children'] = [
        ('d', 'v', 2, ('v', 'PandaNode_C_steal_children_v_ppp', 'ppp'), ['PandaNode*', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode_C_steal_children_v_pp', 'pp'), ['PandaNode*']),
    ]
    c.ct['unstash_child'] = [
        ('d', 'B', 2, ('B', 'PandaNode_C_unstash_child_B_ppp', 'ppp'), ['PandaNode*', 'Thread*']),
        ('d', 'B', 1, ('B', 'PandaNode_C_unstash_child_B_pp', 'pp'), ['PandaNode*']),
        ('d', 'v', 2, ('v', 'PandaNode_C_unstash_child_v_pip', 'pip'), ['int', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode_C_unstash_child_v_pi', 'pi'), ['int']),
    ]
    c.ct['upcast_to_LinkedListNode'] = [
        ('d', 5, 0, ('p', 'PandaNode_C_upcast_to_LinkedListNode_p_p', 'p'), []),
    ]
    c.ct['upcast_to_Namable'] = [
        ('d', 12, 0, ('p', 'PandaNode_C_upcast_to_Namable_p_p', 'p'), []),
    ]
    c.ct['upcast_to_TypedWritableReferenceCount'] = [
        ('d', 18, 0, ('p', 'PandaNode_C_upcast_to_TypedWritableReferenceCount_p_p', 'p'), []),
    ]
    c.ct['update_bam_nested'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_update_bam_nested_v_pp', 'pp'), ['BamWriter*']),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'PandaNode_C_write_v_ppi', 'ppi'), ['std::ostream&', 'int']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'PandaNode_C_write_datagram_v_ppp', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]
    c.ct['write_recorder'] = [
        ('d', 'v', 2, ('v', 'PandaNode_C_write_recorder_v_ppp', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]
    c.ct['xform'] = [
        ('d', 'v', 1, ('v', 'PandaNode_C_xform_v_pp', 'pp'), ['LMatrix4 const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(PandaNode, attr, self)

PandaNode.c.link(PandaNode)



class LensNode(PandaNode):

    c = cxx.cstructs()
    c.register("LensNode", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 30, 2, ('p', 'LensNode_C_ctor_p_sp', 'sp'), ['std::string const&', 'Lens*']),
        ('s', 30, 1, ('p', 'LensNode_C_ctor_p_s', 's'), ['std::string const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LensNode_C_get_class_type_i_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LensNode_C_init_type_v_v', ''), []),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'LensNode_C_register_with_read_factory_v_v', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LensNode, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LensNode, 'init_type', None) )(*args,**kw)

    @classmethod
    def register_with_read_factory(cls, *args,**kw):
        return ( cls.c.get('register_with_read_factory', None) or cls.c.call(LensNode, 'register_with_read_factory', None) )(*args,**kw)

    # instance method type calls

    c.ct['activate_lens'] = [
        ('d', 'B', 1, ('B', 'LensNode_C_activate_lens_B_pi', 'pi'), ['int']),
    ]
    c.ct['copy_lens'] = [
        ('d', 'v', 1, ('v', 'LensNode_C_copy_lens_v_pp', 'pp'), ['Lens const&']),
        ('d', 'v', 2, ('v', 'LensNode_C_copy_lens_v_pip', 'pip'), ['int', 'Lens const&']),
    ]
    c.ct['deactivate_lens'] = [
        ('d', 'B', 1, ('B', 'LensNode_C_deactivate_lens_B_pi', 'pi'), ['int']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'LensNode_C_force_init_type_i_p', 'p'), []),
    ]
    c.ct['get_lens'] = [
        ('d', 'p', 1, ('p', 'LensNode_C_get_lens_p_pi', 'pi'), ['int']),
        ('d', 'p', 0, ('p', 'LensNode_C_get_lens_p_p', 'p'), []),
    ]
    c.ct['get_lens_active'] = [
        ('d', 'B', 1, ('B', 'LensNode_C_get_lens_active_B_pi', 'pi'), ['int']),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'LensNode_C_get_type_i_p', 'p'), []),
    ]
    c.ct['hide_frustum'] = [
        ('d', 'v', 0, ('v', 'LensNode_C_hide_frustum_v_p', 'p'), []),
    ]
    c.ct['is_in_view'] = [
        ('d', 'B', 1, ('B', 'LensNode_C_is_in_view_B_pp', 'pp'), ['LPoint3 const&']),
        ('d', 'B', 2, ('B', 'LensNode_C_is_in_view_B_pip', 'pip'), ['int', 'LPoint3 const&']),
    ]
    c.ct['set_lens'] = [
        ('d', 'v', 1, ('v', 'LensNode_C_set_lens_v_pp', 'pp'), ['Lens*']),
        ('d', 'v', 2, ('v', 'LensNode_C_set_lens_v_pip', 'pip'), ['int', 'Lens*']),
    ]
    c.ct['set_lens_active'] = [
        ('d', 'B', 2, ('B', 'LensNode_C_set_lens_active_B_piB', 'piB'), ['int', 'bool']),
    ]
    c.ct['show_frustum'] = [
        ('d', 'v', 0, ('v', 'LensNode_C_show_frustum_v_p', 'p'), []),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'LensNode_C_write_datagram_v_ppp', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]
    c.ct['xform'] = [
        ('d', 'v', 1, ('v', 'LensNode_C_xform_v_pp', 'pp'), ['LMatrix4 const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LensNode, attr, self)

LensNode.c.link(LensNode)



class Camera(LensNode):

    c = cxx.cstructs()
    c.register("Camera", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 31, 1, ('p', 'Camera_C_ctor_p_p', 'p'), ['Camera const&']),
        ('s', 31, 2, ('p', 'Camera_C_ctor_p_sp', 'sp'), ['std::string const&', 'Lens*']),
        ('s', 31, 1, ('p', 'Camera_C_ctor_p_s', 's'), ['std::string const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'Camera_C_get_class_type_i_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'Camera_C_init_type_v_v', ''), []),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'Camera_C_register_with_read_factory_v_v', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(Camera, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(Camera, 'init_type', None) )(*args,**kw)

    @classmethod
    def register_with_read_factory(cls, *args,**kw):
        return ( cls.c.get('register_with_read_factory', None) or cls.c.call(Camera, 'register_with_read_factory', None) )(*args,**kw)

    # instance method type calls

    c.ct['cleanup_aux_scene_data'] = [
        ('d', 'i', 1, ('i', 'Camera_C_cleanup_aux_scene_data_i_pp', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'Camera_C_cleanup_aux_scene_data_i_p', 'p'), []),
    ]
    c.ct['clear_aux_scene_data'] = [
        ('d', 'B', 1, ('B', 'Camera_C_clear_aux_scene_data_B_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['clear_tag_state'] = [
        ('d', 'v', 1, ('v', 'Camera_C_clear_tag_state_v_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['clear_tag_states'] = [
        ('d', 'v', 0, ('v', 'Camera_C_clear_tag_states_v_p', 'p'), []),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'Camera_C_force_init_type_i_p', 'p'), []),
    ]
    c.ct['get_aux_scene_data'] = [
        ('d', 'p', 1, ('p', 'Camera_C_get_aux_scene_data_p_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_camera_mask'] = [
        ('d', 'p', 0, ('p', 'Camera_C_get_camera_mask_p_p', 'p'), []),
    ]
    c.ct['get_cull_bounds'] = [
        ('d', 'p', 0, ('p', 'Camera_C_get_cull_bounds_p_p', 'p'), []),
    ]
    c.ct['get_cull_center'] = [
        ('d', 7, 0, ('p', 'Camera_C_get_cull_center_p_p', 'p'), []),
    ]
    c.ct['get_display_region'] = [
        ('d', 'p', 1, ('p', 'Camera_C_get_display_region_p_pp', 'pp'), ['std::size_t']),
    ]
    c.ct['get_initial_state'] = [
        ('d', 'p', 0, ('p', 'Camera_C_get_initial_state_p_p', 'p'), []),
    ]
    c.ct['get_lod_center'] = [
        ('d', 7, 0, ('p', 'Camera_C_get_lod_center_p_p', 'p'), []),
    ]
    c.ct['get_lod_scale'] = [
        ('d', 'f', 0, ('f', 'Camera_C_get_lod_scale_f_p', 'p'), []),
    ]
    c.ct['get_num_display_regions'] = [
        ('d', 'p', 0, ('p', 'Camera_C_get_num_display_regions_p_p', 'p'), []),
    ]
    c.ct['get_scene'] = [
        ('d', 7, 0, ('p', 'Camera_C_get_scene_p_p', 'p'), []),
    ]
    c.ct['get_tag_state'] = [
        ('d', 'p', 1, ('p', 'Camera_C_get_tag_state_p_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['get_tag_state_key'] = [
        ('d', 's', 0, ('s', 'Camera_C_get_tag_state_key_s_p', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'Camera_C_get_type_i_p', 'p'), []),
    ]
    c.ct['has_tag_state'] = [
        ('d', 'B', 1, ('B', 'Camera_C_has_tag_state_B_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['is_active'] = [
        ('d', 'B', 0, ('B', 'Camera_C_is_active_B_p', 'p'), []),
    ]
    c.ct['list_aux_scene_data'] = [
        ('d', 'v', 1, ('v', 'Camera_C_list_aux_scene_data_v_pp', 'pp'), ['std::ostream&']),
    ]
    c.ct['make_copy'] = [
        ('d', 29, 0, ('p', 'Camera_C_make_copy_p_p', 'p'), []),
    ]
    c.ct['safe_to_flatten'] = [
        ('d', 'B', 0, ('B', 'Camera_C_safe_to_flatten_B_p', 'p'), []),
    ]
    c.ct['safe_to_transform'] = [
        ('d', 'B', 0, ('B', 'Camera_C_safe_to_transform_B_p', 'p'), []),
    ]
    c.ct['set_active'] = [
        ('d', 'v', 1, ('v', 'Camera_C_set_active_v_pB', 'pB'), ['bool']),
    ]
    c.ct['set_aux_scene_data'] = [
        ('d', 'v', 2, ('v', 'Camera_C_set_aux_scene_data_v_ppp', 'ppp'), ['NodePath const&', 'AuxSceneData*']),
    ]
    c.ct['set_camera_mask'] = [
        ('d', 'v', 1, ('v', 'Camera_C_set_camera_mask_v_pp', 'pp'), ['DrawMask']),
    ]
    c.ct['set_cull_bounds'] = [
        ('d', 'v', 1, ('v', 'Camera_C_set_cull_bounds_v_pp', 'pp'), ['BoundingVolume*']),
    ]
    c.ct['set_cull_center'] = [
        ('d', 'v', 1, ('v', 'Camera_C_set_cull_center_v_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['set_initial_state'] = [
        ('d', 'v', 1, ('v', 'Camera_C_set_initial_state_v_pp', 'pp'), ['RenderState const*']),
    ]
    c.ct['set_lod_center'] = [
        ('d', 'v', 1, ('v', 'Camera_C_set_lod_center_v_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['set_lod_scale'] = [
        ('d', 'v', 1, ('v', 'Camera_C_set_lod_scale_v_pf', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_scene'] = [
        ('d', 'v', 1, ('v', 'Camera_C_set_scene_v_pp', 'pp'), ['NodePath const&']),
    ]
    c.ct['set_tag_state'] = [
        ('d', 'v', 2, ('v', 'Camera_C_set_tag_state_v_psp', 'psp'), ['std::string const&', 'RenderState const*']),
    ]
    c.ct['set_tag_state_key'] = [
        ('d', 'v', 1, ('v', 'Camera_C_set_tag_state_key_v_ps', 'ps'), ['std::string const&']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'Camera_C_write_datagram_v_ppp', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(Camera, attr, self)

Camera.c.link(Camera)



class GeomNode(PandaNode):

    c = cxx.cstructs()
    c.register("GeomNode", "upanda3d", """libupanda3d_cni.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 32, 1, ('p', 'GeomNode_C_ctor_p_s', 's'), ['std::string const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'GeomNode_C_get_class_type_i_v', ''), []),
    ]
    c.ct['get_default_collide_mask'] = [
        ('s', 'p', 0, ('p', 'GeomNode_C_get_default_collide_mask_p_v', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'GeomNode_C_init_type_v_v', ''), []),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'GeomNode_C_register_with_read_factory_v_v', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(GeomNode, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_default_collide_mask(cls, *args,**kw):
        return ( cls.c.get('get_default_collide_mask', None) or cls.c.call(GeomNode, 'get_default_collide_mask', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(GeomNode, 'init_type', None) )(*args,**kw)

    @classmethod
    def register_with_read_factory(cls, *args,**kw):
        return ( cls.c.get('register_with_read_factory', None) or cls.c.call(GeomNode, 'register_with_read_factory', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_for_draw'] = [
        ('d', 'v', 2, ('v', 'GeomNode_C_add_for_draw_v_ppp', 'ppp'), ['CullTraverser*', 'CullTraverserData&']),
    ]
    c.ct['add_geom'] = [
        ('d', 'v', 2, ('v', 'GeomNode_C_add_geom_v_ppp', 'ppp'), ['Geom*', 'RenderState const*']),
        ('d', 'v', 1, ('v', 'GeomNode_C_add_geom_v_pp', 'pp'), ['Geom*']),
    ]
    c.ct['add_geoms_from'] = [
        ('d', 'v', 1, ('v', 'GeomNode_C_add_geoms_from_v_pp', 'pp'), ['GeomNode const*']),
    ]
    c.ct['apply_attribs_to_vertices'] = [
        ('d', 'v', 3, ('v', 'GeomNode_C_apply_attribs_to_vertices_v_ppip', 'ppip'), ['AccumulatedAttribs const&', 'int', 'GeomTransformer&']),
    ]
    c.ct['check_valid'] = [
        ('d', 'B', 0, ('B', 'GeomNode_C_check_valid_B_p', 'p'), []),
    ]
    c.ct['decompose'] = [
        ('d', 'v', 0, ('v', 'GeomNode_C_decompose_v_p', 'p'), []),
    ]
    c.ct['do_premunge'] = [
        ('d', 'v', 3, ('v', 'GeomNode_C_do_premunge_v_pppp', 'pppp'), ['GraphicsStateGuardianBase*', 'RenderState const*', 'GeomTransformer&']),
    ]
    c.ct['finalize'] = [
        ('d', 'v', 1, ('v', 'GeomNode_C_finalize_v_pp', 'pp'), ['BamReader*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'GeomNode_C_force_init_type_i_p', 'p'), []),
    ]
    c.ct['get_geom'] = [
        ('d', 28, 1, ('p', 'GeomNode_C_get_geom_p_pi', 'pi'), ['int']),
    ]
    c.ct['get_geom_state'] = [
        ('d', 'p', 1, ('p', 'GeomNode_C_get_geom_state_p_pi', 'pi'), ['int']),
    ]
    c.ct['get_geoms'] = [
        ('d', 'p', 1, ('p', 'GeomNode_C_get_geoms_p_pp', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'GeomNode_C_get_geoms_p_p', 'p'), []),
    ]
    c.ct['get_num_geoms'] = [
        ('d', 'i', 0, ('i', 'GeomNode_C_get_num_geoms_i_p', 'p'), []),
    ]
    c.ct['get_preserved'] = [
        ('d', 'B', 0, ('B', 'GeomNode_C_get_preserved_B_p', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'GeomNode_C_get_type_i_p', 'p'), []),
    ]
    c.ct['is_renderable'] = [
        ('d', 'B', 0, ('B', 'GeomNode_C_is_renderable_B_p', 'p'), []),
    ]
    c.ct['modify_geom'] = [
        ('d', 28, 1, ('p', 'GeomNode_C_modify_geom_p_pi', 'pi'), ['int']),
    ]
    c.ct['r_prepare_scene'] = [
        ('d', 'v', 4, ('v', 'GeomNode_C_r_prepare_scene_v_ppppp', 'ppppp'), ['GraphicsStateGuardianBase*', 'RenderState const*', 'GeomTransformer&', 'Thread*']),
    ]
    c.ct['remove_all_geoms'] = [
        ('d', 'v', 0, ('v', 'GeomNode_C_remove_all_geoms_v_p', 'p'), []),
    ]
    c.ct['remove_geom'] = [
        ('d', 'v', 1, ('v', 'GeomNode_C_remove_geom_v_pi', 'pi'), ['int']),
    ]
    c.ct['safe_to_combine'] = [
        ('d', 'B', 0, ('B', 'GeomNode_C_safe_to_combine_B_p', 'p'), []),
    ]
    c.ct['safe_to_flatten'] = [
        ('d', 'B', 0, ('B', 'GeomNode_C_safe_to_flatten_B_p', 'p'), []),
    ]
    c.ct['set_geom'] = [
        ('d', 'v', 2, ('v', 'GeomNode_C_set_geom_v_pip', 'pip'), ['int', 'Geom*']),
    ]
    c.ct['set_geom_state'] = [
        ('d', 'v', 2, ('v', 'GeomNode_C_set_geom_state_v_pip', 'pip'), ['int', 'RenderState const*']),
    ]
    c.ct['set_preserved'] = [
        ('d', 'v', 1, ('v', 'GeomNode_C_set_preserved_v_pB', 'pB'), ['bool']),
    ]
    c.ct['unify'] = [
        ('d', 'v', 2, ('v', 'GeomNode_C_unify_v_piB', 'piB'), ['int', 'bool']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'GeomNode_C_write_datagram_v_ppp', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]
    c.ct['write_geoms'] = [
        ('d', 'v', 2, ('v', 'GeomNode_C_write_geoms_v_ppi', 'ppi'), ['std::ostream&', 'int']),
    ]
    c.ct['write_verbose'] = [
        ('d', 'v', 2, ('v', 'GeomNode_C_write_verbose_v_ppi', 'ppi'), ['std::ostream&', 'int']),
    ]
    c.ct['xform'] = [
        ('d', 'v', 1, ('v', 'GeomNode_C_xform_v_pp', 'pp'), ['LMatrix4 const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomNode, attr, self)

GeomNode.c.link(GeomNode)



if __name__ == '__main__':
    import os
    import gc
    import time
    import uctypes
    REFC = cxx.REFC

    def test():


        for proto in Engine.c.ct['ctor']:
            print("C++ class constructor", proto)

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

        E.attach(np)


        Vec3 = LVecBase3f


        v3 = Vec3(0.01, 42.01, 0.01)
        print("Vec3=", v3)


        np.set_pos( v3 )

        v3 = Vec3(2.0, 2.0, 2.0)
        print( v3, v3.get_x() , v3.get_y(), v3.get_z() )
        np.set_scale( v3 )


        # feed the monkey
        GeomTriangles.c.bases.append( GeomPrimitive )

        #Geom.UH_static = 3
        #GeomT.c.bases.append( GeomTriangles )
        #GeomT.c.bases.append( GeomPrimitive )


        def Cube(size=1.0, geom_name="CubeMaker", gvd_name="Data", gvw_name="vertex"):

            format = GeomVertexFormat.get_v3()
            print("GeomVertexFormat.format =",format)

            data = GeomVertexData(gvd_name, format, GeomEnums.UH_static )
            print("GeomVertexData=", data)


            cthr = Thread.get_current_thread()
            print('CurrentThread=', cthr )

            #cxx.TRACE=1
            # BUG
            #vertices = GeomVertexWriter(data,addr gvw_name)
            vertices = E.new_GeomVertexWriter( data, gvw_name);
            cxx.TRACE=0

            print("GeomVertexWriter=", vertices)

            size = float(size) / 2.0
            vertices.add_data3f(-size, -size, -size)
            vertices.add_data3f(+size, -size, -size)
            vertices.add_data3f(-size, +size, -size)
            vertices.add_data3f(+size, +size, -size)
            vertices.add_data3f(-size, -size, +size)
            vertices.add_data3f(+size, -size, +size)
            vertices.add_data3f(-size, +size, +size)
            vertices.add_data3f(+size, +size, +size)

            #triangles = GeomTriangles(GeomEnums.UH_static)
            triangles = E.new_GeomTriangles()

            print("triangles=",triangles)


            def add_quad(v0, v1, v2, v3):
                triangles.add_vertices(v0, v1, v2)
                triangles.add_vertices(v0, v2, v3)
                #
                #BUG
                #triangles.close_primitive()
                cxx.TRACE = 1
                E.close_primitive(triangles)
                cxx.TRACE = 0

            add_quad(4, 5, 7, 6)  # Z+
            add_quad(0, 2, 3, 1)  # Z-
            add_quad(3, 7, 5, 1)  # X+
            add_quad(4, 6, 2, 0)  # X-
            add_quad(2, 6, 7, 3)  # Y+
            add_quad(0, 1, 5, 4)  # Y+

            geom = Geom(data)
            print("Geom=",geom)

            cxx.TRACE = 1

# BUG geom ptr not converted
            E.add_primitive( geom, triangles )
            #geom.add_primitive(triangles)
            cxx.TRACE = 0

            print("geom=",geom)

            node = GeomNode(geom_name)
            node.add_geom(geom)
            return NodePath(node)


        cube = Cube(size=1.0)



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


