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
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("ConfigPage", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['get_default_page'] = [
        ('s', 0, 0, ('p', 'ConfigPage$1$get_default_page', ''), []),
    ]
    c.ct['get_local_page'] = [
        ('s', 0, 0, ('p', 'ConfigPage$2$get_local_page', ''), []),
    ]

    @classmethod
    def get_default_page(cls, *args,**kw):
        return ( cls.c.get('get_default_page', None) or cls.c.call(ConfigPage, 'get_default_page', None) )(*args,**kw)

    @classmethod
    def get_local_page(cls, *args,**kw):
        return ( cls.c.get('get_local_page', None) or cls.c.call(ConfigPage, 'get_local_page', None) )(*args,**kw)

    # instance method type calls

    c.ct['clear'] = [
        ('d', 'v', 0, ('v', 'ConfigPage$12$clear', 'p'), []),
    ]
    c.ct['delete_declaration'] = [
        ('d', 'B', 1, ('B', 'ConfigPage$17$delete_declaration', 'pp'), ['ConfigDeclaration*']),
    ]
    c.ct['get_declaration'] = [
        ('d', 'p', 1, ('p', 'ConfigPage$19$get_declaration', 'pp'), ['std::size_t']),
    ]
    c.ct['get_name'] = [
        ('d', 's', 0, ('s', 'ConfigPage$3$get_name', 'p'), []),
    ]
    c.ct['get_num_declarations'] = [
        ('d', 'p', 0, ('p', 'ConfigPage$18$get_num_declarations', 'p'), []),
    ]
    c.ct['get_page_seq'] = [
        ('d', 'i', 0, ('i', 'ConfigPage$8$get_page_seq', 'p'), []),
    ]
    c.ct['get_signature'] = [
        ('d', 's', 0, ('s', 'ConfigPage$11$get_signature', 'p'), []),
    ]
    c.ct['get_sort'] = [
        ('d', 'i', 0, ('i', 'ConfigPage$7$get_sort', 'p'), []),
    ]
    c.ct['get_string_value'] = [
        ('d', 's', 1, ('s', 'ConfigPage$22$get_string_value', 'pp'), ['std::size_t']),
    ]
    c.ct['get_trust_level'] = [
        ('d', 'i', 0, ('i', 'ConfigPage$9$get_trust_level', 'p'), []),
    ]
    c.ct['get_variable_name'] = [
        ('d', 's', 1, ('s', 'ConfigPage$21$get_variable_name', 'pp'), ['std::size_t']),
    ]
    c.ct['is_implicit'] = [
        ('d', 'B', 0, ('B', 'ConfigPage$5$is_implicit', 'p'), []),
    ]
    c.ct['is_special'] = [
        ('d', 'B', 0, ('B', 'ConfigPage$4$is_special', 'p'), []),
    ]
    c.ct['is_variable_used'] = [
        ('d', 'B', 1, ('B', 'ConfigPage$23$is_variable_used', 'pp'), ['std::size_t']),
    ]
    c.ct['make_declaration'] = [
        ('d', 'p', 2, ('p', 'ConfigPage$15$make_declaration', 'pps'), ['ConfigVariableCore*', 'std::string const&']),
        ('d', 'p', 2, ('p', 'ConfigPage$16$make_declaration', 'pss'), ['std::string const&', 'std::string const&']),
    ]
    c.ct['modify_declaration'] = [
        ('d', 'p', 1, ('p', 'ConfigPage$20$modify_declaration', 'pp'), ['std::size_t']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'ConfigPage$24$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['output_brief_signature'] = [
        ('d', 'v', 1, ('v', 'ConfigPage$25$output_brief_signature', 'pp'), ['std::ostream&']),
    ]
    c.ct['read_encrypted_prc'] = [
        ('d', 'B', 2, ('B', 'ConfigPage$14$read_encrypted_prc', 'pps'), ['std::istream&', 'std::string const&']),
    ]
    c.ct['read_prc'] = [
        ('d', 'B', 1, ('B', 'ConfigPage$13$read_prc', 'pp'), ['std::istream&']),
    ]
    c.ct['set_sort'] = [
        ('d', 'v', 1, ('v', 'ConfigPage$6$set_sort', 'pi'), ['int']),
    ]
    c.ct['set_trust_level'] = [
        ('d', 'v', 1, ('v', 'ConfigPage$10$set_trust_level', 'pi'), ['int']),
    ]
    c.ct['write'] = [
        ('d', 'v', 1, ('v', 'ConfigPage$26$write', 'pp'), ['std::ostream&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(ConfigPage, attr, self)

ConfigPage.c.link(ConfigPage)



class Engine(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("Engine", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 1, 0, ('p', 'Engine$1$Engine', ''), []),
        ('s', 1, 1, ('p', 'Engine$2$Engine', 'p'), ['Engine const&']),
    ]

    # classmethod type calls

    c.ct['dec_ref'] = [
        ('s', 'i', 1, ('i', 'Engine$16$dec_ref', 'p'), ['ReferenceCount*']),
    ]
    c.ct['get_version_string'] = [
        ('s', 's', 0, ('s', 'Engine$19$get_version_string', ''), []),
    ]
    c.ct['inc_ref'] = [
        ('s', 'i', 1, ('i', 'Engine$15$inc_ref', 'p'), ['ReferenceCount*']),
    ]
    c.ct['is_alive'] = [
        ('s', 'i', 0, ('i', 'Engine$5$is_alive', ''), []),
    ]
    c.ct['stop'] = [
        ('s', 'v', 0, ('v', 'Engine$4$stop', ''), []),
    ]

    @classmethod
    def dec_ref(cls, *args,**kw):
        return ( cls.c.get('dec_ref', None) or cls.c.call(Engine, 'dec_ref', None) )(*args,**kw)

    @classmethod
    def get_version_string(cls, *args,**kw):
        return ( cls.c.get('get_version_string', None) or cls.c.call(Engine, 'get_version_string', None) )(*args,**kw)

    @classmethod
    def inc_ref(cls, *args,**kw):
        return ( cls.c.get('inc_ref', None) or cls.c.call(Engine, 'inc_ref', None) )(*args,**kw)

    @classmethod
    def is_alive(cls, *args,**kw):
        return ( cls.c.get('is_alive', None) or cls.c.call(Engine, 'is_alive', None) )(*args,**kw)

    @classmethod
    def stop(cls, *args,**kw):
        return ( cls.c.get('stop', None) or cls.c.call(Engine, 'stop', None) )(*args,**kw)

    # instance method type calls

    c.ct['HelloEngine'] = [
        ('d', 'i', 0, ('i', 'Engine$6$HelloEngine', 'p'), []),
    ]
    c.ct['add_primitive'] = [
        ('d', 'v', 2, ('v', 'Engine$10$add_primitive', 'ppp'), ['Geom*', 'GeomTriangles*']),
    ]
    c.ct['attach'] = [
        ('d', 'v', 1, ('v', 'Engine$14$attach', 'pp'), ['NodePath*']),
    ]
    c.ct['build'] = [
        ('d', 'v', 0, ('v', 'Engine$17$build', 'p'), []),
    ]
    c.ct['casetest'] = [
        ('d', 'i', 3, ('i', 'Engine$7$casetest', 'pisB'), ['int', 'std::string', 'bool']),
    ]
    c.ct['close_primitive'] = [
        ('d', 'v', 1, ('v', 'Engine$11$close_primitive', 'pp'), ['GeomTriangles*']),
    ]
    c.ct['dtor'] = [
        ('d', 'v', 0, ('v', 'Engine$3$dtor', 'p'), []),
    ]
    c.ct['get_framework'] = [
        ('d', 9, 0, ('p', 'Engine$22$get_framework', 'p'), []),
    ]
    c.ct['get_wframe'] = [
        ('d', 20, 0, ('p', 'Engine$20$get_wframe', 'p'), []),
    ]
    c.ct['load_model'] = [
        ('d', 7, 1, ('p', 'Engine$8$load_model', 'ps'), ['char const*']),
    ]
    c.ct['new_Cube'] = [
        ('d', 7, 3, ('p', 'Engine$13$new_Cube', 'pfss'), ['float', 'char const*', 'char const*']),
    ]
    c.ct['new_GeomTriangles'] = [
        ('d', 26, 0, ('p', 'Engine$12$new_GeomTriangles', 'p'), []),
    ]
    c.ct['new_GeomVertexWriter'] = [
        ('d', 11, 2, ('p', 'Engine$9$new_GeomVertexWriter', 'pps'), ['GeomVertexData*', 'char const*']),
    ]
    c.ct['set_framework'] = [
        ('d', 'v', 1, ('v', 'Engine$23$set_framework', 'pp'), ['PandaFramework*']),
    ]
    c.ct['set_wframe'] = [
        ('d', 'v', 1, ('v', 'Engine$21$set_wframe', 'pp'), ['WindowFramework*']),
    ]
    c.ct['step'] = [
        ('d', 'v', 0, ('v', 'Engine$18$step', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(Engine, attr, self)

Engine.c.link(Engine)



class Filename(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("Filename", "upanda3d", """libupanda3d_c.so""")

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
        ('s', 2, 0, ('p', 'Filename$1$Filename', ''), []),
        ('s', 2, 1, ('p', 'Filename$2$Filename', 'p'), ['Filename&&']),
        ('s', 2, 1, ('p', 'Filename$3$Filename', 'p'), ['Filename const&']),
        ('s', 2, 2, ('p', 'Filename$4$Filename', 'pp'), ['Filename const&', 'Filename const&']),
        ('s', 2, 1, ('p', 'Filename$5$Filename', 's'), ['char const*']),
        ('s', 2, 1, ('p', 'Filename$6$Filename', 's'), ['std::string const&']),
        ('s', 2, 1, ('p', 'Filename$7$Filename', 'p'), ['std::wstring const&']),
    ]

    # classmethod type calls

    c.ct['binary_filename'] = [
        ('s', 2, 1, ('p', 'Filename$10$binary_filename', 'p'), ['Filename const&']),
        ('s', 2, 1, ('p', 'Filename$11$binary_filename', 's'), ['std::string const&']),
    ]
    c.ct['dso_filename'] = [
        ('s', 2, 1, ('p', 'Filename$12$dso_filename', 's'), ['std::string const&']),
    ]
    c.ct['executable_filename'] = [
        ('s', 2, 1, ('p', 'Filename$13$executable_filename', 's'), ['std::string const&']),
    ]
    c.ct['expand_from'] = [
        ('s', 2, 2, ('p', 'Filename$19$expand_from', 'sp'), ['std::string const&', 'Filename::Type']),
        ('s', 2, 1, ('p', 'Filename$20$expand_from', 's'), ['std::string const&']),
    ]
    c.ct['from_os_specific'] = [
        ('s', 2, 2, ('p', 'Filename$15$from_os_specific', 'sp'), ['std::string const&', 'Filename::Type']),
        ('s', 2, 1, ('p', 'Filename$16$from_os_specific', 's'), ['std::string const&']),
    ]
    c.ct['from_os_specific_w'] = [
        ('s', 2, 2, ('p', 'Filename$17$from_os_specific_w', 'pp'), ['std::wstring const&', 'Filename::Type']),
        ('s', 2, 1, ('p', 'Filename$18$from_os_specific_w', 'p'), ['std::wstring const&']),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'Filename$117$get_class_type', ''), []),
    ]
    c.ct['get_common_appdata_directory'] = [
        ('s', 2, 0, ('p', 'Filename$27$get_common_appdata_directory', ''), []),
    ]
    c.ct['get_filesystem_encoding'] = [
        ('s', 'p', 0, ('p', 'Filename$116$get_filesystem_encoding', ''), []),
    ]
    c.ct['get_home_directory'] = [
        ('s', 2, 0, ('p', 'Filename$24$get_home_directory', ''), []),
    ]
    c.ct['get_temp_directory'] = [
        ('s', 2, 0, ('p', 'Filename$25$get_temp_directory', ''), []),
    ]
    c.ct['get_user_appdata_directory'] = [
        ('s', 2, 0, ('p', 'Filename$26$get_user_appdata_directory', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'Filename$118$init_type', ''), []),
    ]
    c.ct['pattern_filename'] = [
        ('s', 2, 1, ('p', 'Filename$14$pattern_filename', 's'), ['std::string const&']),
    ]
    c.ct['set_filesystem_encoding'] = [
        ('s', 'v', 1, ('v', 'Filename$115$set_filesystem_encoding', 'p'), ['TextEncoder::Encoding']),
    ]
    c.ct['temporary'] = [
        ('s', 2, 4, ('p', 'Filename$21$temporary', 'sssp'), ['std::string const&', 'std::string const&', 'std::string const&', 'Filename::Type']),
        ('s', 2, 3, ('p', 'Filename$22$temporary', 'sss'), ['std::string const&', 'std::string const&', 'std::string const&']),
        ('s', 2, 2, ('p', 'Filename$23$temporary', 'ss'), ['std::string const&', 'std::string const&']),
    ]
    c.ct['text_filename'] = [
        ('s', 2, 1, ('p', 'Filename$8$text_filename', 'p'), ['Filename const&']),
        ('s', 2, 1, ('p', 'Filename$9$text_filename', 's'), ['std::string const&']),
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
        ('d', 'B', 0, ('B', 'Filename$112$__nonzero__', 'p'), []),
    ]
    c.ct['c_str'] = [
        ('d', 's', 0, ('s', 'Filename$28$c_str', 'p'), []),
    ]
    c.ct['chdir'] = [
        ('d', 'B', 0, ('B', 'Filename$103$chdir', 'p'), []),
    ]
    c.ct['compare_timestamps'] = [
        ('d', 'i', 3, ('i', 'Filename$77$compare_timestamps', 'ppBB'), ['Filename const&', 'bool', 'bool']),
        ('d', 'i', 2, ('i', 'Filename$78$compare_timestamps', 'ppB'), ['Filename const&', 'bool']),
        ('d', 'i', 1, ('i', 'Filename$79$compare_timestamps', 'pp'), ['Filename const&']),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'Filename$111$compare_to', 'pp'), ['Filename const&']),
    ]
    c.ct['copy_to'] = [
        ('d', 'B', 1, ('B', 'Filename$107$copy_to', 'pp'), ['Filename const&']),
    ]
    c.ct['empty'] = [
        ('d', 'B', 0, ('B', 'Filename$29$empty', 'p'), []),
    ]
    c.ct['exists'] = [
        ('d', 'B', 0, ('B', 'Filename$72$exists', 'p'), []),
    ]
    c.ct['extract_components'] = [
        ('d', 'v', 1, ('v', 'Filename$59$extract_components', 'pp'), ['vector_string&']),
    ]
    c.ct['find_on_searchpath'] = [
        ('d', 'i', 1, ('i', 'Filename$87$find_on_searchpath', 'pp'), ['DSearchPath const&']),
    ]
    c.ct['get_access_timestamp'] = [
        ('d', 'p', 0, ('p', 'Filename$81$get_access_timestamp', 'p'), []),
    ]
    c.ct['get_basename'] = [
        ('d', 's', 0, ('s', 'Filename$36$get_basename', 'p'), []),
    ]
    c.ct['get_basename_wo_extension'] = [
        ('d', 's', 0, ('s', 'Filename$38$get_basename_wo_extension', 'p'), []),
    ]
    c.ct['get_dirname'] = [
        ('d', 's', 0, ('s', 'Filename$35$get_dirname', 'p'), []),
    ]
    c.ct['get_extension'] = [
        ('d', 's', 0, ('s', 'Filename$39$get_extension', 'p'), []),
    ]
    c.ct['get_file_size'] = [
        ('d', 'p', 0, ('p', 'Filename$82$get_file_size', 'p'), []),
    ]
    c.ct['get_filename_index'] = [
        ('d', 2, 1, ('p', 'Filename$56$get_filename_index', 'pi'), ['int']),
    ]
    c.ct['get_fullpath'] = [
        ('d', 's', 0, ('s', 'Filename$33$get_fullpath', 'p'), []),
    ]
    c.ct['get_fullpath_w'] = [
        ('d', 'p', 0, ('p', 'Filename$34$get_fullpath_w', 'p'), []),
    ]
    c.ct['get_fullpath_wo_extension'] = [
        ('d', 's', 0, ('s', 'Filename$37$get_fullpath_wo_extension', 'p'), []),
    ]
    c.ct['get_hash'] = [
        ('d', 'i', 0, ('i', 'Filename$113$get_hash', 'p'), []),
    ]
    c.ct['get_hash_to_end'] = [
        ('d', 's', 0, ('s', 'Filename$57$get_hash_to_end', 'p'), []),
    ]
    c.ct['get_pattern'] = [
        ('d', 'B', 0, ('B', 'Filename$54$get_pattern', 'p'), []),
    ]
    c.ct['get_timestamp'] = [
        ('d', 'p', 0, ('p', 'Filename$80$get_timestamp', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'p', 0, ('p', 'Filename$52$get_type', 'p'), []),
    ]
    c.ct['has_hash'] = [
        ('d', 'B', 0, ('B', 'Filename$55$has_hash', 'p'), []),
    ]
    c.ct['is_binary'] = [
        ('d', 'B', 0, ('B', 'Filename$48$is_binary', 'p'), []),
    ]
    c.ct['is_binary_or_text'] = [
        ('d', 'B', 0, ('B', 'Filename$50$is_binary_or_text', 'p'), []),
    ]
    c.ct['is_directory'] = [
        ('d', 'B', 0, ('B', 'Filename$75$is_directory', 'p'), []),
    ]
    c.ct['is_executable'] = [
        ('d', 'B', 0, ('B', 'Filename$76$is_executable', 'p'), []),
    ]
    c.ct['is_fully_qualified'] = [
        ('d', 'B', 0, ('B', 'Filename$62$is_fully_qualified', 'p'), []),
    ]
    c.ct['is_local'] = [
        ('d', 'B', 0, ('B', 'Filename$61$is_local', 'p'), []),
    ]
    c.ct['is_regular_file'] = [
        ('d', 'B', 0, ('B', 'Filename$73$is_regular_file', 'p'), []),
    ]
    c.ct['is_text'] = [
        ('d', 'B', 0, ('B', 'Filename$49$is_text', 'p'), []),
    ]
    c.ct['is_writable'] = [
        ('d', 'B', 0, ('B', 'Filename$74$is_writable', 'p'), []),
    ]
    c.ct['length'] = [
        ('d', 'p', 0, ('p', 'Filename$30$length', 'p'), []),
    ]
    c.ct['make_absolute'] = [
        ('d', 'v', 0, ('v', 'Filename$63$make_absolute', 'p'), []),
        ('d', 'v', 1, ('v', 'Filename$64$make_absolute', 'pp'), ['Filename const&']),
    ]
    c.ct['make_canonical'] = [
        ('d', 'B', 0, ('B', 'Filename$65$make_canonical', 'p'), []),
    ]
    c.ct['make_dir'] = [
        ('d', 'B', 0, ('B', 'Filename$108$make_dir', 'p'), []),
    ]
    c.ct['make_relative_to'] = [
        ('d', 'B', 2, ('B', 'Filename$85$make_relative_to', 'ppB'), ['Filename', 'bool']),
        ('d', 'B', 1, ('B', 'Filename$86$make_relative_to', 'pp'), ['Filename']),
    ]
    c.ct['make_true_case'] = [
        ('d', 'B', 0, ('B', 'Filename$66$make_true_case', 'p'), []),
    ]
    c.ct['mkdir'] = [
        ('d', 'B', 0, ('B', 'Filename$109$mkdir', 'p'), []),
    ]
    c.ct['open_append'] = [
        ('d', 'B', 1, ('B', 'Filename$95$open_append', 'pp'), ['pofstream&']),
        ('d', 'B', 1, ('B', 'Filename$96$open_append', 'pp'), ['std::ofstream&']),
    ]
    c.ct['open_read'] = [
        ('d', 'B', 1, ('B', 'Filename$89$open_read', 'pp'), ['pifstream&']),
        ('d', 'B', 1, ('B', 'Filename$90$open_read', 'pp'), ['std::ifstream&']),
    ]
    c.ct['open_read_append'] = [
        ('d', 'B', 1, ('B', 'Filename$101$open_read_append', 'pp'), ['pfstream&']),
        ('d', 'B', 1, ('B', 'Filename$102$open_read_append', 'pp'), ['std::fstream&']),
    ]
    c.ct['open_read_write'] = [
        ('d', 'B', 2, ('B', 'Filename$97$open_read_write', 'ppB'), ['pfstream&', 'bool']),
        ('d', 'B', 1, ('B', 'Filename$98$open_read_write', 'pp'), ['pfstream&']),
        ('d', 'B', 2, ('B', 'Filename$99$open_read_write', 'ppB'), ['std::fstream&', 'bool']),
        ('d', 'B', 1, ('B', 'Filename$100$open_read_write', 'pp'), ['std::fstream&']),
    ]
    c.ct['open_write'] = [
        ('d', 'B', 2, ('B', 'Filename$91$open_write', 'ppB'), ['pofstream&', 'bool']),
        ('d', 'B', 1, ('B', 'Filename$92$open_write', 'pp'), ['pofstream&']),
        ('d', 'B', 2, ('B', 'Filename$93$open_write', 'ppB'), ['std::ofstream&', 'bool']),
        ('d', 'B', 1, ('B', 'Filename$94$open_write', 'pp'), ['std::ofstream&']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'Filename$114$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['rename_to'] = [
        ('d', 'B', 1, ('B', 'Filename$106$rename_to', 'pp'), ['Filename const&']),
    ]
    c.ct['resolve_filename'] = [
        ('d', 'B', 2, ('B', 'Filename$83$resolve_filename', 'pps'), ['DSearchPath const&', 'std::string const&']),
        ('d', 'B', 1, ('B', 'Filename$84$resolve_filename', 'pp'), ['DSearchPath const&']),
    ]
    c.ct['rmdir'] = [
        ('d', 'B', 0, ('B', 'Filename$110$rmdir', 'p'), []),
    ]
    c.ct['scan_directory'] = [
        ('d', 'B', 1, ('B', 'Filename$88$scan_directory', 'pp'), ['vector_string&']),
    ]
    c.ct['set_basename'] = [
        ('d', 'v', 1, ('v', 'Filename$42$set_basename', 'ps'), ['std::string const&']),
    ]
    c.ct['set_basename_wo_extension'] = [
        ('d', 'v', 1, ('v', 'Filename$44$set_basename_wo_extension', 'ps'), ['std::string const&']),
    ]
    c.ct['set_binary'] = [
        ('d', 'v', 0, ('v', 'Filename$46$set_binary', 'p'), []),
    ]
    c.ct['set_dirname'] = [
        ('d', 'v', 1, ('v', 'Filename$41$set_dirname', 'ps'), ['std::string const&']),
    ]
    c.ct['set_extension'] = [
        ('d', 'v', 1, ('v', 'Filename$45$set_extension', 'ps'), ['std::string const&']),
    ]
    c.ct['set_fullpath'] = [
        ('d', 'v', 1, ('v', 'Filename$40$set_fullpath', 'ps'), ['std::string const&']),
    ]
    c.ct['set_fullpath_wo_extension'] = [
        ('d', 'v', 1, ('v', 'Filename$43$set_fullpath_wo_extension', 'ps'), ['std::string const&']),
    ]
    c.ct['set_hash_to_end'] = [
        ('d', 'v', 1, ('v', 'Filename$58$set_hash_to_end', 'ps'), ['std::string const&']),
    ]
    c.ct['set_pattern'] = [
        ('d', 'v', 1, ('v', 'Filename$53$set_pattern', 'pB'), ['bool']),
    ]
    c.ct['set_text'] = [
        ('d', 'v', 0, ('v', 'Filename$47$set_text', 'p'), []),
    ]
    c.ct['set_type'] = [
        ('d', 'v', 1, ('v', 'Filename$51$set_type', 'pp'), ['Filename::Type']),
    ]
    c.ct['standardize'] = [
        ('d', 'v', 0, ('v', 'Filename$60$standardize', 'p'), []),
    ]
    c.ct['substr'] = [
        ('d', 's', 1, ('s', 'Filename$31$substr', 'pp'), ['std::size_t']),
        ('d', 's', 2, ('s', 'Filename$32$substr', 'ppp'), ['std::size_t', 'std::size_t']),
    ]
    c.ct['to_os_generic'] = [
        ('d', 's', 0, ('s', 'Filename$69$to_os_generic', 'p'), []),
    ]
    c.ct['to_os_long_name'] = [
        ('d', 's', 0, ('s', 'Filename$71$to_os_long_name', 'p'), []),
    ]
    c.ct['to_os_short_name'] = [
        ('d', 's', 0, ('s', 'Filename$70$to_os_short_name', 'p'), []),
    ]
    c.ct['to_os_specific'] = [
        ('d', 's', 0, ('s', 'Filename$67$to_os_specific', 'p'), []),
    ]
    c.ct['to_os_specific_w'] = [
        ('d', 'p', 0, ('p', 'Filename$68$to_os_specific_w', 'p'), []),
    ]
    c.ct['touch'] = [
        ('d', 'B', 0, ('B', 'Filename$104$touch', 'p'), []),
    ]
    c.ct['unlink'] = [
        ('d', 'B', 0, ('B', 'Filename$105$unlink', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(Filename, attr, self)

Filename.c.link(Filename)



class GeomEnums(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("GeomEnums", "upanda3d", """libupanda3d_c.so""")

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
        ('s', 3, 0, ('p', 'GeomEnums$1$GeomEnums', ''), []),
        ('s', 3, 1, ('p', 'GeomEnums$2$GeomEnums', 'p'), ['GeomEnums const&']),
    ]

    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_Geom'] = [
        ('d', 27, 0, ('p', 'GeomEnums$3$downcast_to_Geom', 'p'), []),
    ]
    c.ct['downcast_to_GeomPrimitive'] = [
        ('d', 25, 0, ('p', 'GeomEnums$4$downcast_to_GeomPrimitive', 'p'), []),
    ]
    c.ct['downcast_to_GeomVertexData'] = [
        ('d', 24, 0, ('p', 'GeomEnums$5$downcast_to_GeomVertexData', 'p'), []),
    ]
    c.ct['downcast_to_GeomVertexFormat'] = [
        ('d', 19, 0, ('p', 'GeomEnums$6$downcast_to_GeomVertexFormat', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomEnums, attr, self)

GeomEnums.c.link(GeomEnums)



class LVecBase3f(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("LVecBase3f", "upanda3d", """libupanda3d_c.so""")

    # enum 

    is_int = const(0)
    num_components = const(3)


    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 4, 0, ('p', 'LVecBase3f$1$LVecBase3f', ''), []),
        ('s', 4, 2, ('p', 'LVecBase3f$2$LVecBase3f', 'pf'), ['LVecBase2f const&', 'float']),
        ('s', 4, 1, ('p', 'LVecBase3f$3$LVecBase3f', 'p'), ['LVecBase3f const&']),
        ('s', 4, 1, ('p', 'LVecBase3f$4$LVecBase3f', 'p'), ['LVecBase3f::EVector3 const&']),
        ('s', 4, 1, ('p', 'LVecBase3f$5$LVecBase3f', 'f'), ['float']),
        ('s', 4, 3, ('p', 'LVecBase3f$6$LVecBase3f', 'fff'), ['float', 'float', 'float']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVecBase3f$64$get_class_type', ''), []),
    ]
    c.ct['get_num_components'] = [
        ('s', 'i', 0, ('i', 'LVecBase3f$29$get_num_components', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVecBase3f$65$init_type', ''), []),
    ]
    c.ct['size'] = [
        ('s', 'i', 0, ('i', 'LVecBase3f$11$size', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 4, 0, ('p', 'LVecBase3f$8$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 4, 0, ('p', 'LVecBase3f$9$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 4, 0, ('p', 'LVecBase3f$10$unit_z', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 4, 0, ('p', 'LVecBase3f$7$zero', ''), []),
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
        ('d', 'p', 1, ('p', 'LVecBase3f$48$add_hash', 'pp'), ['std::size_t']),
        ('d', 'p', 2, ('p', 'LVecBase3f$49$add_hash', 'ppf'), ['std::size_t', 'float']),
    ]
    c.ct['add_to_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase3f$24$add_to_cell', 'pif'), ['int', 'float']),
    ]
    c.ct['add_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f$25$add_x', 'pf'), ['float']),
    ]
    c.ct['add_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f$26$add_y', 'pf'), ['float']),
    ]
    c.ct['add_z'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f$27$add_z', 'pf'), ['float']),
    ]
    c.ct['almost_equal'] = [
        ('d', 'B', 1, ('B', 'LVecBase3f$56$almost_equal', 'pp'), ['LVecBase3f const&']),
        ('d', 'B', 2, ('B', 'LVecBase3f$57$almost_equal', 'ppf'), ['LVecBase3f const&', 'float']),
    ]
    c.ct['begin'] = [
        ('d', 'v', 0, ('v', 'LVecBase3f$30$begin', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase3f$31$begin', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'LVecBase3f$44$compare_to', 'pp'), ['LVecBase3f const&']),
        ('d', 'i', 2, ('i', 'LVecBase3f$45$compare_to', 'ppf'), ['LVecBase3f const&', 'float']),
    ]
    c.ct['componentwise_mult'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f$52$componentwise_mult', 'pp'), ['LVecBase3f const&']),
    ]
    c.ct['cross'] = [
        ('d', 4, 1, ('p', 'LVecBase3f$42$cross', 'pp'), ['LVecBase3f const&']),
    ]
    c.ct['cross_into'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f$55$cross_into', 'pp'), ['LVecBase3f const&']),
    ]
    c.ct['dot'] = [
        ('d', 'f', 1, ('f', 'LVecBase3f$36$dot', 'pp'), ['LVecBase3f const&']),
    ]
    c.ct['end'] = [
        ('d', 'v', 0, ('v', 'LVecBase3f$32$end', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase3f$33$end', 'p'), []),
    ]
    c.ct['fill'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f$34$fill', 'pf'), ['float']),
    ]
    c.ct['fmax'] = [
        ('d', 4, 1, ('p', 'LVecBase3f$53$fmax', 'pp'), ['LVecBase3f const&']),
    ]
    c.ct['fmin'] = [
        ('d', 4, 1, ('p', 'LVecBase3f$54$fmin', 'pp'), ['LVecBase3f const&']),
    ]
    c.ct['generate_hash'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f$50$generate_hash', 'pp'), ['ChecksumHashGenerator&']),
        ('d', 'v', 2, ('v', 'LVecBase3f$51$generate_hash', 'ppf'), ['ChecksumHashGenerator&', 'float']),
    ]
    c.ct['get_cell'] = [
        ('d', 'f', 1, ('f', 'LVecBase3f$13$get_cell', 'pi'), ['int']),
    ]
    c.ct['get_data'] = [
        ('d', 'v', 0, ('v', 'LVecBase3f$28$get_data', 'p'), []),
    ]
    c.ct['get_hash'] = [
        ('d', 'p', 0, ('p', 'LVecBase3f$46$get_hash', 'p'), []),
        ('d', 'p', 1, ('p', 'LVecBase3f$47$get_hash', 'pf'), ['float']),
    ]
    c.ct['get_standardized_hpr'] = [
        ('d', 4, 0, ('p', 'LVecBase3f$43$get_standardized_hpr', 'p'), []),
    ]
    c.ct['get_v'] = [
        ('d', 'p', 0, ('p', 'LVecBase3f$63$get_v', 'p'), []),
    ]
    c.ct['get_x'] = [
        ('d', 'f', 0, ('f', 'LVecBase3f$14$get_x', 'p'), []),
    ]
    c.ct['get_xy'] = [
        ('d', 'p', 0, ('p', 'LVecBase3f$21$get_xy', 'p'), []),
    ]
    c.ct['get_xz'] = [
        ('d', 'p', 0, ('p', 'LVecBase3f$22$get_xz', 'p'), []),
    ]
    c.ct['get_y'] = [
        ('d', 'f', 0, ('f', 'LVecBase3f$15$get_y', 'p'), []),
    ]
    c.ct['get_yz'] = [
        ('d', 'p', 0, ('p', 'LVecBase3f$23$get_yz', 'p'), []),
    ]
    c.ct['get_z'] = [
        ('d', 'f', 0, ('f', 'LVecBase3f$16$get_z', 'p'), []),
    ]
    c.ct['is_nan'] = [
        ('d', 'B', 0, ('B', 'LVecBase3f$12$is_nan', 'p'), []),
    ]
    c.ct['length'] = [
        ('d', 'f', 0, ('f', 'LVecBase3f$38$length', 'p'), []),
    ]
    c.ct['length_squared'] = [
        ('d', 'f', 0, ('f', 'LVecBase3f$37$length_squared', 'p'), []),
    ]
    c.ct['normalize'] = [
        ('d', 'B', 0, ('B', 'LVecBase3f$39$normalize', 'p'), []),
    ]
    c.ct['normalized'] = [
        ('d', 4, 0, ('p', 'LVecBase3f$40$normalized', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f$58$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['project'] = [
        ('d', 4, 1, ('p', 'LVecBase3f$41$project', 'pp'), ['LVecBase3f const&']),
    ]
    c.ct['read_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f$62$read_datagram', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['read_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f$60$read_datagram_fixed', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['set'] = [
        ('d', 'v', 3, ('v', 'LVecBase3f$35$set', 'pfff'), ['float', 'float', 'float']),
    ]
    c.ct['set_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase3f$17$set_cell', 'pif'), ['int', 'float']),
    ]
    c.ct['set_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f$18$set_x', 'pf'), ['float']),
    ]
    c.ct['set_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f$19$set_y', 'pf'), ['float']),
    ]
    c.ct['set_z'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f$20$set_z', 'pf'), ['float']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f$61$write_datagram', 'pp'), ['Datagram&']),
    ]
    c.ct['write_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f$59$write_datagram_fixed', 'pp'), ['Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVecBase3f, attr, self)

LVecBase3f.c.link(LVecBase3f)



class LinkedListNode(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("LinkedListNode", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_PandaNode'] = [
        ('d', 28, 0, ('p', 'LinkedListNode$1$downcast_to_PandaNode', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LinkedListNode, attr, self)

LinkedListNode.c.link(LinkedListNode)



class MemoryBase(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("MemoryBase", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 6, 0, ('p', 'MemoryBase$1$MemoryBase', ''), []),
        ('s', 6, 1, ('p', 'MemoryBase$2$MemoryBase', 'p'), ['MemoryBase const&']),
    ]

    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_ReferenceCount'] = [
        ('d', 13, 0, ('p', 'MemoryBase$3$downcast_to_ReferenceCount', 'p'), []),
    ]
    c.ct['downcast_to_TypedObject'] = [
        ('d', 14, 0, ('p', 'MemoryBase$4$downcast_to_TypedObject', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(MemoryBase, attr, self)

MemoryBase.c.link(MemoryBase)



class NodePath(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("NodePath", "upanda3d", """libupanda3d_c.so""")

    # enum ErrorType

    ET_fail = const(3)
    ET_not_found = const(1)
    ET_ok = const(0)
    ET_removed = const(2)


    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 7, 0, ('p', 'NodePath$1$NodePath', ''), []),
        ('s', 7, 1, ('p', 'NodePath$2$NodePath', 'p'), ['NodePath&&']),
        ('s', 7, 1, ('p', 'NodePath$3$NodePath', 'p'), ['NodePath const&']),
        ('s', 7, 3, ('p', 'NodePath$4$NodePath', 'ppp'), ['NodePath const&', 'PandaNode*', 'Thread*']),
        ('s', 7, 2, ('p', 'NodePath$5$NodePath', 'pp'), ['NodePath const&', 'PandaNode*']),
        ('s', 7, 2, ('p', 'NodePath$6$NodePath', 'pp'), ['PandaNode*', 'Thread*']),
        ('s', 7, 1, ('p', 'NodePath$7$NodePath', 'p'), ['PandaNode*']),
        ('s', 7, 2, ('p', 'NodePath$8$NodePath', 'sp'), ['std::string const&', 'Thread*']),
        ('s', 7, 1, ('p', 'NodePath$9$NodePath', 's'), ['std::string const&']),
    ]

    # classmethod type calls

    c.ct['any_path'] = [
        ('s', 7, 2, ('p', 'NodePath$10$any_path', 'pp'), ['PandaNode*', 'Thread*']),
        ('s', 7, 1, ('p', 'NodePath$11$any_path', 'p'), ['PandaNode*']),
    ]
    c.ct['decode_from_bam_stream'] = [
        ('s', 7, 2, ('p', 'NodePath$686$decode_from_bam_stream', 'pp'), ['vector_uchar', 'BamReader*']),
        ('s', 7, 1, ('p', 'NodePath$687$decode_from_bam_stream', 'p'), ['vector_uchar']),
    ]
    c.ct['fail'] = [
        ('s', 7, 0, ('p', 'NodePath$15$fail', ''), []),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'NodePath$690$get_class_type', ''), []),
    ]
    c.ct['get_max_search_depth'] = [
        ('s', 'i', 0, ('i', 'NodePath$17$get_max_search_depth', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'NodePath$691$init_type', ''), []),
    ]
    c.ct['not_found'] = [
        ('s', 7, 0, ('p', 'NodePath$13$not_found', ''), []),
    ]
    c.ct['removed'] = [
        ('s', 7, 0, ('p', 'NodePath$14$removed', ''), []),
    ]
    c.ct['set_max_search_depth'] = [
        ('s', 'v', 1, ('v', 'NodePath$16$set_max_search_depth', 'i'), ['int']),
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
        ('d', 'p', 1, ('p', 'NodePath$34$add_hash', 'pp'), ['std::size_t']),
    ]
    c.ct['adjust_all_priorities'] = [
        ('d', 'v', 1, ('v', 'NodePath$621$adjust_all_priorities', 'pi'), ['int']),
    ]
    c.ct['apply_texture_colors'] = [
        ('d', 'v', 0, ('v', 'NodePath$668$apply_texture_colors', 'p'), []),
    ]
    c.ct['attach_new_node'] = [
        ('d', 7, 3, ('p', 'NodePath$78$attach_new_node', 'ppip'), ['PandaNode*', 'int', 'Thread*']),
        ('d', 7, 2, ('p', 'NodePath$79$attach_new_node', 'ppi'), ['PandaNode*', 'int']),
        ('d', 7, 1, ('p', 'NodePath$80$attach_new_node', 'pp'), ['PandaNode*']),
        ('d', 7, 3, ('p', 'NodePath$81$attach_new_node', 'psip'), ['std::string const&', 'int', 'Thread*']),
        ('d', 7, 2, ('p', 'NodePath$82$attach_new_node', 'psi'), ['std::string const&', 'int']),
        ('d', 7, 1, ('p', 'NodePath$83$attach_new_node', 'ps'), ['std::string const&']),
    ]
    c.ct['calc_tight_bounds'] = [
        ('d', 'B', 4, ('B', 'NodePath$662$calc_tight_bounds', 'ppppp'), ['LPoint3&', 'LPoint3&', 'NodePath const&', 'Thread*']),
        ('d', 'B', 3, ('B', 'NodePath$663$calc_tight_bounds', 'pppp'), ['LPoint3&', 'LPoint3&', 'NodePath const&']),
        ('d', 'B', 2, ('B', 'NodePath$664$calc_tight_bounds', 'ppp'), ['LPoint3&', 'LPoint3&']),
    ]
    c.ct['clear'] = [
        ('d', 'v', 0, ('v', 'NodePath$12$clear', 'p'), []),
    ]
    c.ct['clear_antialias'] = [
        ('d', 'v', 0, ('v', 'NodePath$610$clear_antialias', 'p'), []),
    ]
    c.ct['clear_attrib'] = [
        ('d', 'v', 1, ('v', 'NodePath$109$clear_attrib', 'pi'), ['TypeHandle']),
    ]
    c.ct['clear_audio_volume'] = [
        ('d', 'v', 0, ('v', 'NodePath$614$clear_audio_volume', 'p'), []),
    ]
    c.ct['clear_billboard'] = [
        ('d', 'v', 0, ('v', 'NodePath$592$clear_billboard', 'p'), []),
    ]
    c.ct['clear_bin'] = [
        ('d', 'v', 0, ('v', 'NodePath$346$clear_bin', 'p'), []),
    ]
    c.ct['clear_clip_plane'] = [
        ('d', 'v', 0, ('v', 'NodePath$328$clear_clip_plane', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath$329$clear_clip_plane', 'pp'), ['NodePath const&']),
    ]
    c.ct['clear_color'] = [
        ('d', 'v', 0, ('v', 'NodePath$283$clear_color', 'p'), []),
    ]
    c.ct['clear_color_scale'] = [
        ('d', 'v', 0, ('v', 'NodePath$287$clear_color_scale', 'p'), []),
    ]
    c.ct['clear_compass'] = [
        ('d', 'v', 0, ('v', 'NodePath$596$clear_compass', 'p'), []),
    ]
    c.ct['clear_depth_offset'] = [
        ('d', 'v', 0, ('v', 'NodePath$575$clear_depth_offset', 'p'), []),
    ]
    c.ct['clear_depth_test'] = [
        ('d', 'v', 0, ('v', 'NodePath$565$clear_depth_test', 'p'), []),
    ]
    c.ct['clear_depth_write'] = [
        ('d', 'v', 0, ('v', 'NodePath$570$clear_depth_write', 'p'), []),
    ]
    c.ct['clear_effect'] = [
        ('d', 'v', 1, ('v', 'NodePath$113$clear_effect', 'pi'), ['TypeHandle']),
    ]
    c.ct['clear_effects'] = [
        ('d', 'v', 0, ('v', 'NodePath$116$clear_effects', 'p'), []),
    ]
    c.ct['clear_fog'] = [
        ('d', 'v', 0, ('v', 'NodePath$537$clear_fog', 'p'), []),
    ]
    c.ct['clear_light'] = [
        ('d', 'v', 0, ('v', 'NodePath$317$clear_light', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath$318$clear_light', 'pp'), ['NodePath const&']),
    ]
    c.ct['clear_logic_op'] = [
        ('d', 'v', 0, ('v', 'NodePath$605$clear_logic_op', 'p'), []),
    ]
    c.ct['clear_mat'] = [
        ('d', 'v', 0, ('v', 'NodePath$255$clear_mat', 'p'), []),
    ]
    c.ct['clear_material'] = [
        ('d', 'v', 0, ('v', 'NodePath$529$clear_material', 'p'), []),
    ]
    c.ct['clear_model_nodes'] = [
        ('d', 'i', 0, ('i', 'NodePath$669$clear_model_nodes', 'p'), []),
    ]
    c.ct['clear_occluder'] = [
        ('d', 'v', 0, ('v', 'NodePath$341$clear_occluder', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath$342$clear_occluder', 'pp'), ['NodePath const&']),
    ]
    c.ct['clear_project_texture'] = [
        ('d', 'v', 1, ('v', 'NodePath$506$clear_project_texture', 'pp'), ['TextureStage*']),
    ]
    c.ct['clear_render_mode'] = [
        ('d', 'v', 0, ('v', 'NodePath$553$clear_render_mode', 'p'), []),
    ]
    c.ct['clear_scissor'] = [
        ('d', 'v', 0, ('v', 'NodePath$338$clear_scissor', 'p'), []),
    ]
    c.ct['clear_shader'] = [
        ('d', 'v', 0, ('v', 'NodePath$381$clear_shader', 'p'), []),
    ]
    c.ct['clear_shader_input'] = [
        ('d', 'v', 1, ('v', 'NodePath$442$clear_shader_input', 'ps'), ['CPT_InternalName']),
    ]
    c.ct['clear_tag'] = [
        ('d', 'v', 1, ('v', 'NodePath$674$clear_tag', 'ps'), ['std::string const&']),
    ]
    c.ct['clear_tex_gen'] = [
        ('d', 'v', 0, ('v', 'NodePath$494$clear_tex_gen', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath$495$clear_tex_gen', 'pp'), ['TextureStage*']),
    ]
    c.ct['clear_tex_projector'] = [
        ('d', 'v', 0, ('v', 'NodePath$500$clear_tex_projector', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath$501$clear_tex_projector', 'pp'), ['TextureStage*']),
    ]
    c.ct['clear_tex_transform'] = [
        ('d', 'v', 0, ('v', 'NodePath$449$clear_tex_transform', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath$450$clear_tex_transform', 'pp'), ['TextureStage*']),
    ]
    c.ct['clear_texture'] = [
        ('d', 'v', 0, ('v', 'NodePath$362$clear_texture', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath$363$clear_texture', 'pp'), ['TextureStage*']),
    ]
    c.ct['clear_transform'] = [
        ('d', 'v', 2, ('v', 'NodePath$121$clear_transform', 'ppp'), ['NodePath const&', 'Thread*']),
        ('d', 'v', 1, ('v', 'NodePath$122$clear_transform', 'pp'), ['NodePath const&']),
        ('d', 'v', 1, ('v', 'NodePath$123$clear_transform', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'NodePath$124$clear_transform', 'p'), []),
    ]
    c.ct['clear_transparency'] = [
        ('d', 'v', 0, ('v', 'NodePath$600$clear_transparency', 'p'), []),
    ]
    c.ct['clear_two_sided'] = [
        ('d', 'v', 0, ('v', 'NodePath$560$clear_two_sided', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'NodePath$648$compare_to', 'pp'), ['NodePath const&']),
        ('d', 'i', 1, ('i', 'NodePath$649$compare_to', 'pp'), ['WeakNodePath const&']),
    ]
    c.ct['compose_color_scale'] = [
        ('d', 'v', 2, ('v', 'NodePath$292$compose_color_scale', 'ppi'), ['LVecBase4 const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$293$compose_color_scale', 'pp'), ['LVecBase4 const&']),
        ('d', 'v', 5, ('v', 'NodePath$294$compose_color_scale', 'pffffi'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'int']),
        ('d', 'v', 4, ('v', 'NodePath$295$compose_color_scale', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['copy_to'] = [
        ('d', 7, 3, ('p', 'NodePath$75$copy_to', 'ppip'), ['NodePath const&', 'int', 'Thread*']),
        ('d', 7, 2, ('p', 'NodePath$76$copy_to', 'ppi'), ['NodePath const&', 'int']),
        ('d', 7, 1, ('p', 'NodePath$77$copy_to', 'pp'), ['NodePath const&']),
    ]
    c.ct['count_num_descendants'] = [
        ('d', 'i', 0, ('i', 'NodePath$49$count_num_descendants', 'p'), []),
    ]
    c.ct['detach_node'] = [
        ('d', 'v', 1, ('v', 'NodePath$86$detach_node', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'NodePath$87$detach_node', 'p'), []),
    ]
    c.ct['do_billboard_axis'] = [
        ('d', 'v', 2, ('v', 'NodePath$578$do_billboard_axis', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
    ]
    c.ct['do_billboard_point_eye'] = [
        ('d', 'v', 2, ('v', 'NodePath$579$do_billboard_point_eye', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
    ]
    c.ct['do_billboard_point_world'] = [
        ('d', 'v', 2, ('v', 'NodePath$580$do_billboard_point_world', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
    ]
    c.ct['encode_to_bam_stream'] = [
        ('d', 'p', 0, ('p', 'NodePath$683$encode_to_bam_stream', 'p'), []),
        ('d', 'B', 2, ('B', 'NodePath$684$encode_to_bam_stream', 'ppp'), ['vector_uchar&', 'BamWriter*']),
        ('d', 'B', 1, ('B', 'NodePath$685$encode_to_bam_stream', 'pp'), ['vector_uchar&']),
    ]
    c.ct['fillin'] = [
        ('d', 'v', 2, ('v', 'NodePath$689$fillin', 'ppp'), ['DatagramIterator&', 'BamReader*']),
    ]
    c.ct['find'] = [
        ('d', 7, 1, ('p', 'NodePath$56$find', 'ps'), ['std::string const&']),
    ]
    c.ct['find_all_matches'] = [
        ('d', 8, 1, ('p', 'NodePath$58$find_all_matches', 'ps'), ['std::string const&']),
    ]
    c.ct['find_all_materials'] = [
        ('d', 'p', 0, ('p', 'NodePath$523$find_all_materials', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath$524$find_all_materials', 'ps'), ['std::string const&']),
    ]
    c.ct['find_all_paths_to'] = [
        ('d', 8, 1, ('p', 'NodePath$59$find_all_paths_to', 'pp'), ['PandaNode*']),
    ]
    c.ct['find_all_texcoords'] = [
        ('d', 'p', 0, ('p', 'NodePath$511$find_all_texcoords', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath$512$find_all_texcoords', 'ps'), ['std::string const&']),
    ]
    c.ct['find_all_texture_stages'] = [
        ('d', 'p', 0, ('p', 'NodePath$519$find_all_texture_stages', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath$520$find_all_texture_stages', 'ps'), ['std::string const&']),
    ]
    c.ct['find_all_textures'] = [
        ('d', 'p', 0, ('p', 'NodePath$515$find_all_textures', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath$516$find_all_textures', 'pp'), ['TextureStage*']),
        ('d', 'p', 1, ('p', 'NodePath$517$find_all_textures', 'ps'), ['std::string const&']),
    ]
    c.ct['find_all_vertex_columns'] = [
        ('d', 'p', 0, ('p', 'NodePath$509$find_all_vertex_columns', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath$510$find_all_vertex_columns', 'ps'), ['std::string const&']),
    ]
    c.ct['find_material'] = [
        ('d', 'p', 1, ('p', 'NodePath$522$find_material', 'ps'), ['std::string const&']),
    ]
    c.ct['find_net_tag'] = [
        ('d', 7, 1, ('p', 'NodePath$677$find_net_tag', 'ps'), ['std::string const&']),
    ]
    c.ct['find_path_to'] = [
        ('d', 7, 1, ('p', 'NodePath$57$find_path_to', 'pp'), ['PandaNode*']),
    ]
    c.ct['find_texture'] = [
        ('d', 'p', 1, ('p', 'NodePath$513$find_texture', 'pp'), ['TextureStage*']),
        ('d', 'p', 1, ('p', 'NodePath$514$find_texture', 'ps'), ['std::string const&']),
    ]
    c.ct['find_texture_stage'] = [
        ('d', 'p', 1, ('p', 'NodePath$518$find_texture_stage', 'ps'), ['std::string const&']),
    ]
    c.ct['flatten_light'] = [
        ('d', 'i', 0, ('i', 'NodePath$665$flatten_light', 'p'), []),
    ]
    c.ct['flatten_medium'] = [
        ('d', 'i', 0, ('i', 'NodePath$666$flatten_medium', 'p'), []),
    ]
    c.ct['flatten_strong'] = [
        ('d', 'i', 0, ('i', 'NodePath$667$flatten_strong', 'p'), []),
    ]
    c.ct['force_recompute_bounds'] = [
        ('d', 'v', 0, ('v', 'NodePath$660$force_recompute_bounds', 'p'), []),
    ]
    c.ct['get_ancestor'] = [
        ('d', 7, 2, ('p', 'NodePath$25$get_ancestor', 'pip'), ['int', 'Thread*']),
        ('d', 7, 1, ('p', 'NodePath$26$get_ancestor', 'pi'), ['int']),
    ]
    c.ct['get_antialias'] = [
        ('d', 'p', 0, ('p', 'NodePath$612$get_antialias', 'p'), []),
    ]
    c.ct['get_attrib'] = [
        ('d', 'p', 1, ('p', 'NodePath$107$get_attrib', 'pi'), ['TypeHandle']),
    ]
    c.ct['get_audio_volume'] = [
        ('d', 'f', 0, ('f', 'NodePath$619$get_audio_volume', 'p'), []),
    ]
    c.ct['get_bin_draw_order'] = [
        ('d', 'i', 0, ('i', 'NodePath$349$get_bin_draw_order', 'p'), []),
    ]
    c.ct['get_bin_name'] = [
        ('d', 's', 0, ('s', 'NodePath$348$get_bin_name', 'p'), []),
    ]
    c.ct['get_bounds'] = [
        ('d', 'p', 1, ('p', 'NodePath$658$get_bounds', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'NodePath$659$get_bounds', 'p'), []),
    ]
    c.ct['get_child'] = [
        ('d', 7, 2, ('p', 'NodePath$45$get_child', 'pip'), ['int', 'Thread*']),
        ('d', 7, 1, ('p', 'NodePath$46$get_child', 'pi'), ['int']),
    ]
    c.ct['get_children'] = [
        ('d', 8, 1, ('p', 'NodePath$41$get_children', 'pp'), ['Thread*']),
        ('d', 8, 0, ('p', 'NodePath$42$get_children', 'p'), []),
    ]
    c.ct['get_collide_mask'] = [
        ('d', 'p', 0, ('p', 'NodePath$644$get_collide_mask', 'p'), []),
    ]
    c.ct['get_color'] = [
        ('d', 'p', 0, ('p', 'NodePath$285$get_color', 'p'), []),
    ]
    c.ct['get_color_scale'] = [
        ('d', 'p', 0, ('p', 'NodePath$306$get_color_scale', 'p'), []),
    ]
    c.ct['get_common_ancestor'] = [
        ('d', 7, 2, ('p', 'NodePath$39$get_common_ancestor', 'ppp'), ['NodePath const&', 'Thread*']),
        ('d', 7, 1, ('p', 'NodePath$40$get_common_ancestor', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_depth_offset'] = [
        ('d', 'i', 0, ('i', 'NodePath$577$get_depth_offset', 'p'), []),
    ]
    c.ct['get_depth_test'] = [
        ('d', 'B', 0, ('B', 'NodePath$567$get_depth_test', 'p'), []),
    ]
    c.ct['get_depth_write'] = [
        ('d', 'B', 0, ('B', 'NodePath$572$get_depth_write', 'p'), []),
    ]
    c.ct['get_distance'] = [
        ('d', 'f', 1, ('f', 'NodePath$275$get_distance', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_effect'] = [
        ('d', 'p', 1, ('p', 'NodePath$111$get_effect', 'pi'), ['TypeHandle']),
    ]
    c.ct['get_effects'] = [
        ('d', 'p', 0, ('p', 'NodePath$115$get_effects', 'p'), []),
    ]
    c.ct['get_error_type'] = [
        ('d', 'p', 0, ('p', 'NodePath$27$get_error_type', 'p'), []),
    ]
    c.ct['get_fog'] = [
        ('d', 'p', 0, ('p', 'NodePath$540$get_fog', 'p'), []),
    ]
    c.ct['get_h'] = [
        ('d', 'f', 0, ('f', 'NodePath$183$get_h', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath$184$get_h', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_hidden_ancestor'] = [
        ('d', 7, 2, ('p', 'NodePath$630$get_hidden_ancestor', 'ppp'), ['DrawMask', 'Thread*']),
        ('d', 7, 1, ('p', 'NodePath$631$get_hidden_ancestor', 'pp'), ['DrawMask']),
        ('d', 7, 0, ('p', 'NodePath$632$get_hidden_ancestor', 'p'), []),
    ]
    c.ct['get_hpr'] = [
        ('d', 'p', 0, ('p', 'NodePath$181$get_hpr', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath$182$get_hpr', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_instance_count'] = [
        ('d', 'i', 0, ('i', 'NodePath$446$get_instance_count', 'p'), []),
    ]
    c.ct['get_key'] = [
        ('d', 'i', 0, ('i', 'NodePath$33$get_key', 'p'), []),
    ]
    c.ct['get_logic_op'] = [
        ('d', 'p', 0, ('p', 'NodePath$607$get_logic_op', 'p'), []),
    ]
    c.ct['get_mat'] = [
        ('d', 'p', 0, ('p', 'NodePath$257$get_mat', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath$258$get_mat', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_material'] = [
        ('d', 'p', 0, ('p', 'NodePath$531$get_material', 'p'), []),
    ]
    c.ct['get_name'] = [
        ('d', 's', 0, ('s', 'NodePath$680$get_name', 'p'), []),
    ]
    c.ct['get_net_audio_volume'] = [
        ('d', 'f', 0, ('f', 'NodePath$620$get_net_audio_volume', 'p'), []),
    ]
    c.ct['get_net_prev_transform'] = [
        ('d', 'p', 1, ('p', 'NodePath$139$get_net_prev_transform', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'NodePath$140$get_net_prev_transform', 'p'), []),
    ]
    c.ct['get_net_state'] = [
        ('d', 'p', 1, ('p', 'NodePath$103$get_net_state', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'NodePath$104$get_net_state', 'p'), []),
    ]
    c.ct['get_net_tag'] = [
        ('d', 's', 1, ('s', 'NodePath$675$get_net_tag', 'ps'), ['std::string const&']),
    ]
    c.ct['get_net_transform'] = [
        ('d', 'p', 1, ('p', 'NodePath$129$get_net_transform', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'NodePath$130$get_net_transform', 'p'), []),
    ]
    c.ct['get_node'] = [
        ('d', 28, 2, ('p', 'NodePath$23$get_node', 'pip'), ['int', 'Thread*']),
        ('d', 28, 1, ('p', 'NodePath$24$get_node', 'pi'), ['int']),
    ]
    c.ct['get_num_children'] = [
        ('d', 'i', 1, ('i', 'NodePath$43$get_num_children', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'NodePath$44$get_num_children', 'p'), []),
    ]
    c.ct['get_num_nodes'] = [
        ('d', 'i', 1, ('i', 'NodePath$21$get_num_nodes', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'NodePath$22$get_num_nodes', 'p'), []),
    ]
    c.ct['get_p'] = [
        ('d', 'f', 0, ('f', 'NodePath$185$get_p', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath$186$get_p', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_parent'] = [
        ('d', 7, 1, ('p', 'NodePath$52$get_parent', 'pp'), ['Thread*']),
        ('d', 7, 0, ('p', 'NodePath$53$get_parent', 'p'), []),
    ]
    c.ct['get_pos'] = [
        ('d', 'p', 0, ('p', 'NodePath$161$get_pos', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath$162$get_pos', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_pos_delta'] = [
        ('d', 'p', 0, ('p', 'NodePath$169$get_pos_delta', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath$170$get_pos_delta', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_prev_transform'] = [
        ('d', 'p', 2, ('p', 'NodePath$131$get_prev_transform', 'ppp'), ['NodePath const&', 'Thread*']),
        ('d', 'p', 1, ('p', 'NodePath$132$get_prev_transform', 'pp'), ['NodePath const&']),
        ('d', 'p', 1, ('p', 'NodePath$133$get_prev_transform', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'NodePath$134$get_prev_transform', 'p'), []),
    ]
    c.ct['get_quat'] = [
        ('d', 'p', 0, ('p', 'NodePath$191$get_quat', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath$192$get_quat', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_r'] = [
        ('d', 'f', 0, ('f', 'NodePath$187$get_r', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath$188$get_r', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_relative_point'] = [
        ('d', 'p', 2, ('p', 'NodePath$273$get_relative_point', 'ppp'), ['NodePath const&', 'LVecBase3 const&']),
    ]
    c.ct['get_relative_vector'] = [
        ('d', 'p', 2, ('p', 'NodePath$274$get_relative_vector', 'ppp'), ['NodePath const&', 'LVecBase3 const&']),
    ]
    c.ct['get_render_mode'] = [
        ('d', 'p', 0, ('p', 'NodePath$555$get_render_mode', 'p'), []),
    ]
    c.ct['get_render_mode_perspective'] = [
        ('d', 'B', 0, ('B', 'NodePath$557$get_render_mode_perspective', 'p'), []),
    ]
    c.ct['get_render_mode_thickness'] = [
        ('d', 'f', 0, ('f', 'NodePath$556$get_render_mode_thickness', 'p'), []),
    ]
    c.ct['get_sa'] = [
        ('d', 'f', 0, ('f', 'NodePath$310$get_sa', 'p'), []),
    ]
    c.ct['get_sb'] = [
        ('d', 'f', 0, ('f', 'NodePath$309$get_sb', 'p'), []),
    ]
    c.ct['get_scale'] = [
        ('d', 'p', 0, ('p', 'NodePath$205$get_scale', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath$206$get_scale', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_sg'] = [
        ('d', 'f', 0, ('f', 'NodePath$308$get_sg', 'p'), []),
    ]
    c.ct['get_shader'] = [
        ('d', 'p', 0, ('p', 'NodePath$444$get_shader', 'p'), []),
    ]
    c.ct['get_shader_input'] = [
        ('d', 'p', 1, ('p', 'NodePath$445$get_shader_input', 'ps'), ['CPT_InternalName']),
    ]
    c.ct['get_shear'] = [
        ('d', 'p', 0, ('p', 'NodePath$223$get_shear', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath$224$get_shear', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_shxy'] = [
        ('d', 'f', 0, ('f', 'NodePath$225$get_shxy', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath$226$get_shxy', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_shxz'] = [
        ('d', 'f', 0, ('f', 'NodePath$227$get_shxz', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath$228$get_shxz', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_shyz'] = [
        ('d', 'f', 0, ('f', 'NodePath$229$get_shyz', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath$230$get_shyz', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_sort'] = [
        ('d', 'i', 1, ('i', 'NodePath$54$get_sort', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'NodePath$55$get_sort', 'p'), []),
    ]
    c.ct['get_sr'] = [
        ('d', 'f', 0, ('f', 'NodePath$307$get_sr', 'p'), []),
    ]
    c.ct['get_stashed_ancestor'] = [
        ('d', 7, 1, ('p', 'NodePath$642$get_stashed_ancestor', 'pp'), ['Thread*']),
        ('d', 7, 0, ('p', 'NodePath$643$get_stashed_ancestor', 'p'), []),
    ]
    c.ct['get_stashed_children'] = [
        ('d', 8, 1, ('p', 'NodePath$47$get_stashed_children', 'pp'), ['Thread*']),
        ('d', 8, 0, ('p', 'NodePath$48$get_stashed_children', 'p'), []),
    ]
    c.ct['get_state'] = [
        ('d', 'p', 2, ('p', 'NodePath$95$get_state', 'ppp'), ['NodePath const&', 'Thread*']),
        ('d', 'p', 1, ('p', 'NodePath$96$get_state', 'pp'), ['NodePath const&']),
        ('d', 'p', 1, ('p', 'NodePath$97$get_state', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'NodePath$98$get_state', 'p'), []),
    ]
    c.ct['get_sx'] = [
        ('d', 'f', 0, ('f', 'NodePath$207$get_sx', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath$208$get_sx', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_sy'] = [
        ('d', 'f', 0, ('f', 'NodePath$209$get_sy', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath$210$get_sy', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_sz'] = [
        ('d', 'f', 0, ('f', 'NodePath$211$get_sz', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath$212$get_sz', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_tag'] = [
        ('d', 's', 1, ('s', 'NodePath$671$get_tag', 'ps'), ['std::string const&']),
    ]
    c.ct['get_tag_keys'] = [
        ('d', 'v', 1, ('v', 'NodePath$672$get_tag_keys', 'pp'), ['vector_string&']),
    ]
    c.ct['get_tex_gen'] = [
        ('d', 'p', 1, ('p', 'NodePath$497$get_tex_gen', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_hpr'] = [
        ('d', 'p', 2, ('p', 'NodePath$486$get_tex_hpr', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 'p', 1, ('p', 'NodePath$487$get_tex_hpr', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_offset'] = [
        ('d', 'p', 2, ('p', 'NodePath$470$get_tex_offset', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 'p', 1, ('p', 'NodePath$471$get_tex_offset', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_pos'] = [
        ('d', 'p', 2, ('p', 'NodePath$484$get_tex_pos', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 'p', 1, ('p', 'NodePath$485$get_tex_pos', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_projector_from'] = [
        ('d', 7, 1, ('p', 'NodePath$503$get_tex_projector_from', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_projector_to'] = [
        ('d', 7, 1, ('p', 'NodePath$504$get_tex_projector_to', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_rotate'] = [
        ('d', 'f', 2, ('f', 'NodePath$472$get_tex_rotate', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 'f', 1, ('f', 'NodePath$473$get_tex_rotate', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_scale'] = [
        ('d', 'p', 2, ('p', 'NodePath$474$get_tex_scale', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 'p', 1, ('p', 'NodePath$475$get_tex_scale', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_scale_3d'] = [
        ('d', 'p', 2, ('p', 'NodePath$488$get_tex_scale_3d', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 'p', 1, ('p', 'NodePath$489$get_tex_scale_3d', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_transform'] = [
        ('d', 'p', 2, ('p', 'NodePath$452$get_tex_transform', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 'p', 1, ('p', 'NodePath$453$get_tex_transform', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_texture'] = [
        ('d', 'p', 0, ('p', 'NodePath$368$get_texture', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath$369$get_texture', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_texture_sampler'] = [
        ('d', 'p', 0, ('p', 'NodePath$371$get_texture_sampler', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath$372$get_texture_sampler', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_top'] = [
        ('d', 7, 1, ('p', 'NodePath$30$get_top', 'pp'), ['Thread*']),
        ('d', 7, 0, ('p', 'NodePath$31$get_top', 'p'), []),
    ]
    c.ct['get_top_node'] = [
        ('d', 28, 1, ('p', 'NodePath$28$get_top_node', 'pp'), ['Thread*']),
        ('d', 28, 0, ('p', 'NodePath$29$get_top_node', 'p'), []),
    ]
    c.ct['get_transform'] = [
        ('d', 'p', 2, ('p', 'NodePath$117$get_transform', 'ppp'), ['NodePath const&', 'Thread*']),
        ('d', 'p', 1, ('p', 'NodePath$118$get_transform', 'pp'), ['NodePath const&']),
        ('d', 'p', 1, ('p', 'NodePath$119$get_transform', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'NodePath$120$get_transform', 'p'), []),
    ]
    c.ct['get_transparency'] = [
        ('d', 'p', 0, ('p', 'NodePath$602$get_transparency', 'p'), []),
    ]
    c.ct['get_two_sided'] = [
        ('d', 'B', 0, ('B', 'NodePath$562$get_two_sided', 'p'), []),
    ]
    c.ct['get_x'] = [
        ('d', 'f', 0, ('f', 'NodePath$163$get_x', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath$164$get_x', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_y'] = [
        ('d', 'f', 0, ('f', 'NodePath$165$get_y', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath$166$get_y', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_z'] = [
        ('d', 'f', 0, ('f', 'NodePath$167$get_z', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath$168$get_z', 'pp'), ['NodePath const&']),
    ]
    c.ct['has_antialias'] = [
        ('d', 'B', 0, ('B', 'NodePath$611$has_antialias', 'p'), []),
    ]
    c.ct['has_attrib'] = [
        ('d', 'B', 1, ('B', 'NodePath$108$has_attrib', 'pi'), ['TypeHandle']),
    ]
    c.ct['has_audio_volume'] = [
        ('d', 'B', 0, ('B', 'NodePath$613$has_audio_volume', 'p'), []),
    ]
    c.ct['has_billboard'] = [
        ('d', 'B', 0, ('B', 'NodePath$593$has_billboard', 'p'), []),
    ]
    c.ct['has_bin'] = [
        ('d', 'B', 0, ('B', 'NodePath$347$has_bin', 'p'), []),
    ]
    c.ct['has_clip_plane'] = [
        ('d', 'B', 1, ('B', 'NodePath$330$has_clip_plane', 'pp'), ['NodePath const&']),
    ]
    c.ct['has_clip_plane_off'] = [
        ('d', 'B', 0, ('B', 'NodePath$331$has_clip_plane_off', 'p'), []),
        ('d', 'B', 1, ('B', 'NodePath$332$has_clip_plane_off', 'pp'), ['NodePath const&']),
    ]
    c.ct['has_color'] = [
        ('d', 'B', 0, ('B', 'NodePath$284$has_color', 'p'), []),
    ]
    c.ct['has_color_scale'] = [
        ('d', 'B', 0, ('B', 'NodePath$286$has_color_scale', 'p'), []),
    ]
    c.ct['has_compass'] = [
        ('d', 'B', 0, ('B', 'NodePath$597$has_compass', 'p'), []),
    ]
    c.ct['has_depth_offset'] = [
        ('d', 'B', 0, ('B', 'NodePath$576$has_depth_offset', 'p'), []),
    ]
    c.ct['has_depth_test'] = [
        ('d', 'B', 0, ('B', 'NodePath$566$has_depth_test', 'p'), []),
    ]
    c.ct['has_depth_write'] = [
        ('d', 'B', 0, ('B', 'NodePath$571$has_depth_write', 'p'), []),
    ]
    c.ct['has_effect'] = [
        ('d', 'B', 1, ('B', 'NodePath$112$has_effect', 'pi'), ['TypeHandle']),
    ]
    c.ct['has_fog'] = [
        ('d', 'B', 0, ('B', 'NodePath$538$has_fog', 'p'), []),
    ]
    c.ct['has_fog_off'] = [
        ('d', 'B', 0, ('B', 'NodePath$539$has_fog_off', 'p'), []),
    ]
    c.ct['has_light'] = [
        ('d', 'B', 1, ('B', 'NodePath$319$has_light', 'pp'), ['NodePath const&']),
    ]
    c.ct['has_light_off'] = [
        ('d', 'B', 0, ('B', 'NodePath$320$has_light_off', 'p'), []),
        ('d', 'B', 1, ('B', 'NodePath$321$has_light_off', 'pp'), ['NodePath const&']),
    ]
    c.ct['has_logic_op'] = [
        ('d', 'B', 0, ('B', 'NodePath$606$has_logic_op', 'p'), []),
    ]
    c.ct['has_mat'] = [
        ('d', 'B', 0, ('B', 'NodePath$256$has_mat', 'p'), []),
    ]
    c.ct['has_material'] = [
        ('d', 'B', 0, ('B', 'NodePath$530$has_material', 'p'), []),
    ]
    c.ct['has_net_tag'] = [
        ('d', 'B', 1, ('B', 'NodePath$676$has_net_tag', 'ps'), ['std::string const&']),
    ]
    c.ct['has_occluder'] = [
        ('d', 'B', 1, ('B', 'NodePath$343$has_occluder', 'pp'), ['NodePath const&']),
    ]
    c.ct['has_parent'] = [
        ('d', 'B', 1, ('B', 'NodePath$50$has_parent', 'pp'), ['Thread*']),
        ('d', 'B', 0, ('B', 'NodePath$51$has_parent', 'p'), []),
    ]
    c.ct['has_render_mode'] = [
        ('d', 'B', 0, ('B', 'NodePath$554$has_render_mode', 'p'), []),
    ]
    c.ct['has_scissor'] = [
        ('d', 'B', 0, ('B', 'NodePath$339$has_scissor', 'p'), []),
    ]
    c.ct['has_tag'] = [
        ('d', 'B', 1, ('B', 'NodePath$673$has_tag', 'ps'), ['std::string const&']),
    ]
    c.ct['has_tex_gen'] = [
        ('d', 'B', 1, ('B', 'NodePath$496$has_tex_gen', 'pp'), ['TextureStage*']),
    ]
    c.ct['has_tex_projector'] = [
        ('d', 'B', 1, ('B', 'NodePath$502$has_tex_projector', 'pp'), ['TextureStage*']),
    ]
    c.ct['has_tex_transform'] = [
        ('d', 'B', 1, ('B', 'NodePath$451$has_tex_transform', 'pp'), ['TextureStage*']),
    ]
    c.ct['has_texcoord'] = [
        ('d', 'B', 1, ('B', 'NodePath$507$has_texcoord', 'ps'), ['std::string const&']),
    ]
    c.ct['has_texture'] = [
        ('d', 'B', 0, ('B', 'NodePath$364$has_texture', 'p'), []),
        ('d', 'B', 1, ('B', 'NodePath$365$has_texture', 'pp'), ['TextureStage*']),
    ]
    c.ct['has_texture_off'] = [
        ('d', 'B', 0, ('B', 'NodePath$366$has_texture_off', 'p'), []),
        ('d', 'B', 1, ('B', 'NodePath$367$has_texture_off', 'pp'), ['TextureStage*']),
    ]
    c.ct['has_transparency'] = [
        ('d', 'B', 0, ('B', 'NodePath$601$has_transparency', 'p'), []),
    ]
    c.ct['has_two_sided'] = [
        ('d', 'B', 0, ('B', 'NodePath$561$has_two_sided', 'p'), []),
    ]
    c.ct['has_vertex_column'] = [
        ('d', 'B', 1, ('B', 'NodePath$508$has_vertex_column', 'ps'), ['InternalName const*']),
    ]
    c.ct['heads_up'] = [
        ('d', 'v', 2, ('v', 'NodePath$266$heads_up', 'ppp'), ['LPoint3 const&', 'LVector3 const&']),
        ('d', 'v', 1, ('v', 'NodePath$267$heads_up', 'pp'), ['LPoint3 const&']),
        ('d', 'v', 3, ('v', 'NodePath$268$heads_up', 'pppp'), ['NodePath const&', 'LPoint3 const&', 'LVector3 const&']),
        ('d', 'v', 2, ('v', 'NodePath$269$heads_up', 'ppp'), ['NodePath const&', 'LPoint3 const&']),
        ('d', 'v', 1, ('v', 'NodePath$270$heads_up', 'pp'), ['NodePath const&']),
        ('d', 'v', 4, ('v', 'NodePath$271$heads_up', 'ppfff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath$272$heads_up', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['hide'] = [
        ('d', 'v', 0, ('v', 'NodePath$626$hide', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath$627$hide', 'pp'), ['DrawMask']),
    ]
    c.ct['hide_bounds'] = [
        ('d', 'v', 0, ('v', 'NodePath$657$hide_bounds', 'p'), []),
    ]
    c.ct['instance_to'] = [
        ('d', 7, 3, ('p', 'NodePath$69$instance_to', 'ppip'), ['NodePath const&', 'int', 'Thread*']),
        ('d', 7, 2, ('p', 'NodePath$70$instance_to', 'ppi'), ['NodePath const&', 'int']),
        ('d', 7, 1, ('p', 'NodePath$71$instance_to', 'pp'), ['NodePath const&']),
    ]
    c.ct['instance_under_node'] = [
        ('d', 7, 4, ('p', 'NodePath$72$instance_under_node', 'ppsip'), ['NodePath const&', 'std::string const&', 'int', 'Thread*']),
        ('d', 7, 3, ('p', 'NodePath$73$instance_under_node', 'ppsi'), ['NodePath const&', 'std::string const&', 'int']),
        ('d', 7, 2, ('p', 'NodePath$74$instance_under_node', 'pps'), ['NodePath const&', 'std::string const&']),
    ]
    c.ct['is_ancestor_of'] = [
        ('d', 'B', 2, ('B', 'NodePath$37$is_ancestor_of', 'ppp'), ['NodePath const&', 'Thread*']),
        ('d', 'B', 1, ('B', 'NodePath$38$is_ancestor_of', 'pp'), ['NodePath const&']),
    ]
    c.ct['is_empty'] = [
        ('d', 'B', 0, ('B', 'NodePath$18$is_empty', 'p'), []),
    ]
    c.ct['is_hidden'] = [
        ('d', 'B', 1, ('B', 'NodePath$628$is_hidden', 'pp'), ['DrawMask']),
        ('d', 'B', 0, ('B', 'NodePath$629$is_hidden', 'p'), []),
    ]
    c.ct['is_same_graph'] = [
        ('d', 'B', 2, ('B', 'NodePath$35$is_same_graph', 'ppp'), ['NodePath const&', 'Thread*']),
        ('d', 'B', 1, ('B', 'NodePath$36$is_same_graph', 'pp'), ['NodePath const&']),
    ]
    c.ct['is_singleton'] = [
        ('d', 'B', 1, ('B', 'NodePath$19$is_singleton', 'pp'), ['Thread*']),
        ('d', 'B', 0, ('B', 'NodePath$20$is_singleton', 'p'), []),
    ]
    c.ct['is_stashed'] = [
        ('d', 'B', 0, ('B', 'NodePath$641$is_stashed', 'p'), []),
    ]
    c.ct['list_tags'] = [
        ('d', 'v', 0, ('v', 'NodePath$678$list_tags', 'p'), []),
    ]
    c.ct['look_at'] = [
        ('d', 'v', 2, ('v', 'NodePath$259$look_at', 'ppp'), ['LPoint3 const&', 'LVector3 const&']),
        ('d', 'v', 1, ('v', 'NodePath$260$look_at', 'pp'), ['LPoint3 const&']),
        ('d', 'v', 3, ('v', 'NodePath$261$look_at', 'pppp'), ['NodePath const&', 'LPoint3 const&', 'LVector3 const&']),
        ('d', 'v', 2, ('v', 'NodePath$262$look_at', 'ppp'), ['NodePath const&', 'LPoint3 const&']),
        ('d', 'v', 1, ('v', 'NodePath$263$look_at', 'pp'), ['NodePath const&']),
        ('d', 'v', 4, ('v', 'NodePath$264$look_at', 'ppfff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath$265$look_at', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['ls'] = [
        ('d', 'v', 0, ('v', 'NodePath$89$ls', 'p'), []),
        ('d', 'v', 2, ('v', 'NodePath$90$ls', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$91$ls', 'pp'), ['std::ostream&']),
    ]
    c.ct['node'] = [
        ('d', 28, 0, ('p', 'NodePath$32$node', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'NodePath$88$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['premunge_scene'] = [
        ('d', 'v', 1, ('v', 'NodePath$652$premunge_scene', 'pp'), ['GraphicsStateGuardianBase*']),
        ('d', 'v', 0, ('v', 'NodePath$653$premunge_scene', 'p'), []),
    ]
    c.ct['prepare_scene'] = [
        ('d', 'v', 1, ('v', 'NodePath$654$prepare_scene', 'pp'), ['GraphicsStateGuardianBase*']),
    ]
    c.ct['project_texture'] = [
        ('d', 'v', 3, ('v', 'NodePath$505$project_texture', 'pppp'), ['TextureStage*', 'Texture*', 'NodePath const&']),
    ]
    c.ct['remove_node'] = [
        ('d', 'v', 1, ('v', 'NodePath$84$remove_node', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'NodePath$85$remove_node', 'p'), []),
    ]
    c.ct['reparent_to'] = [
        ('d', 'v', 3, ('v', 'NodePath$60$reparent_to', 'ppip'), ['NodePath const&', 'int', 'Thread*']),
        ('d', 'v', 2, ('v', 'NodePath$61$reparent_to', 'ppi'), ['NodePath const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$62$reparent_to', 'pp'), ['NodePath const&']),
    ]
    c.ct['replace_material'] = [
        ('d', 'v', 2, ('v', 'NodePath$532$replace_material', 'ppp'), ['Material*', 'Material*']),
    ]
    c.ct['replace_texture'] = [
        ('d', 'v', 2, ('v', 'NodePath$370$replace_texture', 'ppp'), ['Texture*', 'Texture*']),
    ]
    c.ct['reverse_ls'] = [
        ('d', 'v', 0, ('v', 'NodePath$92$reverse_ls', 'p'), []),
        ('d', 'i', 2, ('i', 'NodePath$93$reverse_ls', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'i', 1, ('i', 'NodePath$94$reverse_ls', 'pp'), ['std::ostream&']),
    ]
    c.ct['set_all_color_scale'] = [
        ('d', 'v', 2, ('v', 'NodePath$300$set_all_color_scale', 'pfi'), ['PN_stdfloat', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$301$set_all_color_scale', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_alpha_scale'] = [
        ('d', 'v', 2, ('v', 'NodePath$298$set_alpha_scale', 'pfi'), ['PN_stdfloat', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$299$set_alpha_scale', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_antialias'] = [
        ('d', 'v', 2, ('v', 'NodePath$608$set_antialias', 'ppi'), ['unsigned short int', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$609$set_antialias', 'pp'), ['unsigned short int']),
    ]
    c.ct['set_attrib'] = [
        ('d', 'v', 2, ('v', 'NodePath$105$set_attrib', 'ppi'), ['RenderAttrib const*', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$106$set_attrib', 'pp'), ['RenderAttrib const*']),
    ]
    c.ct['set_audio_volume'] = [
        ('d', 'v', 2, ('v', 'NodePath$615$set_audio_volume', 'pfi'), ['PN_stdfloat', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$616$set_audio_volume', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_audio_volume_off'] = [
        ('d', 'v', 1, ('v', 'NodePath$617$set_audio_volume_off', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath$618$set_audio_volume_off', 'p'), []),
    ]
    c.ct['set_billboard_axis'] = [
        ('d', 'v', 2, ('v', 'NodePath$581$set_billboard_axis', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath$582$set_billboard_axis', 'pf'), ['PN_stdfloat']),
        ('d', 'v', 0, ('v', 'NodePath$583$set_billboard_axis', 'p'), []),
    ]
    c.ct['set_billboard_point_eye'] = [
        ('d', 'v', 3, ('v', 'NodePath$584$set_billboard_point_eye', 'ppfB'), ['NodePath const&', 'PN_stdfloat', 'bool']),
        ('d', 'v', 2, ('v', 'NodePath$585$set_billboard_point_eye', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 2, ('v', 'NodePath$586$set_billboard_point_eye', 'pfB'), ['PN_stdfloat', 'bool']),
        ('d', 'v', 1, ('v', 'NodePath$587$set_billboard_point_eye', 'pf'), ['PN_stdfloat']),
        ('d', 'v', 0, ('v', 'NodePath$588$set_billboard_point_eye', 'p'), []),
    ]
    c.ct['set_billboard_point_world'] = [
        ('d', 'v', 2, ('v', 'NodePath$589$set_billboard_point_world', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath$590$set_billboard_point_world', 'pf'), ['PN_stdfloat']),
        ('d', 'v', 0, ('v', 'NodePath$591$set_billboard_point_world', 'p'), []),
    ]
    c.ct['set_bin'] = [
        ('d', 'v', 3, ('v', 'NodePath$344$set_bin', 'psii'), ['std::string const&', 'int', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$345$set_bin', 'psi'), ['std::string const&', 'int']),
    ]
    c.ct['set_clip_plane'] = [
        ('d', 'v', 2, ('v', 'NodePath$322$set_clip_plane', 'ppi'), ['NodePath const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$323$set_clip_plane', 'pp'), ['NodePath const&']),
    ]
    c.ct['set_clip_plane_off'] = [
        ('d', 'v', 2, ('v', 'NodePath$324$set_clip_plane_off', 'ppi'), ['NodePath const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$325$set_clip_plane_off', 'pp'), ['NodePath const&']),
        ('d', 'v', 1, ('v', 'NodePath$326$set_clip_plane_off', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath$327$set_clip_plane_off', 'p'), []),
    ]
    c.ct['set_collide_mask'] = [
        ('d', 'v', 3, ('v', 'NodePath$645$set_collide_mask', 'pppi'), ['CollideMask', 'CollideMask', 'TypeHandle']),
        ('d', 'v', 2, ('v', 'NodePath$646$set_collide_mask', 'ppp'), ['CollideMask', 'CollideMask']),
        ('d', 'v', 1, ('v', 'NodePath$647$set_collide_mask', 'pp'), ['CollideMask']),
    ]
    c.ct['set_color'] = [
        ('d', 'v', 2, ('v', 'NodePath$276$set_color', 'ppi'), ['LColor const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$277$set_color', 'pp'), ['LColor const&']),
        ('d', 'v', 5, ('v', 'NodePath$278$set_color', 'pffffi'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'int']),
        ('d', 'v', 4, ('v', 'NodePath$279$set_color', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath$280$set_color', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_color_off'] = [
        ('d', 'v', 1, ('v', 'NodePath$281$set_color_off', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath$282$set_color_off', 'p'), []),
    ]
    c.ct['set_color_scale'] = [
        ('d', 'v', 2, ('v', 'NodePath$288$set_color_scale', 'ppi'), ['LVecBase4 const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$289$set_color_scale', 'pp'), ['LVecBase4 const&']),
        ('d', 'v', 5, ('v', 'NodePath$290$set_color_scale', 'pffffi'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'int']),
        ('d', 'v', 4, ('v', 'NodePath$291$set_color_scale', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_color_scale_off'] = [
        ('d', 'v', 1, ('v', 'NodePath$296$set_color_scale_off', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath$297$set_color_scale_off', 'p'), []),
    ]
    c.ct['set_compass'] = [
        ('d', 'v', 1, ('v', 'NodePath$594$set_compass', 'pp'), ['NodePath const&']),
        ('d', 'v', 0, ('v', 'NodePath$595$set_compass', 'p'), []),
    ]
    c.ct['set_depth_offset'] = [
        ('d', 'v', 2, ('v', 'NodePath$573$set_depth_offset', 'pii'), ['int', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$574$set_depth_offset', 'pi'), ['int']),
    ]
    c.ct['set_depth_test'] = [
        ('d', 'v', 2, ('v', 'NodePath$563$set_depth_test', 'pBi'), ['bool', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$564$set_depth_test', 'pB'), ['bool']),
    ]
    c.ct['set_depth_write'] = [
        ('d', 'v', 2, ('v', 'NodePath$568$set_depth_write', 'pBi'), ['bool', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$569$set_depth_write', 'pB'), ['bool']),
    ]
    c.ct['set_effect'] = [
        ('d', 'v', 1, ('v', 'NodePath$110$set_effect', 'pp'), ['RenderEffect const*']),
    ]
    c.ct['set_effects'] = [
        ('d', 'v', 1, ('v', 'NodePath$114$set_effects', 'pp'), ['RenderEffects const*']),
    ]
    c.ct['set_fluid_pos'] = [
        ('d', 'v', 1, ('v', 'NodePath$151$set_fluid_pos', 'pp'), ['LVecBase3 const&']),
        ('d', 'v', 2, ('v', 'NodePath$152$set_fluid_pos', 'ppp'), ['NodePath const&', 'LVecBase3 const&']),
        ('d', 'v', 4, ('v', 'NodePath$153$set_fluid_pos', 'ppfff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath$154$set_fluid_pos', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_fluid_x'] = [
        ('d', 'v', 2, ('v', 'NodePath$155$set_fluid_x', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath$156$set_fluid_x', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_fluid_y'] = [
        ('d', 'v', 2, ('v', 'NodePath$157$set_fluid_y', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath$158$set_fluid_y', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_fluid_z'] = [
        ('d', 'v', 2, ('v', 'NodePath$159$set_fluid_z', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath$160$set_fluid_z', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_fog'] = [
        ('d', 'v', 2, ('v', 'NodePath$533$set_fog', 'ppi'), ['Fog*', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$534$set_fog', 'pp'), ['Fog*']),
    ]
    c.ct['set_fog_off'] = [
        ('d', 'v', 1, ('v', 'NodePath$535$set_fog_off', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath$536$set_fog_off', 'p'), []),
    ]
    c.ct['set_h'] = [
        ('d', 'v', 2, ('v', 'NodePath$175$set_h', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath$176$set_h', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_hpr'] = [
        ('d', 'v', 1, ('v', 'NodePath$171$set_hpr', 'pp'), ['LVecBase3 const&']),
        ('d', 'v', 2, ('v', 'NodePath$172$set_hpr', 'ppp'), ['NodePath const&', 'LVecBase3 const&']),
        ('d', 'v', 4, ('v', 'NodePath$173$set_hpr', 'ppfff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath$174$set_hpr', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_hpr_scale'] = [
        ('d', 'v', 2, ('v', 'NodePath$237$set_hpr_scale', 'ppp'), ['LVecBase3 const&', 'LVecBase3 const&']),
        ('d', 'v', 3, ('v', 'NodePath$238$set_hpr_scale', 'pppp'), ['NodePath const&', 'LVecBase3 const&', 'LVecBase3 const&']),
        ('d', 'v', 7, ('v', 'NodePath$239$set_hpr_scale', 'ppffffff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 6, ('v', 'NodePath$240$set_hpr_scale', 'pffffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_instance_count'] = [
        ('d', 'v', 1, ('v', 'NodePath$443$set_instance_count', 'pi'), ['int']),
    ]
    c.ct['set_light'] = [
        ('d', 'v', 2, ('v', 'NodePath$311$set_light', 'ppi'), ['NodePath const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$312$set_light', 'pp'), ['NodePath const&']),
    ]
    c.ct['set_light_off'] = [
        ('d', 'v', 2, ('v', 'NodePath$313$set_light_off', 'ppi'), ['NodePath const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$314$set_light_off', 'pp'), ['NodePath const&']),
        ('d', 'v', 1, ('v', 'NodePath$315$set_light_off', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath$316$set_light_off', 'p'), []),
    ]
    c.ct['set_logic_op'] = [
        ('d', 'v', 2, ('v', 'NodePath$603$set_logic_op', 'ppi'), ['LogicOpAttrib::Operation', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$604$set_logic_op', 'pp'), ['LogicOpAttrib::Operation']),
    ]
    c.ct['set_mat'] = [
        ('d', 'v', 1, ('v', 'NodePath$253$set_mat', 'pp'), ['LMatrix4 const&']),
        ('d', 'v', 2, ('v', 'NodePath$254$set_mat', 'ppp'), ['NodePath const&', 'LMatrix4 const&']),
    ]
    c.ct['set_material'] = [
        ('d', 'v', 2, ('v', 'NodePath$525$set_material', 'ppi'), ['Material*', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$526$set_material', 'pp'), ['Material*']),
    ]
    c.ct['set_material_off'] = [
        ('d', 'v', 1, ('v', 'NodePath$527$set_material_off', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath$528$set_material_off', 'p'), []),
    ]
    c.ct['set_name'] = [
        ('d', 'v', 1, ('v', 'NodePath$679$set_name', 'ps'), ['std::string const&']),
    ]
    c.ct['set_occluder'] = [
        ('d', 'v', 1, ('v', 'NodePath$340$set_occluder', 'pp'), ['NodePath const&']),
    ]
    c.ct['set_p'] = [
        ('d', 'v', 2, ('v', 'NodePath$177$set_p', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath$178$set_p', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_pos'] = [
        ('d', 'v', 1, ('v', 'NodePath$141$set_pos', 'pp'), ['LVecBase3 const&']),
        ('d', 'v', 2, ('v', 'NodePath$142$set_pos', 'ppp'), ['NodePath const&', 'LVecBase3 const&']),
        ('d', 'v', 4, ('v', 'NodePath$143$set_pos', 'ppfff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath$144$set_pos', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_pos_hpr'] = [
        ('d', 'v', 2, ('v', 'NodePath$231$set_pos_hpr', 'ppp'), ['LVecBase3 const&', 'LVecBase3 const&']),
        ('d', 'v', 3, ('v', 'NodePath$232$set_pos_hpr', 'pppp'), ['NodePath const&', 'LVecBase3 const&', 'LVecBase3 const&']),
        ('d', 'v', 7, ('v', 'NodePath$233$set_pos_hpr', 'ppffffff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 6, ('v', 'NodePath$234$set_pos_hpr', 'pffffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_pos_hpr_scale'] = [
        ('d', 'v', 3, ('v', 'NodePath$243$set_pos_hpr_scale', 'pppp'), ['LVecBase3 const&', 'LVecBase3 const&', 'LVecBase3 const&']),
        ('d', 'v', 4, ('v', 'NodePath$244$set_pos_hpr_scale', 'ppppp'), ['NodePath const&', 'LVecBase3 const&', 'LVecBase3 const&', 'LVecBase3 const&']),
        ('d', 'v', 10, ('v', 'NodePath$245$set_pos_hpr_scale', 'ppfffffffff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 9, ('v', 'NodePath$246$set_pos_hpr_scale', 'pfffffffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_pos_hpr_scale_shear'] = [
        ('d', 'v', 4, ('v', 'NodePath$249$set_pos_hpr_scale_shear', 'ppppp'), ['LVecBase3 const&', 'LVecBase3 const&', 'LVecBase3 const&', 'LVecBase3 const&']),
        ('d', 'v', 5, ('v', 'NodePath$250$set_pos_hpr_scale_shear', 'pppppp'), ['NodePath const&', 'LVecBase3 const&', 'LVecBase3 const&', 'LVecBase3 const&', 'LVecBase3 const&']),
    ]
    c.ct['set_pos_quat'] = [
        ('d', 'v', 2, ('v', 'NodePath$235$set_pos_quat', 'ppp'), ['LVecBase3 const&', 'LQuaternion const&']),
        ('d', 'v', 3, ('v', 'NodePath$236$set_pos_quat', 'pppp'), ['NodePath const&', 'LVecBase3 const&', 'LQuaternion const&']),
    ]
    c.ct['set_pos_quat_scale'] = [
        ('d', 'v', 3, ('v', 'NodePath$247$set_pos_quat_scale', 'pppp'), ['LVecBase3 const&', 'LQuaternion const&', 'LVecBase3 const&']),
        ('d', 'v', 4, ('v', 'NodePath$248$set_pos_quat_scale', 'ppppp'), ['NodePath const&', 'LVecBase3 const&', 'LQuaternion const&', 'LVecBase3 const&']),
    ]
    c.ct['set_pos_quat_scale_shear'] = [
        ('d', 'v', 4, ('v', 'NodePath$251$set_pos_quat_scale_shear', 'ppppp'), ['LVecBase3 const&', 'LQuaternion const&', 'LVecBase3 const&', 'LVecBase3 const&']),
        ('d', 'v', 5, ('v', 'NodePath$252$set_pos_quat_scale_shear', 'pppppp'), ['NodePath const&', 'LVecBase3 const&', 'LQuaternion const&', 'LVecBase3 const&', 'LVecBase3 const&']),
    ]
    c.ct['set_prev_transform'] = [
        ('d', 'v', 3, ('v', 'NodePath$135$set_prev_transform', 'pppp'), ['NodePath const&', 'TransformState const*', 'Thread*']),
        ('d', 'v', 2, ('v', 'NodePath$136$set_prev_transform', 'ppp'), ['NodePath const&', 'TransformState const*']),
        ('d', 'v', 2, ('v', 'NodePath$137$set_prev_transform', 'ppp'), ['TransformState const*', 'Thread*']),
        ('d', 'v', 1, ('v', 'NodePath$138$set_prev_transform', 'pp'), ['TransformState const*']),
    ]
    c.ct['set_quat'] = [
        ('d', 'v', 1, ('v', 'NodePath$189$set_quat', 'pp'), ['LQuaternion const&']),
        ('d', 'v', 2, ('v', 'NodePath$190$set_quat', 'ppp'), ['NodePath const&', 'LQuaternion const&']),
    ]
    c.ct['set_quat_scale'] = [
        ('d', 'v', 2, ('v', 'NodePath$241$set_quat_scale', 'ppp'), ['LQuaternion const&', 'LVecBase3 const&']),
        ('d', 'v', 3, ('v', 'NodePath$242$set_quat_scale', 'pppp'), ['NodePath const&', 'LQuaternion const&', 'LVecBase3 const&']),
    ]
    c.ct['set_r'] = [
        ('d', 'v', 2, ('v', 'NodePath$179$set_r', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath$180$set_r', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_render_mode'] = [
        ('d', 'v', 3, ('v', 'NodePath$551$set_render_mode', 'ppfi'), ['RenderModeAttrib::Mode', 'PN_stdfloat', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$552$set_render_mode', 'ppf'), ['RenderModeAttrib::Mode', 'PN_stdfloat']),
    ]
    c.ct['set_render_mode_filled'] = [
        ('d', 'v', 1, ('v', 'NodePath$543$set_render_mode_filled', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath$544$set_render_mode_filled', 'p'), []),
    ]
    c.ct['set_render_mode_filled_wireframe'] = [
        ('d', 'v', 2, ('v', 'NodePath$545$set_render_mode_filled_wireframe', 'ppi'), ['LColor const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$546$set_render_mode_filled_wireframe', 'pp'), ['LColor const&']),
    ]
    c.ct['set_render_mode_perspective'] = [
        ('d', 'v', 2, ('v', 'NodePath$549$set_render_mode_perspective', 'pBi'), ['bool', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$550$set_render_mode_perspective', 'pB'), ['bool']),
    ]
    c.ct['set_render_mode_thickness'] = [
        ('d', 'v', 2, ('v', 'NodePath$547$set_render_mode_thickness', 'pfi'), ['PN_stdfloat', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$548$set_render_mode_thickness', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_render_mode_wireframe'] = [
        ('d', 'v', 1, ('v', 'NodePath$541$set_render_mode_wireframe', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath$542$set_render_mode_wireframe', 'p'), []),
    ]
    c.ct['set_sa'] = [
        ('d', 'v', 1, ('v', 'NodePath$305$set_sa', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_sb'] = [
        ('d', 'v', 1, ('v', 'NodePath$304$set_sb', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_scale'] = [
        ('d', 'v', 1, ('v', 'NodePath$193$set_scale', 'pp'), ['LVecBase3 const&']),
        ('d', 'v', 2, ('v', 'NodePath$194$set_scale', 'ppp'), ['NodePath const&', 'LVecBase3 const&']),
        ('d', 'v', 2, ('v', 'NodePath$195$set_scale', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 4, ('v', 'NodePath$196$set_scale', 'ppfff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath$197$set_scale', 'pf'), ['PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath$198$set_scale', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_scissor'] = [
        ('d', 'v', 2, ('v', 'NodePath$333$set_scissor', 'ppp'), ['LPoint3 const&', 'LPoint3 const&']),
        ('d', 'v', 4, ('v', 'NodePath$334$set_scissor', 'ppppp'), ['LPoint3 const&', 'LPoint3 const&', 'LPoint3 const&', 'LPoint3 const&']),
        ('d', 'v', 3, ('v', 'NodePath$335$set_scissor', 'pppp'), ['NodePath const&', 'LPoint3 const&', 'LPoint3 const&']),
        ('d', 'v', 5, ('v', 'NodePath$336$set_scissor', 'pppppp'), ['NodePath const&', 'LPoint3 const&', 'LPoint3 const&', 'LPoint3 const&', 'LPoint3 const&']),
        ('d', 'v', 4, ('v', 'NodePath$337$set_scissor', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_sg'] = [
        ('d', 'v', 1, ('v', 'NodePath$303$set_sg', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_shader'] = [
        ('d', 'v', 2, ('v', 'NodePath$373$set_shader', 'ppi'), ['Shader const*', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$374$set_shader', 'pp'), ['Shader const*']),
    ]
    c.ct['set_shader_auto'] = [
        ('d', 'v', 2, ('v', 'NodePath$377$set_shader_auto', 'ppi'), ['BitMask32', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$378$set_shader_auto', 'pp'), ['BitMask32']),
        ('d', 'v', 1, ('v', 'NodePath$379$set_shader_auto', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath$380$set_shader_auto', 'p'), []),
    ]
    c.ct['set_shader_input'] = [
        ('d', 'v', 3, ('v', 'NodePath$382$set_shader_input', 'pspi'), ['CPT_InternalName', 'LMatrix3 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$383$set_shader_input', 'psp'), ['CPT_InternalName', 'LMatrix3 const&']),
        ('d', 'v', 3, ('v', 'NodePath$384$set_shader_input', 'pspi'), ['CPT_InternalName', 'LMatrix4 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$385$set_shader_input', 'psp'), ['CPT_InternalName', 'LMatrix4 const&']),
        ('d', 'v', 3, ('v', 'NodePath$386$set_shader_input', 'pspi'), ['CPT_InternalName', 'LVecBase2 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$387$set_shader_input', 'psp'), ['CPT_InternalName', 'LVecBase2 const&']),
        ('d', 'v', 3, ('v', 'NodePath$388$set_shader_input', 'pspi'), ['CPT_InternalName', 'LVecBase2i const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$389$set_shader_input', 'psp'), ['CPT_InternalName', 'LVecBase2i const&']),
        ('d', 'v', 3, ('v', 'NodePath$390$set_shader_input', 'pspi'), ['CPT_InternalName', 'LVecBase3 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$391$set_shader_input', 'psp'), ['CPT_InternalName', 'LVecBase3 const&']),
        ('d', 'v', 3, ('v', 'NodePath$392$set_shader_input', 'pspi'), ['CPT_InternalName', 'LVecBase3i const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$393$set_shader_input', 'psp'), ['CPT_InternalName', 'LVecBase3i const&']),
        ('d', 'v', 3, ('v', 'NodePath$394$set_shader_input', 'pspi'), ['CPT_InternalName', 'LVecBase4 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$395$set_shader_input', 'psp'), ['CPT_InternalName', 'LVecBase4 const&']),
        ('d', 'v', 3, ('v', 'NodePath$396$set_shader_input', 'pspi'), ['CPT_InternalName', 'LVecBase4i const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$397$set_shader_input', 'psp'), ['CPT_InternalName', 'LVecBase4i const&']),
        ('d', 'v', 3, ('v', 'NodePath$398$set_shader_input', 'pspi'), ['CPT_InternalName', 'NodePath const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$399$set_shader_input', 'psp'), ['CPT_InternalName', 'NodePath const&']),
        ('d', 'v', 6, ('v', 'NodePath$400$set_shader_input', 'psffffi'), ['CPT_InternalName', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'int']),
        ('d', 'v', 5, ('v', 'NodePath$401$set_shader_input', 'psffff'), ['CPT_InternalName', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 4, ('v', 'NodePath$402$set_shader_input', 'psfff'), ['CPT_InternalName', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath$403$set_shader_input', 'psff'), ['CPT_InternalName', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath$404$set_shader_input', 'pspi'), ['CPT_InternalName', 'PTA_LMatrix3 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$405$set_shader_input', 'psp'), ['CPT_InternalName', 'PTA_LMatrix3 const&']),
        ('d', 'v', 3, ('v', 'NodePath$406$set_shader_input', 'pspi'), ['CPT_InternalName', 'PTA_LMatrix4 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$407$set_shader_input', 'psp'), ['CPT_InternalName', 'PTA_LMatrix4 const&']),
        ('d', 'v', 3, ('v', 'NodePath$408$set_shader_input', 'pspi'), ['CPT_InternalName', 'PTA_LVecBase2 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$409$set_shader_input', 'psp'), ['CPT_InternalName', 'PTA_LVecBase2 const&']),
        ('d', 'v', 3, ('v', 'NodePath$410$set_shader_input', 'pspi'), ['CPT_InternalName', 'PTA_LVecBase2i const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$411$set_shader_input', 'psp'), ['CPT_InternalName', 'PTA_LVecBase2i const&']),
        ('d', 'v', 3, ('v', 'NodePath$412$set_shader_input', 'pspi'), ['CPT_InternalName', 'PTA_LVecBase3 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$413$set_shader_input', 'psp'), ['CPT_InternalName', 'PTA_LVecBase3 const&']),
        ('d', 'v', 3, ('v', 'NodePath$414$set_shader_input', 'pspi'), ['CPT_InternalName', 'PTA_LVecBase3i const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$415$set_shader_input', 'psp'), ['CPT_InternalName', 'PTA_LVecBase3i const&']),
        ('d', 'v', 3, ('v', 'NodePath$416$set_shader_input', 'pspi'), ['CPT_InternalName', 'PTA_LVecBase4 const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$417$set_shader_input', 'psp'), ['CPT_InternalName', 'PTA_LVecBase4 const&']),
        ('d', 'v', 3, ('v', 'NodePath$418$set_shader_input', 'pspi'), ['CPT_InternalName', 'PTA_LVecBase4i const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$419$set_shader_input', 'psp'), ['CPT_InternalName', 'PTA_LVecBase4i const&']),
        ('d', 'v', 3, ('v', 'NodePath$420$set_shader_input', 'pspi'), ['CPT_InternalName', 'PTA_double const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$421$set_shader_input', 'psp'), ['CPT_InternalName', 'PTA_double const&']),
        ('d', 'v', 3, ('v', 'NodePath$422$set_shader_input', 'pspi'), ['CPT_InternalName', 'PTA_float const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$423$set_shader_input', 'psp'), ['CPT_InternalName', 'PTA_float const&']),
        ('d', 'v', 3, ('v', 'NodePath$424$set_shader_input', 'pspi'), ['CPT_InternalName', 'PTA_int const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$425$set_shader_input', 'psp'), ['CPT_InternalName', 'PTA_int const&']),
        ('d', 'v', 3, ('v', 'NodePath$426$set_shader_input', 'pspi'), ['CPT_InternalName', 'ShaderBuffer*', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$427$set_shader_input', 'psp'), ['CPT_InternalName', 'ShaderBuffer*']),
        ('d', 'v', 4, ('v', 'NodePath$428$set_shader_input', 'psppi'), ['CPT_InternalName', 'Texture*', 'SamplerState const&', 'int']),
        ('d', 'v', 3, ('v', 'NodePath$429$set_shader_input', 'pspp'), ['CPT_InternalName', 'Texture*', 'SamplerState const&']),
        ('d', 'v', 7, ('v', 'NodePath$430$set_shader_input', 'pspBBiii'), ['CPT_InternalName', 'Texture*', 'bool', 'bool', 'int', 'int', 'int']),
        ('d', 'v', 6, ('v', 'NodePath$431$set_shader_input', 'pspBBii'), ['CPT_InternalName', 'Texture*', 'bool', 'bool', 'int', 'int']),
        ('d', 'v', 5, ('v', 'NodePath$432$set_shader_input', 'pspBBi'), ['CPT_InternalName', 'Texture*', 'bool', 'bool', 'int']),
        ('d', 'v', 4, ('v', 'NodePath$433$set_shader_input', 'pspBB'), ['CPT_InternalName', 'Texture*', 'bool', 'bool']),
        ('d', 'v', 3, ('v', 'NodePath$434$set_shader_input', 'pspi'), ['CPT_InternalName', 'Texture*', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$435$set_shader_input', 'psp'), ['CPT_InternalName', 'Texture*']),
        ('d', 'v', 6, ('v', 'NodePath$436$set_shader_input', 'psiiiii'), ['CPT_InternalName', 'int', 'int', 'int', 'int', 'int']),
        ('d', 'v', 5, ('v', 'NodePath$437$set_shader_input', 'psiiii'), ['CPT_InternalName', 'int', 'int', 'int', 'int']),
        ('d', 'v', 4, ('v', 'NodePath$438$set_shader_input', 'psiii'), ['CPT_InternalName', 'int', 'int', 'int']),
        ('d', 'v', 3, ('v', 'NodePath$439$set_shader_input', 'psii'), ['CPT_InternalName', 'int', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$440$set_shader_input', 'pp'), ['ShaderInput&&']),
        ('d', 'v', 1, ('v', 'NodePath$441$set_shader_input', 'pp'), ['ShaderInput const&']),
    ]
    c.ct['set_shader_off'] = [
        ('d', 'v', 1, ('v', 'NodePath$375$set_shader_off', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath$376$set_shader_off', 'p'), []),
    ]
    c.ct['set_shear'] = [
        ('d', 'v', 1, ('v', 'NodePath$213$set_shear', 'pp'), ['LVecBase3 const&']),
        ('d', 'v', 2, ('v', 'NodePath$214$set_shear', 'ppp'), ['NodePath const&', 'LVecBase3 const&']),
        ('d', 'v', 4, ('v', 'NodePath$215$set_shear', 'ppfff'), ['NodePath const&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath$216$set_shear', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_shxy'] = [
        ('d', 'v', 2, ('v', 'NodePath$217$set_shxy', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath$218$set_shxy', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_shxz'] = [
        ('d', 'v', 2, ('v', 'NodePath$219$set_shxz', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath$220$set_shxz', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_shyz'] = [
        ('d', 'v', 2, ('v', 'NodePath$221$set_shyz', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath$222$set_shyz', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_sr'] = [
        ('d', 'v', 1, ('v', 'NodePath$302$set_sr', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_state'] = [
        ('d', 'v', 3, ('v', 'NodePath$99$set_state', 'pppp'), ['NodePath const&', 'RenderState const*', 'Thread*']),
        ('d', 'v', 2, ('v', 'NodePath$100$set_state', 'ppp'), ['NodePath const&', 'RenderState const*']),
        ('d', 'v', 2, ('v', 'NodePath$101$set_state', 'ppp'), ['RenderState const*', 'Thread*']),
        ('d', 'v', 1, ('v', 'NodePath$102$set_state', 'pp'), ['RenderState const*']),
    ]
    c.ct['set_sx'] = [
        ('d', 'v', 2, ('v', 'NodePath$199$set_sx', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath$200$set_sx', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_sy'] = [
        ('d', 'v', 2, ('v', 'NodePath$201$set_sy', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath$202$set_sy', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_sz'] = [
        ('d', 'v', 2, ('v', 'NodePath$203$set_sz', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath$204$set_sz', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_tag'] = [
        ('d', 'v', 2, ('v', 'NodePath$670$set_tag', 'pss'), ['std::string const&', 'std::string const&']),
    ]
    c.ct['set_tex_gen'] = [
        ('d', 'v', 4, ('v', 'NodePath$490$set_tex_gen', 'ppppi'), ['TextureStage*', 'RenderAttrib::TexGenMode', 'LTexCoord3 const&', 'int']),
        ('d', 'v', 3, ('v', 'NodePath$491$set_tex_gen', 'pppp'), ['TextureStage*', 'RenderAttrib::TexGenMode', 'LTexCoord3 const&']),
        ('d', 'v', 3, ('v', 'NodePath$492$set_tex_gen', 'pppi'), ['TextureStage*', 'RenderAttrib::TexGenMode', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$493$set_tex_gen', 'ppp'), ['TextureStage*', 'RenderAttrib::TexGenMode']),
    ]
    c.ct['set_tex_hpr'] = [
        ('d', 'v', 3, ('v', 'NodePath$480$set_tex_hpr', 'pppp'), ['NodePath const&', 'TextureStage*', 'LVecBase3 const&']),
        ('d', 'v', 5, ('v', 'NodePath$481$set_tex_hpr', 'pppfff'), ['NodePath const&', 'TextureStage*', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 2, ('v', 'NodePath$482$set_tex_hpr', 'ppp'), ['TextureStage*', 'LVecBase3 const&']),
        ('d', 'v', 4, ('v', 'NodePath$483$set_tex_hpr', 'ppfff'), ['TextureStage*', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_tex_offset'] = [
        ('d', 'v', 3, ('v', 'NodePath$454$set_tex_offset', 'pppp'), ['NodePath const&', 'TextureStage*', 'LVecBase2 const&']),
        ('d', 'v', 4, ('v', 'NodePath$455$set_tex_offset', 'pppff'), ['NodePath const&', 'TextureStage*', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 2, ('v', 'NodePath$456$set_tex_offset', 'ppp'), ['TextureStage*', 'LVecBase2 const&']),
        ('d', 'v', 3, ('v', 'NodePath$457$set_tex_offset', 'ppff'), ['TextureStage*', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_tex_pos'] = [
        ('d', 'v', 3, ('v', 'NodePath$476$set_tex_pos', 'pppp'), ['NodePath const&', 'TextureStage*', 'LVecBase3 const&']),
        ('d', 'v', 5, ('v', 'NodePath$477$set_tex_pos', 'pppfff'), ['NodePath const&', 'TextureStage*', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 2, ('v', 'NodePath$478$set_tex_pos', 'ppp'), ['TextureStage*', 'LVecBase3 const&']),
        ('d', 'v', 4, ('v', 'NodePath$479$set_tex_pos', 'ppfff'), ['TextureStage*', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_tex_projector'] = [
        ('d', 'v', 4, ('v', 'NodePath$498$set_tex_projector', 'ppppi'), ['TextureStage*', 'NodePath const&', 'NodePath const&', 'int']),
        ('d', 'v', 3, ('v', 'NodePath$499$set_tex_projector', 'pppp'), ['TextureStage*', 'NodePath const&', 'NodePath const&']),
    ]
    c.ct['set_tex_rotate'] = [
        ('d', 'v', 3, ('v', 'NodePath$458$set_tex_rotate', 'pppf'), ['NodePath const&', 'TextureStage*', 'PN_stdfloat']),
        ('d', 'v', 2, ('v', 'NodePath$459$set_tex_rotate', 'ppf'), ['TextureStage*', 'PN_stdfloat']),
    ]
    c.ct['set_tex_scale'] = [
        ('d', 'v', 3, ('v', 'NodePath$460$set_tex_scale', 'pppp'), ['NodePath const&', 'TextureStage*', 'LVecBase2 const&']),
        ('d', 'v', 3, ('v', 'NodePath$461$set_tex_scale', 'pppp'), ['NodePath const&', 'TextureStage*', 'LVecBase3 const&']),
        ('d', 'v', 3, ('v', 'NodePath$462$set_tex_scale', 'pppf'), ['NodePath const&', 'TextureStage*', 'PN_stdfloat']),
        ('d', 'v', 4, ('v', 'NodePath$463$set_tex_scale', 'pppff'), ['NodePath const&', 'TextureStage*', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 5, ('v', 'NodePath$464$set_tex_scale', 'pppfff'), ['NodePath const&', 'TextureStage*', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 2, ('v', 'NodePath$465$set_tex_scale', 'ppp'), ['TextureStage*', 'LVecBase2 const&']),
        ('d', 'v', 2, ('v', 'NodePath$466$set_tex_scale', 'ppp'), ['TextureStage*', 'LVecBase3 const&']),
        ('d', 'v', 2, ('v', 'NodePath$467$set_tex_scale', 'ppf'), ['TextureStage*', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePath$468$set_tex_scale', 'ppff'), ['TextureStage*', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 4, ('v', 'NodePath$469$set_tex_scale', 'ppfff'), ['TextureStage*', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_tex_transform'] = [
        ('d', 'v', 3, ('v', 'NodePath$447$set_tex_transform', 'pppp'), ['NodePath const&', 'TextureStage*', 'TransformState const*']),
        ('d', 'v', 2, ('v', 'NodePath$448$set_tex_transform', 'ppp'), ['TextureStage*', 'TransformState const*']),
    ]
    c.ct['set_texture'] = [
        ('d', 'v', 3, ('v', 'NodePath$350$set_texture', 'pppi'), ['Texture*', 'SamplerState const&', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$351$set_texture', 'ppp'), ['Texture*', 'SamplerState const&']),
        ('d', 'v', 2, ('v', 'NodePath$352$set_texture', 'ppi'), ['Texture*', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$353$set_texture', 'pp'), ['Texture*']),
        ('d', 'v', 4, ('v', 'NodePath$354$set_texture', 'ppppi'), ['TextureStage*', 'Texture*', 'SamplerState const&', 'int']),
        ('d', 'v', 3, ('v', 'NodePath$355$set_texture', 'pppp'), ['TextureStage*', 'Texture*', 'SamplerState const&']),
        ('d', 'v', 3, ('v', 'NodePath$356$set_texture', 'pppi'), ['TextureStage*', 'Texture*', 'int']),
        ('d', 'v', 2, ('v', 'NodePath$357$set_texture', 'ppp'), ['TextureStage*', 'Texture*']),
    ]
    c.ct['set_texture_off'] = [
        ('d', 'v', 2, ('v', 'NodePath$358$set_texture_off', 'ppi'), ['TextureStage*', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$359$set_texture_off', 'pp'), ['TextureStage*']),
        ('d', 'v', 1, ('v', 'NodePath$360$set_texture_off', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath$361$set_texture_off', 'p'), []),
    ]
    c.ct['set_transform'] = [
        ('d', 'v', 3, ('v', 'NodePath$125$set_transform', 'pppp'), ['NodePath const&', 'TransformState const*', 'Thread*']),
        ('d', 'v', 2, ('v', 'NodePath$126$set_transform', 'ppp'), ['NodePath const&', 'TransformState const*']),
        ('d', 'v', 2, ('v', 'NodePath$127$set_transform', 'ppp'), ['TransformState const*', 'Thread*']),
        ('d', 'v', 1, ('v', 'NodePath$128$set_transform', 'pp'), ['TransformState const*']),
    ]
    c.ct['set_transparency'] = [
        ('d', 'v', 2, ('v', 'NodePath$598$set_transparency', 'ppi'), ['TransparencyAttrib::Mode', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$599$set_transparency', 'pp'), ['TransparencyAttrib::Mode']),
    ]
    c.ct['set_two_sided'] = [
        ('d', 'v', 2, ('v', 'NodePath$558$set_two_sided', 'pBi'), ['bool', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$559$set_two_sided', 'pB'), ['bool']),
    ]
    c.ct['set_x'] = [
        ('d', 'v', 2, ('v', 'NodePath$145$set_x', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath$146$set_x', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_y'] = [
        ('d', 'v', 2, ('v', 'NodePath$147$set_y', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath$148$set_y', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_z'] = [
        ('d', 'v', 2, ('v', 'NodePath$149$set_z', 'ppf'), ['NodePath const&', 'PN_stdfloat']),
        ('d', 'v', 1, ('v', 'NodePath$150$set_z', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['show'] = [
        ('d', 'v', 0, ('v', 'NodePath$622$show', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath$623$show', 'pp'), ['DrawMask']),
    ]
    c.ct['show_bounds'] = [
        ('d', 'v', 0, ('v', 'NodePath$655$show_bounds', 'p'), []),
    ]
    c.ct['show_through'] = [
        ('d', 'v', 0, ('v', 'NodePath$624$show_through', 'p'), []),
        ('d', 'v', 1, ('v', 'NodePath$625$show_through', 'pp'), ['DrawMask']),
    ]
    c.ct['show_tight_bounds'] = [
        ('d', 'v', 0, ('v', 'NodePath$656$show_tight_bounds', 'p'), []),
    ]
    c.ct['stash'] = [
        ('d', 'v', 2, ('v', 'NodePath$633$stash', 'pip'), ['int', 'Thread*']),
        ('d', 'v', 1, ('v', 'NodePath$634$stash', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath$635$stash', 'p'), []),
    ]
    c.ct['stash_to'] = [
        ('d', 'v', 3, ('v', 'NodePath$63$stash_to', 'ppip'), ['NodePath const&', 'int', 'Thread*']),
        ('d', 'v', 2, ('v', 'NodePath$64$stash_to', 'ppi'), ['NodePath const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$65$stash_to', 'pp'), ['NodePath const&']),
    ]
    c.ct['unify_texture_stages'] = [
        ('d', 'v', 1, ('v', 'NodePath$521$unify_texture_stages', 'pp'), ['TextureStage*']),
    ]
    c.ct['unstash'] = [
        ('d', 'v', 2, ('v', 'NodePath$636$unstash', 'pip'), ['int', 'Thread*']),
        ('d', 'v', 1, ('v', 'NodePath$637$unstash', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePath$638$unstash', 'p'), []),
    ]
    c.ct['unstash_all'] = [
        ('d', 'v', 1, ('v', 'NodePath$639$unstash_all', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'NodePath$640$unstash_all', 'p'), []),
    ]
    c.ct['verify_complete'] = [
        ('d', 'B', 1, ('B', 'NodePath$650$verify_complete', 'pp'), ['Thread*']),
        ('d', 'B', 0, ('B', 'NodePath$651$verify_complete', 'p'), []),
    ]
    c.ct['write_bam_file'] = [
        ('d', 'B', 1, ('B', 'NodePath$681$write_bam_file', 'pp'), ['Filename const&']),
    ]
    c.ct['write_bam_stream'] = [
        ('d', 'B', 1, ('B', 'NodePath$682$write_bam_stream', 'pp'), ['std::ostream&']),
    ]
    c.ct['write_bounds'] = [
        ('d', 'v', 1, ('v', 'NodePath$661$write_bounds', 'pp'), ['std::ostream&']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'NodePath$688$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]
    c.ct['wrt_reparent_to'] = [
        ('d', 'v', 3, ('v', 'NodePath$66$wrt_reparent_to', 'ppip'), ['NodePath const&', 'int', 'Thread*']),
        ('d', 'v', 2, ('v', 'NodePath$67$wrt_reparent_to', 'ppi'), ['NodePath const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$68$wrt_reparent_to', 'pp'), ['NodePath const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(NodePath, attr, self)

NodePath.c.link(NodePath)



class NodePathCollection(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("NodePathCollection", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 8, 0, ('p', 'NodePathCollection$1$NodePathCollection', ''), []),
        ('s', 8, 1, ('p', 'NodePathCollection$2$NodePathCollection', 'p'), ['NodePathCollection const&']),
    ]

    # classmethod type calls


    # instance method type calls

    c.ct['add_path'] = [
        ('d', 'v', 1, ('v', 'NodePathCollection$3$add_path', 'pp'), ['NodePath const&']),
    ]
    c.ct['add_paths_from'] = [
        ('d', 'v', 1, ('v', 'NodePathCollection$5$add_paths_from', 'pp'), ['NodePathCollection const&']),
    ]
    c.ct['append'] = [
        ('d', 'v', 1, ('v', 'NodePathCollection$15$append', 'pp'), ['NodePath const&']),
    ]
    c.ct['calc_tight_bounds'] = [
        ('d', 'B', 2, ('B', 'NodePathCollection$32$calc_tight_bounds', 'ppp'), ['LPoint3&', 'LPoint3&']),
    ]
    c.ct['clear'] = [
        ('d', 'v', 0, ('v', 'NodePathCollection$9$clear', 'p'), []),
    ]
    c.ct['compose_color_scale'] = [
        ('d', 'v', 2, ('v', 'NodePathCollection$51$compose_color_scale', 'ppi'), ['LVecBase4 const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePathCollection$52$compose_color_scale', 'pp'), ['LVecBase4 const&']),
        ('d', 'v', 5, ('v', 'NodePathCollection$53$compose_color_scale', 'pffffi'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'int']),
        ('d', 'v', 4, ('v', 'NodePathCollection$54$compose_color_scale', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePathCollection$55$compose_color_scale', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['detach'] = [
        ('d', 'v', 0, ('v', 'NodePathCollection$27$detach', 'p'), []),
    ]
    c.ct['extend'] = [
        ('d', 'v', 1, ('v', 'NodePathCollection$16$extend', 'pp'), ['NodePathCollection const&']),
    ]
    c.ct['find_all_matches'] = [
        ('d', 8, 1, ('p', 'NodePathCollection$20$find_all_matches', 'ps'), ['std::string const&']),
    ]
    c.ct['get_collide_mask'] = [
        ('d', 'p', 0, ('p', 'NodePathCollection$28$get_collide_mask', 'p'), []),
    ]
    c.ct['get_num_paths'] = [
        ('d', 'i', 0, ('i', 'NodePathCollection$12$get_num_paths', 'p'), []),
    ]
    c.ct['get_path'] = [
        ('d', 7, 1, ('p', 'NodePathCollection$13$get_path', 'pi'), ['int']),
    ]
    c.ct['has_path'] = [
        ('d', 'B', 1, ('B', 'NodePathCollection$8$has_path', 'pp'), ['NodePath const&']),
    ]
    c.ct['hide'] = [
        ('d', 'v', 0, ('v', 'NodePathCollection$24$hide', 'p'), []),
    ]
    c.ct['is_empty'] = [
        ('d', 'B', 0, ('B', 'NodePathCollection$11$is_empty', 'p'), []),
    ]
    c.ct['ls'] = [
        ('d', 'v', 0, ('v', 'NodePathCollection$17$ls', 'p'), []),
        ('d', 'v', 2, ('v', 'NodePathCollection$18$ls', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'v', 1, ('v', 'NodePathCollection$19$ls', 'pp'), ['std::ostream&']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'NodePathCollection$58$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['remove_duplicate_paths'] = [
        ('d', 'v', 0, ('v', 'NodePathCollection$7$remove_duplicate_paths', 'p'), []),
    ]
    c.ct['remove_path'] = [
        ('d', 'B', 1, ('B', 'NodePathCollection$4$remove_path', 'pp'), ['NodePath const&']),
    ]
    c.ct['remove_paths_from'] = [
        ('d', 'v', 1, ('v', 'NodePathCollection$6$remove_paths_from', 'pp'), ['NodePathCollection const&']),
    ]
    c.ct['reparent_to'] = [
        ('d', 'v', 1, ('v', 'NodePathCollection$21$reparent_to', 'pp'), ['NodePath const&']),
    ]
    c.ct['reserve'] = [
        ('d', 'v', 1, ('v', 'NodePathCollection$10$reserve', 'pp'), ['std::size_t']),
    ]
    c.ct['set_attrib'] = [
        ('d', 'v', 2, ('v', 'NodePathCollection$56$set_attrib', 'ppi'), ['RenderAttrib const*', 'int']),
        ('d', 'v', 1, ('v', 'NodePathCollection$57$set_attrib', 'pp'), ['RenderAttrib const*']),
    ]
    c.ct['set_collide_mask'] = [
        ('d', 'v', 3, ('v', 'NodePathCollection$29$set_collide_mask', 'pppi'), ['CollideMask', 'CollideMask', 'TypeHandle']),
        ('d', 'v', 2, ('v', 'NodePathCollection$30$set_collide_mask', 'ppp'), ['CollideMask', 'CollideMask']),
        ('d', 'v', 1, ('v', 'NodePathCollection$31$set_collide_mask', 'pp'), ['CollideMask']),
    ]
    c.ct['set_color'] = [
        ('d', 'v', 2, ('v', 'NodePathCollection$41$set_color', 'ppi'), ['LColor const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePathCollection$42$set_color', 'pp'), ['LColor const&']),
        ('d', 'v', 5, ('v', 'NodePathCollection$43$set_color', 'pffffi'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'int']),
        ('d', 'v', 4, ('v', 'NodePathCollection$44$set_color', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePathCollection$45$set_color', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_color_scale'] = [
        ('d', 'v', 2, ('v', 'NodePathCollection$46$set_color_scale', 'ppi'), ['LVecBase4 const&', 'int']),
        ('d', 'v', 1, ('v', 'NodePathCollection$47$set_color_scale', 'pp'), ['LVecBase4 const&']),
        ('d', 'v', 5, ('v', 'NodePathCollection$48$set_color_scale', 'pffffi'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'int']),
        ('d', 'v', 4, ('v', 'NodePathCollection$49$set_color_scale', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 3, ('v', 'NodePathCollection$50$set_color_scale', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_texture'] = [
        ('d', 'v', 2, ('v', 'NodePathCollection$33$set_texture', 'ppi'), ['Texture*', 'int']),
        ('d', 'v', 1, ('v', 'NodePathCollection$34$set_texture', 'pp'), ['Texture*']),
        ('d', 'v', 3, ('v', 'NodePathCollection$35$set_texture', 'pppi'), ['TextureStage*', 'Texture*', 'int']),
        ('d', 'v', 2, ('v', 'NodePathCollection$36$set_texture', 'ppp'), ['TextureStage*', 'Texture*']),
    ]
    c.ct['set_texture_off'] = [
        ('d', 'v', 2, ('v', 'NodePathCollection$37$set_texture_off', 'ppi'), ['TextureStage*', 'int']),
        ('d', 'v', 1, ('v', 'NodePathCollection$38$set_texture_off', 'pp'), ['TextureStage*']),
        ('d', 'v', 1, ('v', 'NodePathCollection$39$set_texture_off', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'NodePathCollection$40$set_texture_off', 'p'), []),
    ]
    c.ct['show'] = [
        ('d', 'v', 0, ('v', 'NodePathCollection$23$show', 'p'), []),
    ]
    c.ct['size'] = [
        ('d', 'p', 0, ('p', 'NodePathCollection$14$size', 'p'), []),
    ]
    c.ct['stash'] = [
        ('d', 'v', 0, ('v', 'NodePathCollection$25$stash', 'p'), []),
    ]
    c.ct['unstash'] = [
        ('d', 'v', 0, ('v', 'NodePathCollection$26$unstash', 'p'), []),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'NodePathCollection$59$write', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'v', 1, ('v', 'NodePathCollection$60$write', 'pp'), ['std::ostream&']),
    ]
    c.ct['wrt_reparent_to'] = [
        ('d', 'v', 1, ('v', 'NodePathCollection$22$wrt_reparent_to', 'pp'), ['NodePath const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(NodePathCollection, attr, self)

NodePathCollection.c.link(NodePathCollection)



class PandaFramework(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("PandaFramework", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 9, 0, ('p', 'PandaFramework$1$PandaFramework', ''), []),
        ('s', 9, 1, ('p', 'PandaFramework$2$PandaFramework', 'p'), ['PandaFramework const&']),
    ]

    # classmethod type calls

    c.ct['hide_collision_solids'] = [
        ('s', 'i', 1, ('i', 'PandaFramework$43$hide_collision_solids', 'p'), ['NodePath']),
    ]
    c.ct['show_collision_solids'] = [
        ('s', 'i', 1, ('i', 'PandaFramework$44$show_collision_solids', 'p'), ['NodePath']),
    ]

    @classmethod
    def hide_collision_solids(cls, *args,**kw):
        return ( cls.c.get('hide_collision_solids', None) or cls.c.call(PandaFramework, 'hide_collision_solids', None) )(*args,**kw)

    @classmethod
    def show_collision_solids(cls, *args,**kw):
        return ( cls.c.get('show_collision_solids', None) or cls.c.call(PandaFramework, 'show_collision_solids', None) )(*args,**kw)

    # instance method type calls

    c.ct['all_windows_closed'] = [
        ('d', 'B', 0, ('B', 'PandaFramework$27$all_windows_closed', 'p'), []),
    ]
    c.ct['clear_exit_flag'] = [
        ('d', 'v', 0, ('v', 'PandaFramework$55$clear_exit_flag', 'p'), []),
    ]
    c.ct['clear_highlight'] = [
        ('d', 'v', 0, ('v', 'PandaFramework$46$clear_highlight', 'p'), []),
    ]
    c.ct['close_all_windows'] = [
        ('d', 'v', 0, ('v', 'PandaFramework$26$close_all_windows', 'p'), []),
    ]
    c.ct['close_framework'] = [
        ('d', 'v', 0, ('v', 'PandaFramework$4$close_framework', 'p'), []),
    ]
    c.ct['close_window'] = [
        ('d', 'v', 1, ('v', 'PandaFramework$24$close_window', 'pp'), ['WindowFramework*']),
        ('d', 'v', 1, ('v', 'PandaFramework$25$close_window', 'pi'), ['int']),
    ]
    c.ct['do_frame'] = [
        ('d', 'B', 1, ('B', 'PandaFramework$52$do_frame', 'pp'), ['Thread*']),
    ]
    c.ct['enable_default_keys'] = [
        ('d', 'v', 0, ('v', 'PandaFramework$51$enable_default_keys', 'p'), []),
    ]
    c.ct['find_window'] = [
        ('d', 'i', 1, ('i', 'PandaFramework$22$find_window', 'pp'), ['GraphicsOutput const*']),
        ('d', 'i', 1, ('i', 'PandaFramework$23$find_window', 'pp'), ['WindowFramework const*']),
    ]
    c.ct['get_background_type'] = [
        ('d', 'p', 0, ('p', 'PandaFramework$42$get_background_type', 'p'), []),
    ]
    c.ct['get_data_root'] = [
        ('d', 7, 0, ('p', 'PandaFramework$7$get_data_root', 'p'), []),
    ]
    c.ct['get_default_pipe'] = [
        ('d', 'p', 0, ('p', 'PandaFramework$5$get_default_pipe', 'p'), []),
    ]
    c.ct['get_default_window_props'] = [
        ('d', 'v', 1, ('v', 'PandaFramework$13$get_default_window_props', 'pp'), ['WindowProperties&']),
    ]
    c.ct['get_event_handler'] = [
        ('d', 'p', 0, ('p', 'PandaFramework$8$get_event_handler', 'p'), []),
    ]
    c.ct['get_graphics_engine'] = [
        ('d', 'p', 0, ('p', 'PandaFramework$6$get_graphics_engine', 'p'), []),
    ]
    c.ct['get_highlight'] = [
        ('d', 7, 0, ('p', 'PandaFramework$48$get_highlight', 'p'), []),
    ]
    c.ct['get_lighting'] = [
        ('d', 'B', 0, ('B', 'PandaFramework$40$get_lighting', 'p'), []),
    ]
    c.ct['get_models'] = [
        ('d', 7, 0, ('p', 'PandaFramework$28$get_models', 'p'), []),
    ]
    c.ct['get_mouse'] = [
        ('d', 7, 1, ('p', 'PandaFramework$10$get_mouse', 'pp'), ['GraphicsOutput*']),
    ]
    c.ct['get_num_windows'] = [
        ('d', 'i', 0, ('i', 'PandaFramework$20$get_num_windows', 'p'), []),
    ]
    c.ct['get_perpixel'] = [
        ('d', 'B', 0, ('B', 'PandaFramework$41$get_perpixel', 'p'), []),
    ]
    c.ct['get_recorder'] = [
        ('d', 'p', 0, ('p', 'PandaFramework$49$get_recorder', 'p'), []),
    ]
    c.ct['get_task_mgr'] = [
        ('d', 'p', 0, ('p', 'PandaFramework$9$get_task_mgr', 'p'), []),
    ]
    c.ct['get_texture'] = [
        ('d', 'B', 0, ('B', 'PandaFramework$38$get_texture', 'p'), []),
    ]
    c.ct['get_two_sided'] = [
        ('d', 'B', 0, ('B', 'PandaFramework$39$get_two_sided', 'p'), []),
    ]
    c.ct['get_window'] = [
        ('d', 20, 1, ('p', 'PandaFramework$21$get_window', 'pi'), ['int']),
    ]
    c.ct['get_wireframe'] = [
        ('d', 'B', 0, ('B', 'PandaFramework$37$get_wireframe', 'p'), []),
    ]
    c.ct['has_highlight'] = [
        ('d', 'B', 0, ('B', 'PandaFramework$47$has_highlight', 'p'), []),
    ]
    c.ct['main_loop'] = [
        ('d', 'v', 0, ('v', 'PandaFramework$53$main_loop', 'p'), []),
    ]
    c.ct['open_framework'] = [
        ('d', 'v', 0, ('v', 'PandaFramework$3$open_framework', 'p'), []),
    ]
    c.ct['open_window'] = [
        ('d', 20, 0, ('p', 'PandaFramework$14$open_window', 'p'), []),
        ('d', 20, 2, ('p', 'PandaFramework$15$open_window', 'ppp'), ['GraphicsPipe*', 'GraphicsStateGuardian*']),
        ('d', 20, 1, ('p', 'PandaFramework$16$open_window', 'pp'), ['GraphicsPipe*']),
        ('d', 20, 4, ('p', 'PandaFramework$17$open_window', 'ppipp'), ['WindowProperties const&', 'int', 'GraphicsPipe*', 'GraphicsStateGuardian*']),
        ('d', 20, 3, ('p', 'PandaFramework$18$open_window', 'ppip'), ['WindowProperties const&', 'int', 'GraphicsPipe*']),
        ('d', 20, 2, ('p', 'PandaFramework$19$open_window', 'ppi'), ['WindowProperties const&', 'int']),
    ]
    c.ct['remove_mouse'] = [
        ('d', 'v', 1, ('v', 'PandaFramework$11$remove_mouse', 'pp'), ['GraphicsOutput const*']),
    ]
    c.ct['report_frame_rate'] = [
        ('d', 'v', 1, ('v', 'PandaFramework$29$report_frame_rate', 'pp'), ['std::ostream&']),
    ]
    c.ct['reset_frame_rate'] = [
        ('d', 'v', 0, ('v', 'PandaFramework$30$reset_frame_rate', 'p'), []),
    ]
    c.ct['set_background_type'] = [
        ('d', 'v', 1, ('v', 'PandaFramework$36$set_background_type', 'pp'), ['WindowFramework::BackgroundType']),
    ]
    c.ct['set_exit_flag'] = [
        ('d', 'v', 0, ('v', 'PandaFramework$54$set_exit_flag', 'p'), []),
    ]
    c.ct['set_highlight'] = [
        ('d', 'v', 1, ('v', 'PandaFramework$45$set_highlight', 'pp'), ['NodePath const&']),
    ]
    c.ct['set_lighting'] = [
        ('d', 'v', 1, ('v', 'PandaFramework$34$set_lighting', 'pB'), ['bool']),
    ]
    c.ct['set_perpixel'] = [
        ('d', 'v', 1, ('v', 'PandaFramework$35$set_perpixel', 'pB'), ['bool']),
    ]
    c.ct['set_recorder'] = [
        ('d', 'v', 1, ('v', 'PandaFramework$50$set_recorder', 'pp'), ['RecorderController*']),
    ]
    c.ct['set_texture'] = [
        ('d', 'v', 1, ('v', 'PandaFramework$32$set_texture', 'pB'), ['bool']),
    ]
    c.ct['set_two_sided'] = [
        ('d', 'v', 1, ('v', 'PandaFramework$33$set_two_sided', 'pB'), ['bool']),
    ]
    c.ct['set_window_title'] = [
        ('d', 'v', 1, ('v', 'PandaFramework$12$set_window_title', 'ps'), ['std::string const&']),
    ]
    c.ct['set_wireframe'] = [
        ('d', 'v', 1, ('v', 'PandaFramework$31$set_wireframe', 'pB'), ['bool']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(PandaFramework, attr, self)

PandaFramework.c.link(PandaFramework)



class PandaSystem(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("PandaSystem", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['get_build_date'] = [
        ('s', 's', 0, ('s', 'PandaSystem$12$get_build_date', ''), []),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'PandaSystem$25$get_class_type', ''), []),
    ]
    c.ct['get_compiler'] = [
        ('s', 's', 0, ('s', 'PandaSystem$11$get_compiler', ''), []),
    ]
    c.ct['get_distributor'] = [
        ('s', 's', 0, ('s', 'PandaSystem$10$get_distributor', ''), []),
    ]
    c.ct['get_git_commit'] = [
        ('s', 's', 0, ('s', 'PandaSystem$13$get_git_commit', ''), []),
    ]
    c.ct['get_global_ptr'] = [
        ('s', 10, 0, ('p', 'PandaSystem$24$get_global_ptr', ''), []),
    ]
    c.ct['get_major_version'] = [
        ('s', 'i', 0, ('i', 'PandaSystem$5$get_major_version', ''), []),
    ]
    c.ct['get_memory_alignment'] = [
        ('s', 'i', 0, ('i', 'PandaSystem$9$get_memory_alignment', ''), []),
    ]
    c.ct['get_minor_version'] = [
        ('s', 'i', 0, ('i', 'PandaSystem$6$get_minor_version', ''), []),
    ]
    c.ct['get_p3d_coreapi_version_string'] = [
        ('s', 's', 0, ('s', 'PandaSystem$4$get_p3d_coreapi_version_string', ''), []),
    ]
    c.ct['get_package_host_url'] = [
        ('s', 's', 0, ('s', 'PandaSystem$3$get_package_host_url', ''), []),
    ]
    c.ct['get_package_version_string'] = [
        ('s', 's', 0, ('s', 'PandaSystem$2$get_package_version_string', ''), []),
    ]
    c.ct['get_platform'] = [
        ('s', 's', 0, ('s', 'PandaSystem$14$get_platform', ''), []),
    ]
    c.ct['get_sequence_version'] = [
        ('s', 'i', 0, ('i', 'PandaSystem$7$get_sequence_version', ''), []),
    ]
    c.ct['get_version_string'] = [
        ('s', 's', 0, ('s', 'PandaSystem$1$get_version_string', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'PandaSystem$26$init_type', ''), []),
    ]
    c.ct['is_official_version'] = [
        ('s', 'B', 0, ('B', 'PandaSystem$8$is_official_version', ''), []),
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
        ('d', 'v', 1, ('v', 'PandaSystem$19$add_system', 'ps'), ['std::string const&']),
    ]
    c.ct['get_num_systems'] = [
        ('d', 'p', 0, ('p', 'PandaSystem$16$get_num_systems', 'p'), []),
    ]
    c.ct['get_system'] = [
        ('d', 's', 1, ('s', 'PandaSystem$17$get_system', 'pp'), ['std::size_t']),
    ]
    c.ct['get_system_tag'] = [
        ('d', 's', 2, ('s', 'PandaSystem$18$get_system_tag', 'pss'), ['std::string const&', 'std::string const&']),
    ]
    c.ct['has_system'] = [
        ('d', 'B', 1, ('B', 'PandaSystem$15$has_system', 'ps'), ['std::string const&']),
    ]
    c.ct['heap_trim'] = [
        ('d', 'B', 1, ('B', 'PandaSystem$21$heap_trim', 'pp'), ['std::size_t']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'PandaSystem$22$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['set_system_tag'] = [
        ('d', 'v', 3, ('v', 'PandaSystem$20$set_system_tag', 'psss'), ['std::string const&', 'std::string const&', 'std::string const&']),
    ]
    c.ct['write'] = [
        ('d', 'v', 1, ('v', 'PandaSystem$23$write', 'pp'), ['std::ostream&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(PandaSystem, attr, self)

PandaSystem.c.link(PandaSystem)



class GeomVertexWriter(GeomEnums):
    __bases__ = tuple([GeomEnums])
    c = cxx.cstructs()
    c.register("GeomVertexWriter", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 11, 2, ('p', 'GeomVertexWriter$1$GeomVertexWriter', 'pp'), ['GeomVertexArrayData*', 'Thread*']),
        ('s', 11, 1, ('p', 'GeomVertexWriter$2$GeomVertexWriter', 'p'), ['GeomVertexArrayData*']),
        ('s', 11, 3, ('p', 'GeomVertexWriter$3$GeomVertexWriter', 'pip'), ['GeomVertexArrayData*', 'int', 'Thread*']),
        ('s', 11, 2, ('p', 'GeomVertexWriter$4$GeomVertexWriter', 'pi'), ['GeomVertexArrayData*', 'int']),
        ('s', 11, 3, ('p', 'GeomVertexWriter$5$GeomVertexWriter', 'psp'), ['GeomVertexData*', 'CPT_InternalName', 'Thread*']),
        ('s', 11, 2, ('p', 'GeomVertexWriter$6$GeomVertexWriter', 'ps'), ['GeomVertexData*', 'CPT_InternalName']),
        ('s', 11, 2, ('p', 'GeomVertexWriter$7$GeomVertexWriter', 'pp'), ['GeomVertexData*', 'Thread*']),
        ('s', 11, 1, ('p', 'GeomVertexWriter$8$GeomVertexWriter', 'p'), ['GeomVertexData*']),
        ('s', 11, 2, ('p', 'GeomVertexWriter$9$GeomVertexWriter', 'ps'), ['GeomVertexDataPipelineWriter*', 'InternalName const*']),
        ('s', 11, 1, ('p', 'GeomVertexWriter$10$GeomVertexWriter', 'p'), ['GeomVertexWriter const&']),
        ('s', 11, 1, ('p', 'GeomVertexWriter$11$GeomVertexWriter', 'p'), ['Thread*']),
        ('s', 11, 0, ('p', 'GeomVertexWriter$12$GeomVertexWriter', ''), []),
    ]

    # classmethod type calls


    # instance method type calls

    c.ct['add_data1'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$83$add_data1', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['add_data1d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$74$add_data1d', 'pd'), ['double']),
    ]
    c.ct['add_data1f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$65$add_data1f', 'pf'), ['float']),
    ]
    c.ct['add_data1i'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$92$add_data1i', 'pi'), ['int']),
    ]
    c.ct['add_data2'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$84$add_data2', 'pp'), ['LVecBase2 const&']),
        ('d', 'v', 2, ('v', 'GeomVertexWriter$85$add_data2', 'pff'), ['PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['add_data2d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$75$add_data2d', 'pp'), ['LVecBase2d const&']),
        ('d', 'v', 2, ('v', 'GeomVertexWriter$76$add_data2d', 'pdd'), ['double', 'double']),
    ]
    c.ct['add_data2f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$66$add_data2f', 'pp'), ['LVecBase2f const&']),
        ('d', 'v', 2, ('v', 'GeomVertexWriter$67$add_data2f', 'pff'), ['float', 'float']),
    ]
    c.ct['add_data2i'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$93$add_data2i', 'pp'), ['LVecBase2i const&']),
        ('d', 'v', 2, ('v', 'GeomVertexWriter$94$add_data2i', 'pii'), ['int', 'int']),
    ]
    c.ct['add_data3'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$86$add_data3', 'pp'), ['LVecBase3 const&']),
        ('d', 'v', 3, ('v', 'GeomVertexWriter$87$add_data3', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['add_data3d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$77$add_data3d', 'pp'), ['LVecBase3d const&']),
        ('d', 'v', 3, ('v', 'GeomVertexWriter$78$add_data3d', 'pddd'), ['double', 'double', 'double']),
    ]
    c.ct['add_data3f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$68$add_data3f', 'pp'), ['LVecBase3f const&']),
        ('d', 'v', 3, ('v', 'GeomVertexWriter$69$add_data3f', 'pfff'), ['float', 'float', 'float']),
    ]
    c.ct['add_data3i'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$95$add_data3i', 'pp'), ['LVecBase3i const&']),
        ('d', 'v', 3, ('v', 'GeomVertexWriter$96$add_data3i', 'piii'), ['int', 'int', 'int']),
    ]
    c.ct['add_data4'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$88$add_data4', 'pp'), ['LVecBase4 const&']),
        ('d', 'v', 4, ('v', 'GeomVertexWriter$89$add_data4', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['add_data4d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$79$add_data4d', 'pp'), ['LVecBase4d const&']),
        ('d', 'v', 4, ('v', 'GeomVertexWriter$80$add_data4d', 'pdddd'), ['double', 'double', 'double', 'double']),
    ]
    c.ct['add_data4f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$70$add_data4f', 'pp'), ['LVecBase4f const&']),
        ('d', 'v', 4, ('v', 'GeomVertexWriter$71$add_data4f', 'pffff'), ['float', 'float', 'float', 'float']),
    ]
    c.ct['add_data4i'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$97$add_data4i', 'pp'), ['LVecBase4i const&']),
        ('d', 'v', 4, ('v', 'GeomVertexWriter$98$add_data4i', 'piiii'), ['int', 'int', 'int', 'int']),
    ]
    c.ct['add_matrix3'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$90$add_matrix3', 'pp'), ['LMatrix3 const&']),
    ]
    c.ct['add_matrix3d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$81$add_matrix3d', 'pp'), ['LMatrix3d const&']),
    ]
    c.ct['add_matrix3f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$72$add_matrix3f', 'pp'), ['LMatrix3f const&']),
    ]
    c.ct['add_matrix4'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$91$add_matrix4', 'pp'), ['LMatrix4 const&']),
    ]
    c.ct['add_matrix4d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$82$add_matrix4d', 'pp'), ['LMatrix4d const&']),
    ]
    c.ct['add_matrix4f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$73$add_matrix4f', 'pp'), ['LMatrix4f const&']),
    ]
    c.ct['clear'] = [
        ('d', 'v', 0, ('v', 'GeomVertexWriter$21$clear', 'p'), []),
    ]
    c.ct['get_array'] = [
        ('d', 'i', 0, ('i', 'GeomVertexWriter$24$get_array', 'p'), []),
    ]
    c.ct['get_array_data'] = [
        ('d', 'p', 0, ('p', 'GeomVertexWriter$14$get_array_data', 'p'), []),
    ]
    c.ct['get_array_handle'] = [
        ('d', 'p', 0, ('p', 'GeomVertexWriter$15$get_array_handle', 'p'), []),
    ]
    c.ct['get_column'] = [
        ('d', 'p', 0, ('p', 'GeomVertexWriter$25$get_column', 'p'), []),
    ]
    c.ct['get_current_thread'] = [
        ('d', 17, 0, ('p', 'GeomVertexWriter$17$get_current_thread', 'p'), []),
    ]
    c.ct['get_start_row'] = [
        ('d', 'i', 0, ('i', 'GeomVertexWriter$28$get_start_row', 'p'), []),
    ]
    c.ct['get_stride'] = [
        ('d', 'p', 0, ('p', 'GeomVertexWriter$16$get_stride', 'p'), []),
    ]
    c.ct['get_vertex_data'] = [
        ('d', 24, 0, ('p', 'GeomVertexWriter$13$get_vertex_data', 'p'), []),
    ]
    c.ct['get_write_row'] = [
        ('d', 'i', 0, ('i', 'GeomVertexWriter$29$get_write_row', 'p'), []),
    ]
    c.ct['has_column'] = [
        ('d', 'B', 0, ('B', 'GeomVertexWriter$23$has_column', 'p'), []),
    ]
    c.ct['is_at_end'] = [
        ('d', 'B', 0, ('B', 'GeomVertexWriter$30$is_at_end', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$99$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['reserve_num_rows'] = [
        ('d', 'B', 1, ('B', 'GeomVertexWriter$22$reserve_num_rows', 'pi'), ['int']),
    ]
    c.ct['set_column'] = [
        ('d', 'B', 1, ('B', 'GeomVertexWriter$18$set_column', 'ps'), ['CPT_InternalName']),
        ('d', 'B', 1, ('B', 'GeomVertexWriter$19$set_column', 'pi'), ['int']),
        ('d', 'B', 2, ('B', 'GeomVertexWriter$20$set_column', 'pip'), ['int', 'GeomVertexColumn const*']),
    ]
    c.ct['set_data1'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$49$set_data1', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_data1d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$40$set_data1d', 'pd'), ['double']),
    ]
    c.ct['set_data1f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$31$set_data1f', 'pf'), ['float']),
    ]
    c.ct['set_data1i'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$58$set_data1i', 'pi'), ['int']),
    ]
    c.ct['set_data2'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$50$set_data2', 'pp'), ['LVecBase2 const&']),
        ('d', 'v', 2, ('v', 'GeomVertexWriter$51$set_data2', 'pff'), ['PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_data2d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$41$set_data2d', 'pp'), ['LVecBase2d const&']),
        ('d', 'v', 2, ('v', 'GeomVertexWriter$42$set_data2d', 'pdd'), ['double', 'double']),
    ]
    c.ct['set_data2f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$32$set_data2f', 'pp'), ['LVecBase2f const&']),
        ('d', 'v', 2, ('v', 'GeomVertexWriter$33$set_data2f', 'pff'), ['float', 'float']),
    ]
    c.ct['set_data2i'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$59$set_data2i', 'pp'), ['LVecBase2i const&']),
        ('d', 'v', 2, ('v', 'GeomVertexWriter$60$set_data2i', 'pii'), ['int', 'int']),
    ]
    c.ct['set_data3'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$52$set_data3', 'pp'), ['LVecBase3 const&']),
        ('d', 'v', 3, ('v', 'GeomVertexWriter$53$set_data3', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_data3d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$43$set_data3d', 'pp'), ['LVecBase3d const&']),
        ('d', 'v', 3, ('v', 'GeomVertexWriter$44$set_data3d', 'pddd'), ['double', 'double', 'double']),
    ]
    c.ct['set_data3f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$34$set_data3f', 'pp'), ['LVecBase3f const&']),
        ('d', 'v', 3, ('v', 'GeomVertexWriter$35$set_data3f', 'pfff'), ['float', 'float', 'float']),
    ]
    c.ct['set_data3i'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$61$set_data3i', 'pp'), ['LVecBase3i const&']),
        ('d', 'v', 3, ('v', 'GeomVertexWriter$62$set_data3i', 'piii'), ['int', 'int', 'int']),
    ]
    c.ct['set_data4'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$54$set_data4', 'pp'), ['LVecBase4 const&']),
        ('d', 'v', 4, ('v', 'GeomVertexWriter$55$set_data4', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_data4d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$45$set_data4d', 'pp'), ['LVecBase4d const&']),
        ('d', 'v', 4, ('v', 'GeomVertexWriter$46$set_data4d', 'pdddd'), ['double', 'double', 'double', 'double']),
    ]
    c.ct['set_data4f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$36$set_data4f', 'pp'), ['LVecBase4f const&']),
        ('d', 'v', 4, ('v', 'GeomVertexWriter$37$set_data4f', 'pffff'), ['float', 'float', 'float', 'float']),
    ]
    c.ct['set_data4i'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$63$set_data4i', 'pp'), ['LVecBase4i const&']),
        ('d', 'v', 4, ('v', 'GeomVertexWriter$64$set_data4i', 'piiii'), ['int', 'int', 'int', 'int']),
    ]
    c.ct['set_matrix3'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$56$set_matrix3', 'pp'), ['LMatrix3 const&']),
    ]
    c.ct['set_matrix3d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$47$set_matrix3d', 'pp'), ['LMatrix3d const&']),
    ]
    c.ct['set_matrix3f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$38$set_matrix3f', 'pp'), ['LMatrix3f const&']),
    ]
    c.ct['set_matrix4'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$57$set_matrix4', 'pp'), ['LMatrix4 const&']),
    ]
    c.ct['set_matrix4d'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$48$set_matrix4d', 'pp'), ['LMatrix4d const&']),
    ]
    c.ct['set_matrix4f'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$39$set_matrix4f', 'pp'), ['LMatrix4f const&']),
    ]
    c.ct['set_row'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$27$set_row', 'pi'), ['int']),
    ]
    c.ct['set_row_unsafe'] = [
        ('d', 'v', 1, ('v', 'GeomVertexWriter$26$set_row_unsafe', 'pi'), ['int']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomVertexWriter, attr, self)

GeomVertexWriter.c.link(GeomVertexWriter)



class Namable(MemoryBase):
    __bases__ = tuple([MemoryBase])
    c = cxx.cstructs()
    c.register("Namable", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_PandaNode'] = [
        ('d', 28, 0, ('p', 'Namable$1$downcast_to_PandaNode', 'p'), []),
    ]
    c.ct['downcast_to_Thread'] = [
        ('d', 17, 0, ('p', 'Namable$2$downcast_to_Thread', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(Namable, attr, self)

Namable.c.link(Namable)



class ReferenceCount(MemoryBase):
    __bases__ = tuple([MemoryBase])
    c = cxx.cstructs()
    c.register("ReferenceCount", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'ReferenceCount$13$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'ReferenceCount$14$init_type', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(ReferenceCount, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(ReferenceCount, 'init_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['get_ref_count'] = [
        ('d', 'i', 0, ('i', 'ReferenceCount$2$get_ref_count', 'p'), []),
    ]
    c.ct['get_weak_list'] = [
        ('d', 'p', 0, ('p', 'ReferenceCount$9$get_weak_list', 'p'), []),
    ]
    c.ct['has_weak_list'] = [
        ('d', 'B', 0, ('B', 'ReferenceCount$8$has_weak_list', 'p'), []),
    ]
    c.ct['local_object'] = [
        ('d', 'v', 0, ('v', 'ReferenceCount$7$local_object', 'p'), []),
    ]
    c.ct['ref'] = [
        ('d', 'v', 0, ('v', 'ReferenceCount$3$ref', 'p'), []),
    ]
    c.ct['ref_if_nonzero'] = [
        ('d', 'B', 0, ('B', 'ReferenceCount$12$ref_if_nonzero', 'p'), []),
    ]
    c.ct['test_ref_count_integrity'] = [
        ('d', 'B', 0, ('B', 'ReferenceCount$5$test_ref_count_integrity', 'p'), []),
    ]
    c.ct['test_ref_count_nonzero'] = [
        ('d', 'B', 0, ('B', 'ReferenceCount$6$test_ref_count_nonzero', 'p'), []),
    ]
    c.ct['unref'] = [
        ('d', 'B', 0, ('B', 'ReferenceCount$4$unref', 'p'), []),
    ]
    c.ct['upcast_to_MemoryBase'] = [
        ('d', 6, 0, ('p', 'ReferenceCount$1$upcast_to_MemoryBase', 'p'), []),
    ]
    c.ct['weak_ref'] = [
        ('d', 'p', 0, ('p', 'ReferenceCount$10$weak_ref', 'p'), []),
    ]
    c.ct['weak_unref'] = [
        ('d', 'v', 0, ('v', 'ReferenceCount$11$weak_unref', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(ReferenceCount, attr, self)

ReferenceCount.c.link(ReferenceCount)



class TypedObject(MemoryBase):
    __bases__ = tuple([MemoryBase])
    c = cxx.cstructs()
    c.register("TypedObject", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'TypedObject$10$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'TypedObject$11$init_type', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(TypedObject, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(TypedObject, 'init_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['as_typed_object'] = [
        ('d', 14, 0, ('p', 'TypedObject$8$as_typed_object', 'p'), []),
        ('d', 14, 0, ('p', 'TypedObject$9$as_typed_object', 'p'), []),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'TypedObject$7$force_init_type', 'p'), []),
    ]
    c.ct['get_best_parent_from_Set'] = [
        ('d', 'i', 1, ('i', 'TypedObject$6$get_best_parent_from_Set', 'pp'), ['set< int > const&']),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'TypedObject$2$get_type', 'p'), []),
    ]
    c.ct['get_type_index'] = [
        ('d', 'i', 0, ('i', 'TypedObject$3$get_type_index', 'p'), []),
    ]
    c.ct['is_exact_type'] = [
        ('d', 'B', 1, ('B', 'TypedObject$5$is_exact_type', 'pi'), ['TypeHandle']),
    ]
    c.ct['is_of_type'] = [
        ('d', 'B', 1, ('B', 'TypedObject$4$is_of_type', 'pi'), ['TypeHandle']),
    ]
    c.ct['upcast_to_MemoryBase'] = [
        ('d', 6, 0, ('p', 'TypedObject$1$upcast_to_MemoryBase', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TypedObject, attr, self)

TypedObject.c.link(TypedObject)



class TypedWritable(TypedObject):
    __bases__ = tuple([TypedObject])
    c = cxx.cstructs()
    c.register("TypedWritable", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 15, 0, ('p', 'TypedWritable$1$TypedWritable', ''), []),
        ('s', 15, 1, ('p', 'TypedWritable$2$TypedWritable', 'p'), ['TypedWritable const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'TypedWritable$14$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'TypedWritable$15$init_type', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(TypedWritable, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(TypedWritable, 'init_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['as_reference_count'] = [
        ('d', 13, 0, ('p', 'TypedWritable$8$as_reference_count', 'p'), []),
    ]
    c.ct['encode_to_bam_stream'] = [
        ('d', 'p', 0, ('p', 'TypedWritable$11$encode_to_bam_stream', 'p'), []),
        ('d', 'B', 2, ('B', 'TypedWritable$12$encode_to_bam_stream', 'ppp'), ['vector_uchar&', 'BamWriter*']),
        ('d', 'B', 1, ('B', 'TypedWritable$13$encode_to_bam_stream', 'pp'), ['vector_uchar&']),
    ]
    c.ct['fillin'] = [
        ('d', 'v', 2, ('v', 'TypedWritable$6$fillin', 'ppp'), ['DatagramIterator&', 'BamReader*']),
    ]
    c.ct['finalize'] = [
        ('d', 'v', 1, ('v', 'TypedWritable$7$finalize', 'pp'), ['BamReader*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'TypedWritable$16$force_init_type', 'p'), []),
    ]
    c.ct['get_bam_modified'] = [
        ('d', 'p', 0, ('p', 'TypedWritable$10$get_bam_modified', 'p'), []),
    ]
    c.ct['mark_bam_modified'] = [
        ('d', 'v', 0, ('v', 'TypedWritable$9$mark_bam_modified', 'p'), []),
    ]
    c.ct['require_fully_complete'] = [
        ('d', 'B', 0, ('B', 'TypedWritable$5$require_fully_complete', 'p'), []),
    ]
    c.ct['update_bam_nested'] = [
        ('d', 'v', 1, ('v', 'TypedWritable$4$update_bam_nested', 'pp'), ['BamWriter*']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'TypedWritable$3$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TypedWritable, attr, self)

TypedWritable.c.link(TypedWritable)



class TypedReferenceCount(TypedObject, ReferenceCount):
    __bases__ = tuple([TypedObject, ReferenceCount])
    c = cxx.cstructs()
    c.register("TypedReferenceCount", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_Thread'] = [
        ('d', 17, 0, ('p', 'TypedReferenceCount$1$downcast_to_Thread', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TypedReferenceCount, attr, self)

TypedReferenceCount.c.link(TypedReferenceCount)



class Thread(TypedReferenceCount, Namable):
    __bases__ = tuple([TypedReferenceCount, Namable])
    c = cxx.cstructs()
    c.register("Thread", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['bind_thread'] = [
        ('s', 17, 2, ('p', 'Thread$3$bind_thread', 'ss'), ['std::string const&', 'std::string const&']),
    ]
    c.ct['consider_yield'] = [
        ('s', 'v', 0, ('v', 'Thread$20$consider_yield', ''), []),
    ]
    c.ct['force_yield'] = [
        ('s', 'v', 0, ('v', 'Thread$19$force_yield', ''), []),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'Thread$35$get_class_type', ''), []),
    ]
    c.ct['get_current_pipeline_stage'] = [
        ('s', 'i', 0, ('i', 'Thread$14$get_current_pipeline_stage', ''), []),
    ]
    c.ct['get_current_thread'] = [
        ('s', 17, 0, ('p', 'Thread$13$get_current_thread', ''), []),
    ]
    c.ct['get_external_thread'] = [
        ('s', 17, 0, ('p', 'Thread$12$get_external_thread', ''), []),
    ]
    c.ct['get_main_thread'] = [
        ('s', 17, 0, ('p', 'Thread$11$get_main_thread', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'Thread$36$init_type', ''), []),
    ]
    c.ct['is_simple_threads'] = [
        ('s', 'B', 0, ('B', 'Thread$17$is_simple_threads', ''), []),
    ]
    c.ct['is_threading_supported'] = [
        ('s', 'B', 0, ('B', 'Thread$15$is_threading_supported', ''), []),
    ]
    c.ct['is_true_threads'] = [
        ('s', 'B', 0, ('B', 'Thread$16$is_true_threads', ''), []),
    ]
    c.ct['prepare_for_exit'] = [
        ('s', 'v', 0, ('v', 'Thread$31$prepare_for_exit', ''), []),
    ]
    c.ct['sleep'] = [
        ('s', 'v', 1, ('v', 'Thread$18$sleep', 'd'), ['double']),
    ]
    c.ct['write_status'] = [
        ('s', 'v', 1, ('v', 'Thread$23$write_status', 'p'), ['std::ostream&']),
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
        ('d', 'i', 0, ('i', 'Thread$38$force_init_type', 'p'), []),
    ]
    c.ct['get_current_task'] = [
        ('d', 16, 0, ('p', 'Thread$29$get_current_task', 'p'), []),
    ]
    c.ct['get_pipeline_stage'] = [
        ('d', 'i', 0, ('i', 'Thread$8$get_pipeline_stage', 'p'), []),
    ]
    c.ct['get_pstats_callback'] = [
        ('d', 'p', 0, ('p', 'Thread$34$get_pstats_callback', 'p'), []),
    ]
    c.ct['get_pstats_index'] = [
        ('d', 'i', 0, ('i', 'Thread$5$get_pstats_index', 'p'), []),
    ]
    c.ct['get_python_index'] = [
        ('d', 'i', 0, ('i', 'Thread$6$get_python_index', 'p'), []),
    ]
    c.ct['get_sync_name'] = [
        ('d', 's', 0, ('s', 'Thread$4$get_sync_name', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'Thread$37$get_type', 'p'), []),
    ]
    c.ct['get_unique_id'] = [
        ('d', 's', 0, ('s', 'Thread$7$get_unique_id', 'p'), []),
    ]
    c.ct['is_joinable'] = [
        ('d', 'B', 0, ('B', 'Thread$25$is_joinable', 'p'), []),
    ]
    c.ct['is_started'] = [
        ('d', 'B', 0, ('B', 'Thread$24$is_started', 'p'), []),
    ]
    c.ct['join'] = [
        ('d', 'v', 0, ('v', 'Thread$27$join', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'Thread$21$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['output_blocker'] = [
        ('d', 'v', 1, ('v', 'Thread$22$output_blocker', 'pp'), ['std::ostream&']),
    ]
    c.ct['preempt'] = [
        ('d', 'v', 0, ('v', 'Thread$28$preempt', 'p'), []),
    ]
    c.ct['set_min_pipeline_stage'] = [
        ('d', 'v', 1, ('v', 'Thread$10$set_min_pipeline_stage', 'pi'), ['int']),
    ]
    c.ct['set_pipeline_stage'] = [
        ('d', 'v', 1, ('v', 'Thread$9$set_pipeline_stage', 'pi'), ['int']),
    ]
    c.ct['set_pstats_callback'] = [
        ('d', 'v', 1, ('v', 'Thread$33$set_pstats_callback', 'pp'), ['Thread::PStatsCallback*']),
    ]
    c.ct['set_pstats_index'] = [
        ('d', 'v', 1, ('v', 'Thread$32$set_pstats_index', 'pi'), ['int']),
    ]
    c.ct['set_python_index'] = [
        ('d', 'v', 1, ('v', 'Thread$30$set_python_index', 'pi'), ['int']),
    ]
    c.ct['start'] = [
        ('d', 'B', 2, ('B', 'Thread$26$start', 'ppB'), ['ThreadPriority', 'bool']),
    ]
    c.ct['upcast_to_Namable'] = [
        ('d', 12, 0, ('p', 'Thread$2$upcast_to_Namable', 'p'), []),
    ]
    c.ct['upcast_to_TypedReferenceCount'] = [
        ('d', 16, 0, ('p', 'Thread$1$upcast_to_TypedReferenceCount', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(Thread, attr, self)

Thread.c.link(Thread)



class TypedWritableReferenceCount(TypedWritable, ReferenceCount):
    __bases__ = tuple([TypedWritable, ReferenceCount])
    c = cxx.cstructs()
    c.register("TypedWritableReferenceCount", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_GeomVertexFormat'] = [
        ('d', 19, 0, ('p', 'TypedWritableReferenceCount$2$downcast_to_GeomVertexFormat', 'p'), []),
    ]
    c.ct['downcast_to_PandaNode'] = [
        ('d', 28, 0, ('p', 'TypedWritableReferenceCount$1$downcast_to_PandaNode', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TypedWritableReferenceCount, attr, self)

TypedWritableReferenceCount.c.link(TypedWritableReferenceCount)



class GeomVertexFormat(TypedWritableReferenceCount, GeomEnums):
    __bases__ = tuple([TypedWritableReferenceCount, GeomEnums])
    c = cxx.cstructs()
    c.register("GeomVertexFormat", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat$3$GeomVertexFormat', ''), []),
        ('s', 19, 1, ('p', 'GeomVertexFormat$4$GeomVertexFormat', 'p'), ['GeomVertexArrayFormat const*']),
        ('s', 19, 1, ('p', 'GeomVertexFormat$5$GeomVertexFormat', 'p'), ['GeomVertexFormat const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'GeomVertexFormat$71$get_class_type', ''), []),
    ]
    c.ct['get_empty'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat$49$get_empty', ''), []),
    ]
    c.ct['get_v3'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat$50$get_v3', ''), []),
    ]
    c.ct['get_v3c4'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat$58$get_v3c4', ''), []),
    ]
    c.ct['get_v3c4t2'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat$59$get_v3c4t2', ''), []),
    ]
    c.ct['get_v3cp'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat$54$get_v3cp', ''), []),
    ]
    c.ct['get_v3cpt2'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat$55$get_v3cpt2', ''), []),
    ]
    c.ct['get_v3n3'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat$51$get_v3n3', ''), []),
    ]
    c.ct['get_v3n3c4'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat$60$get_v3n3c4', ''), []),
    ]
    c.ct['get_v3n3c4t2'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat$61$get_v3n3c4t2', ''), []),
    ]
    c.ct['get_v3n3cp'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat$56$get_v3n3cp', ''), []),
    ]
    c.ct['get_v3n3cpt2'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat$57$get_v3n3cpt2', ''), []),
    ]
    c.ct['get_v3n3t2'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat$53$get_v3n3t2', ''), []),
    ]
    c.ct['get_v3t2'] = [
        ('s', 19, 0, ('p', 'GeomVertexFormat$52$get_v3t2', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'GeomVertexFormat$72$init_type', ''), []),
    ]
    c.ct['register_format'] = [
        ('s', 19, 1, ('p', 'GeomVertexFormat$8$register_format', 'p'), ['GeomVertexArrayFormat const*']),
        ('s', 19, 1, ('p', 'GeomVertexFormat$9$register_format', 'p'), ['GeomVertexFormat const*']),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'GeomVertexFormat$69$register_with_read_factory', ''), []),
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
        ('d', 'p', 1, ('p', 'GeomVertexFormat$19$add_array', 'pp'), ['GeomVertexArrayFormat const*']),
    ]
    c.ct['align_columns_for_animation'] = [
        ('d', 'v', 0, ('v', 'GeomVertexFormat$33$align_columns_for_animation', 'p'), []),
    ]
    c.ct['clear_arrays'] = [
        ('d', 'v', 0, ('v', 'GeomVertexFormat$21$clear_arrays', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'GeomVertexFormat$68$compare_to', 'pp'), ['GeomVertexFormat const&']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'GeomVertexFormat$74$force_init_type', 'p'), []),
    ]
    c.ct['get_animation'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat$10$get_animation', 'p'), []),
    ]
    c.ct['get_array'] = [
        ('d', 'p', 1, ('p', 'GeomVertexFormat$15$get_array', 'pp'), ['std::size_t']),
    ]
    c.ct['get_array_with'] = [
        ('d', 'i', 1, ('i', 'GeomVertexFormat$24$get_array_with', 'ps'), ['InternalName const*']),
        ('d', 'i', 1, ('i', 'GeomVertexFormat$25$get_array_with', 'pp'), ['std::size_t']),
    ]
    c.ct['get_color_array_index'] = [
        ('d', 'i', 0, ('i', 'GeomVertexFormat$66$get_color_array_index', 'p'), []),
    ]
    c.ct['get_color_column'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat$67$get_color_column', 'p'), []),
    ]
    c.ct['get_column'] = [
        ('d', 'p', 1, ('p', 'GeomVertexFormat$26$get_column', 'ps'), ['InternalName const*']),
        ('d', 'p', 1, ('p', 'GeomVertexFormat$27$get_column', 'pp'), ['std::size_t']),
    ]
    c.ct['get_column_name'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat$29$get_column_name', 'pp'), ['std::size_t']),
    ]
    c.ct['get_morph_base'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat$43$get_morph_base', 'pp'), ['std::size_t']),
    ]
    c.ct['get_morph_delta'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat$44$get_morph_delta', 'pp'), ['std::size_t']),
    ]
    c.ct['get_morph_slider'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat$42$get_morph_slider', 'pp'), ['std::size_t']),
    ]
    c.ct['get_normal_array_index'] = [
        ('d', 'i', 0, ('i', 'GeomVertexFormat$64$get_normal_array_index', 'p'), []),
    ]
    c.ct['get_normal_column'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat$65$get_normal_column', 'p'), []),
    ]
    c.ct['get_num_arrays'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat$14$get_num_arrays', 'p'), []),
    ]
    c.ct['get_num_columns'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat$23$get_num_columns', 'p'), []),
    ]
    c.ct['get_num_morphs'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat$41$get_num_morphs', 'p'), []),
    ]
    c.ct['get_num_points'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat$35$get_num_points', 'p'), []),
    ]
    c.ct['get_num_texcoords'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat$39$get_num_texcoords', 'p'), []),
    ]
    c.ct['get_num_vectors'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat$37$get_num_vectors', 'p'), []),
    ]
    c.ct['get_point'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat$36$get_point', 'pp'), ['std::size_t']),
    ]
    c.ct['get_post_animated_format'] = [
        ('d', 19, 0, ('p', 'GeomVertexFormat$12$get_post_animated_format', 'p'), []),
    ]
    c.ct['get_texcoord'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat$40$get_texcoord', 'pp'), ['std::size_t']),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'GeomVertexFormat$73$get_type', 'p'), []),
    ]
    c.ct['get_union_format'] = [
        ('d', 19, 1, ('p', 'GeomVertexFormat$13$get_union_format', 'pp'), ['GeomVertexFormat const*']),
    ]
    c.ct['get_vector'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat$38$get_vector', 'pp'), ['std::size_t']),
    ]
    c.ct['get_vertex_array_index'] = [
        ('d', 'i', 0, ('i', 'GeomVertexFormat$62$get_vertex_array_index', 'p'), []),
    ]
    c.ct['get_vertex_column'] = [
        ('d', 'p', 0, ('p', 'GeomVertexFormat$63$get_vertex_column', 'p'), []),
    ]
    c.ct['has_column'] = [
        ('d', 'B', 1, ('B', 'GeomVertexFormat$28$has_column', 'ps'), ['InternalName const*']),
    ]
    c.ct['insert_array'] = [
        ('d', 'v', 2, ('v', 'GeomVertexFormat$20$insert_array', 'ppp'), ['std::size_t', 'GeomVertexArrayFormat const*']),
    ]
    c.ct['is_registered'] = [
        ('d', 'B', 0, ('B', 'GeomVertexFormat$7$is_registered', 'p'), []),
    ]
    c.ct['maybe_align_columns_for_animation'] = [
        ('d', 'v', 0, ('v', 'GeomVertexFormat$34$maybe_align_columns_for_animation', 'p'), []),
    ]
    c.ct['modify_array'] = [
        ('d', 'p', 1, ('p', 'GeomVertexFormat$16$modify_array', 'pp'), ['std::size_t']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'GeomVertexFormat$45$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['pack_columns'] = [
        ('d', 'v', 0, ('v', 'GeomVertexFormat$32$pack_columns', 'p'), []),
    ]
    c.ct['remove_array'] = [
        ('d', 'v', 1, ('v', 'GeomVertexFormat$18$remove_array', 'pp'), ['std::size_t']),
    ]
    c.ct['remove_column'] = [
        ('d', 'v', 2, ('v', 'GeomVertexFormat$30$remove_column', 'psB'), ['InternalName const*', 'bool']),
        ('d', 'v', 1, ('v', 'GeomVertexFormat$31$remove_column', 'ps'), ['InternalName const*']),
    ]
    c.ct['remove_empty_arrays'] = [
        ('d', 'v', 0, ('v', 'GeomVertexFormat$22$remove_empty_arrays', 'p'), []),
    ]
    c.ct['set_animation'] = [
        ('d', 'v', 1, ('v', 'GeomVertexFormat$11$set_animation', 'pp'), ['GeomVertexAnimationSpec const&']),
    ]
    c.ct['set_array'] = [
        ('d', 'v', 2, ('v', 'GeomVertexFormat$17$set_array', 'ppp'), ['std::size_t', 'GeomVertexArrayFormat const*']),
    ]
    c.ct['unref'] = [
        ('d', 'B', 0, ('B', 'GeomVertexFormat$6$unref', 'p'), []),
    ]
    c.ct['upcast_to_GeomEnums'] = [
        ('d', 3, 0, ('p', 'GeomVertexFormat$2$upcast_to_GeomEnums', 'p'), []),
    ]
    c.ct['upcast_to_TypedWritableReferenceCount'] = [
        ('d', 18, 0, ('p', 'GeomVertexFormat$1$upcast_to_TypedWritableReferenceCount', 'p'), []),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'GeomVertexFormat$46$write', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'v', 1, ('v', 'GeomVertexFormat$47$write', 'pp'), ['std::ostream&']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'GeomVertexFormat$70$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]
    c.ct['write_with_data'] = [
        ('d', 'v', 3, ('v', 'GeomVertexFormat$48$write_with_data', 'ppip'), ['std::ostream&', 'int', 'GeomVertexData const*']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomVertexFormat, attr, self)

GeomVertexFormat.c.link(GeomVertexFormat)



class WindowFramework(TypedWritableReferenceCount):
    __bases__ = tuple([TypedWritableReferenceCount])
    c = cxx.cstructs()
    c.register("WindowFramework", "upanda3d", """libupanda3d_c.so""")

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
        ('s', 20, 1, ('p', 'WindowFramework$52$WindowFramework', 'p'), ['WindowFramework const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'WindowFramework$48$get_class_type', ''), []),
    ]
    c.ct['get_shuttle_controls_font'] = [
        ('s', 'p', 0, ('p', 'WindowFramework$46$get_shuttle_controls_font', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'WindowFramework$49$init_type', ''), []),
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
        ('d', 'v', 0, ('v', 'WindowFramework$27$adjust_dimensions', 'p'), []),
    ]
    c.ct['center_trackball'] = [
        ('d', 'v', 1, ('v', 'WindowFramework$17$center_trackball', 'pp'), ['NodePath const&']),
    ]
    c.ct['enable_keyboard'] = [
        ('d', 'v', 0, ('v', 'WindowFramework$15$enable_keyboard', 'p'), []),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'WindowFramework$51$force_init_type', 'p'), []),
    ]
    c.ct['get_anim_controls'] = [
        ('d', 'B', 0, ('B', 'WindowFramework$26$get_anim_controls', 'p'), []),
    ]
    c.ct['get_aspect_2d'] = [
        ('d', 7, 0, ('p', 'WindowFramework$11$get_aspect_2d', 'p'), []),
    ]
    c.ct['get_background_type'] = [
        ('d', 'p', 0, ('p', 'WindowFramework$45$get_background_type', 'p'), []),
    ]
    c.ct['get_button_thrower'] = [
        ('d', 7, 0, ('p', 'WindowFramework$14$get_button_thrower', 'p'), []),
    ]
    c.ct['get_camera'] = [
        ('d', 30, 1, ('p', 'WindowFramework$6$get_camera', 'pi'), ['int']),
    ]
    c.ct['get_camera_group'] = [
        ('d', 7, 0, ('p', 'WindowFramework$4$get_camera_group', 'p'), []),
    ]
    c.ct['get_display_region_2d'] = [
        ('d', 'p', 0, ('p', 'WindowFramework$7$get_display_region_2d', 'p'), []),
    ]
    c.ct['get_display_region_3d'] = [
        ('d', 'p', 0, ('p', 'WindowFramework$8$get_display_region_3d', 'p'), []),
    ]
    c.ct['get_graphics_output'] = [
        ('d', 'p', 0, ('p', 'WindowFramework$3$get_graphics_output', 'p'), []),
    ]
    c.ct['get_graphics_window'] = [
        ('d', 'p', 0, ('p', 'WindowFramework$2$get_graphics_window', 'p'), []),
    ]
    c.ct['get_lighting'] = [
        ('d', 'B', 0, ('B', 'WindowFramework$43$get_lighting', 'p'), []),
    ]
    c.ct['get_mouse'] = [
        ('d', 7, 0, ('p', 'WindowFramework$13$get_mouse', 'p'), []),
    ]
    c.ct['get_num_cameras'] = [
        ('d', 'i', 0, ('i', 'WindowFramework$5$get_num_cameras', 'p'), []),
    ]
    c.ct['get_one_sided_reverse'] = [
        ('d', 'B', 0, ('B', 'WindowFramework$42$get_one_sided_reverse', 'p'), []),
    ]
    c.ct['get_panda_framework'] = [
        ('d', 9, 0, ('p', 'WindowFramework$1$get_panda_framework', 'p'), []),
    ]
    c.ct['get_perpixel'] = [
        ('d', 'B', 0, ('B', 'WindowFramework$44$get_perpixel', 'p'), []),
    ]
    c.ct['get_pixel_2d'] = [
        ('d', 7, 0, ('p', 'WindowFramework$12$get_pixel_2d', 'p'), []),
    ]
    c.ct['get_render'] = [
        ('d', 7, 0, ('p', 'WindowFramework$9$get_render', 'p'), []),
    ]
    c.ct['get_render_2d'] = [
        ('d', 7, 0, ('p', 'WindowFramework$10$get_render_2d', 'p'), []),
    ]
    c.ct['get_texture'] = [
        ('d', 'B', 0, ('B', 'WindowFramework$40$get_texture', 'p'), []),
    ]
    c.ct['get_two_sided'] = [
        ('d', 'B', 0, ('B', 'WindowFramework$41$get_two_sided', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'WindowFramework$50$get_type', 'p'), []),
    ]
    c.ct['get_wireframe'] = [
        ('d', 'B', 0, ('B', 'WindowFramework$38$get_wireframe', 'p'), []),
    ]
    c.ct['get_wireframe_filled'] = [
        ('d', 'B', 0, ('B', 'WindowFramework$39$get_wireframe_filled', 'p'), []),
    ]
    c.ct['load_default_model'] = [
        ('d', 7, 1, ('p', 'WindowFramework$20$load_default_model', 'pp'), ['NodePath const&']),
    ]
    c.ct['load_model'] = [
        ('d', 7, 2, ('p', 'WindowFramework$19$load_model', 'ppp'), ['NodePath const&', 'Filename']),
    ]
    c.ct['load_models'] = [
        ('d', 'B', 2, ('B', 'WindowFramework$18$load_models', 'ppp'), ['NodePath const&', 'pvector< Filename > const&']),
    ]
    c.ct['loop_animations'] = [
        ('d', 'v', 1, ('v', 'WindowFramework$21$loop_animations', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'WindowFramework$22$loop_animations', 'p'), []),
    ]
    c.ct['make_camera'] = [
        ('d', 7, 0, ('p', 'WindowFramework$47$make_camera', 'p'), []),
    ]
    c.ct['next_anim_control'] = [
        ('d', 'v', 0, ('v', 'WindowFramework$24$next_anim_control', 'p'), []),
    ]
    c.ct['set_anim_controls'] = [
        ('d', 'v', 1, ('v', 'WindowFramework$25$set_anim_controls', 'pB'), ['bool']),
    ]
    c.ct['set_background_type'] = [
        ('d', 'v', 1, ('v', 'WindowFramework$37$set_background_type', 'pp'), ['WindowFramework::BackgroundType']),
    ]
    c.ct['set_lighting'] = [
        ('d', 'v', 1, ('v', 'WindowFramework$35$set_lighting', 'pB'), ['bool']),
    ]
    c.ct['set_one_sided_reverse'] = [
        ('d', 'v', 1, ('v', 'WindowFramework$34$set_one_sided_reverse', 'pB'), ['bool']),
    ]
    c.ct['set_perpixel'] = [
        ('d', 'v', 1, ('v', 'WindowFramework$36$set_perpixel', 'pB'), ['bool']),
    ]
    c.ct['set_texture'] = [
        ('d', 'v', 1, ('v', 'WindowFramework$32$set_texture', 'pB'), ['bool']),
    ]
    c.ct['set_two_sided'] = [
        ('d', 'v', 1, ('v', 'WindowFramework$33$set_two_sided', 'pB'), ['bool']),
    ]
    c.ct['set_wireframe'] = [
        ('d', 'v', 2, ('v', 'WindowFramework$30$set_wireframe', 'pBB'), ['bool', 'bool']),
        ('d', 'v', 1, ('v', 'WindowFramework$31$set_wireframe', 'pB'), ['bool']),
    ]
    c.ct['setup_trackball'] = [
        ('d', 'v', 0, ('v', 'WindowFramework$16$setup_trackball', 'p'), []),
    ]
    c.ct['split_window'] = [
        ('d', 20, 1, ('p', 'WindowFramework$28$split_window', 'pp'), ['WindowFramework::SplitType']),
        ('d', 20, 0, ('p', 'WindowFramework$29$split_window', 'p'), []),
    ]
    c.ct['stagger_animations'] = [
        ('d', 'v', 0, ('v', 'WindowFramework$23$stagger_animations', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(WindowFramework, attr, self)

WindowFramework.c.link(WindowFramework)



class InternalName(TypedWritableReferenceCount):
    __bases__ = tuple([TypedWritableReferenceCount])
    c = cxx.cstructs()
    c.register("InternalName", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['get_aspect_ratio'] = [
        ('s', 'p', 0, ('p', 'InternalName$26$get_aspect_ratio', ''), []),
    ]
    c.ct['get_binormal'] = [
        ('s', 'p', 0, ('p', 'InternalName$19$get_binormal', ''), []),
    ]
    c.ct['get_binormal_name'] = [
        ('s', 'p', 1, ('p', 'InternalName$20$get_binormal_name', 's'), ['std::string const&']),
    ]
    c.ct['get_camera'] = [
        ('s', 'p', 0, ('p', 'InternalName$33$get_camera', ''), []),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'InternalName$39$get_class_type', ''), []),
    ]
    c.ct['get_color'] = [
        ('s', 'p', 0, ('p', 'InternalName$23$get_color', ''), []),
    ]
    c.ct['get_error'] = [
        ('s', 'p', 0, ('p', 'InternalName$14$get_error', ''), []),
    ]
    c.ct['get_index'] = [
        ('s', 'p', 0, ('p', 'InternalName$31$get_index', ''), []),
    ]
    c.ct['get_model'] = [
        ('s', 'p', 0, ('p', 'InternalName$34$get_model', ''), []),
    ]
    c.ct['get_morph'] = [
        ('s', 'p', 2, ('p', 'InternalName$30$get_morph', 'ps'), ['InternalName*', 'std::string const&']),
    ]
    c.ct['get_normal'] = [
        ('s', 'p', 0, ('p', 'InternalName$16$get_normal', ''), []),
    ]
    c.ct['get_root'] = [
        ('s', 'p', 0, ('p', 'InternalName$13$get_root', ''), []),
    ]
    c.ct['get_rotate'] = [
        ('s', 'p', 0, ('p', 'InternalName$24$get_rotate', ''), []),
    ]
    c.ct['get_size'] = [
        ('s', 'p', 0, ('p', 'InternalName$25$get_size', ''), []),
    ]
    c.ct['get_tangent'] = [
        ('s', 'p', 0, ('p', 'InternalName$17$get_tangent', ''), []),
    ]
    c.ct['get_tangent_name'] = [
        ('s', 'p', 1, ('p', 'InternalName$18$get_tangent_name', 's'), ['std::string const&']),
    ]
    c.ct['get_texcoord'] = [
        ('s', 'p', 0, ('p', 'InternalName$21$get_texcoord', ''), []),
    ]
    c.ct['get_texcoord_name'] = [
        ('s', 'p', 1, ('p', 'InternalName$22$get_texcoord_name', 's'), ['std::string const&']),
    ]
    c.ct['get_transform_blend'] = [
        ('s', 'p', 0, ('p', 'InternalName$27$get_transform_blend', ''), []),
    ]
    c.ct['get_transform_index'] = [
        ('s', 'p', 0, ('p', 'InternalName$29$get_transform_index', ''), []),
    ]
    c.ct['get_transform_weight'] = [
        ('s', 'p', 0, ('p', 'InternalName$28$get_transform_weight', ''), []),
    ]
    c.ct['get_vertex'] = [
        ('s', 'p', 0, ('p', 'InternalName$15$get_vertex', ''), []),
    ]
    c.ct['get_view'] = [
        ('s', 'p', 0, ('p', 'InternalName$35$get_view', ''), []),
    ]
    c.ct['get_world'] = [
        ('s', 'p', 0, ('p', 'InternalName$32$get_world', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'InternalName$40$init_type', ''), []),
    ]
    c.ct['make'] = [
        ('s', 'p', 1, ('p', 'InternalName$1$make', 's'), ['std::string const&']),
        ('s', 'p', 2, ('p', 'InternalName$2$make', 'si'), ['std::string const&', 'int']),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'InternalName$36$register_with_read_factory', ''), []),
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
        ('d', 'p', 1, ('p', 'InternalName$3$append', 'ps'), ['std::string const&']),
    ]
    c.ct['finalize'] = [
        ('d', 'v', 1, ('v', 'InternalName$38$finalize', 'pp'), ['BamReader*']),
    ]
    c.ct['find_ancestor'] = [
        ('d', 'i', 1, ('i', 'InternalName$8$find_ancestor', 'ss'), ['std::string const&']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'InternalName$42$force_init_type', 'p'), []),
    ]
    c.ct['get_ancestor'] = [
        ('d', 's', 1, ('s', 'InternalName$9$get_ancestor', 'si'), ['int']),
    ]
    c.ct['get_basename'] = [
        ('d', 's', 0, ('s', 'InternalName$7$get_basename', 'p'), []),
    ]
    c.ct['get_name'] = [
        ('d', 's', 0, ('s', 'InternalName$5$get_name', 'p'), []),
    ]
    c.ct['get_net_basename'] = [
        ('d', 's', 1, ('s', 'InternalName$11$get_net_basename', 'si'), ['int']),
    ]
    c.ct['get_parent'] = [
        ('d', 21, 0, ('p', 'InternalName$4$get_parent', 'p'), []),
    ]
    c.ct['get_top'] = [
        ('d', 's', 0, ('s', 'InternalName$10$get_top', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'InternalName$41$get_type', 'p'), []),
    ]
    c.ct['join'] = [
        ('d', 's', 1, ('s', 'InternalName$6$join', 'ss'), ['std::string const&']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'InternalName$12$output', 'sp'), ['std::ostream&']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'InternalName$37$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(InternalName, attr, self)

InternalName.c.link(InternalName)



class CachedTypedWritableReferenceCount(TypedWritableReferenceCount):
    __bases__ = tuple([TypedWritableReferenceCount])
    c = cxx.cstructs()
    c.register("CachedTypedWritableReferenceCount", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'CachedTypedWritableReferenceCount$6$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'CachedTypedWritableReferenceCount$7$init_type', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(CachedTypedWritableReferenceCount, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(CachedTypedWritableReferenceCount, 'init_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['cache_ref'] = [
        ('d', 'v', 0, ('v', 'CachedTypedWritableReferenceCount$2$cache_ref', 'p'), []),
    ]
    c.ct['cache_ref_only'] = [
        ('d', 'v', 0, ('v', 'CachedTypedWritableReferenceCount$5$cache_ref_only', 'p'), []),
    ]
    c.ct['cache_unref'] = [
        ('d', 'B', 0, ('B', 'CachedTypedWritableReferenceCount$3$cache_unref', 'p'), []),
    ]
    c.ct['get_cache_ref_count'] = [
        ('d', 'i', 0, ('i', 'CachedTypedWritableReferenceCount$1$get_cache_ref_count', 'p'), []),
    ]
    c.ct['test_ref_count_integrity'] = [
        ('d', 'B', 0, ('B', 'CachedTypedWritableReferenceCount$4$test_ref_count_integrity', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(CachedTypedWritableReferenceCount, attr, self)

CachedTypedWritableReferenceCount.c.link(CachedTypedWritableReferenceCount)



class CopyOnWriteObject(CachedTypedWritableReferenceCount):
    __bases__ = tuple([CachedTypedWritableReferenceCount])
    c = cxx.cstructs()
    c.register("CopyOnWriteObject", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_Geom'] = [
        ('d', 27, 0, ('p', 'CopyOnWriteObject$1$downcast_to_Geom', 'p'), []),
    ]
    c.ct['downcast_to_GeomPrimitive'] = [
        ('d', 25, 0, ('p', 'CopyOnWriteObject$2$downcast_to_GeomPrimitive', 'p'), []),
    ]
    c.ct['downcast_to_GeomVertexData'] = [
        ('d', 24, 0, ('p', 'CopyOnWriteObject$3$downcast_to_GeomVertexData', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(CopyOnWriteObject, attr, self)

CopyOnWriteObject.c.link(CopyOnWriteObject)



class GeomVertexData(CopyOnWriteObject, GeomEnums):
    __bases__ = tuple([CopyOnWriteObject, GeomEnums])
    c = cxx.cstructs()
    c.register("GeomVertexData", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 24, 1, ('p', 'GeomVertexData$3$GeomVertexData', 'p'), ['GeomVertexData const&']),
        ('s', 24, 2, ('p', 'GeomVertexData$4$GeomVertexData', 'pp'), ['GeomVertexData const&', 'GeomVertexFormat const*']),
        ('s', 24, 3, ('p', 'GeomVertexData$5$GeomVertexData', 'spp'), ['std::string const&', 'GeomVertexFormat const*', 'GeomEnums::UsageHint']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'GeomVertexData$74$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'GeomVertexData$75$init_type', ''), []),
    ]
    c.ct['pack_abcd'] = [
        ('s', 'I', 4, ('I', 'GeomVertexData$61$pack_abcd', 'IIII'), ['unsigned int', 'unsigned int', 'unsigned int', 'unsigned int']),
    ]
    c.ct['pack_ufloat'] = [
        ('s', 'I', 3, ('I', 'GeomVertexData$66$pack_ufloat', 'fff'), ['float', 'float', 'float']),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'GeomVertexData$70$register_with_read_factory', ''), []),
    ]
    c.ct['unpack_abcd_a'] = [
        ('s', 'I', 1, ('I', 'GeomVertexData$62$unpack_abcd_a', 'I'), ['uint32_t']),
    ]
    c.ct['unpack_abcd_b'] = [
        ('s', 'I', 1, ('I', 'GeomVertexData$63$unpack_abcd_b', 'I'), ['uint32_t']),
    ]
    c.ct['unpack_abcd_c'] = [
        ('s', 'I', 1, ('I', 'GeomVertexData$64$unpack_abcd_c', 'I'), ['uint32_t']),
    ]
    c.ct['unpack_abcd_d'] = [
        ('s', 'I', 1, ('I', 'GeomVertexData$65$unpack_abcd_d', 'I'), ['uint32_t']),
    ]
    c.ct['unpack_ufloat_a'] = [
        ('s', 'f', 1, ('f', 'GeomVertexData$67$unpack_ufloat_a', 'I'), ['uint32_t']),
    ]
    c.ct['unpack_ufloat_b'] = [
        ('s', 'f', 1, ('f', 'GeomVertexData$68$unpack_ufloat_b', 'I'), ['uint32_t']),
    ]
    c.ct['unpack_ufloat_c'] = [
        ('s', 'f', 1, ('f', 'GeomVertexData$69$unpack_ufloat_c', 'I'), ['uint32_t']),
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
        ('d', 24, 2, ('p', 'GeomVertexData$49$animate_vertices', 'pBp'), ['bool', 'Thread*']),
    ]
    c.ct['clear_animated_vertices'] = [
        ('d', 'v', 0, ('v', 'GeomVertexData$50$clear_animated_vertices', 'p'), []),
    ]
    c.ct['clear_cache'] = [
        ('d', 'v', 0, ('v', 'GeomVertexData$59$clear_cache', 'p'), []),
    ]
    c.ct['clear_cache_stage'] = [
        ('d', 'v', 0, ('v', 'GeomVertexData$60$clear_cache_stage', 'p'), []),
    ]
    c.ct['clear_rows'] = [
        ('d', 'v', 0, ('v', 'GeomVertexData$19$clear_rows', 'p'), []),
    ]
    c.ct['clear_slider_table'] = [
        ('d', 'v', 0, ('v', 'GeomVertexData$35$clear_slider_table', 'p'), []),
    ]
    c.ct['clear_transform_blend_table'] = [
        ('d', 'v', 0, ('v', 'GeomVertexData$32$clear_transform_blend_table', 'p'), []),
    ]
    c.ct['clear_transform_table'] = [
        ('d', 'v', 0, ('v', 'GeomVertexData$28$clear_transform_table', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'GeomVertexData$6$compare_to', 'pp'), ['GeomVertexData const&']),
    ]
    c.ct['convert_to'] = [
        ('d', 24, 1, ('p', 'GeomVertexData$43$convert_to', 'pp'), ['GeomVertexFormat const*']),
    ]
    c.ct['copy_from'] = [
        ('d', 'v', 3, ('v', 'GeomVertexData$40$copy_from', 'ppBp'), ['GeomVertexData const*', 'bool', 'Thread*']),
        ('d', 'v', 2, ('v', 'GeomVertexData$41$copy_from', 'ppB'), ['GeomVertexData const*', 'bool']),
    ]
    c.ct['copy_row_from'] = [
        ('d', 'v', 4, ('v', 'GeomVertexData$42$copy_row_from', 'pipip'), ['int', 'GeomVertexData const*', 'int', 'Thread*']),
    ]
    c.ct['describe_vertex'] = [
        ('d', 'v', 2, ('v', 'GeomVertexData$58$describe_vertex', 'ppi'), ['std::ostream&', 'int']),
    ]
    c.ct['finalize'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData$73$finalize', 'pp'), ['BamReader*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'GeomVertexData$77$force_init_type', 'p'), []),
    ]
    c.ct['get_array'] = [
        ('d', 'p', 1, ('p', 'GeomVertexData$21$get_array', 'pp'), ['std::size_t']),
    ]
    c.ct['get_array_handle'] = [
        ('d', 'p', 1, ('p', 'GeomVertexData$22$get_array_handle', 'pp'), ['std::size_t']),
    ]
    c.ct['get_format'] = [
        ('d', 19, 0, ('p', 'GeomVertexData$11$get_format', 'p'), []),
    ]
    c.ct['get_modified'] = [
        ('d', 'p', 1, ('p', 'GeomVertexData$37$get_modified', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'GeomVertexData$38$get_modified', 'p'), []),
    ]
    c.ct['get_name'] = [
        ('d', 's', 0, ('s', 'GeomVertexData$7$get_name', 'p'), []),
    ]
    c.ct['get_num_arrays'] = [
        ('d', 'p', 0, ('p', 'GeomVertexData$20$get_num_arrays', 'p'), []),
    ]
    c.ct['get_num_bytes'] = [
        ('d', 'i', 0, ('i', 'GeomVertexData$36$get_num_bytes', 'p'), []),
    ]
    c.ct['get_num_rows'] = [
        ('d', 'i', 0, ('i', 'GeomVertexData$15$get_num_rows', 'p'), []),
    ]
    c.ct['get_slider_table'] = [
        ('d', 'p', 0, ('p', 'GeomVertexData$33$get_slider_table', 'p'), []),
    ]
    c.ct['get_transform_blend_table'] = [
        ('d', 'p', 0, ('p', 'GeomVertexData$29$get_transform_blend_table', 'p'), []),
    ]
    c.ct['get_transform_table'] = [
        ('d', 'p', 0, ('p', 'GeomVertexData$26$get_transform_table', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'GeomVertexData$76$get_type', 'p'), []),
    ]
    c.ct['get_usage_hint'] = [
        ('d', 'p', 0, ('p', 'GeomVertexData$9$get_usage_hint', 'p'), []),
    ]
    c.ct['has_column'] = [
        ('d', 'B', 1, ('B', 'GeomVertexData$14$has_column', 'ps'), ['InternalName const*']),
    ]
    c.ct['modify_array'] = [
        ('d', 'p', 1, ('p', 'GeomVertexData$23$modify_array', 'pp'), ['std::size_t']),
    ]
    c.ct['modify_array_handle'] = [
        ('d', 'p', 1, ('p', 'GeomVertexData$24$modify_array_handle', 'pp'), ['std::size_t']),
    ]
    c.ct['modify_transform_blend_table'] = [
        ('d', 'p', 0, ('p', 'GeomVertexData$30$modify_transform_blend_table', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData$55$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['replace_column'] = [
        ('d', 24, 4, ('p', 'GeomVertexData$54$replace_column', 'ppipp'), ['InternalName*', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents']),
    ]
    c.ct['request_resident'] = [
        ('d', 'B', 0, ('B', 'GeomVertexData$39$request_resident', 'p'), []),
    ]
    c.ct['require_fully_complete'] = [
        ('d', 'B', 0, ('B', 'GeomVertexData$72$require_fully_complete', 'p'), []),
    ]
    c.ct['reserve_num_rows'] = [
        ('d', 'B', 1, ('B', 'GeomVertexData$18$reserve_num_rows', 'pi'), ['int']),
    ]
    c.ct['reverse_normals'] = [
        ('d', 24, 0, ('p', 'GeomVertexData$48$reverse_normals', 'p'), []),
    ]
    c.ct['scale_color'] = [
        ('d', 24, 1, ('p', 'GeomVertexData$44$scale_color', 'pp'), ['LVecBase4 const&']),
        ('d', 24, 4, ('p', 'GeomVertexData$45$scale_color', 'ppipp'), ['LVecBase4 const&', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents']),
    ]
    c.ct['set_array'] = [
        ('d', 'v', 2, ('v', 'GeomVertexData$25$set_array', 'ppp'), ['std::size_t', 'GeomVertexArrayData const*']),
    ]
    c.ct['set_color'] = [
        ('d', 24, 1, ('p', 'GeomVertexData$46$set_color', 'pp'), ['LColor const&']),
        ('d', 24, 4, ('p', 'GeomVertexData$47$set_color', 'ppipp'), ['LColor const&', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents']),
    ]
    c.ct['set_format'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData$12$set_format', 'pp'), ['GeomVertexFormat const*']),
    ]
    c.ct['set_name'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData$8$set_name', 'ps'), ['std::string const&']),
    ]
    c.ct['set_num_rows'] = [
        ('d', 'B', 1, ('B', 'GeomVertexData$16$set_num_rows', 'pi'), ['int']),
    ]
    c.ct['set_slider_table'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData$34$set_slider_table', 'pp'), ['SliderTable const*']),
    ]
    c.ct['set_transform_blend_table'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData$31$set_transform_blend_table', 'pp'), ['TransformBlendTable const*']),
    ]
    c.ct['set_transform_table'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData$27$set_transform_table', 'pp'), ['TransformTable const*']),
    ]
    c.ct['set_usage_hint'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData$10$set_usage_hint', 'pp'), ['GeomEnums::UsageHint']),
    ]
    c.ct['transform_vertices'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData$51$transform_vertices', 'pp'), ['LMatrix4 const&']),
        ('d', 'v', 2, ('v', 'GeomVertexData$52$transform_vertices', 'ppp'), ['LMatrix4 const&', 'SparseArray const&']),
        ('d', 'v', 3, ('v', 'GeomVertexData$53$transform_vertices', 'ppii'), ['LMatrix4 const&', 'int', 'int']),
    ]
    c.ct['unclean_set_format'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData$13$unclean_set_format', 'pp'), ['GeomVertexFormat const*']),
    ]
    c.ct['unclean_set_num_rows'] = [
        ('d', 'B', 1, ('B', 'GeomVertexData$17$unclean_set_num_rows', 'pi'), ['int']),
    ]
    c.ct['upcast_to_CopyOnWriteObject'] = [
        ('d', 23, 0, ('p', 'GeomVertexData$1$upcast_to_CopyOnWriteObject', 'p'), []),
    ]
    c.ct['upcast_to_GeomEnums'] = [
        ('d', 3, 0, ('p', 'GeomVertexData$2$upcast_to_GeomEnums', 'p'), []),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'GeomVertexData$56$write', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'v', 1, ('v', 'GeomVertexData$57$write', 'pp'), ['std::ostream&']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'GeomVertexData$71$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomVertexData, attr, self)

GeomVertexData.c.link(GeomVertexData)



class GeomPrimitive(CopyOnWriteObject, GeomEnums):
    __bases__ = tuple([CopyOnWriteObject, GeomEnums])
    c = cxx.cstructs()
    c.register("GeomPrimitive", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'GeomPrimitive$91$get_class_type', ''), []),
    ]
    c.ct['get_index_format'] = [
        ('s', 'p', 0, ('p', 'GeomPrimitive$85$get_index_format', 'p'), []),
        ('s', 'p', 1, ('p', 'GeomPrimitive$86$get_index_format', 'p'), ['GeomEnums::NumericType']),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'GeomPrimitive$92$init_type', ''), []),
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
        ('d', 'v', 2, ('v', 'GeomPrimitive$21$add_consecutive_vertices', 'pii'), ['int', 'int']),
    ]
    c.ct['add_next_vertices'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive$22$add_next_vertices', 'pi'), ['int']),
    ]
    c.ct['add_vertex'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive$17$add_vertex', 'pi'), ['int']),
    ]
    c.ct['add_vertices'] = [
        ('d', 'v', 2, ('v', 'GeomPrimitive$18$add_vertices', 'pii'), ['int', 'int']),
        ('d', 'v', 3, ('v', 'GeomPrimitive$19$add_vertices', 'piii'), ['int', 'int', 'int']),
        ('d', 'v', 4, ('v', 'GeomPrimitive$20$add_vertices', 'piiii'), ['int', 'int', 'int', 'int']),
    ]
    c.ct['check_valid'] = [
        ('d', 'B', 1, ('B', 'GeomPrimitive$56$check_valid', 'pp'), ['GeomVertexData const*']),
        ('d', 'B', 1, ('B', 'GeomPrimitive$57$check_valid', 'pp'), ['GeomVertexDataPipelineReader const*']),
    ]
    c.ct['clear_minmax'] = [
        ('d', 'v', 0, ('v', 'GeomPrimitive$76$clear_minmax', 'p'), []),
    ]
    c.ct['clear_vertices'] = [
        ('d', 'v', 0, ('v', 'GeomPrimitive$25$clear_vertices', 'p'), []),
    ]
    c.ct['close_primitive'] = [
        ('d', 'B', 0, ('B', 'GeomPrimitive$24$close_primitive', 'p'), []),
    ]
    c.ct['decompose'] = [
        ('d', 25, 0, ('p', 'GeomPrimitive$42$decompose', 'p'), []),
    ]
    c.ct['doubleside'] = [
        ('d', 25, 0, ('p', 'GeomPrimitive$44$doubleside', 'p'), []),
    ]
    c.ct['draw'] = [
        ('d', 'B', 3, ('B', 'GeomPrimitive$88$draw', 'pppB'), ['GraphicsStateGuardianBase*', 'GeomPrimitivePipelineReader const*', 'bool']),
    ]
    c.ct['finalize'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive$90$finalize', 'pp'), ['BamReader*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$94$force_init_type', 'p'), []),
    ]
    c.ct['get_data_size_bytes'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$52$get_data_size_bytes', 'p'), []),
    ]
    c.ct['get_ends'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive$70$get_ends', 'p'), []),
    ]
    c.ct['get_first_vertex'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$14$get_first_vertex', 'p'), []),
    ]
    c.ct['get_geom_rendering'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$5$get_geom_rendering', 'p'), []),
    ]
    c.ct['get_index_format'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive$85$get_index_format', 'p'), []),
        ('d', 'p', 1, ('p', 'GeomPrimitive$86$get_index_format', 'p'), ['GeomEnums::NumericType']),
    ]
    c.ct['get_index_stride'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$68$get_index_stride', 'p'), []),
    ]
    c.ct['get_index_type'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive$10$get_index_type', 'p'), []),
    ]
    c.ct['get_max_vertex'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$40$get_max_vertex', 'p'), []),
    ]
    c.ct['get_maxs'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive$74$get_maxs', 'p'), []),
    ]
    c.ct['get_min_num_vertices_per_primitive'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$78$get_min_num_vertices_per_primitive', 'p'), []),
    ]
    c.ct['get_min_vertex'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$38$get_min_vertex', 'p'), []),
    ]
    c.ct['get_mins'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive$73$get_mins', 'p'), []),
    ]
    c.ct['get_modified'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive$53$get_modified', 'p'), []),
    ]
    c.ct['get_num_bytes'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$51$get_num_bytes', 'p'), []),
    ]
    c.ct['get_num_faces'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$36$get_num_faces', 'p'), []),
    ]
    c.ct['get_num_primitives'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$31$get_num_primitives', 'p'), []),
    ]
    c.ct['get_num_unused_vertices_per_primitive'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$79$get_num_unused_vertices_per_primitive', 'p'), []),
    ]
    c.ct['get_num_used_vertices'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$35$get_num_used_vertices', 'p'), []),
    ]
    c.ct['get_num_vertices'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$15$get_num_vertices', 'p'), []),
    ]
    c.ct['get_num_vertices_per_primitive'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$77$get_num_vertices_per_primitive', 'p'), []),
    ]
    c.ct['get_primitive_end'] = [
        ('d', 'i', 1, ('i', 'GeomPrimitive$33$get_primitive_end', 'pi'), ['int']),
    ]
    c.ct['get_primitive_max_vertex'] = [
        ('d', 'i', 1, ('i', 'GeomPrimitive$41$get_primitive_max_vertex', 'pi'), ['int']),
    ]
    c.ct['get_primitive_min_vertex'] = [
        ('d', 'i', 1, ('i', 'GeomPrimitive$39$get_primitive_min_vertex', 'pi'), ['int']),
    ]
    c.ct['get_primitive_num_faces'] = [
        ('d', 'i', 1, ('i', 'GeomPrimitive$37$get_primitive_num_faces', 'pi'), ['int']),
    ]
    c.ct['get_primitive_num_vertices'] = [
        ('d', 'i', 1, ('i', 'GeomPrimitive$34$get_primitive_num_vertices', 'pi'), ['int']),
    ]
    c.ct['get_primitive_start'] = [
        ('d', 'i', 1, ('i', 'GeomPrimitive$32$get_primitive_start', 'pi'), ['int']),
    ]
    c.ct['get_primitive_type'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive$4$get_primitive_type', 'p'), []),
    ]
    c.ct['get_shade_model'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive$6$get_shade_model', 'p'), []),
    ]
    c.ct['get_strip_cut_index'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$69$get_strip_cut_index', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$93$get_type', 'p'), []),
    ]
    c.ct['get_usage_hint'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive$8$get_usage_hint', 'p'), []),
    ]
    c.ct['get_vertex'] = [
        ('d', 'i', 1, ('i', 'GeomPrimitive$16$get_vertex', 'pi'), ['int']),
    ]
    c.ct['get_vertices'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive$60$get_vertices', 'p'), []),
    ]
    c.ct['get_vertices_handle'] = [
        ('d', 'p', 1, ('p', 'GeomPrimitive$61$get_vertices_handle', 'pp'), ['Thread*']),
    ]
    c.ct['is_composite'] = [
        ('d', 'B', 0, ('B', 'GeomPrimitive$12$is_composite', 'p'), []),
    ]
    c.ct['is_indexed'] = [
        ('d', 'B', 0, ('B', 'GeomPrimitive$13$is_indexed', 'p'), []),
    ]
    c.ct['is_prepared'] = [
        ('d', 'B', 1, ('B', 'GeomPrimitive$81$is_prepared', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['make_adjacency'] = [
        ('d', 25, 0, ('p', 'GeomPrimitive$50$make_adjacency', 'p'), []),
    ]
    c.ct['make_copy'] = [
        ('d', 25, 0, ('p', 'GeomPrimitive$3$make_copy', 'p'), []),
    ]
    c.ct['make_index_data'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive$87$make_index_data', 'p'), []),
    ]
    c.ct['make_indexed'] = [
        ('d', 'v', 0, ('v', 'GeomPrimitive$30$make_indexed', 'p'), []),
    ]
    c.ct['make_lines'] = [
        ('d', 25, 0, ('p', 'GeomPrimitive$48$make_lines', 'p'), []),
    ]
    c.ct['make_nonindexed'] = [
        ('d', 'v', 2, ('v', 'GeomPrimitive$28$make_nonindexed', 'ppp'), ['GeomVertexData*', 'GeomVertexData const*']),
    ]
    c.ct['make_patches'] = [
        ('d', 25, 0, ('p', 'GeomPrimitive$49$make_patches', 'p'), []),
    ]
    c.ct['make_points'] = [
        ('d', 25, 0, ('p', 'GeomPrimitive$47$make_points', 'p'), []),
    ]
    c.ct['match_shade_model'] = [
        ('d', 25, 1, ('p', 'GeomPrimitive$46$match_shade_model', 'pp'), ['GeomEnums::ShadeModel']),
    ]
    c.ct['modify_ends'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive$71$modify_ends', 'p'), []),
    ]
    c.ct['modify_vertices'] = [
        ('d', 'p', 1, ('p', 'GeomPrimitive$62$modify_vertices', 'pi'), ['int']),
        ('d', 'p', 0, ('p', 'GeomPrimitive$63$modify_vertices', 'p'), []),
    ]
    c.ct['modify_vertices_handle'] = [
        ('d', 'p', 1, ('p', 'GeomPrimitive$64$modify_vertices_handle', 'pp'), ['Thread*']),
    ]
    c.ct['offset_vertices'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive$26$offset_vertices', 'pi'), ['int']),
        ('d', 'v', 3, ('v', 'GeomPrimitive$27$offset_vertices', 'piii'), ['int', 'int', 'int']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive$58$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['pack_vertices'] = [
        ('d', 'v', 2, ('v', 'GeomPrimitive$29$pack_vertices', 'ppp'), ['GeomVertexData*', 'GeomVertexData const*']),
    ]
    c.ct['prepare'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive$80$prepare', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['prepare_now'] = [
        ('d', 'p', 2, ('p', 'GeomPrimitive$82$prepare_now', 'ppp'), ['PreparedGraphicsObjects*', 'GraphicsStateGuardianBase*']),
    ]
    c.ct['release'] = [
        ('d', 'B', 1, ('B', 'GeomPrimitive$83$release', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['release_all'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$84$release_all', 'p'), []),
    ]
    c.ct['request_resident'] = [
        ('d', 'B', 1, ('B', 'GeomPrimitive$54$request_resident', 'pp'), ['Thread*']),
        ('d', 'B', 0, ('B', 'GeomPrimitive$55$request_resident', 'p'), []),
    ]
    c.ct['reserve_num_vertices'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive$23$reserve_num_vertices', 'pi'), ['int']),
    ]
    c.ct['reverse'] = [
        ('d', 25, 0, ('p', 'GeomPrimitive$45$reverse', 'p'), []),
    ]
    c.ct['rotate'] = [
        ('d', 25, 0, ('p', 'GeomPrimitive$43$rotate', 'p'), []),
    ]
    c.ct['set_ends'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive$72$set_ends', 'pp'), ['PTA_int']),
    ]
    c.ct['set_index_type'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive$11$set_index_type', 'pp'), ['GeomEnums::NumericType']),
    ]
    c.ct['set_minmax'] = [
        ('d', 'v', 4, ('v', 'GeomPrimitive$75$set_minmax', 'piipp'), ['int', 'int', 'GeomVertexArrayData*', 'GeomVertexArrayData*']),
    ]
    c.ct['set_nonindexed_vertices'] = [
        ('d', 'v', 2, ('v', 'GeomPrimitive$67$set_nonindexed_vertices', 'pii'), ['int', 'int']),
    ]
    c.ct['set_shade_model'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive$7$set_shade_model', 'pp'), ['GeomEnums::ShadeModel']),
    ]
    c.ct['set_usage_hint'] = [
        ('d', 'v', 1, ('v', 'GeomPrimitive$9$set_usage_hint', 'pp'), ['GeomEnums::UsageHint']),
    ]
    c.ct['set_vertices'] = [
        ('d', 'v', 2, ('v', 'GeomPrimitive$65$set_vertices', 'ppi'), ['GeomVertexArrayData const*', 'int']),
        ('d', 'v', 1, ('v', 'GeomPrimitive$66$set_vertices', 'pp'), ['GeomVertexArrayData const*']),
    ]
    c.ct['upcast_to_CopyOnWriteObject'] = [
        ('d', 23, 0, ('p', 'GeomPrimitive$1$upcast_to_CopyOnWriteObject', 'p'), []),
    ]
    c.ct['upcast_to_GeomEnums'] = [
        ('d', 3, 0, ('p', 'GeomPrimitive$2$upcast_to_GeomEnums', 'p'), []),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'GeomPrimitive$59$write', 'ppi'), ['std::ostream&', 'int']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'GeomPrimitive$89$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomPrimitive, attr, self)

GeomPrimitive.c.link(GeomPrimitive)



class GeomTriangles(GeomPrimitive):
    __bases__ = tuple([GeomPrimitive])
    c = cxx.cstructs()
    c.register("GeomTriangles", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 26, 1, ('p', 'GeomTriangles$1$GeomTriangles', 'p'), ['GeomEnums::UsageHint']),
        ('s', 26, 1, ('p', 'GeomTriangles$2$GeomTriangles', 'p'), ['GeomTriangles const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'GeomTriangles$5$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'GeomTriangles$6$init_type', ''), []),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'GeomTriangles$4$register_with_read_factory', ''), []),
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
        ('d', 'B', 3, ('B', 'GeomTriangles$3$draw', 'pppB'), ['GraphicsStateGuardianBase*', 'GeomPrimitivePipelineReader const*', 'bool']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'GeomTriangles$8$force_init_type', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'GeomTriangles$7$get_type', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomTriangles, attr, self)

GeomTriangles.c.link(GeomTriangles)



class Geom(CopyOnWriteObject, GeomEnums):
    __bases__ = tuple([CopyOnWriteObject, GeomEnums])
    c = cxx.cstructs()
    c.register("Geom", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 27, 1, ('p', 'Geom$3$Geom', 'p'), ['GeomVertexData const*']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'Geom$77$get_class_type', ''), []),
    ]
    c.ct['get_next_modified'] = [
        ('s', 'p', 0, ('p', 'Geom$73$get_next_modified', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'Geom$78$init_type', ''), []),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'Geom$74$register_with_read_factory', ''), []),
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
        ('d', 'v', 1, ('v', 'Geom$24$add_primitive', 'pp'), ['GeomPrimitive const*']),
    ]
    c.ct['check_valid'] = [
        ('d', 'B', 0, ('B', 'Geom$51$check_valid', 'p'), []),
        ('d', 'B', 1, ('B', 'Geom$52$check_valid', 'pp'), ['GeomVertexData const*']),
    ]
    c.ct['clear_bounds'] = [
        ('d', 'v', 0, ('v', 'Geom$61$clear_bounds', 'p'), []),
    ]
    c.ct['clear_cache'] = [
        ('d', 'v', 0, ('v', 'Geom$65$clear_cache', 'p'), []),
    ]
    c.ct['clear_cache_stage'] = [
        ('d', 'v', 1, ('v', 'Geom$66$clear_cache_stage', 'pp'), ['Thread*']),
    ]
    c.ct['clear_primitives'] = [
        ('d', 'v', 0, ('v', 'Geom$26$clear_primitives', 'p'), []),
    ]
    c.ct['copy_primitives_from'] = [
        ('d', 'B', 1, ('B', 'Geom$45$copy_primitives_from', 'pp'), ['Geom const*']),
    ]
    c.ct['decompose'] = [
        ('d', 27, 0, ('p', 'Geom$27$decompose', 'p'), []),
    ]
    c.ct['decompose_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom$36$decompose_in_place', 'p'), []),
    ]
    c.ct['doubleside'] = [
        ('d', 27, 0, ('p', 'Geom$28$doubleside', 'p'), []),
    ]
    c.ct['doubleside_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom$37$doubleside_in_place', 'p'), []),
    ]
    c.ct['draw'] = [
        ('d', 'B', 4, ('B', 'Geom$72$draw', 'pppBp'), ['GraphicsStateGuardianBase*', 'GeomVertexData const*', 'bool', 'Thread*']),
    ]
    c.ct['finalize'] = [
        ('d', 'v', 1, ('v', 'Geom$76$finalize', 'pp'), ['BamReader*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'Geom$80$force_init_type', 'p'), []),
    ]
    c.ct['get_animated_vertex_data'] = [
        ('d', 24, 2, ('p', 'Geom$16$get_animated_vertex_data', 'pBp'), ['bool', 'Thread*']),
        ('d', 24, 1, ('p', 'Geom$17$get_animated_vertex_data', 'pB'), ['bool']),
    ]
    c.ct['get_bounds'] = [
        ('d', 'p', 1, ('p', 'Geom$53$get_bounds', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'Geom$54$get_bounds', 'p'), []),
    ]
    c.ct['get_bounds_type'] = [
        ('d', 'p', 0, ('p', 'Geom$59$get_bounds_type', 'p'), []),
    ]
    c.ct['get_geom_rendering'] = [
        ('d', 'i', 0, ('i', 'Geom$7$get_geom_rendering', 'p'), []),
    ]
    c.ct['get_modified'] = [
        ('d', 'p', 1, ('p', 'Geom$47$get_modified', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'Geom$48$get_modified', 'p'), []),
    ]
    c.ct['get_nested_vertices'] = [
        ('d', 'i', 1, ('i', 'Geom$55$get_nested_vertices', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'Geom$56$get_nested_vertices', 'p'), []),
    ]
    c.ct['get_num_bytes'] = [
        ('d', 'i', 0, ('i', 'Geom$46$get_num_bytes', 'p'), []),
    ]
    c.ct['get_num_primitives'] = [
        ('d', 'p', 0, ('p', 'Geom$19$get_num_primitives', 'p'), []),
    ]
    c.ct['get_primitive'] = [
        ('d', 25, 1, ('p', 'Geom$20$get_primitive', 'pp'), ['std::size_t']),
    ]
    c.ct['get_primitive_type'] = [
        ('d', 'p', 0, ('p', 'Geom$5$get_primitive_type', 'p'), []),
    ]
    c.ct['get_shade_model'] = [
        ('d', 'p', 0, ('p', 'Geom$6$get_shade_model', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'Geom$79$get_type', 'p'), []),
    ]
    c.ct['get_usage_hint'] = [
        ('d', 'p', 0, ('p', 'Geom$8$get_usage_hint', 'p'), []),
    ]
    c.ct['get_vertex_data'] = [
        ('d', 24, 1, ('p', 'Geom$10$get_vertex_data', 'pp'), ['Thread*']),
        ('d', 24, 0, ('p', 'Geom$11$get_vertex_data', 'p'), []),
    ]
    c.ct['insert_primitive'] = [
        ('d', 'v', 2, ('v', 'Geom$23$insert_primitive', 'ppp'), ['std::size_t', 'GeomPrimitive const*']),
    ]
    c.ct['is_empty'] = [
        ('d', 'B', 0, ('B', 'Geom$18$is_empty', 'p'), []),
    ]
    c.ct['is_prepared'] = [
        ('d', 'B', 1, ('B', 'Geom$68$is_prepared', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['make_adjacency'] = [
        ('d', 27, 0, ('p', 'Geom$35$make_adjacency', 'p'), []),
    ]
    c.ct['make_adjacency_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom$44$make_adjacency_in_place', 'p'), []),
    ]
    c.ct['make_copy'] = [
        ('d', 27, 0, ('p', 'Geom$4$make_copy', 'p'), []),
    ]
    c.ct['make_lines'] = [
        ('d', 27, 0, ('p', 'Geom$33$make_lines', 'p'), []),
    ]
    c.ct['make_lines_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom$42$make_lines_in_place', 'p'), []),
    ]
    c.ct['make_nonindexed'] = [
        ('d', 'i', 1, ('i', 'Geom$15$make_nonindexed', 'pB'), ['bool']),
    ]
    c.ct['make_patches'] = [
        ('d', 27, 0, ('p', 'Geom$34$make_patches', 'p'), []),
    ]
    c.ct['make_patches_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom$43$make_patches_in_place', 'p'), []),
    ]
    c.ct['make_points'] = [
        ('d', 27, 0, ('p', 'Geom$32$make_points', 'p'), []),
    ]
    c.ct['make_points_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom$41$make_points_in_place', 'p'), []),
    ]
    c.ct['mark_bounds_stale'] = [
        ('d', 'v', 0, ('v', 'Geom$57$mark_bounds_stale', 'p'), []),
    ]
    c.ct['modify_primitive'] = [
        ('d', 25, 1, ('p', 'Geom$21$modify_primitive', 'pp'), ['std::size_t']),
    ]
    c.ct['modify_vertex_data'] = [
        ('d', 24, 0, ('p', 'Geom$12$modify_vertex_data', 'p'), []),
    ]
    c.ct['offset_vertices'] = [
        ('d', 'v', 2, ('v', 'Geom$14$offset_vertices', 'ppi'), ['GeomVertexData const*', 'int']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'Geom$62$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['prepare'] = [
        ('d', 'v', 1, ('v', 'Geom$67$prepare', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['prepare_now'] = [
        ('d', 'p', 2, ('p', 'Geom$71$prepare_now', 'ppp'), ['PreparedGraphicsObjects*', 'GraphicsStateGuardianBase*']),
    ]
    c.ct['release'] = [
        ('d', 'B', 1, ('B', 'Geom$69$release', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['release_all'] = [
        ('d', 'i', 0, ('i', 'Geom$70$release_all', 'p'), []),
    ]
    c.ct['remove_primitive'] = [
        ('d', 'v', 1, ('v', 'Geom$25$remove_primitive', 'pp'), ['std::size_t']),
    ]
    c.ct['request_resident'] = [
        ('d', 'B', 0, ('B', 'Geom$49$request_resident', 'p'), []),
    ]
    c.ct['reverse'] = [
        ('d', 27, 0, ('p', 'Geom$29$reverse', 'p'), []),
    ]
    c.ct['reverse_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom$38$reverse_in_place', 'p'), []),
    ]
    c.ct['rotate'] = [
        ('d', 27, 0, ('p', 'Geom$30$rotate', 'p'), []),
    ]
    c.ct['rotate_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom$39$rotate_in_place', 'p'), []),
    ]
    c.ct['set_bounds'] = [
        ('d', 'v', 1, ('v', 'Geom$60$set_bounds', 'pp'), ['BoundingVolume const*']),
    ]
    c.ct['set_bounds_type'] = [
        ('d', 'v', 1, ('v', 'Geom$58$set_bounds_type', 'pp'), ['BoundingVolume::BoundsType']),
    ]
    c.ct['set_primitive'] = [
        ('d', 'v', 2, ('v', 'Geom$22$set_primitive', 'ppp'), ['std::size_t', 'GeomPrimitive const*']),
    ]
    c.ct['set_usage_hint'] = [
        ('d', 'v', 1, ('v', 'Geom$9$set_usage_hint', 'pp'), ['GeomEnums::UsageHint']),
    ]
    c.ct['set_vertex_data'] = [
        ('d', 'v', 1, ('v', 'Geom$13$set_vertex_data', 'pp'), ['GeomVertexData const*']),
    ]
    c.ct['transform_vertices'] = [
        ('d', 'v', 1, ('v', 'Geom$50$transform_vertices', 'pp'), ['LMatrix4 const&']),
    ]
    c.ct['unify'] = [
        ('d', 27, 2, ('p', 'Geom$31$unify', 'piB'), ['int', 'bool']),
    ]
    c.ct['unify_in_place'] = [
        ('d', 'v', 2, ('v', 'Geom$40$unify_in_place', 'piB'), ['int', 'bool']),
    ]
    c.ct['upcast_to_CopyOnWriteObject'] = [
        ('d', 23, 0, ('p', 'Geom$1$upcast_to_CopyOnWriteObject', 'p'), []),
    ]
    c.ct['upcast_to_GeomEnums'] = [
        ('d', 3, 0, ('p', 'Geom$2$upcast_to_GeomEnums', 'p'), []),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'Geom$63$write', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'v', 1, ('v', 'Geom$64$write', 'pp'), ['std::ostream&']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'Geom$75$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(Geom, attr, self)

Geom.c.link(Geom)



class PandaNode(TypedWritableReferenceCount, Namable, LinkedListNode):
    __bases__ = tuple([TypedWritableReferenceCount, Namable, LinkedListNode])
    c = cxx.cstructs()
    c.register("PandaNode", "upanda3d", """libupanda3d_c.so""")

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
        ('s', 28, 1, ('p', 'PandaNode$4$PandaNode', 's'), ['std::string const&']),
    ]

    # classmethod type calls

    c.ct['decode_from_bam_stream'] = [
        ('s', 28, 2, ('p', 'PandaNode$193$decode_from_bam_stream', 'pp'), ['vector_uchar', 'BamReader*']),
        ('s', 28, 1, ('p', 'PandaNode$194$decode_from_bam_stream', 'p'), ['vector_uchar']),
    ]
    c.ct['get_all_camera_mask'] = [
        ('s', 'p', 0, ('p', 'PandaNode$142$get_all_camera_mask', ''), []),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'PandaNode$204$get_class_type', ''), []),
    ]
    c.ct['get_overall_bit'] = [
        ('s', 'p', 0, ('p', 'PandaNode$141$get_overall_bit', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'PandaNode$205$init_type', ''), []),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'PandaNode$200$register_with_read_factory', ''), []),
    ]
    c.ct['reset_all_prev_transform'] = [
        ('s', 'v', 1, ('v', 'PandaNode$118$reset_all_prev_transform', 'p'), ['Thread*']),
        ('s', 'v', 0, ('v', 'PandaNode$119$reset_all_prev_transform', ''), []),
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
        ('d', 'v', 3, ('v', 'PandaNode$43$add_child', 'ppip'), ['PandaNode*', 'int', 'Thread*']),
        ('d', 'v', 2, ('v', 'PandaNode$44$add_child', 'ppi'), ['PandaNode*', 'int']),
        ('d', 'v', 1, ('v', 'PandaNode$45$add_child', 'pp'), ['PandaNode*']),
    ]
    c.ct['add_for_draw'] = [
        ('d', 'v', 2, ('v', 'PandaNode$24$add_for_draw', 'ppp'), ['CullTraverser*', 'CullTraverserData&']),
    ]
    c.ct['add_stashed'] = [
        ('d', 'v', 3, ('v', 'PandaNode$70$add_stashed', 'ppip'), ['PandaNode*', 'int', 'Thread*']),
        ('d', 'v', 2, ('v', 'PandaNode$71$add_stashed', 'ppi'), ['PandaNode*', 'int']),
        ('d', 'v', 1, ('v', 'PandaNode$72$add_stashed', 'pp'), ['PandaNode*']),
    ]
    c.ct['adjust_draw_mask'] = [
        ('d', 'v', 3, ('v', 'PandaNode$145$adjust_draw_mask', 'pppp'), ['DrawMask', 'DrawMask', 'DrawMask']),
    ]
    c.ct['apply_attribs_to_vertices'] = [
        ('d', 'v', 3, ('v', 'PandaNode$15$apply_attribs_to_vertices', 'ppip'), ['AccumulatedAttribs const&', 'int', 'GeomTransformer&']),
    ]
    c.ct['as_light'] = [
        ('d', 'p', 0, ('p', 'PandaNode$189$as_light', 'p'), []),
    ]
    c.ct['clear_attrib'] = [
        ('d', 'v', 1, ('v', 'PandaNode$87$clear_attrib', 'pi'), ['TypeHandle']),
        ('d', 'v', 1, ('v', 'PandaNode$88$clear_attrib', 'pi'), ['int']),
    ]
    c.ct['clear_bounds'] = [
        ('d', 'v', 0, ('v', 'PandaNode$167$clear_bounds', 'p'), []),
    ]
    c.ct['clear_effect'] = [
        ('d', 'v', 1, ('v', 'PandaNode$92$clear_effect', 'pi'), ['TypeHandle']),
    ]
    c.ct['clear_effects'] = [
        ('d', 'v', 1, ('v', 'PandaNode$103$clear_effects', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'PandaNode$104$clear_effects', 'p'), []),
    ]
    c.ct['clear_state'] = [
        ('d', 'v', 1, ('v', 'PandaNode$97$clear_state', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'PandaNode$98$clear_state', 'p'), []),
    ]
    c.ct['clear_tag'] = [
        ('d', 'v', 2, ('v', 'PandaNode$126$clear_tag', 'psp'), ['std::string const&', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode$127$clear_tag', 'ps'), ['std::string const&']),
    ]
    c.ct['clear_transform'] = [
        ('d', 'v', 1, ('v', 'PandaNode$109$clear_transform', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'PandaNode$110$clear_transform', 'p'), []),
    ]
    c.ct['clear_unexpected_change'] = [
        ('d', 'v', 1, ('v', 'PandaNode$140$clear_unexpected_change', 'pI'), ['unsigned int']),
    ]
    c.ct['combine_with'] = [
        ('d', 28, 1, ('p', 'PandaNode$5$combine_with', 'pp'), ['PandaNode*']),
    ]
    c.ct['compare_tags'] = [
        ('d', 'i', 1, ('i', 'PandaNode$135$compare_tags', 'pp'), ['PandaNode const*']),
    ]
    c.ct['copy_all_properties'] = [
        ('d', 'v', 1, ('v', 'PandaNode$136$copy_all_properties', 'pp'), ['PandaNode*']),
    ]
    c.ct['copy_children'] = [
        ('d', 'v', 2, ('v', 'PandaNode$79$copy_children', 'ppp'), ['PandaNode*', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode$80$copy_children', 'pp'), ['PandaNode*']),
    ]
    c.ct['copy_subgraph'] = [
        ('d', 28, 1, ('p', 'PandaNode$26$copy_subgraph', 'pp'), ['Thread*']),
        ('d', 28, 0, ('p', 'PandaNode$27$copy_subgraph', 'p'), []),
    ]
    c.ct['copy_tags'] = [
        ('d', 'v', 1, ('v', 'PandaNode$132$copy_tags', 'pp'), ['PandaNode*']),
    ]
    c.ct['count_num_descendants'] = [
        ('d', 'i', 0, ('i', 'PandaNode$42$count_num_descendants', 'p'), []),
    ]
    c.ct['cull_callback'] = [
        ('d', 'B', 2, ('B', 'PandaNode$17$cull_callback', 'ppp'), ['CullTraverser*', 'CullTraverserData&']),
    ]
    c.ct['dupe_for_flatten'] = [
        ('d', 28, 0, ('p', 'PandaNode$6$dupe_for_flatten', 'p'), []),
    ]
    c.ct['find_child'] = [
        ('d', 'i', 2, ('i', 'PandaNode$40$find_child', 'ppp'), ['PandaNode*', 'Thread*']),
        ('d', 'i', 1, ('i', 'PandaNode$41$find_child', 'pp'), ['PandaNode*']),
    ]
    c.ct['find_parent'] = [
        ('d', 'i', 2, ('i', 'PandaNode$32$find_parent', 'ppp'), ['PandaNode*', 'Thread*']),
        ('d', 'i', 1, ('i', 'PandaNode$33$find_parent', 'pp'), ['PandaNode*']),
    ]
    c.ct['find_stashed'] = [
        ('d', 'i', 2, ('i', 'PandaNode$68$find_stashed', 'ppp'), ['PandaNode*', 'Thread*']),
        ('d', 'i', 1, ('i', 'PandaNode$69$find_stashed', 'pp'), ['PandaNode*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'PandaNode$207$force_init_type', 'p'), []),
    ]
    c.ct['get_attrib'] = [
        ('d', 'p', 1, ('p', 'PandaNode$83$get_attrib', 'pi'), ['TypeHandle']),
        ('d', 'p', 1, ('p', 'PandaNode$84$get_attrib', 'pi'), ['int']),
    ]
    c.ct['get_bounds'] = [
        ('d', 'p', 1, ('p', 'PandaNode$168$get_bounds', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode$169$get_bounds', 'p'), []),
        ('d', 'p', 2, ('p', 'PandaNode$170$get_bounds', 'ppp'), ['UpdateSeq&', 'Thread*']),
        ('d', 'p', 1, ('p', 'PandaNode$171$get_bounds', 'pp'), ['UpdateSeq&']),
    ]
    c.ct['get_bounds_type'] = [
        ('d', 'p', 0, ('p', 'PandaNode$164$get_bounds_type', 'p'), []),
    ]
    c.ct['get_child'] = [
        ('d', 28, 2, ('p', 'PandaNode$36$get_child', 'pip'), ['int', 'Thread*']),
        ('d', 28, 1, ('p', 'PandaNode$37$get_child', 'pi'), ['int']),
    ]
    c.ct['get_child_sort'] = [
        ('d', 'i', 2, ('i', 'PandaNode$38$get_child_sort', 'pip'), ['int', 'Thread*']),
        ('d', 'i', 1, ('i', 'PandaNode$39$get_child_sort', 'pi'), ['int']),
    ]
    c.ct['get_children'] = [
        ('d', 'p', 1, ('p', 'PandaNode$196$get_children', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode$197$get_children', 'p'), []),
    ]
    c.ct['get_draw_control_mask'] = [
        ('d', 'p', 0, ('p', 'PandaNode$146$get_draw_control_mask', 'p'), []),
    ]
    c.ct['get_draw_show_mask'] = [
        ('d', 'p', 0, ('p', 'PandaNode$147$get_draw_show_mask', 'p'), []),
    ]
    c.ct['get_effect'] = [
        ('d', 'p', 1, ('p', 'PandaNode$90$get_effect', 'pi'), ['TypeHandle']),
    ]
    c.ct['get_effects'] = [
        ('d', 'p', 1, ('p', 'PandaNode$101$get_effects', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode$102$get_effects', 'p'), []),
    ]
    c.ct['get_fancy_bits'] = [
        ('d', 'i', 1, ('i', 'PandaNode$191$get_fancy_bits', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'PandaNode$192$get_fancy_bits', 'p'), []),
    ]
    c.ct['get_first_visible_child'] = [
        ('d', 'i', 0, ('i', 'PandaNode$19$get_first_visible_child', 'p'), []),
    ]
    c.ct['get_internal_bounds'] = [
        ('d', 'p', 1, ('p', 'PandaNode$174$get_internal_bounds', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode$175$get_internal_bounds', 'p'), []),
    ]
    c.ct['get_internal_vertices'] = [
        ('d', 'i', 1, ('i', 'PandaNode$176$get_internal_vertices', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'PandaNode$177$get_internal_vertices', 'p'), []),
    ]
    c.ct['get_into_collide_mask'] = [
        ('d', 'p', 0, ('p', 'PandaNode$151$get_into_collide_mask', 'p'), []),
    ]
    c.ct['get_legal_collide_mask'] = [
        ('d', 'p', 0, ('p', 'PandaNode$152$get_legal_collide_mask', 'p'), []),
    ]
    c.ct['get_nested_vertices'] = [
        ('d', 'i', 1, ('i', 'PandaNode$172$get_nested_vertices', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'PandaNode$173$get_nested_vertices', 'p'), []),
    ]
    c.ct['get_net_collide_mask'] = [
        ('d', 'p', 1, ('p', 'PandaNode$153$get_net_collide_mask', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode$154$get_net_collide_mask', 'p'), []),
    ]
    c.ct['get_net_draw_control_mask'] = [
        ('d', 'p', 0, ('p', 'PandaNode$148$get_net_draw_control_mask', 'p'), []),
    ]
    c.ct['get_net_draw_show_mask'] = [
        ('d', 'p', 0, ('p', 'PandaNode$149$get_net_draw_show_mask', 'p'), []),
    ]
    c.ct['get_next_visible_child'] = [
        ('d', 'i', 1, ('i', 'PandaNode$20$get_next_visible_child', 'pi'), ['int']),
    ]
    c.ct['get_num_children'] = [
        ('d', 'i', 1, ('i', 'PandaNode$34$get_num_children', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'PandaNode$35$get_num_children', 'p'), []),
    ]
    c.ct['get_num_parents'] = [
        ('d', 'i', 1, ('i', 'PandaNode$28$get_num_parents', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'PandaNode$29$get_num_parents', 'p'), []),
    ]
    c.ct['get_num_stashed'] = [
        ('d', 'i', 1, ('i', 'PandaNode$60$get_num_stashed', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'PandaNode$61$get_num_stashed', 'p'), []),
    ]
    c.ct['get_num_tags'] = [
        ('d', 'p', 0, ('p', 'PandaNode$129$get_num_tags', 'p'), []),
    ]
    c.ct['get_off_clip_planes'] = [
        ('d', 'p', 1, ('p', 'PandaNode$155$get_off_clip_planes', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode$156$get_off_clip_planes', 'p'), []),
    ]
    c.ct['get_parent'] = [
        ('d', 28, 2, ('p', 'PandaNode$30$get_parent', 'pip'), ['int', 'Thread*']),
        ('d', 28, 1, ('p', 'PandaNode$31$get_parent', 'pi'), ['int']),
    ]
    c.ct['get_parents'] = [
        ('d', 'p', 1, ('p', 'PandaNode$198$get_parents', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode$199$get_parents', 'p'), []),
    ]
    c.ct['get_prev_transform'] = [
        ('d', 'p', 1, ('p', 'PandaNode$113$get_prev_transform', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode$114$get_prev_transform', 'p'), []),
    ]
    c.ct['get_stashed'] = [
        ('d', 'p', 1, ('p', 'PandaNode$62$get_stashed', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode$63$get_stashed', 'p'), []),
        ('d', 28, 2, ('p', 'PandaNode$64$get_stashed', 'pip'), ['int', 'Thread*']),
        ('d', 28, 1, ('p', 'PandaNode$65$get_stashed', 'pi'), ['int']),
    ]
    c.ct['get_stashed_sort'] = [
        ('d', 'i', 2, ('i', 'PandaNode$66$get_stashed_sort', 'pip'), ['int', 'Thread*']),
        ('d', 'i', 1, ('i', 'PandaNode$67$get_stashed_sort', 'pi'), ['int']),
    ]
    c.ct['get_state'] = [
        ('d', 'p', 1, ('p', 'PandaNode$95$get_state', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode$96$get_state', 'p'), []),
    ]
    c.ct['get_tag'] = [
        ('d', 's', 2, ('s', 'PandaNode$122$get_tag', 'psp'), ['std::string const&', 'Thread*']),
        ('d', 's', 1, ('s', 'PandaNode$123$get_tag', 'ps'), ['std::string const&']),
    ]
    c.ct['get_tag_key'] = [
        ('d', 's', 1, ('s', 'PandaNode$130$get_tag_key', 'pp'), ['std::size_t']),
    ]
    c.ct['get_tag_keys'] = [
        ('d', 'v', 1, ('v', 'PandaNode$128$get_tag_keys', 'pp'), ['vector_string&']),
    ]
    c.ct['get_transform'] = [
        ('d', 'p', 1, ('p', 'PandaNode$107$get_transform', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode$108$get_transform', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'PandaNode$206$get_type', 'p'), []),
    ]
    c.ct['get_unexpected_change'] = [
        ('d', 'I', 1, ('I', 'PandaNode$139$get_unexpected_change', 'pI'), ['unsigned int']),
    ]
    c.ct['get_unsafe_to_apply_attribs'] = [
        ('d', 'i', 0, ('i', 'PandaNode$14$get_unsafe_to_apply_attribs', 'p'), []),
    ]
    c.ct['get_visible_child'] = [
        ('d', 'i', 0, ('i', 'PandaNode$22$get_visible_child', 'p'), []),
    ]
    c.ct['has_attrib'] = [
        ('d', 'B', 1, ('B', 'PandaNode$85$has_attrib', 'pi'), ['TypeHandle']),
        ('d', 'B', 1, ('B', 'PandaNode$86$has_attrib', 'pi'), ['int']),
    ]
    c.ct['has_dirty_prev_transform'] = [
        ('d', 'B', 0, ('B', 'PandaNode$117$has_dirty_prev_transform', 'p'), []),
    ]
    c.ct['has_effect'] = [
        ('d', 'B', 1, ('B', 'PandaNode$91$has_effect', 'pi'), ['TypeHandle']),
    ]
    c.ct['has_selective_visibility'] = [
        ('d', 'B', 0, ('B', 'PandaNode$18$has_selective_visibility', 'p'), []),
    ]
    c.ct['has_single_child_visibility'] = [
        ('d', 'B', 0, ('B', 'PandaNode$21$has_single_child_visibility', 'p'), []),
    ]
    c.ct['has_tag'] = [
        ('d', 'B', 2, ('B', 'PandaNode$124$has_tag', 'psp'), ['std::string const&', 'Thread*']),
        ('d', 'B', 1, ('B', 'PandaNode$125$has_tag', 'ps'), ['std::string const&']),
    ]
    c.ct['has_tags'] = [
        ('d', 'B', 0, ('B', 'PandaNode$131$has_tags', 'p'), []),
    ]
    c.ct['is_ambient_light'] = [
        ('d', 'B', 0, ('B', 'PandaNode$190$is_ambient_light', 'p'), []),
    ]
    c.ct['is_bounds_stale'] = [
        ('d', 'B', 0, ('B', 'PandaNode$182$is_bounds_stale', 'p'), []),
    ]
    c.ct['is_collision_node'] = [
        ('d', 'B', 0, ('B', 'PandaNode$188$is_collision_node', 'p'), []),
    ]
    c.ct['is_final'] = [
        ('d', 'B', 1, ('B', 'PandaNode$184$is_final', 'pp'), ['Thread*']),
        ('d', 'B', 0, ('B', 'PandaNode$185$is_final', 'p'), []),
    ]
    c.ct['is_geom_node'] = [
        ('d', 'B', 0, ('B', 'PandaNode$186$is_geom_node', 'p'), []),
    ]
    c.ct['is_lod_node'] = [
        ('d', 'B', 0, ('B', 'PandaNode$187$is_lod_node', 'p'), []),
    ]
    c.ct['is_overall_hidden'] = [
        ('d', 'B', 0, ('B', 'PandaNode$143$is_overall_hidden', 'p'), []),
    ]
    c.ct['is_renderable'] = [
        ('d', 'B', 0, ('B', 'PandaNode$23$is_renderable', 'p'), []),
    ]
    c.ct['is_scene_root'] = [
        ('d', 'B', 0, ('B', 'PandaNode$158$is_scene_root', 'p'), []),
    ]
    c.ct['is_under_scene_root'] = [
        ('d', 'B', 0, ('B', 'PandaNode$159$is_under_scene_root', 'p'), []),
    ]
    c.ct['list_tags'] = [
        ('d', 'v', 2, ('v', 'PandaNode$133$list_tags', 'pps'), ['std::ostream&', 'std::string const&']),
        ('d', 'v', 1, ('v', 'PandaNode$134$list_tags', 'pp'), ['std::ostream&']),
    ]
    c.ct['ls'] = [
        ('d', 'v', 2, ('v', 'PandaNode$162$ls', 'ppi'), ['std::ostream&', 'int']),
    ]
    c.ct['make_copy'] = [
        ('d', 28, 0, ('p', 'PandaNode$25$make_copy', 'p'), []),
    ]
    c.ct['mark_bounds_stale'] = [
        ('d', 'v', 1, ('v', 'PandaNode$178$mark_bounds_stale', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'PandaNode$179$mark_bounds_stale', 'p'), []),
    ]
    c.ct['mark_internal_bounds_stale'] = [
        ('d', 'v', 1, ('v', 'PandaNode$180$mark_internal_bounds_stale', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'PandaNode$181$mark_internal_bounds_stale', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'PandaNode$160$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['prepare_scene'] = [
        ('d', 'v', 2, ('v', 'PandaNode$157$prepare_scene', 'ppp'), ['GraphicsStateGuardianBase*', 'RenderState const*']),
    ]
    c.ct['preserve_name'] = [
        ('d', 'B', 0, ('B', 'PandaNode$13$preserve_name', 'p'), []),
    ]
    c.ct['r_prepare_scene'] = [
        ('d', 'v', 4, ('v', 'PandaNode$195$r_prepare_scene', 'ppppp'), ['GraphicsStateGuardianBase*', 'RenderState const*', 'GeomTransformer&', 'Thread*']),
    ]
    c.ct['remove_all_children'] = [
        ('d', 'v', 1, ('v', 'PandaNode$75$remove_all_children', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'PandaNode$76$remove_all_children', 'p'), []),
    ]
    c.ct['remove_child'] = [
        ('d', 'B', 2, ('B', 'PandaNode$46$remove_child', 'ppp'), ['PandaNode*', 'Thread*']),
        ('d', 'B', 1, ('B', 'PandaNode$47$remove_child', 'pp'), ['PandaNode*']),
        ('d', 'v', 2, ('v', 'PandaNode$48$remove_child', 'pip'), ['int', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode$49$remove_child', 'pi'), ['int']),
    ]
    c.ct['remove_stashed'] = [
        ('d', 'v', 2, ('v', 'PandaNode$73$remove_stashed', 'pip'), ['int', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode$74$remove_stashed', 'pi'), ['int']),
    ]
    c.ct['replace_child'] = [
        ('d', 'B', 3, ('B', 'PandaNode$50$replace_child', 'pppp'), ['PandaNode*', 'PandaNode*', 'Thread*']),
        ('d', 'B', 2, ('B', 'PandaNode$51$replace_child', 'ppp'), ['PandaNode*', 'PandaNode*']),
    ]
    c.ct['replace_node'] = [
        ('d', 'v', 1, ('v', 'PandaNode$137$replace_node', 'pp'), ['PandaNode*']),
    ]
    c.ct['reset_prev_transform'] = [
        ('d', 'v', 1, ('v', 'PandaNode$115$reset_prev_transform', 'pp'), ['Thread*']),
        ('d', 'v', 0, ('v', 'PandaNode$116$reset_prev_transform', 'p'), []),
    ]
    c.ct['safe_to_combine'] = [
        ('d', 'B', 0, ('B', 'PandaNode$10$safe_to_combine', 'p'), []),
    ]
    c.ct['safe_to_combine_children'] = [
        ('d', 'B', 0, ('B', 'PandaNode$11$safe_to_combine_children', 'p'), []),
    ]
    c.ct['safe_to_flatten'] = [
        ('d', 'B', 0, ('B', 'PandaNode$7$safe_to_flatten', 'p'), []),
    ]
    c.ct['safe_to_flatten_below'] = [
        ('d', 'B', 0, ('B', 'PandaNode$12$safe_to_flatten_below', 'p'), []),
    ]
    c.ct['safe_to_modify_transform'] = [
        ('d', 'B', 0, ('B', 'PandaNode$9$safe_to_modify_transform', 'p'), []),
    ]
    c.ct['safe_to_transform'] = [
        ('d', 'B', 0, ('B', 'PandaNode$8$safe_to_transform', 'p'), []),
    ]
    c.ct['set_attrib'] = [
        ('d', 'v', 2, ('v', 'PandaNode$81$set_attrib', 'ppi'), ['RenderAttrib const*', 'int']),
        ('d', 'v', 1, ('v', 'PandaNode$82$set_attrib', 'pp'), ['RenderAttrib const*']),
    ]
    c.ct['set_bound'] = [
        ('d', 'v', 1, ('v', 'PandaNode$166$set_bound', 'pp'), ['BoundingVolume const*']),
    ]
    c.ct['set_bounds'] = [
        ('d', 'v', 1, ('v', 'PandaNode$165$set_bounds', 'pp'), ['BoundingVolume const*']),
    ]
    c.ct['set_bounds_type'] = [
        ('d', 'v', 1, ('v', 'PandaNode$163$set_bounds_type', 'pp'), ['BoundingVolume::BoundsType']),
    ]
    c.ct['set_effect'] = [
        ('d', 'v', 1, ('v', 'PandaNode$89$set_effect', 'pp'), ['RenderEffect const*']),
    ]
    c.ct['set_effects'] = [
        ('d', 'v', 2, ('v', 'PandaNode$99$set_effects', 'ppp'), ['RenderEffects const*', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode$100$set_effects', 'pp'), ['RenderEffects const*']),
    ]
    c.ct['set_final'] = [
        ('d', 'v', 1, ('v', 'PandaNode$183$set_final', 'pB'), ['bool']),
    ]
    c.ct['set_into_collide_mask'] = [
        ('d', 'v', 1, ('v', 'PandaNode$150$set_into_collide_mask', 'pp'), ['CollideMask']),
    ]
    c.ct['set_overall_hidden'] = [
        ('d', 'v', 1, ('v', 'PandaNode$144$set_overall_hidden', 'pB'), ['bool']),
    ]
    c.ct['set_prev_transform'] = [
        ('d', 'v', 2, ('v', 'PandaNode$111$set_prev_transform', 'ppp'), ['TransformState const*', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode$112$set_prev_transform', 'pp'), ['TransformState const*']),
    ]
    c.ct['set_state'] = [
        ('d', 'v', 2, ('v', 'PandaNode$93$set_state', 'ppp'), ['RenderState const*', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode$94$set_state', 'pp'), ['RenderState const*']),
    ]
    c.ct['set_tag'] = [
        ('d', 'v', 3, ('v', 'PandaNode$120$set_tag', 'pssp'), ['std::string const&', 'std::string const&', 'Thread*']),
        ('d', 'v', 2, ('v', 'PandaNode$121$set_tag', 'pss'), ['std::string const&', 'std::string const&']),
    ]
    c.ct['set_transform'] = [
        ('d', 'v', 2, ('v', 'PandaNode$105$set_transform', 'ppp'), ['TransformState const*', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode$106$set_transform', 'pp'), ['TransformState const*']),
    ]
    c.ct['set_unexpected_change'] = [
        ('d', 'v', 1, ('v', 'PandaNode$138$set_unexpected_change', 'pI'), ['unsigned int']),
    ]
    c.ct['stash_child'] = [
        ('d', 'B', 2, ('B', 'PandaNode$52$stash_child', 'ppp'), ['PandaNode*', 'Thread*']),
        ('d', 'B', 1, ('B', 'PandaNode$53$stash_child', 'pp'), ['PandaNode*']),
        ('d', 'v', 2, ('v', 'PandaNode$54$stash_child', 'pip'), ['int', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode$55$stash_child', 'pi'), ['int']),
    ]
    c.ct['steal_children'] = [
        ('d', 'v', 2, ('v', 'PandaNode$77$steal_children', 'ppp'), ['PandaNode*', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode$78$steal_children', 'pp'), ['PandaNode*']),
    ]
    c.ct['unstash_child'] = [
        ('d', 'B', 2, ('B', 'PandaNode$56$unstash_child', 'ppp'), ['PandaNode*', 'Thread*']),
        ('d', 'B', 1, ('B', 'PandaNode$57$unstash_child', 'pp'), ['PandaNode*']),
        ('d', 'v', 2, ('v', 'PandaNode$58$unstash_child', 'pip'), ['int', 'Thread*']),
        ('d', 'v', 1, ('v', 'PandaNode$59$unstash_child', 'pi'), ['int']),
    ]
    c.ct['upcast_to_LinkedListNode'] = [
        ('d', 5, 0, ('p', 'PandaNode$3$upcast_to_LinkedListNode', 'p'), []),
    ]
    c.ct['upcast_to_Namable'] = [
        ('d', 12, 0, ('p', 'PandaNode$2$upcast_to_Namable', 'p'), []),
    ]
    c.ct['upcast_to_TypedWritableReferenceCount'] = [
        ('d', 18, 0, ('p', 'PandaNode$1$upcast_to_TypedWritableReferenceCount', 'p'), []),
    ]
    c.ct['update_bam_nested'] = [
        ('d', 'v', 1, ('v', 'PandaNode$202$update_bam_nested', 'pp'), ['BamWriter*']),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'PandaNode$161$write', 'ppi'), ['std::ostream&', 'int']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'PandaNode$201$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]
    c.ct['write_recorder'] = [
        ('d', 'v', 2, ('v', 'PandaNode$203$write_recorder', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]
    c.ct['xform'] = [
        ('d', 'v', 1, ('v', 'PandaNode$16$xform', 'pp'), ['LMatrix4 const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(PandaNode, attr, self)

PandaNode.c.link(PandaNode)



class LensNode(PandaNode):
    __bases__ = tuple([PandaNode])
    c = cxx.cstructs()
    c.register("LensNode", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 29, 2, ('p', 'LensNode$1$LensNode', 'sp'), ['std::string const&', 'Lens*']),
        ('s', 29, 1, ('p', 'LensNode$2$LensNode', 's'), ['std::string const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LensNode$20$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LensNode$21$init_type', ''), []),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'LensNode$18$register_with_read_factory', ''), []),
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
        ('d', 'B', 1, ('B', 'LensNode$12$activate_lens', 'pi'), ['int']),
    ]
    c.ct['copy_lens'] = [
        ('d', 'v', 1, ('v', 'LensNode$4$copy_lens', 'pp'), ['Lens const&']),
        ('d', 'v', 2, ('v', 'LensNode$5$copy_lens', 'pip'), ['int', 'Lens const&']),
    ]
    c.ct['deactivate_lens'] = [
        ('d', 'B', 1, ('B', 'LensNode$13$deactivate_lens', 'pi'), ['int']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'LensNode$23$force_init_type', 'p'), []),
    ]
    c.ct['get_lens'] = [
        ('d', 'p', 1, ('p', 'LensNode$8$get_lens', 'pi'), ['int']),
        ('d', 'p', 0, ('p', 'LensNode$9$get_lens', 'p'), []),
    ]
    c.ct['get_lens_active'] = [
        ('d', 'B', 1, ('B', 'LensNode$11$get_lens_active', 'pi'), ['int']),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'LensNode$22$get_type', 'p'), []),
    ]
    c.ct['hide_frustum'] = [
        ('d', 'v', 0, ('v', 'LensNode$17$hide_frustum', 'p'), []),
    ]
    c.ct['is_in_view'] = [
        ('d', 'B', 1, ('B', 'LensNode$14$is_in_view', 'pp'), ['LPoint3 const&']),
        ('d', 'B', 2, ('B', 'LensNode$15$is_in_view', 'pip'), ['int', 'LPoint3 const&']),
    ]
    c.ct['set_lens'] = [
        ('d', 'v', 1, ('v', 'LensNode$6$set_lens', 'pp'), ['Lens*']),
        ('d', 'v', 2, ('v', 'LensNode$7$set_lens', 'pip'), ['int', 'Lens*']),
    ]
    c.ct['set_lens_active'] = [
        ('d', 'B', 2, ('B', 'LensNode$10$set_lens_active', 'piB'), ['int', 'bool']),
    ]
    c.ct['show_frustum'] = [
        ('d', 'v', 0, ('v', 'LensNode$16$show_frustum', 'p'), []),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'LensNode$19$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]
    c.ct['xform'] = [
        ('d', 'v', 1, ('v', 'LensNode$3$xform', 'pp'), ['LMatrix4 const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LensNode, attr, self)

LensNode.c.link(LensNode)



class Camera(LensNode):
    __bases__ = tuple([LensNode])
    c = cxx.cstructs()
    c.register("Camera", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 30, 1, ('p', 'Camera$1$Camera', 'p'), ['Camera const&']),
        ('s', 30, 2, ('p', 'Camera$2$Camera', 'sp'), ['std::string const&', 'Lens*']),
        ('s', 30, 1, ('p', 'Camera$3$Camera', 's'), ['std::string const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'Camera$40$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'Camera$41$init_type', ''), []),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'Camera$38$register_with_read_factory', ''), []),
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
        ('d', 'i', 1, ('i', 'Camera$36$cleanup_aux_scene_data', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'Camera$37$cleanup_aux_scene_data', 'p'), []),
    ]
    c.ct['clear_aux_scene_data'] = [
        ('d', 'B', 1, ('B', 'Camera$33$clear_aux_scene_data', 'pp'), ['NodePath const&']),
    ]
    c.ct['clear_tag_state'] = [
        ('d', 'v', 1, ('v', 'Camera$28$clear_tag_state', 'ps'), ['std::string const&']),
    ]
    c.ct['clear_tag_states'] = [
        ('d', 'v', 0, ('v', 'Camera$29$clear_tag_states', 'p'), []),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'Camera$43$force_init_type', 'p'), []),
    ]
    c.ct['get_aux_scene_data'] = [
        ('d', 'p', 1, ('p', 'Camera$34$get_aux_scene_data', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_camera_mask'] = [
        ('d', 'p', 0, ('p', 'Camera$14$get_camera_mask', 'p'), []),
    ]
    c.ct['get_cull_bounds'] = [
        ('d', 'p', 0, ('p', 'Camera$18$get_cull_bounds', 'p'), []),
    ]
    c.ct['get_cull_center'] = [
        ('d', 7, 0, ('p', 'Camera$16$get_cull_center', 'p'), []),
    ]
    c.ct['get_display_region'] = [
        ('d', 'p', 1, ('p', 'Camera$12$get_display_region', 'pp'), ['std::size_t']),
    ]
    c.ct['get_initial_state'] = [
        ('d', 'p', 0, ('p', 'Camera$22$get_initial_state', 'p'), []),
    ]
    c.ct['get_lod_center'] = [
        ('d', 7, 0, ('p', 'Camera$20$get_lod_center', 'p'), []),
    ]
    c.ct['get_lod_scale'] = [
        ('d', 'f', 0, ('f', 'Camera$26$get_lod_scale', 'p'), []),
    ]
    c.ct['get_num_display_regions'] = [
        ('d', 'p', 0, ('p', 'Camera$11$get_num_display_regions', 'p'), []),
    ]
    c.ct['get_scene'] = [
        ('d', 7, 0, ('p', 'Camera$10$get_scene', 'p'), []),
    ]
    c.ct['get_tag_state'] = [
        ('d', 'p', 1, ('p', 'Camera$31$get_tag_state', 'ps'), ['std::string const&']),
    ]
    c.ct['get_tag_state_key'] = [
        ('d', 's', 0, ('s', 'Camera$24$get_tag_state_key', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'Camera$42$get_type', 'p'), []),
    ]
    c.ct['has_tag_state'] = [
        ('d', 'B', 1, ('B', 'Camera$30$has_tag_state', 'ps'), ['std::string const&']),
    ]
    c.ct['is_active'] = [
        ('d', 'B', 0, ('B', 'Camera$8$is_active', 'p'), []),
    ]
    c.ct['list_aux_scene_data'] = [
        ('d', 'v', 1, ('v', 'Camera$35$list_aux_scene_data', 'pp'), ['std::ostream&']),
    ]
    c.ct['make_copy'] = [
        ('d', 28, 0, ('p', 'Camera$4$make_copy', 'p'), []),
    ]
    c.ct['safe_to_flatten'] = [
        ('d', 'B', 0, ('B', 'Camera$5$safe_to_flatten', 'p'), []),
    ]
    c.ct['safe_to_transform'] = [
        ('d', 'B', 0, ('B', 'Camera$6$safe_to_transform', 'p'), []),
    ]
    c.ct['set_active'] = [
        ('d', 'v', 1, ('v', 'Camera$7$set_active', 'pB'), ['bool']),
    ]
    c.ct['set_aux_scene_data'] = [
        ('d', 'v', 2, ('v', 'Camera$32$set_aux_scene_data', 'ppp'), ['NodePath const&', 'AuxSceneData*']),
    ]
    c.ct['set_camera_mask'] = [
        ('d', 'v', 1, ('v', 'Camera$13$set_camera_mask', 'pp'), ['DrawMask']),
    ]
    c.ct['set_cull_bounds'] = [
        ('d', 'v', 1, ('v', 'Camera$17$set_cull_bounds', 'pp'), ['BoundingVolume*']),
    ]
    c.ct['set_cull_center'] = [
        ('d', 'v', 1, ('v', 'Camera$15$set_cull_center', 'pp'), ['NodePath const&']),
    ]
    c.ct['set_initial_state'] = [
        ('d', 'v', 1, ('v', 'Camera$21$set_initial_state', 'pp'), ['RenderState const*']),
    ]
    c.ct['set_lod_center'] = [
        ('d', 'v', 1, ('v', 'Camera$19$set_lod_center', 'pp'), ['NodePath const&']),
    ]
    c.ct['set_lod_scale'] = [
        ('d', 'v', 1, ('v', 'Camera$25$set_lod_scale', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_scene'] = [
        ('d', 'v', 1, ('v', 'Camera$9$set_scene', 'pp'), ['NodePath const&']),
    ]
    c.ct['set_tag_state'] = [
        ('d', 'v', 2, ('v', 'Camera$27$set_tag_state', 'psp'), ['std::string const&', 'RenderState const*']),
    ]
    c.ct['set_tag_state_key'] = [
        ('d', 'v', 1, ('v', 'Camera$23$set_tag_state_key', 'ps'), ['std::string const&']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'Camera$39$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(Camera, attr, self)

Camera.c.link(Camera)



class GeomNode(PandaNode):
    __bases__ = tuple([PandaNode])
    c = cxx.cstructs()
    c.register("GeomNode", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 31, 1, ('p', 'GeomNode$1$GeomNode', 's'), ['std::string const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'GeomNode$34$get_class_type', ''), []),
    ]
    c.ct['get_default_collide_mask'] = [
        ('s', 'p', 0, ('p', 'GeomNode$27$get_default_collide_mask', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'GeomNode$35$init_type', ''), []),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'GeomNode$31$register_with_read_factory', ''), []),
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
        ('d', 'v', 2, ('v', 'GeomNode$5$add_for_draw', 'ppp'), ['CullTraverser*', 'CullTraverserData&']),
    ]
    c.ct['add_geom'] = [
        ('d', 'v', 2, ('v', 'GeomNode$16$add_geom', 'ppp'), ['Geom*', 'RenderState const*']),
        ('d', 'v', 1, ('v', 'GeomNode$17$add_geom', 'pp'), ['Geom*']),
    ]
    c.ct['add_geoms_from'] = [
        ('d', 'v', 1, ('v', 'GeomNode$18$add_geoms_from', 'pp'), ['GeomNode const*']),
    ]
    c.ct['apply_attribs_to_vertices'] = [
        ('d', 'v', 3, ('v', 'GeomNode$2$apply_attribs_to_vertices', 'ppip'), ['AccumulatedAttribs const&', 'int', 'GeomTransformer&']),
    ]
    c.ct['check_valid'] = [
        ('d', 'B', 0, ('B', 'GeomNode$22$check_valid', 'p'), []),
    ]
    c.ct['decompose'] = [
        ('d', 'v', 0, ('v', 'GeomNode$23$decompose', 'p'), []),
    ]
    c.ct['do_premunge'] = [
        ('d', 'v', 3, ('v', 'GeomNode$28$do_premunge', 'pppp'), ['GraphicsStateGuardianBase*', 'RenderState const*', 'GeomTransformer&']),
    ]
    c.ct['finalize'] = [
        ('d', 'v', 1, ('v', 'GeomNode$33$finalize', 'pp'), ['BamReader*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'GeomNode$37$force_init_type', 'p'), []),
    ]
    c.ct['get_geom'] = [
        ('d', 27, 1, ('p', 'GeomNode$12$get_geom', 'pi'), ['int']),
    ]
    c.ct['get_geom_state'] = [
        ('d', 'p', 1, ('p', 'GeomNode$14$get_geom_state', 'pi'), ['int']),
    ]
    c.ct['get_geoms'] = [
        ('d', 'p', 1, ('p', 'GeomNode$29$get_geoms', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'GeomNode$30$get_geoms', 'p'), []),
    ]
    c.ct['get_num_geoms'] = [
        ('d', 'i', 0, ('i', 'GeomNode$11$get_num_geoms', 'p'), []),
    ]
    c.ct['get_preserved'] = [
        ('d', 'B', 0, ('B', 'GeomNode$10$get_preserved', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'GeomNode$36$get_type', 'p'), []),
    ]
    c.ct['is_renderable'] = [
        ('d', 'B', 0, ('B', 'GeomNode$4$is_renderable', 'p'), []),
    ]
    c.ct['modify_geom'] = [
        ('d', 27, 1, ('p', 'GeomNode$13$modify_geom', 'pi'), ['int']),
    ]
    c.ct['r_prepare_scene'] = [
        ('d', 'v', 4, ('v', 'GeomNode$8$r_prepare_scene', 'ppppp'), ['GraphicsStateGuardianBase*', 'RenderState const*', 'GeomTransformer&', 'Thread*']),
    ]
    c.ct['remove_all_geoms'] = [
        ('d', 'v', 0, ('v', 'GeomNode$21$remove_all_geoms', 'p'), []),
    ]
    c.ct['remove_geom'] = [
        ('d', 'v', 1, ('v', 'GeomNode$20$remove_geom', 'pi'), ['int']),
    ]
    c.ct['safe_to_combine'] = [
        ('d', 'B', 0, ('B', 'GeomNode$7$safe_to_combine', 'p'), []),
    ]
    c.ct['safe_to_flatten'] = [
        ('d', 'B', 0, ('B', 'GeomNode$6$safe_to_flatten', 'p'), []),
    ]
    c.ct['set_geom'] = [
        ('d', 'v', 2, ('v', 'GeomNode$19$set_geom', 'pip'), ['int', 'Geom*']),
    ]
    c.ct['set_geom_state'] = [
        ('d', 'v', 2, ('v', 'GeomNode$15$set_geom_state', 'pip'), ['int', 'RenderState const*']),
    ]
    c.ct['set_preserved'] = [
        ('d', 'v', 1, ('v', 'GeomNode$9$set_preserved', 'pB'), ['bool']),
    ]
    c.ct['unify'] = [
        ('d', 'v', 2, ('v', 'GeomNode$24$unify', 'piB'), ['int', 'bool']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'GeomNode$32$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]
    c.ct['write_geoms'] = [
        ('d', 'v', 2, ('v', 'GeomNode$25$write_geoms', 'ppi'), ['std::ostream&', 'int']),
    ]
    c.ct['write_verbose'] = [
        ('d', 'v', 2, ('v', 'GeomNode$26$write_verbose', 'ppi'), ['std::ostream&', 'int']),
    ]
    c.ct['xform'] = [
        ('d', 'v', 1, ('v', 'GeomNode$3$xform', 'pp'), ['LMatrix4 const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomNode, attr, self)

GeomNode.c.link(GeomNode)




cxx.REFCOUNTED = ReferenceCount
cxx.INCREF = Engine.inc_ref
cxx.DECREF = Engine.dec_ref





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


        cube = E.new_Cube(1.0, "CubeMaker", "Data")
        print('cube=',cube)

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


