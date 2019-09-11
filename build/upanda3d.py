# upy

import sys


if not '.' in sys.path: sys.path.insert(0,'.')
import interrogator.uplusplus as cxx

extern = cxx.cstructs.decl.append
extern('ConfigPage') # 
extern('DrawableRegion') # 
extern('Engine') # 
extern('Filename') # 
extern('FrameBufferProperties') # 
extern('GeomEnums') # 
extern('LVecBase2d') # 
extern('LVecBase2f') # 
extern('LVecBase2i') # 
extern('LVecBase3d') # 
extern('LVecBase3f') # 
extern('LVecBase3i') # 
extern('LVecBase4d') # 
extern('LVecBase4f') # 
extern('LVecBase4i') # 
extern('LinkedListNode') # 
extern('MemoryBase') # 
extern('NodePath') # 
extern('NodePathCollection') # 
extern('PandaFramework') # 
extern('PandaSystem') # 
extern('ShaderInput') # 
extern('TextEncoder') # 
extern('TextProperties') # 
extern('TextureCollection') # 
extern('TouchInfo') # 
extern('UpdateSeq') # 
extern('WindowProperties') # 
extern('GeomVertexColumn') # GeomEnums
extern('GeomVertexWriter') # GeomEnums
extern('LPoint2d') # LVecBase2d
extern('LPoint2f') # LVecBase2f
extern('LPoint2i') # LVecBase2i
extern('LPoint3d') # LVecBase3d
extern('LPoint3f') # LVecBase3f
extern('LPoint3i') # LVecBase3i
extern('LPoint4d') # LVecBase4d
extern('LPoint4f') # LVecBase4f
extern('LPoint4i') # LVecBase4i
extern('LVector2d') # LVecBase2d
extern('LVector2f') # LVecBase2f
extern('LVector2i') # LVecBase2i
extern('LVector3d') # LVecBase3d
extern('LVector3f') # LVecBase3f
extern('LVector3i') # LVecBase3i
extern('LVector4d') # LVecBase4d
extern('LVector4f') # LVecBase4f
extern('LVector4i') # LVecBase4i
extern('Namable') # MemoryBase
extern('ReferenceCount') # MemoryBase
extern('GraphicsEngine') # ReferenceCount
extern('SimpleLruPage') # LinkedListNode
extern('TexturePeeker') # ReferenceCount
extern('TypedObject') # MemoryBase
extern('EventHandler') # TypedObject
extern('TypedWritable') # TypedObject
extern('GeomVertexArrayDataHandle') # ReferenceCount, GeomEnums
extern('TypedReferenceCount') # TypedObject, ReferenceCount
extern('Thread') # TypedReferenceCount, Namable
extern('TextFont') # TypedReferenceCount, Namable
extern('Loader') # TypedReferenceCount, Namable
extern('DisplayRegion') # TypedReferenceCount, DrawableRegion
extern('WindowHandle') # TypedReferenceCount
extern('TypedWritableReferenceCount') # TypedWritable, ReferenceCount
extern('Texture') # TypedWritableReferenceCount, Namable
extern('GeomVertexFormat') # TypedWritableReferenceCount, GeomEnums
extern('GeomVertexArrayFormat') # TypedWritableReferenceCount, GeomEnums
extern('WindowFramework') # TypedWritableReferenceCount
extern('TransformTable') # TypedWritableReferenceCount
extern('Shader') # TypedWritableReferenceCount
extern('RenderEffect') # TypedWritableReferenceCount
extern('Lens') # TypedWritableReferenceCount
extern('InternalName') # TypedWritableReferenceCount
extern('GraphicsOutputBase') # TypedWritableReferenceCount
extern('GraphicsOutput') # GraphicsOutputBase, DrawableRegion
extern('GraphicsWindow') # GraphicsOutput
extern('CachedTypedWritableReferenceCount') # TypedWritableReferenceCount
extern('NodeCachedReferenceCount') # CachedTypedWritableReferenceCount
extern('TransformState') # NodeCachedReferenceCount
extern('RenderState') # NodeCachedReferenceCount
extern('CopyOnWriteObject') # CachedTypedWritableReferenceCount
extern('GeomVertexData') # CopyOnWriteObject, GeomEnums
extern('GeomPrimitive') # CopyOnWriteObject, GeomEnums
extern('GeomTriangles') # GeomPrimitive
extern('Geom') # CopyOnWriteObject, GeomEnums
extern('GeomVertexArrayData') # CopyOnWriteObject, SimpleLruPage, GeomEnums
extern('PandaNode') # TypedWritableReferenceCount, Namable, LinkedListNode
extern('LensNode') # PandaNode
extern('Camera') # LensNode
extern('GeomNode') # PandaNode
extern('Fog') # PandaNode
extern('TextNode') # PandaNode, TextEncoder, TextProperties
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
        ('d', 'p', 1, ('p', 'ConfigPage$19$get_declaration', 'pl'), ['std::size_t']),
    ]
    c.ct['get_name'] = [
        ('d', 's', 0, ('s', 'ConfigPage$3$get_name', 'p'), []),
    ]
    c.ct['get_num_declarations'] = [
        ('d', 'l', 0, ('l', 'ConfigPage$18$get_num_declarations', 'p'), []),
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
        ('d', 's', 1, ('s', 'ConfigPage$22$get_string_value', 'pl'), ['std::size_t']),
    ]
    c.ct['get_trust_level'] = [
        ('d', 'i', 0, ('i', 'ConfigPage$9$get_trust_level', 'p'), []),
    ]
    c.ct['get_variable_name'] = [
        ('d', 's', 1, ('s', 'ConfigPage$21$get_variable_name', 'pl'), ['std::size_t']),
    ]
    c.ct['is_implicit'] = [
        ('d', 'B', 0, ('B', 'ConfigPage$5$is_implicit', 'p'), []),
    ]
    c.ct['is_special'] = [
        ('d', 'B', 0, ('B', 'ConfigPage$4$is_special', 'p'), []),
    ]
    c.ct['is_variable_used'] = [
        ('d', 'B', 1, ('B', 'ConfigPage$23$is_variable_used', 'pl'), ['std::size_t']),
    ]
    c.ct['make_declaration'] = [
        ('d', 'p', 2, ('p', 'ConfigPage$15$make_declaration', 'pps'), ['ConfigVariableCore*', 'std::string const&']),
        ('d', 'p', 2, ('p', 'ConfigPage$16$make_declaration', 'pss'), ['std::string const&', 'std::string const&']),
    ]
    c.ct['modify_declaration'] = [
        ('d', 'p', 1, ('p', 'ConfigPage$20$modify_declaration', 'pl'), ['std::size_t']),
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



class DrawableRegion(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("DrawableRegion", "upanda3d", """libupanda3d_c.so""")

    # enum RenderTexturePlane

    RTP_COUNT = const(16)
    RTP_aux_float_0 = const(11)
    RTP_aux_float_1 = const(12)
    RTP_aux_float_2 = const(13)
    RTP_aux_float_3 = const(14)
    RTP_aux_hrgba_0 = const(7)
    RTP_aux_hrgba_1 = const(8)
    RTP_aux_hrgba_2 = const(9)
    RTP_aux_hrgba_3 = const(10)
    RTP_aux_rgba_0 = const(3)
    RTP_aux_rgba_1 = const(4)
    RTP_aux_rgba_2 = const(5)
    RTP_aux_rgba_3 = const(6)
    RTP_color = const(2)
    RTP_depth = const(15)
    RTP_depth_stencil = const(1)
    RTP_stencil = const(0)


    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 1, 0, ('p', 'DrawableRegion$1$DrawableRegion', ''), []),
        ('s', 1, 1, ('p', 'DrawableRegion$2$DrawableRegion', 'p'), ['DrawableRegion const&']),
    ]

    # classmethod type calls

    c.ct['get_renderbuffer_type'] = [
        ('s', 'i', 1, ('i', 'DrawableRegion$26$get_renderbuffer_type', 'i'), ['int']),
    ]

    @classmethod
    def get_renderbuffer_type(cls, *args,**kw):
        return ( cls.c.get('get_renderbuffer_type', None) or cls.c.call(DrawableRegion, 'get_renderbuffer_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['copy_clear_settings'] = [
        ('d', 'v', 1, ('v', 'DrawableRegion$3$copy_clear_settings', 'pp'), ['DrawableRegion const&']),
    ]
    c.ct['disable_clears'] = [
        ('d', 'v', 0, ('v', 'DrawableRegion$20$disable_clears', 'p'), []),
    ]
    c.ct['downcast_to_DisplayRegion'] = [
        ('d', 61, 0, ('p', 'DrawableRegion$29$downcast_to_DisplayRegion', 'p'), []),
    ]
    c.ct['downcast_to_GraphicsOutput'] = [
        ('d', 74, 0, ('p', 'DrawableRegion$30$downcast_to_GraphicsOutput', 'p'), []),
    ]
    c.ct['get_clear_active'] = [
        ('d', 'B', 1, ('B', 'DrawableRegion$17$get_clear_active', 'pi'), ['int']),
    ]
    c.ct['get_clear_color'] = [
        ('d', 'p', 0, ('p', 'DrawableRegion$11$get_clear_color', 'p'), []),
    ]
    c.ct['get_clear_color_active'] = [
        ('d', 'B', 0, ('B', 'DrawableRegion$5$get_clear_color_active', 'p'), []),
    ]
    c.ct['get_clear_depth'] = [
        ('d', 'f', 0, ('f', 'DrawableRegion$13$get_clear_depth', 'p'), []),
    ]
    c.ct['get_clear_depth_active'] = [
        ('d', 'B', 0, ('B', 'DrawableRegion$7$get_clear_depth_active', 'p'), []),
    ]
    c.ct['get_clear_stencil'] = [
        ('d', 'I', 0, ('I', 'DrawableRegion$15$get_clear_stencil', 'p'), []),
    ]
    c.ct['get_clear_stencil_active'] = [
        ('d', 'B', 0, ('B', 'DrawableRegion$9$get_clear_stencil_active', 'p'), []),
    ]
    c.ct['get_clear_value'] = [
        ('d', 'p', 1, ('p', 'DrawableRegion$19$get_clear_value', 'pi'), ['int']),
    ]
    c.ct['get_draw_buffer_type'] = [
        ('d', 'i', 0, ('i', 'DrawableRegion$28$get_draw_buffer_type', 'p'), []),
    ]
    c.ct['get_pixel_factor'] = [
        ('d', 'f', 0, ('f', 'DrawableRegion$24$get_pixel_factor', 'p'), []),
    ]
    c.ct['get_pixel_zoom'] = [
        ('d', 'f', 0, ('f', 'DrawableRegion$23$get_pixel_zoom', 'p'), []),
    ]
    c.ct['get_screenshot_buffer_type'] = [
        ('d', 'i', 0, ('i', 'DrawableRegion$27$get_screenshot_buffer_type', 'p'), []),
    ]
    c.ct['is_any_clear_active'] = [
        ('d', 'B', 0, ('B', 'DrawableRegion$21$is_any_clear_active', 'p'), []),
    ]
    c.ct['set_clear_active'] = [
        ('d', 'v', 2, ('v', 'DrawableRegion$16$set_clear_active', 'piB'), ['int', 'bool']),
    ]
    c.ct['set_clear_color'] = [
        ('d', 'v', 1, ('v', 'DrawableRegion$10$set_clear_color', 'pp'), ['LColor const&']),
    ]
    c.ct['set_clear_color_active'] = [
        ('d', 'v', 1, ('v', 'DrawableRegion$4$set_clear_color_active', 'pB'), ['bool']),
    ]
    c.ct['set_clear_depth'] = [
        ('d', 'v', 1, ('v', 'DrawableRegion$12$set_clear_depth', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_clear_depth_active'] = [
        ('d', 'v', 1, ('v', 'DrawableRegion$6$set_clear_depth_active', 'pB'), ['bool']),
    ]
    c.ct['set_clear_stencil'] = [
        ('d', 'v', 1, ('v', 'DrawableRegion$14$set_clear_stencil', 'pI'), ['unsigned int']),
    ]
    c.ct['set_clear_stencil_active'] = [
        ('d', 'v', 1, ('v', 'DrawableRegion$8$set_clear_stencil_active', 'pB'), ['bool']),
    ]
    c.ct['set_clear_value'] = [
        ('d', 'v', 2, ('v', 'DrawableRegion$18$set_clear_value', 'pip'), ['int', 'LColor const&']),
    ]
    c.ct['set_pixel_zoom'] = [
        ('d', 'v', 1, ('v', 'DrawableRegion$22$set_pixel_zoom', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['supports_pixel_zoom'] = [
        ('d', 'B', 0, ('B', 'DrawableRegion$25$supports_pixel_zoom', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(DrawableRegion, attr, self)

DrawableRegion.c.link(DrawableRegion)



class Engine(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("Engine", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 2, 0, ('p', 'Engine$1$Engine', ''), []),
        ('s', 2, 1, ('p', 'Engine$2$Engine', 'p'), ['Engine const&']),
    ]

    # classmethod type calls

    c.ct['dec_ref'] = [
        ('s', 'i', 1, ('i', 'Engine$16$dec_ref', 'p'), ['ReferenceCount*']),
    ]
    c.ct['get_version_string'] = [
        ('s', 's', 0, ('s', 'Engine$21$get_version_string', ''), []),
    ]
    c.ct['inc_ref'] = [
        ('s', 'i', 1, ('i', 'Engine$15$inc_ref', 'p'), ['ReferenceCount*']),
    ]
    c.ct['is_alive'] = [
        ('s', 'i', 0, ('i', 'Engine$5$is_alive', ''), []),
    ]
    c.ct['prc'] = [
        ('s', 'v', 1, ('v', 'Engine$17$prc', 'p'), ['Filename const&']),
        ('s', 'v', 2, ('v', 'Engine$18$prc', 'ss'), ['char const*', 'char const*']),
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
    def prc(cls, *args,**kw):
        return ( cls.c.get('prc', None) or cls.c.call(Engine, 'prc', None) )(*args,**kw)

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
        ('d', 'v', 0, ('v', 'Engine$19$build', 'p'), []),
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
        ('d', 19, 0, ('p', 'Engine$24$get_framework', 'p'), []),
    ]
    c.ct['get_wframe'] = [
        ('d', 67, 0, ('p', 'Engine$22$get_wframe', 'p'), []),
    ]
    c.ct['load_model'] = [
        ('d', 17, 1, ('p', 'Engine$8$load_model', 'ps'), ['char const*']),
    ]
    c.ct['new_Cube'] = [
        ('d', 17, 3, ('p', 'Engine$13$new_Cube', 'pfss'), ['float', 'char const*', 'char const*']),
    ]
    c.ct['new_GeomTriangles'] = [
        ('d', 83, 0, ('p', 'Engine$12$new_GeomTriangles', 'p'), []),
    ]
    c.ct['new_GeomVertexWriter'] = [
        ('d', 29, 2, ('p', 'Engine$9$new_GeomVertexWriter', 'pps'), ['GeomVertexData*', 'char const*']),
    ]
    c.ct['set_framework'] = [
        ('d', 'v', 1, ('v', 'Engine$25$set_framework', 'pp'), ['PandaFramework*']),
    ]
    c.ct['set_wframe'] = [
        ('d', 'v', 1, ('v', 'Engine$23$set_wframe', 'pp'), ['WindowFramework*']),
    ]
    c.ct['step'] = [
        ('d', 'v', 0, ('v', 'Engine$20$step', 'p'), []),
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
        ('s', 3, 0, ('p', 'Filename$1$Filename', ''), []),
        ('s', 3, 1, ('p', 'Filename$2$Filename', 'p'), ['Filename&&']),
        ('s', 3, 1, ('p', 'Filename$3$Filename', 'p'), ['Filename const&']),
        ('s', 3, 2, ('p', 'Filename$4$Filename', 'pp'), ['Filename const&', 'Filename const&']),
        ('s', 3, 1, ('p', 'Filename$5$Filename', 's'), ['char const*']),
        ('s', 3, 1, ('p', 'Filename$6$Filename', 's'), ['std::string const&']),
        ('s', 3, 1, ('p', 'Filename$7$Filename', 's'), ['std::wstring const&']),
    ]

    # classmethod type calls

    c.ct['binary_filename'] = [
        ('s', 3, 1, ('p', 'Filename$10$binary_filename', 'p'), ['Filename const&']),
        ('s', 3, 1, ('p', 'Filename$11$binary_filename', 's'), ['std::string const&']),
    ]
    c.ct['dso_filename'] = [
        ('s', 3, 1, ('p', 'Filename$12$dso_filename', 's'), ['std::string const&']),
    ]
    c.ct['executable_filename'] = [
        ('s', 3, 1, ('p', 'Filename$13$executable_filename', 's'), ['std::string const&']),
    ]
    c.ct['expand_from'] = [
        ('s', 3, 2, ('p', 'Filename$19$expand_from', 'sp'), ['std::string const&', 'Filename::Type']),
        ('s', 3, 1, ('p', 'Filename$20$expand_from', 's'), ['std::string const&']),
    ]
    c.ct['from_os_specific'] = [
        ('s', 3, 2, ('p', 'Filename$15$from_os_specific', 'sp'), ['std::string const&', 'Filename::Type']),
        ('s', 3, 1, ('p', 'Filename$16$from_os_specific', 's'), ['std::string const&']),
    ]
    c.ct['from_os_specific_w'] = [
        ('s', 3, 2, ('p', 'Filename$17$from_os_specific_w', 'sp'), ['std::wstring const&', 'Filename::Type']),
        ('s', 3, 1, ('p', 'Filename$18$from_os_specific_w', 's'), ['std::wstring const&']),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'Filename$117$get_class_type', ''), []),
    ]
    c.ct['get_common_appdata_directory'] = [
        ('s', 3, 0, ('p', 'Filename$27$get_common_appdata_directory', ''), []),
    ]
    c.ct['get_filesystem_encoding'] = [
        ('s', 'p', 0, ('p', 'Filename$116$get_filesystem_encoding', ''), []),
    ]
    c.ct['get_home_directory'] = [
        ('s', 3, 0, ('p', 'Filename$24$get_home_directory', ''), []),
    ]
    c.ct['get_temp_directory'] = [
        ('s', 3, 0, ('p', 'Filename$25$get_temp_directory', ''), []),
    ]
    c.ct['get_user_appdata_directory'] = [
        ('s', 3, 0, ('p', 'Filename$26$get_user_appdata_directory', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'Filename$118$init_type', ''), []),
    ]
    c.ct['pattern_filename'] = [
        ('s', 3, 1, ('p', 'Filename$14$pattern_filename', 's'), ['std::string const&']),
    ]
    c.ct['set_filesystem_encoding'] = [
        ('s', 'v', 1, ('v', 'Filename$115$set_filesystem_encoding', 'p'), ['TextEncoder::Encoding']),
    ]
    c.ct['temporary'] = [
        ('s', 3, 4, ('p', 'Filename$21$temporary', 'sssp'), ['std::string const&', 'std::string const&', 'std::string const&', 'Filename::Type']),
        ('s', 3, 3, ('p', 'Filename$22$temporary', 'sss'), ['std::string const&', 'std::string const&', 'std::string const&']),
        ('s', 3, 2, ('p', 'Filename$23$temporary', 'ss'), ['std::string const&', 'std::string const&']),
    ]
    c.ct['text_filename'] = [
        ('s', 3, 1, ('p', 'Filename$8$text_filename', 'p'), ['Filename const&']),
        ('s', 3, 1, ('p', 'Filename$9$text_filename', 's'), ['std::string const&']),
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
        ('d', 'l', 0, ('l', 'Filename$82$get_file_size', 'p'), []),
    ]
    c.ct['get_filename_index'] = [
        ('d', 3, 1, ('p', 'Filename$56$get_filename_index', 'pi'), ['int']),
    ]
    c.ct['get_fullpath'] = [
        ('d', 's', 0, ('s', 'Filename$33$get_fullpath', 'p'), []),
    ]
    c.ct['get_fullpath_w'] = [
        ('d', 's', 0, ('s', 'Filename$34$get_fullpath_w', 'p'), []),
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
        ('d', 'l', 0, ('l', 'Filename$30$length', 'p'), []),
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
        ('d', 's', 1, ('s', 'Filename$31$substr', 'pl'), ['std::size_t']),
        ('d', 's', 2, ('s', 'Filename$32$substr', 'pll'), ['std::size_t', 'std::size_t']),
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
        ('d', 's', 0, ('s', 'Filename$68$to_os_specific_w', 'p'), []),
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



class FrameBufferProperties(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("FrameBufferProperties", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 4, 0, ('p', 'FrameBufferProperties$46$FrameBufferProperties', ''), []),
        ('s', 4, 1, ('p', 'FrameBufferProperties$47$FrameBufferProperties', 'p'), ['FrameBufferProperties const&']),
    ]

    # classmethod type calls

    c.ct['get_default'] = [
        ('s', 4, 0, ('p', 'FrameBufferProperties$48$get_default', ''), []),
    ]

    @classmethod
    def get_default(cls, *args,**kw):
        return ( cls.c.get('get_default', None) or cls.c.call(FrameBufferProperties, 'get_default', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_properties'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$52$add_properties', 'pp'), ['FrameBufferProperties const&']),
    ]
    c.ct['clear'] = [
        ('d', 'v', 0, ('v', 'FrameBufferProperties$49$clear', 'p'), []),
    ]
    c.ct['get_accum_bits'] = [
        ('d', 'i', 0, ('i', 'FrameBufferProperties$8$get_accum_bits', 'p'), []),
    ]
    c.ct['get_alpha_bits'] = [
        ('d', 'i', 0, ('i', 'FrameBufferProperties$6$get_alpha_bits', 'p'), []),
    ]
    c.ct['get_aux_float'] = [
        ('d', 'i', 0, ('i', 'FrameBufferProperties$11$get_aux_float', 'p'), []),
    ]
    c.ct['get_aux_hrgba'] = [
        ('d', 'i', 0, ('i', 'FrameBufferProperties$10$get_aux_hrgba', 'p'), []),
    ]
    c.ct['get_aux_mask'] = [
        ('d', 'i', 0, ('i', 'FrameBufferProperties$60$get_aux_mask', 'p'), []),
    ]
    c.ct['get_aux_rgba'] = [
        ('d', 'i', 0, ('i', 'FrameBufferProperties$9$get_aux_rgba', 'p'), []),
    ]
    c.ct['get_back_buffers'] = [
        ('d', 'i', 0, ('i', 'FrameBufferProperties$14$get_back_buffers', 'p'), []),
    ]
    c.ct['get_blue_bits'] = [
        ('d', 'i', 0, ('i', 'FrameBufferProperties$5$get_blue_bits', 'p'), []),
    ]
    c.ct['get_buffer_mask'] = [
        ('d', 'i', 0, ('i', 'FrameBufferProperties$61$get_buffer_mask', 'p'), []),
    ]
    c.ct['get_color_bits'] = [
        ('d', 'i', 0, ('i', 'FrameBufferProperties$2$get_color_bits', 'p'), []),
    ]
    c.ct['get_coverage_samples'] = [
        ('d', 'i', 0, ('i', 'FrameBufferProperties$13$get_coverage_samples', 'p'), []),
    ]
    c.ct['get_depth_bits'] = [
        ('d', 'i', 0, ('i', 'FrameBufferProperties$1$get_depth_bits', 'p'), []),
    ]
    c.ct['get_float_color'] = [
        ('d', 'B', 0, ('B', 'FrameBufferProperties$21$get_float_color', 'p'), []),
    ]
    c.ct['get_float_depth'] = [
        ('d', 'B', 0, ('B', 'FrameBufferProperties$22$get_float_depth', 'p'), []),
    ]
    c.ct['get_force_hardware'] = [
        ('d', 'B', 0, ('B', 'FrameBufferProperties$18$get_force_hardware', 'p'), []),
    ]
    c.ct['get_force_software'] = [
        ('d', 'B', 0, ('B', 'FrameBufferProperties$19$get_force_software', 'p'), []),
    ]
    c.ct['get_green_bits'] = [
        ('d', 'i', 0, ('i', 'FrameBufferProperties$4$get_green_bits', 'p'), []),
    ]
    c.ct['get_indexed_color'] = [
        ('d', 'B', 0, ('B', 'FrameBufferProperties$15$get_indexed_color', 'p'), []),
    ]
    c.ct['get_multisamples'] = [
        ('d', 'i', 0, ('i', 'FrameBufferProperties$12$get_multisamples', 'p'), []),
    ]
    c.ct['get_quality'] = [
        ('d', 'i', 1, ('i', 'FrameBufferProperties$57$get_quality', 'pp'), ['FrameBufferProperties const&']),
    ]
    c.ct['get_red_bits'] = [
        ('d', 'i', 0, ('i', 'FrameBufferProperties$3$get_red_bits', 'p'), []),
    ]
    c.ct['get_rgb_color'] = [
        ('d', 'B', 0, ('B', 'FrameBufferProperties$16$get_rgb_color', 'p'), []),
    ]
    c.ct['get_srgb_color'] = [
        ('d', 'B', 0, ('B', 'FrameBufferProperties$20$get_srgb_color', 'p'), []),
    ]
    c.ct['get_stencil_bits'] = [
        ('d', 'i', 0, ('i', 'FrameBufferProperties$7$get_stencil_bits', 'p'), []),
    ]
    c.ct['get_stereo'] = [
        ('d', 'B', 0, ('B', 'FrameBufferProperties$17$get_stereo', 'p'), []),
    ]
    c.ct['is_any_specified'] = [
        ('d', 'B', 0, ('B', 'FrameBufferProperties$58$is_any_specified', 'p'), []),
    ]
    c.ct['is_basic'] = [
        ('d', 'B', 0, ('B', 'FrameBufferProperties$59$is_basic', 'p'), []),
    ]
    c.ct['is_single_buffered'] = [
        ('d', 'B', 0, ('B', 'FrameBufferProperties$56$is_single_buffered', 'p'), []),
    ]
    c.ct['is_stereo'] = [
        ('d', 'B', 0, ('B', 'FrameBufferProperties$55$is_stereo', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$53$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['set_accum_bits'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$31$set_accum_bits', 'pi'), ['int']),
    ]
    c.ct['set_all_specified'] = [
        ('d', 'v', 0, ('v', 'FrameBufferProperties$50$set_all_specified', 'p'), []),
    ]
    c.ct['set_alpha_bits'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$29$set_alpha_bits', 'pi'), ['int']),
    ]
    c.ct['set_aux_float'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$34$set_aux_float', 'pi'), ['int']),
    ]
    c.ct['set_aux_hrgba'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$33$set_aux_hrgba', 'pi'), ['int']),
    ]
    c.ct['set_aux_rgba'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$32$set_aux_rgba', 'pi'), ['int']),
    ]
    c.ct['set_back_buffers'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$37$set_back_buffers', 'pi'), ['int']),
    ]
    c.ct['set_blue_bits'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$28$set_blue_bits', 'pi'), ['int']),
    ]
    c.ct['set_color_bits'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$24$set_color_bits', 'pi'), ['int']),
    ]
    c.ct['set_coverage_samples'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$36$set_coverage_samples', 'pi'), ['int']),
    ]
    c.ct['set_depth_bits'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$23$set_depth_bits', 'pi'), ['int']),
    ]
    c.ct['set_float_color'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$44$set_float_color', 'pB'), ['bool']),
    ]
    c.ct['set_float_depth'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$45$set_float_depth', 'pB'), ['bool']),
    ]
    c.ct['set_force_hardware'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$41$set_force_hardware', 'pB'), ['bool']),
    ]
    c.ct['set_force_software'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$42$set_force_software', 'pB'), ['bool']),
    ]
    c.ct['set_green_bits'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$27$set_green_bits', 'pi'), ['int']),
    ]
    c.ct['set_indexed_color'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$38$set_indexed_color', 'pB'), ['bool']),
    ]
    c.ct['set_multisamples'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$35$set_multisamples', 'pi'), ['int']),
    ]
    c.ct['set_one_bit_per_channel'] = [
        ('d', 'v', 0, ('v', 'FrameBufferProperties$54$set_one_bit_per_channel', 'p'), []),
    ]
    c.ct['set_red_bits'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$26$set_red_bits', 'pi'), ['int']),
    ]
    c.ct['set_rgb_color'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$39$set_rgb_color', 'pB'), ['bool']),
    ]
    c.ct['set_rgba_bits'] = [
        ('d', 'v', 4, ('v', 'FrameBufferProperties$25$set_rgba_bits', 'piiii'), ['int', 'int', 'int', 'int']),
    ]
    c.ct['set_srgb_color'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$43$set_srgb_color', 'pB'), ['bool']),
    ]
    c.ct['set_stencil_bits'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$30$set_stencil_bits', 'pi'), ['int']),
    ]
    c.ct['set_stereo'] = [
        ('d', 'v', 1, ('v', 'FrameBufferProperties$40$set_stereo', 'pB'), ['bool']),
    ]
    c.ct['setup_color_texture'] = [
        ('d', 'B', 1, ('B', 'FrameBufferProperties$63$setup_color_texture', 'pp'), ['Texture*']),
    ]
    c.ct['setup_depth_texture'] = [
        ('d', 'B', 1, ('B', 'FrameBufferProperties$64$setup_depth_texture', 'pp'), ['Texture*']),
    ]
    c.ct['subsumes'] = [
        ('d', 'B', 1, ('B', 'FrameBufferProperties$51$subsumes', 'pp'), ['FrameBufferProperties const&']),
    ]
    c.ct['verify_hardware_software'] = [
        ('d', 'B', 2, ('B', 'FrameBufferProperties$62$verify_hardware_software', 'pps'), ['FrameBufferProperties const&', 'std::string const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(FrameBufferProperties, attr, self)

FrameBufferProperties.c.link(FrameBufferProperties)



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
        ('s', 5, 0, ('p', 'GeomEnums$1$GeomEnums', ''), []),
        ('s', 5, 1, ('p', 'GeomEnums$2$GeomEnums', 'p'), ['GeomEnums const&']),
    ]

    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_Geom'] = [
        ('d', 84, 0, ('p', 'GeomEnums$3$downcast_to_Geom', 'p'), []),
    ]
    c.ct['downcast_to_GeomPrimitive'] = [
        ('d', 82, 0, ('p', 'GeomEnums$4$downcast_to_GeomPrimitive', 'p'), []),
    ]
    c.ct['downcast_to_GeomVertexArrayData'] = [
        ('d', 85, 0, ('p', 'GeomEnums$5$downcast_to_GeomVertexArrayData', 'p'), []),
    ]
    c.ct['downcast_to_GeomVertexArrayDataHandle'] = [
        ('d', 56, 0, ('p', 'GeomEnums$7$downcast_to_GeomVertexArrayDataHandle', 'p'), []),
    ]
    c.ct['downcast_to_GeomVertexArrayFormat'] = [
        ('d', 66, 0, ('p', 'GeomEnums$6$downcast_to_GeomVertexArrayFormat', 'p'), []),
    ]
    c.ct['downcast_to_GeomVertexData'] = [
        ('d', 81, 0, ('p', 'GeomEnums$8$downcast_to_GeomVertexData', 'p'), []),
    ]
    c.ct['downcast_to_GeomVertexFormat'] = [
        ('d', 65, 0, ('p', 'GeomEnums$9$downcast_to_GeomVertexFormat', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomEnums, attr, self)

GeomEnums.c.link(GeomEnums)



class LVecBase2d(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("LVecBase2d", "upanda3d", """libupanda3d_c.so""")

    # enum 



    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 6, 0, ('p', 'LVecBase2d$1$LVecBase2d', ''), []),
        ('s', 6, 1, ('p', 'LVecBase2d$2$LVecBase2d', 'p'), ['LVecBase2d const&']),
        ('s', 6, 1, ('p', 'LVecBase2d$3$LVecBase2d', 'p'), ['LVecBase2d::EVector2 const&']),
        ('s', 6, 1, ('p', 'LVecBase2d$4$LVecBase2d', 'd'), ['double']),
        ('s', 6, 2, ('p', 'LVecBase2d$5$LVecBase2d', 'dd'), ['double', 'double']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVecBase2d$53$get_class_type', ''), []),
    ]
    c.ct['get_num_components'] = [
        ('s', 'i', 0, ('i', 'LVecBase2d$21$get_num_components', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVecBase2d$54$init_type', ''), []),
    ]
    c.ct['size'] = [
        ('s', 'i', 0, ('i', 'LVecBase2d$9$size', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 'p', 0, ('p', 'LVecBase2d$7$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 'p', 0, ('p', 'LVecBase2d$8$unit_y', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 'p', 0, ('p', 'LVecBase2d$6$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LVecBase2d, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_num_components(cls, *args,**kw):
        return ( cls.c.get('get_num_components', None) or cls.c.call(LVecBase2d, 'get_num_components', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LVecBase2d, 'init_type', None) )(*args,**kw)

    @classmethod
    def size(cls, *args,**kw):
        return ( cls.c.get('size', None) or cls.c.call(LVecBase2d, 'size', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LVecBase2d, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LVecBase2d, 'unit_y', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LVecBase2d, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_hash'] = [
        ('d', 'l', 1, ('l', 'LVecBase2d$38$add_hash', 'pl'), ['std::size_t']),
        ('d', 'l', 2, ('l', 'LVecBase2d$39$add_hash', 'pld'), ['std::size_t', 'double']),
    ]
    c.ct['add_to_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase2d$17$add_to_cell', 'pid'), ['int', 'double']),
    ]
    c.ct['add_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase2d$18$add_x', 'pd'), ['double']),
    ]
    c.ct['add_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase2d$19$add_y', 'pd'), ['double']),
    ]
    c.ct['almost_equal'] = [
        ('d', 'B', 1, ('B', 'LVecBase2d$45$almost_equal', 'pp'), ['LVecBase2d const&']),
        ('d', 'B', 2, ('B', 'LVecBase2d$46$almost_equal', 'ppd'), ['LVecBase2d const&', 'double']),
    ]
    c.ct['begin'] = [
        ('d', 'v', 0, ('v', 'LVecBase2d$22$begin', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase2d$23$begin', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'LVecBase2d$34$compare_to', 'pp'), ['LVecBase2d const&']),
        ('d', 'i', 2, ('i', 'LVecBase2d$35$compare_to', 'ppd'), ['LVecBase2d const&', 'double']),
    ]
    c.ct['componentwise_mult'] = [
        ('d', 'v', 1, ('v', 'LVecBase2d$42$componentwise_mult', 'pp'), ['LVecBase2d const&']),
    ]
    c.ct['dot'] = [
        ('d', 'd', 1, ('d', 'LVecBase2d$28$dot', 'pp'), ['LVecBase2d const&']),
    ]
    c.ct['end'] = [
        ('d', 'v', 0, ('v', 'LVecBase2d$24$end', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase2d$25$end', 'p'), []),
    ]
    c.ct['fill'] = [
        ('d', 'v', 1, ('v', 'LVecBase2d$26$fill', 'pd'), ['double']),
    ]
    c.ct['fmax'] = [
        ('d', 'p', 1, ('p', 'LVecBase2d$43$fmax', 'pp'), ['LVecBase2d const&']),
    ]
    c.ct['fmin'] = [
        ('d', 'p', 1, ('p', 'LVecBase2d$44$fmin', 'pp'), ['LVecBase2d const&']),
    ]
    c.ct['generate_hash'] = [
        ('d', 'v', 1, ('v', 'LVecBase2d$40$generate_hash', 'pp'), ['ChecksumHashGenerator&']),
        ('d', 'v', 2, ('v', 'LVecBase2d$41$generate_hash', 'ppd'), ['ChecksumHashGenerator&', 'double']),
    ]
    c.ct['get_cell'] = [
        ('d', 'd', 1, ('d', 'LVecBase2d$11$get_cell', 'pi'), ['int']),
    ]
    c.ct['get_data'] = [
        ('d', 'v', 0, ('v', 'LVecBase2d$20$get_data', 'p'), []),
    ]
    c.ct['get_hash'] = [
        ('d', 'l', 0, ('l', 'LVecBase2d$36$get_hash', 'p'), []),
        ('d', 'l', 1, ('l', 'LVecBase2d$37$get_hash', 'pd'), ['double']),
    ]
    c.ct['get_v'] = [
        ('d', 'p', 0, ('p', 'LVecBase2d$52$get_v', 'p'), []),
    ]
    c.ct['get_x'] = [
        ('d', 'd', 0, ('d', 'LVecBase2d$13$get_x', 'p'), []),
    ]
    c.ct['get_y'] = [
        ('d', 'd', 0, ('d', 'LVecBase2d$14$get_y', 'p'), []),
    ]
    c.ct['is_nan'] = [
        ('d', 'B', 0, ('B', 'LVecBase2d$10$is_nan', 'p'), []),
    ]
    c.ct['length'] = [
        ('d', 'd', 0, ('d', 'LVecBase2d$30$length', 'p'), []),
    ]
    c.ct['length_squared'] = [
        ('d', 'd', 0, ('d', 'LVecBase2d$29$length_squared', 'p'), []),
    ]
    c.ct['normalize'] = [
        ('d', 'B', 0, ('B', 'LVecBase2d$31$normalize', 'p'), []),
    ]
    c.ct['normalized'] = [
        ('d', 'p', 0, ('p', 'LVecBase2d$32$normalized', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'LVecBase2d$47$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['project'] = [
        ('d', 'p', 1, ('p', 'LVecBase2d$33$project', 'pp'), ['LVecBase2d const&']),
    ]
    c.ct['read_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase2d$51$read_datagram', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['read_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase2d$49$read_datagram_fixed', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['set'] = [
        ('d', 'v', 2, ('v', 'LVecBase2d$27$set', 'pdd'), ['double', 'double']),
    ]
    c.ct['set_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase2d$12$set_cell', 'pid'), ['int', 'double']),
    ]
    c.ct['set_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase2d$15$set_x', 'pd'), ['double']),
    ]
    c.ct['set_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase2d$16$set_y', 'pd'), ['double']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase2d$50$write_datagram', 'pp'), ['Datagram&']),
    ]
    c.ct['write_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase2d$48$write_datagram_fixed', 'pp'), ['Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVecBase2d, attr, self)

LVecBase2d.c.link(LVecBase2d)



class LVecBase2f(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("LVecBase2f", "upanda3d", """libupanda3d_c.so""")

    # enum 



    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 7, 0, ('p', 'LVecBase2f$1$LVecBase2f', ''), []),
        ('s', 7, 1, ('p', 'LVecBase2f$2$LVecBase2f', 'p'), ['LVecBase2f const&']),
        ('s', 7, 1, ('p', 'LVecBase2f$3$LVecBase2f', 'p'), ['LVecBase2f::EVector2 const&']),
        ('s', 7, 1, ('p', 'LVecBase2f$4$LVecBase2f', 'f'), ['float']),
        ('s', 7, 2, ('p', 'LVecBase2f$5$LVecBase2f', 'ff'), ['float', 'float']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVecBase2f$53$get_class_type', ''), []),
    ]
    c.ct['get_num_components'] = [
        ('s', 'i', 0, ('i', 'LVecBase2f$21$get_num_components', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVecBase2f$54$init_type', ''), []),
    ]
    c.ct['size'] = [
        ('s', 'i', 0, ('i', 'LVecBase2f$9$size', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 7, 0, ('p', 'LVecBase2f$7$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 7, 0, ('p', 'LVecBase2f$8$unit_y', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 7, 0, ('p', 'LVecBase2f$6$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LVecBase2f, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_num_components(cls, *args,**kw):
        return ( cls.c.get('get_num_components', None) or cls.c.call(LVecBase2f, 'get_num_components', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LVecBase2f, 'init_type', None) )(*args,**kw)

    @classmethod
    def size(cls, *args,**kw):
        return ( cls.c.get('size', None) or cls.c.call(LVecBase2f, 'size', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LVecBase2f, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LVecBase2f, 'unit_y', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LVecBase2f, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_hash'] = [
        ('d', 'l', 1, ('l', 'LVecBase2f$38$add_hash', 'pl'), ['std::size_t']),
        ('d', 'l', 2, ('l', 'LVecBase2f$39$add_hash', 'plf'), ['std::size_t', 'float']),
    ]
    c.ct['add_to_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase2f$17$add_to_cell', 'pif'), ['int', 'float']),
    ]
    c.ct['add_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase2f$18$add_x', 'pf'), ['float']),
    ]
    c.ct['add_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase2f$19$add_y', 'pf'), ['float']),
    ]
    c.ct['almost_equal'] = [
        ('d', 'B', 1, ('B', 'LVecBase2f$45$almost_equal', 'pp'), ['LVecBase2f const&']),
        ('d', 'B', 2, ('B', 'LVecBase2f$46$almost_equal', 'ppf'), ['LVecBase2f const&', 'float']),
    ]
    c.ct['begin'] = [
        ('d', 'v', 0, ('v', 'LVecBase2f$22$begin', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase2f$23$begin', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'LVecBase2f$34$compare_to', 'pp'), ['LVecBase2f const&']),
        ('d', 'i', 2, ('i', 'LVecBase2f$35$compare_to', 'ppf'), ['LVecBase2f const&', 'float']),
    ]
    c.ct['componentwise_mult'] = [
        ('d', 'v', 1, ('v', 'LVecBase2f$42$componentwise_mult', 'pp'), ['LVecBase2f const&']),
    ]
    c.ct['dot'] = [
        ('d', 'f', 1, ('f', 'LVecBase2f$28$dot', 'pp'), ['LVecBase2f const&']),
    ]
    c.ct['end'] = [
        ('d', 'v', 0, ('v', 'LVecBase2f$24$end', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase2f$25$end', 'p'), []),
    ]
    c.ct['fill'] = [
        ('d', 'v', 1, ('v', 'LVecBase2f$26$fill', 'pf'), ['float']),
    ]
    c.ct['fmax'] = [
        ('d', 7, 1, ('p', 'LVecBase2f$43$fmax', 'pp'), ['LVecBase2f const&']),
    ]
    c.ct['fmin'] = [
        ('d', 7, 1, ('p', 'LVecBase2f$44$fmin', 'pp'), ['LVecBase2f const&']),
    ]
    c.ct['generate_hash'] = [
        ('d', 'v', 1, ('v', 'LVecBase2f$40$generate_hash', 'pp'), ['ChecksumHashGenerator&']),
        ('d', 'v', 2, ('v', 'LVecBase2f$41$generate_hash', 'ppf'), ['ChecksumHashGenerator&', 'float']),
    ]
    c.ct['get_cell'] = [
        ('d', 'f', 1, ('f', 'LVecBase2f$11$get_cell', 'pi'), ['int']),
    ]
    c.ct['get_data'] = [
        ('d', 'v', 0, ('v', 'LVecBase2f$20$get_data', 'p'), []),
    ]
    c.ct['get_hash'] = [
        ('d', 'l', 0, ('l', 'LVecBase2f$36$get_hash', 'p'), []),
        ('d', 'l', 1, ('l', 'LVecBase2f$37$get_hash', 'pf'), ['float']),
    ]
    c.ct['get_v'] = [
        ('d', 'p', 0, ('p', 'LVecBase2f$52$get_v', 'p'), []),
    ]
    c.ct['get_x'] = [
        ('d', 'f', 0, ('f', 'LVecBase2f$13$get_x', 'p'), []),
    ]
    c.ct['get_y'] = [
        ('d', 'f', 0, ('f', 'LVecBase2f$14$get_y', 'p'), []),
    ]
    c.ct['is_nan'] = [
        ('d', 'B', 0, ('B', 'LVecBase2f$10$is_nan', 'p'), []),
    ]
    c.ct['length'] = [
        ('d', 'f', 0, ('f', 'LVecBase2f$30$length', 'p'), []),
    ]
    c.ct['length_squared'] = [
        ('d', 'f', 0, ('f', 'LVecBase2f$29$length_squared', 'p'), []),
    ]
    c.ct['normalize'] = [
        ('d', 'B', 0, ('B', 'LVecBase2f$31$normalize', 'p'), []),
    ]
    c.ct['normalized'] = [
        ('d', 7, 0, ('p', 'LVecBase2f$32$normalized', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'LVecBase2f$47$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['project'] = [
        ('d', 7, 1, ('p', 'LVecBase2f$33$project', 'pp'), ['LVecBase2f const&']),
    ]
    c.ct['read_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase2f$51$read_datagram', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['read_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase2f$49$read_datagram_fixed', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['set'] = [
        ('d', 'v', 2, ('v', 'LVecBase2f$27$set', 'pff'), ['float', 'float']),
    ]
    c.ct['set_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase2f$12$set_cell', 'pif'), ['int', 'float']),
    ]
    c.ct['set_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase2f$15$set_x', 'pf'), ['float']),
    ]
    c.ct['set_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase2f$16$set_y', 'pf'), ['float']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase2f$50$write_datagram', 'pp'), ['Datagram&']),
    ]
    c.ct['write_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase2f$48$write_datagram_fixed', 'pp'), ['Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVecBase2f, attr, self)

LVecBase2f.c.link(LVecBase2f)



class LVecBase2i(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("LVecBase2i", "upanda3d", """libupanda3d_c.so""")

    # enum 



    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 8, 0, ('p', 'LVecBase2i$1$LVecBase2i', ''), []),
        ('s', 8, 1, ('p', 'LVecBase2i$2$LVecBase2i', 'p'), ['LVecBase2i const&']),
        ('s', 8, 1, ('p', 'LVecBase2i$3$LVecBase2i', 'p'), ['LVecBase2i::EVector2 const&']),
        ('s', 8, 1, ('p', 'LVecBase2i$4$LVecBase2i', 'i'), ['int']),
        ('s', 8, 2, ('p', 'LVecBase2i$5$LVecBase2i', 'ii'), ['int', 'int']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVecBase2i$45$get_class_type', ''), []),
    ]
    c.ct['get_num_components'] = [
        ('s', 'i', 0, ('i', 'LVecBase2i$21$get_num_components', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVecBase2i$46$init_type', ''), []),
    ]
    c.ct['size'] = [
        ('s', 'i', 0, ('i', 'LVecBase2i$9$size', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 'p', 0, ('p', 'LVecBase2i$7$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 'p', 0, ('p', 'LVecBase2i$8$unit_y', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 'p', 0, ('p', 'LVecBase2i$6$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LVecBase2i, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_num_components(cls, *args,**kw):
        return ( cls.c.get('get_num_components', None) or cls.c.call(LVecBase2i, 'get_num_components', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LVecBase2i, 'init_type', None) )(*args,**kw)

    @classmethod
    def size(cls, *args,**kw):
        return ( cls.c.get('size', None) or cls.c.call(LVecBase2i, 'size', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LVecBase2i, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LVecBase2i, 'unit_y', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LVecBase2i, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_hash'] = [
        ('d', 'l', 1, ('l', 'LVecBase2i$32$add_hash', 'pl'), ['std::size_t']),
    ]
    c.ct['add_to_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase2i$17$add_to_cell', 'pii'), ['int', 'int']),
    ]
    c.ct['add_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase2i$18$add_x', 'pi'), ['int']),
    ]
    c.ct['add_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase2i$19$add_y', 'pi'), ['int']),
    ]
    c.ct['almost_equal'] = [
        ('d', 'B', 1, ('B', 'LVecBase2i$37$almost_equal', 'pp'), ['LVecBase2i const&']),
        ('d', 'B', 2, ('B', 'LVecBase2i$38$almost_equal', 'ppi'), ['LVecBase2i const&', 'int']),
    ]
    c.ct['begin'] = [
        ('d', 'v', 0, ('v', 'LVecBase2i$22$begin', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase2i$23$begin', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'LVecBase2i$30$compare_to', 'pp'), ['LVecBase2i const&']),
    ]
    c.ct['componentwise_mult'] = [
        ('d', 'v', 1, ('v', 'LVecBase2i$34$componentwise_mult', 'pp'), ['LVecBase2i const&']),
    ]
    c.ct['dot'] = [
        ('d', 'i', 1, ('i', 'LVecBase2i$28$dot', 'pp'), ['LVecBase2i const&']),
    ]
    c.ct['end'] = [
        ('d', 'v', 0, ('v', 'LVecBase2i$24$end', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase2i$25$end', 'p'), []),
    ]
    c.ct['fill'] = [
        ('d', 'v', 1, ('v', 'LVecBase2i$26$fill', 'pi'), ['int']),
    ]
    c.ct['fmax'] = [
        ('d', 'p', 1, ('p', 'LVecBase2i$35$fmax', 'pp'), ['LVecBase2i const&']),
    ]
    c.ct['fmin'] = [
        ('d', 'p', 1, ('p', 'LVecBase2i$36$fmin', 'pp'), ['LVecBase2i const&']),
    ]
    c.ct['generate_hash'] = [
        ('d', 'v', 1, ('v', 'LVecBase2i$33$generate_hash', 'pp'), ['ChecksumHashGenerator&']),
    ]
    c.ct['get_cell'] = [
        ('d', 'i', 1, ('i', 'LVecBase2i$11$get_cell', 'pi'), ['int']),
    ]
    c.ct['get_data'] = [
        ('d', 'v', 0, ('v', 'LVecBase2i$20$get_data', 'p'), []),
    ]
    c.ct['get_hash'] = [
        ('d', 'l', 0, ('l', 'LVecBase2i$31$get_hash', 'p'), []),
    ]
    c.ct['get_v'] = [
        ('d', 'p', 0, ('p', 'LVecBase2i$44$get_v', 'p'), []),
    ]
    c.ct['get_x'] = [
        ('d', 'i', 0, ('i', 'LVecBase2i$13$get_x', 'p'), []),
    ]
    c.ct['get_y'] = [
        ('d', 'i', 0, ('i', 'LVecBase2i$14$get_y', 'p'), []),
    ]
    c.ct['is_nan'] = [
        ('d', 'B', 0, ('B', 'LVecBase2i$10$is_nan', 'p'), []),
    ]
    c.ct['length_squared'] = [
        ('d', 'i', 0, ('i', 'LVecBase2i$29$length_squared', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'LVecBase2i$39$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['read_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase2i$43$read_datagram', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['read_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase2i$41$read_datagram_fixed', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['set'] = [
        ('d', 'v', 2, ('v', 'LVecBase2i$27$set', 'pii'), ['int', 'int']),
    ]
    c.ct['set_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase2i$12$set_cell', 'pii'), ['int', 'int']),
    ]
    c.ct['set_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase2i$15$set_x', 'pi'), ['int']),
    ]
    c.ct['set_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase2i$16$set_y', 'pi'), ['int']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase2i$42$write_datagram', 'pp'), ['Datagram&']),
    ]
    c.ct['write_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase2i$40$write_datagram_fixed', 'pp'), ['Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVecBase2i, attr, self)

LVecBase2i.c.link(LVecBase2i)



class LVecBase3d(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("LVecBase3d", "upanda3d", """libupanda3d_c.so""")

    # enum 



    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 9, 0, ('p', 'LVecBase3d$1$LVecBase3d', ''), []),
        ('s', 9, 2, ('p', 'LVecBase3d$2$LVecBase3d', 'pd'), ['LVecBase2d const&', 'double']),
        ('s', 9, 1, ('p', 'LVecBase3d$3$LVecBase3d', 'p'), ['LVecBase3d const&']),
        ('s', 9, 1, ('p', 'LVecBase3d$4$LVecBase3d', 'p'), ['LVecBase3d::EVector3 const&']),
        ('s', 9, 1, ('p', 'LVecBase3d$5$LVecBase3d', 'd'), ['double']),
        ('s', 9, 3, ('p', 'LVecBase3d$6$LVecBase3d', 'ddd'), ['double', 'double', 'double']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVecBase3d$64$get_class_type', ''), []),
    ]
    c.ct['get_num_components'] = [
        ('s', 'i', 0, ('i', 'LVecBase3d$29$get_num_components', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVecBase3d$65$init_type', ''), []),
    ]
    c.ct['size'] = [
        ('s', 'i', 0, ('i', 'LVecBase3d$11$size', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 'p', 0, ('p', 'LVecBase3d$8$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 'p', 0, ('p', 'LVecBase3d$9$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 'p', 0, ('p', 'LVecBase3d$10$unit_z', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 'p', 0, ('p', 'LVecBase3d$7$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LVecBase3d, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_num_components(cls, *args,**kw):
        return ( cls.c.get('get_num_components', None) or cls.c.call(LVecBase3d, 'get_num_components', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LVecBase3d, 'init_type', None) )(*args,**kw)

    @classmethod
    def size(cls, *args,**kw):
        return ( cls.c.get('size', None) or cls.c.call(LVecBase3d, 'size', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LVecBase3d, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LVecBase3d, 'unit_y', None) )(*args,**kw)

    @classmethod
    def unit_z(cls, *args,**kw):
        return ( cls.c.get('unit_z', None) or cls.c.call(LVecBase3d, 'unit_z', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LVecBase3d, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_hash'] = [
        ('d', 'l', 1, ('l', 'LVecBase3d$48$add_hash', 'pl'), ['std::size_t']),
        ('d', 'l', 2, ('l', 'LVecBase3d$49$add_hash', 'pld'), ['std::size_t', 'double']),
    ]
    c.ct['add_to_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase3d$24$add_to_cell', 'pid'), ['int', 'double']),
    ]
    c.ct['add_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase3d$25$add_x', 'pd'), ['double']),
    ]
    c.ct['add_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase3d$26$add_y', 'pd'), ['double']),
    ]
    c.ct['add_z'] = [
        ('d', 'v', 1, ('v', 'LVecBase3d$27$add_z', 'pd'), ['double']),
    ]
    c.ct['almost_equal'] = [
        ('d', 'B', 1, ('B', 'LVecBase3d$56$almost_equal', 'pp'), ['LVecBase3d const&']),
        ('d', 'B', 2, ('B', 'LVecBase3d$57$almost_equal', 'ppd'), ['LVecBase3d const&', 'double']),
    ]
    c.ct['begin'] = [
        ('d', 'v', 0, ('v', 'LVecBase3d$30$begin', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase3d$31$begin', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'LVecBase3d$44$compare_to', 'pp'), ['LVecBase3d const&']),
        ('d', 'i', 2, ('i', 'LVecBase3d$45$compare_to', 'ppd'), ['LVecBase3d const&', 'double']),
    ]
    c.ct['componentwise_mult'] = [
        ('d', 'v', 1, ('v', 'LVecBase3d$52$componentwise_mult', 'pp'), ['LVecBase3d const&']),
    ]
    c.ct['cross'] = [
        ('d', 'p', 1, ('p', 'LVecBase3d$42$cross', 'pp'), ['LVecBase3d const&']),
    ]
    c.ct['cross_into'] = [
        ('d', 'v', 1, ('v', 'LVecBase3d$55$cross_into', 'pp'), ['LVecBase3d const&']),
    ]
    c.ct['dot'] = [
        ('d', 'd', 1, ('d', 'LVecBase3d$36$dot', 'pp'), ['LVecBase3d const&']),
    ]
    c.ct['end'] = [
        ('d', 'v', 0, ('v', 'LVecBase3d$32$end', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase3d$33$end', 'p'), []),
    ]
    c.ct['fill'] = [
        ('d', 'v', 1, ('v', 'LVecBase3d$34$fill', 'pd'), ['double']),
    ]
    c.ct['fmax'] = [
        ('d', 'p', 1, ('p', 'LVecBase3d$53$fmax', 'pp'), ['LVecBase3d const&']),
    ]
    c.ct['fmin'] = [
        ('d', 'p', 1, ('p', 'LVecBase3d$54$fmin', 'pp'), ['LVecBase3d const&']),
    ]
    c.ct['generate_hash'] = [
        ('d', 'v', 1, ('v', 'LVecBase3d$50$generate_hash', 'pp'), ['ChecksumHashGenerator&']),
        ('d', 'v', 2, ('v', 'LVecBase3d$51$generate_hash', 'ppd'), ['ChecksumHashGenerator&', 'double']),
    ]
    c.ct['get_cell'] = [
        ('d', 'd', 1, ('d', 'LVecBase3d$13$get_cell', 'pi'), ['int']),
    ]
    c.ct['get_data'] = [
        ('d', 'v', 0, ('v', 'LVecBase3d$28$get_data', 'p'), []),
    ]
    c.ct['get_hash'] = [
        ('d', 'l', 0, ('l', 'LVecBase3d$46$get_hash', 'p'), []),
        ('d', 'l', 1, ('l', 'LVecBase3d$47$get_hash', 'pd'), ['double']),
    ]
    c.ct['get_standardized_hpr'] = [
        ('d', 'p', 0, ('p', 'LVecBase3d$43$get_standardized_hpr', 'p'), []),
    ]
    c.ct['get_v'] = [
        ('d', 'p', 0, ('p', 'LVecBase3d$63$get_v', 'p'), []),
    ]
    c.ct['get_x'] = [
        ('d', 'd', 0, ('d', 'LVecBase3d$14$get_x', 'p'), []),
    ]
    c.ct['get_xy'] = [
        ('d', 'p', 0, ('p', 'LVecBase3d$21$get_xy', 'p'), []),
    ]
    c.ct['get_xz'] = [
        ('d', 'p', 0, ('p', 'LVecBase3d$22$get_xz', 'p'), []),
    ]
    c.ct['get_y'] = [
        ('d', 'd', 0, ('d', 'LVecBase3d$15$get_y', 'p'), []),
    ]
    c.ct['get_yz'] = [
        ('d', 'p', 0, ('p', 'LVecBase3d$23$get_yz', 'p'), []),
    ]
    c.ct['get_z'] = [
        ('d', 'd', 0, ('d', 'LVecBase3d$16$get_z', 'p'), []),
    ]
    c.ct['is_nan'] = [
        ('d', 'B', 0, ('B', 'LVecBase3d$12$is_nan', 'p'), []),
    ]
    c.ct['length'] = [
        ('d', 'd', 0, ('d', 'LVecBase3d$38$length', 'p'), []),
    ]
    c.ct['length_squared'] = [
        ('d', 'd', 0, ('d', 'LVecBase3d$37$length_squared', 'p'), []),
    ]
    c.ct['normalize'] = [
        ('d', 'B', 0, ('B', 'LVecBase3d$39$normalize', 'p'), []),
    ]
    c.ct['normalized'] = [
        ('d', 'p', 0, ('p', 'LVecBase3d$40$normalized', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'LVecBase3d$58$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['project'] = [
        ('d', 'p', 1, ('p', 'LVecBase3d$41$project', 'pp'), ['LVecBase3d const&']),
    ]
    c.ct['read_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase3d$62$read_datagram', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['read_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase3d$60$read_datagram_fixed', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['set'] = [
        ('d', 'v', 3, ('v', 'LVecBase3d$35$set', 'pddd'), ['double', 'double', 'double']),
    ]
    c.ct['set_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase3d$17$set_cell', 'pid'), ['int', 'double']),
    ]
    c.ct['set_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase3d$18$set_x', 'pd'), ['double']),
    ]
    c.ct['set_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase3d$19$set_y', 'pd'), ['double']),
    ]
    c.ct['set_z'] = [
        ('d', 'v', 1, ('v', 'LVecBase3d$20$set_z', 'pd'), ['double']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase3d$61$write_datagram', 'pp'), ['Datagram&']),
    ]
    c.ct['write_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase3d$59$write_datagram_fixed', 'pp'), ['Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVecBase3d, attr, self)

LVecBase3d.c.link(LVecBase3d)



class LVecBase3f(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("LVecBase3f", "upanda3d", """libupanda3d_c.so""")

    # enum 



    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 10, 0, ('p', 'LVecBase3f$1$LVecBase3f', ''), []),
        ('s', 10, 2, ('p', 'LVecBase3f$2$LVecBase3f', 'pf'), ['LVecBase2f const&', 'float']),
        ('s', 10, 1, ('p', 'LVecBase3f$3$LVecBase3f', 'p'), ['LVecBase3f const&']),
        ('s', 10, 1, ('p', 'LVecBase3f$4$LVecBase3f', 'p'), ['LVecBase3f::EVector3 const&']),
        ('s', 10, 1, ('p', 'LVecBase3f$5$LVecBase3f', 'f'), ['float']),
        ('s', 10, 3, ('p', 'LVecBase3f$6$LVecBase3f', 'fff'), ['float', 'float', 'float']),
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
        ('s', 10, 0, ('p', 'LVecBase3f$8$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 10, 0, ('p', 'LVecBase3f$9$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 10, 0, ('p', 'LVecBase3f$10$unit_z', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 10, 0, ('p', 'LVecBase3f$7$zero', ''), []),
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
        ('d', 'l', 1, ('l', 'LVecBase3f$48$add_hash', 'pl'), ['std::size_t']),
        ('d', 'l', 2, ('l', 'LVecBase3f$49$add_hash', 'plf'), ['std::size_t', 'float']),
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
        ('d', 10, 1, ('p', 'LVecBase3f$42$cross', 'pp'), ['LVecBase3f const&']),
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
        ('d', 10, 1, ('p', 'LVecBase3f$53$fmax', 'pp'), ['LVecBase3f const&']),
    ]
    c.ct['fmin'] = [
        ('d', 10, 1, ('p', 'LVecBase3f$54$fmin', 'pp'), ['LVecBase3f const&']),
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
        ('d', 'l', 0, ('l', 'LVecBase3f$46$get_hash', 'p'), []),
        ('d', 'l', 1, ('l', 'LVecBase3f$47$get_hash', 'pf'), ['float']),
    ]
    c.ct['get_standardized_hpr'] = [
        ('d', 10, 0, ('p', 'LVecBase3f$43$get_standardized_hpr', 'p'), []),
    ]
    c.ct['get_v'] = [
        ('d', 'p', 0, ('p', 'LVecBase3f$63$get_v', 'p'), []),
    ]
    c.ct['get_x'] = [
        ('d', 'f', 0, ('f', 'LVecBase3f$14$get_x', 'p'), []),
    ]
    c.ct['get_xy'] = [
        ('d', 7, 0, ('p', 'LVecBase3f$21$get_xy', 'p'), []),
    ]
    c.ct['get_xz'] = [
        ('d', 7, 0, ('p', 'LVecBase3f$22$get_xz', 'p'), []),
    ]
    c.ct['get_y'] = [
        ('d', 'f', 0, ('f', 'LVecBase3f$15$get_y', 'p'), []),
    ]
    c.ct['get_yz'] = [
        ('d', 7, 0, ('p', 'LVecBase3f$23$get_yz', 'p'), []),
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
        ('d', 10, 0, ('p', 'LVecBase3f$40$normalized', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'LVecBase3f$58$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['project'] = [
        ('d', 10, 1, ('p', 'LVecBase3f$41$project', 'pp'), ['LVecBase3f const&']),
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



class LVecBase3i(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("LVecBase3i", "upanda3d", """libupanda3d_c.so""")

    # enum 



    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 11, 0, ('p', 'LVecBase3i$1$LVecBase3i', ''), []),
        ('s', 11, 2, ('p', 'LVecBase3i$2$LVecBase3i', 'pi'), ['LVecBase2i const&', 'int']),
        ('s', 11, 1, ('p', 'LVecBase3i$3$LVecBase3i', 'p'), ['LVecBase3i const&']),
        ('s', 11, 1, ('p', 'LVecBase3i$4$LVecBase3i', 'p'), ['LVecBase3i::EVector3 const&']),
        ('s', 11, 1, ('p', 'LVecBase3i$5$LVecBase3i', 'i'), ['int']),
        ('s', 11, 3, ('p', 'LVecBase3i$6$LVecBase3i', 'iii'), ['int', 'int', 'int']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVecBase3i$55$get_class_type', ''), []),
    ]
    c.ct['get_num_components'] = [
        ('s', 'i', 0, ('i', 'LVecBase3i$29$get_num_components', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVecBase3i$56$init_type', ''), []),
    ]
    c.ct['size'] = [
        ('s', 'i', 0, ('i', 'LVecBase3i$11$size', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 'p', 0, ('p', 'LVecBase3i$8$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 'p', 0, ('p', 'LVecBase3i$9$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 'p', 0, ('p', 'LVecBase3i$10$unit_z', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 'p', 0, ('p', 'LVecBase3i$7$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LVecBase3i, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_num_components(cls, *args,**kw):
        return ( cls.c.get('get_num_components', None) or cls.c.call(LVecBase3i, 'get_num_components', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LVecBase3i, 'init_type', None) )(*args,**kw)

    @classmethod
    def size(cls, *args,**kw):
        return ( cls.c.get('size', None) or cls.c.call(LVecBase3i, 'size', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LVecBase3i, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LVecBase3i, 'unit_y', None) )(*args,**kw)

    @classmethod
    def unit_z(cls, *args,**kw):
        return ( cls.c.get('unit_z', None) or cls.c.call(LVecBase3i, 'unit_z', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LVecBase3i, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_hash'] = [
        ('d', 'l', 1, ('l', 'LVecBase3i$41$add_hash', 'pl'), ['std::size_t']),
    ]
    c.ct['add_to_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase3i$24$add_to_cell', 'pii'), ['int', 'int']),
    ]
    c.ct['add_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase3i$25$add_x', 'pi'), ['int']),
    ]
    c.ct['add_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase3i$26$add_y', 'pi'), ['int']),
    ]
    c.ct['add_z'] = [
        ('d', 'v', 1, ('v', 'LVecBase3i$27$add_z', 'pi'), ['int']),
    ]
    c.ct['almost_equal'] = [
        ('d', 'B', 1, ('B', 'LVecBase3i$47$almost_equal', 'pp'), ['LVecBase3i const&']),
        ('d', 'B', 2, ('B', 'LVecBase3i$48$almost_equal', 'ppi'), ['LVecBase3i const&', 'int']),
    ]
    c.ct['begin'] = [
        ('d', 'v', 0, ('v', 'LVecBase3i$30$begin', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase3i$31$begin', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'LVecBase3i$39$compare_to', 'pp'), ['LVecBase3i const&']),
    ]
    c.ct['componentwise_mult'] = [
        ('d', 'v', 1, ('v', 'LVecBase3i$43$componentwise_mult', 'pp'), ['LVecBase3i const&']),
    ]
    c.ct['cross'] = [
        ('d', 'p', 1, ('p', 'LVecBase3i$38$cross', 'pp'), ['LVecBase3i const&']),
    ]
    c.ct['cross_into'] = [
        ('d', 'v', 1, ('v', 'LVecBase3i$46$cross_into', 'pp'), ['LVecBase3i const&']),
    ]
    c.ct['dot'] = [
        ('d', 'i', 1, ('i', 'LVecBase3i$36$dot', 'pp'), ['LVecBase3i const&']),
    ]
    c.ct['end'] = [
        ('d', 'v', 0, ('v', 'LVecBase3i$32$end', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase3i$33$end', 'p'), []),
    ]
    c.ct['fill'] = [
        ('d', 'v', 1, ('v', 'LVecBase3i$34$fill', 'pi'), ['int']),
    ]
    c.ct['fmax'] = [
        ('d', 'p', 1, ('p', 'LVecBase3i$44$fmax', 'pp'), ['LVecBase3i const&']),
    ]
    c.ct['fmin'] = [
        ('d', 'p', 1, ('p', 'LVecBase3i$45$fmin', 'pp'), ['LVecBase3i const&']),
    ]
    c.ct['generate_hash'] = [
        ('d', 'v', 1, ('v', 'LVecBase3i$42$generate_hash', 'pp'), ['ChecksumHashGenerator&']),
    ]
    c.ct['get_cell'] = [
        ('d', 'i', 1, ('i', 'LVecBase3i$13$get_cell', 'pi'), ['int']),
    ]
    c.ct['get_data'] = [
        ('d', 'v', 0, ('v', 'LVecBase3i$28$get_data', 'p'), []),
    ]
    c.ct['get_hash'] = [
        ('d', 'l', 0, ('l', 'LVecBase3i$40$get_hash', 'p'), []),
    ]
    c.ct['get_v'] = [
        ('d', 'p', 0, ('p', 'LVecBase3i$54$get_v', 'p'), []),
    ]
    c.ct['get_x'] = [
        ('d', 'i', 0, ('i', 'LVecBase3i$14$get_x', 'p'), []),
    ]
    c.ct['get_xy'] = [
        ('d', 'p', 0, ('p', 'LVecBase3i$21$get_xy', 'p'), []),
    ]
    c.ct['get_xz'] = [
        ('d', 'p', 0, ('p', 'LVecBase3i$22$get_xz', 'p'), []),
    ]
    c.ct['get_y'] = [
        ('d', 'i', 0, ('i', 'LVecBase3i$15$get_y', 'p'), []),
    ]
    c.ct['get_yz'] = [
        ('d', 'p', 0, ('p', 'LVecBase3i$23$get_yz', 'p'), []),
    ]
    c.ct['get_z'] = [
        ('d', 'i', 0, ('i', 'LVecBase3i$16$get_z', 'p'), []),
    ]
    c.ct['is_nan'] = [
        ('d', 'B', 0, ('B', 'LVecBase3i$12$is_nan', 'p'), []),
    ]
    c.ct['length_squared'] = [
        ('d', 'i', 0, ('i', 'LVecBase3i$37$length_squared', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'LVecBase3i$49$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['read_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase3i$53$read_datagram', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['read_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase3i$51$read_datagram_fixed', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['set'] = [
        ('d', 'v', 3, ('v', 'LVecBase3i$35$set', 'piii'), ['int', 'int', 'int']),
    ]
    c.ct['set_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase3i$17$set_cell', 'pii'), ['int', 'int']),
    ]
    c.ct['set_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase3i$18$set_x', 'pi'), ['int']),
    ]
    c.ct['set_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase3i$19$set_y', 'pi'), ['int']),
    ]
    c.ct['set_z'] = [
        ('d', 'v', 1, ('v', 'LVecBase3i$20$set_z', 'pi'), ['int']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase3i$52$write_datagram', 'pp'), ['Datagram&']),
    ]
    c.ct['write_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase3i$50$write_datagram_fixed', 'pp'), ['Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVecBase3i, attr, self)

LVecBase3i.c.link(LVecBase3i)



class LVecBase4d(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("LVecBase4d", "upanda3d", """libupanda3d_c.so""")

    # enum 



    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 12, 0, ('p', 'LVecBase4d$1$LVecBase4d', ''), []),
        ('s', 12, 1, ('p', 'LVecBase4d$2$LVecBase4d', 'p'), ['LPoint3d const&']),
        ('s', 12, 2, ('p', 'LVecBase4d$3$LVecBase4d', 'pd'), ['LVecBase3d const&', 'double']),
        ('s', 12, 1, ('p', 'LVecBase4d$4$LVecBase4d', 'p'), ['LVecBase4d const&']),
        ('s', 12, 1, ('p', 'LVecBase4d$5$LVecBase4d', 'p'), ['LVecBase4d::EVector4 const&']),
        ('s', 12, 1, ('p', 'LVecBase4d$6$LVecBase4d', 'p'), ['LVector3d const&']),
        ('s', 12, 1, ('p', 'LVecBase4d$7$LVecBase4d', 'p'), ['UnalignedLVecBase4d const&']),
        ('s', 12, 1, ('p', 'LVecBase4d$8$LVecBase4d', 'd'), ['double']),
        ('s', 12, 4, ('p', 'LVecBase4d$9$LVecBase4d', 'dddd'), ['double', 'double', 'double', 'double']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVecBase4d$67$get_class_type', ''), []),
    ]
    c.ct['get_num_components'] = [
        ('s', 'i', 0, ('i', 'LVecBase4d$35$get_num_components', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVecBase4d$68$init_type', ''), []),
    ]
    c.ct['size'] = [
        ('s', 'i', 0, ('i', 'LVecBase4d$15$size', ''), []),
    ]
    c.ct['unit_w'] = [
        ('s', 'p', 0, ('p', 'LVecBase4d$14$unit_w', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 'p', 0, ('p', 'LVecBase4d$11$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 'p', 0, ('p', 'LVecBase4d$12$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 'p', 0, ('p', 'LVecBase4d$13$unit_z', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 'p', 0, ('p', 'LVecBase4d$10$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LVecBase4d, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_num_components(cls, *args,**kw):
        return ( cls.c.get('get_num_components', None) or cls.c.call(LVecBase4d, 'get_num_components', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LVecBase4d, 'init_type', None) )(*args,**kw)

    @classmethod
    def size(cls, *args,**kw):
        return ( cls.c.get('size', None) or cls.c.call(LVecBase4d, 'size', None) )(*args,**kw)

    @classmethod
    def unit_w(cls, *args,**kw):
        return ( cls.c.get('unit_w', None) or cls.c.call(LVecBase4d, 'unit_w', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LVecBase4d, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LVecBase4d, 'unit_y', None) )(*args,**kw)

    @classmethod
    def unit_z(cls, *args,**kw):
        return ( cls.c.get('unit_z', None) or cls.c.call(LVecBase4d, 'unit_z', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LVecBase4d, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_hash'] = [
        ('d', 'l', 1, ('l', 'LVecBase4d$52$add_hash', 'pl'), ['std::size_t']),
        ('d', 'l', 2, ('l', 'LVecBase4d$53$add_hash', 'pld'), ['std::size_t', 'double']),
    ]
    c.ct['add_to_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase4d$29$add_to_cell', 'pid'), ['int', 'double']),
    ]
    c.ct['add_w'] = [
        ('d', 'v', 1, ('v', 'LVecBase4d$33$add_w', 'pd'), ['double']),
    ]
    c.ct['add_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase4d$30$add_x', 'pd'), ['double']),
    ]
    c.ct['add_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase4d$31$add_y', 'pd'), ['double']),
    ]
    c.ct['add_z'] = [
        ('d', 'v', 1, ('v', 'LVecBase4d$32$add_z', 'pd'), ['double']),
    ]
    c.ct['almost_equal'] = [
        ('d', 'B', 1, ('B', 'LVecBase4d$59$almost_equal', 'pp'), ['LVecBase4d const&']),
        ('d', 'B', 2, ('B', 'LVecBase4d$60$almost_equal', 'ppd'), ['LVecBase4d const&', 'double']),
    ]
    c.ct['begin'] = [
        ('d', 'v', 0, ('v', 'LVecBase4d$36$begin', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase4d$37$begin', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'LVecBase4d$48$compare_to', 'pp'), ['LVecBase4d const&']),
        ('d', 'i', 2, ('i', 'LVecBase4d$49$compare_to', 'ppd'), ['LVecBase4d const&', 'double']),
    ]
    c.ct['componentwise_mult'] = [
        ('d', 'v', 1, ('v', 'LVecBase4d$56$componentwise_mult', 'pp'), ['LVecBase4d const&']),
    ]
    c.ct['dot'] = [
        ('d', 'd', 1, ('d', 'LVecBase4d$42$dot', 'pp'), ['LVecBase4d const&']),
    ]
    c.ct['end'] = [
        ('d', 'v', 0, ('v', 'LVecBase4d$38$end', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase4d$39$end', 'p'), []),
    ]
    c.ct['fill'] = [
        ('d', 'v', 1, ('v', 'LVecBase4d$40$fill', 'pd'), ['double']),
    ]
    c.ct['fmax'] = [
        ('d', 'p', 1, ('p', 'LVecBase4d$57$fmax', 'pp'), ['LVecBase4d const&']),
    ]
    c.ct['fmin'] = [
        ('d', 'p', 1, ('p', 'LVecBase4d$58$fmin', 'pp'), ['LVecBase4d const&']),
    ]
    c.ct['generate_hash'] = [
        ('d', 'v', 1, ('v', 'LVecBase4d$54$generate_hash', 'pp'), ['ChecksumHashGenerator&']),
        ('d', 'v', 2, ('v', 'LVecBase4d$55$generate_hash', 'ppd'), ['ChecksumHashGenerator&', 'double']),
    ]
    c.ct['get_cell'] = [
        ('d', 'd', 1, ('d', 'LVecBase4d$17$get_cell', 'pi'), ['int']),
    ]
    c.ct['get_data'] = [
        ('d', 'v', 0, ('v', 'LVecBase4d$34$get_data', 'p'), []),
    ]
    c.ct['get_hash'] = [
        ('d', 'l', 0, ('l', 'LVecBase4d$50$get_hash', 'p'), []),
        ('d', 'l', 1, ('l', 'LVecBase4d$51$get_hash', 'pd'), ['double']),
    ]
    c.ct['get_v'] = [
        ('d', 'p', 0, ('p', 'LVecBase4d$66$get_v', 'p'), []),
    ]
    c.ct['get_w'] = [
        ('d', 'd', 0, ('d', 'LVecBase4d$22$get_w', 'p'), []),
    ]
    c.ct['get_x'] = [
        ('d', 'd', 0, ('d', 'LVecBase4d$19$get_x', 'p'), []),
    ]
    c.ct['get_xy'] = [
        ('d', 'p', 0, ('p', 'LVecBase4d$24$get_xy', 'p'), []),
    ]
    c.ct['get_xyz'] = [
        ('d', 'p', 0, ('p', 'LVecBase4d$23$get_xyz', 'p'), []),
    ]
    c.ct['get_y'] = [
        ('d', 'd', 0, ('d', 'LVecBase4d$20$get_y', 'p'), []),
    ]
    c.ct['get_z'] = [
        ('d', 'd', 0, ('d', 'LVecBase4d$21$get_z', 'p'), []),
    ]
    c.ct['is_nan'] = [
        ('d', 'B', 0, ('B', 'LVecBase4d$16$is_nan', 'p'), []),
    ]
    c.ct['length'] = [
        ('d', 'd', 0, ('d', 'LVecBase4d$44$length', 'p'), []),
    ]
    c.ct['length_squared'] = [
        ('d', 'd', 0, ('d', 'LVecBase4d$43$length_squared', 'p'), []),
    ]
    c.ct['normalize'] = [
        ('d', 'B', 0, ('B', 'LVecBase4d$45$normalize', 'p'), []),
    ]
    c.ct['normalized'] = [
        ('d', 'p', 0, ('p', 'LVecBase4d$46$normalized', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'LVecBase4d$61$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['project'] = [
        ('d', 'p', 1, ('p', 'LVecBase4d$47$project', 'pp'), ['LVecBase4d const&']),
    ]
    c.ct['read_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase4d$65$read_datagram', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['read_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase4d$63$read_datagram_fixed', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['set'] = [
        ('d', 'v', 4, ('v', 'LVecBase4d$41$set', 'pdddd'), ['double', 'double', 'double', 'double']),
    ]
    c.ct['set_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase4d$18$set_cell', 'pid'), ['int', 'double']),
    ]
    c.ct['set_w'] = [
        ('d', 'v', 1, ('v', 'LVecBase4d$28$set_w', 'pd'), ['double']),
    ]
    c.ct['set_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase4d$25$set_x', 'pd'), ['double']),
    ]
    c.ct['set_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase4d$26$set_y', 'pd'), ['double']),
    ]
    c.ct['set_z'] = [
        ('d', 'v', 1, ('v', 'LVecBase4d$27$set_z', 'pd'), ['double']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase4d$64$write_datagram', 'pp'), ['Datagram&']),
    ]
    c.ct['write_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase4d$62$write_datagram_fixed', 'pp'), ['Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVecBase4d, attr, self)

LVecBase4d.c.link(LVecBase4d)



class LVecBase4f(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("LVecBase4f", "upanda3d", """libupanda3d_c.so""")

    # enum 



    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 13, 0, ('p', 'LVecBase4f$1$LVecBase4f', ''), []),
        ('s', 13, 1, ('p', 'LVecBase4f$2$LVecBase4f', 'p'), ['LPoint3f const&']),
        ('s', 13, 2, ('p', 'LVecBase4f$3$LVecBase4f', 'pf'), ['LVecBase3f const&', 'float']),
        ('s', 13, 1, ('p', 'LVecBase4f$4$LVecBase4f', 'p'), ['LVecBase4f const&']),
        ('s', 13, 1, ('p', 'LVecBase4f$5$LVecBase4f', 'p'), ['LVecBase4f::EVector4 const&']),
        ('s', 13, 1, ('p', 'LVecBase4f$6$LVecBase4f', 'p'), ['LVector3f const&']),
        ('s', 13, 1, ('p', 'LVecBase4f$7$LVecBase4f', 'p'), ['UnalignedLVecBase4f const&']),
        ('s', 13, 1, ('p', 'LVecBase4f$8$LVecBase4f', 'f'), ['float']),
        ('s', 13, 4, ('p', 'LVecBase4f$9$LVecBase4f', 'ffff'), ['float', 'float', 'float', 'float']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVecBase4f$67$get_class_type', ''), []),
    ]
    c.ct['get_num_components'] = [
        ('s', 'i', 0, ('i', 'LVecBase4f$35$get_num_components', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVecBase4f$68$init_type', ''), []),
    ]
    c.ct['size'] = [
        ('s', 'i', 0, ('i', 'LVecBase4f$15$size', ''), []),
    ]
    c.ct['unit_w'] = [
        ('s', 13, 0, ('p', 'LVecBase4f$14$unit_w', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 13, 0, ('p', 'LVecBase4f$11$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 13, 0, ('p', 'LVecBase4f$12$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 13, 0, ('p', 'LVecBase4f$13$unit_z', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 13, 0, ('p', 'LVecBase4f$10$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LVecBase4f, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_num_components(cls, *args,**kw):
        return ( cls.c.get('get_num_components', None) or cls.c.call(LVecBase4f, 'get_num_components', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LVecBase4f, 'init_type', None) )(*args,**kw)

    @classmethod
    def size(cls, *args,**kw):
        return ( cls.c.get('size', None) or cls.c.call(LVecBase4f, 'size', None) )(*args,**kw)

    @classmethod
    def unit_w(cls, *args,**kw):
        return ( cls.c.get('unit_w', None) or cls.c.call(LVecBase4f, 'unit_w', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LVecBase4f, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LVecBase4f, 'unit_y', None) )(*args,**kw)

    @classmethod
    def unit_z(cls, *args,**kw):
        return ( cls.c.get('unit_z', None) or cls.c.call(LVecBase4f, 'unit_z', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LVecBase4f, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_hash'] = [
        ('d', 'l', 1, ('l', 'LVecBase4f$52$add_hash', 'pl'), ['std::size_t']),
        ('d', 'l', 2, ('l', 'LVecBase4f$53$add_hash', 'plf'), ['std::size_t', 'float']),
    ]
    c.ct['add_to_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase4f$29$add_to_cell', 'pif'), ['int', 'float']),
    ]
    c.ct['add_w'] = [
        ('d', 'v', 1, ('v', 'LVecBase4f$33$add_w', 'pf'), ['float']),
    ]
    c.ct['add_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase4f$30$add_x', 'pf'), ['float']),
    ]
    c.ct['add_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase4f$31$add_y', 'pf'), ['float']),
    ]
    c.ct['add_z'] = [
        ('d', 'v', 1, ('v', 'LVecBase4f$32$add_z', 'pf'), ['float']),
    ]
    c.ct['almost_equal'] = [
        ('d', 'B', 1, ('B', 'LVecBase4f$59$almost_equal', 'pp'), ['LVecBase4f const&']),
        ('d', 'B', 2, ('B', 'LVecBase4f$60$almost_equal', 'ppf'), ['LVecBase4f const&', 'float']),
    ]
    c.ct['begin'] = [
        ('d', 'v', 0, ('v', 'LVecBase4f$36$begin', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase4f$37$begin', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'LVecBase4f$48$compare_to', 'pp'), ['LVecBase4f const&']),
        ('d', 'i', 2, ('i', 'LVecBase4f$49$compare_to', 'ppf'), ['LVecBase4f const&', 'float']),
    ]
    c.ct['componentwise_mult'] = [
        ('d', 'v', 1, ('v', 'LVecBase4f$56$componentwise_mult', 'pp'), ['LVecBase4f const&']),
    ]
    c.ct['dot'] = [
        ('d', 'f', 1, ('f', 'LVecBase4f$42$dot', 'pp'), ['LVecBase4f const&']),
    ]
    c.ct['end'] = [
        ('d', 'v', 0, ('v', 'LVecBase4f$38$end', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase4f$39$end', 'p'), []),
    ]
    c.ct['fill'] = [
        ('d', 'v', 1, ('v', 'LVecBase4f$40$fill', 'pf'), ['float']),
    ]
    c.ct['fmax'] = [
        ('d', 13, 1, ('p', 'LVecBase4f$57$fmax', 'pp'), ['LVecBase4f const&']),
    ]
    c.ct['fmin'] = [
        ('d', 13, 1, ('p', 'LVecBase4f$58$fmin', 'pp'), ['LVecBase4f const&']),
    ]
    c.ct['generate_hash'] = [
        ('d', 'v', 1, ('v', 'LVecBase4f$54$generate_hash', 'pp'), ['ChecksumHashGenerator&']),
        ('d', 'v', 2, ('v', 'LVecBase4f$55$generate_hash', 'ppf'), ['ChecksumHashGenerator&', 'float']),
    ]
    c.ct['get_cell'] = [
        ('d', 'f', 1, ('f', 'LVecBase4f$17$get_cell', 'pi'), ['int']),
    ]
    c.ct['get_data'] = [
        ('d', 'v', 0, ('v', 'LVecBase4f$34$get_data', 'p'), []),
    ]
    c.ct['get_hash'] = [
        ('d', 'l', 0, ('l', 'LVecBase4f$50$get_hash', 'p'), []),
        ('d', 'l', 1, ('l', 'LVecBase4f$51$get_hash', 'pf'), ['float']),
    ]
    c.ct['get_v'] = [
        ('d', 'p', 0, ('p', 'LVecBase4f$66$get_v', 'p'), []),
    ]
    c.ct['get_w'] = [
        ('d', 'f', 0, ('f', 'LVecBase4f$22$get_w', 'p'), []),
    ]
    c.ct['get_x'] = [
        ('d', 'f', 0, ('f', 'LVecBase4f$19$get_x', 'p'), []),
    ]
    c.ct['get_xy'] = [
        ('d', 7, 0, ('p', 'LVecBase4f$24$get_xy', 'p'), []),
    ]
    c.ct['get_xyz'] = [
        ('d', 10, 0, ('p', 'LVecBase4f$23$get_xyz', 'p'), []),
    ]
    c.ct['get_y'] = [
        ('d', 'f', 0, ('f', 'LVecBase4f$20$get_y', 'p'), []),
    ]
    c.ct['get_z'] = [
        ('d', 'f', 0, ('f', 'LVecBase4f$21$get_z', 'p'), []),
    ]
    c.ct['is_nan'] = [
        ('d', 'B', 0, ('B', 'LVecBase4f$16$is_nan', 'p'), []),
    ]
    c.ct['length'] = [
        ('d', 'f', 0, ('f', 'LVecBase4f$44$length', 'p'), []),
    ]
    c.ct['length_squared'] = [
        ('d', 'f', 0, ('f', 'LVecBase4f$43$length_squared', 'p'), []),
    ]
    c.ct['normalize'] = [
        ('d', 'B', 0, ('B', 'LVecBase4f$45$normalize', 'p'), []),
    ]
    c.ct['normalized'] = [
        ('d', 13, 0, ('p', 'LVecBase4f$46$normalized', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'LVecBase4f$61$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['project'] = [
        ('d', 13, 1, ('p', 'LVecBase4f$47$project', 'pp'), ['LVecBase4f const&']),
    ]
    c.ct['read_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase4f$65$read_datagram', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['read_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase4f$63$read_datagram_fixed', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['set'] = [
        ('d', 'v', 4, ('v', 'LVecBase4f$41$set', 'pffff'), ['float', 'float', 'float', 'float']),
    ]
    c.ct['set_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase4f$18$set_cell', 'pif'), ['int', 'float']),
    ]
    c.ct['set_w'] = [
        ('d', 'v', 1, ('v', 'LVecBase4f$28$set_w', 'pf'), ['float']),
    ]
    c.ct['set_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase4f$25$set_x', 'pf'), ['float']),
    ]
    c.ct['set_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase4f$26$set_y', 'pf'), ['float']),
    ]
    c.ct['set_z'] = [
        ('d', 'v', 1, ('v', 'LVecBase4f$27$set_z', 'pf'), ['float']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase4f$64$write_datagram', 'pp'), ['Datagram&']),
    ]
    c.ct['write_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase4f$62$write_datagram_fixed', 'pp'), ['Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVecBase4f, attr, self)

LVecBase4f.c.link(LVecBase4f)



class LVecBase4i(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("LVecBase4i", "upanda3d", """libupanda3d_c.so""")

    # enum 



    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 14, 0, ('p', 'LVecBase4i$1$LVecBase4i', ''), []),
        ('s', 14, 1, ('p', 'LVecBase4i$2$LVecBase4i', 'p'), ['LPoint3i const&']),
        ('s', 14, 2, ('p', 'LVecBase4i$3$LVecBase4i', 'pi'), ['LVecBase3i const&', 'int']),
        ('s', 14, 1, ('p', 'LVecBase4i$4$LVecBase4i', 'p'), ['LVecBase4i const&']),
        ('s', 14, 1, ('p', 'LVecBase4i$5$LVecBase4i', 'p'), ['LVecBase4i::EVector4 const&']),
        ('s', 14, 1, ('p', 'LVecBase4i$6$LVecBase4i', 'p'), ['LVector3i const&']),
        ('s', 14, 1, ('p', 'LVecBase4i$7$LVecBase4i', 'p'), ['UnalignedLVecBase4i const&']),
        ('s', 14, 1, ('p', 'LVecBase4i$8$LVecBase4i', 'i'), ['int']),
        ('s', 14, 4, ('p', 'LVecBase4i$9$LVecBase4i', 'iiii'), ['int', 'int', 'int', 'int']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVecBase4i$59$get_class_type', ''), []),
    ]
    c.ct['get_num_components'] = [
        ('s', 'i', 0, ('i', 'LVecBase4i$35$get_num_components', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVecBase4i$60$init_type', ''), []),
    ]
    c.ct['size'] = [
        ('s', 'i', 0, ('i', 'LVecBase4i$15$size', ''), []),
    ]
    c.ct['unit_w'] = [
        ('s', 'p', 0, ('p', 'LVecBase4i$14$unit_w', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 'p', 0, ('p', 'LVecBase4i$11$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 'p', 0, ('p', 'LVecBase4i$12$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 'p', 0, ('p', 'LVecBase4i$13$unit_z', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 'p', 0, ('p', 'LVecBase4i$10$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LVecBase4i, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_num_components(cls, *args,**kw):
        return ( cls.c.get('get_num_components', None) or cls.c.call(LVecBase4i, 'get_num_components', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LVecBase4i, 'init_type', None) )(*args,**kw)

    @classmethod
    def size(cls, *args,**kw):
        return ( cls.c.get('size', None) or cls.c.call(LVecBase4i, 'size', None) )(*args,**kw)

    @classmethod
    def unit_w(cls, *args,**kw):
        return ( cls.c.get('unit_w', None) or cls.c.call(LVecBase4i, 'unit_w', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LVecBase4i, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LVecBase4i, 'unit_y', None) )(*args,**kw)

    @classmethod
    def unit_z(cls, *args,**kw):
        return ( cls.c.get('unit_z', None) or cls.c.call(LVecBase4i, 'unit_z', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LVecBase4i, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_hash'] = [
        ('d', 'l', 1, ('l', 'LVecBase4i$46$add_hash', 'pl'), ['std::size_t']),
    ]
    c.ct['add_to_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase4i$29$add_to_cell', 'pii'), ['int', 'int']),
    ]
    c.ct['add_w'] = [
        ('d', 'v', 1, ('v', 'LVecBase4i$33$add_w', 'pi'), ['int']),
    ]
    c.ct['add_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase4i$30$add_x', 'pi'), ['int']),
    ]
    c.ct['add_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase4i$31$add_y', 'pi'), ['int']),
    ]
    c.ct['add_z'] = [
        ('d', 'v', 1, ('v', 'LVecBase4i$32$add_z', 'pi'), ['int']),
    ]
    c.ct['almost_equal'] = [
        ('d', 'B', 1, ('B', 'LVecBase4i$51$almost_equal', 'pp'), ['LVecBase4i const&']),
        ('d', 'B', 2, ('B', 'LVecBase4i$52$almost_equal', 'ppi'), ['LVecBase4i const&', 'int']),
    ]
    c.ct['begin'] = [
        ('d', 'v', 0, ('v', 'LVecBase4i$36$begin', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase4i$37$begin', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'LVecBase4i$44$compare_to', 'pp'), ['LVecBase4i const&']),
    ]
    c.ct['componentwise_mult'] = [
        ('d', 'v', 1, ('v', 'LVecBase4i$48$componentwise_mult', 'pp'), ['LVecBase4i const&']),
    ]
    c.ct['dot'] = [
        ('d', 'i', 1, ('i', 'LVecBase4i$42$dot', 'pp'), ['LVecBase4i const&']),
    ]
    c.ct['end'] = [
        ('d', 'v', 0, ('v', 'LVecBase4i$38$end', 'p'), []),
        ('d', 'v', 0, ('v', 'LVecBase4i$39$end', 'p'), []),
    ]
    c.ct['fill'] = [
        ('d', 'v', 1, ('v', 'LVecBase4i$40$fill', 'pi'), ['int']),
    ]
    c.ct['fmax'] = [
        ('d', 'p', 1, ('p', 'LVecBase4i$49$fmax', 'pp'), ['LVecBase4i const&']),
    ]
    c.ct['fmin'] = [
        ('d', 'p', 1, ('p', 'LVecBase4i$50$fmin', 'pp'), ['LVecBase4i const&']),
    ]
    c.ct['generate_hash'] = [
        ('d', 'v', 1, ('v', 'LVecBase4i$47$generate_hash', 'pp'), ['ChecksumHashGenerator&']),
    ]
    c.ct['get_cell'] = [
        ('d', 'i', 1, ('i', 'LVecBase4i$17$get_cell', 'pi'), ['int']),
    ]
    c.ct['get_data'] = [
        ('d', 'v', 0, ('v', 'LVecBase4i$34$get_data', 'p'), []),
    ]
    c.ct['get_hash'] = [
        ('d', 'l', 0, ('l', 'LVecBase4i$45$get_hash', 'p'), []),
    ]
    c.ct['get_v'] = [
        ('d', 'p', 0, ('p', 'LVecBase4i$58$get_v', 'p'), []),
    ]
    c.ct['get_w'] = [
        ('d', 'i', 0, ('i', 'LVecBase4i$22$get_w', 'p'), []),
    ]
    c.ct['get_x'] = [
        ('d', 'i', 0, ('i', 'LVecBase4i$19$get_x', 'p'), []),
    ]
    c.ct['get_xy'] = [
        ('d', 'p', 0, ('p', 'LVecBase4i$24$get_xy', 'p'), []),
    ]
    c.ct['get_xyz'] = [
        ('d', 'p', 0, ('p', 'LVecBase4i$23$get_xyz', 'p'), []),
    ]
    c.ct['get_y'] = [
        ('d', 'i', 0, ('i', 'LVecBase4i$20$get_y', 'p'), []),
    ]
    c.ct['get_z'] = [
        ('d', 'i', 0, ('i', 'LVecBase4i$21$get_z', 'p'), []),
    ]
    c.ct['is_nan'] = [
        ('d', 'B', 0, ('B', 'LVecBase4i$16$is_nan', 'p'), []),
    ]
    c.ct['length_squared'] = [
        ('d', 'i', 0, ('i', 'LVecBase4i$43$length_squared', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'LVecBase4i$53$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['read_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase4i$57$read_datagram', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['read_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase4i$55$read_datagram_fixed', 'pp'), ['DatagramIterator&']),
    ]
    c.ct['set'] = [
        ('d', 'v', 4, ('v', 'LVecBase4i$41$set', 'piiii'), ['int', 'int', 'int', 'int']),
    ]
    c.ct['set_cell'] = [
        ('d', 'v', 2, ('v', 'LVecBase4i$18$set_cell', 'pii'), ['int', 'int']),
    ]
    c.ct['set_w'] = [
        ('d', 'v', 1, ('v', 'LVecBase4i$28$set_w', 'pi'), ['int']),
    ]
    c.ct['set_x'] = [
        ('d', 'v', 1, ('v', 'LVecBase4i$25$set_x', 'pi'), ['int']),
    ]
    c.ct['set_y'] = [
        ('d', 'v', 1, ('v', 'LVecBase4i$26$set_y', 'pi'), ['int']),
    ]
    c.ct['set_z'] = [
        ('d', 'v', 1, ('v', 'LVecBase4i$27$set_z', 'pi'), ['int']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 1, ('v', 'LVecBase4i$56$write_datagram', 'pp'), ['Datagram&']),
    ]
    c.ct['write_datagram_fixed'] = [
        ('d', 'v', 1, ('v', 'LVecBase4i$54$write_datagram_fixed', 'pp'), ['Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVecBase4i, attr, self)

LVecBase4i.c.link(LVecBase4i)



class LinkedListNode(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("LinkedListNode", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_PandaNode'] = [
        ('d', 86, 0, ('p', 'LinkedListNode$1$downcast_to_PandaNode', 'p'), []),
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
        ('s', 16, 0, ('p', 'MemoryBase$1$MemoryBase', ''), []),
        ('s', 16, 1, ('p', 'MemoryBase$2$MemoryBase', 'p'), ['MemoryBase const&']),
    ]

    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_ReferenceCount'] = [
        ('d', 49, 0, ('p', 'MemoryBase$3$downcast_to_ReferenceCount', 'p'), []),
    ]
    c.ct['downcast_to_TypedObject'] = [
        ('d', 53, 0, ('p', 'MemoryBase$4$downcast_to_TypedObject', 'p'), []),
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
        ('s', 17, 0, ('p', 'NodePath$1$NodePath', ''), []),
        ('s', 17, 1, ('p', 'NodePath$2$NodePath', 'p'), ['NodePath&&']),
        ('s', 17, 1, ('p', 'NodePath$3$NodePath', 'p'), ['NodePath const&']),
        ('s', 17, 3, ('p', 'NodePath$4$NodePath', 'ppp'), ['NodePath const&', 'PandaNode*', 'Thread*']),
        ('s', 17, 2, ('p', 'NodePath$5$NodePath', 'pp'), ['NodePath const&', 'PandaNode*']),
        ('s', 17, 2, ('p', 'NodePath$6$NodePath', 'pp'), ['PandaNode*', 'Thread*']),
        ('s', 17, 1, ('p', 'NodePath$7$NodePath', 'p'), ['PandaNode*']),
        ('s', 17, 2, ('p', 'NodePath$8$NodePath', 'sp'), ['std::string const&', 'Thread*']),
        ('s', 17, 1, ('p', 'NodePath$9$NodePath', 's'), ['std::string const&']),
    ]

    # classmethod type calls

    c.ct['any_path'] = [
        ('s', 17, 2, ('p', 'NodePath$10$any_path', 'pp'), ['PandaNode*', 'Thread*']),
        ('s', 17, 1, ('p', 'NodePath$11$any_path', 'p'), ['PandaNode*']),
    ]
    c.ct['decode_from_bam_stream'] = [
        ('s', 17, 2, ('p', 'NodePath$686$decode_from_bam_stream', 'pp'), ['vector_uchar', 'BamReader*']),
        ('s', 17, 1, ('p', 'NodePath$687$decode_from_bam_stream', 'p'), ['vector_uchar']),
    ]
    c.ct['fail'] = [
        ('s', 17, 0, ('p', 'NodePath$15$fail', ''), []),
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
        ('s', 17, 0, ('p', 'NodePath$13$not_found', ''), []),
    ]
    c.ct['removed'] = [
        ('s', 17, 0, ('p', 'NodePath$14$removed', ''), []),
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
        ('d', 'l', 1, ('l', 'NodePath$34$add_hash', 'pl'), ['std::size_t']),
    ]
    c.ct['adjust_all_priorities'] = [
        ('d', 'v', 1, ('v', 'NodePath$621$adjust_all_priorities', 'pi'), ['int']),
    ]
    c.ct['apply_texture_colors'] = [
        ('d', 'v', 0, ('v', 'NodePath$668$apply_texture_colors', 'p'), []),
    ]
    c.ct['attach_new_node'] = [
        ('d', 17, 3, ('p', 'NodePath$78$attach_new_node', 'ppip'), ['PandaNode*', 'int', 'Thread*']),
        ('d', 17, 2, ('p', 'NodePath$79$attach_new_node', 'ppi'), ['PandaNode*', 'int']),
        ('d', 17, 1, ('p', 'NodePath$80$attach_new_node', 'pp'), ['PandaNode*']),
        ('d', 17, 3, ('p', 'NodePath$81$attach_new_node', 'psip'), ['std::string const&', 'int', 'Thread*']),
        ('d', 17, 2, ('p', 'NodePath$82$attach_new_node', 'psi'), ['std::string const&', 'int']),
        ('d', 17, 1, ('p', 'NodePath$83$attach_new_node', 'ps'), ['std::string const&']),
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
        ('d', 17, 3, ('p', 'NodePath$75$copy_to', 'ppip'), ['NodePath const&', 'int', 'Thread*']),
        ('d', 17, 2, ('p', 'NodePath$76$copy_to', 'ppi'), ['NodePath const&', 'int']),
        ('d', 17, 1, ('p', 'NodePath$77$copy_to', 'pp'), ['NodePath const&']),
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
        ('d', 17, 1, ('p', 'NodePath$56$find', 'ps'), ['std::string const&']),
    ]
    c.ct['find_all_matches'] = [
        ('d', 18, 1, ('p', 'NodePath$58$find_all_matches', 'ps'), ['std::string const&']),
    ]
    c.ct['find_all_materials'] = [
        ('d', 'p', 0, ('p', 'NodePath$523$find_all_materials', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath$524$find_all_materials', 'ps'), ['std::string const&']),
    ]
    c.ct['find_all_paths_to'] = [
        ('d', 18, 1, ('p', 'NodePath$59$find_all_paths_to', 'pp'), ['PandaNode*']),
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
        ('d', 24, 0, ('p', 'NodePath$515$find_all_textures', 'p'), []),
        ('d', 24, 1, ('p', 'NodePath$516$find_all_textures', 'pp'), ['TextureStage*']),
        ('d', 24, 1, ('p', 'NodePath$517$find_all_textures', 'ps'), ['std::string const&']),
    ]
    c.ct['find_all_vertex_columns'] = [
        ('d', 'p', 0, ('p', 'NodePath$509$find_all_vertex_columns', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath$510$find_all_vertex_columns', 'ps'), ['std::string const&']),
    ]
    c.ct['find_material'] = [
        ('d', 'p', 1, ('p', 'NodePath$522$find_material', 'ps'), ['std::string const&']),
    ]
    c.ct['find_net_tag'] = [
        ('d', 17, 1, ('p', 'NodePath$677$find_net_tag', 'ps'), ['std::string const&']),
    ]
    c.ct['find_path_to'] = [
        ('d', 17, 1, ('p', 'NodePath$57$find_path_to', 'pp'), ['PandaNode*']),
    ]
    c.ct['find_texture'] = [
        ('d', 64, 1, ('p', 'NodePath$513$find_texture', 'pp'), ['TextureStage*']),
        ('d', 64, 1, ('p', 'NodePath$514$find_texture', 'ps'), ['std::string const&']),
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
        ('d', 17, 2, ('p', 'NodePath$25$get_ancestor', 'pip'), ['int', 'Thread*']),
        ('d', 17, 1, ('p', 'NodePath$26$get_ancestor', 'pi'), ['int']),
    ]
    c.ct['get_antialias'] = [
        ('d', 'H', 0, ('H', 'NodePath$612$get_antialias', 'p'), []),
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
        ('d', 17, 2, ('p', 'NodePath$45$get_child', 'pip'), ['int', 'Thread*']),
        ('d', 17, 1, ('p', 'NodePath$46$get_child', 'pi'), ['int']),
    ]
    c.ct['get_children'] = [
        ('d', 18, 1, ('p', 'NodePath$41$get_children', 'pp'), ['Thread*']),
        ('d', 18, 0, ('p', 'NodePath$42$get_children', 'p'), []),
    ]
    c.ct['get_collide_mask'] = [
        ('d', 'p', 0, ('p', 'NodePath$644$get_collide_mask', 'p'), []),
    ]
    c.ct['get_color'] = [
        ('d', 'p', 0, ('p', 'NodePath$285$get_color', 'p'), []),
    ]
    c.ct['get_color_scale'] = [
        ('d', 12, 0, ('p', 'NodePath$306$get_color_scale', 'p'), []),
    ]
    c.ct['get_common_ancestor'] = [
        ('d', 17, 2, ('p', 'NodePath$39$get_common_ancestor', 'ppp'), ['NodePath const&', 'Thread*']),
        ('d', 17, 1, ('p', 'NodePath$40$get_common_ancestor', 'pp'), ['NodePath const&']),
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
        ('d', 70, 1, ('p', 'NodePath$111$get_effect', 'pi'), ['TypeHandle']),
    ]
    c.ct['get_effects'] = [
        ('d', 'p', 0, ('p', 'NodePath$115$get_effects', 'p'), []),
    ]
    c.ct['get_error_type'] = [
        ('d', 'p', 0, ('p', 'NodePath$27$get_error_type', 'p'), []),
    ]
    c.ct['get_fog'] = [
        ('d', 90, 0, ('p', 'NodePath$540$get_fog', 'p'), []),
    ]
    c.ct['get_h'] = [
        ('d', 'f', 0, ('f', 'NodePath$183$get_h', 'p'), []),
        ('d', 'f', 1, ('f', 'NodePath$184$get_h', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_hidden_ancestor'] = [
        ('d', 17, 2, ('p', 'NodePath$630$get_hidden_ancestor', 'ppp'), ['DrawMask', 'Thread*']),
        ('d', 17, 1, ('p', 'NodePath$631$get_hidden_ancestor', 'pp'), ['DrawMask']),
        ('d', 17, 0, ('p', 'NodePath$632$get_hidden_ancestor', 'p'), []),
    ]
    c.ct['get_hpr'] = [
        ('d', 9, 0, ('p', 'NodePath$181$get_hpr', 'p'), []),
        ('d', 9, 1, ('p', 'NodePath$182$get_hpr', 'pp'), ['NodePath const&']),
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
        ('d', 78, 1, ('p', 'NodePath$139$get_net_prev_transform', 'pp'), ['Thread*']),
        ('d', 78, 0, ('p', 'NodePath$140$get_net_prev_transform', 'p'), []),
    ]
    c.ct['get_net_state'] = [
        ('d', 79, 1, ('p', 'NodePath$103$get_net_state', 'pp'), ['Thread*']),
        ('d', 79, 0, ('p', 'NodePath$104$get_net_state', 'p'), []),
    ]
    c.ct['get_net_tag'] = [
        ('d', 's', 1, ('s', 'NodePath$675$get_net_tag', 'ps'), ['std::string const&']),
    ]
    c.ct['get_net_transform'] = [
        ('d', 78, 1, ('p', 'NodePath$129$get_net_transform', 'pp'), ['Thread*']),
        ('d', 78, 0, ('p', 'NodePath$130$get_net_transform', 'p'), []),
    ]
    c.ct['get_node'] = [
        ('d', 86, 2, ('p', 'NodePath$23$get_node', 'pip'), ['int', 'Thread*']),
        ('d', 86, 1, ('p', 'NodePath$24$get_node', 'pi'), ['int']),
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
        ('d', 17, 1, ('p', 'NodePath$52$get_parent', 'pp'), ['Thread*']),
        ('d', 17, 0, ('p', 'NodePath$53$get_parent', 'p'), []),
    ]
    c.ct['get_pos'] = [
        ('d', 33, 0, ('p', 'NodePath$161$get_pos', 'p'), []),
        ('d', 33, 1, ('p', 'NodePath$162$get_pos', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_pos_delta'] = [
        ('d', 42, 0, ('p', 'NodePath$169$get_pos_delta', 'p'), []),
        ('d', 42, 1, ('p', 'NodePath$170$get_pos_delta', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_prev_transform'] = [
        ('d', 78, 2, ('p', 'NodePath$131$get_prev_transform', 'ppp'), ['NodePath const&', 'Thread*']),
        ('d', 78, 1, ('p', 'NodePath$132$get_prev_transform', 'pp'), ['NodePath const&']),
        ('d', 78, 1, ('p', 'NodePath$133$get_prev_transform', 'pp'), ['Thread*']),
        ('d', 78, 0, ('p', 'NodePath$134$get_prev_transform', 'p'), []),
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
        ('d', 33, 2, ('p', 'NodePath$273$get_relative_point', 'ppp'), ['NodePath const&', 'LVecBase3 const&']),
    ]
    c.ct['get_relative_vector'] = [
        ('d', 42, 2, ('p', 'NodePath$274$get_relative_vector', 'ppp'), ['NodePath const&', 'LVecBase3 const&']),
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
        ('d', 9, 0, ('p', 'NodePath$205$get_scale', 'p'), []),
        ('d', 9, 1, ('p', 'NodePath$206$get_scale', 'pp'), ['NodePath const&']),
    ]
    c.ct['get_sg'] = [
        ('d', 'f', 0, ('f', 'NodePath$308$get_sg', 'p'), []),
    ]
    c.ct['get_shader'] = [
        ('d', 69, 0, ('p', 'NodePath$444$get_shader', 'p'), []),
    ]
    c.ct['get_shader_input'] = [
        ('d', 21, 1, ('p', 'NodePath$445$get_shader_input', 'ps'), ['CPT_InternalName']),
    ]
    c.ct['get_shear'] = [
        ('d', 9, 0, ('p', 'NodePath$223$get_shear', 'p'), []),
        ('d', 9, 1, ('p', 'NodePath$224$get_shear', 'pp'), ['NodePath const&']),
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
        ('d', 17, 1, ('p', 'NodePath$642$get_stashed_ancestor', 'pp'), ['Thread*']),
        ('d', 17, 0, ('p', 'NodePath$643$get_stashed_ancestor', 'p'), []),
    ]
    c.ct['get_stashed_children'] = [
        ('d', 18, 1, ('p', 'NodePath$47$get_stashed_children', 'pp'), ['Thread*']),
        ('d', 18, 0, ('p', 'NodePath$48$get_stashed_children', 'p'), []),
    ]
    c.ct['get_state'] = [
        ('d', 79, 2, ('p', 'NodePath$95$get_state', 'ppp'), ['NodePath const&', 'Thread*']),
        ('d', 79, 1, ('p', 'NodePath$96$get_state', 'pp'), ['NodePath const&']),
        ('d', 79, 1, ('p', 'NodePath$97$get_state', 'pp'), ['Thread*']),
        ('d', 79, 0, ('p', 'NodePath$98$get_state', 'p'), []),
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
        ('d', 9, 2, ('p', 'NodePath$486$get_tex_hpr', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 9, 1, ('p', 'NodePath$487$get_tex_hpr', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_offset'] = [
        ('d', 6, 2, ('p', 'NodePath$470$get_tex_offset', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 6, 1, ('p', 'NodePath$471$get_tex_offset', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_pos'] = [
        ('d', 9, 2, ('p', 'NodePath$484$get_tex_pos', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 9, 1, ('p', 'NodePath$485$get_tex_pos', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_projector_from'] = [
        ('d', 17, 1, ('p', 'NodePath$503$get_tex_projector_from', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_projector_to'] = [
        ('d', 17, 1, ('p', 'NodePath$504$get_tex_projector_to', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_rotate'] = [
        ('d', 'f', 2, ('f', 'NodePath$472$get_tex_rotate', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 'f', 1, ('f', 'NodePath$473$get_tex_rotate', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_scale'] = [
        ('d', 6, 2, ('p', 'NodePath$474$get_tex_scale', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 6, 1, ('p', 'NodePath$475$get_tex_scale', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_scale_3d'] = [
        ('d', 9, 2, ('p', 'NodePath$488$get_tex_scale_3d', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 9, 1, ('p', 'NodePath$489$get_tex_scale_3d', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_tex_transform'] = [
        ('d', 78, 2, ('p', 'NodePath$452$get_tex_transform', 'ppp'), ['NodePath const&', 'TextureStage*']),
        ('d', 78, 1, ('p', 'NodePath$453$get_tex_transform', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_texture'] = [
        ('d', 64, 0, ('p', 'NodePath$368$get_texture', 'p'), []),
        ('d', 64, 1, ('p', 'NodePath$369$get_texture', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_texture_sampler'] = [
        ('d', 'p', 0, ('p', 'NodePath$371$get_texture_sampler', 'p'), []),
        ('d', 'p', 1, ('p', 'NodePath$372$get_texture_sampler', 'pp'), ['TextureStage*']),
    ]
    c.ct['get_top'] = [
        ('d', 17, 1, ('p', 'NodePath$30$get_top', 'pp'), ['Thread*']),
        ('d', 17, 0, ('p', 'NodePath$31$get_top', 'p'), []),
    ]
    c.ct['get_top_node'] = [
        ('d', 86, 1, ('p', 'NodePath$28$get_top_node', 'pp'), ['Thread*']),
        ('d', 86, 0, ('p', 'NodePath$29$get_top_node', 'p'), []),
    ]
    c.ct['get_transform'] = [
        ('d', 78, 2, ('p', 'NodePath$117$get_transform', 'ppp'), ['NodePath const&', 'Thread*']),
        ('d', 78, 1, ('p', 'NodePath$118$get_transform', 'pp'), ['NodePath const&']),
        ('d', 78, 1, ('p', 'NodePath$119$get_transform', 'pp'), ['Thread*']),
        ('d', 78, 0, ('p', 'NodePath$120$get_transform', 'p'), []),
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
        ('d', 17, 3, ('p', 'NodePath$69$instance_to', 'ppip'), ['NodePath const&', 'int', 'Thread*']),
        ('d', 17, 2, ('p', 'NodePath$70$instance_to', 'ppi'), ['NodePath const&', 'int']),
        ('d', 17, 1, ('p', 'NodePath$71$instance_to', 'pp'), ['NodePath const&']),
    ]
    c.ct['instance_under_node'] = [
        ('d', 17, 4, ('p', 'NodePath$72$instance_under_node', 'ppsip'), ['NodePath const&', 'std::string const&', 'int', 'Thread*']),
        ('d', 17, 3, ('p', 'NodePath$73$instance_under_node', 'ppsi'), ['NodePath const&', 'std::string const&', 'int']),
        ('d', 17, 2, ('p', 'NodePath$74$instance_under_node', 'pps'), ['NodePath const&', 'std::string const&']),
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
        ('d', 86, 0, ('p', 'NodePath$32$node', 'p'), []),
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
        ('d', 'v', 2, ('v', 'NodePath$608$set_antialias', 'pHi'), ['unsigned short int', 'int']),
        ('d', 'v', 1, ('v', 'NodePath$609$set_antialias', 'pH'), ['unsigned short int']),
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
        ('s', 18, 0, ('p', 'NodePathCollection$1$NodePathCollection', ''), []),
        ('s', 18, 1, ('p', 'NodePathCollection$2$NodePathCollection', 'p'), ['NodePathCollection const&']),
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
        ('d', 18, 1, ('p', 'NodePathCollection$20$find_all_matches', 'ps'), ['std::string const&']),
    ]
    c.ct['get_collide_mask'] = [
        ('d', 'p', 0, ('p', 'NodePathCollection$28$get_collide_mask', 'p'), []),
    ]
    c.ct['get_num_paths'] = [
        ('d', 'i', 0, ('i', 'NodePathCollection$12$get_num_paths', 'p'), []),
    ]
    c.ct['get_path'] = [
        ('d', 17, 1, ('p', 'NodePathCollection$13$get_path', 'pi'), ['int']),
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
        ('d', 'v', 1, ('v', 'NodePathCollection$10$reserve', 'pl'), ['std::size_t']),
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
        ('d', 'l', 0, ('l', 'NodePathCollection$14$size', 'p'), []),
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
        ('s', 19, 0, ('p', 'PandaFramework$1$PandaFramework', ''), []),
        ('s', 19, 1, ('p', 'PandaFramework$2$PandaFramework', 'p'), ['PandaFramework const&']),
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
        ('d', 17, 0, ('p', 'PandaFramework$7$get_data_root', 'p'), []),
    ]
    c.ct['get_default_pipe'] = [
        ('d', 'p', 0, ('p', 'PandaFramework$5$get_default_pipe', 'p'), []),
    ]
    c.ct['get_default_window_props'] = [
        ('d', 'v', 1, ('v', 'PandaFramework$13$get_default_window_props', 'pp'), ['WindowProperties&']),
    ]
    c.ct['get_event_handler'] = [
        ('d', 54, 0, ('p', 'PandaFramework$8$get_event_handler', 'p'), []),
    ]
    c.ct['get_graphics_engine'] = [
        ('d', 50, 0, ('p', 'PandaFramework$6$get_graphics_engine', 'p'), []),
    ]
    c.ct['get_highlight'] = [
        ('d', 17, 0, ('p', 'PandaFramework$48$get_highlight', 'p'), []),
    ]
    c.ct['get_lighting'] = [
        ('d', 'B', 0, ('B', 'PandaFramework$40$get_lighting', 'p'), []),
    ]
    c.ct['get_models'] = [
        ('d', 17, 0, ('p', 'PandaFramework$28$get_models', 'p'), []),
    ]
    c.ct['get_mouse'] = [
        ('d', 17, 1, ('p', 'PandaFramework$10$get_mouse', 'pp'), ['GraphicsOutput*']),
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
        ('d', 67, 1, ('p', 'PandaFramework$21$get_window', 'pi'), ['int']),
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
        ('d', 67, 0, ('p', 'PandaFramework$14$open_window', 'p'), []),
        ('d', 67, 2, ('p', 'PandaFramework$15$open_window', 'ppp'), ['GraphicsPipe*', 'GraphicsStateGuardian*']),
        ('d', 67, 1, ('p', 'PandaFramework$16$open_window', 'pp'), ['GraphicsPipe*']),
        ('d', 67, 4, ('p', 'PandaFramework$17$open_window', 'ppipp'), ['WindowProperties const&', 'int', 'GraphicsPipe*', 'GraphicsStateGuardian*']),
        ('d', 67, 3, ('p', 'PandaFramework$18$open_window', 'ppip'), ['WindowProperties const&', 'int', 'GraphicsPipe*']),
        ('d', 67, 2, ('p', 'PandaFramework$19$open_window', 'ppi'), ['WindowProperties const&', 'int']),
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
        ('s', 20, 0, ('p', 'PandaSystem$24$get_global_ptr', ''), []),
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
        ('d', 'l', 0, ('l', 'PandaSystem$16$get_num_systems', 'p'), []),
    ]
    c.ct['get_system'] = [
        ('d', 's', 1, ('s', 'PandaSystem$17$get_system', 'pl'), ['std::size_t']),
    ]
    c.ct['get_system_tag'] = [
        ('d', 's', 2, ('s', 'PandaSystem$18$get_system_tag', 'pss'), ['std::string const&', 'std::string const&']),
    ]
    c.ct['has_system'] = [
        ('d', 'B', 1, ('B', 'PandaSystem$15$has_system', 'ps'), ['std::string const&']),
    ]
    c.ct['heap_trim'] = [
        ('d', 'B', 1, ('B', 'PandaSystem$21$heap_trim', 'pl'), ['std::size_t']),
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



class ShaderInput(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("ShaderInput", "upanda3d", """libupanda3d_c.so""")

    # enum AccessFlags

    A_layered = const(4)
    A_read = const(1)
    A_write = const(2)


    # enum ShaderInputType

    M_buffer = const(8)
    M_invalid = const(0)
    M_nodepath = const(2)
    M_numeric = const(4)
    M_param = const(6)
    M_texture = const(1)
    M_texture_image = const(7)
    M_texture_sampler = const(5)
    M_vector = const(3)


    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 21, 0, ('p', 'ShaderInput$2$ShaderInput', ''), []),
        ('s', 21, 3, ('p', 'ShaderInput$3$ShaderInput', 'spi'), ['CPT_InternalName', 'LMatrix3d const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$4$ShaderInput', 'sp'), ['CPT_InternalName', 'LMatrix3d const&']),
        ('s', 21, 3, ('p', 'ShaderInput$5$ShaderInput', 'spi'), ['CPT_InternalName', 'LMatrix3f const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$6$ShaderInput', 'sp'), ['CPT_InternalName', 'LMatrix3f const&']),
        ('s', 21, 3, ('p', 'ShaderInput$7$ShaderInput', 'spi'), ['CPT_InternalName', 'LMatrix4d const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$8$ShaderInput', 'sp'), ['CPT_InternalName', 'LMatrix4d const&']),
        ('s', 21, 3, ('p', 'ShaderInput$9$ShaderInput', 'spi'), ['CPT_InternalName', 'LMatrix4f const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$10$ShaderInput', 'sp'), ['CPT_InternalName', 'LMatrix4f const&']),
        ('s', 21, 3, ('p', 'ShaderInput$11$ShaderInput', 'spi'), ['CPT_InternalName', 'LVecBase2d const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$12$ShaderInput', 'sp'), ['CPT_InternalName', 'LVecBase2d const&']),
        ('s', 21, 3, ('p', 'ShaderInput$13$ShaderInput', 'spi'), ['CPT_InternalName', 'LVecBase2f const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$14$ShaderInput', 'sp'), ['CPT_InternalName', 'LVecBase2f const&']),
        ('s', 21, 3, ('p', 'ShaderInput$15$ShaderInput', 'spi'), ['CPT_InternalName', 'LVecBase2i const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$16$ShaderInput', 'sp'), ['CPT_InternalName', 'LVecBase2i const&']),
        ('s', 21, 3, ('p', 'ShaderInput$17$ShaderInput', 'spi'), ['CPT_InternalName', 'LVecBase3d const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$18$ShaderInput', 'sp'), ['CPT_InternalName', 'LVecBase3d const&']),
        ('s', 21, 3, ('p', 'ShaderInput$19$ShaderInput', 'spi'), ['CPT_InternalName', 'LVecBase3f const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$20$ShaderInput', 'sp'), ['CPT_InternalName', 'LVecBase3f const&']),
        ('s', 21, 3, ('p', 'ShaderInput$21$ShaderInput', 'spi'), ['CPT_InternalName', 'LVecBase3i const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$22$ShaderInput', 'sp'), ['CPT_InternalName', 'LVecBase3i const&']),
        ('s', 21, 3, ('p', 'ShaderInput$23$ShaderInput', 'spi'), ['CPT_InternalName', 'LVecBase4d const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$24$ShaderInput', 'sp'), ['CPT_InternalName', 'LVecBase4d const&']),
        ('s', 21, 3, ('p', 'ShaderInput$25$ShaderInput', 'spi'), ['CPT_InternalName', 'LVecBase4f const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$26$ShaderInput', 'sp'), ['CPT_InternalName', 'LVecBase4f const&']),
        ('s', 21, 3, ('p', 'ShaderInput$27$ShaderInput', 'spi'), ['CPT_InternalName', 'LVecBase4i const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$28$ShaderInput', 'sp'), ['CPT_InternalName', 'LVecBase4i const&']),
        ('s', 21, 3, ('p', 'ShaderInput$29$ShaderInput', 'spi'), ['CPT_InternalName', 'NodePath const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$30$ShaderInput', 'sp'), ['CPT_InternalName', 'NodePath const&']),
        ('s', 21, 3, ('p', 'ShaderInput$31$ShaderInput', 'spi'), ['CPT_InternalName', 'PTA_LMatrix3d const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$32$ShaderInput', 'sp'), ['CPT_InternalName', 'PTA_LMatrix3d const&']),
        ('s', 21, 3, ('p', 'ShaderInput$33$ShaderInput', 'spi'), ['CPT_InternalName', 'PTA_LMatrix3f const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$34$ShaderInput', 'sp'), ['CPT_InternalName', 'PTA_LMatrix3f const&']),
        ('s', 21, 3, ('p', 'ShaderInput$35$ShaderInput', 'spi'), ['CPT_InternalName', 'PTA_LMatrix4d const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$36$ShaderInput', 'sp'), ['CPT_InternalName', 'PTA_LMatrix4d const&']),
        ('s', 21, 3, ('p', 'ShaderInput$37$ShaderInput', 'spi'), ['CPT_InternalName', 'PTA_LMatrix4f const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$38$ShaderInput', 'sp'), ['CPT_InternalName', 'PTA_LMatrix4f const&']),
        ('s', 21, 3, ('p', 'ShaderInput$39$ShaderInput', 'spi'), ['CPT_InternalName', 'PTA_LVecBase2d const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$40$ShaderInput', 'sp'), ['CPT_InternalName', 'PTA_LVecBase2d const&']),
        ('s', 21, 3, ('p', 'ShaderInput$41$ShaderInput', 'spi'), ['CPT_InternalName', 'PTA_LVecBase2f const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$42$ShaderInput', 'sp'), ['CPT_InternalName', 'PTA_LVecBase2f const&']),
        ('s', 21, 3, ('p', 'ShaderInput$43$ShaderInput', 'spi'), ['CPT_InternalName', 'PTA_LVecBase2i const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$44$ShaderInput', 'sp'), ['CPT_InternalName', 'PTA_LVecBase2i const&']),
        ('s', 21, 3, ('p', 'ShaderInput$45$ShaderInput', 'spi'), ['CPT_InternalName', 'PTA_LVecBase3d const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$46$ShaderInput', 'sp'), ['CPT_InternalName', 'PTA_LVecBase3d const&']),
        ('s', 21, 3, ('p', 'ShaderInput$47$ShaderInput', 'spi'), ['CPT_InternalName', 'PTA_LVecBase3f const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$48$ShaderInput', 'sp'), ['CPT_InternalName', 'PTA_LVecBase3f const&']),
        ('s', 21, 3, ('p', 'ShaderInput$49$ShaderInput', 'spi'), ['CPT_InternalName', 'PTA_LVecBase3i const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$50$ShaderInput', 'sp'), ['CPT_InternalName', 'PTA_LVecBase3i const&']),
        ('s', 21, 3, ('p', 'ShaderInput$51$ShaderInput', 'spi'), ['CPT_InternalName', 'PTA_LVecBase4d const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$52$ShaderInput', 'sp'), ['CPT_InternalName', 'PTA_LVecBase4d const&']),
        ('s', 21, 3, ('p', 'ShaderInput$53$ShaderInput', 'spi'), ['CPT_InternalName', 'PTA_LVecBase4f const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$54$ShaderInput', 'sp'), ['CPT_InternalName', 'PTA_LVecBase4f const&']),
        ('s', 21, 3, ('p', 'ShaderInput$55$ShaderInput', 'spi'), ['CPT_InternalName', 'PTA_LVecBase4i const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$56$ShaderInput', 'sp'), ['CPT_InternalName', 'PTA_LVecBase4i const&']),
        ('s', 21, 3, ('p', 'ShaderInput$57$ShaderInput', 'spi'), ['CPT_InternalName', 'PTA_double const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$58$ShaderInput', 'sp'), ['CPT_InternalName', 'PTA_double const&']),
        ('s', 21, 3, ('p', 'ShaderInput$59$ShaderInput', 'spi'), ['CPT_InternalName', 'PTA_float const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$60$ShaderInput', 'sp'), ['CPT_InternalName', 'PTA_float const&']),
        ('s', 21, 3, ('p', 'ShaderInput$61$ShaderInput', 'spi'), ['CPT_InternalName', 'PTA_int const&', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$62$ShaderInput', 'sp'), ['CPT_InternalName', 'PTA_int const&']),
        ('s', 21, 3, ('p', 'ShaderInput$63$ShaderInput', 'spi'), ['CPT_InternalName', 'ParamValueBase*', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$64$ShaderInput', 'sp'), ['CPT_InternalName', 'ParamValueBase*']),
        ('s', 21, 3, ('p', 'ShaderInput$65$ShaderInput', 'spi'), ['CPT_InternalName', 'ShaderBuffer*', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$66$ShaderInput', 'sp'), ['CPT_InternalName', 'ShaderBuffer*']),
        ('s', 21, 4, ('p', 'ShaderInput$67$ShaderInput', 'sppi'), ['CPT_InternalName', 'Texture*', 'SamplerState const&', 'int']),
        ('s', 21, 3, ('p', 'ShaderInput$68$ShaderInput', 'spp'), ['CPT_InternalName', 'Texture*', 'SamplerState const&']),
        ('s', 21, 7, ('p', 'ShaderInput$69$ShaderInput', 'spBBiii'), ['CPT_InternalName', 'Texture*', 'bool', 'bool', 'int', 'int', 'int']),
        ('s', 21, 6, ('p', 'ShaderInput$70$ShaderInput', 'spBBii'), ['CPT_InternalName', 'Texture*', 'bool', 'bool', 'int', 'int']),
        ('s', 21, 5, ('p', 'ShaderInput$71$ShaderInput', 'spBBi'), ['CPT_InternalName', 'Texture*', 'bool', 'bool', 'int']),
        ('s', 21, 4, ('p', 'ShaderInput$72$ShaderInput', 'spBB'), ['CPT_InternalName', 'Texture*', 'bool', 'bool']),
        ('s', 21, 3, ('p', 'ShaderInput$73$ShaderInput', 'spi'), ['CPT_InternalName', 'Texture*', 'int']),
        ('s', 21, 2, ('p', 'ShaderInput$74$ShaderInput', 'sp'), ['CPT_InternalName', 'Texture*']),
        ('s', 21, 2, ('p', 'ShaderInput$75$ShaderInput', 'si'), ['CPT_InternalName', 'int']),
        ('s', 21, 1, ('p', 'ShaderInput$76$ShaderInput', 's'), ['CPT_InternalName']),
        ('s', 21, 1, ('p', 'ShaderInput$77$ShaderInput', 'p'), ['ShaderInput const&']),
    ]

    # classmethod type calls

    c.ct['get_blank'] = [
        ('s', 21, 0, ('p', 'ShaderInput$1$get_blank', ''), []),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'ShaderInput$89$register_with_read_factory', ''), []),
    ]

    @classmethod
    def get_blank(cls, *args,**kw):
        return ( cls.c.get('get_blank', None) or cls.c.call(ShaderInput, 'get_blank', None) )(*args,**kw)

    @classmethod
    def register_with_read_factory(cls, *args,**kw):
        return ( cls.c.get('register_with_read_factory', None) or cls.c.call(ShaderInput, 'register_with_read_factory', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_hash'] = [
        ('d', 'l', 1, ('l', 'ShaderInput$78$add_hash', 'pl'), ['std::size_t']),
    ]
    c.ct['get_name'] = [
        ('d', 's', 0, ('s', 'ShaderInput$79$get_name', 'p'), []),
    ]
    c.ct['get_nodepath'] = [
        ('d', 17, 0, ('p', 'ShaderInput$84$get_nodepath', 'p'), []),
    ]
    c.ct['get_param'] = [
        ('d', 'p', 0, ('p', 'ShaderInput$87$get_param', 'p'), []),
    ]
    c.ct['get_priority'] = [
        ('d', 'i', 0, ('i', 'ShaderInput$81$get_priority', 'p'), []),
    ]
    c.ct['get_ptr'] = [
        ('d', 'p', 0, ('p', 'ShaderInput$83$get_ptr', 'p'), []),
    ]
    c.ct['get_sampler'] = [
        ('d', 'p', 0, ('p', 'ShaderInput$86$get_sampler', 'p'), []),
    ]
    c.ct['get_texture'] = [
        ('d', 64, 0, ('p', 'ShaderInput$85$get_texture', 'p'), []),
    ]
    c.ct['get_value'] = [
        ('d', 63, 0, ('p', 'ShaderInput$88$get_value', 'p'), []),
    ]
    c.ct['get_value_type'] = [
        ('d', 'i', 0, ('i', 'ShaderInput$80$get_value_type', 'p'), []),
    ]
    c.ct['get_vector'] = [
        ('d', 12, 0, ('p', 'ShaderInput$82$get_vector', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(ShaderInput, attr, self)

ShaderInput.c.link(ShaderInput)



class TextEncoder(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("TextEncoder", "upanda3d", """libupanda3d_c.so""")

    # enum Encoding

    E_iso8859 = const(0)
    E_unicode = const(2)
    E_utf16be = const(2)
    E_utf8 = const(1)


    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_TextNode'] = [
        ('d', 91, 0, ('p', 'TextEncoder$1$downcast_to_TextNode', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TextEncoder, attr, self)

TextEncoder.c.link(TextEncoder)



class TextProperties(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("TextProperties", "upanda3d", """libupanda3d_c.so""")

    # enum Alignment

    A_boxed_center = const(5)
    A_boxed_left = const(3)
    A_boxed_right = const(4)
    A_center = const(2)
    A_left = const(0)
    A_right = const(1)


    # enum Direction

    D_ltr = const(0)
    D_rtl = const(1)


    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_TextNode'] = [
        ('d', 91, 0, ('p', 'TextProperties$1$downcast_to_TextNode', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TextProperties, attr, self)

TextProperties.c.link(TextProperties)



class TextureCollection(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("TextureCollection", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 24, 0, ('p', 'TextureCollection$1$TextureCollection', ''), []),
        ('s', 24, 1, ('p', 'TextureCollection$2$TextureCollection', 'p'), ['TextureCollection const&']),
    ]

    # classmethod type calls


    # instance method type calls

    c.ct['add_texture'] = [
        ('d', 'v', 1, ('v', 'TextureCollection$3$add_texture', 'pp'), ['Texture*']),
    ]
    c.ct['add_textures_from'] = [
        ('d', 'v', 1, ('v', 'TextureCollection$5$add_textures_from', 'pp'), ['TextureCollection const&']),
    ]
    c.ct['append'] = [
        ('d', 'v', 1, ('v', 'TextureCollection$15$append', 'pp'), ['Texture*']),
    ]
    c.ct['clear'] = [
        ('d', 'v', 0, ('v', 'TextureCollection$9$clear', 'p'), []),
    ]
    c.ct['extend'] = [
        ('d', 'v', 1, ('v', 'TextureCollection$16$extend', 'pp'), ['TextureCollection const&']),
    ]
    c.ct['find_texture'] = [
        ('d', 64, 1, ('p', 'TextureCollection$11$find_texture', 'ps'), ['std::string const&']),
    ]
    c.ct['get_num_textures'] = [
        ('d', 'i', 0, ('i', 'TextureCollection$12$get_num_textures', 'p'), []),
    ]
    c.ct['get_texture'] = [
        ('d', 64, 1, ('p', 'TextureCollection$13$get_texture', 'pi'), ['int']),
    ]
    c.ct['has_texture'] = [
        ('d', 'B', 1, ('B', 'TextureCollection$8$has_texture', 'pp'), ['Texture*']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'TextureCollection$17$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['remove_duplicate_textures'] = [
        ('d', 'v', 0, ('v', 'TextureCollection$7$remove_duplicate_textures', 'p'), []),
    ]
    c.ct['remove_texture'] = [
        ('d', 'B', 1, ('B', 'TextureCollection$4$remove_texture', 'pp'), ['Texture*']),
    ]
    c.ct['remove_textures_from'] = [
        ('d', 'v', 1, ('v', 'TextureCollection$6$remove_textures_from', 'pp'), ['TextureCollection const&']),
    ]
    c.ct['reserve'] = [
        ('d', 'v', 1, ('v', 'TextureCollection$10$reserve', 'pl'), ['std::size_t']),
    ]
    c.ct['size'] = [
        ('d', 'i', 0, ('i', 'TextureCollection$14$size', 'p'), []),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'TextureCollection$18$write', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'v', 1, ('v', 'TextureCollection$19$write', 'pp'), ['std::ostream&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TextureCollection, attr, self)

TextureCollection.c.link(TextureCollection)



class TouchInfo(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("TouchInfo", "upanda3d", """libupanda3d_c.so""")

    # enum TouchInfoFlags

    TIF_down = const(2)
    TIF_move = const(1)
    TIF_up = const(4)


    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 25, 0, ('p', 'TouchInfo$1$TouchInfo', ''), []),
        ('s', 25, 1, ('p', 'TouchInfo$2$TouchInfo', 'p'), ['TouchInfo const&']),
    ]

    # classmethod type calls


    # instance method type calls

    c.ct['get_flags'] = [
        ('d', 'i', 0, ('i', 'TouchInfo$10$get_flags', 'p'), []),
    ]
    c.ct['get_id'] = [
        ('d', 'i', 0, ('i', 'TouchInfo$9$get_id', 'p'), []),
    ]
    c.ct['get_x'] = [
        ('d', 'i', 0, ('i', 'TouchInfo$7$get_x', 'p'), []),
    ]
    c.ct['get_y'] = [
        ('d', 'i', 0, ('i', 'TouchInfo$8$get_y', 'p'), []),
    ]
    c.ct['set_flags'] = [
        ('d', 'v', 1, ('v', 'TouchInfo$6$set_flags', 'pi'), ['int']),
    ]
    c.ct['set_id'] = [
        ('d', 'v', 1, ('v', 'TouchInfo$5$set_id', 'pi'), ['int']),
    ]
    c.ct['set_x'] = [
        ('d', 'v', 1, ('v', 'TouchInfo$3$set_x', 'pi'), ['int']),
    ]
    c.ct['set_y'] = [
        ('d', 'v', 1, ('v', 'TouchInfo$4$set_y', 'pi'), ['int']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TouchInfo, attr, self)

TouchInfo.c.link(TouchInfo)



class UpdateSeq(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("UpdateSeq", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 26, 0, ('p', 'UpdateSeq$1$UpdateSeq', ''), []),
        ('s', 26, 1, ('p', 'UpdateSeq$2$UpdateSeq', 'p'), ['UpdateSeq const&']),
    ]

    # classmethod type calls

    c.ct['fresh'] = [
        ('s', 'p', 0, ('p', 'UpdateSeq$5$fresh', ''), []),
    ]
    c.ct['initial'] = [
        ('s', 'p', 0, ('p', 'UpdateSeq$3$initial', ''), []),
    ]
    c.ct['old'] = [
        ('s', 'p', 0, ('p', 'UpdateSeq$4$old', ''), []),
    ]

    @classmethod
    def fresh(cls, *args,**kw):
        return ( cls.c.get('fresh', None) or cls.c.call(UpdateSeq, 'fresh', None) )(*args,**kw)

    @classmethod
    def initial(cls, *args,**kw):
        return ( cls.c.get('initial', None) or cls.c.call(UpdateSeq, 'initial', None) )(*args,**kw)

    @classmethod
    def old(cls, *args,**kw):
        return ( cls.c.get('old', None) or cls.c.call(UpdateSeq, 'old', None) )(*args,**kw)

    # instance method type calls

    c.ct['clear'] = [
        ('d', 'v', 0, ('v', 'UpdateSeq$6$clear', 'p'), []),
    ]
    c.ct['get_seq'] = [
        ('d', 'p', 0, ('p', 'UpdateSeq$11$get_seq', 'p'), []),
    ]
    c.ct['is_fresh'] = [
        ('d', 'B', 0, ('B', 'UpdateSeq$9$is_fresh', 'p'), []),
    ]
    c.ct['is_initial'] = [
        ('d', 'B', 0, ('B', 'UpdateSeq$7$is_initial', 'p'), []),
    ]
    c.ct['is_old'] = [
        ('d', 'B', 0, ('B', 'UpdateSeq$8$is_old', 'p'), []),
    ]
    c.ct['is_special'] = [
        ('d', 'B', 0, ('B', 'UpdateSeq$10$is_special', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'UpdateSeq$12$output', 'pp'), ['std::ostream&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(UpdateSeq, attr, self)

UpdateSeq.c.link(UpdateSeq)



class WindowProperties(cxx.cplusplus):
    __bases__ = tuple([])
    c = cxx.cstructs()
    c.register("WindowProperties", "upanda3d", """libupanda3d_c.so""")

    # enum ZOrder

    Z_bottom = const(0)
    Z_normal = const(1)
    Z_top = const(2)


    # enum MouseMode

    M_absolute = const(0)
    M_confined = const(2)
    M_relative = const(1)


    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 27, 0, ('p', 'WindowProperties$1$WindowProperties', ''), []),
        ('s', 27, 1, ('p', 'WindowProperties$2$WindowProperties', 'p'), ['WindowProperties const&']),
    ]

    # classmethod type calls

    c.ct['clear_default'] = [
        ('s', 'v', 0, ('v', 'WindowProperties$6$clear_default', ''), []),
    ]
    c.ct['get_config_properties'] = [
        ('s', 27, 0, ('p', 'WindowProperties$3$get_config_properties', ''), []),
    ]
    c.ct['get_default'] = [
        ('s', 27, 0, ('p', 'WindowProperties$4$get_default', ''), []),
    ]
    c.ct['set_default'] = [
        ('s', 'v', 1, ('v', 'WindowProperties$5$set_default', 'p'), ['WindowProperties const&']),
    ]
    c.ct['size'] = [
        ('s', 27, 1, ('p', 'WindowProperties$7$size', 'p'), ['LVecBase2i const&']),
        ('s', 27, 2, ('p', 'WindowProperties$8$size', 'ii'), ['int', 'int']),
    ]

    @classmethod
    def clear_default(cls, *args,**kw):
        return ( cls.c.get('clear_default', None) or cls.c.call(WindowProperties, 'clear_default', None) )(*args,**kw)

    @classmethod
    def get_config_properties(cls, *args,**kw):
        return ( cls.c.get('get_config_properties', None) or cls.c.call(WindowProperties, 'get_config_properties', None) )(*args,**kw)

    @classmethod
    def get_default(cls, *args,**kw):
        return ( cls.c.get('get_default', None) or cls.c.call(WindowProperties, 'get_default', None) )(*args,**kw)

    @classmethod
    def set_default(cls, *args,**kw):
        return ( cls.c.get('set_default', None) or cls.c.call(WindowProperties, 'set_default', None) )(*args,**kw)

    @classmethod
    def size(cls, *args,**kw):
        return ( cls.c.get('size', None) or cls.c.call(WindowProperties, 'size', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_properties'] = [
        ('d', 'v', 1, ('v', 'WindowProperties$83$add_properties', 'pp'), ['WindowProperties const&']),
    ]
    c.ct['clear'] = [
        ('d', 'v', 0, ('v', 'WindowProperties$9$clear', 'p'), []),
    ]
    c.ct['clear_cursor_filename'] = [
        ('d', 'v', 0, ('v', 'WindowProperties$72$clear_cursor_filename', 'p'), []),
    ]
    c.ct['clear_cursor_hidden'] = [
        ('d', 'v', 0, ('v', 'WindowProperties$64$clear_cursor_hidden', 'p'), []),
    ]
    c.ct['clear_fixed_size'] = [
        ('d', 'v', 0, ('v', 'WindowProperties$40$clear_fixed_size', 'p'), []),
    ]
    c.ct['clear_foreground'] = [
        ('d', 'v', 0, ('v', 'WindowProperties$48$clear_foreground', 'p'), []),
    ]
    c.ct['clear_fullscreen'] = [
        ('d', 'v', 0, ('v', 'WindowProperties$44$clear_fullscreen', 'p'), []),
    ]
    c.ct['clear_icon_filename'] = [
        ('d', 'v', 0, ('v', 'WindowProperties$68$clear_icon_filename', 'p'), []),
    ]
    c.ct['clear_minimized'] = [
        ('d', 'v', 0, ('v', 'WindowProperties$52$clear_minimized', 'p'), []),
    ]
    c.ct['clear_mouse_mode'] = [
        ('d', 'v', 0, ('v', 'WindowProperties$28$clear_mouse_mode', 'p'), []),
    ]
    c.ct['clear_open'] = [
        ('d', 'v', 0, ('v', 'WindowProperties$60$clear_open', 'p'), []),
    ]
    c.ct['clear_origin'] = [
        ('d', 'v', 0, ('v', 'WindowProperties$17$clear_origin', 'p'), []),
    ]
    c.ct['clear_parent_window'] = [
        ('d', 'v', 0, ('v', 'WindowProperties$82$clear_parent_window', 'p'), []),
    ]
    c.ct['clear_raw_mice'] = [
        ('d', 'v', 0, ('v', 'WindowProperties$56$clear_raw_mice', 'p'), []),
    ]
    c.ct['clear_size'] = [
        ('d', 'v', 0, ('v', 'WindowProperties$24$clear_size', 'p'), []),
    ]
    c.ct['clear_title'] = [
        ('d', 'v', 0, ('v', 'WindowProperties$32$clear_title', 'p'), []),
    ]
    c.ct['clear_undecorated'] = [
        ('d', 'v', 0, ('v', 'WindowProperties$36$clear_undecorated', 'p'), []),
    ]
    c.ct['clear_z_order'] = [
        ('d', 'v', 0, ('v', 'WindowProperties$76$clear_z_order', 'p'), []),
    ]
    c.ct['get_cursor_filename'] = [
        ('d', 3, 0, ('p', 'WindowProperties$70$get_cursor_filename', 'p'), []),
    ]
    c.ct['get_cursor_hidden'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$62$get_cursor_hidden', 'p'), []),
    ]
    c.ct['get_fixed_size'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$38$get_fixed_size', 'p'), []),
    ]
    c.ct['get_foreground'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$46$get_foreground', 'p'), []),
    ]
    c.ct['get_fullscreen'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$42$get_fullscreen', 'p'), []),
    ]
    c.ct['get_icon_filename'] = [
        ('d', 3, 0, ('p', 'WindowProperties$66$get_icon_filename', 'p'), []),
    ]
    c.ct['get_minimized'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$50$get_minimized', 'p'), []),
    ]
    c.ct['get_mouse_mode'] = [
        ('d', 'p', 0, ('p', 'WindowProperties$27$get_mouse_mode', 'p'), []),
    ]
    c.ct['get_open'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$58$get_open', 'p'), []),
    ]
    c.ct['get_origin'] = [
        ('d', 'p', 0, ('p', 'WindowProperties$13$get_origin', 'p'), []),
    ]
    c.ct['get_parent_window'] = [
        ('d', 62, 0, ('p', 'WindowProperties$80$get_parent_window', 'p'), []),
    ]
    c.ct['get_raw_mice'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$54$get_raw_mice', 'p'), []),
    ]
    c.ct['get_size'] = [
        ('d', 'p', 0, ('p', 'WindowProperties$20$get_size', 'p'), []),
    ]
    c.ct['get_title'] = [
        ('d', 's', 0, ('s', 'WindowProperties$30$get_title', 'p'), []),
    ]
    c.ct['get_undecorated'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$34$get_undecorated', 'p'), []),
    ]
    c.ct['get_x_origin'] = [
        ('d', 'i', 0, ('i', 'WindowProperties$14$get_x_origin', 'p'), []),
    ]
    c.ct['get_x_size'] = [
        ('d', 'i', 0, ('i', 'WindowProperties$21$get_x_size', 'p'), []),
    ]
    c.ct['get_y_origin'] = [
        ('d', 'i', 0, ('i', 'WindowProperties$15$get_y_origin', 'p'), []),
    ]
    c.ct['get_y_size'] = [
        ('d', 'i', 0, ('i', 'WindowProperties$22$get_y_size', 'p'), []),
    ]
    c.ct['get_z_order'] = [
        ('d', 'p', 0, ('p', 'WindowProperties$74$get_z_order', 'p'), []),
    ]
    c.ct['has_cursor_filename'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$71$has_cursor_filename', 'p'), []),
    ]
    c.ct['has_cursor_hidden'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$63$has_cursor_hidden', 'p'), []),
    ]
    c.ct['has_fixed_size'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$39$has_fixed_size', 'p'), []),
    ]
    c.ct['has_foreground'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$47$has_foreground', 'p'), []),
    ]
    c.ct['has_fullscreen'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$43$has_fullscreen', 'p'), []),
    ]
    c.ct['has_icon_filename'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$67$has_icon_filename', 'p'), []),
    ]
    c.ct['has_minimized'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$51$has_minimized', 'p'), []),
    ]
    c.ct['has_mouse_mode'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$25$has_mouse_mode', 'p'), []),
    ]
    c.ct['has_open'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$59$has_open', 'p'), []),
    ]
    c.ct['has_origin'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$16$has_origin', 'p'), []),
    ]
    c.ct['has_parent_window'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$81$has_parent_window', 'p'), []),
    ]
    c.ct['has_raw_mice'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$55$has_raw_mice', 'p'), []),
    ]
    c.ct['has_size'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$23$has_size', 'p'), []),
    ]
    c.ct['has_title'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$31$has_title', 'p'), []),
    ]
    c.ct['has_undecorated'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$35$has_undecorated', 'p'), []),
    ]
    c.ct['has_z_order'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$75$has_z_order', 'p'), []),
    ]
    c.ct['is_any_specified'] = [
        ('d', 'B', 0, ('B', 'WindowProperties$10$is_any_specified', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'WindowProperties$84$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['set_cursor_filename'] = [
        ('d', 'v', 1, ('v', 'WindowProperties$69$set_cursor_filename', 'pp'), ['Filename const&']),
    ]
    c.ct['set_cursor_hidden'] = [
        ('d', 'v', 1, ('v', 'WindowProperties$61$set_cursor_hidden', 'pB'), ['bool']),
    ]
    c.ct['set_fixed_size'] = [
        ('d', 'v', 1, ('v', 'WindowProperties$37$set_fixed_size', 'pB'), ['bool']),
    ]
    c.ct['set_foreground'] = [
        ('d', 'v', 1, ('v', 'WindowProperties$45$set_foreground', 'pB'), ['bool']),
    ]
    c.ct['set_fullscreen'] = [
        ('d', 'v', 1, ('v', 'WindowProperties$41$set_fullscreen', 'pB'), ['bool']),
    ]
    c.ct['set_icon_filename'] = [
        ('d', 'v', 1, ('v', 'WindowProperties$65$set_icon_filename', 'pp'), ['Filename const&']),
    ]
    c.ct['set_minimized'] = [
        ('d', 'v', 1, ('v', 'WindowProperties$49$set_minimized', 'pB'), ['bool']),
    ]
    c.ct['set_mouse_mode'] = [
        ('d', 'v', 1, ('v', 'WindowProperties$26$set_mouse_mode', 'pp'), ['WindowProperties::MouseMode']),
    ]
    c.ct['set_open'] = [
        ('d', 'v', 1, ('v', 'WindowProperties$57$set_open', 'pB'), ['bool']),
    ]
    c.ct['set_origin'] = [
        ('d', 'v', 1, ('v', 'WindowProperties$11$set_origin', 'pp'), ['LPoint2i const&']),
        ('d', 'v', 2, ('v', 'WindowProperties$12$set_origin', 'pii'), ['int', 'int']),
    ]
    c.ct['set_parent_window'] = [
        ('d', 'v', 1, ('v', 'WindowProperties$77$set_parent_window', 'pp'), ['WindowHandle*']),
        ('d', 'v', 0, ('v', 'WindowProperties$78$set_parent_window', 'p'), []),
        ('d', 'v', 1, ('v', 'WindowProperties$79$set_parent_window', 'pl'), ['std::size_t']),
    ]
    c.ct['set_raw_mice'] = [
        ('d', 'v', 1, ('v', 'WindowProperties$53$set_raw_mice', 'pB'), ['bool']),
    ]
    c.ct['set_size'] = [
        ('d', 'v', 1, ('v', 'WindowProperties$18$set_size', 'pp'), ['LVector2i const&']),
        ('d', 'v', 2, ('v', 'WindowProperties$19$set_size', 'pii'), ['int', 'int']),
    ]
    c.ct['set_title'] = [
        ('d', 'v', 1, ('v', 'WindowProperties$29$set_title', 'ps'), ['std::string const&']),
    ]
    c.ct['set_undecorated'] = [
        ('d', 'v', 1, ('v', 'WindowProperties$33$set_undecorated', 'pB'), ['bool']),
    ]
    c.ct['set_z_order'] = [
        ('d', 'v', 1, ('v', 'WindowProperties$73$set_z_order', 'pp'), ['WindowProperties::ZOrder']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(WindowProperties, attr, self)

WindowProperties.c.link(WindowProperties)



class GeomVertexColumn(GeomEnums):
    __bases__ = tuple([GeomEnums])
    c = cxx.cstructs()
    c.register("GeomVertexColumn", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 28, 8, ('p', 'GeomVertexColumn$1$GeomVertexColumn', 'sippiiii'), ['CPT_InternalName', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents', 'int', 'int', 'int', 'int']),
        ('s', 28, 7, ('p', 'GeomVertexColumn$2$GeomVertexColumn', 'sippiii'), ['CPT_InternalName', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents', 'int', 'int', 'int']),
        ('s', 28, 6, ('p', 'GeomVertexColumn$3$GeomVertexColumn', 'sippii'), ['CPT_InternalName', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents', 'int', 'int']),
        ('s', 28, 5, ('p', 'GeomVertexColumn$4$GeomVertexColumn', 'sippi'), ['CPT_InternalName', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents', 'int']),
        ('s', 28, 1, ('p', 'GeomVertexColumn$5$GeomVertexColumn', 'p'), ['GeomVertexColumn const&']),
    ]

    # classmethod type calls


    # instance method type calls

    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'GeomVertexColumn$29$compare_to', 'pp'), ['GeomVertexColumn const&']),
    ]
    c.ct['fillin'] = [
        ('d', 'v', 2, ('v', 'GeomVertexColumn$31$fillin', 'ppp'), ['DatagramIterator&', 'BamReader*']),
    ]
    c.ct['get_column_alignment'] = [
        ('d', 'i', 0, ('i', 'GeomVertexColumn$13$get_column_alignment', 'p'), []),
    ]
    c.ct['get_component_bytes'] = [
        ('d', 'i', 0, ('i', 'GeomVertexColumn$15$get_component_bytes', 'p'), []),
    ]
    c.ct['get_contents'] = [
        ('d', 'p', 0, ('p', 'GeomVertexColumn$11$get_contents', 'p'), []),
    ]
    c.ct['get_element_stride'] = [
        ('d', 'i', 0, ('i', 'GeomVertexColumn$14$get_element_stride', 'p'), []),
    ]
    c.ct['get_name'] = [
        ('d', 's', 0, ('s', 'GeomVertexColumn$6$get_name', 'p'), []),
    ]
    c.ct['get_num_components'] = [
        ('d', 'i', 0, ('i', 'GeomVertexColumn$7$get_num_components', 'p'), []),
    ]
    c.ct['get_num_elements'] = [
        ('d', 'i', 0, ('i', 'GeomVertexColumn$9$get_num_elements', 'p'), []),
    ]
    c.ct['get_num_values'] = [
        ('d', 'i', 0, ('i', 'GeomVertexColumn$8$get_num_values', 'p'), []),
    ]
    c.ct['get_numeric_type'] = [
        ('d', 'p', 0, ('p', 'GeomVertexColumn$10$get_numeric_type', 'p'), []),
    ]
    c.ct['get_start'] = [
        ('d', 'i', 0, ('i', 'GeomVertexColumn$12$get_start', 'p'), []),
    ]
    c.ct['get_total_bytes'] = [
        ('d', 'i', 0, ('i', 'GeomVertexColumn$16$get_total_bytes', 'p'), []),
    ]
    c.ct['has_homogeneous_coord'] = [
        ('d', 'B', 0, ('B', 'GeomVertexColumn$17$has_homogeneous_coord', 'p'), []),
    ]
    c.ct['is_bytewise_equivalent'] = [
        ('d', 'B', 1, ('B', 'GeomVertexColumn$19$is_bytewise_equivalent', 'pp'), ['GeomVertexColumn const&']),
    ]
    c.ct['is_packed_argb'] = [
        ('d', 'B', 0, ('B', 'GeomVertexColumn$27$is_packed_argb', 'p'), []),
    ]
    c.ct['is_uint8_rgba'] = [
        ('d', 'B', 0, ('B', 'GeomVertexColumn$28$is_uint8_rgba', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'GeomVertexColumn$26$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['overlaps_with'] = [
        ('d', 'B', 2, ('B', 'GeomVertexColumn$18$overlaps_with', 'pii'), ['int', 'int']),
    ]
    c.ct['set_column_alignment'] = [
        ('d', 'v', 1, ('v', 'GeomVertexColumn$25$set_column_alignment', 'pi'), ['int']),
    ]
    c.ct['set_contents'] = [
        ('d', 'v', 1, ('v', 'GeomVertexColumn$23$set_contents', 'pp'), ['GeomEnums::Contents']),
    ]
    c.ct['set_name'] = [
        ('d', 'v', 1, ('v', 'GeomVertexColumn$20$set_name', 'pp'), ['InternalName*']),
    ]
    c.ct['set_num_components'] = [
        ('d', 'v', 1, ('v', 'GeomVertexColumn$21$set_num_components', 'pi'), ['int']),
    ]
    c.ct['set_numeric_type'] = [
        ('d', 'v', 1, ('v', 'GeomVertexColumn$22$set_numeric_type', 'pp'), ['GeomEnums::NumericType']),
    ]
    c.ct['set_start'] = [
        ('d', 'v', 1, ('v', 'GeomVertexColumn$24$set_start', 'pi'), ['int']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'GeomVertexColumn$30$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomVertexColumn, attr, self)

GeomVertexColumn.c.link(GeomVertexColumn)



class GeomVertexWriter(GeomEnums):
    __bases__ = tuple([GeomEnums])
    c = cxx.cstructs()
    c.register("GeomVertexWriter", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 29, 2, ('p', 'GeomVertexWriter$1$GeomVertexWriter', 'pp'), ['GeomVertexArrayData*', 'Thread*']),
        ('s', 29, 1, ('p', 'GeomVertexWriter$2$GeomVertexWriter', 'p'), ['GeomVertexArrayData*']),
        ('s', 29, 3, ('p', 'GeomVertexWriter$3$GeomVertexWriter', 'pip'), ['GeomVertexArrayData*', 'int', 'Thread*']),
        ('s', 29, 2, ('p', 'GeomVertexWriter$4$GeomVertexWriter', 'pi'), ['GeomVertexArrayData*', 'int']),
        ('s', 29, 3, ('p', 'GeomVertexWriter$5$GeomVertexWriter', 'psp'), ['GeomVertexData*', 'CPT_InternalName', 'Thread*']),
        ('s', 29, 2, ('p', 'GeomVertexWriter$6$GeomVertexWriter', 'ps'), ['GeomVertexData*', 'CPT_InternalName']),
        ('s', 29, 2, ('p', 'GeomVertexWriter$7$GeomVertexWriter', 'pp'), ['GeomVertexData*', 'Thread*']),
        ('s', 29, 1, ('p', 'GeomVertexWriter$8$GeomVertexWriter', 'p'), ['GeomVertexData*']),
        ('s', 29, 2, ('p', 'GeomVertexWriter$9$GeomVertexWriter', 'ps'), ['GeomVertexDataPipelineWriter*', 'InternalName const*']),
        ('s', 29, 1, ('p', 'GeomVertexWriter$10$GeomVertexWriter', 'p'), ['GeomVertexWriter const&']),
        ('s', 29, 1, ('p', 'GeomVertexWriter$11$GeomVertexWriter', 'p'), ['Thread*']),
        ('s', 29, 0, ('p', 'GeomVertexWriter$12$GeomVertexWriter', ''), []),
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
        ('d', 85, 0, ('p', 'GeomVertexWriter$14$get_array_data', 'p'), []),
    ]
    c.ct['get_array_handle'] = [
        ('d', 56, 0, ('p', 'GeomVertexWriter$15$get_array_handle', 'p'), []),
    ]
    c.ct['get_column'] = [
        ('d', 28, 0, ('p', 'GeomVertexWriter$25$get_column', 'p'), []),
    ]
    c.ct['get_current_thread'] = [
        ('d', 58, 0, ('p', 'GeomVertexWriter$17$get_current_thread', 'p'), []),
    ]
    c.ct['get_start_row'] = [
        ('d', 'i', 0, ('i', 'GeomVertexWriter$28$get_start_row', 'p'), []),
    ]
    c.ct['get_stride'] = [
        ('d', 'l', 0, ('l', 'GeomVertexWriter$16$get_stride', 'p'), []),
    ]
    c.ct['get_vertex_data'] = [
        ('d', 81, 0, ('p', 'GeomVertexWriter$13$get_vertex_data', 'p'), []),
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



class LPoint2d(LVecBase2d):
    __bases__ = tuple([LVecBase2d])
    c = cxx.cstructs()
    c.register("LPoint2d", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 30, 0, ('p', 'LPoint2d$1$LPoint2d', ''), []),
        ('s', 30, 1, ('p', 'LPoint2d$2$LPoint2d', 'p'), ['LPoint2d const&']),
        ('s', 30, 1, ('p', 'LPoint2d$3$LPoint2d', 'p'), ['LVecBase2d const&']),
        ('s', 30, 1, ('p', 'LPoint2d$4$LPoint2d', 'd'), ['double']),
        ('s', 30, 2, ('p', 'LPoint2d$5$LPoint2d', 'dd'), ['double', 'double']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LPoint2d$11$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LPoint2d$12$init_type', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 'p', 0, ('p', 'LPoint2d$7$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 'p', 0, ('p', 'LPoint2d$8$unit_y', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 'p', 0, ('p', 'LPoint2d$6$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LPoint2d, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LPoint2d, 'init_type', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LPoint2d, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LPoint2d, 'unit_y', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LPoint2d, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['normalized'] = [
        ('d', 'p', 0, ('p', 'LPoint2d$9$normalized', 'p'), []),
    ]
    c.ct['project'] = [
        ('d', 'p', 1, ('p', 'LPoint2d$10$project', 'pp'), ['LVecBase2d const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LPoint2d, attr, self)

LPoint2d.c.link(LPoint2d)



class LPoint2f(LVecBase2f):
    __bases__ = tuple([LVecBase2f])
    c = cxx.cstructs()
    c.register("LPoint2f", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 31, 0, ('p', 'LPoint2f$1$LPoint2f', ''), []),
        ('s', 31, 1, ('p', 'LPoint2f$2$LPoint2f', 'p'), ['LPoint2f const&']),
        ('s', 31, 1, ('p', 'LPoint2f$3$LPoint2f', 'p'), ['LVecBase2f const&']),
        ('s', 31, 1, ('p', 'LPoint2f$4$LPoint2f', 'f'), ['float']),
        ('s', 31, 2, ('p', 'LPoint2f$5$LPoint2f', 'ff'), ['float', 'float']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LPoint2f$11$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LPoint2f$12$init_type', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 31, 0, ('p', 'LPoint2f$7$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 31, 0, ('p', 'LPoint2f$8$unit_y', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 31, 0, ('p', 'LPoint2f$6$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LPoint2f, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LPoint2f, 'init_type', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LPoint2f, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LPoint2f, 'unit_y', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LPoint2f, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['normalized'] = [
        ('d', 31, 0, ('p', 'LPoint2f$9$normalized', 'p'), []),
    ]
    c.ct['project'] = [
        ('d', 31, 1, ('p', 'LPoint2f$10$project', 'pp'), ['LVecBase2f const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LPoint2f, attr, self)

LPoint2f.c.link(LPoint2f)



class LPoint2i(LVecBase2i):
    __bases__ = tuple([LVecBase2i])
    c = cxx.cstructs()
    c.register("LPoint2i", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 32, 0, ('p', 'LPoint2i$1$LPoint2i', ''), []),
        ('s', 32, 1, ('p', 'LPoint2i$2$LPoint2i', 'p'), ['LPoint2i const&']),
        ('s', 32, 1, ('p', 'LPoint2i$3$LPoint2i', 'p'), ['LVecBase2i const&']),
        ('s', 32, 1, ('p', 'LPoint2i$4$LPoint2i', 'i'), ['int']),
        ('s', 32, 2, ('p', 'LPoint2i$5$LPoint2i', 'ii'), ['int', 'int']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LPoint2i$9$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LPoint2i$10$init_type', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 'p', 0, ('p', 'LPoint2i$7$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 'p', 0, ('p', 'LPoint2i$8$unit_y', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 'p', 0, ('p', 'LPoint2i$6$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LPoint2i, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LPoint2i, 'init_type', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LPoint2i, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LPoint2i, 'unit_y', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LPoint2i, 'zero', None) )(*args,**kw)

    # instance method type calls



    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LPoint2i, attr, self)

LPoint2i.c.link(LPoint2i)



class LPoint3d(LVecBase3d):
    __bases__ = tuple([LVecBase3d])
    c = cxx.cstructs()
    c.register("LPoint3d", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 33, 0, ('p', 'LPoint3d$1$LPoint3d', ''), []),
        ('s', 33, 1, ('p', 'LPoint3d$2$LPoint3d', 'p'), ['LPoint3d const&']),
        ('s', 33, 2, ('p', 'LPoint3d$3$LPoint3d', 'pd'), ['LVecBase2d const&', 'double']),
        ('s', 33, 1, ('p', 'LPoint3d$4$LPoint3d', 'p'), ['LVecBase3d const&']),
        ('s', 33, 1, ('p', 'LPoint3d$5$LPoint3d', 'd'), ['double']),
        ('s', 33, 3, ('p', 'LPoint3d$6$LPoint3d', 'ddd'), ['double', 'double', 'double']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LPoint3d$21$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LPoint3d$22$init_type', ''), []),
    ]
    c.ct['origin'] = [
        ('s', 'p', 1, ('p', 'LPoint3d$17$origin', 'p'), ['CoordinateSystem']),
        ('s', 'p', 0, ('p', 'LPoint3d$18$origin', ''), []),
    ]
    c.ct['rfu'] = [
        ('s', 'p', 4, ('p', 'LPoint3d$19$rfu', 'dddp'), ['double', 'double', 'double', 'CoordinateSystem']),
        ('s', 'p', 3, ('p', 'LPoint3d$20$rfu', 'ddd'), ['double', 'double', 'double']),
    ]
    c.ct['unit_x'] = [
        ('s', 'p', 0, ('p', 'LPoint3d$8$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 'p', 0, ('p', 'LPoint3d$9$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 'p', 0, ('p', 'LPoint3d$10$unit_z', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 'p', 0, ('p', 'LPoint3d$7$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LPoint3d, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LPoint3d, 'init_type', None) )(*args,**kw)

    @classmethod
    def origin(cls, *args,**kw):
        return ( cls.c.get('origin', None) or cls.c.call(LPoint3d, 'origin', None) )(*args,**kw)

    @classmethod
    def rfu(cls, *args,**kw):
        return ( cls.c.get('rfu', None) or cls.c.call(LPoint3d, 'rfu', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LPoint3d, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LPoint3d, 'unit_y', None) )(*args,**kw)

    @classmethod
    def unit_z(cls, *args,**kw):
        return ( cls.c.get('unit_z', None) or cls.c.call(LPoint3d, 'unit_z', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LPoint3d, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['cross'] = [
        ('d', 'p', 1, ('p', 'LPoint3d$14$cross', 'pp'), ['LVecBase3d const&']),
    ]
    c.ct['get_xy'] = [
        ('d', 'p', 0, ('p', 'LPoint3d$11$get_xy', 'p'), []),
    ]
    c.ct['get_xz'] = [
        ('d', 'p', 0, ('p', 'LPoint3d$12$get_xz', 'p'), []),
    ]
    c.ct['get_yz'] = [
        ('d', 'p', 0, ('p', 'LPoint3d$13$get_yz', 'p'), []),
    ]
    c.ct['normalized'] = [
        ('d', 'p', 0, ('p', 'LPoint3d$15$normalized', 'p'), []),
    ]
    c.ct['project'] = [
        ('d', 'p', 1, ('p', 'LPoint3d$16$project', 'pp'), ['LVecBase3d const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LPoint3d, attr, self)

LPoint3d.c.link(LPoint3d)



class LPoint3f(LVecBase3f):
    __bases__ = tuple([LVecBase3f])
    c = cxx.cstructs()
    c.register("LPoint3f", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 34, 0, ('p', 'LPoint3f$1$LPoint3f', ''), []),
        ('s', 34, 1, ('p', 'LPoint3f$2$LPoint3f', 'p'), ['LPoint3f const&']),
        ('s', 34, 2, ('p', 'LPoint3f$3$LPoint3f', 'pf'), ['LVecBase2f const&', 'float']),
        ('s', 34, 1, ('p', 'LPoint3f$4$LPoint3f', 'p'), ['LVecBase3f const&']),
        ('s', 34, 1, ('p', 'LPoint3f$5$LPoint3f', 'f'), ['float']),
        ('s', 34, 3, ('p', 'LPoint3f$6$LPoint3f', 'fff'), ['float', 'float', 'float']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LPoint3f$21$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LPoint3f$22$init_type', ''), []),
    ]
    c.ct['origin'] = [
        ('s', 34, 1, ('p', 'LPoint3f$17$origin', 'p'), ['CoordinateSystem']),
        ('s', 34, 0, ('p', 'LPoint3f$18$origin', ''), []),
    ]
    c.ct['rfu'] = [
        ('s', 34, 4, ('p', 'LPoint3f$19$rfu', 'fffp'), ['float', 'float', 'float', 'CoordinateSystem']),
        ('s', 34, 3, ('p', 'LPoint3f$20$rfu', 'fff'), ['float', 'float', 'float']),
    ]
    c.ct['unit_x'] = [
        ('s', 34, 0, ('p', 'LPoint3f$8$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 34, 0, ('p', 'LPoint3f$9$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 34, 0, ('p', 'LPoint3f$10$unit_z', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 34, 0, ('p', 'LPoint3f$7$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LPoint3f, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LPoint3f, 'init_type', None) )(*args,**kw)

    @classmethod
    def origin(cls, *args,**kw):
        return ( cls.c.get('origin', None) or cls.c.call(LPoint3f, 'origin', None) )(*args,**kw)

    @classmethod
    def rfu(cls, *args,**kw):
        return ( cls.c.get('rfu', None) or cls.c.call(LPoint3f, 'rfu', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LPoint3f, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LPoint3f, 'unit_y', None) )(*args,**kw)

    @classmethod
    def unit_z(cls, *args,**kw):
        return ( cls.c.get('unit_z', None) or cls.c.call(LPoint3f, 'unit_z', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LPoint3f, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['cross'] = [
        ('d', 34, 1, ('p', 'LPoint3f$14$cross', 'pp'), ['LVecBase3f const&']),
    ]
    c.ct['get_xy'] = [
        ('d', 31, 0, ('p', 'LPoint3f$11$get_xy', 'p'), []),
    ]
    c.ct['get_xz'] = [
        ('d', 31, 0, ('p', 'LPoint3f$12$get_xz', 'p'), []),
    ]
    c.ct['get_yz'] = [
        ('d', 31, 0, ('p', 'LPoint3f$13$get_yz', 'p'), []),
    ]
    c.ct['normalized'] = [
        ('d', 34, 0, ('p', 'LPoint3f$15$normalized', 'p'), []),
    ]
    c.ct['project'] = [
        ('d', 34, 1, ('p', 'LPoint3f$16$project', 'pp'), ['LVecBase3f const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LPoint3f, attr, self)

LPoint3f.c.link(LPoint3f)



class LPoint3i(LVecBase3i):
    __bases__ = tuple([LVecBase3i])
    c = cxx.cstructs()
    c.register("LPoint3i", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 35, 0, ('p', 'LPoint3i$1$LPoint3i', ''), []),
        ('s', 35, 1, ('p', 'LPoint3i$2$LPoint3i', 'p'), ['LPoint3i const&']),
        ('s', 35, 2, ('p', 'LPoint3i$3$LPoint3i', 'pi'), ['LVecBase2i const&', 'int']),
        ('s', 35, 1, ('p', 'LPoint3i$4$LPoint3i', 'p'), ['LVecBase3i const&']),
        ('s', 35, 1, ('p', 'LPoint3i$5$LPoint3i', 'i'), ['int']),
        ('s', 35, 3, ('p', 'LPoint3i$6$LPoint3i', 'iii'), ['int', 'int', 'int']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LPoint3i$19$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LPoint3i$20$init_type', ''), []),
    ]
    c.ct['origin'] = [
        ('s', 'p', 1, ('p', 'LPoint3i$15$origin', 'p'), ['CoordinateSystem']),
        ('s', 'p', 0, ('p', 'LPoint3i$16$origin', ''), []),
    ]
    c.ct['rfu'] = [
        ('s', 'p', 4, ('p', 'LPoint3i$17$rfu', 'iiip'), ['int', 'int', 'int', 'CoordinateSystem']),
        ('s', 'p', 3, ('p', 'LPoint3i$18$rfu', 'iii'), ['int', 'int', 'int']),
    ]
    c.ct['unit_x'] = [
        ('s', 'p', 0, ('p', 'LPoint3i$8$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 'p', 0, ('p', 'LPoint3i$9$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 'p', 0, ('p', 'LPoint3i$10$unit_z', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 'p', 0, ('p', 'LPoint3i$7$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LPoint3i, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LPoint3i, 'init_type', None) )(*args,**kw)

    @classmethod
    def origin(cls, *args,**kw):
        return ( cls.c.get('origin', None) or cls.c.call(LPoint3i, 'origin', None) )(*args,**kw)

    @classmethod
    def rfu(cls, *args,**kw):
        return ( cls.c.get('rfu', None) or cls.c.call(LPoint3i, 'rfu', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LPoint3i, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LPoint3i, 'unit_y', None) )(*args,**kw)

    @classmethod
    def unit_z(cls, *args,**kw):
        return ( cls.c.get('unit_z', None) or cls.c.call(LPoint3i, 'unit_z', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LPoint3i, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['cross'] = [
        ('d', 'p', 1, ('p', 'LPoint3i$14$cross', 'pp'), ['LVecBase3i const&']),
    ]
    c.ct['get_xy'] = [
        ('d', 'p', 0, ('p', 'LPoint3i$11$get_xy', 'p'), []),
    ]
    c.ct['get_xz'] = [
        ('d', 'p', 0, ('p', 'LPoint3i$12$get_xz', 'p'), []),
    ]
    c.ct['get_yz'] = [
        ('d', 'p', 0, ('p', 'LPoint3i$13$get_yz', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LPoint3i, attr, self)

LPoint3i.c.link(LPoint3i)



class LPoint4d(LVecBase4d):
    __bases__ = tuple([LVecBase4d])
    c = cxx.cstructs()
    c.register("LPoint4d", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 36, 0, ('p', 'LPoint4d$1$LPoint4d', ''), []),
        ('s', 36, 1, ('p', 'LPoint4d$2$LPoint4d', 'p'), ['LPoint4d const&']),
        ('s', 36, 2, ('p', 'LPoint4d$3$LPoint4d', 'pd'), ['LVecBase3d const&', 'double']),
        ('s', 36, 1, ('p', 'LPoint4d$4$LPoint4d', 'p'), ['LVecBase4d const&']),
        ('s', 36, 1, ('p', 'LPoint4d$5$LPoint4d', 'd'), ['double']),
        ('s', 36, 4, ('p', 'LPoint4d$6$LPoint4d', 'dddd'), ['double', 'double', 'double', 'double']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LPoint4d$16$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LPoint4d$17$init_type', ''), []),
    ]
    c.ct['unit_w'] = [
        ('s', 36, 0, ('p', 'LPoint4d$11$unit_w', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 36, 0, ('p', 'LPoint4d$8$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 36, 0, ('p', 'LPoint4d$9$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 36, 0, ('p', 'LPoint4d$10$unit_z', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 36, 0, ('p', 'LPoint4d$7$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LPoint4d, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LPoint4d, 'init_type', None) )(*args,**kw)

    @classmethod
    def unit_w(cls, *args,**kw):
        return ( cls.c.get('unit_w', None) or cls.c.call(LPoint4d, 'unit_w', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LPoint4d, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LPoint4d, 'unit_y', None) )(*args,**kw)

    @classmethod
    def unit_z(cls, *args,**kw):
        return ( cls.c.get('unit_z', None) or cls.c.call(LPoint4d, 'unit_z', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LPoint4d, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['get_xy'] = [
        ('d', 'p', 0, ('p', 'LPoint4d$13$get_xy', 'p'), []),
    ]
    c.ct['get_xyz'] = [
        ('d', 'p', 0, ('p', 'LPoint4d$12$get_xyz', 'p'), []),
    ]
    c.ct['normalized'] = [
        ('d', 36, 0, ('p', 'LPoint4d$14$normalized', 'p'), []),
    ]
    c.ct['project'] = [
        ('d', 36, 1, ('p', 'LPoint4d$15$project', 'pp'), ['LVecBase4d const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LPoint4d, attr, self)

LPoint4d.c.link(LPoint4d)



class LPoint4f(LVecBase4f):
    __bases__ = tuple([LVecBase4f])
    c = cxx.cstructs()
    c.register("LPoint4f", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 37, 0, ('p', 'LPoint4f$1$LPoint4f', ''), []),
        ('s', 37, 1, ('p', 'LPoint4f$2$LPoint4f', 'p'), ['LPoint4f const&']),
        ('s', 37, 2, ('p', 'LPoint4f$3$LPoint4f', 'pf'), ['LVecBase3f const&', 'float']),
        ('s', 37, 1, ('p', 'LPoint4f$4$LPoint4f', 'p'), ['LVecBase4f const&']),
        ('s', 37, 1, ('p', 'LPoint4f$5$LPoint4f', 'f'), ['float']),
        ('s', 37, 4, ('p', 'LPoint4f$6$LPoint4f', 'ffff'), ['float', 'float', 'float', 'float']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LPoint4f$16$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LPoint4f$17$init_type', ''), []),
    ]
    c.ct['unit_w'] = [
        ('s', 37, 0, ('p', 'LPoint4f$11$unit_w', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 37, 0, ('p', 'LPoint4f$8$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 37, 0, ('p', 'LPoint4f$9$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 37, 0, ('p', 'LPoint4f$10$unit_z', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 37, 0, ('p', 'LPoint4f$7$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LPoint4f, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LPoint4f, 'init_type', None) )(*args,**kw)

    @classmethod
    def unit_w(cls, *args,**kw):
        return ( cls.c.get('unit_w', None) or cls.c.call(LPoint4f, 'unit_w', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LPoint4f, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LPoint4f, 'unit_y', None) )(*args,**kw)

    @classmethod
    def unit_z(cls, *args,**kw):
        return ( cls.c.get('unit_z', None) or cls.c.call(LPoint4f, 'unit_z', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LPoint4f, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['get_xy'] = [
        ('d', 31, 0, ('p', 'LPoint4f$13$get_xy', 'p'), []),
    ]
    c.ct['get_xyz'] = [
        ('d', 34, 0, ('p', 'LPoint4f$12$get_xyz', 'p'), []),
    ]
    c.ct['normalized'] = [
        ('d', 37, 0, ('p', 'LPoint4f$14$normalized', 'p'), []),
    ]
    c.ct['project'] = [
        ('d', 37, 1, ('p', 'LPoint4f$15$project', 'pp'), ['LVecBase4f const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LPoint4f, attr, self)

LPoint4f.c.link(LPoint4f)



class LPoint4i(LVecBase4i):
    __bases__ = tuple([LVecBase4i])
    c = cxx.cstructs()
    c.register("LPoint4i", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 38, 0, ('p', 'LPoint4i$1$LPoint4i', ''), []),
        ('s', 38, 1, ('p', 'LPoint4i$2$LPoint4i', 'p'), ['LPoint4i const&']),
        ('s', 38, 2, ('p', 'LPoint4i$3$LPoint4i', 'pi'), ['LVecBase3i const&', 'int']),
        ('s', 38, 1, ('p', 'LPoint4i$4$LPoint4i', 'p'), ['LVecBase4i const&']),
        ('s', 38, 1, ('p', 'LPoint4i$5$LPoint4i', 'i'), ['int']),
        ('s', 38, 4, ('p', 'LPoint4i$6$LPoint4i', 'iiii'), ['int', 'int', 'int', 'int']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LPoint4i$14$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LPoint4i$15$init_type', ''), []),
    ]
    c.ct['unit_w'] = [
        ('s', 38, 0, ('p', 'LPoint4i$11$unit_w', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 38, 0, ('p', 'LPoint4i$8$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 38, 0, ('p', 'LPoint4i$9$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 38, 0, ('p', 'LPoint4i$10$unit_z', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 38, 0, ('p', 'LPoint4i$7$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LPoint4i, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LPoint4i, 'init_type', None) )(*args,**kw)

    @classmethod
    def unit_w(cls, *args,**kw):
        return ( cls.c.get('unit_w', None) or cls.c.call(LPoint4i, 'unit_w', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LPoint4i, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LPoint4i, 'unit_y', None) )(*args,**kw)

    @classmethod
    def unit_z(cls, *args,**kw):
        return ( cls.c.get('unit_z', None) or cls.c.call(LPoint4i, 'unit_z', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LPoint4i, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['get_xy'] = [
        ('d', 'p', 0, ('p', 'LPoint4i$13$get_xy', 'p'), []),
    ]
    c.ct['get_xyz'] = [
        ('d', 'p', 0, ('p', 'LPoint4i$12$get_xyz', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LPoint4i, attr, self)

LPoint4i.c.link(LPoint4i)



class LVector2d(LVecBase2d):
    __bases__ = tuple([LVecBase2d])
    c = cxx.cstructs()
    c.register("LVector2d", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 39, 0, ('p', 'LVector2d$1$LVector2d', ''), []),
        ('s', 39, 1, ('p', 'LVector2d$2$LVector2d', 'p'), ['LVecBase2d const&']),
        ('s', 39, 1, ('p', 'LVector2d$3$LVector2d', 'p'), ['LVector2d const&']),
        ('s', 39, 1, ('p', 'LVector2d$4$LVector2d', 'd'), ['double']),
        ('s', 39, 2, ('p', 'LVector2d$5$LVector2d', 'dd'), ['double', 'double']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVector2d$13$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVector2d$14$init_type', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 'p', 0, ('p', 'LVector2d$7$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 'p', 0, ('p', 'LVector2d$8$unit_y', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 'p', 0, ('p', 'LVector2d$6$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LVector2d, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LVector2d, 'init_type', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LVector2d, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LVector2d, 'unit_y', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LVector2d, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['normalized'] = [
        ('d', 'p', 0, ('p', 'LVector2d$9$normalized', 'p'), []),
    ]
    c.ct['project'] = [
        ('d', 'p', 1, ('p', 'LVector2d$10$project', 'pp'), ['LVecBase2d const&']),
    ]
    c.ct['signed_angle_deg'] = [
        ('d', 'd', 1, ('d', 'LVector2d$12$signed_angle_deg', 'pp'), ['LVector2d const&']),
    ]
    c.ct['signed_angle_rad'] = [
        ('d', 'd', 1, ('d', 'LVector2d$11$signed_angle_rad', 'pp'), ['LVector2d const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVector2d, attr, self)

LVector2d.c.link(LVector2d)



class LVector2f(LVecBase2f):
    __bases__ = tuple([LVecBase2f])
    c = cxx.cstructs()
    c.register("LVector2f", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 40, 0, ('p', 'LVector2f$1$LVector2f', ''), []),
        ('s', 40, 1, ('p', 'LVector2f$2$LVector2f', 'p'), ['LVecBase2f const&']),
        ('s', 40, 1, ('p', 'LVector2f$3$LVector2f', 'p'), ['LVector2f const&']),
        ('s', 40, 1, ('p', 'LVector2f$4$LVector2f', 'f'), ['float']),
        ('s', 40, 2, ('p', 'LVector2f$5$LVector2f', 'ff'), ['float', 'float']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVector2f$13$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVector2f$14$init_type', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 40, 0, ('p', 'LVector2f$7$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 40, 0, ('p', 'LVector2f$8$unit_y', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 40, 0, ('p', 'LVector2f$6$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LVector2f, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LVector2f, 'init_type', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LVector2f, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LVector2f, 'unit_y', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LVector2f, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['normalized'] = [
        ('d', 40, 0, ('p', 'LVector2f$9$normalized', 'p'), []),
    ]
    c.ct['project'] = [
        ('d', 40, 1, ('p', 'LVector2f$10$project', 'pp'), ['LVecBase2f const&']),
    ]
    c.ct['signed_angle_deg'] = [
        ('d', 'f', 1, ('f', 'LVector2f$12$signed_angle_deg', 'pp'), ['LVector2f const&']),
    ]
    c.ct['signed_angle_rad'] = [
        ('d', 'f', 1, ('f', 'LVector2f$11$signed_angle_rad', 'pp'), ['LVector2f const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVector2f, attr, self)

LVector2f.c.link(LVector2f)



class LVector2i(LVecBase2i):
    __bases__ = tuple([LVecBase2i])
    c = cxx.cstructs()
    c.register("LVector2i", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 41, 0, ('p', 'LVector2i$1$LVector2i', ''), []),
        ('s', 41, 1, ('p', 'LVector2i$2$LVector2i', 'p'), ['LVecBase2i const&']),
        ('s', 41, 1, ('p', 'LVector2i$3$LVector2i', 'p'), ['LVector2i const&']),
        ('s', 41, 1, ('p', 'LVector2i$4$LVector2i', 'i'), ['int']),
        ('s', 41, 2, ('p', 'LVector2i$5$LVector2i', 'ii'), ['int', 'int']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVector2i$9$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVector2i$10$init_type', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 'p', 0, ('p', 'LVector2i$7$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 'p', 0, ('p', 'LVector2i$8$unit_y', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 'p', 0, ('p', 'LVector2i$6$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LVector2i, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LVector2i, 'init_type', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LVector2i, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LVector2i, 'unit_y', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LVector2i, 'zero', None) )(*args,**kw)

    # instance method type calls



    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVector2i, attr, self)

LVector2i.c.link(LVector2i)



class LVector3d(LVecBase3d):
    __bases__ = tuple([LVecBase3d])
    c = cxx.cstructs()
    c.register("LVector3d", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 42, 0, ('p', 'LVector3d$1$LVector3d', ''), []),
        ('s', 42, 2, ('p', 'LVector3d$2$LVector3d', 'pd'), ['LVecBase2d const&', 'double']),
        ('s', 42, 1, ('p', 'LVector3d$3$LVector3d', 'p'), ['LVecBase3d const&']),
        ('s', 42, 1, ('p', 'LVector3d$4$LVector3d', 'p'), ['LVector3d const&']),
        ('s', 42, 1, ('p', 'LVector3d$5$LVector3d', 'd'), ['double']),
        ('s', 42, 3, ('p', 'LVector3d$6$LVector3d', 'ddd'), ['double', 'double', 'double']),
    ]

    # classmethod type calls

    c.ct['back'] = [
        ('s', 'p', 1, ('p', 'LVector3d$33$back', 'p'), ['CoordinateSystem']),
        ('s', 'p', 0, ('p', 'LVector3d$34$back', ''), []),
    ]
    c.ct['down'] = [
        ('s', 'p', 1, ('p', 'LVector3d$29$down', 'p'), ['CoordinateSystem']),
        ('s', 'p', 0, ('p', 'LVector3d$30$down', ''), []),
    ]
    c.ct['forward'] = [
        ('s', 'p', 1, ('p', 'LVector3d$27$forward', 'p'), ['CoordinateSystem']),
        ('s', 'p', 0, ('p', 'LVector3d$28$forward', ''), []),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVector3d$37$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVector3d$38$init_type', ''), []),
    ]
    c.ct['left'] = [
        ('s', 'p', 1, ('p', 'LVector3d$31$left', 'p'), ['CoordinateSystem']),
        ('s', 'p', 0, ('p', 'LVector3d$32$left', ''), []),
    ]
    c.ct['rfu'] = [
        ('s', 'p', 4, ('p', 'LVector3d$35$rfu', 'dddp'), ['double', 'double', 'double', 'CoordinateSystem']),
        ('s', 'p', 3, ('p', 'LVector3d$36$rfu', 'ddd'), ['double', 'double', 'double']),
    ]
    c.ct['right'] = [
        ('s', 'p', 1, ('p', 'LVector3d$25$right', 'p'), ['CoordinateSystem']),
        ('s', 'p', 0, ('p', 'LVector3d$26$right', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 'p', 0, ('p', 'LVector3d$8$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 'p', 0, ('p', 'LVector3d$9$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 'p', 0, ('p', 'LVector3d$10$unit_z', ''), []),
    ]
    c.ct['up'] = [
        ('s', 'p', 1, ('p', 'LVector3d$23$up', 'p'), ['CoordinateSystem']),
        ('s', 'p', 0, ('p', 'LVector3d$24$up', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 'p', 0, ('p', 'LVector3d$7$zero', ''), []),
    ]

    @classmethod
    def back(cls, *args,**kw):
        return ( cls.c.get('back', None) or cls.c.call(LVector3d, 'back', None) )(*args,**kw)

    @classmethod
    def down(cls, *args,**kw):
        return ( cls.c.get('down', None) or cls.c.call(LVector3d, 'down', None) )(*args,**kw)

    @classmethod
    def forward(cls, *args,**kw):
        return ( cls.c.get('forward', None) or cls.c.call(LVector3d, 'forward', None) )(*args,**kw)

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LVector3d, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LVector3d, 'init_type', None) )(*args,**kw)

    @classmethod
    def left(cls, *args,**kw):
        return ( cls.c.get('left', None) or cls.c.call(LVector3d, 'left', None) )(*args,**kw)

    @classmethod
    def rfu(cls, *args,**kw):
        return ( cls.c.get('rfu', None) or cls.c.call(LVector3d, 'rfu', None) )(*args,**kw)

    @classmethod
    def right(cls, *args,**kw):
        return ( cls.c.get('right', None) or cls.c.call(LVector3d, 'right', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LVector3d, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LVector3d, 'unit_y', None) )(*args,**kw)

    @classmethod
    def unit_z(cls, *args,**kw):
        return ( cls.c.get('unit_z', None) or cls.c.call(LVector3d, 'unit_z', None) )(*args,**kw)

    @classmethod
    def up(cls, *args,**kw):
        return ( cls.c.get('up', None) or cls.c.call(LVector3d, 'up', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LVector3d, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['angle_deg'] = [
        ('d', 'd', 1, ('d', 'LVector3d$18$angle_deg', 'pp'), ['LVector3d const&']),
    ]
    c.ct['angle_rad'] = [
        ('d', 'd', 1, ('d', 'LVector3d$17$angle_rad', 'pp'), ['LVector3d const&']),
    ]
    c.ct['cross'] = [
        ('d', 'p', 1, ('p', 'LVector3d$14$cross', 'pp'), ['LVecBase3d const&']),
    ]
    c.ct['get_xy'] = [
        ('d', 'p', 0, ('p', 'LVector3d$11$get_xy', 'p'), []),
    ]
    c.ct['get_xz'] = [
        ('d', 'p', 0, ('p', 'LVector3d$12$get_xz', 'p'), []),
    ]
    c.ct['get_yz'] = [
        ('d', 'p', 0, ('p', 'LVector3d$13$get_yz', 'p'), []),
    ]
    c.ct['normalized'] = [
        ('d', 'p', 0, ('p', 'LVector3d$15$normalized', 'p'), []),
    ]
    c.ct['project'] = [
        ('d', 'p', 1, ('p', 'LVector3d$16$project', 'pp'), ['LVecBase3d const&']),
    ]
    c.ct['relative_angle_deg'] = [
        ('d', 'd', 1, ('d', 'LVector3d$22$relative_angle_deg', 'pp'), ['LVector3d const&']),
    ]
    c.ct['relative_angle_rad'] = [
        ('d', 'd', 1, ('d', 'LVector3d$21$relative_angle_rad', 'pp'), ['LVector3d const&']),
    ]
    c.ct['signed_angle_deg'] = [
        ('d', 'd', 2, ('d', 'LVector3d$20$signed_angle_deg', 'ppp'), ['LVector3d const&', 'LVector3d const&']),
    ]
    c.ct['signed_angle_rad'] = [
        ('d', 'd', 2, ('d', 'LVector3d$19$signed_angle_rad', 'ppp'), ['LVector3d const&', 'LVector3d const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVector3d, attr, self)

LVector3d.c.link(LVector3d)



class LVector3f(LVecBase3f):
    __bases__ = tuple([LVecBase3f])
    c = cxx.cstructs()
    c.register("LVector3f", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 43, 0, ('p', 'LVector3f$1$LVector3f', ''), []),
        ('s', 43, 2, ('p', 'LVector3f$2$LVector3f', 'pf'), ['LVecBase2f const&', 'float']),
        ('s', 43, 1, ('p', 'LVector3f$3$LVector3f', 'p'), ['LVecBase3f const&']),
        ('s', 43, 1, ('p', 'LVector3f$4$LVector3f', 'p'), ['LVector3f const&']),
        ('s', 43, 1, ('p', 'LVector3f$5$LVector3f', 'f'), ['float']),
        ('s', 43, 3, ('p', 'LVector3f$6$LVector3f', 'fff'), ['float', 'float', 'float']),
    ]

    # classmethod type calls

    c.ct['back'] = [
        ('s', 43, 1, ('p', 'LVector3f$33$back', 'p'), ['CoordinateSystem']),
        ('s', 43, 0, ('p', 'LVector3f$34$back', ''), []),
    ]
    c.ct['down'] = [
        ('s', 43, 1, ('p', 'LVector3f$29$down', 'p'), ['CoordinateSystem']),
        ('s', 43, 0, ('p', 'LVector3f$30$down', ''), []),
    ]
    c.ct['forward'] = [
        ('s', 43, 1, ('p', 'LVector3f$27$forward', 'p'), ['CoordinateSystem']),
        ('s', 43, 0, ('p', 'LVector3f$28$forward', ''), []),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVector3f$37$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVector3f$38$init_type', ''), []),
    ]
    c.ct['left'] = [
        ('s', 43, 1, ('p', 'LVector3f$31$left', 'p'), ['CoordinateSystem']),
        ('s', 43, 0, ('p', 'LVector3f$32$left', ''), []),
    ]
    c.ct['rfu'] = [
        ('s', 43, 4, ('p', 'LVector3f$35$rfu', 'fffp'), ['float', 'float', 'float', 'CoordinateSystem']),
        ('s', 43, 3, ('p', 'LVector3f$36$rfu', 'fff'), ['float', 'float', 'float']),
    ]
    c.ct['right'] = [
        ('s', 43, 1, ('p', 'LVector3f$25$right', 'p'), ['CoordinateSystem']),
        ('s', 43, 0, ('p', 'LVector3f$26$right', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 43, 0, ('p', 'LVector3f$8$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 43, 0, ('p', 'LVector3f$9$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 43, 0, ('p', 'LVector3f$10$unit_z', ''), []),
    ]
    c.ct['up'] = [
        ('s', 43, 1, ('p', 'LVector3f$23$up', 'p'), ['CoordinateSystem']),
        ('s', 43, 0, ('p', 'LVector3f$24$up', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 43, 0, ('p', 'LVector3f$7$zero', ''), []),
    ]

    @classmethod
    def back(cls, *args,**kw):
        return ( cls.c.get('back', None) or cls.c.call(LVector3f, 'back', None) )(*args,**kw)

    @classmethod
    def down(cls, *args,**kw):
        return ( cls.c.get('down', None) or cls.c.call(LVector3f, 'down', None) )(*args,**kw)

    @classmethod
    def forward(cls, *args,**kw):
        return ( cls.c.get('forward', None) or cls.c.call(LVector3f, 'forward', None) )(*args,**kw)

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LVector3f, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LVector3f, 'init_type', None) )(*args,**kw)

    @classmethod
    def left(cls, *args,**kw):
        return ( cls.c.get('left', None) or cls.c.call(LVector3f, 'left', None) )(*args,**kw)

    @classmethod
    def rfu(cls, *args,**kw):
        return ( cls.c.get('rfu', None) or cls.c.call(LVector3f, 'rfu', None) )(*args,**kw)

    @classmethod
    def right(cls, *args,**kw):
        return ( cls.c.get('right', None) or cls.c.call(LVector3f, 'right', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LVector3f, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LVector3f, 'unit_y', None) )(*args,**kw)

    @classmethod
    def unit_z(cls, *args,**kw):
        return ( cls.c.get('unit_z', None) or cls.c.call(LVector3f, 'unit_z', None) )(*args,**kw)

    @classmethod
    def up(cls, *args,**kw):
        return ( cls.c.get('up', None) or cls.c.call(LVector3f, 'up', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LVector3f, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['angle_deg'] = [
        ('d', 'f', 1, ('f', 'LVector3f$18$angle_deg', 'pp'), ['LVector3f const&']),
    ]
    c.ct['angle_rad'] = [
        ('d', 'f', 1, ('f', 'LVector3f$17$angle_rad', 'pp'), ['LVector3f const&']),
    ]
    c.ct['cross'] = [
        ('d', 43, 1, ('p', 'LVector3f$14$cross', 'pp'), ['LVecBase3f const&']),
    ]
    c.ct['get_xy'] = [
        ('d', 40, 0, ('p', 'LVector3f$11$get_xy', 'p'), []),
    ]
    c.ct['get_xz'] = [
        ('d', 40, 0, ('p', 'LVector3f$12$get_xz', 'p'), []),
    ]
    c.ct['get_yz'] = [
        ('d', 40, 0, ('p', 'LVector3f$13$get_yz', 'p'), []),
    ]
    c.ct['normalized'] = [
        ('d', 43, 0, ('p', 'LVector3f$15$normalized', 'p'), []),
    ]
    c.ct['project'] = [
        ('d', 43, 1, ('p', 'LVector3f$16$project', 'pp'), ['LVecBase3f const&']),
    ]
    c.ct['relative_angle_deg'] = [
        ('d', 'f', 1, ('f', 'LVector3f$22$relative_angle_deg', 'pp'), ['LVector3f const&']),
    ]
    c.ct['relative_angle_rad'] = [
        ('d', 'f', 1, ('f', 'LVector3f$21$relative_angle_rad', 'pp'), ['LVector3f const&']),
    ]
    c.ct['signed_angle_deg'] = [
        ('d', 'f', 2, ('f', 'LVector3f$20$signed_angle_deg', 'ppp'), ['LVector3f const&', 'LVector3f const&']),
    ]
    c.ct['signed_angle_rad'] = [
        ('d', 'f', 2, ('f', 'LVector3f$19$signed_angle_rad', 'ppp'), ['LVector3f const&', 'LVector3f const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVector3f, attr, self)

LVector3f.c.link(LVector3f)



class LVector3i(LVecBase3i):
    __bases__ = tuple([LVecBase3i])
    c = cxx.cstructs()
    c.register("LVector3i", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 44, 0, ('p', 'LVector3i$1$LVector3i', ''), []),
        ('s', 44, 2, ('p', 'LVector3i$2$LVector3i', 'pi'), ['LVecBase2i const&', 'int']),
        ('s', 44, 1, ('p', 'LVector3i$3$LVector3i', 'p'), ['LVecBase3i const&']),
        ('s', 44, 1, ('p', 'LVector3i$4$LVector3i', 'p'), ['LVector3i const&']),
        ('s', 44, 1, ('p', 'LVector3i$5$LVector3i', 'i'), ['int']),
        ('s', 44, 3, ('p', 'LVector3i$6$LVector3i', 'iii'), ['int', 'int', 'int']),
    ]

    # classmethod type calls

    c.ct['back'] = [
        ('s', 'p', 1, ('p', 'LVector3i$25$back', 'p'), ['CoordinateSystem']),
        ('s', 'p', 0, ('p', 'LVector3i$26$back', ''), []),
    ]
    c.ct['down'] = [
        ('s', 'p', 1, ('p', 'LVector3i$21$down', 'p'), ['CoordinateSystem']),
        ('s', 'p', 0, ('p', 'LVector3i$22$down', ''), []),
    ]
    c.ct['forward'] = [
        ('s', 'p', 1, ('p', 'LVector3i$19$forward', 'p'), ['CoordinateSystem']),
        ('s', 'p', 0, ('p', 'LVector3i$20$forward', ''), []),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVector3i$29$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVector3i$30$init_type', ''), []),
    ]
    c.ct['left'] = [
        ('s', 'p', 1, ('p', 'LVector3i$23$left', 'p'), ['CoordinateSystem']),
        ('s', 'p', 0, ('p', 'LVector3i$24$left', ''), []),
    ]
    c.ct['rfu'] = [
        ('s', 'p', 4, ('p', 'LVector3i$27$rfu', 'iiip'), ['int', 'int', 'int', 'CoordinateSystem']),
        ('s', 'p', 3, ('p', 'LVector3i$28$rfu', 'iii'), ['int', 'int', 'int']),
    ]
    c.ct['right'] = [
        ('s', 'p', 1, ('p', 'LVector3i$17$right', 'p'), ['CoordinateSystem']),
        ('s', 'p', 0, ('p', 'LVector3i$18$right', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 'p', 0, ('p', 'LVector3i$8$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 'p', 0, ('p', 'LVector3i$9$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 'p', 0, ('p', 'LVector3i$10$unit_z', ''), []),
    ]
    c.ct['up'] = [
        ('s', 'p', 1, ('p', 'LVector3i$15$up', 'p'), ['CoordinateSystem']),
        ('s', 'p', 0, ('p', 'LVector3i$16$up', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 'p', 0, ('p', 'LVector3i$7$zero', ''), []),
    ]

    @classmethod
    def back(cls, *args,**kw):
        return ( cls.c.get('back', None) or cls.c.call(LVector3i, 'back', None) )(*args,**kw)

    @classmethod
    def down(cls, *args,**kw):
        return ( cls.c.get('down', None) or cls.c.call(LVector3i, 'down', None) )(*args,**kw)

    @classmethod
    def forward(cls, *args,**kw):
        return ( cls.c.get('forward', None) or cls.c.call(LVector3i, 'forward', None) )(*args,**kw)

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LVector3i, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LVector3i, 'init_type', None) )(*args,**kw)

    @classmethod
    def left(cls, *args,**kw):
        return ( cls.c.get('left', None) or cls.c.call(LVector3i, 'left', None) )(*args,**kw)

    @classmethod
    def rfu(cls, *args,**kw):
        return ( cls.c.get('rfu', None) or cls.c.call(LVector3i, 'rfu', None) )(*args,**kw)

    @classmethod
    def right(cls, *args,**kw):
        return ( cls.c.get('right', None) or cls.c.call(LVector3i, 'right', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LVector3i, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LVector3i, 'unit_y', None) )(*args,**kw)

    @classmethod
    def unit_z(cls, *args,**kw):
        return ( cls.c.get('unit_z', None) or cls.c.call(LVector3i, 'unit_z', None) )(*args,**kw)

    @classmethod
    def up(cls, *args,**kw):
        return ( cls.c.get('up', None) or cls.c.call(LVector3i, 'up', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LVector3i, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['cross'] = [
        ('d', 'p', 1, ('p', 'LVector3i$14$cross', 'pp'), ['LVecBase3i const&']),
    ]
    c.ct['get_xy'] = [
        ('d', 'p', 0, ('p', 'LVector3i$11$get_xy', 'p'), []),
    ]
    c.ct['get_xz'] = [
        ('d', 'p', 0, ('p', 'LVector3i$12$get_xz', 'p'), []),
    ]
    c.ct['get_yz'] = [
        ('d', 'p', 0, ('p', 'LVector3i$13$get_yz', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVector3i, attr, self)

LVector3i.c.link(LVector3i)



class LVector4d(LVecBase4d):
    __bases__ = tuple([LVecBase4d])
    c = cxx.cstructs()
    c.register("LVector4d", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 45, 0, ('p', 'LVector4d$1$LVector4d', ''), []),
        ('s', 45, 2, ('p', 'LVector4d$2$LVector4d', 'pd'), ['LVecBase3d const&', 'double']),
        ('s', 45, 1, ('p', 'LVector4d$3$LVector4d', 'p'), ['LVecBase4d const&']),
        ('s', 45, 1, ('p', 'LVector4d$4$LVector4d', 'p'), ['LVector4d const&']),
        ('s', 45, 1, ('p', 'LVector4d$5$LVector4d', 'd'), ['double']),
        ('s', 45, 4, ('p', 'LVector4d$6$LVector4d', 'dddd'), ['double', 'double', 'double', 'double']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVector4d$16$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVector4d$17$init_type', ''), []),
    ]
    c.ct['unit_w'] = [
        ('s', 'p', 0, ('p', 'LVector4d$11$unit_w', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 'p', 0, ('p', 'LVector4d$8$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 'p', 0, ('p', 'LVector4d$9$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 'p', 0, ('p', 'LVector4d$10$unit_z', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 'p', 0, ('p', 'LVector4d$7$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LVector4d, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LVector4d, 'init_type', None) )(*args,**kw)

    @classmethod
    def unit_w(cls, *args,**kw):
        return ( cls.c.get('unit_w', None) or cls.c.call(LVector4d, 'unit_w', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LVector4d, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LVector4d, 'unit_y', None) )(*args,**kw)

    @classmethod
    def unit_z(cls, *args,**kw):
        return ( cls.c.get('unit_z', None) or cls.c.call(LVector4d, 'unit_z', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LVector4d, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['get_xy'] = [
        ('d', 'p', 0, ('p', 'LVector4d$13$get_xy', 'p'), []),
    ]
    c.ct['get_xyz'] = [
        ('d', 'p', 0, ('p', 'LVector4d$12$get_xyz', 'p'), []),
    ]
    c.ct['normalized'] = [
        ('d', 'p', 0, ('p', 'LVector4d$14$normalized', 'p'), []),
    ]
    c.ct['project'] = [
        ('d', 'p', 1, ('p', 'LVector4d$15$project', 'pp'), ['LVecBase4d const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVector4d, attr, self)

LVector4d.c.link(LVector4d)



class LVector4f(LVecBase4f):
    __bases__ = tuple([LVecBase4f])
    c = cxx.cstructs()
    c.register("LVector4f", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 46, 0, ('p', 'LVector4f$1$LVector4f', ''), []),
        ('s', 46, 2, ('p', 'LVector4f$2$LVector4f', 'pf'), ['LVecBase3f const&', 'float']),
        ('s', 46, 1, ('p', 'LVector4f$3$LVector4f', 'p'), ['LVecBase4f const&']),
        ('s', 46, 1, ('p', 'LVector4f$4$LVector4f', 'p'), ['LVector4f const&']),
        ('s', 46, 1, ('p', 'LVector4f$5$LVector4f', 'f'), ['float']),
        ('s', 46, 4, ('p', 'LVector4f$6$LVector4f', 'ffff'), ['float', 'float', 'float', 'float']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVector4f$16$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVector4f$17$init_type', ''), []),
    ]
    c.ct['unit_w'] = [
        ('s', 46, 0, ('p', 'LVector4f$11$unit_w', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 46, 0, ('p', 'LVector4f$8$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 46, 0, ('p', 'LVector4f$9$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 46, 0, ('p', 'LVector4f$10$unit_z', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 46, 0, ('p', 'LVector4f$7$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LVector4f, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LVector4f, 'init_type', None) )(*args,**kw)

    @classmethod
    def unit_w(cls, *args,**kw):
        return ( cls.c.get('unit_w', None) or cls.c.call(LVector4f, 'unit_w', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LVector4f, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LVector4f, 'unit_y', None) )(*args,**kw)

    @classmethod
    def unit_z(cls, *args,**kw):
        return ( cls.c.get('unit_z', None) or cls.c.call(LVector4f, 'unit_z', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LVector4f, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['get_xy'] = [
        ('d', 40, 0, ('p', 'LVector4f$13$get_xy', 'p'), []),
    ]
    c.ct['get_xyz'] = [
        ('d', 43, 0, ('p', 'LVector4f$12$get_xyz', 'p'), []),
    ]
    c.ct['normalized'] = [
        ('d', 46, 0, ('p', 'LVector4f$14$normalized', 'p'), []),
    ]
    c.ct['project'] = [
        ('d', 46, 1, ('p', 'LVector4f$15$project', 'pp'), ['LVecBase4f const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVector4f, attr, self)

LVector4f.c.link(LVector4f)



class LVector4i(LVecBase4i):
    __bases__ = tuple([LVecBase4i])
    c = cxx.cstructs()
    c.register("LVector4i", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 47, 0, ('p', 'LVector4i$1$LVector4i', ''), []),
        ('s', 47, 2, ('p', 'LVector4i$2$LVector4i', 'pi'), ['LVecBase3i const&', 'int']),
        ('s', 47, 1, ('p', 'LVector4i$3$LVector4i', 'p'), ['LVecBase4i const&']),
        ('s', 47, 1, ('p', 'LVector4i$4$LVector4i', 'p'), ['LVector4i const&']),
        ('s', 47, 1, ('p', 'LVector4i$5$LVector4i', 'i'), ['int']),
        ('s', 47, 4, ('p', 'LVector4i$6$LVector4i', 'iiii'), ['int', 'int', 'int', 'int']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'LVector4i$14$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'LVector4i$15$init_type', ''), []),
    ]
    c.ct['unit_w'] = [
        ('s', 'p', 0, ('p', 'LVector4i$11$unit_w', ''), []),
    ]
    c.ct['unit_x'] = [
        ('s', 'p', 0, ('p', 'LVector4i$8$unit_x', ''), []),
    ]
    c.ct['unit_y'] = [
        ('s', 'p', 0, ('p', 'LVector4i$9$unit_y', ''), []),
    ]
    c.ct['unit_z'] = [
        ('s', 'p', 0, ('p', 'LVector4i$10$unit_z', ''), []),
    ]
    c.ct['zero'] = [
        ('s', 'p', 0, ('p', 'LVector4i$7$zero', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(LVector4i, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(LVector4i, 'init_type', None) )(*args,**kw)

    @classmethod
    def unit_w(cls, *args,**kw):
        return ( cls.c.get('unit_w', None) or cls.c.call(LVector4i, 'unit_w', None) )(*args,**kw)

    @classmethod
    def unit_x(cls, *args,**kw):
        return ( cls.c.get('unit_x', None) or cls.c.call(LVector4i, 'unit_x', None) )(*args,**kw)

    @classmethod
    def unit_y(cls, *args,**kw):
        return ( cls.c.get('unit_y', None) or cls.c.call(LVector4i, 'unit_y', None) )(*args,**kw)

    @classmethod
    def unit_z(cls, *args,**kw):
        return ( cls.c.get('unit_z', None) or cls.c.call(LVector4i, 'unit_z', None) )(*args,**kw)

    @classmethod
    def zero(cls, *args,**kw):
        return ( cls.c.get('zero', None) or cls.c.call(LVector4i, 'zero', None) )(*args,**kw)

    # instance method type calls

    c.ct['get_xy'] = [
        ('d', 'p', 0, ('p', 'LVector4i$13$get_xy', 'p'), []),
    ]
    c.ct['get_xyz'] = [
        ('d', 'p', 0, ('p', 'LVector4i$12$get_xyz', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(LVector4i, attr, self)

LVector4i.c.link(LVector4i)



class Namable(MemoryBase):
    __bases__ = tuple([MemoryBase])
    c = cxx.cstructs()
    c.register("Namable", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_Loader'] = [
        ('d', 60, 0, ('p', 'Namable$2$downcast_to_Loader', 'p'), []),
    ]
    c.ct['downcast_to_PandaNode'] = [
        ('d', 86, 0, ('p', 'Namable$1$downcast_to_PandaNode', 'p'), []),
    ]
    c.ct['downcast_to_TextFont'] = [
        ('d', 59, 0, ('p', 'Namable$3$downcast_to_TextFont', 'p'), []),
    ]
    c.ct['downcast_to_Texture'] = [
        ('d', 64, 0, ('p', 'Namable$4$downcast_to_Texture', 'p'), []),
    ]
    c.ct['downcast_to_Thread'] = [
        ('d', 58, 0, ('p', 'Namable$5$downcast_to_Thread', 'p'), []),
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

    c.ct['downcast_to_GeomVertexArrayDataHandle'] = [
        ('d', 56, 0, ('p', 'ReferenceCount$15$downcast_to_GeomVertexArrayDataHandle', 'p'), []),
    ]
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
        ('d', 16, 0, ('p', 'ReferenceCount$1$upcast_to_MemoryBase', 'p'), []),
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



class GraphicsEngine(ReferenceCount):
    __bases__ = tuple([ReferenceCount])
    c = cxx.cstructs()
    c.register("GraphicsEngine", "upanda3d", """libupanda3d_c.so""")

    # enum ThreadState

    TS_do_compute = const(5)
    TS_do_extract = const(6)
    TS_do_flip = const(2)
    TS_do_frame = const(1)
    TS_do_release = const(3)
    TS_do_screenshot = const(7)
    TS_do_windows = const(4)
    TS_done = const(9)
    TS_terminate = const(8)
    TS_wait = const(0)


    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 50, 1, ('p', 'GraphicsEngine$1$GraphicsEngine', 'p'), ['Pipeline*']),
        ('s', 50, 0, ('p', 'GraphicsEngine$2$GraphicsEngine', ''), []),
    ]

    # classmethod type calls

    c.ct['do_cull'] = [
        ('s', 'v', 4, ('v', 'GraphicsEngine$35$do_cull', 'pppp'), ['CullHandler*', 'SceneSetup*', 'GraphicsStateGuardian*', 'Thread*']),
    ]
    c.ct['get_global_ptr'] = [
        ('s', 50, 0, ('p', 'GraphicsEngine$32$get_global_ptr', ''), []),
    ]

    @classmethod
    def do_cull(cls, *args,**kw):
        return ( cls.c.get('do_cull', None) or cls.c.call(GraphicsEngine, 'do_cull', None) )(*args,**kw)

    @classmethod
    def get_global_ptr(cls, *args,**kw):
        return ( cls.c.get('get_global_ptr', None) or cls.c.call(GraphicsEngine, 'get_global_ptr', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_window'] = [
        ('d', 'B', 2, ('B', 'GraphicsEngine$18$add_window', 'ppi'), ['GraphicsOutput*', 'int']),
    ]
    c.ct['dispatch_compute'] = [
        ('d', 'v', 3, ('v', 'GraphicsEngine$31$dispatch_compute', 'pppp'), ['LVecBase3i const&', 'ShaderAttrib const*', 'GraphicsStateGuardian*']),
    ]
    c.ct['do_get_screenshot'] = [
        ('d', 64, 2, ('p', 'GraphicsEngine$34$do_get_screenshot', 'ppp'), ['DisplayRegion*', 'GraphicsStateGuardian*']),
    ]
    c.ct['extract_texture_data'] = [
        ('d', 'B', 2, ('B', 'GraphicsEngine$30$extract_texture_data', 'ppp'), ['Texture*', 'GraphicsStateGuardian*']),
    ]
    c.ct['flip_frame'] = [
        ('d', 'v', 0, ('v', 'GraphicsEngine$29$flip_frame', 'p'), []),
    ]
    c.ct['get_auto_flip'] = [
        ('d', 'B', 0, ('B', 'GraphicsEngine$7$get_auto_flip', 'p'), []),
    ]
    c.ct['get_default_loader'] = [
        ('d', 60, 0, ('p', 'GraphicsEngine$11$get_default_loader', 'p'), []),
    ]
    c.ct['get_num_windows'] = [
        ('d', 'i', 0, ('i', 'GraphicsEngine$23$get_num_windows', 'p'), []),
    ]
    c.ct['get_portal_cull'] = [
        ('d', 'B', 0, ('B', 'GraphicsEngine$9$get_portal_cull', 'p'), []),
    ]
    c.ct['get_render_lock'] = [
        ('d', 'p', 0, ('p', 'GraphicsEngine$5$get_render_lock', 'p'), []),
    ]
    c.ct['get_threading_model'] = [
        ('d', 'p', 0, ('p', 'GraphicsEngine$4$get_threading_model', 'p'), []),
    ]
    c.ct['get_window'] = [
        ('d', 74, 1, ('p', 'GraphicsEngine$24$get_window', 'pi'), ['int']),
    ]
    c.ct['is_empty'] = [
        ('d', 'B', 0, ('B', 'GraphicsEngine$22$is_empty', 'p'), []),
    ]
    c.ct['make_buffer'] = [
        ('d', 74, 5, ('p', 'GraphicsEngine$15$make_buffer', 'ppsiii'), ['GraphicsOutput*', 'std::string const&', 'int', 'int', 'int']),
        ('d', 74, 5, ('p', 'GraphicsEngine$16$make_buffer', 'ppsiii'), ['GraphicsStateGuardian*', 'std::string const&', 'int', 'int', 'int']),
    ]
    c.ct['make_output'] = [
        ('d', 74, 8, ('p', 'GraphicsEngine$12$make_output', 'ppsippipp'), ['GraphicsPipe*', 'std::string const&', 'int', 'FrameBufferProperties const&', 'WindowProperties const&', 'int', 'GraphicsStateGuardian*', 'GraphicsOutput*']),
        ('d', 74, 7, ('p', 'GraphicsEngine$13$make_output', 'ppsippip'), ['GraphicsPipe*', 'std::string const&', 'int', 'FrameBufferProperties const&', 'WindowProperties const&', 'int', 'GraphicsStateGuardian*']),
        ('d', 74, 6, ('p', 'GraphicsEngine$14$make_output', 'ppsippi'), ['GraphicsPipe*', 'std::string const&', 'int', 'FrameBufferProperties const&', 'WindowProperties const&', 'int']),
    ]
    c.ct['make_parasite'] = [
        ('d', 74, 5, ('p', 'GraphicsEngine$17$make_parasite', 'ppsiii'), ['GraphicsOutput*', 'std::string const&', 'int', 'int', 'int']),
    ]
    c.ct['open_windows'] = [
        ('d', 'v', 0, ('v', 'GraphicsEngine$26$open_windows', 'p'), []),
    ]
    c.ct['ready_flip'] = [
        ('d', 'v', 0, ('v', 'GraphicsEngine$28$ready_flip', 'p'), []),
    ]
    c.ct['remove_all_windows'] = [
        ('d', 'v', 0, ('v', 'GraphicsEngine$20$remove_all_windows', 'p'), []),
    ]
    c.ct['remove_window'] = [
        ('d', 'B', 1, ('B', 'GraphicsEngine$19$remove_window', 'pp'), ['GraphicsOutput*']),
    ]
    c.ct['render_frame'] = [
        ('d', 'v', 0, ('v', 'GraphicsEngine$25$render_frame', 'p'), []),
    ]
    c.ct['reset_all_windows'] = [
        ('d', 'v', 1, ('v', 'GraphicsEngine$21$reset_all_windows', 'pB'), ['bool']),
    ]
    c.ct['set_auto_flip'] = [
        ('d', 'v', 1, ('v', 'GraphicsEngine$6$set_auto_flip', 'pB'), ['bool']),
    ]
    c.ct['set_default_loader'] = [
        ('d', 'v', 1, ('v', 'GraphicsEngine$10$set_default_loader', 'pp'), ['Loader*']),
    ]
    c.ct['set_portal_cull'] = [
        ('d', 'v', 1, ('v', 'GraphicsEngine$8$set_portal_cull', 'pB'), ['bool']),
    ]
    c.ct['set_threading_model'] = [
        ('d', 'v', 1, ('v', 'GraphicsEngine$3$set_threading_model', 'pp'), ['GraphicsThreadingModel const&']),
    ]
    c.ct['sync_frame'] = [
        ('d', 'v', 0, ('v', 'GraphicsEngine$27$sync_frame', 'p'), []),
    ]
    c.ct['texture_uploaded'] = [
        ('d', 'v', 1, ('v', 'GraphicsEngine$33$texture_uploaded', 'pp'), ['Texture*']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GraphicsEngine, attr, self)

GraphicsEngine.c.link(GraphicsEngine)



class SimpleLruPage(LinkedListNode):
    __bases__ = tuple([LinkedListNode])
    c = cxx.cstructs()
    c.register("SimpleLruPage", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_GeomVertexArrayData'] = [
        ('d', 85, 0, ('p', 'SimpleLruPage$1$downcast_to_GeomVertexArrayData', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(SimpleLruPage, attr, self)

SimpleLruPage.c.link(SimpleLruPage)



class TexturePeeker(ReferenceCount):
    __bases__ = tuple([ReferenceCount])
    c = cxx.cstructs()
    c.register("TexturePeeker", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 52, 1, ('p', 'TexturePeeker$12$TexturePeeker', 'p'), ['TexturePeeker const&']),
    ]

    # classmethod type calls


    # instance method type calls

    c.ct['fetch_pixel'] = [
        ('d', 'v', 3, ('v', 'TexturePeeker$8$fetch_pixel', 'ppii'), ['LColor&', 'int', 'int']),
    ]
    c.ct['filter_rect'] = [
        ('d', 'v', 5, ('v', 'TexturePeeker$10$filter_rect', 'ppffff'), ['LColor&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 7, ('v', 'TexturePeeker$11$filter_rect', 'ppffffff'), ['LColor&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['get_x_size'] = [
        ('d', 'i', 0, ('i', 'TexturePeeker$2$get_x_size', 'p'), []),
    ]
    c.ct['get_y_size'] = [
        ('d', 'i', 0, ('i', 'TexturePeeker$3$get_y_size', 'p'), []),
    ]
    c.ct['get_z_size'] = [
        ('d', 'i', 0, ('i', 'TexturePeeker$4$get_z_size', 'p'), []),
    ]
    c.ct['has_pixel'] = [
        ('d', 'B', 2, ('B', 'TexturePeeker$5$has_pixel', 'pii'), ['int', 'int']),
    ]
    c.ct['is_valid'] = [
        ('d', 'B', 0, ('B', 'TexturePeeker$1$is_valid', 'p'), []),
    ]
    c.ct['lookup'] = [
        ('d', 'v', 3, ('v', 'TexturePeeker$6$lookup', 'ppff'), ['LColor&', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 4, ('v', 'TexturePeeker$7$lookup', 'ppfff'), ['LColor&', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['lookup_bilinear'] = [
        ('d', 'B', 3, ('B', 'TexturePeeker$9$lookup_bilinear', 'ppff'), ['LColor&', 'PN_stdfloat', 'PN_stdfloat']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TexturePeeker, attr, self)

TexturePeeker.c.link(TexturePeeker)



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
        ('d', 53, 0, ('p', 'TypedObject$8$as_typed_object', 'p'), []),
        ('d', 53, 0, ('p', 'TypedObject$9$as_typed_object', 'p'), []),
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
        ('d', 16, 0, ('p', 'TypedObject$1$upcast_to_MemoryBase', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TypedObject, attr, self)

TypedObject.c.link(TypedObject)



class EventHandler(TypedObject):
    __bases__ = tuple([TypedObject])
    c = cxx.cstructs()
    c.register("EventHandler", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 54, 1, ('p', 'EventHandler$1$EventHandler', 'p'), ['EventQueue*']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'EventHandler$11$get_class_type', ''), []),
    ]
    c.ct['get_global_event_handler'] = [
        ('s', 54, 1, ('p', 'EventHandler$6$get_global_event_handler', 'p'), ['EventQueue*']),
        ('s', 54, 0, ('p', 'EventHandler$7$get_global_event_handler', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'EventHandler$12$init_type', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(EventHandler, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_global_event_handler(cls, *args,**kw):
        return ( cls.c.get('get_global_event_handler', None) or cls.c.call(EventHandler, 'get_global_event_handler', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(EventHandler, 'init_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['dispatch_event'] = [
        ('d', 'v', 1, ('v', 'EventHandler$4$dispatch_event', 'pp'), ['Event const*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'EventHandler$13$force_init_type', 'p'), []),
    ]
    c.ct['get_future'] = [
        ('d', 'p', 1, ('p', 'EventHandler$2$get_future', 'ps'), ['std::string const&']),
    ]
    c.ct['has_hook'] = [
        ('d', 'B', 1, ('B', 'EventHandler$8$has_hook', 'ps'), ['std::string const&']),
    ]
    c.ct['process_events'] = [
        ('d', 'v', 0, ('v', 'EventHandler$3$process_events', 'p'), []),
    ]
    c.ct['remove_all_hooks'] = [
        ('d', 'v', 0, ('v', 'EventHandler$10$remove_all_hooks', 'p'), []),
    ]
    c.ct['remove_hooks'] = [
        ('d', 'B', 1, ('B', 'EventHandler$9$remove_hooks', 'ps'), ['std::string const&']),
    ]
    c.ct['write'] = [
        ('d', 'v', 1, ('v', 'EventHandler$5$write', 'pp'), ['std::ostream&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(EventHandler, attr, self)

EventHandler.c.link(EventHandler)



class TypedWritable(TypedObject):
    __bases__ = tuple([TypedObject])
    c = cxx.cstructs()
    c.register("TypedWritable", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 55, 0, ('p', 'TypedWritable$1$TypedWritable', ''), []),
        ('s', 55, 1, ('p', 'TypedWritable$2$TypedWritable', 'p'), ['TypedWritable const&']),
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
        ('d', 49, 0, ('p', 'TypedWritable$8$as_reference_count', 'p'), []),
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
        ('d', 26, 0, ('p', 'TypedWritable$10$get_bam_modified', 'p'), []),
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



class GeomVertexArrayDataHandle(ReferenceCount, GeomEnums):
    __bases__ = tuple([ReferenceCount, GeomEnums])
    c = cxx.cstructs()
    c.register("GeomVertexArrayDataHandle", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'GeomVertexArrayDataHandle$26$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'GeomVertexArrayDataHandle$27$init_type', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(GeomVertexArrayDataHandle, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(GeomVertexArrayDataHandle, 'init_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['clear_rows'] = [
        ('d', 'v', 0, ('v', 'GeomVertexArrayDataHandle$14$clear_rows', 'p'), []),
    ]
    c.ct['copy_data_from'] = [
        ('d', 'v', 1, ('v', 'GeomVertexArrayDataHandle$19$copy_data_from', 'pp'), ['GeomVertexArrayDataHandle const*']),
    ]
    c.ct['copy_subdata_from'] = [
        ('d', 'v', 5, ('v', 'GeomVertexArrayDataHandle$20$copy_subdata_from', 'pllpll'), ['std::size_t', 'std::size_t', 'GeomVertexArrayDataHandle const*', 'std::size_t', 'std::size_t']),
    ]
    c.ct['get_array_format'] = [
        ('d', 66, 0, ('p', 'GeomVertexArrayDataHandle$8$get_array_format', 'p'), []),
    ]
    c.ct['get_current_thread'] = [
        ('d', 58, 0, ('p', 'GeomVertexArrayDataHandle$3$get_current_thread', 'p'), []),
    ]
    c.ct['get_data'] = [
        ('d', 'p', 0, ('p', 'GeomVertexArrayDataHandle$21$get_data', 'p'), []),
    ]
    c.ct['get_data_size_bytes'] = [
        ('d', 'l', 0, ('l', 'GeomVertexArrayDataHandle$15$get_data_size_bytes', 'p'), []),
    ]
    c.ct['get_modified'] = [
        ('d', 26, 0, ('p', 'GeomVertexArrayDataHandle$16$get_modified', 'p'), []),
    ]
    c.ct['get_num_rows'] = [
        ('d', 'i', 0, ('i', 'GeomVertexArrayDataHandle$10$get_num_rows', 'p'), []),
    ]
    c.ct['get_object'] = [
        ('d', 85, 0, ('p', 'GeomVertexArrayDataHandle$6$get_object', 'p'), []),
        ('d', 85, 0, ('p', 'GeomVertexArrayDataHandle$7$get_object', 'p'), []),
    ]
    c.ct['get_read_pointer'] = [
        ('d', 'v', 1, ('v', 'GeomVertexArrayDataHandle$4$get_read_pointer', 'pB'), ['bool']),
    ]
    c.ct['get_subdata'] = [
        ('d', 'p', 2, ('p', 'GeomVertexArrayDataHandle$23$get_subdata', 'pll'), ['std::size_t', 'std::size_t']),
    ]
    c.ct['get_usage_hint'] = [
        ('d', 'p', 0, ('p', 'GeomVertexArrayDataHandle$9$get_usage_hint', 'p'), []),
    ]
    c.ct['get_write_pointer'] = [
        ('d', 'v', 0, ('v', 'GeomVertexArrayDataHandle$5$get_write_pointer', 'p'), []),
    ]
    c.ct['mark_used'] = [
        ('d', 'v', 0, ('v', 'GeomVertexArrayDataHandle$25$mark_used', 'p'), []),
    ]
    c.ct['prepare_now'] = [
        ('d', 'p', 2, ('p', 'GeomVertexArrayDataHandle$18$prepare_now', 'ppp'), ['PreparedGraphicsObjects*', 'GraphicsStateGuardianBase*']),
    ]
    c.ct['request_resident'] = [
        ('d', 'B', 0, ('B', 'GeomVertexArrayDataHandle$17$request_resident', 'p'), []),
    ]
    c.ct['reserve_num_rows'] = [
        ('d', 'B', 1, ('B', 'GeomVertexArrayDataHandle$13$reserve_num_rows', 'pi'), ['int']),
    ]
    c.ct['set_data'] = [
        ('d', 'v', 1, ('v', 'GeomVertexArrayDataHandle$22$set_data', 'pp'), ['vector_uchar const&']),
    ]
    c.ct['set_num_rows'] = [
        ('d', 'B', 1, ('B', 'GeomVertexArrayDataHandle$11$set_num_rows', 'pi'), ['int']),
    ]
    c.ct['set_subdata'] = [
        ('d', 'v', 3, ('v', 'GeomVertexArrayDataHandle$24$set_subdata', 'pllp'), ['std::size_t', 'std::size_t', 'vector_uchar const&']),
    ]
    c.ct['unclean_set_num_rows'] = [
        ('d', 'B', 1, ('B', 'GeomVertexArrayDataHandle$12$unclean_set_num_rows', 'pi'), ['int']),
    ]
    c.ct['upcast_to_GeomEnums'] = [
        ('d', 5, 0, ('p', 'GeomVertexArrayDataHandle$2$upcast_to_GeomEnums', 'p'), []),
    ]
    c.ct['upcast_to_ReferenceCount'] = [
        ('d', 49, 0, ('p', 'GeomVertexArrayDataHandle$1$upcast_to_ReferenceCount', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomVertexArrayDataHandle, attr, self)

GeomVertexArrayDataHandle.c.link(GeomVertexArrayDataHandle)



class TypedReferenceCount(TypedObject, ReferenceCount):
    __bases__ = tuple([TypedObject, ReferenceCount])
    c = cxx.cstructs()
    c.register("TypedReferenceCount", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_DisplayRegion'] = [
        ('d', 61, 0, ('p', 'TypedReferenceCount$1$downcast_to_DisplayRegion', 'p'), []),
    ]
    c.ct['downcast_to_Loader'] = [
        ('d', 60, 0, ('p', 'TypedReferenceCount$2$downcast_to_Loader', 'p'), []),
    ]
    c.ct['downcast_to_TextFont'] = [
        ('d', 59, 0, ('p', 'TypedReferenceCount$3$downcast_to_TextFont', 'p'), []),
    ]
    c.ct['downcast_to_Thread'] = [
        ('d', 58, 0, ('p', 'TypedReferenceCount$4$downcast_to_Thread', 'p'), []),
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
        ('s', 58, 2, ('p', 'Thread$3$bind_thread', 'ss'), ['std::string const&', 'std::string const&']),
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
        ('s', 58, 0, ('p', 'Thread$13$get_current_thread', ''), []),
    ]
    c.ct['get_external_thread'] = [
        ('s', 58, 0, ('p', 'Thread$12$get_external_thread', ''), []),
    ]
    c.ct['get_main_thread'] = [
        ('s', 58, 0, ('p', 'Thread$11$get_main_thread', ''), []),
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
        ('d', 57, 0, ('p', 'Thread$29$get_current_task', 'p'), []),
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
        ('d', 48, 0, ('p', 'Thread$2$upcast_to_Namable', 'p'), []),
    ]
    c.ct['upcast_to_TypedReferenceCount'] = [
        ('d', 57, 0, ('p', 'Thread$1$upcast_to_TypedReferenceCount', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(Thread, attr, self)

Thread.c.link(Thread)



class TextFont(TypedReferenceCount, Namable):
    __bases__ = tuple([TypedReferenceCount, Namable])
    c = cxx.cstructs()
    c.register("TextFont", "upanda3d", """libupanda3d_c.so""")

    # enum RenderMode

    RM_distance_field = const(5)
    RM_extruded = const(3)
    RM_invalid = const(6)
    RM_polygon = const(2)
    RM_solid = const(4)
    RM_texture = const(0)
    RM_wireframe = const(1)


    # ctor/dtor


    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'TextFont$16$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'TextFont$17$init_type', ''), []),
    ]
    c.ct['string_render_mode'] = [
        ('s', 'p', 1, ('p', 'TextFont$15$string_render_mode', 's'), ['std::string const&']),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(TextFont, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(TextFont, 'init_type', None) )(*args,**kw)

    @classmethod
    def string_render_mode(cls, *args,**kw):
        return ( cls.c.get('string_render_mode', None) or cls.c.call(TextFont, 'string_render_mode', None) )(*args,**kw)

    # instance method type calls

    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'TextFont$19$force_init_type', 'p'), []),
    ]
    c.ct['get_glyph'] = [
        ('d', 'p', 1, ('p', 'TextFont$9$get_glyph', 'pi'), ['int']),
        ('d', 'B', 2, ('B', 'TextFont$10$get_glyph', 'pip'), ['int', 'ConstPointerTo< TextGlyph >&']),
    ]
    c.ct['get_invalid_glyph'] = [
        ('d', 'p', 0, ('p', 'TextFont$14$get_invalid_glyph', 'p'), []),
    ]
    c.ct['get_kerning'] = [
        ('d', 'f', 2, ('f', 'TextFont$11$get_kerning', 'pii'), ['int', 'int']),
    ]
    c.ct['get_line_height'] = [
        ('d', 'f', 0, ('f', 'TextFont$5$get_line_height', 'p'), []),
    ]
    c.ct['get_space_advance'] = [
        ('d', 'f', 0, ('f', 'TextFont$7$get_space_advance', 'p'), []),
    ]
    c.ct['get_total_poly_margin'] = [
        ('d', 'f', 0, ('f', 'TextFont$13$get_total_poly_margin', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'TextFont$18$get_type', 'p'), []),
    ]
    c.ct['is_valid'] = [
        ('d', 'B', 0, ('B', 'TextFont$4$is_valid', 'p'), []),
    ]
    c.ct['make_copy'] = [
        ('d', 59, 0, ('p', 'TextFont$3$make_copy', 'p'), []),
    ]
    c.ct['set_line_height'] = [
        ('d', 'v', 1, ('v', 'TextFont$6$set_line_height', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_space_advance'] = [
        ('d', 'v', 1, ('v', 'TextFont$8$set_space_advance', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['upcast_to_Namable'] = [
        ('d', 48, 0, ('p', 'TextFont$2$upcast_to_Namable', 'p'), []),
    ]
    c.ct['upcast_to_TypedReferenceCount'] = [
        ('d', 57, 0, ('p', 'TextFont$1$upcast_to_TypedReferenceCount', 'p'), []),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'TextFont$12$write', 'ppi'), ['std::ostream&', 'int']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TextFont, attr, self)

TextFont.c.link(TextFont)



class Loader(TypedReferenceCount, Namable):
    __bases__ = tuple([TypedReferenceCount, Namable])
    c = cxx.cstructs()
    c.register("Loader", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 60, 1, ('p', 'Loader$3$Loader', 'p'), ['Loader const&']),
        ('s', 60, 1, ('p', 'Loader$4$Loader', 's'), ['std::string const&']),
        ('s', 60, 0, ('p', 'Loader$5$Loader', ''), []),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'Loader$23$get_class_type', ''), []),
    ]
    c.ct['get_global_ptr'] = [
        ('s', 60, 0, ('p', 'Loader$22$get_global_ptr', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'Loader$24$init_type', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(Loader, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_global_ptr(cls, *args,**kw):
        return ( cls.c.get('get_global_ptr', None) or cls.c.call(Loader, 'get_global_ptr', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(Loader, 'init_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'Loader$26$force_init_type', 'p'), []),
    ]
    c.ct['get_task_chain'] = [
        ('d', 's', 0, ('s', 'Loader$9$get_task_chain', 'p'), []),
    ]
    c.ct['get_task_manager'] = [
        ('d', 'p', 0, ('p', 'Loader$7$get_task_manager', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'Loader$25$get_type', 'p'), []),
    ]
    c.ct['load_async'] = [
        ('d', 'v', 1, ('v', 'Loader$16$load_async', 'pp'), ['AsyncTask*']),
    ]
    c.ct['load_bam_stream'] = [
        ('d', 86, 1, ('p', 'Loader$20$load_bam_stream', 'pp'), ['std::istream&']),
    ]
    c.ct['load_sync'] = [
        ('d', 86, 2, ('p', 'Loader$12$load_sync', 'ppp'), ['Filename const&', 'LoaderOptions const&']),
        ('d', 86, 1, ('p', 'Loader$13$load_sync', 'pp'), ['Filename const&']),
    ]
    c.ct['make_async_request'] = [
        ('d', 'p', 2, ('p', 'Loader$14$make_async_request', 'ppp'), ['Filename const&', 'LoaderOptions const&']),
        ('d', 'p', 1, ('p', 'Loader$15$make_async_request', 'pp'), ['Filename const&']),
    ]
    c.ct['make_async_save_request'] = [
        ('d', 'p', 3, ('p', 'Loader$18$make_async_save_request', 'pppp'), ['Filename const&', 'LoaderOptions const&', 'PandaNode*']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'Loader$21$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['remove'] = [
        ('d', 'B', 1, ('B', 'Loader$11$remove', 'pp'), ['AsyncTask*']),
    ]
    c.ct['save_async'] = [
        ('d', 'v', 1, ('v', 'Loader$19$save_async', 'pp'), ['AsyncTask*']),
    ]
    c.ct['save_sync'] = [
        ('d', 'B', 3, ('B', 'Loader$17$save_sync', 'pppp'), ['Filename const&', 'LoaderOptions const&', 'PandaNode*']),
    ]
    c.ct['set_task_chain'] = [
        ('d', 'v', 1, ('v', 'Loader$8$set_task_chain', 'ps'), ['std::string const&']),
    ]
    c.ct['set_task_manager'] = [
        ('d', 'v', 1, ('v', 'Loader$6$set_task_manager', 'pp'), ['AsyncTaskManager*']),
    ]
    c.ct['stop_threads'] = [
        ('d', 'v', 0, ('v', 'Loader$10$stop_threads', 'p'), []),
    ]
    c.ct['upcast_to_Namable'] = [
        ('d', 48, 0, ('p', 'Loader$2$upcast_to_Namable', 'p'), []),
    ]
    c.ct['upcast_to_TypedReferenceCount'] = [
        ('d', 57, 0, ('p', 'Loader$1$upcast_to_TypedReferenceCount', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(Loader, attr, self)

Loader.c.link(Loader)



class DisplayRegion(TypedReferenceCount, DrawableRegion):
    __bases__ = tuple([TypedReferenceCount, DrawableRegion])
    c = cxx.cstructs()
    c.register("DisplayRegion", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'DisplayRegion$80$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'DisplayRegion$81$init_type', ''), []),
    ]
    c.ct['make_screenshot_filename'] = [
        ('s', 3, 1, ('p', 'DisplayRegion$60$make_screenshot_filename', 's'), ['std::string const&']),
        ('s', 3, 0, ('p', 'DisplayRegion$61$make_screenshot_filename', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(DisplayRegion, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(DisplayRegion, 'init_type', None) )(*args,**kw)

    @classmethod
    def make_screenshot_filename(cls, *args,**kw):
        return ( cls.c.get('make_screenshot_filename', None) or cls.c.call(DisplayRegion, 'make_screenshot_filename', None) )(*args,**kw)

    # instance method type calls

    c.ct['cleanup'] = [
        ('d', 'v', 0, ('v', 'DisplayRegion$3$cleanup', 'p'), []),
    ]
    c.ct['clear_cull_callback'] = [
        ('d', 'v', 0, ('v', 'DisplayRegion$48$clear_cull_callback', 'p'), []),
    ]
    c.ct['clear_draw_callback'] = [
        ('d', 'v', 0, ('v', 'DisplayRegion$51$clear_draw_callback', 'p'), []),
    ]
    c.ct['compute_pixels'] = [
        ('d', 'v', 0, ('v', 'DisplayRegion$69$compute_pixels', 'p'), []),
        ('d', 'v', 2, ('v', 'DisplayRegion$70$compute_pixels', 'pii'), ['int', 'int']),
    ]
    c.ct['compute_pixels_all_stages'] = [
        ('d', 'v', 0, ('v', 'DisplayRegion$71$compute_pixels_all_stages', 'p'), []),
        ('d', 'v', 2, ('v', 'DisplayRegion$72$compute_pixels_all_stages', 'pii'), ['int', 'int']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'DisplayRegion$83$force_init_type', 'p'), []),
    ]
    c.ct['get_bottom'] = [
        ('d', 'f', 1, ('f', 'DisplayRegion$12$get_bottom', 'pi'), ['int']),
        ('d', 'f', 0, ('f', 'DisplayRegion$13$get_bottom', 'p'), []),
    ]
    c.ct['get_camera'] = [
        ('d', 17, 1, ('p', 'DisplayRegion$24$get_camera', 'pp'), ['Thread*']),
        ('d', 17, 0, ('p', 'DisplayRegion$25$get_camera', 'p'), []),
    ]
    c.ct['get_cull_callback'] = [
        ('d', 'p', 0, ('p', 'DisplayRegion$49$get_cull_callback', 'p'), []),
    ]
    c.ct['get_cull_region_pcollector'] = [
        ('d', 'p', 0, ('p', 'DisplayRegion$77$get_cull_region_pcollector', 'p'), []),
    ]
    c.ct['get_cull_result'] = [
        ('d', 'p', 1, ('p', 'DisplayRegion$75$get_cull_result', 'pp'), ['Thread*']),
    ]
    c.ct['get_cull_traverser'] = [
        ('d', 'p', 0, ('p', 'DisplayRegion$41$get_cull_traverser', 'p'), []),
    ]
    c.ct['get_debug_name'] = [
        ('d', 's', 0, ('s', 'DisplayRegion$79$get_debug_name', 'p'), []),
    ]
    c.ct['get_dimensions'] = [
        ('d', 12, 1, ('p', 'DisplayRegion$6$get_dimensions', 'pi'), ['int']),
        ('d', 12, 0, ('p', 'DisplayRegion$7$get_dimensions', 'p'), []),
    ]
    c.ct['get_draw_callback'] = [
        ('d', 'p', 0, ('p', 'DisplayRegion$52$get_draw_callback', 'p'), []),
    ]
    c.ct['get_draw_region_pcollector'] = [
        ('d', 'p', 0, ('p', 'DisplayRegion$78$get_draw_region_pcollector', 'p'), []),
    ]
    c.ct['get_incomplete_render'] = [
        ('d', 'B', 0, ('B', 'DisplayRegion$35$get_incomplete_render', 'p'), []),
    ]
    c.ct['get_left'] = [
        ('d', 'f', 1, ('f', 'DisplayRegion$8$get_left', 'pi'), ['int']),
        ('d', 'f', 0, ('f', 'DisplayRegion$9$get_left', 'p'), []),
    ]
    c.ct['get_lens_index'] = [
        ('d', 'i', 0, ('i', 'DisplayRegion$39$get_lens_index', 'p'), []),
    ]
    c.ct['get_num_regions'] = [
        ('d', 'i', 0, ('i', 'DisplayRegion$4$get_num_regions', 'p'), []),
    ]
    c.ct['get_pipe'] = [
        ('d', 'p', 0, ('p', 'DisplayRegion$21$get_pipe', 'p'), []),
    ]
    c.ct['get_pixel_height'] = [
        ('d', 'i', 1, ('i', 'DisplayRegion$55$get_pixel_height', 'pi'), ['int']),
        ('d', 'i', 0, ('i', 'DisplayRegion$56$get_pixel_height', 'p'), []),
    ]
    c.ct['get_pixel_size'] = [
        ('d', 'p', 1, ('p', 'DisplayRegion$57$get_pixel_size', 'pi'), ['int']),
        ('d', 'p', 0, ('p', 'DisplayRegion$58$get_pixel_size', 'p'), []),
    ]
    c.ct['get_pixel_width'] = [
        ('d', 'i', 1, ('i', 'DisplayRegion$53$get_pixel_width', 'pi'), ['int']),
        ('d', 'i', 0, ('i', 'DisplayRegion$54$get_pixel_width', 'p'), []),
    ]
    c.ct['get_right'] = [
        ('d', 'f', 1, ('f', 'DisplayRegion$10$get_right', 'pi'), ['int']),
        ('d', 'f', 0, ('f', 'DisplayRegion$11$get_right', 'p'), []),
    ]
    c.ct['get_scene_setup'] = [
        ('d', 'p', 1, ('p', 'DisplayRegion$76$get_scene_setup', 'pp'), ['Thread*']),
    ]
    c.ct['get_scissor_enabled'] = [
        ('d', 'B', 0, ('B', 'DisplayRegion$46$get_scissor_enabled', 'p'), []),
    ]
    c.ct['get_screenshot'] = [
        ('d', 64, 0, ('p', 'DisplayRegion$66$get_screenshot', 'p'), []),
        ('d', 'B', 1, ('B', 'DisplayRegion$67$get_screenshot', 'pp'), ['PNMImage&']),
    ]
    c.ct['get_sort'] = [
        ('d', 'i', 0, ('i', 'DisplayRegion$29$get_sort', 'p'), []),
    ]
    c.ct['get_stereo_channel'] = [
        ('d', 'p', 0, ('p', 'DisplayRegion$31$get_stereo_channel', 'p'), []),
    ]
    c.ct['get_target_tex_page'] = [
        ('d', 'i', 0, ('i', 'DisplayRegion$44$get_target_tex_page', 'p'), []),
    ]
    c.ct['get_tex_view_offset'] = [
        ('d', 'i', 0, ('i', 'DisplayRegion$33$get_tex_view_offset', 'p'), []),
    ]
    c.ct['get_texture_reload_priority'] = [
        ('d', 'i', 0, ('i', 'DisplayRegion$37$get_texture_reload_priority', 'p'), []),
    ]
    c.ct['get_top'] = [
        ('d', 'f', 1, ('f', 'DisplayRegion$14$get_top', 'pi'), ['int']),
        ('d', 'f', 0, ('f', 'DisplayRegion$15$get_top', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'DisplayRegion$82$get_type', 'p'), []),
    ]
    c.ct['get_window'] = [
        ('d', 74, 0, ('p', 'DisplayRegion$20$get_window', 'p'), []),
    ]
    c.ct['is_active'] = [
        ('d', 'B', 0, ('B', 'DisplayRegion$27$is_active', 'p'), []),
    ]
    c.ct['is_stereo'] = [
        ('d', 'B', 0, ('B', 'DisplayRegion$22$is_stereo', 'p'), []),
    ]
    c.ct['make_cull_result_graph'] = [
        ('d', 86, 0, ('p', 'DisplayRegion$68$make_cull_result_graph', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'DisplayRegion$59$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['save_screenshot'] = [
        ('d', 'B', 2, ('B', 'DisplayRegion$64$save_screenshot', 'pps'), ['Filename const&', 'std::string const&']),
        ('d', 'B', 1, ('B', 'DisplayRegion$65$save_screenshot', 'pp'), ['Filename const&']),
    ]
    c.ct['save_screenshot_default'] = [
        ('d', 3, 1, ('p', 'DisplayRegion$62$save_screenshot_default', 'ps'), ['std::string const&']),
        ('d', 3, 0, ('p', 'DisplayRegion$63$save_screenshot_default', 'p'), []),
    ]
    c.ct['set_active'] = [
        ('d', 'v', 1, ('v', 'DisplayRegion$26$set_active', 'pB'), ['bool']),
    ]
    c.ct['set_camera'] = [
        ('d', 'v', 1, ('v', 'DisplayRegion$23$set_camera', 'pp'), ['NodePath const&']),
    ]
    c.ct['set_cube_map_index'] = [
        ('d', 'v', 1, ('v', 'DisplayRegion$42$set_cube_map_index', 'pi'), ['int']),
    ]
    c.ct['set_cull_callback'] = [
        ('d', 'v', 1, ('v', 'DisplayRegion$47$set_cull_callback', 'pp'), ['CallbackObject*']),
    ]
    c.ct['set_cull_result'] = [
        ('d', 'v', 3, ('v', 'DisplayRegion$74$set_cull_result', 'pppp'), ['PointerTo< CullResult >', 'PointerTo< SceneSetup >', 'Thread*']),
    ]
    c.ct['set_cull_traverser'] = [
        ('d', 'v', 1, ('v', 'DisplayRegion$40$set_cull_traverser', 'pp'), ['CullTraverser*']),
    ]
    c.ct['set_dimensions'] = [
        ('d', 'v', 1, ('v', 'DisplayRegion$16$set_dimensions', 'pp'), ['LVecBase4 const&']),
        ('d', 'v', 4, ('v', 'DisplayRegion$17$set_dimensions', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
        ('d', 'v', 2, ('v', 'DisplayRegion$18$set_dimensions', 'pip'), ['int', 'LVecBase4 const&']),
        ('d', 'v', 5, ('v', 'DisplayRegion$19$set_dimensions', 'piffff'), ['int', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_draw_callback'] = [
        ('d', 'v', 1, ('v', 'DisplayRegion$50$set_draw_callback', 'pp'), ['CallbackObject*']),
    ]
    c.ct['set_incomplete_render'] = [
        ('d', 'v', 1, ('v', 'DisplayRegion$34$set_incomplete_render', 'pB'), ['bool']),
    ]
    c.ct['set_lens_index'] = [
        ('d', 'v', 1, ('v', 'DisplayRegion$38$set_lens_index', 'pi'), ['int']),
    ]
    c.ct['set_num_regions'] = [
        ('d', 'v', 1, ('v', 'DisplayRegion$5$set_num_regions', 'pi'), ['int']),
    ]
    c.ct['set_scissor_enabled'] = [
        ('d', 'v', 1, ('v', 'DisplayRegion$45$set_scissor_enabled', 'pB'), ['bool']),
    ]
    c.ct['set_sort'] = [
        ('d', 'v', 1, ('v', 'DisplayRegion$28$set_sort', 'pi'), ['int']),
    ]
    c.ct['set_stereo_channel'] = [
        ('d', 'v', 1, ('v', 'DisplayRegion$30$set_stereo_channel', 'pp'), ['Lens::StereoChannel']),
    ]
    c.ct['set_target_tex_page'] = [
        ('d', 'v', 1, ('v', 'DisplayRegion$43$set_target_tex_page', 'pi'), ['int']),
    ]
    c.ct['set_tex_view_offset'] = [
        ('d', 'v', 1, ('v', 'DisplayRegion$32$set_tex_view_offset', 'pi'), ['int']),
    ]
    c.ct['set_texture_reload_priority'] = [
        ('d', 'v', 1, ('v', 'DisplayRegion$36$set_texture_reload_priority', 'pi'), ['int']),
    ]
    c.ct['supports_pixel_zoom'] = [
        ('d', 'B', 0, ('B', 'DisplayRegion$73$supports_pixel_zoom', 'p'), []),
    ]
    c.ct['upcast_to_DrawableRegion'] = [
        ('d', 1, 0, ('p', 'DisplayRegion$2$upcast_to_DrawableRegion', 'p'), []),
    ]
    c.ct['upcast_to_TypedReferenceCount'] = [
        ('d', 57, 0, ('p', 'DisplayRegion$1$upcast_to_TypedReferenceCount', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(DisplayRegion, attr, self)

DisplayRegion.c.link(DisplayRegion)



class WindowHandle(TypedReferenceCount):
    __bases__ = tuple([TypedReferenceCount])
    c = cxx.cstructs()
    c.register("WindowHandle", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 62, 1, ('p', 'WindowHandle$1$WindowHandle', 'p'), ['WindowHandle const&']),
        ('s', 62, 1, ('p', 'WindowHandle$2$WindowHandle', 'p'), ['WindowHandle::OSHandle*']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'WindowHandle$12$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'WindowHandle$13$init_type', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(WindowHandle, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(WindowHandle, 'init_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['attach_child'] = [
        ('d', 'v', 1, ('v', 'WindowHandle$8$attach_child', 'pp'), ['WindowHandle*']),
    ]
    c.ct['detach_child'] = [
        ('d', 'v', 1, ('v', 'WindowHandle$9$detach_child', 'pp'), ['WindowHandle*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'WindowHandle$15$force_init_type', 'p'), []),
    ]
    c.ct['get_int_handle'] = [
        ('d', 'l', 0, ('l', 'WindowHandle$6$get_int_handle', 'p'), []),
    ]
    c.ct['get_os_handle'] = [
        ('d', 'p', 0, ('p', 'WindowHandle$3$get_os_handle', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'WindowHandle$14$get_type', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'WindowHandle$7$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['receive_windows_message'] = [
        ('d', 'v', 3, ('v', 'WindowHandle$11$receive_windows_message', 'pIii'), ['unsigned int', 'int', 'int']),
    ]
    c.ct['request_keyboard_focus'] = [
        ('d', 'v', 1, ('v', 'WindowHandle$10$request_keyboard_focus', 'pp'), ['WindowHandle*']),
    ]
    c.ct['send_windows_message'] = [
        ('d', 'v', 3, ('v', 'WindowHandle$5$send_windows_message', 'pIii'), ['unsigned int', 'int', 'int']),
    ]
    c.ct['set_os_handle'] = [
        ('d', 'v', 1, ('v', 'WindowHandle$4$set_os_handle', 'pp'), ['WindowHandle::OSHandle*']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(WindowHandle, attr, self)

WindowHandle.c.link(WindowHandle)



class TypedWritableReferenceCount(TypedWritable, ReferenceCount):
    __bases__ = tuple([TypedWritable, ReferenceCount])
    c = cxx.cstructs()
    c.register("TypedWritableReferenceCount", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_GeomVertexArrayFormat'] = [
        ('d', 66, 0, ('p', 'TypedWritableReferenceCount$2$downcast_to_GeomVertexArrayFormat', 'p'), []),
    ]
    c.ct['downcast_to_GeomVertexFormat'] = [
        ('d', 65, 0, ('p', 'TypedWritableReferenceCount$3$downcast_to_GeomVertexFormat', 'p'), []),
    ]
    c.ct['downcast_to_PandaNode'] = [
        ('d', 86, 0, ('p', 'TypedWritableReferenceCount$1$downcast_to_PandaNode', 'p'), []),
    ]
    c.ct['downcast_to_Texture'] = [
        ('d', 64, 0, ('p', 'TypedWritableReferenceCount$4$downcast_to_Texture', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TypedWritableReferenceCount, attr, self)

TypedWritableReferenceCount.c.link(TypedWritableReferenceCount)



class Texture(TypedWritableReferenceCount, Namable):
    __bases__ = tuple([TypedWritableReferenceCount, Namable])
    c = cxx.cstructs()
    c.register("Texture", "upanda3d", """libupanda3d_c.so""")

    # enum CompressionMode

    CM_default = const(0)
    CM_dxt1 = const(4)
    CM_dxt2 = const(5)
    CM_dxt3 = const(6)
    CM_dxt4 = const(7)
    CM_dxt5 = const(8)
    CM_eac = const(14)
    CM_etc1 = const(12)
    CM_etc2 = const(13)
    CM_fxt1 = const(3)
    CM_off = const(1)
    CM_on = const(2)
    CM_pvr1_2bpp = const(9)
    CM_pvr1_4bpp = const(10)
    CM_rgtc = const(11)


    # enum ComponentType

    T_byte = const(5)
    T_float = const(2)
    T_half_float = const(7)
    T_int = const(4)
    T_short = const(6)
    T_unsigned_byte = const(0)
    T_unsigned_int = const(8)
    T_unsigned_int_24_8 = const(3)
    T_unsigned_short = const(1)


    # enum DeprecatedWrapMode

    WM_border_color = const(4)
    WM_clamp = const(0)
    WM_invalid = const(5)
    WM_mirror = const(2)
    WM_mirror_once = const(3)
    WM_repeat = const(1)


    # enum DeprecatedFilterType

    FT_default = const(7)
    FT_invalid = const(8)
    FT_linear = const(1)
    FT_linear_mipmap_linear = const(5)
    FT_linear_mipmap_nearest = const(3)
    FT_nearest = const(0)
    FT_nearest_mipmap_linear = const(4)
    FT_nearest_mipmap_nearest = const(2)
    FT_shadow = const(6)


    # enum TextureType

    TT_1d_texture = const(0)
    TT_1d_texture_array = const(7)
    TT_2d_texture = const(1)
    TT_2d_texture_array = const(3)
    TT_3d_texture = const(2)
    TT_buffer_texture = const(5)
    TT_cube_map = const(4)
    TT_cube_map_array = const(6)


    # enum Format

    F_alpha = const(6)
    F_blue = const(5)
    F_color_index = const(2)
    F_depth_component = const(23)
    F_depth_component16 = const(24)
    F_depth_component24 = const(25)
    F_depth_component32 = const(26)
    F_depth_stencil = const(1)
    F_green = const(4)
    F_luminance = const(18)
    F_luminance_alpha = const(19)
    F_luminance_alphamask = const(20)
    F_r11_g11_b10 = const(42)
    F_r16 = const(27)
    F_r16i = const(46)
    F_r32 = const(35)
    F_r32i = const(34)
    F_r8i = const(38)
    F_red = const(3)
    F_rg = const(45)
    F_rg16 = const(28)
    F_rg32 = const(36)
    F_rg8i = const(39)
    F_rgb = const(7)
    F_rgb10_a2 = const(44)
    F_rgb12 = const(10)
    F_rgb16 = const(29)
    F_rgb32 = const(37)
    F_rgb332 = const(11)
    F_rgb5 = const(8)
    F_rgb8 = const(9)
    F_rgb8i = const(40)
    F_rgb9_e5 = const(43)
    F_rgba = const(12)
    F_rgba12 = const(17)
    F_rgba16 = const(21)
    F_rgba32 = const(22)
    F_rgba4 = const(14)
    F_rgba5 = const(15)
    F_rgba8 = const(16)
    F_rgba8i = const(41)
    F_rgbm = const(13)
    F_sluminance = const(32)
    F_sluminance_alpha = const(33)
    F_srgb = const(30)
    F_srgb_alpha = const(31)


    # enum QualityLevel

    QL_best = const(3)
    QL_default = const(0)
    QL_fastest = const(1)
    QL_normal = const(2)


    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 64, 1, ('p', 'Texture$3$Texture', 's'), ['std::string const&']),
        ('s', 64, 0, ('p', 'Texture$4$Texture', ''), []),
    ]

    # classmethod type calls

    c.ct['consider_rescale'] = [
        ('s', 'v', 1, ('v', 'Texture$243$consider_rescale', 'pp'), ['PNMImage&']),
        ('s', 'v', 3, ('v', 'Texture$244$consider_rescale', 'psp'), ['PNMImage&', 'std::string const&', 'AutoTextureScale']),
        ('s', 'v', 2, ('v', 'Texture$245$consider_rescale', 'ps'), ['PNMImage&', 'std::string const&']),
    ]
    c.ct['down_to_power_2'] = [
        ('s', 'i', 1, ('i', 'Texture$242$down_to_power_2', 'i'), ['int']),
    ]
    c.ct['format_component_type'] = [
        ('s', 's', 1, ('s', 'Texture$249$format_component_type', 'p'), ['Texture::ComponentType']),
    ]
    c.ct['format_compression_mode'] = [
        ('s', 's', 1, ('s', 'Texture$253$format_compression_mode', 'p'), ['Texture::CompressionMode']),
    ]
    c.ct['format_format'] = [
        ('s', 's', 1, ('s', 'Texture$251$format_format', 'p'), ['Texture::Format']),
    ]
    c.ct['format_quality_level'] = [
        ('s', 's', 1, ('s', 'Texture$255$format_quality_level', 'p'), ['Texture::QualityLevel']),
    ]
    c.ct['format_texture_type'] = [
        ('s', 's', 1, ('s', 'Texture$247$format_texture_type', 'p'), ['Texture::TextureType']),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'Texture$270$get_class_type', ''), []),
    ]
    c.ct['get_textures_power_2'] = [
        ('s', 'p', 0, ('p', 'Texture$211$get_textures_power_2', ''), []),
    ]
    c.ct['has_alpha'] = [
        ('s', 'B', 1, ('B', 'Texture$263$has_alpha', 'p'), ['Texture::Format']),
    ]
    c.ct['has_binary_alpha'] = [
        ('s', 'B', 1, ('B', 'Texture$264$has_binary_alpha', 'p'), ['Texture::Format']),
    ]
    c.ct['has_textures_power_2'] = [
        ('s', 'B', 0, ('B', 'Texture$212$has_textures_power_2', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'Texture$271$init_type', ''), []),
    ]
    c.ct['is_specific'] = [
        ('s', 'B', 1, ('B', 'Texture$262$is_specific', 'p'), ['Texture::CompressionMode']),
    ]
    c.ct['is_srgb'] = [
        ('s', 'B', 1, ('B', 'Texture$265$is_srgb', 'p'), ['Texture::Format']),
    ]
    c.ct['is_unsigned'] = [
        ('s', 'B', 1, ('B', 'Texture$261$is_unsigned', 'p'), ['Texture::ComponentType']),
    ]
    c.ct['make_from_txo'] = [
        ('s', 64, 2, ('p', 'Texture$45$make_from_txo', 'ps'), ['std::istream&', 'std::string const&']),
        ('s', 64, 1, ('p', 'Texture$46$make_from_txo', 'p'), ['std::istream&']),
    ]
    c.ct['make_texture'] = [
        ('s', 64, 0, ('p', 'Texture$260$make_texture', ''), []),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'Texture$267$register_with_read_factory', ''), []),
    ]
    c.ct['set_textures_power_2'] = [
        ('s', 'v', 1, ('v', 'Texture$210$set_textures_power_2', 'p'), ['AutoTextureScale']),
    ]
    c.ct['string_component_type'] = [
        ('s', 'p', 1, ('p', 'Texture$250$string_component_type', 's'), ['std::string const&']),
    ]
    c.ct['string_compression_mode'] = [
        ('s', 'p', 1, ('p', 'Texture$254$string_compression_mode', 's'), ['std::string const&']),
    ]
    c.ct['string_format'] = [
        ('s', 'p', 1, ('p', 'Texture$252$string_format', 's'), ['std::string const&']),
    ]
    c.ct['string_quality_level'] = [
        ('s', 'p', 1, ('p', 'Texture$256$string_quality_level', 's'), ['std::string const&']),
    ]
    c.ct['string_texture_type'] = [
        ('s', 'p', 1, ('p', 'Texture$248$string_texture_type', 's'), ['std::string const&']),
    ]
    c.ct['up_to_power_2'] = [
        ('s', 'i', 1, ('i', 'Texture$241$up_to_power_2', 'i'), ['int']),
    ]

    @classmethod
    def consider_rescale(cls, *args,**kw):
        return ( cls.c.get('consider_rescale', None) or cls.c.call(Texture, 'consider_rescale', None) )(*args,**kw)

    @classmethod
    def down_to_power_2(cls, *args,**kw):
        return ( cls.c.get('down_to_power_2', None) or cls.c.call(Texture, 'down_to_power_2', None) )(*args,**kw)

    @classmethod
    def format_component_type(cls, *args,**kw):
        return ( cls.c.get('format_component_type', None) or cls.c.call(Texture, 'format_component_type', None) )(*args,**kw)

    @classmethod
    def format_compression_mode(cls, *args,**kw):
        return ( cls.c.get('format_compression_mode', None) or cls.c.call(Texture, 'format_compression_mode', None) )(*args,**kw)

    @classmethod
    def format_format(cls, *args,**kw):
        return ( cls.c.get('format_format', None) or cls.c.call(Texture, 'format_format', None) )(*args,**kw)

    @classmethod
    def format_quality_level(cls, *args,**kw):
        return ( cls.c.get('format_quality_level', None) or cls.c.call(Texture, 'format_quality_level', None) )(*args,**kw)

    @classmethod
    def format_texture_type(cls, *args,**kw):
        return ( cls.c.get('format_texture_type', None) or cls.c.call(Texture, 'format_texture_type', None) )(*args,**kw)

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(Texture, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_textures_power_2(cls, *args,**kw):
        return ( cls.c.get('get_textures_power_2', None) or cls.c.call(Texture, 'get_textures_power_2', None) )(*args,**kw)

    @classmethod
    def has_alpha(cls, *args,**kw):
        return ( cls.c.get('has_alpha', None) or cls.c.call(Texture, 'has_alpha', None) )(*args,**kw)

    @classmethod
    def has_binary_alpha(cls, *args,**kw):
        return ( cls.c.get('has_binary_alpha', None) or cls.c.call(Texture, 'has_binary_alpha', None) )(*args,**kw)

    @classmethod
    def has_textures_power_2(cls, *args,**kw):
        return ( cls.c.get('has_textures_power_2', None) or cls.c.call(Texture, 'has_textures_power_2', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(Texture, 'init_type', None) )(*args,**kw)

    @classmethod
    def is_specific(cls, *args,**kw):
        return ( cls.c.get('is_specific', None) or cls.c.call(Texture, 'is_specific', None) )(*args,**kw)

    @classmethod
    def is_srgb(cls, *args,**kw):
        return ( cls.c.get('is_srgb', None) or cls.c.call(Texture, 'is_srgb', None) )(*args,**kw)

    @classmethod
    def is_unsigned(cls, *args,**kw):
        return ( cls.c.get('is_unsigned', None) or cls.c.call(Texture, 'is_unsigned', None) )(*args,**kw)

    @classmethod
    def make_from_txo(cls, *args,**kw):
        return ( cls.c.get('make_from_txo', None) or cls.c.call(Texture, 'make_from_txo', None) )(*args,**kw)

    @classmethod
    def make_texture(cls, *args,**kw):
        return ( cls.c.get('make_texture', None) or cls.c.call(Texture, 'make_texture', None) )(*args,**kw)

    @classmethod
    def register_with_read_factory(cls, *args,**kw):
        return ( cls.c.get('register_with_read_factory', None) or cls.c.call(Texture, 'register_with_read_factory', None) )(*args,**kw)

    @classmethod
    def set_textures_power_2(cls, *args,**kw):
        return ( cls.c.get('set_textures_power_2', None) or cls.c.call(Texture, 'set_textures_power_2', None) )(*args,**kw)

    @classmethod
    def string_component_type(cls, *args,**kw):
        return ( cls.c.get('string_component_type', None) or cls.c.call(Texture, 'string_component_type', None) )(*args,**kw)

    @classmethod
    def string_compression_mode(cls, *args,**kw):
        return ( cls.c.get('string_compression_mode', None) or cls.c.call(Texture, 'string_compression_mode', None) )(*args,**kw)

    @classmethod
    def string_format(cls, *args,**kw):
        return ( cls.c.get('string_format', None) or cls.c.call(Texture, 'string_format', None) )(*args,**kw)

    @classmethod
    def string_quality_level(cls, *args,**kw):
        return ( cls.c.get('string_quality_level', None) or cls.c.call(Texture, 'string_quality_level', None) )(*args,**kw)

    @classmethod
    def string_texture_type(cls, *args,**kw):
        return ( cls.c.get('string_texture_type', None) or cls.c.call(Texture, 'string_texture_type', None) )(*args,**kw)

    @classmethod
    def up_to_power_2(cls, *args,**kw):
        return ( cls.c.get('up_to_power_2', None) or cls.c.call(Texture, 'up_to_power_2', None) )(*args,**kw)

    # instance method type calls

    c.ct['clear'] = [
        ('d', 'v', 0, ('v', 'Texture$6$clear', 'p'), []),
    ]
    c.ct['clear_alpha_filename'] = [
        ('d', 'v', 0, ('v', 'Texture$79$clear_alpha_filename', 'p'), []),
    ]
    c.ct['clear_alpha_fullpath'] = [
        ('d', 'v', 0, ('v', 'Texture$87$clear_alpha_fullpath', 'p'), []),
    ]
    c.ct['clear_aux_data'] = [
        ('d', 'v', 1, ('v', 'Texture$208$clear_aux_data', 'ps'), ['std::string const&']),
    ]
    c.ct['clear_clear_color'] = [
        ('d', 'v', 0, ('v', 'Texture$29$clear_clear_color', 'p'), []),
    ]
    c.ct['clear_filename'] = [
        ('d', 'v', 0, ('v', 'Texture$75$clear_filename', 'p'), []),
    ]
    c.ct['clear_fullpath'] = [
        ('d', 'v', 0, ('v', 'Texture$83$clear_fullpath', 'p'), []),
    ]
    c.ct['clear_image'] = [
        ('d', 'v', 0, ('v', 'Texture$25$clear_image', 'p'), []),
    ]
    c.ct['clear_ram_image'] = [
        ('d', 'v', 0, ('v', 'Texture$152$clear_ram_image', 'p'), []),
    ]
    c.ct['clear_ram_mipmap_image'] = [
        ('d', 'v', 1, ('v', 'Texture$178$clear_ram_mipmap_image', 'pi'), ['int']),
    ]
    c.ct['clear_ram_mipmap_images'] = [
        ('d', 'v', 0, ('v', 'Texture$179$clear_ram_mipmap_images', 'p'), []),
    ]
    c.ct['clear_simple_ram_image'] = [
        ('d', 'v', 0, ('v', 'Texture$190$clear_simple_ram_image', 'p'), []),
    ]
    c.ct['compress_ram_image'] = [
        ('d', 'B', 3, ('B', 'Texture$156$compress_ram_image', 'pppp'), ['Texture::CompressionMode', 'Texture::QualityLevel', 'GraphicsStateGuardianBase*']),
        ('d', 'B', 2, ('B', 'Texture$157$compress_ram_image', 'ppp'), ['Texture::CompressionMode', 'Texture::QualityLevel']),
        ('d', 'B', 1, ('B', 'Texture$158$compress_ram_image', 'pp'), ['Texture::CompressionMode']),
        ('d', 'B', 0, ('B', 'Texture$159$compress_ram_image', 'p'), []),
    ]
    c.ct['consider_rescale'] = [
        ('d', 'v', 1, ('v', 'Texture$243$consider_rescale', 'pp'), ['PNMImage&']),
        ('d', 'v', 3, ('v', 'Texture$244$consider_rescale', 'psp'), ['PNMImage&', 'std::string const&', 'AutoTextureScale']),
        ('d', 'v', 2, ('v', 'Texture$245$consider_rescale', 'ps'), ['PNMImage&', 'std::string const&']),
    ]
    c.ct['cull_callback'] = [
        ('d', 'B', 2, ('B', 'Texture$259$cull_callback', 'ppp'), ['CullTraverser*', 'CullTraverserData const&']),
    ]
    c.ct['ensure_loader_type'] = [
        ('d', 'v', 1, ('v', 'Texture$266$ensure_loader_type', 'pp'), ['Filename const&']),
    ]
    c.ct['estimate_texture_memory'] = [
        ('d', 'l', 0, ('l', 'Texture$206$estimate_texture_memory', 'p'), []),
    ]
    c.ct['finalize'] = [
        ('d', 'v', 1, ('v', 'Texture$269$finalize', 'pp'), ['BamReader*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'Texture$273$force_init_type', 'p'), []),
    ]
    c.ct['generate_alpha_scale_map'] = [
        ('d', 'v', 0, ('v', 'Texture$24$generate_alpha_scale_map', 'p'), []),
    ]
    c.ct['generate_normalization_cube_map'] = [
        ('d', 'v', 1, ('v', 'Texture$23$generate_normalization_cube_map', 'pi'), ['int']),
    ]
    c.ct['generate_ram_mipmap_images'] = [
        ('d', 'v', 0, ('v', 'Texture$180$generate_ram_mipmap_images', 'p'), []),
    ]
    c.ct['generate_simple_ram_image'] = [
        ('d', 'v', 0, ('v', 'Texture$189$generate_simple_ram_image', 'p'), []),
    ]
    c.ct['get_active'] = [
        ('d', 'B', 1, ('B', 'Texture$202$get_active', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['get_alpha_filename'] = [
        ('d', 3, 0, ('p', 'Texture$77$get_alpha_filename', 'p'), []),
    ]
    c.ct['get_alpha_fullpath'] = [
        ('d', 3, 0, ('p', 'Texture$85$get_alpha_fullpath', 'p'), []),
    ]
    c.ct['get_anisotropic_degree'] = [
        ('d', 'i', 0, ('i', 'Texture$117$get_anisotropic_degree', 'p'), []),
    ]
    c.ct['get_auto_texture_scale'] = [
        ('d', 'p', 0, ('p', 'Texture$196$get_auto_texture_scale', 'p'), []),
    ]
    c.ct['get_aux_data'] = [
        ('d', 57, 1, ('p', 'Texture$209$get_aux_data', 'ps'), ['std::string const&']),
    ]
    c.ct['get_border_color'] = [
        ('d', 'p', 0, ('p', 'Texture$120$get_border_color', 'p'), []),
    ]
    c.ct['get_clear_color'] = [
        ('d', 'p', 0, ('p', 'Texture$27$get_clear_color', 'p'), []),
    ]
    c.ct['get_clear_data'] = [
        ('d', 'p', 0, ('p', 'Texture$30$get_clear_data', 'p'), []),
    ]
    c.ct['get_component_type'] = [
        ('d', 'p', 0, ('p', 'Texture$103$get_component_type', 'p'), []),
    ]
    c.ct['get_component_width'] = [
        ('d', 'i', 0, ('i', 'Texture$98$get_component_width', 'p'), []),
    ]
    c.ct['get_compression'] = [
        ('d', 'p', 0, ('p', 'Texture$123$get_compression', 'p'), []),
    ]
    c.ct['get_data_size_bytes'] = [
        ('d', 'l', 1, ('l', 'Texture$201$get_data_size_bytes', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['get_default_sampler'] = [
        ('d', 'p', 0, ('p', 'Texture$127$get_default_sampler', 'p'), []),
    ]
    c.ct['get_effective_anisotropic_degree'] = [
        ('d', 'i', 0, ('i', 'Texture$118$get_effective_anisotropic_degree', 'p'), []),
    ]
    c.ct['get_effective_magfilter'] = [
        ('d', 'p', 0, ('p', 'Texture$115$get_effective_magfilter', 'p'), []),
    ]
    c.ct['get_effective_minfilter'] = [
        ('d', 'p', 0, ('p', 'Texture$112$get_effective_minfilter', 'p'), []),
    ]
    c.ct['get_effective_quality_level'] = [
        ('d', 'p', 0, ('p', 'Texture$131$get_effective_quality_level', 'p'), []),
    ]
    c.ct['get_expected_mipmap_num_pages'] = [
        ('d', 'i', 1, ('i', 'Texture$137$get_expected_mipmap_num_pages', 'pi'), ['int']),
    ]
    c.ct['get_expected_mipmap_x_size'] = [
        ('d', 'i', 1, ('i', 'Texture$134$get_expected_mipmap_x_size', 'pi'), ['int']),
    ]
    c.ct['get_expected_mipmap_y_size'] = [
        ('d', 'i', 1, ('i', 'Texture$135$get_expected_mipmap_y_size', 'pi'), ['int']),
    ]
    c.ct['get_expected_mipmap_z_size'] = [
        ('d', 'i', 1, ('i', 'Texture$136$get_expected_mipmap_z_size', 'pi'), ['int']),
    ]
    c.ct['get_expected_num_mipmap_levels'] = [
        ('d', 'i', 0, ('i', 'Texture$133$get_expected_num_mipmap_levels', 'p'), []),
    ]
    c.ct['get_expected_ram_image_size'] = [
        ('d', 'l', 0, ('l', 'Texture$144$get_expected_ram_image_size', 'p'), []),
    ]
    c.ct['get_expected_ram_mipmap_image_size'] = [
        ('d', 'l', 1, ('l', 'Texture$168$get_expected_ram_mipmap_image_size', 'pi'), ['int']),
    ]
    c.ct['get_expected_ram_mipmap_page_size'] = [
        ('d', 'l', 1, ('l', 'Texture$170$get_expected_ram_mipmap_page_size', 'pi'), ['int']),
    ]
    c.ct['get_expected_ram_mipmap_view_size'] = [
        ('d', 'l', 1, ('l', 'Texture$169$get_expected_ram_mipmap_view_size', 'pi'), ['int']),
    ]
    c.ct['get_expected_ram_page_size'] = [
        ('d', 'l', 0, ('l', 'Texture$145$get_expected_ram_page_size', 'p'), []),
    ]
    c.ct['get_filename'] = [
        ('d', 3, 0, ('p', 'Texture$73$get_filename', 'p'), []),
    ]
    c.ct['get_format'] = [
        ('d', 'p', 0, ('p', 'Texture$101$get_format', 'p'), []),
    ]
    c.ct['get_fullpath'] = [
        ('d', 3, 0, ('p', 'Texture$81$get_fullpath', 'p'), []),
    ]
    c.ct['get_image_modified'] = [
        ('d', 26, 0, ('p', 'Texture$193$get_image_modified', 'p'), []),
    ]
    c.ct['get_keep_ram_image'] = [
        ('d', 'B', 0, ('B', 'Texture$154$get_keep_ram_image', 'p'), []),
    ]
    c.ct['get_loaded_from_image'] = [
        ('d', 'B', 0, ('B', 'Texture$232$get_loaded_from_image', 'p'), []),
    ]
    c.ct['get_loaded_from_txo'] = [
        ('d', 'B', 0, ('B', 'Texture$235$get_loaded_from_txo', 'p'), []),
    ]
    c.ct['get_magfilter'] = [
        ('d', 'p', 0, ('p', 'Texture$114$get_magfilter', 'p'), []),
    ]
    c.ct['get_match_framebuffer_format'] = [
        ('d', 'B', 0, ('B', 'Texture$236$get_match_framebuffer_format', 'p'), []),
    ]
    c.ct['get_minfilter'] = [
        ('d', 'p', 0, ('p', 'Texture$111$get_minfilter', 'p'), []),
    ]
    c.ct['get_num_components'] = [
        ('d', 'i', 0, ('i', 'Texture$97$get_num_components', 'p'), []),
    ]
    c.ct['get_num_loadable_ram_mipmap_images'] = [
        ('d', 'i', 0, ('i', 'Texture$163$get_num_loadable_ram_mipmap_images', 'p'), []),
    ]
    c.ct['get_num_pages'] = [
        ('d', 'i', 0, ('i', 'Texture$96$get_num_pages', 'p'), []),
    ]
    c.ct['get_num_ram_mipmap_images'] = [
        ('d', 'i', 0, ('i', 'Texture$161$get_num_ram_mipmap_images', 'p'), []),
    ]
    c.ct['get_num_views'] = [
        ('d', 'i', 0, ('i', 'Texture$94$get_num_views', 'p'), []),
    ]
    c.ct['get_orig_file_x_size'] = [
        ('d', 'i', 0, ('i', 'Texture$225$get_orig_file_x_size', 'p'), []),
    ]
    c.ct['get_orig_file_y_size'] = [
        ('d', 'i', 0, ('i', 'Texture$226$get_orig_file_y_size', 'p'), []),
    ]
    c.ct['get_orig_file_z_size'] = [
        ('d', 'i', 0, ('i', 'Texture$227$get_orig_file_z_size', 'p'), []),
    ]
    c.ct['get_pad_x_size'] = [
        ('d', 'i', 0, ('i', 'Texture$213$get_pad_x_size', 'p'), []),
    ]
    c.ct['get_pad_y_size'] = [
        ('d', 'i', 0, ('i', 'Texture$214$get_pad_y_size', 'p'), []),
    ]
    c.ct['get_pad_z_size'] = [
        ('d', 'i', 0, ('i', 'Texture$215$get_pad_z_size', 'p'), []),
    ]
    c.ct['get_post_load_store_cache'] = [
        ('d', 'B', 0, ('B', 'Texture$238$get_post_load_store_cache', 'p'), []),
    ]
    c.ct['get_properties_modified'] = [
        ('d', 26, 0, ('p', 'Texture$192$get_properties_modified', 'p'), []),
    ]
    c.ct['get_quality_level'] = [
        ('d', 'p', 0, ('p', 'Texture$130$get_quality_level', 'p'), []),
    ]
    c.ct['get_ram_image'] = [
        ('d', 'p', 0, ('p', 'Texture$146$get_ram_image', 'p'), []),
    ]
    c.ct['get_ram_image_as'] = [
        ('d', 'p', 1, ('p', 'Texture$149$get_ram_image_as', 'ps'), ['std::string const&']),
    ]
    c.ct['get_ram_image_compression'] = [
        ('d', 'p', 0, ('p', 'Texture$147$get_ram_image_compression', 'p'), []),
    ]
    c.ct['get_ram_image_size'] = [
        ('d', 'l', 0, ('l', 'Texture$141$get_ram_image_size', 'p'), []),
    ]
    c.ct['get_ram_mipmap_image'] = [
        ('d', 'p', 1, ('p', 'Texture$171$get_ram_mipmap_image', 'pi'), ['int']),
    ]
    c.ct['get_ram_mipmap_image_size'] = [
        ('d', 'l', 1, ('l', 'Texture$165$get_ram_mipmap_image_size', 'pi'), ['int']),
    ]
    c.ct['get_ram_mipmap_page_size'] = [
        ('d', 'l', 1, ('l', 'Texture$167$get_ram_mipmap_page_size', 'pi'), ['int']),
    ]
    c.ct['get_ram_mipmap_pointer'] = [
        ('d', 'v', 1, ('v', 'Texture$172$get_ram_mipmap_pointer', 'pi'), ['int']),
    ]
    c.ct['get_ram_mipmap_view_size'] = [
        ('d', 'l', 1, ('l', 'Texture$166$get_ram_mipmap_view_size', 'pi'), ['int']),
    ]
    c.ct['get_ram_page_size'] = [
        ('d', 'l', 0, ('l', 'Texture$143$get_ram_page_size', 'p'), []),
    ]
    c.ct['get_ram_view_size'] = [
        ('d', 'l', 0, ('l', 'Texture$142$get_ram_view_size', 'p'), []),
    ]
    c.ct['get_render_to_texture'] = [
        ('d', 'B', 0, ('B', 'Texture$125$get_render_to_texture', 'p'), []),
    ]
    c.ct['get_resident'] = [
        ('d', 'B', 1, ('B', 'Texture$203$get_resident', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['get_simple_image_modified'] = [
        ('d', 26, 0, ('p', 'Texture$194$get_simple_image_modified', 'p'), []),
    ]
    c.ct['get_simple_ram_image'] = [
        ('d', 'p', 0, ('p', 'Texture$185$get_simple_ram_image', 'p'), []),
    ]
    c.ct['get_simple_ram_image_size'] = [
        ('d', 'l', 0, ('l', 'Texture$184$get_simple_ram_image_size', 'p'), []),
    ]
    c.ct['get_simple_x_size'] = [
        ('d', 'i', 0, ('i', 'Texture$181$get_simple_x_size', 'p'), []),
    ]
    c.ct['get_simple_y_size'] = [
        ('d', 'i', 0, ('i', 'Texture$182$get_simple_y_size', 'p'), []),
    ]
    c.ct['get_tex_scale'] = [
        ('d', 6, 0, ('p', 'Texture$216$get_tex_scale', 'p'), []),
    ]
    c.ct['get_texture_type'] = [
        ('d', 'p', 0, ('p', 'Texture$99$get_texture_type', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'Texture$272$get_type', 'p'), []),
    ]
    c.ct['get_uncompressed_ram_image'] = [
        ('d', 'p', 0, ('p', 'Texture$148$get_uncompressed_ram_image', 'p'), []),
    ]
    c.ct['get_usage_hint'] = [
        ('d', 'p', 0, ('p', 'Texture$100$get_usage_hint', 'p'), []),
    ]
    c.ct['get_wrap_u'] = [
        ('d', 'p', 0, ('p', 'Texture$105$get_wrap_u', 'p'), []),
    ]
    c.ct['get_wrap_v'] = [
        ('d', 'p', 0, ('p', 'Texture$107$get_wrap_v', 'p'), []),
    ]
    c.ct['get_wrap_w'] = [
        ('d', 'p', 0, ('p', 'Texture$109$get_wrap_w', 'p'), []),
    ]
    c.ct['get_x_size'] = [
        ('d', 'i', 0, ('i', 'Texture$88$get_x_size', 'p'), []),
    ]
    c.ct['get_y_size'] = [
        ('d', 'i', 0, ('i', 'Texture$90$get_y_size', 'p'), []),
    ]
    c.ct['get_z_size'] = [
        ('d', 'i', 0, ('i', 'Texture$92$get_z_size', 'p'), []),
    ]
    c.ct['has_all_ram_mipmap_images'] = [
        ('d', 'B', 0, ('B', 'Texture$164$has_all_ram_mipmap_images', 'p'), []),
    ]
    c.ct['has_alpha_filename'] = [
        ('d', 'B', 0, ('B', 'Texture$76$has_alpha_filename', 'p'), []),
    ]
    c.ct['has_alpha_fullpath'] = [
        ('d', 'B', 0, ('B', 'Texture$84$has_alpha_fullpath', 'p'), []),
    ]
    c.ct['has_auto_texture_scale'] = [
        ('d', 'B', 0, ('B', 'Texture$195$has_auto_texture_scale', 'p'), []),
    ]
    c.ct['has_clear_color'] = [
        ('d', 'B', 0, ('B', 'Texture$26$has_clear_color', 'p'), []),
    ]
    c.ct['has_compression'] = [
        ('d', 'B', 0, ('B', 'Texture$122$has_compression', 'p'), []),
    ]
    c.ct['has_cull_callback'] = [
        ('d', 'B', 0, ('B', 'Texture$258$has_cull_callback', 'p'), []),
    ]
    c.ct['has_filename'] = [
        ('d', 'B', 0, ('B', 'Texture$72$has_filename', 'p'), []),
    ]
    c.ct['has_fullpath'] = [
        ('d', 'B', 0, ('B', 'Texture$80$has_fullpath', 'p'), []),
    ]
    c.ct['has_ram_image'] = [
        ('d', 'B', 0, ('B', 'Texture$138$has_ram_image', 'p'), []),
    ]
    c.ct['has_ram_mipmap_image'] = [
        ('d', 'B', 1, ('B', 'Texture$162$has_ram_mipmap_image', 'pi'), ['int']),
    ]
    c.ct['has_simple_ram_image'] = [
        ('d', 'B', 0, ('B', 'Texture$183$has_simple_ram_image', 'p'), []),
    ]
    c.ct['has_uncompressed_ram_image'] = [
        ('d', 'B', 0, ('B', 'Texture$139$has_uncompressed_ram_image', 'p'), []),
    ]
    c.ct['is_cacheable'] = [
        ('d', 'B', 0, ('B', 'Texture$155$is_cacheable', 'p'), []),
    ]
    c.ct['is_prepared'] = [
        ('d', 'B', 1, ('B', 'Texture$199$is_prepared', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['load'] = [
        ('d', 'B', 2, ('B', 'Texture$55$load', 'ppp'), ['PNMImage const&', 'LoaderOptions const&']),
        ('d', 'B', 1, ('B', 'Texture$56$load', 'pp'), ['PNMImage const&']),
        ('d', 'B', 4, ('B', 'Texture$57$load', 'ppiip'), ['PNMImage const&', 'int', 'int', 'LoaderOptions const&']),
        ('d', 'B', 3, ('B', 'Texture$58$load', 'ppii'), ['PNMImage const&', 'int', 'int']),
        ('d', 'B', 2, ('B', 'Texture$59$load', 'ppp'), ['PfmFile const&', 'LoaderOptions const&']),
        ('d', 'B', 1, ('B', 'Texture$60$load', 'pp'), ['PfmFile const&']),
        ('d', 'B', 4, ('B', 'Texture$61$load', 'ppiip'), ['PfmFile const&', 'int', 'int', 'LoaderOptions const&']),
        ('d', 'B', 3, ('B', 'Texture$62$load', 'ppii'), ['PfmFile const&', 'int', 'int']),
    ]
    c.ct['load_related'] = [
        ('d', 64, 1, ('p', 'Texture$71$load_related', 'ps'), ['InternalName const*']),
    ]
    c.ct['load_sub_image'] = [
        ('d', 'B', 5, ('B', 'Texture$63$load_sub_image', 'ppiiii'), ['PNMImage const&', 'int', 'int', 'int', 'int']),
        ('d', 'B', 4, ('B', 'Texture$64$load_sub_image', 'ppiii'), ['PNMImage const&', 'int', 'int', 'int']),
        ('d', 'B', 3, ('B', 'Texture$65$load_sub_image', 'ppii'), ['PNMImage const&', 'int', 'int']),
    ]
    c.ct['make_copy'] = [
        ('d', 64, 0, ('p', 'Texture$5$make_copy', 'p'), []),
    ]
    c.ct['make_ram_image'] = [
        ('d', 'p', 0, ('p', 'Texture$151$make_ram_image', 'p'), []),
    ]
    c.ct['make_ram_mipmap_image'] = [
        ('d', 'p', 1, ('p', 'Texture$174$make_ram_mipmap_image', 'pi'), ['int']),
    ]
    c.ct['might_have_ram_image'] = [
        ('d', 'B', 0, ('B', 'Texture$140$might_have_ram_image', 'p'), []),
    ]
    c.ct['modify_ram_image'] = [
        ('d', 'p', 0, ('p', 'Texture$150$modify_ram_image', 'p'), []),
    ]
    c.ct['modify_ram_mipmap_image'] = [
        ('d', 'p', 1, ('p', 'Texture$173$modify_ram_mipmap_image', 'pi'), ['int']),
    ]
    c.ct['modify_simple_ram_image'] = [
        ('d', 'p', 0, ('p', 'Texture$187$modify_simple_ram_image', 'p'), []),
    ]
    c.ct['new_simple_ram_image'] = [
        ('d', 'p', 2, ('p', 'Texture$188$new_simple_ram_image', 'pii'), ['int', 'int']),
    ]
    c.ct['peek'] = [
        ('d', 52, 0, ('p', 'Texture$191$peek', 'p'), []),
    ]
    c.ct['prepare'] = [
        ('d', 'p', 1, ('p', 'Texture$198$prepare', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['prepare_now'] = [
        ('d', 'p', 3, ('p', 'Texture$240$prepare_now', 'pipp'), ['int', 'PreparedGraphicsObjects*', 'GraphicsStateGuardianBase*']),
    ]
    c.ct['read'] = [
        ('d', 'B', 5, ('B', 'Texture$31$read', 'pppiip'), ['Filename const&', 'Filename const&', 'int', 'int', 'LoaderOptions const&']),
        ('d', 'B', 4, ('B', 'Texture$32$read', 'pppii'), ['Filename const&', 'Filename const&', 'int', 'int']),
        ('d', 'B', 10, ('B', 'Texture$33$read', 'pppiiiiBBpp'), ['Filename const&', 'Filename const&', 'int', 'int', 'int', 'int', 'bool', 'bool', 'BamCacheRecord*', 'LoaderOptions const&']),
        ('d', 'B', 9, ('B', 'Texture$34$read', 'pppiiiiBBp'), ['Filename const&', 'Filename const&', 'int', 'int', 'int', 'int', 'bool', 'bool', 'BamCacheRecord*']),
        ('d', 'B', 8, ('B', 'Texture$35$read', 'pppiiiiBB'), ['Filename const&', 'Filename const&', 'int', 'int', 'int', 'int', 'bool', 'bool']),
        ('d', 'B', 2, ('B', 'Texture$36$read', 'ppp'), ['Filename const&', 'LoaderOptions const&']),
        ('d', 'B', 1, ('B', 'Texture$37$read', 'pp'), ['Filename const&']),
        ('d', 'B', 6, ('B', 'Texture$38$read', 'ppiiBBp'), ['Filename const&', 'int', 'int', 'bool', 'bool', 'LoaderOptions const&']),
        ('d', 'B', 5, ('B', 'Texture$39$read', 'ppiiBB'), ['Filename const&', 'int', 'int', 'bool', 'bool']),
    ]
    c.ct['read_dds'] = [
        ('d', 'B', 3, ('B', 'Texture$49$read_dds', 'ppsB'), ['std::istream&', 'std::string const&', 'bool']),
        ('d', 'B', 2, ('B', 'Texture$50$read_dds', 'pps'), ['std::istream&', 'std::string const&']),
        ('d', 'B', 1, ('B', 'Texture$51$read_dds', 'pp'), ['std::istream&']),
    ]
    c.ct['read_ktx'] = [
        ('d', 'B', 3, ('B', 'Texture$52$read_ktx', 'ppsB'), ['std::istream&', 'std::string const&', 'bool']),
        ('d', 'B', 2, ('B', 'Texture$53$read_ktx', 'pps'), ['std::istream&', 'std::string const&']),
        ('d', 'B', 1, ('B', 'Texture$54$read_ktx', 'pp'), ['std::istream&']),
    ]
    c.ct['read_txo'] = [
        ('d', 'B', 2, ('B', 'Texture$43$read_txo', 'pps'), ['std::istream&', 'std::string const&']),
        ('d', 'B', 1, ('B', 'Texture$44$read_txo', 'pp'), ['std::istream&']),
    ]
    c.ct['release'] = [
        ('d', 'B', 1, ('B', 'Texture$204$release', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['release_all'] = [
        ('d', 'i', 0, ('i', 'Texture$205$release_all', 'p'), []),
    ]
    c.ct['reload'] = [
        ('d', 'B', 0, ('B', 'Texture$70$reload', 'p'), []),
    ]
    c.ct['rescale_texture'] = [
        ('d', 'B', 0, ('B', 'Texture$246$rescale_texture', 'p'), []),
    ]
    c.ct['set_alpha_filename'] = [
        ('d', 'v', 1, ('v', 'Texture$78$set_alpha_filename', 'pp'), ['Filename const&']),
    ]
    c.ct['set_alpha_fullpath'] = [
        ('d', 'v', 1, ('v', 'Texture$86$set_alpha_fullpath', 'pp'), ['Filename const&']),
    ]
    c.ct['set_anisotropic_degree'] = [
        ('d', 'v', 1, ('v', 'Texture$119$set_anisotropic_degree', 'pi'), ['int']),
    ]
    c.ct['set_auto_texture_scale'] = [
        ('d', 'v', 1, ('v', 'Texture$197$set_auto_texture_scale', 'pp'), ['AutoTextureScale']),
    ]
    c.ct['set_aux_data'] = [
        ('d', 'v', 2, ('v', 'Texture$207$set_aux_data', 'psp'), ['std::string const&', 'TypedReferenceCount*']),
    ]
    c.ct['set_border_color'] = [
        ('d', 'v', 1, ('v', 'Texture$121$set_border_color', 'pp'), ['LColor const&']),
    ]
    c.ct['set_clear_color'] = [
        ('d', 'v', 1, ('v', 'Texture$28$set_clear_color', 'pp'), ['LColor const&']),
    ]
    c.ct['set_component_type'] = [
        ('d', 'v', 1, ('v', 'Texture$104$set_component_type', 'pp'), ['Texture::ComponentType']),
    ]
    c.ct['set_compression'] = [
        ('d', 'v', 1, ('v', 'Texture$124$set_compression', 'pp'), ['Texture::CompressionMode']),
    ]
    c.ct['set_default_sampler'] = [
        ('d', 'v', 1, ('v', 'Texture$128$set_default_sampler', 'pp'), ['SamplerState const&']),
    ]
    c.ct['set_filename'] = [
        ('d', 'v', 1, ('v', 'Texture$74$set_filename', 'pp'), ['Filename const&']),
    ]
    c.ct['set_format'] = [
        ('d', 'v', 1, ('v', 'Texture$102$set_format', 'pp'), ['Texture::Format']),
    ]
    c.ct['set_fullpath'] = [
        ('d', 'v', 1, ('v', 'Texture$82$set_fullpath', 'pp'), ['Filename const&']),
    ]
    c.ct['set_keep_ram_image'] = [
        ('d', 'v', 1, ('v', 'Texture$153$set_keep_ram_image', 'pB'), ['bool']),
    ]
    c.ct['set_loaded_from_image'] = [
        ('d', 'v', 1, ('v', 'Texture$230$set_loaded_from_image', 'pB'), ['bool']),
        ('d', 'v', 0, ('v', 'Texture$231$set_loaded_from_image', 'p'), []),
    ]
    c.ct['set_loaded_from_txo'] = [
        ('d', 'v', 1, ('v', 'Texture$233$set_loaded_from_txo', 'pB'), ['bool']),
        ('d', 'v', 0, ('v', 'Texture$234$set_loaded_from_txo', 'p'), []),
    ]
    c.ct['set_magfilter'] = [
        ('d', 'v', 1, ('v', 'Texture$116$set_magfilter', 'pp'), ['Texture::FilterType']),
    ]
    c.ct['set_match_framebuffer_format'] = [
        ('d', 'v', 1, ('v', 'Texture$237$set_match_framebuffer_format', 'pB'), ['bool']),
    ]
    c.ct['set_minfilter'] = [
        ('d', 'v', 1, ('v', 'Texture$113$set_minfilter', 'pp'), ['Texture::FilterType']),
    ]
    c.ct['set_num_views'] = [
        ('d', 'v', 1, ('v', 'Texture$95$set_num_views', 'pi'), ['int']),
    ]
    c.ct['set_orig_file_size'] = [
        ('d', 'v', 3, ('v', 'Texture$228$set_orig_file_size', 'piii'), ['int', 'int', 'int']),
        ('d', 'v', 2, ('v', 'Texture$229$set_orig_file_size', 'pii'), ['int', 'int']),
    ]
    c.ct['set_pad_size'] = [
        ('d', 'v', 3, ('v', 'Texture$217$set_pad_size', 'piii'), ['int', 'int', 'int']),
        ('d', 'v', 2, ('v', 'Texture$218$set_pad_size', 'pii'), ['int', 'int']),
        ('d', 'v', 1, ('v', 'Texture$219$set_pad_size', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'Texture$220$set_pad_size', 'p'), []),
    ]
    c.ct['set_post_load_store_cache'] = [
        ('d', 'v', 1, ('v', 'Texture$239$set_post_load_store_cache', 'pB'), ['bool']),
    ]
    c.ct['set_quality_level'] = [
        ('d', 'v', 1, ('v', 'Texture$132$set_quality_level', 'pp'), ['Texture::QualityLevel']),
    ]
    c.ct['set_ram_mipmap_image'] = [
        ('d', 'v', 3, ('v', 'Texture$176$set_ram_mipmap_image', 'pipl'), ['int', 'CPTA_uchar', 'std::size_t']),
        ('d', 'v', 2, ('v', 'Texture$177$set_ram_mipmap_image', 'pip'), ['int', 'CPTA_uchar']),
    ]
    c.ct['set_ram_mipmap_pointer_from_int'] = [
        ('d', 'v', 3, ('v', 'Texture$175$set_ram_mipmap_pointer_from_int', 'ppii'), ['long long int', 'int', 'int']),
    ]
    c.ct['set_render_to_texture'] = [
        ('d', 'v', 1, ('v', 'Texture$126$set_render_to_texture', 'pB'), ['bool']),
    ]
    c.ct['set_simple_ram_image'] = [
        ('d', 'v', 3, ('v', 'Texture$186$set_simple_ram_image', 'ppii'), ['CPTA_uchar', 'int', 'int']),
    ]
    c.ct['set_size_padded'] = [
        ('d', 'v', 3, ('v', 'Texture$221$set_size_padded', 'piii'), ['int', 'int', 'int']),
        ('d', 'v', 2, ('v', 'Texture$222$set_size_padded', 'pii'), ['int', 'int']),
        ('d', 'v', 1, ('v', 'Texture$223$set_size_padded', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'Texture$224$set_size_padded', 'p'), []),
    ]
    c.ct['set_wrap_u'] = [
        ('d', 'v', 1, ('v', 'Texture$106$set_wrap_u', 'pp'), ['Texture::WrapMode']),
    ]
    c.ct['set_wrap_v'] = [
        ('d', 'v', 1, ('v', 'Texture$108$set_wrap_v', 'pp'), ['Texture::WrapMode']),
    ]
    c.ct['set_wrap_w'] = [
        ('d', 'v', 1, ('v', 'Texture$110$set_wrap_w', 'pp'), ['Texture::WrapMode']),
    ]
    c.ct['set_x_size'] = [
        ('d', 'v', 1, ('v', 'Texture$89$set_x_size', 'pi'), ['int']),
    ]
    c.ct['set_y_size'] = [
        ('d', 'v', 1, ('v', 'Texture$91$set_y_size', 'pi'), ['int']),
    ]
    c.ct['set_z_size'] = [
        ('d', 'v', 1, ('v', 'Texture$93$set_z_size', 'pi'), ['int']),
    ]
    c.ct['setup_1d_texture'] = [
        ('d', 'v', 0, ('v', 'Texture$8$setup_1d_texture', 'p'), []),
        ('d', 'v', 3, ('v', 'Texture$9$setup_1d_texture', 'pipp'), ['int', 'Texture::ComponentType', 'Texture::Format']),
    ]
    c.ct['setup_2d_texture'] = [
        ('d', 'v', 0, ('v', 'Texture$10$setup_2d_texture', 'p'), []),
        ('d', 'v', 4, ('v', 'Texture$11$setup_2d_texture', 'piipp'), ['int', 'int', 'Texture::ComponentType', 'Texture::Format']),
    ]
    c.ct['setup_2d_texture_array'] = [
        ('d', 'v', 1, ('v', 'Texture$17$setup_2d_texture_array', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'Texture$18$setup_2d_texture_array', 'p'), []),
        ('d', 'v', 5, ('v', 'Texture$19$setup_2d_texture_array', 'piiipp'), ['int', 'int', 'int', 'Texture::ComponentType', 'Texture::Format']),
    ]
    c.ct['setup_3d_texture'] = [
        ('d', 'v', 1, ('v', 'Texture$12$setup_3d_texture', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'Texture$13$setup_3d_texture', 'p'), []),
        ('d', 'v', 5, ('v', 'Texture$14$setup_3d_texture', 'piiipp'), ['int', 'int', 'int', 'Texture::ComponentType', 'Texture::Format']),
    ]
    c.ct['setup_buffer_texture'] = [
        ('d', 'v', 4, ('v', 'Texture$22$setup_buffer_texture', 'pippp'), ['int', 'Texture::ComponentType', 'Texture::Format', 'GeomEnums::UsageHint']),
    ]
    c.ct['setup_cube_map'] = [
        ('d', 'v', 0, ('v', 'Texture$15$setup_cube_map', 'p'), []),
        ('d', 'v', 3, ('v', 'Texture$16$setup_cube_map', 'pipp'), ['int', 'Texture::ComponentType', 'Texture::Format']),
    ]
    c.ct['setup_cube_map_array'] = [
        ('d', 'v', 1, ('v', 'Texture$20$setup_cube_map_array', 'pi'), ['int']),
        ('d', 'v', 4, ('v', 'Texture$21$setup_cube_map_array', 'piipp'), ['int', 'int', 'Texture::ComponentType', 'Texture::Format']),
    ]
    c.ct['setup_texture'] = [
        ('d', 'v', 6, ('v', 'Texture$7$setup_texture', 'ppiiipp'), ['Texture::TextureType', 'int', 'int', 'int', 'Texture::ComponentType', 'Texture::Format']),
    ]
    c.ct['store'] = [
        ('d', 'B', 1, ('B', 'Texture$66$store', 'pp'), ['PNMImage&']),
        ('d', 'B', 3, ('B', 'Texture$67$store', 'ppii'), ['PNMImage&', 'int', 'int']),
        ('d', 'B', 1, ('B', 'Texture$68$store', 'pp'), ['PfmFile&']),
        ('d', 'B', 3, ('B', 'Texture$69$store', 'ppii'), ['PfmFile&', 'int', 'int']),
    ]
    c.ct['texture_uploaded'] = [
        ('d', 'v', 0, ('v', 'Texture$257$texture_uploaded', 'p'), []),
    ]
    c.ct['uncompress_ram_image'] = [
        ('d', 'B', 0, ('B', 'Texture$160$uncompress_ram_image', 'p'), []),
    ]
    c.ct['upcast_to_Namable'] = [
        ('d', 48, 0, ('p', 'Texture$2$upcast_to_Namable', 'p'), []),
    ]
    c.ct['upcast_to_TypedWritableReferenceCount'] = [
        ('d', 63, 0, ('p', 'Texture$1$upcast_to_TypedWritableReferenceCount', 'p'), []),
    ]
    c.ct['uses_mipmaps'] = [
        ('d', 'B', 0, ('B', 'Texture$129$uses_mipmaps', 'p'), []),
    ]
    c.ct['was_image_modified'] = [
        ('d', 'B', 1, ('B', 'Texture$200$was_image_modified', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['write'] = [
        ('d', 'B', 1, ('B', 'Texture$40$write', 'pp'), ['Filename const&']),
        ('d', 'B', 5, ('B', 'Texture$41$write', 'ppiiBB'), ['Filename const&', 'int', 'int', 'bool', 'bool']),
        ('d', 'v', 2, ('v', 'Texture$42$write', 'ppi'), ['std::ostream&', 'int']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'Texture$268$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]
    c.ct['write_txo'] = [
        ('d', 'B', 2, ('B', 'Texture$47$write_txo', 'pps'), ['std::ostream&', 'std::string const&']),
        ('d', 'B', 1, ('B', 'Texture$48$write_txo', 'pp'), ['std::ostream&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(Texture, attr, self)

Texture.c.link(Texture)



class GeomVertexFormat(TypedWritableReferenceCount, GeomEnums):
    __bases__ = tuple([TypedWritableReferenceCount, GeomEnums])
    c = cxx.cstructs()
    c.register("GeomVertexFormat", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 65, 0, ('p', 'GeomVertexFormat$3$GeomVertexFormat', ''), []),
        ('s', 65, 1, ('p', 'GeomVertexFormat$4$GeomVertexFormat', 'p'), ['GeomVertexArrayFormat const*']),
        ('s', 65, 1, ('p', 'GeomVertexFormat$5$GeomVertexFormat', 'p'), ['GeomVertexFormat const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'GeomVertexFormat$71$get_class_type', ''), []),
    ]
    c.ct['get_empty'] = [
        ('s', 65, 0, ('p', 'GeomVertexFormat$49$get_empty', ''), []),
    ]
    c.ct['get_v3'] = [
        ('s', 65, 0, ('p', 'GeomVertexFormat$50$get_v3', ''), []),
    ]
    c.ct['get_v3c4'] = [
        ('s', 65, 0, ('p', 'GeomVertexFormat$58$get_v3c4', ''), []),
    ]
    c.ct['get_v3c4t2'] = [
        ('s', 65, 0, ('p', 'GeomVertexFormat$59$get_v3c4t2', ''), []),
    ]
    c.ct['get_v3cp'] = [
        ('s', 65, 0, ('p', 'GeomVertexFormat$54$get_v3cp', ''), []),
    ]
    c.ct['get_v3cpt2'] = [
        ('s', 65, 0, ('p', 'GeomVertexFormat$55$get_v3cpt2', ''), []),
    ]
    c.ct['get_v3n3'] = [
        ('s', 65, 0, ('p', 'GeomVertexFormat$51$get_v3n3', ''), []),
    ]
    c.ct['get_v3n3c4'] = [
        ('s', 65, 0, ('p', 'GeomVertexFormat$60$get_v3n3c4', ''), []),
    ]
    c.ct['get_v3n3c4t2'] = [
        ('s', 65, 0, ('p', 'GeomVertexFormat$61$get_v3n3c4t2', ''), []),
    ]
    c.ct['get_v3n3cp'] = [
        ('s', 65, 0, ('p', 'GeomVertexFormat$56$get_v3n3cp', ''), []),
    ]
    c.ct['get_v3n3cpt2'] = [
        ('s', 65, 0, ('p', 'GeomVertexFormat$57$get_v3n3cpt2', ''), []),
    ]
    c.ct['get_v3n3t2'] = [
        ('s', 65, 0, ('p', 'GeomVertexFormat$53$get_v3n3t2', ''), []),
    ]
    c.ct['get_v3t2'] = [
        ('s', 65, 0, ('p', 'GeomVertexFormat$52$get_v3t2', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'GeomVertexFormat$72$init_type', ''), []),
    ]
    c.ct['register_format'] = [
        ('s', 65, 1, ('p', 'GeomVertexFormat$8$register_format', 'p'), ['GeomVertexArrayFormat const*']),
        ('s', 65, 1, ('p', 'GeomVertexFormat$9$register_format', 'p'), ['GeomVertexFormat const*']),
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
        ('d', 'l', 1, ('l', 'GeomVertexFormat$19$add_array', 'pp'), ['GeomVertexArrayFormat const*']),
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
        ('d', 66, 1, ('p', 'GeomVertexFormat$15$get_array', 'pl'), ['std::size_t']),
    ]
    c.ct['get_array_with'] = [
        ('d', 'i', 1, ('i', 'GeomVertexFormat$24$get_array_with', 'ps'), ['InternalName const*']),
        ('d', 'i', 1, ('i', 'GeomVertexFormat$25$get_array_with', 'pl'), ['std::size_t']),
    ]
    c.ct['get_color_array_index'] = [
        ('d', 'i', 0, ('i', 'GeomVertexFormat$66$get_color_array_index', 'p'), []),
    ]
    c.ct['get_color_column'] = [
        ('d', 28, 0, ('p', 'GeomVertexFormat$67$get_color_column', 'p'), []),
    ]
    c.ct['get_column'] = [
        ('d', 28, 1, ('p', 'GeomVertexFormat$26$get_column', 'ps'), ['InternalName const*']),
        ('d', 28, 1, ('p', 'GeomVertexFormat$27$get_column', 'pl'), ['std::size_t']),
    ]
    c.ct['get_column_name'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat$29$get_column_name', 'pl'), ['std::size_t']),
    ]
    c.ct['get_morph_base'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat$43$get_morph_base', 'pl'), ['std::size_t']),
    ]
    c.ct['get_morph_delta'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat$44$get_morph_delta', 'pl'), ['std::size_t']),
    ]
    c.ct['get_morph_slider'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat$42$get_morph_slider', 'pl'), ['std::size_t']),
    ]
    c.ct['get_normal_array_index'] = [
        ('d', 'i', 0, ('i', 'GeomVertexFormat$64$get_normal_array_index', 'p'), []),
    ]
    c.ct['get_normal_column'] = [
        ('d', 28, 0, ('p', 'GeomVertexFormat$65$get_normal_column', 'p'), []),
    ]
    c.ct['get_num_arrays'] = [
        ('d', 'l', 0, ('l', 'GeomVertexFormat$14$get_num_arrays', 'p'), []),
    ]
    c.ct['get_num_columns'] = [
        ('d', 'l', 0, ('l', 'GeomVertexFormat$23$get_num_columns', 'p'), []),
    ]
    c.ct['get_num_morphs'] = [
        ('d', 'l', 0, ('l', 'GeomVertexFormat$41$get_num_morphs', 'p'), []),
    ]
    c.ct['get_num_points'] = [
        ('d', 'l', 0, ('l', 'GeomVertexFormat$35$get_num_points', 'p'), []),
    ]
    c.ct['get_num_texcoords'] = [
        ('d', 'l', 0, ('l', 'GeomVertexFormat$39$get_num_texcoords', 'p'), []),
    ]
    c.ct['get_num_vectors'] = [
        ('d', 'l', 0, ('l', 'GeomVertexFormat$37$get_num_vectors', 'p'), []),
    ]
    c.ct['get_point'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat$36$get_point', 'pl'), ['std::size_t']),
    ]
    c.ct['get_post_animated_format'] = [
        ('d', 65, 0, ('p', 'GeomVertexFormat$12$get_post_animated_format', 'p'), []),
    ]
    c.ct['get_texcoord'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat$40$get_texcoord', 'pl'), ['std::size_t']),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'GeomVertexFormat$73$get_type', 'p'), []),
    ]
    c.ct['get_union_format'] = [
        ('d', 65, 1, ('p', 'GeomVertexFormat$13$get_union_format', 'pp'), ['GeomVertexFormat const*']),
    ]
    c.ct['get_vector'] = [
        ('d', 's', 1, ('s', 'GeomVertexFormat$38$get_vector', 'pl'), ['std::size_t']),
    ]
    c.ct['get_vertex_array_index'] = [
        ('d', 'i', 0, ('i', 'GeomVertexFormat$62$get_vertex_array_index', 'p'), []),
    ]
    c.ct['get_vertex_column'] = [
        ('d', 28, 0, ('p', 'GeomVertexFormat$63$get_vertex_column', 'p'), []),
    ]
    c.ct['has_column'] = [
        ('d', 'B', 1, ('B', 'GeomVertexFormat$28$has_column', 'ps'), ['InternalName const*']),
    ]
    c.ct['insert_array'] = [
        ('d', 'v', 2, ('v', 'GeomVertexFormat$20$insert_array', 'plp'), ['std::size_t', 'GeomVertexArrayFormat const*']),
    ]
    c.ct['is_registered'] = [
        ('d', 'B', 0, ('B', 'GeomVertexFormat$7$is_registered', 'p'), []),
    ]
    c.ct['maybe_align_columns_for_animation'] = [
        ('d', 'v', 0, ('v', 'GeomVertexFormat$34$maybe_align_columns_for_animation', 'p'), []),
    ]
    c.ct['modify_array'] = [
        ('d', 66, 1, ('p', 'GeomVertexFormat$16$modify_array', 'pl'), ['std::size_t']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'GeomVertexFormat$45$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['pack_columns'] = [
        ('d', 'v', 0, ('v', 'GeomVertexFormat$32$pack_columns', 'p'), []),
    ]
    c.ct['remove_array'] = [
        ('d', 'v', 1, ('v', 'GeomVertexFormat$18$remove_array', 'pl'), ['std::size_t']),
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
        ('d', 'v', 2, ('v', 'GeomVertexFormat$17$set_array', 'plp'), ['std::size_t', 'GeomVertexArrayFormat const*']),
    ]
    c.ct['unref'] = [
        ('d', 'B', 0, ('B', 'GeomVertexFormat$6$unref', 'p'), []),
    ]
    c.ct['upcast_to_GeomEnums'] = [
        ('d', 5, 0, ('p', 'GeomVertexFormat$2$upcast_to_GeomEnums', 'p'), []),
    ]
    c.ct['upcast_to_TypedWritableReferenceCount'] = [
        ('d', 63, 0, ('p', 'GeomVertexFormat$1$upcast_to_TypedWritableReferenceCount', 'p'), []),
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



class GeomVertexArrayFormat(TypedWritableReferenceCount, GeomEnums):
    __bases__ = tuple([TypedWritableReferenceCount, GeomEnums])
    c = cxx.cstructs()
    c.register("GeomVertexArrayFormat", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 66, 0, ('p', 'GeomVertexArrayFormat$3$GeomVertexArrayFormat', ''), []),
        ('s', 66, 4, ('p', 'GeomVertexArrayFormat$4$GeomVertexArrayFormat', 'sipp'), ['CPT_InternalName', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents']),
        ('s', 66, 8, ('p', 'GeomVertexArrayFormat$5$GeomVertexArrayFormat', 'sippsipp'), ['CPT_InternalName', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents', 'CPT_InternalName', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents']),
        ('s', 66, 12, ('p', 'GeomVertexArrayFormat$6$GeomVertexArrayFormat', 'sippsippsipp'), ['CPT_InternalName', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents', 'CPT_InternalName', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents', 'CPT_InternalName', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents']),
        ('s', 66, 16, ('p', 'GeomVertexArrayFormat$7$GeomVertexArrayFormat', 'sippsippsippsipp'), ['CPT_InternalName', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents', 'CPT_InternalName', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents', 'CPT_InternalName', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents', 'CPT_InternalName', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents']),
        ('s', 66, 1, ('p', 'GeomVertexArrayFormat$8$GeomVertexArrayFormat', 'p'), ['GeomVertexArrayFormat const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'GeomVertexArrayFormat$44$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'GeomVertexArrayFormat$45$init_type', ''), []),
    ]
    c.ct['register_format'] = [
        ('s', 66, 1, ('p', 'GeomVertexArrayFormat$11$register_format', 'p'), ['GeomVertexArrayFormat const*']),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'GeomVertexArrayFormat$41$register_with_read_factory', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(GeomVertexArrayFormat, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(GeomVertexArrayFormat, 'init_type', None) )(*args,**kw)

    @classmethod
    def register_format(cls, *args,**kw):
        return ( cls.c.get('register_format', None) or cls.c.call(GeomVertexArrayFormat, 'register_format', None) )(*args,**kw)

    @classmethod
    def register_with_read_factory(cls, *args,**kw):
        return ( cls.c.get('register_with_read_factory', None) or cls.c.call(GeomVertexArrayFormat, 'register_with_read_factory', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_column'] = [
        ('d', 'i', 6, ('i', 'GeomVertexArrayFormat$19$add_column', 'psippii'), ['CPT_InternalName', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents', 'int', 'int']),
        ('d', 'i', 5, ('i', 'GeomVertexArrayFormat$20$add_column', 'psippi'), ['CPT_InternalName', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents', 'int']),
        ('d', 'i', 4, ('i', 'GeomVertexArrayFormat$21$add_column', 'psipp'), ['CPT_InternalName', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents']),
        ('d', 'i', 1, ('i', 'GeomVertexArrayFormat$22$add_column', 'pp'), ['GeomVertexColumn const&']),
    ]
    c.ct['align_columns_for_animation'] = [
        ('d', 'v', 0, ('v', 'GeomVertexArrayFormat$26$align_columns_for_animation', 'p'), []),
    ]
    c.ct['clear_columns'] = [
        ('d', 'v', 0, ('v', 'GeomVertexArrayFormat$24$clear_columns', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'GeomVertexArrayFormat$40$compare_to', 'pp'), ['GeomVertexArrayFormat const&']),
    ]
    c.ct['count_unused_space'] = [
        ('d', 'i', 0, ('i', 'GeomVertexArrayFormat$33$count_unused_space', 'p'), []),
    ]
    c.ct['finalize'] = [
        ('d', 'v', 1, ('v', 'GeomVertexArrayFormat$43$finalize', 'pp'), ['BamReader*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'GeomVertexArrayFormat$47$force_init_type', 'p'), []),
    ]
    c.ct['get_column'] = [
        ('d', 28, 1, ('p', 'GeomVertexArrayFormat$28$get_column', 'ps'), ['InternalName const*']),
        ('d', 28, 1, ('p', 'GeomVertexArrayFormat$29$get_column', 'pi'), ['int']),
        ('d', 28, 2, ('p', 'GeomVertexArrayFormat$30$get_column', 'pii'), ['int', 'int']),
    ]
    c.ct['get_divisor'] = [
        ('d', 'i', 0, ('i', 'GeomVertexArrayFormat$16$get_divisor', 'p'), []),
    ]
    c.ct['get_format_string'] = [
        ('d', 's', 1, ('s', 'GeomVertexArrayFormat$38$get_format_string', 'pB'), ['bool']),
        ('d', 's', 0, ('s', 'GeomVertexArrayFormat$39$get_format_string', 'p'), []),
    ]
    c.ct['get_num_columns'] = [
        ('d', 'i', 0, ('i', 'GeomVertexArrayFormat$27$get_num_columns', 'p'), []),
    ]
    c.ct['get_pad_to'] = [
        ('d', 'i', 0, ('i', 'GeomVertexArrayFormat$14$get_pad_to', 'p'), []),
    ]
    c.ct['get_stride'] = [
        ('d', 'i', 0, ('i', 'GeomVertexArrayFormat$12$get_stride', 'p'), []),
    ]
    c.ct['get_total_bytes'] = [
        ('d', 'i', 0, ('i', 'GeomVertexArrayFormat$18$get_total_bytes', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'GeomVertexArrayFormat$46$get_type', 'p'), []),
    ]
    c.ct['has_column'] = [
        ('d', 'B', 1, ('B', 'GeomVertexArrayFormat$31$has_column', 'ps'), ['InternalName const*']),
    ]
    c.ct['is_data_subset_of'] = [
        ('d', 'B', 1, ('B', 'GeomVertexArrayFormat$32$is_data_subset_of', 'pp'), ['GeomVertexArrayFormat const&']),
    ]
    c.ct['is_registered'] = [
        ('d', 'B', 0, ('B', 'GeomVertexArrayFormat$10$is_registered', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'GeomVertexArrayFormat$34$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['pack_columns'] = [
        ('d', 'v', 0, ('v', 'GeomVertexArrayFormat$25$pack_columns', 'p'), []),
    ]
    c.ct['remove_column'] = [
        ('d', 'v', 1, ('v', 'GeomVertexArrayFormat$23$remove_column', 'ps'), ['InternalName const*']),
    ]
    c.ct['set_divisor'] = [
        ('d', 'v', 1, ('v', 'GeomVertexArrayFormat$17$set_divisor', 'pi'), ['int']),
    ]
    c.ct['set_pad_to'] = [
        ('d', 'v', 1, ('v', 'GeomVertexArrayFormat$15$set_pad_to', 'pi'), ['int']),
    ]
    c.ct['set_stride'] = [
        ('d', 'v', 1, ('v', 'GeomVertexArrayFormat$13$set_stride', 'pi'), ['int']),
    ]
    c.ct['unref'] = [
        ('d', 'B', 0, ('B', 'GeomVertexArrayFormat$9$unref', 'p'), []),
    ]
    c.ct['upcast_to_GeomEnums'] = [
        ('d', 5, 0, ('p', 'GeomVertexArrayFormat$2$upcast_to_GeomEnums', 'p'), []),
    ]
    c.ct['upcast_to_TypedWritableReferenceCount'] = [
        ('d', 63, 0, ('p', 'GeomVertexArrayFormat$1$upcast_to_TypedWritableReferenceCount', 'p'), []),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'GeomVertexArrayFormat$35$write', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'v', 1, ('v', 'GeomVertexArrayFormat$36$write', 'pp'), ['std::ostream&']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'GeomVertexArrayFormat$42$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]
    c.ct['write_with_data'] = [
        ('d', 'v', 3, ('v', 'GeomVertexArrayFormat$37$write_with_data', 'ppip'), ['std::ostream&', 'int', 'GeomVertexArrayData const*']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomVertexArrayFormat, attr, self)

GeomVertexArrayFormat.c.link(GeomVertexArrayFormat)



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
        ('s', 67, 1, ('p', 'WindowFramework$52$WindowFramework', 'p'), ['WindowFramework const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'WindowFramework$48$get_class_type', ''), []),
    ]
    c.ct['get_shuttle_controls_font'] = [
        ('s', 59, 0, ('p', 'WindowFramework$46$get_shuttle_controls_font', ''), []),
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
        ('d', 17, 0, ('p', 'WindowFramework$11$get_aspect_2d', 'p'), []),
    ]
    c.ct['get_background_type'] = [
        ('d', 'p', 0, ('p', 'WindowFramework$45$get_background_type', 'p'), []),
    ]
    c.ct['get_button_thrower'] = [
        ('d', 17, 0, ('p', 'WindowFramework$14$get_button_thrower', 'p'), []),
    ]
    c.ct['get_camera'] = [
        ('d', 88, 1, ('p', 'WindowFramework$6$get_camera', 'pi'), ['int']),
    ]
    c.ct['get_camera_group'] = [
        ('d', 17, 0, ('p', 'WindowFramework$4$get_camera_group', 'p'), []),
    ]
    c.ct['get_display_region_2d'] = [
        ('d', 61, 0, ('p', 'WindowFramework$7$get_display_region_2d', 'p'), []),
    ]
    c.ct['get_display_region_3d'] = [
        ('d', 61, 0, ('p', 'WindowFramework$8$get_display_region_3d', 'p'), []),
    ]
    c.ct['get_graphics_output'] = [
        ('d', 74, 0, ('p', 'WindowFramework$3$get_graphics_output', 'p'), []),
    ]
    c.ct['get_graphics_window'] = [
        ('d', 75, 0, ('p', 'WindowFramework$2$get_graphics_window', 'p'), []),
    ]
    c.ct['get_lighting'] = [
        ('d', 'B', 0, ('B', 'WindowFramework$43$get_lighting', 'p'), []),
    ]
    c.ct['get_mouse'] = [
        ('d', 17, 0, ('p', 'WindowFramework$13$get_mouse', 'p'), []),
    ]
    c.ct['get_num_cameras'] = [
        ('d', 'i', 0, ('i', 'WindowFramework$5$get_num_cameras', 'p'), []),
    ]
    c.ct['get_one_sided_reverse'] = [
        ('d', 'B', 0, ('B', 'WindowFramework$42$get_one_sided_reverse', 'p'), []),
    ]
    c.ct['get_panda_framework'] = [
        ('d', 19, 0, ('p', 'WindowFramework$1$get_panda_framework', 'p'), []),
    ]
    c.ct['get_perpixel'] = [
        ('d', 'B', 0, ('B', 'WindowFramework$44$get_perpixel', 'p'), []),
    ]
    c.ct['get_pixel_2d'] = [
        ('d', 17, 0, ('p', 'WindowFramework$12$get_pixel_2d', 'p'), []),
    ]
    c.ct['get_render'] = [
        ('d', 17, 0, ('p', 'WindowFramework$9$get_render', 'p'), []),
    ]
    c.ct['get_render_2d'] = [
        ('d', 17, 0, ('p', 'WindowFramework$10$get_render_2d', 'p'), []),
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
        ('d', 17, 1, ('p', 'WindowFramework$20$load_default_model', 'pp'), ['NodePath const&']),
    ]
    c.ct['load_model'] = [
        ('d', 17, 2, ('p', 'WindowFramework$19$load_model', 'ppp'), ['NodePath const&', 'Filename']),
    ]
    c.ct['load_models'] = [
        ('d', 'B', 2, ('B', 'WindowFramework$18$load_models', 'ppp'), ['NodePath const&', 'pvector< Filename > const&']),
    ]
    c.ct['loop_animations'] = [
        ('d', 'v', 1, ('v', 'WindowFramework$21$loop_animations', 'pi'), ['int']),
        ('d', 'v', 0, ('v', 'WindowFramework$22$loop_animations', 'p'), []),
    ]
    c.ct['make_camera'] = [
        ('d', 17, 0, ('p', 'WindowFramework$47$make_camera', 'p'), []),
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
        ('d', 67, 1, ('p', 'WindowFramework$28$split_window', 'pp'), ['WindowFramework::SplitType']),
        ('d', 67, 0, ('p', 'WindowFramework$29$split_window', 'p'), []),
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



class TransformTable(TypedWritableReferenceCount):
    __bases__ = tuple([TypedWritableReferenceCount])
    c = cxx.cstructs()
    c.register("TransformTable", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 68, 0, ('p', 'TransformTable$1$TransformTable', ''), []),
        ('s', 68, 1, ('p', 'TransformTable$2$TransformTable', 'p'), ['TransformTable const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'TransformTable$16$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'TransformTable$17$init_type', ''), []),
    ]
    c.ct['register_table'] = [
        ('s', 68, 1, ('p', 'TransformTable$4$register_table', 'p'), ['TransformTable const*']),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'TransformTable$14$register_with_read_factory', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(TransformTable, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(TransformTable, 'init_type', None) )(*args,**kw)

    @classmethod
    def register_table(cls, *args,**kw):
        return ( cls.c.get('register_table', None) or cls.c.call(TransformTable, 'register_table', None) )(*args,**kw)

    @classmethod
    def register_with_read_factory(cls, *args,**kw):
        return ( cls.c.get('register_with_read_factory', None) or cls.c.call(TransformTable, 'register_with_read_factory', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_transform'] = [
        ('d', 'l', 1, ('l', 'TransformTable$12$add_transform', 'pp'), ['VertexTransform const*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'TransformTable$19$force_init_type', 'p'), []),
    ]
    c.ct['get_modified'] = [
        ('d', 26, 1, ('p', 'TransformTable$7$get_modified', 'pp'), ['Thread*']),
        ('d', 26, 0, ('p', 'TransformTable$8$get_modified', 'p'), []),
    ]
    c.ct['get_num_transforms'] = [
        ('d', 'l', 0, ('l', 'TransformTable$5$get_num_transforms', 'p'), []),
    ]
    c.ct['get_transform'] = [
        ('d', 'p', 1, ('p', 'TransformTable$6$get_transform', 'pl'), ['std::size_t']),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'TransformTable$18$get_type', 'p'), []),
    ]
    c.ct['insert_transform'] = [
        ('d', 'v', 2, ('v', 'TransformTable$10$insert_transform', 'plp'), ['std::size_t', 'VertexTransform const*']),
    ]
    c.ct['is_registered'] = [
        ('d', 'B', 0, ('B', 'TransformTable$3$is_registered', 'p'), []),
    ]
    c.ct['remove_transform'] = [
        ('d', 'v', 1, ('v', 'TransformTable$11$remove_transform', 'pl'), ['std::size_t']),
    ]
    c.ct['set_transform'] = [
        ('d', 'v', 2, ('v', 'TransformTable$9$set_transform', 'plp'), ['std::size_t', 'VertexTransform const*']),
    ]
    c.ct['write'] = [
        ('d', 'v', 1, ('v', 'TransformTable$13$write', 'pp'), ['std::ostream&']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'TransformTable$15$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TransformTable, attr, self)

TransformTable.c.link(TransformTable)



class Shader(TypedWritableReferenceCount):
    __bases__ = tuple([TypedWritableReferenceCount])
    c = cxx.cstructs()
    c.register("Shader", "upanda3d", """libupanda3d_c.so""")

    # enum AutoShaderBit

    bit_AutoShaderGloss = const(2)
    bit_AutoShaderGlow = const(1)
    bit_AutoShaderNormal = const(0)
    bit_AutoShaderRamp = const(3)
    bit_AutoShaderShadow = const(4)


    # enum ShaderArgClass

    SAC_array = const(4)
    SAC_matrix = const(2)
    SAC_sampler = const(3)
    SAC_scalar = const(0)
    SAC_unknown = const(5)
    SAC_vector = const(1)


    # enum ShaderType

    ST_COUNT = const(7)
    ST_compute = const(6)
    ST_fragment = const(2)
    ST_geometry = const(3)
    ST_none = const(0)
    ST_tess_control = const(4)
    ST_tess_evaluation = const(5)
    ST_vertex = const(1)


    # enum ShaderLanguage

    SL_Cg = const(1)
    SL_GLSL = const(2)
    SL_HLSL = const(3)
    SL_SPIR_V = const(4)
    SL_none = const(0)


    # enum ShaderMatFunc

    SMF_compose = const(0)
    SMF_first = const(4)
    SMF_transform_dlight = const(1)
    SMF_transform_plight = const(2)
    SMF_transform_slight = const(3)


    # enum ShaderMatPiece

    SMP_cell13 = const(17)
    SMP_cell14 = const(16)
    SMP_cell15 = const(15)
    SMP_col0 = const(6)
    SMP_col1 = const(7)
    SMP_col2 = const(8)
    SMP_col3 = const(9)
    SMP_row0 = const(2)
    SMP_row1 = const(3)
    SMP_row2 = const(4)
    SMP_row3 = const(5)
    SMP_row3x1 = const(10)
    SMP_row3x2 = const(11)
    SMP_row3x3 = const(12)
    SMP_transpose = const(1)
    SMP_transpose3x3 = const(14)
    SMP_upper3x3 = const(13)
    SMP_whole = const(0)


    # enum ShaderBug

    SBUG_ati_draw_buffers = const(0)


    # enum ShaderArgType

    SAT_mat1x1 = const(5)
    SAT_mat1x2 = const(6)
    SAT_mat1x3 = const(7)
    SAT_mat1x4 = const(8)
    SAT_mat2x1 = const(9)
    SAT_mat2x2 = const(10)
    SAT_mat2x3 = const(11)
    SAT_mat2x4 = const(12)
    SAT_mat3x1 = const(13)
    SAT_mat3x2 = const(14)
    SAT_mat3x3 = const(15)
    SAT_mat3x4 = const(16)
    SAT_mat4x1 = const(17)
    SAT_mat4x2 = const(18)
    SAT_mat4x3 = const(19)
    SAT_mat4x4 = const(20)
    SAT_sampler1d = const(21)
    SAT_sampler2d = const(22)
    SAT_sampler2d_array = const(24)
    SAT_sampler3d = const(23)
    SAT_sampler_buffer = const(26)
    SAT_sampler_cube = const(25)
    SAT_sampler_cube_array = const(27)
    SAT_scalar = const(0)
    SAT_unknown = const(28)
    SAT_vec1 = const(1)
    SAT_vec2 = const(2)
    SAT_vec3 = const(3)
    SAT_vec4 = const(4)


    # enum ShaderMatInput

    SMO_INVALID = const(61)
    SMO_alight_x = const(8)
    SMO_apiclip_to_apiview = const(52)
    SMO_apiclip_to_view = const(26)
    SMO_apiclip_x_to_view = const(34)
    SMO_apiview_clipplane_i = const(48)
    SMO_apiview_to_apiclip = const(51)
    SMO_apiview_to_model = const(50)
    SMO_apiview_to_view = const(22)
    SMO_apiview_x_to_view = const(30)
    SMO_attr_color = const(6)
    SMO_attr_colorscale = const(7)
    SMO_attr_fog = const(36)
    SMO_attr_fogcolor = const(37)
    SMO_attr_material = const(5)
    SMO_attr_material2 = const(54)
    SMO_clip_to_view = const(24)
    SMO_clip_x_to_view = const(32)
    SMO_clipplane_x = const(15)
    SMO_dlight_x = const(9)
    SMO_frame_delta = const(40)
    SMO_frame_number = const(38)
    SMO_frame_time = const(39)
    SMO_identity = const(0)
    SMO_inv_texmat_i = const(53)
    SMO_light_ambient = const(43)
    SMO_light_product_i_ambient = const(45)
    SMO_light_product_i_diffuse = const(46)
    SMO_light_product_i_specular = const(47)
    SMO_light_source_i_attrib = const(44)
    SMO_light_source_i_packed = const(58)
    SMO_mat_constant_x = const(16)
    SMO_mat_constant_x_attrib = const(41)
    SMO_model_to_apiview = const(49)
    SMO_model_to_view = const(20)
    SMO_pixel_size = const(2)
    SMO_plane_x = const(14)
    SMO_plight_x = const(10)
    SMO_satten_x = const(12)
    SMO_slider_i = const(57)
    SMO_slight_x = const(11)
    SMO_tex_is_alpha_i = const(55)
    SMO_texcolor_i = const(60)
    SMO_texmat_i = const(13)
    SMO_texpad_x = const(3)
    SMO_texpix_x = const(4)
    SMO_texscale_i = const(59)
    SMO_transform_i = const(56)
    SMO_vec_constant_x = const(17)
    SMO_vec_constant_x_attrib = const(42)
    SMO_view_to_apiclip = const(27)
    SMO_view_to_apiclip_x = const(35)
    SMO_view_to_apiview = const(23)
    SMO_view_to_apiview_x = const(31)
    SMO_view_to_clip = const(25)
    SMO_view_to_clip_x = const(33)
    SMO_view_to_model = const(21)
    SMO_view_to_view_x = const(29)
    SMO_view_to_world = const(19)
    SMO_view_x_to_view = const(28)
    SMO_window_size = const(1)
    SMO_world_to_view = const(18)


    # enum AutoShaderSwitch

    AS_gloss = const(4)
    AS_glow = const(2)
    AS_normal = const(1)
    AS_ramp = const(8)
    AS_shadow = const(16)


    # enum ShaderPtrType

    SPT_double = const(1)
    SPT_float = const(0)
    SPT_int = const(2)
    SPT_uint = const(3)
    SPT_unknown = const(4)


    # enum ShaderStateDep

    SSD_NONE = const(0)
    SSD_clip_planes = const(256)
    SSD_color = const(4)
    SSD_colorscale = const(8)
    SSD_fog = const(64)
    SSD_frame = const(1024)
    SSD_general = const(1)
    SSD_light = const(128)
    SSD_material = const(16)
    SSD_projection = const(2048)
    SSD_shaderinputs = const(32)
    SSD_tex_matrix = const(512)
    SSD_texture = const(4096)
    SSD_transform = const(8194)
    SSD_view_transform = const(8192)


    # enum ShaderArgDir

    SAD_in = const(0)
    SAD_inout = const(2)
    SAD_out = const(1)
    SAD_unknown = const(3)


    # enum ShaderTexInput

    STO_INVALID = const(0)
    STO_light_i_shadow_map = const(4)
    STO_named_input = const(1)
    STO_named_stage = const(2)
    STO_stage_i = const(3)


    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 69, 1, ('p', 'Shader$60$Shader', 'p'), ['Shader const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'Shader$56$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'Shader$57$init_type', ''), []),
    ]
    c.ct['load'] = [
        ('s', 69, 2, ('p', 'Shader$1$load', 'pp'), ['Filename const&', 'Shader::ShaderLanguage']),
        ('s', 69, 1, ('p', 'Shader$2$load', 'p'), ['Filename const&']),
        ('s', 69, 6, ('p', 'Shader$3$load', 'pppppp'), ['Shader::ShaderLanguage', 'Filename const&', 'Filename const&', 'Filename const&', 'Filename const&', 'Filename const&']),
        ('s', 69, 5, ('p', 'Shader$4$load', 'ppppp'), ['Shader::ShaderLanguage', 'Filename const&', 'Filename const&', 'Filename const&', 'Filename const&']),
        ('s', 69, 4, ('p', 'Shader$5$load', 'pppp'), ['Shader::ShaderLanguage', 'Filename const&', 'Filename const&', 'Filename const&']),
        ('s', 69, 3, ('p', 'Shader$6$load', 'ppp'), ['Shader::ShaderLanguage', 'Filename const&', 'Filename const&']),
    ]
    c.ct['load_compute'] = [
        ('s', 69, 2, ('p', 'Shader$13$load_compute', 'pp'), ['Shader::ShaderLanguage', 'Filename const&']),
    ]
    c.ct['make'] = [
        ('s', 69, 6, ('p', 'Shader$7$make', 'psssss'), ['Shader::ShaderLanguage', 'std::string', 'std::string', 'std::string', 'std::string', 'std::string']),
        ('s', 69, 5, ('p', 'Shader$8$make', 'pssss'), ['Shader::ShaderLanguage', 'std::string', 'std::string', 'std::string', 'std::string']),
        ('s', 69, 4, ('p', 'Shader$9$make', 'psss'), ['Shader::ShaderLanguage', 'std::string', 'std::string', 'std::string']),
        ('s', 69, 3, ('p', 'Shader$10$make', 'pss'), ['Shader::ShaderLanguage', 'std::string', 'std::string']),
        ('s', 69, 2, ('p', 'Shader$11$make', 'sp'), ['std::string', 'Shader::ShaderLanguage']),
        ('s', 69, 1, ('p', 'Shader$12$make', 's'), ['std::string']),
    ]
    c.ct['make_compute'] = [
        ('s', 69, 2, ('p', 'Shader$14$make_compute', 'ps'), ['Shader::ShaderLanguage', 'std::string']),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'Shader$54$register_with_read_factory', ''), []),
    ]
    c.ct['set_default_caps'] = [
        ('s', 'v', 1, ('v', 'Shader$45$set_default_caps', 'p'), ['Shader::ShaderCaps const&']),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(Shader, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(Shader, 'init_type', None) )(*args,**kw)

    @classmethod
    def load(cls, *args,**kw):
        return ( cls.c.get('load', None) or cls.c.call(Shader, 'load', None) )(*args,**kw)

    @classmethod
    def load_compute(cls, *args,**kw):
        return ( cls.c.get('load_compute', None) or cls.c.call(Shader, 'load_compute', None) )(*args,**kw)

    @classmethod
    def make(cls, *args,**kw):
        return ( cls.c.get('make', None) or cls.c.call(Shader, 'make', None) )(*args,**kw)

    @classmethod
    def make_compute(cls, *args,**kw):
        return ( cls.c.get('make_compute', None) or cls.c.call(Shader, 'make_compute', None) )(*args,**kw)

    @classmethod
    def register_with_read_factory(cls, *args,**kw):
        return ( cls.c.get('register_with_read_factory', None) or cls.c.call(Shader, 'register_with_read_factory', None) )(*args,**kw)

    @classmethod
    def set_default_caps(cls, *args,**kw):
        return ( cls.c.get('set_default_caps', None) or cls.c.call(Shader, 'set_default_caps', None) )(*args,**kw)

    # instance method type calls

    c.ct['clear_parameters'] = [
        ('d', 'v', 0, ('v', 'Shader$43$clear_parameters', 'p'), []),
    ]
    c.ct['cp_dependency'] = [
        ('d', 'i', 1, ('i', 'Shader$41$cp_dependency', 'pp'), ['Shader::ShaderMatInput']),
    ]
    c.ct['cp_errchk_parameter_float'] = [
        ('d', 'B', 3, ('B', 'Shader$39$cp_errchk_parameter_float', 'ppii'), ['Shader::ShaderArgInfo&', 'int', 'int']),
    ]
    c.ct['cp_errchk_parameter_in'] = [
        ('d', 'B', 1, ('B', 'Shader$35$cp_errchk_parameter_in', 'pp'), ['Shader::ShaderArgInfo&']),
    ]
    c.ct['cp_errchk_parameter_ptr'] = [
        ('d', 'B', 1, ('B', 'Shader$36$cp_errchk_parameter_ptr', 'pp'), ['Shader::ShaderArgInfo&']),
    ]
    c.ct['cp_errchk_parameter_sampler'] = [
        ('d', 'B', 1, ('B', 'Shader$40$cp_errchk_parameter_sampler', 'pp'), ['Shader::ShaderArgInfo&']),
    ]
    c.ct['cp_errchk_parameter_uniform'] = [
        ('d', 'B', 1, ('B', 'Shader$38$cp_errchk_parameter_uniform', 'pp'), ['Shader::ShaderArgInfo&']),
    ]
    c.ct['cp_errchk_parameter_varying'] = [
        ('d', 'B', 1, ('B', 'Shader$37$cp_errchk_parameter_varying', 'pp'), ['Shader::ShaderArgInfo&']),
    ]
    c.ct['cp_errchk_parameter_words'] = [
        ('d', 'B', 2, ('B', 'Shader$34$cp_errchk_parameter_words', 'ppi'), ['Shader::ShaderArgInfo&', 'int']),
    ]
    c.ct['cp_optimize_mat_spec'] = [
        ('d', 'v', 1, ('v', 'Shader$42$cp_optimize_mat_spec', 'pp'), ['Shader::ShaderMatSpec&']),
    ]
    c.ct['cp_report_error'] = [
        ('d', 'v', 2, ('v', 'Shader$33$cp_report_error', 'pps'), ['Shader::ShaderArgInfo&', 'std::string const&']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'Shader$59$force_init_type', 'p'), []),
    ]
    c.ct['get_cache_compiled_shader'] = [
        ('d', 'B', 0, ('B', 'Shader$24$get_cache_compiled_shader', 'p'), []),
    ]
    c.ct['get_error_flag'] = [
        ('d', 'B', 0, ('B', 'Shader$20$get_error_flag', 'p'), []),
    ]
    c.ct['get_filename'] = [
        ('d', 3, 1, ('p', 'Shader$15$get_filename', 'pp'), ['Shader::ShaderType']),
        ('d', 3, 0, ('p', 'Shader$16$get_filename', 'p'), []),
    ]
    c.ct['get_filename_from_index'] = [
        ('d', 3, 2, ('p', 'Shader$53$get_filename_from_index', 'pip'), ['int', 'Shader::ShaderType']),
    ]
    c.ct['get_fullpath'] = [
        ('d', 3, 0, ('p', 'Shader$23$get_fullpath', 'p'), []),
    ]
    c.ct['get_language'] = [
        ('d', 'p', 0, ('p', 'Shader$21$get_language', 'p'), []),
    ]
    c.ct['get_mat_deps'] = [
        ('d', 'i', 0, ('i', 'Shader$50$get_mat_deps', 'p'), []),
    ]
    c.ct['get_mat_spec'] = [
        ('d', 'p', 0, ('p', 'Shader$47$get_mat_spec', 'p'), []),
    ]
    c.ct['get_ptr_spec'] = [
        ('d', 'p', 0, ('p', 'Shader$46$get_ptr_spec', 'p'), []),
    ]
    c.ct['get_tex_spec'] = [
        ('d', 'p', 0, ('p', 'Shader$48$get_tex_spec', 'p'), []),
    ]
    c.ct['get_text'] = [
        ('d', 's', 1, ('s', 'Shader$18$get_text', 'pp'), ['Shader::ShaderType']),
        ('d', 's', 0, ('s', 'Shader$19$get_text', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'Shader$58$get_type', 'p'), []),
    ]
    c.ct['get_var_spec'] = [
        ('d', 'p', 0, ('p', 'Shader$49$get_var_spec', 'p'), []),
    ]
    c.ct['has_fullpath'] = [
        ('d', 'B', 0, ('B', 'Shader$22$has_fullpath', 'p'), []),
    ]
    c.ct['is_prepared'] = [
        ('d', 'B', 1, ('B', 'Shader$27$is_prepared', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['parse_eof'] = [
        ('d', 'B', 0, ('B', 'Shader$32$parse_eof', 'p'), []),
    ]
    c.ct['parse_init'] = [
        ('d', 'v', 0, ('v', 'Shader$31$parse_init', 'p'), []),
    ]
    c.ct['prepare'] = [
        ('d', 'p', 1, ('p', 'Shader$26$prepare', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['prepare_now'] = [
        ('d', 'p', 2, ('p', 'Shader$30$prepare_now', 'ppp'), ['PreparedGraphicsObjects*', 'GraphicsStateGuardianBase*']),
    ]
    c.ct['release'] = [
        ('d', 'B', 1, ('B', 'Shader$28$release', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['release_all'] = [
        ('d', 'i', 0, ('i', 'Shader$29$release_all', 'p'), []),
    ]
    c.ct['set_cache_compiled_shader'] = [
        ('d', 'v', 1, ('v', 'Shader$25$set_cache_compiled_shader', 'pB'), ['bool']),
    ]
    c.ct['set_compiled'] = [
        ('d', 'v', 3, ('v', 'Shader$44$set_compiled', 'pIsl'), ['unsigned int', 'char const*', 'std::size_t']),
    ]
    c.ct['set_error_flag'] = [
        ('d', 'v', 1, ('v', 'Shader$52$set_error_flag', 'pB'), ['bool']),
    ]
    c.ct['set_filename'] = [
        ('d', 'v', 2, ('v', 'Shader$17$set_filename', 'ppp'), ['Shader::ShaderType', 'Filename const&']),
    ]
    c.ct['set_mat_deps'] = [
        ('d', 'v', 1, ('v', 'Shader$51$set_mat_deps', 'pi'), ['int']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'Shader$55$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(Shader, attr, self)

Shader.c.link(Shader)



class RenderEffect(TypedWritableReferenceCount):
    __bases__ = tuple([TypedWritableReferenceCount])
    c = cxx.cstructs()
    c.register("RenderEffect", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['change_this'] = [
        ('s', 55, 2, ('p', 'RenderEffect$16$change_this', 'pp'), ['TypedWritable*', 'BamReader*']),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'RenderEffect$18$get_class_type', ''), []),
    ]
    c.ct['get_num_effects'] = [
        ('s', 'i', 0, ('i', 'RenderEffect$12$get_num_effects', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'RenderEffect$19$init_type', ''), []),
    ]
    c.ct['list_effects'] = [
        ('s', 'v', 1, ('v', 'RenderEffect$13$list_effects', 'p'), ['std::ostream&']),
    ]
    c.ct['validate_effects'] = [
        ('s', 'B', 0, ('B', 'RenderEffect$14$validate_effects', ''), []),
    ]

    @classmethod
    def change_this(cls, *args,**kw):
        return ( cls.c.get('change_this', None) or cls.c.call(RenderEffect, 'change_this', None) )(*args,**kw)

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(RenderEffect, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_num_effects(cls, *args,**kw):
        return ( cls.c.get('get_num_effects', None) or cls.c.call(RenderEffect, 'get_num_effects', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(RenderEffect, 'init_type', None) )(*args,**kw)

    @classmethod
    def list_effects(cls, *args,**kw):
        return ( cls.c.get('list_effects', None) or cls.c.call(RenderEffect, 'list_effects', None) )(*args,**kw)

    @classmethod
    def validate_effects(cls, *args,**kw):
        return ( cls.c.get('validate_effects', None) or cls.c.call(RenderEffect, 'validate_effects', None) )(*args,**kw)

    # instance method type calls

    c.ct['adjust_transform'] = [
        ('d', 'v', 3, ('v', 'RenderEffect$8$adjust_transform', 'pppp'), ['ConstPointerTo< TransformState >&', 'ConstPointerTo< TransformState >&', 'PandaNode const*']),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'RenderEffect$9$compare_to', 'pp'), ['RenderEffect const&']),
    ]
    c.ct['cull_callback'] = [
        ('d', 'v', 4, ('v', 'RenderEffect$6$cull_callback', 'ppppp'), ['CullTraverser*', 'CullTraverserData&', 'ConstPointerTo< TransformState >&', 'ConstPointerTo< RenderState >&']),
    ]
    c.ct['finalize'] = [
        ('d', 'v', 1, ('v', 'RenderEffect$17$finalize', 'pp'), ['BamReader*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'RenderEffect$21$force_init_type', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'RenderEffect$20$get_type', 'p'), []),
    ]
    c.ct['has_adjust_transform'] = [
        ('d', 'B', 0, ('B', 'RenderEffect$7$has_adjust_transform', 'p'), []),
    ]
    c.ct['has_cull_callback'] = [
        ('d', 'B', 0, ('B', 'RenderEffect$5$has_cull_callback', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'RenderEffect$10$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['prepare_flatten_transform'] = [
        ('d', 78, 1, ('p', 'RenderEffect$2$prepare_flatten_transform', 'pp'), ['TransformState const*']),
    ]
    c.ct['safe_to_combine'] = [
        ('d', 'B', 0, ('B', 'RenderEffect$3$safe_to_combine', 'p'), []),
    ]
    c.ct['safe_to_transform'] = [
        ('d', 'B', 0, ('B', 'RenderEffect$1$safe_to_transform', 'p'), []),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'RenderEffect$11$write', 'ppi'), ['std::ostream&', 'int']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'RenderEffect$15$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]
    c.ct['xform'] = [
        ('d', 70, 1, ('p', 'RenderEffect$4$xform', 'pp'), ['LMatrix4 const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(RenderEffect, attr, self)

RenderEffect.c.link(RenderEffect)



class Lens(TypedWritableReferenceCount):
    __bases__ = tuple([TypedWritableReferenceCount])
    c = cxx.cstructs()
    c.register("Lens", "upanda3d", """libupanda3d_c.so""")

    # enum StereoChannel

    SC_left = const(1)
    SC_mono = const(0)
    SC_right = const(2)
    SC_stereo = const(3)


    # enum FromCorners

    FC_aspect_ratio = const(8)
    FC_camera_plane = const(2)
    FC_keystone = const(32)
    FC_off_axis = const(4)
    FC_roll = const(1)
    FC_shear = const(16)


    # ctor/dtor


    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'Lens$83$get_class_type', ''), []),
    ]
    c.ct['get_default_far'] = [
        ('s', 'f', 0, ('f', 'Lens$39$get_default_far', ''), []),
    ]
    c.ct['get_default_near'] = [
        ('s', 'f', 0, ('f', 'Lens$38$get_default_near', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'Lens$84$init_type', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(Lens, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_default_far(cls, *args,**kw):
        return ( cls.c.get('get_default_far', None) or cls.c.call(Lens, 'get_default_far', None) )(*args,**kw)

    @classmethod
    def get_default_near(cls, *args,**kw):
        return ( cls.c.get('get_default_near', None) or cls.c.call(Lens, 'get_default_near', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(Lens, 'init_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['clear'] = [
        ('d', 'v', 0, ('v', 'Lens$13$clear', 'p'), []),
    ]
    c.ct['clear_custom_film_mat'] = [
        ('d', 'v', 0, ('v', 'Lens$60$clear_custom_film_mat', 'p'), []),
    ]
    c.ct['clear_keystone'] = [
        ('d', 'v', 0, ('v', 'Lens$57$clear_keystone', 'p'), []),
    ]
    c.ct['clear_view_mat'] = [
        ('d', 'v', 0, ('v', 'Lens$54$clear_view_mat', 'p'), []),
    ]
    c.ct['extrude'] = [
        ('d', 'B', 3, ('B', 'Lens$2$extrude', 'pppp'), ['LPoint2 const&', 'LPoint3&', 'LPoint3&']),
        ('d', 'B', 3, ('B', 'Lens$3$extrude', 'pppp'), ['LPoint3 const&', 'LPoint3&', 'LPoint3&']),
    ]
    c.ct['extrude_depth'] = [
        ('d', 'B', 2, ('B', 'Lens$4$extrude_depth', 'ppp'), ['LPoint3 const&', 'LPoint3&']),
    ]
    c.ct['extrude_vec'] = [
        ('d', 'B', 2, ('B', 'Lens$5$extrude_vec', 'ppp'), ['LPoint2 const&', 'LVector3&']),
        ('d', 'B', 2, ('B', 'Lens$6$extrude_vec', 'ppp'), ['LPoint3 const&', 'LVector3&']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'Lens$82$force_init_type', 'p'), []),
    ]
    c.ct['get_aspect_ratio'] = [
        ('d', 'f', 0, ('f', 'Lens$32$get_aspect_ratio', 'p'), []),
    ]
    c.ct['get_change_event'] = [
        ('d', 's', 0, ('s', 'Lens$10$get_change_event', 'p'), []),
    ]
    c.ct['get_convergence_distance'] = [
        ('d', 'f', 0, ('f', 'Lens$51$get_convergence_distance', 'p'), []),
    ]
    c.ct['get_coordinate_system'] = [
        ('d', 'p', 0, ('p', 'Lens$12$get_coordinate_system', 'p'), []),
    ]
    c.ct['get_custom_film_mat'] = [
        ('d', 'p', 0, ('p', 'Lens$59$get_custom_film_mat', 'p'), []),
    ]
    c.ct['get_far'] = [
        ('d', 'f', 0, ('f', 'Lens$36$get_far', 'p'), []),
    ]
    c.ct['get_film_mat'] = [
        ('d', 'p', 0, ('p', 'Lens$72$get_film_mat', 'p'), []),
    ]
    c.ct['get_film_mat_inv'] = [
        ('d', 'p', 0, ('p', 'Lens$73$get_film_mat_inv', 'p'), []),
    ]
    c.ct['get_film_offset'] = [
        ('d', 39, 0, ('p', 'Lens$20$get_film_offset', 'p'), []),
    ]
    c.ct['get_film_size'] = [
        ('d', 6, 0, ('p', 'Lens$17$get_film_size', 'p'), []),
    ]
    c.ct['get_focal_length'] = [
        ('d', 'f', 0, ('f', 'Lens$22$get_focal_length', 'p'), []),
    ]
    c.ct['get_fov'] = [
        ('d', 6, 0, ('p', 'Lens$27$get_fov', 'p'), []),
    ]
    c.ct['get_hfov'] = [
        ('d', 'f', 0, ('f', 'Lens$28$get_hfov', 'p'), []),
    ]
    c.ct['get_interocular_distance'] = [
        ('d', 'f', 0, ('f', 'Lens$49$get_interocular_distance', 'p'), []),
    ]
    c.ct['get_keystone'] = [
        ('d', 6, 0, ('p', 'Lens$56$get_keystone', 'p'), []),
    ]
    c.ct['get_last_change'] = [
        ('d', 26, 0, ('p', 'Lens$79$get_last_change', 'p'), []),
    ]
    c.ct['get_lens_mat'] = [
        ('d', 'p', 0, ('p', 'Lens$74$get_lens_mat', 'p'), []),
    ]
    c.ct['get_lens_mat_inv'] = [
        ('d', 'p', 0, ('p', 'Lens$75$get_lens_mat_inv', 'p'), []),
    ]
    c.ct['get_min_fov'] = [
        ('d', 'f', 0, ('f', 'Lens$30$get_min_fov', 'p'), []),
    ]
    c.ct['get_near'] = [
        ('d', 'f', 0, ('f', 'Lens$34$get_near', 'p'), []),
    ]
    c.ct['get_nodal_point'] = [
        ('d', 33, 0, ('p', 'Lens$47$get_nodal_point', 'p'), []),
    ]
    c.ct['get_projection_mat'] = [
        ('d', 'p', 1, ('p', 'Lens$68$get_projection_mat', 'pp'), ['Lens::StereoChannel']),
        ('d', 'p', 0, ('p', 'Lens$69$get_projection_mat', 'p'), []),
    ]
    c.ct['get_projection_mat_inv'] = [
        ('d', 'p', 1, ('p', 'Lens$70$get_projection_mat_inv', 'pp'), ['Lens::StereoChannel']),
        ('d', 'p', 0, ('p', 'Lens$71$get_projection_mat_inv', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'Lens$81$get_type', 'p'), []),
    ]
    c.ct['get_up_vector'] = [
        ('d', 42, 0, ('p', 'Lens$46$get_up_vector', 'p'), []),
    ]
    c.ct['get_vfov'] = [
        ('d', 'f', 0, ('f', 'Lens$29$get_vfov', 'p'), []),
    ]
    c.ct['get_view_hpr'] = [
        ('d', 9, 0, ('p', 'Lens$42$get_view_hpr', 'p'), []),
    ]
    c.ct['get_view_mat'] = [
        ('d', 'p', 0, ('p', 'Lens$53$get_view_mat', 'p'), []),
    ]
    c.ct['get_view_vector'] = [
        ('d', 42, 0, ('p', 'Lens$45$get_view_vector', 'p'), []),
    ]
    c.ct['is_linear'] = [
        ('d', 'B', 0, ('B', 'Lens$63$is_linear', 'p'), []),
    ]
    c.ct['is_orthographic'] = [
        ('d', 'B', 0, ('B', 'Lens$65$is_orthographic', 'p'), []),
    ]
    c.ct['is_perspective'] = [
        ('d', 'B', 0, ('B', 'Lens$64$is_perspective', 'p'), []),
    ]
    c.ct['make_bounds'] = [
        ('d', 'p', 0, ('p', 'Lens$67$make_bounds', 'p'), []),
    ]
    c.ct['make_copy'] = [
        ('d', 71, 0, ('p', 'Lens$1$make_copy', 'p'), []),
    ]
    c.ct['make_geometry'] = [
        ('d', 84, 0, ('p', 'Lens$66$make_geometry', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'Lens$76$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['project'] = [
        ('d', 'B', 2, ('B', 'Lens$7$project', 'ppp'), ['LPoint3 const&', 'LPoint2&']),
        ('d', 'B', 2, ('B', 'Lens$8$project', 'ppp'), ['LPoint3 const&', 'LPoint3&']),
    ]
    c.ct['recompute_all'] = [
        ('d', 'v', 0, ('v', 'Lens$62$recompute_all', 'p'), []),
    ]
    c.ct['set_aspect_ratio'] = [
        ('d', 'v', 1, ('v', 'Lens$31$set_aspect_ratio', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_change_event'] = [
        ('d', 'v', 1, ('v', 'Lens$9$set_change_event', 'ps'), ['std::string const&']),
    ]
    c.ct['set_convergence_distance'] = [
        ('d', 'v', 1, ('v', 'Lens$50$set_convergence_distance', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_coordinate_system'] = [
        ('d', 'v', 1, ('v', 'Lens$11$set_coordinate_system', 'pp'), ['CoordinateSystem']),
    ]
    c.ct['set_custom_film_mat'] = [
        ('d', 'v', 1, ('v', 'Lens$58$set_custom_film_mat', 'pp'), ['LMatrix4 const&']),
    ]
    c.ct['set_far'] = [
        ('d', 'v', 1, ('v', 'Lens$35$set_far', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_film_offset'] = [
        ('d', 'v', 1, ('v', 'Lens$18$set_film_offset', 'pp'), ['LVecBase2 const&']),
        ('d', 'v', 2, ('v', 'Lens$19$set_film_offset', 'pff'), ['PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_film_size'] = [
        ('d', 'v', 1, ('v', 'Lens$14$set_film_size', 'pp'), ['LVecBase2 const&']),
        ('d', 'v', 1, ('v', 'Lens$15$set_film_size', 'pf'), ['PN_stdfloat']),
        ('d', 'v', 2, ('v', 'Lens$16$set_film_size', 'pff'), ['PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_focal_length'] = [
        ('d', 'v', 1, ('v', 'Lens$21$set_focal_length', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_fov'] = [
        ('d', 'v', 1, ('v', 'Lens$24$set_fov', 'pp'), ['LVecBase2 const&']),
        ('d', 'v', 1, ('v', 'Lens$25$set_fov', 'pf'), ['PN_stdfloat']),
        ('d', 'v', 2, ('v', 'Lens$26$set_fov', 'pff'), ['PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_frustum_from_corners'] = [
        ('d', 'v', 5, ('v', 'Lens$61$set_frustum_from_corners', 'pppppi'), ['LVecBase3 const&', 'LVecBase3 const&', 'LVecBase3 const&', 'LVecBase3 const&', 'int']),
    ]
    c.ct['set_interocular_distance'] = [
        ('d', 'v', 1, ('v', 'Lens$48$set_interocular_distance', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_keystone'] = [
        ('d', 'v', 1, ('v', 'Lens$55$set_keystone', 'pp'), ['LVecBase2 const&']),
    ]
    c.ct['set_min_fov'] = [
        ('d', 'v', 1, ('v', 'Lens$23$set_min_fov', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_near'] = [
        ('d', 'v', 1, ('v', 'Lens$33$set_near', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_near_far'] = [
        ('d', 'v', 2, ('v', 'Lens$37$set_near_far', 'pff'), ['PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_view_hpr'] = [
        ('d', 'v', 1, ('v', 'Lens$40$set_view_hpr', 'pp'), ['LVecBase3 const&']),
        ('d', 'v', 3, ('v', 'Lens$41$set_view_hpr', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_view_mat'] = [
        ('d', 'v', 1, ('v', 'Lens$52$set_view_mat', 'pp'), ['LMatrix4 const&']),
    ]
    c.ct['set_view_vector'] = [
        ('d', 'v', 2, ('v', 'Lens$43$set_view_vector', 'ppp'), ['LVector3 const&', 'LVector3 const&']),
        ('d', 'v', 6, ('v', 'Lens$44$set_view_vector', 'pffffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'Lens$77$write', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'v', 1, ('v', 'Lens$78$write', 'pp'), ['std::ostream&']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'Lens$80$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(Lens, attr, self)

Lens.c.link(Lens)



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
        ('d', 72, 0, ('p', 'InternalName$4$get_parent', 'p'), []),
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



class GraphicsOutputBase(TypedWritableReferenceCount):
    __bases__ = tuple([TypedWritableReferenceCount])
    c = cxx.cstructs()
    c.register("GraphicsOutputBase", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_GraphicsOutput'] = [
        ('d', 74, 0, ('p', 'GraphicsOutputBase$1$downcast_to_GraphicsOutput', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GraphicsOutputBase, attr, self)

GraphicsOutputBase.c.link(GraphicsOutputBase)



class GraphicsOutput(GraphicsOutputBase, DrawableRegion):
    __bases__ = tuple([GraphicsOutputBase, DrawableRegion])
    c = cxx.cstructs()
    c.register("GraphicsOutput", "upanda3d", """libupanda3d_c.so""")

    # enum RenderTextureMode

    RTM_bind_layered = const(6)
    RTM_bind_or_copy = const(1)
    RTM_copy_ram = const(3)
    RTM_copy_texture = const(2)
    RTM_none = const(0)
    RTM_triggered_copy_ram = const(5)
    RTM_triggered_copy_texture = const(4)


    # enum FrameMode

    FM_parasite = const(1)
    FM_refresh = const(2)
    FM_render = const(0)


    # ctor/dtor


    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'GraphicsOutput$118$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'GraphicsOutput$119$init_type', ''), []),
    ]
    c.ct['make_screenshot_filename'] = [
        ('s', 3, 1, ('p', 'GraphicsOutput$86$make_screenshot_filename', 's'), ['std::string const&']),
        ('s', 3, 0, ('p', 'GraphicsOutput$87$make_screenshot_filename', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(GraphicsOutput, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(GraphicsOutput, 'init_type', None) )(*args,**kw)

    @classmethod
    def make_screenshot_filename(cls, *args,**kw):
        return ( cls.c.get('make_screenshot_filename', None) or cls.c.call(GraphicsOutput, 'make_screenshot_filename', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_render_texture'] = [
        ('d', 'v', 3, ('v', 'GraphicsOutput$16$add_render_texture', 'pppp'), ['Texture*', 'GraphicsOutput::RenderTextureMode', 'DrawableRegion::RenderTexturePlane']),
        ('d', 'v', 2, ('v', 'GraphicsOutput$17$add_render_texture', 'ppp'), ['Texture*', 'GraphicsOutput::RenderTextureMode']),
    ]
    c.ct['begin_flip'] = [
        ('d', 'v', 0, ('v', 'GraphicsOutput$111$begin_flip', 'p'), []),
    ]
    c.ct['begin_frame'] = [
        ('d', 'B', 2, ('B', 'GraphicsOutput$107$begin_frame', 'ppp'), ['GraphicsOutput::FrameMode', 'Thread*']),
    ]
    c.ct['change_scenes'] = [
        ('d', 'v', 1, ('v', 'GraphicsOutput$109$change_scenes', 'pp'), ['DisplayRegionPipelineReader*']),
    ]
    c.ct['clear'] = [
        ('d', 'v', 1, ('v', 'GraphicsOutput$106$clear', 'pp'), ['Thread*']),
    ]
    c.ct['clear_child_sort'] = [
        ('d', 'v', 0, ('v', 'GraphicsOutput$58$clear_child_sort', 'p'), []),
    ]
    c.ct['clear_delete_flag'] = [
        ('d', 'v', 0, ('v', 'GraphicsOutput$53$clear_delete_flag', 'p'), []),
    ]
    c.ct['clear_pipe'] = [
        ('d', 'v', 0, ('v', 'GraphicsOutput$104$clear_pipe', 'p'), []),
    ]
    c.ct['clear_render_textures'] = [
        ('d', 'v', 0, ('v', 'GraphicsOutput$15$clear_render_textures', 'p'), []),
    ]
    c.ct['count_textures'] = [
        ('d', 'i', 0, ('i', 'GraphicsOutput$7$count_textures', 'p'), []),
    ]
    c.ct['end_flip'] = [
        ('d', 'v', 0, ('v', 'GraphicsOutput$113$end_flip', 'p'), []),
    ]
    c.ct['end_frame'] = [
        ('d', 'v', 2, ('v', 'GraphicsOutput$108$end_frame', 'ppp'), ['GraphicsOutput::FrameMode', 'Thread*']),
    ]
    c.ct['flip_ready'] = [
        ('d', 'B', 0, ('B', 'GraphicsOutput$98$flip_ready', 'p'), []),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'GraphicsOutput$121$force_init_type', 'p'), []),
    ]
    c.ct['get_active_display_region'] = [
        ('d', 61, 1, ('p', 'GraphicsOutput$77$get_active_display_region', 'pi'), ['int']),
    ]
    c.ct['get_child_sort'] = [
        ('d', 'i', 0, ('i', 'GraphicsOutput$59$get_child_sort', 'p'), []),
    ]
    c.ct['get_clear_window_pcollector'] = [
        ('d', 'p', 0, ('p', 'GraphicsOutput$117$get_clear_window_pcollector', 'p'), []),
    ]
    c.ct['get_cull_window_pcollector'] = [
        ('d', 'p', 0, ('p', 'GraphicsOutput$115$get_cull_window_pcollector', 'p'), []),
    ]
    c.ct['get_delete_flag'] = [
        ('d', 'B', 0, ('B', 'GraphicsOutput$54$get_delete_flag', 'p'), []),
    ]
    c.ct['get_display_region'] = [
        ('d', 61, 1, ('p', 'GraphicsOutput$75$get_display_region', 'pi'), ['int']),
    ]
    c.ct['get_draw_window_pcollector'] = [
        ('d', 'p', 0, ('p', 'GraphicsOutput$116$get_draw_window_pcollector', 'p'), []),
    ]
    c.ct['get_engine'] = [
        ('d', 50, 0, ('p', 'GraphicsOutput$5$get_engine', 'p'), []),
    ]
    c.ct['get_fb_properties'] = [
        ('d', 4, 0, ('p', 'GraphicsOutput$51$get_fb_properties', 'p'), []),
    ]
    c.ct['get_fb_size'] = [
        ('d', 'p', 0, ('p', 'GraphicsOutput$22$get_fb_size', 'p'), []),
    ]
    c.ct['get_fb_x_size'] = [
        ('d', 'i', 0, ('i', 'GraphicsOutput$23$get_fb_x_size', 'p'), []),
    ]
    c.ct['get_fb_y_size'] = [
        ('d', 'i', 0, ('i', 'GraphicsOutput$24$get_fb_y_size', 'p'), []),
    ]
    c.ct['get_gsg'] = [
        ('d', 'p', 0, ('p', 'GraphicsOutput$3$get_gsg', 'p'), []),
    ]
    c.ct['get_host'] = [
        ('d', 74, 0, ('p', 'GraphicsOutput$99$get_host', 'p'), []),
    ]
    c.ct['get_inverted'] = [
        ('d', 'B', 0, ('B', 'GraphicsOutput$39$get_inverted', 'p'), []),
    ]
    c.ct['get_left_eye_color_mask'] = [
        ('d', 'I', 0, ('I', 'GraphicsOutput$44$get_left_eye_color_mask', 'p'), []),
    ]
    c.ct['get_name'] = [
        ('d', 's', 0, ('s', 'GraphicsOutput$6$get_name', 'p'), []),
    ]
    c.ct['get_num_active_display_regions'] = [
        ('d', 'i', 0, ('i', 'GraphicsOutput$76$get_num_active_display_regions', 'p'), []),
    ]
    c.ct['get_num_display_regions'] = [
        ('d', 'i', 0, ('i', 'GraphicsOutput$74$get_num_display_regions', 'p'), []),
    ]
    c.ct['get_one_shot'] = [
        ('d', 'B', 0, ('B', 'GraphicsOutput$37$get_one_shot', 'p'), []),
    ]
    c.ct['get_overlay_display_region'] = [
        ('d', 61, 0, ('p', 'GraphicsOutput$72$get_overlay_display_region', 'p'), []),
    ]
    c.ct['get_pipe'] = [
        ('d', 'p', 0, ('p', 'GraphicsOutput$4$get_pipe', 'p'), []),
    ]
    c.ct['get_red_blue_stereo'] = [
        ('d', 'B', 0, ('B', 'GraphicsOutput$43$get_red_blue_stereo', 'p'), []),
    ]
    c.ct['get_right_eye_color_mask'] = [
        ('d', 'I', 0, ('I', 'GraphicsOutput$45$get_right_eye_color_mask', 'p'), []),
    ]
    c.ct['get_rtm_mode'] = [
        ('d', 'p', 1, ('p', 'GraphicsOutput$13$get_rtm_mode', 'pi'), ['int']),
        ('d', 'p', 0, ('p', 'GraphicsOutput$14$get_rtm_mode', 'p'), []),
    ]
    c.ct['get_sbs_left_dimensions'] = [
        ('d', 12, 0, ('p', 'GraphicsOutput$49$get_sbs_left_dimensions', 'p'), []),
    ]
    c.ct['get_sbs_left_size'] = [
        ('d', 'p', 0, ('p', 'GraphicsOutput$25$get_sbs_left_size', 'p'), []),
    ]
    c.ct['get_sbs_left_x_size'] = [
        ('d', 'i', 0, ('i', 'GraphicsOutput$26$get_sbs_left_x_size', 'p'), []),
    ]
    c.ct['get_sbs_left_y_size'] = [
        ('d', 'i', 0, ('i', 'GraphicsOutput$27$get_sbs_left_y_size', 'p'), []),
    ]
    c.ct['get_sbs_right_dimensions'] = [
        ('d', 12, 0, ('p', 'GraphicsOutput$50$get_sbs_right_dimensions', 'p'), []),
    ]
    c.ct['get_sbs_right_size'] = [
        ('d', 'p', 0, ('p', 'GraphicsOutput$28$get_sbs_right_size', 'p'), []),
    ]
    c.ct['get_sbs_right_x_size'] = [
        ('d', 'i', 0, ('i', 'GraphicsOutput$29$get_sbs_right_x_size', 'p'), []),
    ]
    c.ct['get_sbs_right_y_size'] = [
        ('d', 'i', 0, ('i', 'GraphicsOutput$30$get_sbs_right_y_size', 'p'), []),
    ]
    c.ct['get_screenshot'] = [
        ('d', 64, 0, ('p', 'GraphicsOutput$92$get_screenshot', 'p'), []),
        ('d', 'B', 1, ('B', 'GraphicsOutput$93$get_screenshot', 'pp'), ['PNMImage&']),
    ]
    c.ct['get_side_by_side_stereo'] = [
        ('d', 'B', 0, ('B', 'GraphicsOutput$48$get_side_by_side_stereo', 'p'), []),
    ]
    c.ct['get_size'] = [
        ('d', 'p', 0, ('p', 'GraphicsOutput$19$get_size', 'p'), []),
    ]
    c.ct['get_sort'] = [
        ('d', 'i', 0, ('i', 'GraphicsOutput$56$get_sort', 'p'), []),
    ]
    c.ct['get_supports_render_texture'] = [
        ('d', 'B', 0, ('B', 'GraphicsOutput$97$get_supports_render_texture', 'p'), []),
    ]
    c.ct['get_swap_eyes'] = [
        ('d', 'B', 0, ('B', 'GraphicsOutput$41$get_swap_eyes', 'p'), []),
    ]
    c.ct['get_texture'] = [
        ('d', 64, 1, ('p', 'GraphicsOutput$9$get_texture', 'pi'), ['int']),
        ('d', 64, 0, ('p', 'GraphicsOutput$10$get_texture', 'p'), []),
    ]
    c.ct['get_texture_card'] = [
        ('d', 17, 0, ('p', 'GraphicsOutput$94$get_texture_card', 'p'), []),
    ]
    c.ct['get_texture_plane'] = [
        ('d', 'p', 1, ('p', 'GraphicsOutput$11$get_texture_plane', 'pi'), ['int']),
        ('d', 'p', 0, ('p', 'GraphicsOutput$12$get_texture_plane', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'GraphicsOutput$120$get_type', 'p'), []),
    ]
    c.ct['get_x_size'] = [
        ('d', 'i', 0, ('i', 'GraphicsOutput$20$get_x_size', 'p'), []),
    ]
    c.ct['get_y_size'] = [
        ('d', 'i', 0, ('i', 'GraphicsOutput$21$get_y_size', 'p'), []),
    ]
    c.ct['has_size'] = [
        ('d', 'B', 0, ('B', 'GraphicsOutput$31$has_size', 'p'), []),
    ]
    c.ct['has_texture'] = [
        ('d', 'B', 0, ('B', 'GraphicsOutput$8$has_texture', 'p'), []),
    ]
    c.ct['is_active'] = [
        ('d', 'B', 0, ('B', 'GraphicsOutput$35$is_active', 'p'), []),
    ]
    c.ct['is_nonzero_size'] = [
        ('d', 'B', 0, ('B', 'GraphicsOutput$33$is_nonzero_size', 'p'), []),
    ]
    c.ct['is_stereo'] = [
        ('d', 'B', 0, ('B', 'GraphicsOutput$52$is_stereo', 'p'), []),
    ]
    c.ct['is_valid'] = [
        ('d', 'B', 0, ('B', 'GraphicsOutput$32$is_valid', 'p'), []),
    ]
    c.ct['make_cube_map'] = [
        ('d', 74, 6, ('p', 'GraphicsOutput$82$make_cube_map', 'psippBp'), ['std::string const&', 'int', 'NodePath&', 'DrawMask', 'bool', 'FrameBufferProperties*']),
        ('d', 74, 5, ('p', 'GraphicsOutput$83$make_cube_map', 'psippB'), ['std::string const&', 'int', 'NodePath&', 'DrawMask', 'bool']),
        ('d', 74, 4, ('p', 'GraphicsOutput$84$make_cube_map', 'psipp'), ['std::string const&', 'int', 'NodePath&', 'DrawMask']),
        ('d', 74, 3, ('p', 'GraphicsOutput$85$make_cube_map', 'psip'), ['std::string const&', 'int', 'NodePath&']),
    ]
    c.ct['make_display_region'] = [
        ('d', 61, 0, ('p', 'GraphicsOutput$61$make_display_region', 'p'), []),
        ('d', 61, 1, ('p', 'GraphicsOutput$62$make_display_region', 'pp'), ['LVecBase4 const&']),
        ('d', 61, 4, ('p', 'GraphicsOutput$63$make_display_region', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['make_mono_display_region'] = [
        ('d', 61, 0, ('p', 'GraphicsOutput$64$make_mono_display_region', 'p'), []),
        ('d', 61, 1, ('p', 'GraphicsOutput$65$make_mono_display_region', 'pp'), ['LVecBase4 const&']),
        ('d', 61, 4, ('p', 'GraphicsOutput$66$make_mono_display_region', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['make_stereo_display_region'] = [
        ('d', 'p', 0, ('p', 'GraphicsOutput$67$make_stereo_display_region', 'p'), []),
        ('d', 'p', 1, ('p', 'GraphicsOutput$68$make_stereo_display_region', 'pp'), ['LVecBase4 const&']),
        ('d', 'p', 4, ('p', 'GraphicsOutput$69$make_stereo_display_region', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['make_texture_buffer'] = [
        ('d', 74, 6, ('p', 'GraphicsOutput$78$make_texture_buffer', 'psiipBp'), ['std::string const&', 'int', 'int', 'Texture*', 'bool', 'FrameBufferProperties*']),
        ('d', 74, 5, ('p', 'GraphicsOutput$79$make_texture_buffer', 'psiipB'), ['std::string const&', 'int', 'int', 'Texture*', 'bool']),
        ('d', 74, 4, ('p', 'GraphicsOutput$80$make_texture_buffer', 'psiip'), ['std::string const&', 'int', 'int', 'Texture*']),
        ('d', 74, 3, ('p', 'GraphicsOutput$81$make_texture_buffer', 'psii'), ['std::string const&', 'int', 'int']),
    ]
    c.ct['process_events'] = [
        ('d', 'v', 0, ('v', 'GraphicsOutput$114$process_events', 'p'), []),
    ]
    c.ct['ready_flip'] = [
        ('d', 'v', 0, ('v', 'GraphicsOutput$112$ready_flip', 'p'), []),
    ]
    c.ct['remove_all_display_regions'] = [
        ('d', 'v', 0, ('v', 'GraphicsOutput$71$remove_all_display_regions', 'p'), []),
    ]
    c.ct['remove_display_region'] = [
        ('d', 'B', 1, ('B', 'GraphicsOutput$70$remove_display_region', 'pp'), ['DisplayRegion*']),
    ]
    c.ct['request_close'] = [
        ('d', 'v', 0, ('v', 'GraphicsOutput$101$request_close', 'p'), []),
    ]
    c.ct['request_open'] = [
        ('d', 'v', 0, ('v', 'GraphicsOutput$100$request_open', 'p'), []),
    ]
    c.ct['reset_window'] = [
        ('d', 'v', 1, ('v', 'GraphicsOutput$103$reset_window', 'pB'), ['bool']),
    ]
    c.ct['save_screenshot'] = [
        ('d', 'B', 2, ('B', 'GraphicsOutput$90$save_screenshot', 'pps'), ['Filename const&', 'std::string const&']),
        ('d', 'B', 1, ('B', 'GraphicsOutput$91$save_screenshot', 'pp'), ['Filename const&']),
    ]
    c.ct['save_screenshot_default'] = [
        ('d', 3, 1, ('p', 'GraphicsOutput$88$save_screenshot_default', 'ps'), ['std::string const&']),
        ('d', 3, 0, ('p', 'GraphicsOutput$89$save_screenshot_default', 'p'), []),
    ]
    c.ct['select_target_tex_page'] = [
        ('d', 'v', 1, ('v', 'GraphicsOutput$110$select_target_tex_page', 'pi'), ['int']),
    ]
    c.ct['set_active'] = [
        ('d', 'v', 1, ('v', 'GraphicsOutput$34$set_active', 'pB'), ['bool']),
    ]
    c.ct['set_child_sort'] = [
        ('d', 'v', 1, ('v', 'GraphicsOutput$57$set_child_sort', 'pi'), ['int']),
    ]
    c.ct['set_close_now'] = [
        ('d', 'v', 0, ('v', 'GraphicsOutput$102$set_close_now', 'p'), []),
    ]
    c.ct['set_inverted'] = [
        ('d', 'v', 1, ('v', 'GraphicsOutput$38$set_inverted', 'pB'), ['bool']),
    ]
    c.ct['set_one_shot'] = [
        ('d', 'v', 1, ('v', 'GraphicsOutput$36$set_one_shot', 'pB'), ['bool']),
    ]
    c.ct['set_overlay_display_region'] = [
        ('d', 'v', 1, ('v', 'GraphicsOutput$73$set_overlay_display_region', 'pp'), ['DisplayRegion*']),
    ]
    c.ct['set_red_blue_stereo'] = [
        ('d', 'v', 3, ('v', 'GraphicsOutput$42$set_red_blue_stereo', 'pBII'), ['bool', 'unsigned int', 'unsigned int']),
    ]
    c.ct['set_side_by_side_stereo'] = [
        ('d', 'v', 1, ('v', 'GraphicsOutput$46$set_side_by_side_stereo', 'pB'), ['bool']),
        ('d', 'v', 3, ('v', 'GraphicsOutput$47$set_side_by_side_stereo', 'pBpp'), ['bool', 'LVecBase4 const&', 'LVecBase4 const&']),
    ]
    c.ct['set_size_and_recalc'] = [
        ('d', 'v', 2, ('v', 'GraphicsOutput$105$set_size_and_recalc', 'pii'), ['int', 'int']),
    ]
    c.ct['set_sort'] = [
        ('d', 'v', 1, ('v', 'GraphicsOutput$55$set_sort', 'pi'), ['int']),
    ]
    c.ct['set_swap_eyes'] = [
        ('d', 'v', 1, ('v', 'GraphicsOutput$40$set_swap_eyes', 'pB'), ['bool']),
    ]
    c.ct['setup_render_texture'] = [
        ('d', 'v', 3, ('v', 'GraphicsOutput$18$setup_render_texture', 'ppBB'), ['Texture*', 'bool', 'bool']),
    ]
    c.ct['share_depth_buffer'] = [
        ('d', 'B', 1, ('B', 'GraphicsOutput$95$share_depth_buffer', 'pp'), ['GraphicsOutput*']),
    ]
    c.ct['trigger_copy'] = [
        ('d', 'p', 0, ('p', 'GraphicsOutput$60$trigger_copy', 'p'), []),
    ]
    c.ct['unshare_depth_buffer'] = [
        ('d', 'v', 0, ('v', 'GraphicsOutput$96$unshare_depth_buffer', 'p'), []),
    ]
    c.ct['upcast_to_DrawableRegion'] = [
        ('d', 1, 0, ('p', 'GraphicsOutput$2$upcast_to_DrawableRegion', 'p'), []),
    ]
    c.ct['upcast_to_GraphicsOutputBase'] = [
        ('d', 73, 0, ('p', 'GraphicsOutput$1$upcast_to_GraphicsOutputBase', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GraphicsOutput, attr, self)

GraphicsOutput.c.link(GraphicsOutput)



class GraphicsWindow(GraphicsOutput):
    __bases__ = tuple([GraphicsOutput])
    c = cxx.cstructs()
    c.register("GraphicsWindow", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'GraphicsWindow$38$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'GraphicsWindow$39$init_type', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(GraphicsWindow, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(GraphicsWindow, 'init_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_window_proc'] = [
        ('d', 'v', 1, ('v', 'GraphicsWindow$26$add_window_proc', 'pp'), ['GraphicsWindowProc const*']),
    ]
    c.ct['clear_rejected_properties'] = [
        ('d', 'v', 0, ('v', 'GraphicsWindow$3$clear_rejected_properties', 'p'), []),
    ]
    c.ct['clear_window_procs'] = [
        ('d', 'v', 0, ('v', 'GraphicsWindow$28$clear_window_procs', 'p'), []),
    ]
    c.ct['close_ime'] = [
        ('d', 'v', 0, ('v', 'GraphicsWindow$25$close_ime', 'p'), []),
    ]
    c.ct['disable_pointer_events'] = [
        ('d', 'v', 1, ('v', 'GraphicsWindow$22$disable_pointer_events', 'pi'), ['int']),
    ]
    c.ct['enable_pointer_events'] = [
        ('d', 'v', 1, ('v', 'GraphicsWindow$21$enable_pointer_events', 'pi'), ['int']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'GraphicsWindow$41$force_init_type', 'p'), []),
    ]
    c.ct['get_close_request_event'] = [
        ('d', 's', 0, ('s', 'GraphicsWindow$11$get_close_request_event', 'p'), []),
    ]
    c.ct['get_input_device'] = [
        ('d', 'p', 1, ('p', 'GraphicsWindow$16$get_input_device', 'pi'), ['int']),
    ]
    c.ct['get_input_device_name'] = [
        ('d', 's', 1, ('s', 'GraphicsWindow$17$get_input_device_name', 'pi'), ['int']),
    ]
    c.ct['get_keyboard_map'] = [
        ('d', 'p', 0, ('p', 'GraphicsWindow$20$get_keyboard_map', 'p'), []),
    ]
    c.ct['get_num_input_devices'] = [
        ('d', 'i', 0, ('i', 'GraphicsWindow$15$get_num_input_devices', 'p'), []),
    ]
    c.ct['get_num_touches'] = [
        ('d', 'i', 0, ('i', 'GraphicsWindow$31$get_num_touches', 'p'), []),
    ]
    c.ct['get_pointer'] = [
        ('d', 'p', 1, ('p', 'GraphicsWindow$23$get_pointer', 'pi'), ['int']),
    ]
    c.ct['get_properties'] = [
        ('d', 27, 0, ('p', 'GraphicsWindow$1$get_properties', 'p'), []),
    ]
    c.ct['get_rejected_properties'] = [
        ('d', 27, 0, ('p', 'GraphicsWindow$4$get_rejected_properties', 'p'), []),
    ]
    c.ct['get_requested_properties'] = [
        ('d', 27, 0, ('p', 'GraphicsWindow$2$get_requested_properties', 'p'), []),
    ]
    c.ct['get_touch_info'] = [
        ('d', 25, 1, ('p', 'GraphicsWindow$32$get_touch_info', 'pi'), ['int']),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'GraphicsWindow$40$get_type', 'p'), []),
    ]
    c.ct['get_unexposed_draw'] = [
        ('d', 'B', 0, ('B', 'GraphicsWindow$13$get_unexposed_draw', 'p'), []),
    ]
    c.ct['get_window_event'] = [
        ('d', 's', 0, ('s', 'GraphicsWindow$9$get_window_event', 'p'), []),
    ]
    c.ct['get_window_handle'] = [
        ('d', 62, 0, ('p', 'GraphicsWindow$14$get_window_handle', 'p'), []),
    ]
    c.ct['has_keyboard'] = [
        ('d', 'B', 1, ('B', 'GraphicsWindow$19$has_keyboard', 'pi'), ['int']),
    ]
    c.ct['has_pointer'] = [
        ('d', 'B', 1, ('B', 'GraphicsWindow$18$has_pointer', 'pi'), ['int']),
    ]
    c.ct['is_closed'] = [
        ('d', 'B', 0, ('B', 'GraphicsWindow$6$is_closed', 'p'), []),
    ]
    c.ct['is_fullscreen'] = [
        ('d', 'B', 0, ('B', 'GraphicsWindow$7$is_fullscreen', 'p'), []),
    ]
    c.ct['is_touch_event'] = [
        ('d', 'B', 1, ('B', 'GraphicsWindow$30$is_touch_event', 'pp'), ['GraphicsWindowProcCallbackData*']),
    ]
    c.ct['move_pointer'] = [
        ('d', 'B', 3, ('B', 'GraphicsWindow$24$move_pointer', 'piii'), ['int', 'int', 'int']),
    ]
    c.ct['process_events'] = [
        ('d', 'v', 0, ('v', 'GraphicsWindow$36$process_events', 'p'), []),
    ]
    c.ct['remove_window_proc'] = [
        ('d', 'v', 1, ('v', 'GraphicsWindow$27$remove_window_proc', 'pp'), ['GraphicsWindowProc const*']),
    ]
    c.ct['request_close'] = [
        ('d', 'v', 0, ('v', 'GraphicsWindow$34$request_close', 'p'), []),
    ]
    c.ct['request_open'] = [
        ('d', 'v', 0, ('v', 'GraphicsWindow$33$request_open', 'p'), []),
    ]
    c.ct['request_properties'] = [
        ('d', 'v', 1, ('v', 'GraphicsWindow$5$request_properties', 'pp'), ['WindowProperties const&']),
    ]
    c.ct['set_close_now'] = [
        ('d', 'v', 0, ('v', 'GraphicsWindow$35$set_close_now', 'p'), []),
    ]
    c.ct['set_close_request_event'] = [
        ('d', 'v', 1, ('v', 'GraphicsWindow$10$set_close_request_event', 'ps'), ['std::string const&']),
    ]
    c.ct['set_properties_now'] = [
        ('d', 'v', 1, ('v', 'GraphicsWindow$37$set_properties_now', 'pp'), ['WindowProperties&']),
    ]
    c.ct['set_unexposed_draw'] = [
        ('d', 'v', 1, ('v', 'GraphicsWindow$12$set_unexposed_draw', 'pB'), ['bool']),
    ]
    c.ct['set_window_event'] = [
        ('d', 'v', 1, ('v', 'GraphicsWindow$8$set_window_event', 'ps'), ['std::string const&']),
    ]
    c.ct['supports_window_procs'] = [
        ('d', 'B', 0, ('B', 'GraphicsWindow$29$supports_window_procs', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GraphicsWindow, attr, self)

GraphicsWindow.c.link(GraphicsWindow)



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



class NodeCachedReferenceCount(CachedTypedWritableReferenceCount):
    __bases__ = tuple([CachedTypedWritableReferenceCount])
    c = cxx.cstructs()
    c.register("NodeCachedReferenceCount", "upanda3d", """libupanda3d_c.so""")

    # enum Referenced

    R_cache = const(2)
    R_node = const(1)


    # ctor/dtor


    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'NodeCachedReferenceCount$6$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'NodeCachedReferenceCount$7$init_type', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(NodeCachedReferenceCount, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(NodeCachedReferenceCount, 'init_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['get_node_ref_count'] = [
        ('d', 'i', 0, ('i', 'NodeCachedReferenceCount$1$get_node_ref_count', 'p'), []),
    ]
    c.ct['get_referenced_bits'] = [
        ('d', 'i', 0, ('i', 'NodeCachedReferenceCount$5$get_referenced_bits', 'p'), []),
    ]
    c.ct['node_ref'] = [
        ('d', 'v', 0, ('v', 'NodeCachedReferenceCount$2$node_ref', 'p'), []),
    ]
    c.ct['node_unref'] = [
        ('d', 'B', 0, ('B', 'NodeCachedReferenceCount$3$node_unref', 'p'), []),
    ]
    c.ct['test_ref_count_integrity'] = [
        ('d', 'B', 0, ('B', 'NodeCachedReferenceCount$4$test_ref_count_integrity', 'p'), []),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(NodeCachedReferenceCount, attr, self)

NodeCachedReferenceCount.c.link(NodeCachedReferenceCount)



class TransformState(NodeCachedReferenceCount):
    __bases__ = tuple([NodeCachedReferenceCount])
    c = cxx.cstructs()
    c.register("TransformState", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['change_this'] = [
        ('s', 63, 2, ('p', 'TransformState$98$change_this', 'pp'), ['TypedWritableReferenceCount*', 'BamReader*']),
    ]
    c.ct['clear_cache'] = [
        ('s', 'i', 0, ('i', 'TransformState$89$clear_cache', ''), []),
    ]
    c.ct['flush_level'] = [
        ('s', 'v', 0, ('v', 'TransformState$95$flush_level', ''), []),
    ]
    c.ct['garbage_collect'] = [
        ('s', 'i', 0, ('i', 'TransformState$90$garbage_collect', ''), []),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'TransformState$99$get_class_type', ''), []),
    ]
    c.ct['get_num_states'] = [
        ('s', 'i', 0, ('i', 'TransformState$87$get_num_states', ''), []),
    ]
    c.ct['get_num_unused_states'] = [
        ('s', 'i', 0, ('i', 'TransformState$88$get_num_unused_states', ''), []),
    ]
    c.ct['init_states'] = [
        ('s', 'v', 0, ('v', 'TransformState$94$init_states', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'TransformState$100$init_type', ''), []),
    ]
    c.ct['list_cycles'] = [
        ('s', 'v', 1, ('v', 'TransformState$91$list_cycles', 'p'), ['std::ostream&']),
    ]
    c.ct['list_states'] = [
        ('s', 'v', 1, ('v', 'TransformState$92$list_states', 'p'), ['std::ostream&']),
    ]
    c.ct['make_hpr'] = [
        ('s', 78, 1, ('p', 'TransformState$7$make_hpr', 'p'), ['LVecBase3 const&']),
    ]
    c.ct['make_identity'] = [
        ('s', 78, 0, ('p', 'TransformState$4$make_identity', ''), []),
    ]
    c.ct['make_invalid'] = [
        ('s', 78, 0, ('p', 'TransformState$5$make_invalid', ''), []),
    ]
    c.ct['make_mat'] = [
        ('s', 78, 1, ('p', 'TransformState$17$make_mat', 'p'), ['LMatrix4 const&']),
    ]
    c.ct['make_mat3'] = [
        ('s', 78, 1, ('p', 'TransformState$26$make_mat3', 'p'), ['LMatrix3 const&']),
    ]
    c.ct['make_pos'] = [
        ('s', 78, 1, ('p', 'TransformState$6$make_pos', 'p'), ['LVecBase3 const&']),
    ]
    c.ct['make_pos2d'] = [
        ('s', 78, 1, ('p', 'TransformState$18$make_pos2d', 'p'), ['LVecBase2 const&']),
    ]
    c.ct['make_pos_hpr'] = [
        ('s', 78, 2, ('p', 'TransformState$9$make_pos_hpr', 'pp'), ['LVecBase3 const&', 'LVecBase3 const&']),
    ]
    c.ct['make_pos_hpr_scale'] = [
        ('s', 78, 3, ('p', 'TransformState$13$make_pos_hpr_scale', 'ppp'), ['LVecBase3 const&', 'LVecBase3 const&', 'LVecBase3 const&']),
    ]
    c.ct['make_pos_hpr_scale_shear'] = [
        ('s', 78, 4, ('p', 'TransformState$15$make_pos_hpr_scale_shear', 'pppp'), ['LVecBase3 const&', 'LVecBase3 const&', 'LVecBase3 const&', 'LVecBase3 const&']),
    ]
    c.ct['make_pos_quat_scale'] = [
        ('s', 78, 3, ('p', 'TransformState$14$make_pos_quat_scale', 'ppp'), ['LVecBase3 const&', 'LQuaternion const&', 'LVecBase3 const&']),
    ]
    c.ct['make_pos_quat_scale_shear'] = [
        ('s', 78, 4, ('p', 'TransformState$16$make_pos_quat_scale_shear', 'pppp'), ['LVecBase3 const&', 'LQuaternion const&', 'LVecBase3 const&', 'LVecBase3 const&']),
    ]
    c.ct['make_pos_rotate2d'] = [
        ('s', 78, 2, ('p', 'TransformState$20$make_pos_rotate2d', 'pf'), ['LVecBase2 const&', 'PN_stdfloat']),
    ]
    c.ct['make_pos_rotate_scale2d'] = [
        ('s', 78, 3, ('p', 'TransformState$24$make_pos_rotate_scale2d', 'pfp'), ['LVecBase2 const&', 'PN_stdfloat', 'LVecBase2 const&']),
    ]
    c.ct['make_pos_rotate_scale_shear2d'] = [
        ('s', 78, 4, ('p', 'TransformState$25$make_pos_rotate_scale_shear2d', 'pfpf'), ['LVecBase2 const&', 'PN_stdfloat', 'LVecBase2 const&', 'PN_stdfloat']),
    ]
    c.ct['make_quat'] = [
        ('s', 78, 1, ('p', 'TransformState$8$make_quat', 'p'), ['LQuaternion const&']),
    ]
    c.ct['make_rotate2d'] = [
        ('s', 78, 1, ('p', 'TransformState$19$make_rotate2d', 'f'), ['PN_stdfloat']),
    ]
    c.ct['make_scale'] = [
        ('s', 78, 1, ('p', 'TransformState$10$make_scale', 'p'), ['LVecBase3 const&']),
        ('s', 78, 1, ('p', 'TransformState$11$make_scale', 'f'), ['PN_stdfloat']),
    ]
    c.ct['make_scale2d'] = [
        ('s', 78, 1, ('p', 'TransformState$21$make_scale2d', 'p'), ['LVecBase2 const&']),
        ('s', 78, 1, ('p', 'TransformState$22$make_scale2d', 'f'), ['PN_stdfloat']),
    ]
    c.ct['make_shear'] = [
        ('s', 78, 1, ('p', 'TransformState$12$make_shear', 'p'), ['LVecBase3 const&']),
    ]
    c.ct['make_shear2d'] = [
        ('s', 78, 1, ('p', 'TransformState$23$make_shear2d', 'f'), ['PN_stdfloat']),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'TransformState$96$register_with_read_factory', ''), []),
    ]
    c.ct['validate_states'] = [
        ('s', 'B', 0, ('B', 'TransformState$93$validate_states', ''), []),
    ]

    @classmethod
    def change_this(cls, *args,**kw):
        return ( cls.c.get('change_this', None) or cls.c.call(TransformState, 'change_this', None) )(*args,**kw)

    @classmethod
    def clear_cache(cls, *args,**kw):
        return ( cls.c.get('clear_cache', None) or cls.c.call(TransformState, 'clear_cache', None) )(*args,**kw)

    @classmethod
    def flush_level(cls, *args,**kw):
        return ( cls.c.get('flush_level', None) or cls.c.call(TransformState, 'flush_level', None) )(*args,**kw)

    @classmethod
    def garbage_collect(cls, *args,**kw):
        return ( cls.c.get('garbage_collect', None) or cls.c.call(TransformState, 'garbage_collect', None) )(*args,**kw)

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(TransformState, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_num_states(cls, *args,**kw):
        return ( cls.c.get('get_num_states', None) or cls.c.call(TransformState, 'get_num_states', None) )(*args,**kw)

    @classmethod
    def get_num_unused_states(cls, *args,**kw):
        return ( cls.c.get('get_num_unused_states', None) or cls.c.call(TransformState, 'get_num_unused_states', None) )(*args,**kw)

    @classmethod
    def init_states(cls, *args,**kw):
        return ( cls.c.get('init_states', None) or cls.c.call(TransformState, 'init_states', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(TransformState, 'init_type', None) )(*args,**kw)

    @classmethod
    def list_cycles(cls, *args,**kw):
        return ( cls.c.get('list_cycles', None) or cls.c.call(TransformState, 'list_cycles', None) )(*args,**kw)

    @classmethod
    def list_states(cls, *args,**kw):
        return ( cls.c.get('list_states', None) or cls.c.call(TransformState, 'list_states', None) )(*args,**kw)

    @classmethod
    def make_hpr(cls, *args,**kw):
        return ( cls.c.get('make_hpr', None) or cls.c.call(TransformState, 'make_hpr', None) )(*args,**kw)

    @classmethod
    def make_identity(cls, *args,**kw):
        return ( cls.c.get('make_identity', None) or cls.c.call(TransformState, 'make_identity', None) )(*args,**kw)

    @classmethod
    def make_invalid(cls, *args,**kw):
        return ( cls.c.get('make_invalid', None) or cls.c.call(TransformState, 'make_invalid', None) )(*args,**kw)

    @classmethod
    def make_mat(cls, *args,**kw):
        return ( cls.c.get('make_mat', None) or cls.c.call(TransformState, 'make_mat', None) )(*args,**kw)

    @classmethod
    def make_mat3(cls, *args,**kw):
        return ( cls.c.get('make_mat3', None) or cls.c.call(TransformState, 'make_mat3', None) )(*args,**kw)

    @classmethod
    def make_pos(cls, *args,**kw):
        return ( cls.c.get('make_pos', None) or cls.c.call(TransformState, 'make_pos', None) )(*args,**kw)

    @classmethod
    def make_pos2d(cls, *args,**kw):
        return ( cls.c.get('make_pos2d', None) or cls.c.call(TransformState, 'make_pos2d', None) )(*args,**kw)

    @classmethod
    def make_pos_hpr(cls, *args,**kw):
        return ( cls.c.get('make_pos_hpr', None) or cls.c.call(TransformState, 'make_pos_hpr', None) )(*args,**kw)

    @classmethod
    def make_pos_hpr_scale(cls, *args,**kw):
        return ( cls.c.get('make_pos_hpr_scale', None) or cls.c.call(TransformState, 'make_pos_hpr_scale', None) )(*args,**kw)

    @classmethod
    def make_pos_hpr_scale_shear(cls, *args,**kw):
        return ( cls.c.get('make_pos_hpr_scale_shear', None) or cls.c.call(TransformState, 'make_pos_hpr_scale_shear', None) )(*args,**kw)

    @classmethod
    def make_pos_quat_scale(cls, *args,**kw):
        return ( cls.c.get('make_pos_quat_scale', None) or cls.c.call(TransformState, 'make_pos_quat_scale', None) )(*args,**kw)

    @classmethod
    def make_pos_quat_scale_shear(cls, *args,**kw):
        return ( cls.c.get('make_pos_quat_scale_shear', None) or cls.c.call(TransformState, 'make_pos_quat_scale_shear', None) )(*args,**kw)

    @classmethod
    def make_pos_rotate2d(cls, *args,**kw):
        return ( cls.c.get('make_pos_rotate2d', None) or cls.c.call(TransformState, 'make_pos_rotate2d', None) )(*args,**kw)

    @classmethod
    def make_pos_rotate_scale2d(cls, *args,**kw):
        return ( cls.c.get('make_pos_rotate_scale2d', None) or cls.c.call(TransformState, 'make_pos_rotate_scale2d', None) )(*args,**kw)

    @classmethod
    def make_pos_rotate_scale_shear2d(cls, *args,**kw):
        return ( cls.c.get('make_pos_rotate_scale_shear2d', None) or cls.c.call(TransformState, 'make_pos_rotate_scale_shear2d', None) )(*args,**kw)

    @classmethod
    def make_quat(cls, *args,**kw):
        return ( cls.c.get('make_quat', None) or cls.c.call(TransformState, 'make_quat', None) )(*args,**kw)

    @classmethod
    def make_rotate2d(cls, *args,**kw):
        return ( cls.c.get('make_rotate2d', None) or cls.c.call(TransformState, 'make_rotate2d', None) )(*args,**kw)

    @classmethod
    def make_scale(cls, *args,**kw):
        return ( cls.c.get('make_scale', None) or cls.c.call(TransformState, 'make_scale', None) )(*args,**kw)

    @classmethod
    def make_scale2d(cls, *args,**kw):
        return ( cls.c.get('make_scale2d', None) or cls.c.call(TransformState, 'make_scale2d', None) )(*args,**kw)

    @classmethod
    def make_shear(cls, *args,**kw):
        return ( cls.c.get('make_shear', None) or cls.c.call(TransformState, 'make_shear', None) )(*args,**kw)

    @classmethod
    def make_shear2d(cls, *args,**kw):
        return ( cls.c.get('make_shear2d', None) or cls.c.call(TransformState, 'make_shear2d', None) )(*args,**kw)

    @classmethod
    def register_with_read_factory(cls, *args,**kw):
        return ( cls.c.get('register_with_read_factory', None) or cls.c.call(TransformState, 'register_with_read_factory', None) )(*args,**kw)

    @classmethod
    def validate_states(cls, *args,**kw):
        return ( cls.c.get('validate_states', None) or cls.c.call(TransformState, 'validate_states', None) )(*args,**kw)

    # instance method type calls

    c.ct['cache_ref'] = [
        ('d', 'v', 0, ('v', 'TransformState$71$cache_ref', 'p'), []),
    ]
    c.ct['cache_unref'] = [
        ('d', 'B', 0, ('B', 'TransformState$72$cache_unref', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'TransformState$1$compare_to', 'pp'), ['TransformState const&']),
        ('d', 'i', 2, ('i', 'TransformState$2$compare_to', 'ppB'), ['TransformState const&', 'bool']),
    ]
    c.ct['components_given'] = [
        ('d', 'B', 0, ('B', 'TransformState$32$components_given', 'p'), []),
    ]
    c.ct['compose'] = [
        ('d', 78, 1, ('p', 'TransformState$66$compose', 'pp'), ['TransformState const*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'TransformState$102$force_init_type', 'p'), []),
    ]
    c.ct['get_composition_cache_num_entries'] = [
        ('d', 'l', 0, ('l', 'TransformState$75$get_composition_cache_num_entries', 'p'), []),
    ]
    c.ct['get_composition_cache_result'] = [
        ('d', 78, 1, ('p', 'TransformState$79$get_composition_cache_result', 'pl'), ['std::size_t']),
    ]
    c.ct['get_composition_cache_size'] = [
        ('d', 'l', 0, ('l', 'TransformState$77$get_composition_cache_size', 'p'), []),
    ]
    c.ct['get_composition_cache_source'] = [
        ('d', 78, 1, ('p', 'TransformState$78$get_composition_cache_source', 'pl'), ['std::size_t']),
    ]
    c.ct['get_geom_rendering'] = [
        ('d', 'i', 1, ('i', 'TransformState$70$get_geom_rendering', 'pi'), ['int']),
    ]
    c.ct['get_hash'] = [
        ('d', 'l', 0, ('l', 'TransformState$3$get_hash', 'p'), []),
    ]
    c.ct['get_hpr'] = [
        ('d', 9, 0, ('p', 'TransformState$45$get_hpr', 'p'), []),
    ]
    c.ct['get_inverse'] = [
        ('d', 78, 0, ('p', 'TransformState$68$get_inverse', 'p'), []),
    ]
    c.ct['get_invert_composition_cache_num_entries'] = [
        ('d', 'l', 0, ('l', 'TransformState$76$get_invert_composition_cache_num_entries', 'p'), []),
    ]
    c.ct['get_invert_composition_cache_result'] = [
        ('d', 78, 1, ('p', 'TransformState$82$get_invert_composition_cache_result', 'pl'), ['std::size_t']),
    ]
    c.ct['get_invert_composition_cache_size'] = [
        ('d', 'l', 0, ('l', 'TransformState$80$get_invert_composition_cache_size', 'p'), []),
    ]
    c.ct['get_invert_composition_cache_source'] = [
        ('d', 78, 1, ('p', 'TransformState$81$get_invert_composition_cache_source', 'pl'), ['std::size_t']),
    ]
    c.ct['get_mat'] = [
        ('d', 'p', 0, ('p', 'TransformState$51$get_mat', 'p'), []),
    ]
    c.ct['get_mat3'] = [
        ('d', 'p', 0, ('p', 'TransformState$56$get_mat3', 'p'), []),
    ]
    c.ct['get_norm_quat'] = [
        ('d', 'p', 0, ('p', 'TransformState$47$get_norm_quat', 'p'), []),
    ]
    c.ct['get_pos'] = [
        ('d', 33, 0, ('p', 'TransformState$44$get_pos', 'p'), []),
    ]
    c.ct['get_pos2d'] = [
        ('d', 6, 0, ('p', 'TransformState$52$get_pos2d', 'p'), []),
    ]
    c.ct['get_quat'] = [
        ('d', 'p', 0, ('p', 'TransformState$46$get_quat', 'p'), []),
    ]
    c.ct['get_rotate2d'] = [
        ('d', 'f', 0, ('f', 'TransformState$53$get_rotate2d', 'p'), []),
    ]
    c.ct['get_scale'] = [
        ('d', 9, 0, ('p', 'TransformState$48$get_scale', 'p'), []),
    ]
    c.ct['get_scale2d'] = [
        ('d', 6, 0, ('p', 'TransformState$54$get_scale2d', 'p'), []),
    ]
    c.ct['get_shear'] = [
        ('d', 9, 0, ('p', 'TransformState$50$get_shear', 'p'), []),
    ]
    c.ct['get_shear2d'] = [
        ('d', 'f', 0, ('f', 'TransformState$55$get_shear2d', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'TransformState$101$get_type', 'p'), []),
    ]
    c.ct['get_uniform_scale'] = [
        ('d', 'f', 0, ('f', 'TransformState$49$get_uniform_scale', 'p'), []),
    ]
    c.ct['get_unique'] = [
        ('d', 78, 0, ('p', 'TransformState$69$get_unique', 'p'), []),
    ]
    c.ct['has_components'] = [
        ('d', 'B', 0, ('B', 'TransformState$31$has_components', 'p'), []),
    ]
    c.ct['has_hpr'] = [
        ('d', 'B', 0, ('B', 'TransformState$36$has_hpr', 'p'), []),
    ]
    c.ct['has_identity_scale'] = [
        ('d', 'B', 0, ('B', 'TransformState$39$has_identity_scale', 'p'), []),
    ]
    c.ct['has_mat'] = [
        ('d', 'B', 0, ('B', 'TransformState$43$has_mat', 'p'), []),
    ]
    c.ct['has_nonzero_shear'] = [
        ('d', 'B', 0, ('B', 'TransformState$42$has_nonzero_shear', 'p'), []),
    ]
    c.ct['has_pos'] = [
        ('d', 'B', 0, ('B', 'TransformState$35$has_pos', 'p'), []),
    ]
    c.ct['has_quat'] = [
        ('d', 'B', 0, ('B', 'TransformState$37$has_quat', 'p'), []),
    ]
    c.ct['has_scale'] = [
        ('d', 'B', 0, ('B', 'TransformState$38$has_scale', 'p'), []),
    ]
    c.ct['has_shear'] = [
        ('d', 'B', 0, ('B', 'TransformState$41$has_shear', 'p'), []),
    ]
    c.ct['has_uniform_scale'] = [
        ('d', 'B', 0, ('B', 'TransformState$40$has_uniform_scale', 'p'), []),
    ]
    c.ct['hpr_given'] = [
        ('d', 'B', 0, ('B', 'TransformState$33$hpr_given', 'p'), []),
    ]
    c.ct['invert_compose'] = [
        ('d', 78, 1, ('p', 'TransformState$67$invert_compose', 'pp'), ['TransformState const*']),
    ]
    c.ct['is_2d'] = [
        ('d', 'B', 0, ('B', 'TransformState$30$is_2d', 'p'), []),
    ]
    c.ct['is_identity'] = [
        ('d', 'B', 0, ('B', 'TransformState$27$is_identity', 'p'), []),
    ]
    c.ct['is_invalid'] = [
        ('d', 'B', 0, ('B', 'TransformState$28$is_invalid', 'p'), []),
    ]
    c.ct['is_singular'] = [
        ('d', 'B', 0, ('B', 'TransformState$29$is_singular', 'p'), []),
    ]
    c.ct['node_ref'] = [
        ('d', 'v', 0, ('v', 'TransformState$73$node_ref', 'p'), []),
    ]
    c.ct['node_unref'] = [
        ('d', 'B', 0, ('B', 'TransformState$74$node_unref', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'TransformState$84$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['quat_given'] = [
        ('d', 'B', 0, ('B', 'TransformState$34$quat_given', 'p'), []),
    ]
    c.ct['set_hpr'] = [
        ('d', 78, 1, ('p', 'TransformState$58$set_hpr', 'pp'), ['LVecBase3 const&']),
    ]
    c.ct['set_pos'] = [
        ('d', 78, 1, ('p', 'TransformState$57$set_pos', 'pp'), ['LVecBase3 const&']),
    ]
    c.ct['set_pos2d'] = [
        ('d', 78, 1, ('p', 'TransformState$62$set_pos2d', 'pp'), ['LVecBase2 const&']),
    ]
    c.ct['set_quat'] = [
        ('d', 78, 1, ('p', 'TransformState$59$set_quat', 'pp'), ['LQuaternion const&']),
    ]
    c.ct['set_rotate2d'] = [
        ('d', 78, 1, ('p', 'TransformState$63$set_rotate2d', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_scale'] = [
        ('d', 78, 1, ('p', 'TransformState$60$set_scale', 'pp'), ['LVecBase3 const&']),
    ]
    c.ct['set_scale2d'] = [
        ('d', 78, 1, ('p', 'TransformState$64$set_scale2d', 'pp'), ['LVecBase2 const&']),
    ]
    c.ct['set_shear'] = [
        ('d', 78, 1, ('p', 'TransformState$61$set_shear', 'pp'), ['LVecBase3 const&']),
    ]
    c.ct['set_shear2d'] = [
        ('d', 78, 1, ('p', 'TransformState$65$set_shear2d', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['validate_composition_cache'] = [
        ('d', 'B', 0, ('B', 'TransformState$83$validate_composition_cache', 'p'), []),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'TransformState$85$write', 'ppi'), ['std::ostream&', 'int']),
    ]
    c.ct['write_composition_cache'] = [
        ('d', 'v', 2, ('v', 'TransformState$86$write_composition_cache', 'ppi'), ['std::ostream&', 'int']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'TransformState$97$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TransformState, attr, self)

TransformState.c.link(TransformState)



class RenderState(NodeCachedReferenceCount):
    __bases__ = tuple([NodeCachedReferenceCount])
    c = cxx.cstructs()
    c.register("RenderState", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls

    c.ct['bin_removed'] = [
        ('s', 'v', 1, ('v', 'RenderState$62$bin_removed', 'i'), ['int']),
    ]
    c.ct['change_this'] = [
        ('s', 55, 2, ('p', 'RenderState$69$change_this', 'pp'), ['TypedWritable*', 'BamReader*']),
    ]
    c.ct['clear_cache'] = [
        ('s', 'i', 0, ('i', 'RenderState$53$clear_cache', ''), []),
    ]
    c.ct['clear_munger_cache'] = [
        ('s', 'v', 0, ('v', 'RenderState$54$clear_munger_cache', ''), []),
    ]
    c.ct['flush_level'] = [
        ('s', 'v', 0, ('v', 'RenderState$63$flush_level', ''), []),
    ]
    c.ct['garbage_collect'] = [
        ('s', 'i', 0, ('i', 'RenderState$55$garbage_collect', ''), []),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'RenderState$71$get_class_type', ''), []),
    ]
    c.ct['get_max_priority'] = [
        ('s', 'i', 0, ('i', 'RenderState$50$get_max_priority', ''), []),
    ]
    c.ct['get_num_states'] = [
        ('s', 'i', 0, ('i', 'RenderState$51$get_num_states', ''), []),
    ]
    c.ct['get_num_unused_states'] = [
        ('s', 'i', 0, ('i', 'RenderState$52$get_num_unused_states', ''), []),
    ]
    c.ct['init_states'] = [
        ('s', 'v', 0, ('v', 'RenderState$64$init_states', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'RenderState$72$init_type', ''), []),
    ]
    c.ct['list_cycles'] = [
        ('s', 'v', 1, ('v', 'RenderState$56$list_cycles', 'p'), ['std::ostream&']),
    ]
    c.ct['list_states'] = [
        ('s', 'v', 1, ('v', 'RenderState$57$list_states', 'p'), ['std::ostream&']),
    ]
    c.ct['make'] = [
        ('s', 79, 6, ('p', 'RenderState$9$make', 'pppppi'), ['RenderAttrib const*', 'RenderAttrib const*', 'RenderAttrib const*', 'RenderAttrib const*', 'RenderAttrib const*', 'int']),
        ('s', 79, 5, ('p', 'RenderState$10$make', 'ppppp'), ['RenderAttrib const*', 'RenderAttrib const*', 'RenderAttrib const*', 'RenderAttrib const*', 'RenderAttrib const*']),
        ('s', 79, 5, ('p', 'RenderState$11$make', 'ppppi'), ['RenderAttrib const*', 'RenderAttrib const*', 'RenderAttrib const*', 'RenderAttrib const*', 'int']),
        ('s', 79, 4, ('p', 'RenderState$12$make', 'pppp'), ['RenderAttrib const*', 'RenderAttrib const*', 'RenderAttrib const*', 'RenderAttrib const*']),
        ('s', 79, 4, ('p', 'RenderState$13$make', 'pppi'), ['RenderAttrib const*', 'RenderAttrib const*', 'RenderAttrib const*', 'int']),
        ('s', 79, 3, ('p', 'RenderState$14$make', 'ppp'), ['RenderAttrib const*', 'RenderAttrib const*', 'RenderAttrib const*']),
        ('s', 79, 3, ('p', 'RenderState$15$make', 'ppi'), ['RenderAttrib const*', 'RenderAttrib const*', 'int']),
        ('s', 79, 2, ('p', 'RenderState$16$make', 'pp'), ['RenderAttrib const*', 'RenderAttrib const*']),
        ('s', 79, 2, ('p', 'RenderState$17$make', 'pi'), ['RenderAttrib const*', 'int']),
        ('s', 79, 1, ('p', 'RenderState$18$make', 'p'), ['RenderAttrib const*']),
    ]
    c.ct['make_empty'] = [
        ('s', 79, 0, ('p', 'RenderState$8$make_empty', ''), []),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'RenderState$67$register_with_read_factory', ''), []),
    ]
    c.ct['validate_states'] = [
        ('s', 'B', 0, ('B', 'RenderState$58$validate_states', ''), []),
    ]

    @classmethod
    def bin_removed(cls, *args,**kw):
        return ( cls.c.get('bin_removed', None) or cls.c.call(RenderState, 'bin_removed', None) )(*args,**kw)

    @classmethod
    def change_this(cls, *args,**kw):
        return ( cls.c.get('change_this', None) or cls.c.call(RenderState, 'change_this', None) )(*args,**kw)

    @classmethod
    def clear_cache(cls, *args,**kw):
        return ( cls.c.get('clear_cache', None) or cls.c.call(RenderState, 'clear_cache', None) )(*args,**kw)

    @classmethod
    def clear_munger_cache(cls, *args,**kw):
        return ( cls.c.get('clear_munger_cache', None) or cls.c.call(RenderState, 'clear_munger_cache', None) )(*args,**kw)

    @classmethod
    def flush_level(cls, *args,**kw):
        return ( cls.c.get('flush_level', None) or cls.c.call(RenderState, 'flush_level', None) )(*args,**kw)

    @classmethod
    def garbage_collect(cls, *args,**kw):
        return ( cls.c.get('garbage_collect', None) or cls.c.call(RenderState, 'garbage_collect', None) )(*args,**kw)

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(RenderState, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_max_priority(cls, *args,**kw):
        return ( cls.c.get('get_max_priority', None) or cls.c.call(RenderState, 'get_max_priority', None) )(*args,**kw)

    @classmethod
    def get_num_states(cls, *args,**kw):
        return ( cls.c.get('get_num_states', None) or cls.c.call(RenderState, 'get_num_states', None) )(*args,**kw)

    @classmethod
    def get_num_unused_states(cls, *args,**kw):
        return ( cls.c.get('get_num_unused_states', None) or cls.c.call(RenderState, 'get_num_unused_states', None) )(*args,**kw)

    @classmethod
    def init_states(cls, *args,**kw):
        return ( cls.c.get('init_states', None) or cls.c.call(RenderState, 'init_states', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(RenderState, 'init_type', None) )(*args,**kw)

    @classmethod
    def list_cycles(cls, *args,**kw):
        return ( cls.c.get('list_cycles', None) or cls.c.call(RenderState, 'list_cycles', None) )(*args,**kw)

    @classmethod
    def list_states(cls, *args,**kw):
        return ( cls.c.get('list_states', None) or cls.c.call(RenderState, 'list_states', None) )(*args,**kw)

    @classmethod
    def make(cls, *args,**kw):
        return ( cls.c.get('make', None) or cls.c.call(RenderState, 'make', None) )(*args,**kw)

    @classmethod
    def make_empty(cls, *args,**kw):
        return ( cls.c.get('make_empty', None) or cls.c.call(RenderState, 'make_empty', None) )(*args,**kw)

    @classmethod
    def register_with_read_factory(cls, *args,**kw):
        return ( cls.c.get('register_with_read_factory', None) or cls.c.call(RenderState, 'register_with_read_factory', None) )(*args,**kw)

    @classmethod
    def validate_states(cls, *args,**kw):
        return ( cls.c.get('validate_states', None) or cls.c.call(RenderState, 'validate_states', None) )(*args,**kw)

    # instance method type calls

    c.ct['add_attrib'] = [
        ('d', 79, 2, ('p', 'RenderState$21$add_attrib', 'ppi'), ['RenderAttrib const*', 'int']),
        ('d', 79, 1, ('p', 'RenderState$22$add_attrib', 'pp'), ['RenderAttrib const*']),
    ]
    c.ct['adjust_all_priorities'] = [
        ('d', 79, 1, ('p', 'RenderState$27$adjust_all_priorities', 'pi'), ['int']),
    ]
    c.ct['cache_ref'] = [
        ('d', 'v', 0, ('v', 'RenderState$36$cache_ref', 'p'), []),
    ]
    c.ct['cache_unref'] = [
        ('d', 'B', 0, ('B', 'RenderState$37$cache_unref', 'p'), []),
    ]
    c.ct['compare_mask'] = [
        ('d', 'i', 2, ('i', 'RenderState$3$compare_mask', 'ppp'), ['RenderState const&', 'RenderState::SlotMask']),
    ]
    c.ct['compare_sort'] = [
        ('d', 'i', 1, ('i', 'RenderState$2$compare_sort', 'pp'), ['RenderState const&']),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'RenderState$1$compare_to', 'pp'), ['RenderState const&']),
    ]
    c.ct['compose'] = [
        ('d', 79, 1, ('p', 'RenderState$19$compose', 'pp'), ['RenderState const*']),
    ]
    c.ct['cull_callback'] = [
        ('d', 'B', 2, ('B', 'RenderState$7$cull_callback', 'ppp'), ['CullTraverser*', 'CullTraverserData const&']),
    ]
    c.ct['finalize'] = [
        ('d', 'v', 1, ('v', 'RenderState$70$finalize', 'pp'), ['BamReader*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'RenderState$74$force_init_type', 'p'), []),
    ]
    c.ct['get_attrib'] = [
        ('d', 'p', 1, ('p', 'RenderState$30$get_attrib', 'pi'), ['TypeHandle']),
        ('d', 'p', 1, ('p', 'RenderState$31$get_attrib', 'pi'), ['int']),
    ]
    c.ct['get_attrib_def'] = [
        ('d', 'p', 1, ('p', 'RenderState$32$get_attrib_def', 'pi'), ['int']),
    ]
    c.ct['get_bin_index'] = [
        ('d', 'i', 0, ('i', 'RenderState$60$get_bin_index', 'p'), []),
    ]
    c.ct['get_composition_cache_num_entries'] = [
        ('d', 'l', 0, ('l', 'RenderState$40$get_composition_cache_num_entries', 'p'), []),
    ]
    c.ct['get_composition_cache_result'] = [
        ('d', 79, 1, ('p', 'RenderState$44$get_composition_cache_result', 'pl'), ['std::size_t']),
    ]
    c.ct['get_composition_cache_size'] = [
        ('d', 'l', 0, ('l', 'RenderState$42$get_composition_cache_size', 'p'), []),
    ]
    c.ct['get_composition_cache_source'] = [
        ('d', 79, 1, ('p', 'RenderState$43$get_composition_cache_source', 'pl'), ['std::size_t']),
    ]
    c.ct['get_draw_order'] = [
        ('d', 'i', 0, ('i', 'RenderState$59$get_draw_order', 'p'), []),
    ]
    c.ct['get_generated_shader'] = [
        ('d', 'p', 0, ('p', 'RenderState$65$get_generated_shader', 'p'), []),
    ]
    c.ct['get_generated_shader_seq'] = [
        ('d', 26, 0, ('p', 'RenderState$66$get_generated_shader_seq', 'p'), []),
    ]
    c.ct['get_geom_rendering'] = [
        ('d', 'i', 1, ('i', 'RenderState$61$get_geom_rendering', 'pi'), ['int']),
    ]
    c.ct['get_hash'] = [
        ('d', 'l', 0, ('l', 'RenderState$4$get_hash', 'p'), []),
    ]
    c.ct['get_invert_composition_cache_num_entries'] = [
        ('d', 'l', 0, ('l', 'RenderState$41$get_invert_composition_cache_num_entries', 'p'), []),
    ]
    c.ct['get_invert_composition_cache_result'] = [
        ('d', 79, 1, ('p', 'RenderState$47$get_invert_composition_cache_result', 'pl'), ['std::size_t']),
    ]
    c.ct['get_invert_composition_cache_size'] = [
        ('d', 'l', 0, ('l', 'RenderState$45$get_invert_composition_cache_size', 'p'), []),
    ]
    c.ct['get_invert_composition_cache_source'] = [
        ('d', 79, 1, ('p', 'RenderState$46$get_invert_composition_cache_source', 'pl'), ['std::size_t']),
    ]
    c.ct['get_override'] = [
        ('d', 'i', 1, ('i', 'RenderState$33$get_override', 'pi'), ['TypeHandle']),
        ('d', 'i', 1, ('i', 'RenderState$34$get_override', 'pi'), ['int']),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'RenderState$73$get_type', 'p'), []),
    ]
    c.ct['get_unique'] = [
        ('d', 79, 0, ('p', 'RenderState$35$get_unique', 'p'), []),
    ]
    c.ct['has_attrib'] = [
        ('d', 'B', 1, ('B', 'RenderState$28$has_attrib', 'pi'), ['TypeHandle']),
        ('d', 'B', 1, ('B', 'RenderState$29$has_attrib', 'pi'), ['int']),
    ]
    c.ct['has_cull_callback'] = [
        ('d', 'B', 0, ('B', 'RenderState$6$has_cull_callback', 'p'), []),
    ]
    c.ct['invert_compose'] = [
        ('d', 79, 1, ('p', 'RenderState$20$invert_compose', 'pp'), ['RenderState const*']),
    ]
    c.ct['is_empty'] = [
        ('d', 'B', 0, ('B', 'RenderState$5$is_empty', 'p'), []),
    ]
    c.ct['node_ref'] = [
        ('d', 'v', 0, ('v', 'RenderState$38$node_ref', 'p'), []),
    ]
    c.ct['node_unref'] = [
        ('d', 'B', 0, ('B', 'RenderState$39$node_unref', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'RenderState$48$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['remove_attrib'] = [
        ('d', 79, 1, ('p', 'RenderState$25$remove_attrib', 'pi'), ['TypeHandle']),
        ('d', 79, 1, ('p', 'RenderState$26$remove_attrib', 'pi'), ['int']),
    ]
    c.ct['set_attrib'] = [
        ('d', 79, 1, ('p', 'RenderState$23$set_attrib', 'pp'), ['RenderAttrib const*']),
        ('d', 79, 2, ('p', 'RenderState$24$set_attrib', 'ppi'), ['RenderAttrib const*', 'int']),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'RenderState$49$write', 'ppi'), ['std::ostream&', 'int']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'RenderState$68$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(RenderState, attr, self)

RenderState.c.link(RenderState)



class CopyOnWriteObject(CachedTypedWritableReferenceCount):
    __bases__ = tuple([CachedTypedWritableReferenceCount])
    c = cxx.cstructs()
    c.register("CopyOnWriteObject", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor


    # classmethod type calls


    # instance method type calls

    c.ct['downcast_to_Geom'] = [
        ('d', 84, 0, ('p', 'CopyOnWriteObject$1$downcast_to_Geom', 'p'), []),
    ]
    c.ct['downcast_to_GeomPrimitive'] = [
        ('d', 82, 0, ('p', 'CopyOnWriteObject$2$downcast_to_GeomPrimitive', 'p'), []),
    ]
    c.ct['downcast_to_GeomVertexArrayData'] = [
        ('d', 85, 0, ('p', 'CopyOnWriteObject$3$downcast_to_GeomVertexArrayData', 'p'), []),
    ]
    c.ct['downcast_to_GeomVertexData'] = [
        ('d', 81, 0, ('p', 'CopyOnWriteObject$4$downcast_to_GeomVertexData', 'p'), []),
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
        ('s', 81, 1, ('p', 'GeomVertexData$3$GeomVertexData', 'p'), ['GeomVertexData const&']),
        ('s', 81, 2, ('p', 'GeomVertexData$4$GeomVertexData', 'pp'), ['GeomVertexData const&', 'GeomVertexFormat const*']),
        ('s', 81, 3, ('p', 'GeomVertexData$5$GeomVertexData', 'spp'), ['std::string const&', 'GeomVertexFormat const*', 'GeomEnums::UsageHint']),
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
        ('d', 81, 2, ('p', 'GeomVertexData$49$animate_vertices', 'pBp'), ['bool', 'Thread*']),
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
        ('d', 81, 1, ('p', 'GeomVertexData$43$convert_to', 'pp'), ['GeomVertexFormat const*']),
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
        ('d', 85, 1, ('p', 'GeomVertexData$21$get_array', 'pl'), ['std::size_t']),
    ]
    c.ct['get_array_handle'] = [
        ('d', 56, 1, ('p', 'GeomVertexData$22$get_array_handle', 'pl'), ['std::size_t']),
    ]
    c.ct['get_format'] = [
        ('d', 65, 0, ('p', 'GeomVertexData$11$get_format', 'p'), []),
    ]
    c.ct['get_modified'] = [
        ('d', 26, 1, ('p', 'GeomVertexData$37$get_modified', 'pp'), ['Thread*']),
        ('d', 26, 0, ('p', 'GeomVertexData$38$get_modified', 'p'), []),
    ]
    c.ct['get_name'] = [
        ('d', 's', 0, ('s', 'GeomVertexData$7$get_name', 'p'), []),
    ]
    c.ct['get_num_arrays'] = [
        ('d', 'l', 0, ('l', 'GeomVertexData$20$get_num_arrays', 'p'), []),
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
        ('d', 68, 0, ('p', 'GeomVertexData$26$get_transform_table', 'p'), []),
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
        ('d', 85, 1, ('p', 'GeomVertexData$23$modify_array', 'pl'), ['std::size_t']),
    ]
    c.ct['modify_array_handle'] = [
        ('d', 56, 1, ('p', 'GeomVertexData$24$modify_array_handle', 'pl'), ['std::size_t']),
    ]
    c.ct['modify_transform_blend_table'] = [
        ('d', 'p', 0, ('p', 'GeomVertexData$30$modify_transform_blend_table', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'GeomVertexData$55$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['replace_column'] = [
        ('d', 81, 4, ('p', 'GeomVertexData$54$replace_column', 'ppipp'), ['InternalName*', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents']),
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
        ('d', 81, 0, ('p', 'GeomVertexData$48$reverse_normals', 'p'), []),
    ]
    c.ct['scale_color'] = [
        ('d', 81, 1, ('p', 'GeomVertexData$44$scale_color', 'pp'), ['LVecBase4 const&']),
        ('d', 81, 4, ('p', 'GeomVertexData$45$scale_color', 'ppipp'), ['LVecBase4 const&', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents']),
    ]
    c.ct['set_array'] = [
        ('d', 'v', 2, ('v', 'GeomVertexData$25$set_array', 'plp'), ['std::size_t', 'GeomVertexArrayData const*']),
    ]
    c.ct['set_color'] = [
        ('d', 81, 1, ('p', 'GeomVertexData$46$set_color', 'pp'), ['LColor const&']),
        ('d', 81, 4, ('p', 'GeomVertexData$47$set_color', 'ppipp'), ['LColor const&', 'int', 'GeomEnums::NumericType', 'GeomEnums::Contents']),
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
        ('d', 80, 0, ('p', 'GeomVertexData$1$upcast_to_CopyOnWriteObject', 'p'), []),
    ]
    c.ct['upcast_to_GeomEnums'] = [
        ('d', 5, 0, ('p', 'GeomVertexData$2$upcast_to_GeomEnums', 'p'), []),
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
        ('s', 66, 0, ('p', 'GeomPrimitive$85$get_index_format', 'p'), []),
        ('s', 66, 1, ('p', 'GeomPrimitive$86$get_index_format', 'p'), ['GeomEnums::NumericType']),
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
        ('d', 82, 0, ('p', 'GeomPrimitive$42$decompose', 'p'), []),
    ]
    c.ct['doubleside'] = [
        ('d', 82, 0, ('p', 'GeomPrimitive$44$doubleside', 'p'), []),
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
        ('d', 66, 0, ('p', 'GeomPrimitive$85$get_index_format', 'p'), []),
        ('d', 66, 1, ('p', 'GeomPrimitive$86$get_index_format', 'p'), ['GeomEnums::NumericType']),
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
        ('d', 85, 0, ('p', 'GeomPrimitive$74$get_maxs', 'p'), []),
    ]
    c.ct['get_min_num_vertices_per_primitive'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$78$get_min_num_vertices_per_primitive', 'p'), []),
    ]
    c.ct['get_min_vertex'] = [
        ('d', 'i', 0, ('i', 'GeomPrimitive$38$get_min_vertex', 'p'), []),
    ]
    c.ct['get_mins'] = [
        ('d', 85, 0, ('p', 'GeomPrimitive$73$get_mins', 'p'), []),
    ]
    c.ct['get_modified'] = [
        ('d', 26, 0, ('p', 'GeomPrimitive$53$get_modified', 'p'), []),
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
        ('d', 85, 0, ('p', 'GeomPrimitive$60$get_vertices', 'p'), []),
    ]
    c.ct['get_vertices_handle'] = [
        ('d', 56, 1, ('p', 'GeomPrimitive$61$get_vertices_handle', 'pp'), ['Thread*']),
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
        ('d', 82, 0, ('p', 'GeomPrimitive$50$make_adjacency', 'p'), []),
    ]
    c.ct['make_copy'] = [
        ('d', 82, 0, ('p', 'GeomPrimitive$3$make_copy', 'p'), []),
    ]
    c.ct['make_index_data'] = [
        ('d', 85, 0, ('p', 'GeomPrimitive$87$make_index_data', 'p'), []),
    ]
    c.ct['make_indexed'] = [
        ('d', 'v', 0, ('v', 'GeomPrimitive$30$make_indexed', 'p'), []),
    ]
    c.ct['make_lines'] = [
        ('d', 82, 0, ('p', 'GeomPrimitive$48$make_lines', 'p'), []),
    ]
    c.ct['make_nonindexed'] = [
        ('d', 'v', 2, ('v', 'GeomPrimitive$28$make_nonindexed', 'ppp'), ['GeomVertexData*', 'GeomVertexData const*']),
    ]
    c.ct['make_patches'] = [
        ('d', 82, 0, ('p', 'GeomPrimitive$49$make_patches', 'p'), []),
    ]
    c.ct['make_points'] = [
        ('d', 82, 0, ('p', 'GeomPrimitive$47$make_points', 'p'), []),
    ]
    c.ct['match_shade_model'] = [
        ('d', 82, 1, ('p', 'GeomPrimitive$46$match_shade_model', 'pp'), ['GeomEnums::ShadeModel']),
    ]
    c.ct['modify_ends'] = [
        ('d', 'p', 0, ('p', 'GeomPrimitive$71$modify_ends', 'p'), []),
    ]
    c.ct['modify_vertices'] = [
        ('d', 85, 1, ('p', 'GeomPrimitive$62$modify_vertices', 'pi'), ['int']),
        ('d', 85, 0, ('p', 'GeomPrimitive$63$modify_vertices', 'p'), []),
    ]
    c.ct['modify_vertices_handle'] = [
        ('d', 56, 1, ('p', 'GeomPrimitive$64$modify_vertices_handle', 'pp'), ['Thread*']),
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
        ('d', 82, 0, ('p', 'GeomPrimitive$45$reverse', 'p'), []),
    ]
    c.ct['rotate'] = [
        ('d', 82, 0, ('p', 'GeomPrimitive$43$rotate', 'p'), []),
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
        ('d', 80, 0, ('p', 'GeomPrimitive$1$upcast_to_CopyOnWriteObject', 'p'), []),
    ]
    c.ct['upcast_to_GeomEnums'] = [
        ('d', 5, 0, ('p', 'GeomPrimitive$2$upcast_to_GeomEnums', 'p'), []),
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
        ('s', 83, 1, ('p', 'GeomTriangles$1$GeomTriangles', 'p'), ['GeomEnums::UsageHint']),
        ('s', 83, 1, ('p', 'GeomTriangles$2$GeomTriangles', 'p'), ['GeomTriangles const&']),
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
        ('s', 84, 1, ('p', 'Geom$3$Geom', 'p'), ['GeomVertexData const*']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'Geom$77$get_class_type', ''), []),
    ]
    c.ct['get_next_modified'] = [
        ('s', 26, 0, ('p', 'Geom$73$get_next_modified', ''), []),
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
        ('d', 84, 0, ('p', 'Geom$27$decompose', 'p'), []),
    ]
    c.ct['decompose_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom$36$decompose_in_place', 'p'), []),
    ]
    c.ct['doubleside'] = [
        ('d', 84, 0, ('p', 'Geom$28$doubleside', 'p'), []),
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
        ('d', 81, 2, ('p', 'Geom$16$get_animated_vertex_data', 'pBp'), ['bool', 'Thread*']),
        ('d', 81, 1, ('p', 'Geom$17$get_animated_vertex_data', 'pB'), ['bool']),
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
        ('d', 26, 1, ('p', 'Geom$47$get_modified', 'pp'), ['Thread*']),
        ('d', 26, 0, ('p', 'Geom$48$get_modified', 'p'), []),
    ]
    c.ct['get_nested_vertices'] = [
        ('d', 'i', 1, ('i', 'Geom$55$get_nested_vertices', 'pp'), ['Thread*']),
        ('d', 'i', 0, ('i', 'Geom$56$get_nested_vertices', 'p'), []),
    ]
    c.ct['get_num_bytes'] = [
        ('d', 'i', 0, ('i', 'Geom$46$get_num_bytes', 'p'), []),
    ]
    c.ct['get_num_primitives'] = [
        ('d', 'l', 0, ('l', 'Geom$19$get_num_primitives', 'p'), []),
    ]
    c.ct['get_primitive'] = [
        ('d', 82, 1, ('p', 'Geom$20$get_primitive', 'pl'), ['std::size_t']),
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
        ('d', 81, 1, ('p', 'Geom$10$get_vertex_data', 'pp'), ['Thread*']),
        ('d', 81, 0, ('p', 'Geom$11$get_vertex_data', 'p'), []),
    ]
    c.ct['insert_primitive'] = [
        ('d', 'v', 2, ('v', 'Geom$23$insert_primitive', 'plp'), ['std::size_t', 'GeomPrimitive const*']),
    ]
    c.ct['is_empty'] = [
        ('d', 'B', 0, ('B', 'Geom$18$is_empty', 'p'), []),
    ]
    c.ct['is_prepared'] = [
        ('d', 'B', 1, ('B', 'Geom$68$is_prepared', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['make_adjacency'] = [
        ('d', 84, 0, ('p', 'Geom$35$make_adjacency', 'p'), []),
    ]
    c.ct['make_adjacency_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom$44$make_adjacency_in_place', 'p'), []),
    ]
    c.ct['make_copy'] = [
        ('d', 84, 0, ('p', 'Geom$4$make_copy', 'p'), []),
    ]
    c.ct['make_lines'] = [
        ('d', 84, 0, ('p', 'Geom$33$make_lines', 'p'), []),
    ]
    c.ct['make_lines_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom$42$make_lines_in_place', 'p'), []),
    ]
    c.ct['make_nonindexed'] = [
        ('d', 'i', 1, ('i', 'Geom$15$make_nonindexed', 'pB'), ['bool']),
    ]
    c.ct['make_patches'] = [
        ('d', 84, 0, ('p', 'Geom$34$make_patches', 'p'), []),
    ]
    c.ct['make_patches_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom$43$make_patches_in_place', 'p'), []),
    ]
    c.ct['make_points'] = [
        ('d', 84, 0, ('p', 'Geom$32$make_points', 'p'), []),
    ]
    c.ct['make_points_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom$41$make_points_in_place', 'p'), []),
    ]
    c.ct['mark_bounds_stale'] = [
        ('d', 'v', 0, ('v', 'Geom$57$mark_bounds_stale', 'p'), []),
    ]
    c.ct['modify_primitive'] = [
        ('d', 82, 1, ('p', 'Geom$21$modify_primitive', 'pl'), ['std::size_t']),
    ]
    c.ct['modify_vertex_data'] = [
        ('d', 81, 0, ('p', 'Geom$12$modify_vertex_data', 'p'), []),
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
        ('d', 'v', 1, ('v', 'Geom$25$remove_primitive', 'pl'), ['std::size_t']),
    ]
    c.ct['request_resident'] = [
        ('d', 'B', 0, ('B', 'Geom$49$request_resident', 'p'), []),
    ]
    c.ct['reverse'] = [
        ('d', 84, 0, ('p', 'Geom$29$reverse', 'p'), []),
    ]
    c.ct['reverse_in_place'] = [
        ('d', 'v', 0, ('v', 'Geom$38$reverse_in_place', 'p'), []),
    ]
    c.ct['rotate'] = [
        ('d', 84, 0, ('p', 'Geom$30$rotate', 'p'), []),
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
        ('d', 'v', 2, ('v', 'Geom$22$set_primitive', 'plp'), ['std::size_t', 'GeomPrimitive const*']),
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
        ('d', 84, 2, ('p', 'Geom$31$unify', 'piB'), ['int', 'bool']),
    ]
    c.ct['unify_in_place'] = [
        ('d', 'v', 2, ('v', 'Geom$40$unify_in_place', 'piB'), ['int', 'bool']),
    ]
    c.ct['upcast_to_CopyOnWriteObject'] = [
        ('d', 80, 0, ('p', 'Geom$1$upcast_to_CopyOnWriteObject', 'p'), []),
    ]
    c.ct['upcast_to_GeomEnums'] = [
        ('d', 5, 0, ('p', 'Geom$2$upcast_to_GeomEnums', 'p'), []),
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



class GeomVertexArrayData(CopyOnWriteObject, SimpleLruPage, GeomEnums):
    __bases__ = tuple([CopyOnWriteObject, SimpleLruPage, GeomEnums])
    c = cxx.cstructs()
    c.register("GeomVertexArrayData", "upanda3d", """libupanda3d_c.so""")

    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 85, 1, ('p', 'GeomVertexArrayData$4$GeomVertexArrayData', 'p'), ['GeomVertexArrayData const&']),
        ('s', 85, 2, ('p', 'GeomVertexArrayData$5$GeomVertexArrayData', 'pp'), ['GeomVertexArrayFormat const*', 'GeomEnums::UsageHint']),
    ]

    # classmethod type calls

    c.ct['get_book'] = [
        ('s', 'p', 0, ('p', 'GeomVertexArrayData$35$get_book', ''), []),
    ]
    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'GeomVertexArrayData$41$get_class_type', ''), []),
    ]
    c.ct['get_independent_lru'] = [
        ('s', 'p', 0, ('p', 'GeomVertexArrayData$32$get_independent_lru', ''), []),
    ]
    c.ct['get_small_lru'] = [
        ('s', 'p', 0, ('p', 'GeomVertexArrayData$33$get_small_lru', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'GeomVertexArrayData$42$init_type', ''), []),
    ]
    c.ct['lru_epoch'] = [
        ('s', 'v', 0, ('v', 'GeomVertexArrayData$34$lru_epoch', ''), []),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'GeomVertexArrayData$37$register_with_read_factory', ''), []),
    ]

    @classmethod
    def get_book(cls, *args,**kw):
        return ( cls.c.get('get_book', None) or cls.c.call(GeomVertexArrayData, 'get_book', None) )(*args,**kw)

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(GeomVertexArrayData, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def get_independent_lru(cls, *args,**kw):
        return ( cls.c.get('get_independent_lru', None) or cls.c.call(GeomVertexArrayData, 'get_independent_lru', None) )(*args,**kw)

    @classmethod
    def get_small_lru(cls, *args,**kw):
        return ( cls.c.get('get_small_lru', None) or cls.c.call(GeomVertexArrayData, 'get_small_lru', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(GeomVertexArrayData, 'init_type', None) )(*args,**kw)

    @classmethod
    def lru_epoch(cls, *args,**kw):
        return ( cls.c.get('lru_epoch', None) or cls.c.call(GeomVertexArrayData, 'lru_epoch', None) )(*args,**kw)

    @classmethod
    def register_with_read_factory(cls, *args,**kw):
        return ( cls.c.get('register_with_read_factory', None) or cls.c.call(GeomVertexArrayData, 'register_with_read_factory', None) )(*args,**kw)

    # instance method type calls

    c.ct['clear_rows'] = [
        ('d', 'v', 0, ('v', 'GeomVertexArrayData$15$clear_rows', 'p'), []),
    ]
    c.ct['compare_to'] = [
        ('d', 'i', 1, ('i', 'GeomVertexArrayData$6$compare_to', 'pp'), ['GeomVertexArrayData const&']),
    ]
    c.ct['evict_lru'] = [
        ('d', 'v', 0, ('v', 'GeomVertexArrayData$36$evict_lru', 'p'), []),
    ]
    c.ct['finalize'] = [
        ('d', 'v', 1, ('v', 'GeomVertexArrayData$40$finalize', 'pp'), ['BamReader*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'GeomVertexArrayData$44$force_init_type', 'p'), []),
    ]
    c.ct['get_array_format'] = [
        ('d', 66, 0, ('p', 'GeomVertexArrayData$7$get_array_format', 'p'), []),
    ]
    c.ct['get_data_size_bytes'] = [
        ('d', 'l', 0, ('l', 'GeomVertexArrayData$16$get_data_size_bytes', 'p'), []),
    ]
    c.ct['get_handle'] = [
        ('d', 56, 1, ('p', 'GeomVertexArrayData$23$get_handle', 'pp'), ['Thread*']),
        ('d', 56, 0, ('p', 'GeomVertexArrayData$24$get_handle', 'p'), []),
    ]
    c.ct['get_modified'] = [
        ('d', 26, 0, ('p', 'GeomVertexArrayData$17$get_modified', 'p'), []),
    ]
    c.ct['get_num_rows'] = [
        ('d', 'i', 0, ('i', 'GeomVertexArrayData$11$get_num_rows', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'GeomVertexArrayData$43$get_type', 'p'), []),
    ]
    c.ct['get_usage_hint'] = [
        ('d', 'p', 0, ('p', 'GeomVertexArrayData$8$get_usage_hint', 'p'), []),
    ]
    c.ct['has_column'] = [
        ('d', 'B', 1, ('B', 'GeomVertexArrayData$10$has_column', 'ps'), ['InternalName const*']),
    ]
    c.ct['is_prepared'] = [
        ('d', 'B', 1, ('B', 'GeomVertexArrayData$28$is_prepared', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['modify_handle'] = [
        ('d', 56, 1, ('p', 'GeomVertexArrayData$25$modify_handle', 'pp'), ['Thread*']),
        ('d', 56, 0, ('p', 'GeomVertexArrayData$26$modify_handle', 'p'), []),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'GeomVertexArrayData$18$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['prepare'] = [
        ('d', 'v', 1, ('v', 'GeomVertexArrayData$27$prepare', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['prepare_now'] = [
        ('d', 'p', 2, ('p', 'GeomVertexArrayData$29$prepare_now', 'ppp'), ['PreparedGraphicsObjects*', 'GraphicsStateGuardianBase*']),
    ]
    c.ct['read_raw_data'] = [
        ('d', 'p', 2, ('p', 'GeomVertexArrayData$39$read_raw_data', 'ppp'), ['BamReader*', 'DatagramIterator&']),
    ]
    c.ct['release'] = [
        ('d', 'B', 1, ('B', 'GeomVertexArrayData$30$release', 'pp'), ['PreparedGraphicsObjects*']),
    ]
    c.ct['release_all'] = [
        ('d', 'i', 0, ('i', 'GeomVertexArrayData$31$release_all', 'p'), []),
    ]
    c.ct['request_resident'] = [
        ('d', 'B', 1, ('B', 'GeomVertexArrayData$21$request_resident', 'pp'), ['Thread*']),
        ('d', 'B', 0, ('B', 'GeomVertexArrayData$22$request_resident', 'p'), []),
    ]
    c.ct['reserve_num_rows'] = [
        ('d', 'B', 1, ('B', 'GeomVertexArrayData$14$reserve_num_rows', 'pi'), ['int']),
    ]
    c.ct['set_num_rows'] = [
        ('d', 'B', 1, ('B', 'GeomVertexArrayData$12$set_num_rows', 'pi'), ['int']),
    ]
    c.ct['set_usage_hint'] = [
        ('d', 'v', 1, ('v', 'GeomVertexArrayData$9$set_usage_hint', 'pp'), ['GeomEnums::UsageHint']),
    ]
    c.ct['unclean_set_num_rows'] = [
        ('d', 'B', 1, ('B', 'GeomVertexArrayData$13$unclean_set_num_rows', 'pi'), ['int']),
    ]
    c.ct['upcast_to_CopyOnWriteObject'] = [
        ('d', 80, 0, ('p', 'GeomVertexArrayData$1$upcast_to_CopyOnWriteObject', 'p'), []),
    ]
    c.ct['upcast_to_GeomEnums'] = [
        ('d', 5, 0, ('p', 'GeomVertexArrayData$3$upcast_to_GeomEnums', 'p'), []),
    ]
    c.ct['upcast_to_SimpleLruPage'] = [
        ('d', 51, 0, ('p', 'GeomVertexArrayData$2$upcast_to_SimpleLruPage', 'p'), []),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'GeomVertexArrayData$19$write', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'v', 1, ('v', 'GeomVertexArrayData$20$write', 'pp'), ['std::ostream&']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'GeomVertexArrayData$38$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(GeomVertexArrayData, attr, self)

GeomVertexArrayData.c.link(GeomVertexArrayData)



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
        ('s', 86, 1, ('p', 'PandaNode$4$PandaNode', 's'), ['std::string const&']),
    ]

    # classmethod type calls

    c.ct['decode_from_bam_stream'] = [
        ('s', 86, 2, ('p', 'PandaNode$193$decode_from_bam_stream', 'pp'), ['vector_uchar', 'BamReader*']),
        ('s', 86, 1, ('p', 'PandaNode$194$decode_from_bam_stream', 'p'), ['vector_uchar']),
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
        ('d', 86, 1, ('p', 'PandaNode$5$combine_with', 'pp'), ['PandaNode*']),
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
        ('d', 86, 1, ('p', 'PandaNode$26$copy_subgraph', 'pp'), ['Thread*']),
        ('d', 86, 0, ('p', 'PandaNode$27$copy_subgraph', 'p'), []),
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
    c.ct['downcast_to_TextNode'] = [
        ('d', 91, 0, ('p', 'PandaNode$208$downcast_to_TextNode', 'p'), []),
    ]
    c.ct['dupe_for_flatten'] = [
        ('d', 86, 0, ('p', 'PandaNode$6$dupe_for_flatten', 'p'), []),
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
        ('d', 86, 2, ('p', 'PandaNode$36$get_child', 'pip'), ['int', 'Thread*']),
        ('d', 86, 1, ('p', 'PandaNode$37$get_child', 'pi'), ['int']),
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
        ('d', 70, 1, ('p', 'PandaNode$90$get_effect', 'pi'), ['TypeHandle']),
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
        ('d', 'l', 0, ('l', 'PandaNode$129$get_num_tags', 'p'), []),
    ]
    c.ct['get_off_clip_planes'] = [
        ('d', 'p', 1, ('p', 'PandaNode$155$get_off_clip_planes', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode$156$get_off_clip_planes', 'p'), []),
    ]
    c.ct['get_parent'] = [
        ('d', 86, 2, ('p', 'PandaNode$30$get_parent', 'pip'), ['int', 'Thread*']),
        ('d', 86, 1, ('p', 'PandaNode$31$get_parent', 'pi'), ['int']),
    ]
    c.ct['get_parents'] = [
        ('d', 'p', 1, ('p', 'PandaNode$198$get_parents', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode$199$get_parents', 'p'), []),
    ]
    c.ct['get_prev_transform'] = [
        ('d', 78, 1, ('p', 'PandaNode$113$get_prev_transform', 'pp'), ['Thread*']),
        ('d', 78, 0, ('p', 'PandaNode$114$get_prev_transform', 'p'), []),
    ]
    c.ct['get_stashed'] = [
        ('d', 'p', 1, ('p', 'PandaNode$62$get_stashed', 'pp'), ['Thread*']),
        ('d', 'p', 0, ('p', 'PandaNode$63$get_stashed', 'p'), []),
        ('d', 86, 2, ('p', 'PandaNode$64$get_stashed', 'pip'), ['int', 'Thread*']),
        ('d', 86, 1, ('p', 'PandaNode$65$get_stashed', 'pi'), ['int']),
    ]
    c.ct['get_stashed_sort'] = [
        ('d', 'i', 2, ('i', 'PandaNode$66$get_stashed_sort', 'pip'), ['int', 'Thread*']),
        ('d', 'i', 1, ('i', 'PandaNode$67$get_stashed_sort', 'pi'), ['int']),
    ]
    c.ct['get_state'] = [
        ('d', 79, 1, ('p', 'PandaNode$95$get_state', 'pp'), ['Thread*']),
        ('d', 79, 0, ('p', 'PandaNode$96$get_state', 'p'), []),
    ]
    c.ct['get_tag'] = [
        ('d', 's', 2, ('s', 'PandaNode$122$get_tag', 'psp'), ['std::string const&', 'Thread*']),
        ('d', 's', 1, ('s', 'PandaNode$123$get_tag', 'ps'), ['std::string const&']),
    ]
    c.ct['get_tag_key'] = [
        ('d', 's', 1, ('s', 'PandaNode$130$get_tag_key', 'pl'), ['std::size_t']),
    ]
    c.ct['get_tag_keys'] = [
        ('d', 'v', 1, ('v', 'PandaNode$128$get_tag_keys', 'pp'), ['vector_string&']),
    ]
    c.ct['get_transform'] = [
        ('d', 78, 1, ('p', 'PandaNode$107$get_transform', 'pp'), ['Thread*']),
        ('d', 78, 0, ('p', 'PandaNode$108$get_transform', 'p'), []),
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
        ('d', 86, 0, ('p', 'PandaNode$25$make_copy', 'p'), []),
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
        ('d', 15, 0, ('p', 'PandaNode$3$upcast_to_LinkedListNode', 'p'), []),
    ]
    c.ct['upcast_to_Namable'] = [
        ('d', 48, 0, ('p', 'PandaNode$2$upcast_to_Namable', 'p'), []),
    ]
    c.ct['upcast_to_TypedWritableReferenceCount'] = [
        ('d', 63, 0, ('p', 'PandaNode$1$upcast_to_TypedWritableReferenceCount', 'p'), []),
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
        ('s', 87, 2, ('p', 'LensNode$1$LensNode', 'sp'), ['std::string const&', 'Lens*']),
        ('s', 87, 1, ('p', 'LensNode$2$LensNode', 's'), ['std::string const&']),
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
        ('d', 71, 1, ('p', 'LensNode$8$get_lens', 'pi'), ['int']),
        ('d', 71, 0, ('p', 'LensNode$9$get_lens', 'p'), []),
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
        ('s', 88, 1, ('p', 'Camera$1$Camera', 'p'), ['Camera const&']),
        ('s', 88, 2, ('p', 'Camera$2$Camera', 'sp'), ['std::string const&', 'Lens*']),
        ('s', 88, 1, ('p', 'Camera$3$Camera', 's'), ['std::string const&']),
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
        ('d', 17, 0, ('p', 'Camera$16$get_cull_center', 'p'), []),
    ]
    c.ct['get_display_region'] = [
        ('d', 61, 1, ('p', 'Camera$12$get_display_region', 'pl'), ['std::size_t']),
    ]
    c.ct['get_initial_state'] = [
        ('d', 79, 0, ('p', 'Camera$22$get_initial_state', 'p'), []),
    ]
    c.ct['get_lod_center'] = [
        ('d', 17, 0, ('p', 'Camera$20$get_lod_center', 'p'), []),
    ]
    c.ct['get_lod_scale'] = [
        ('d', 'f', 0, ('f', 'Camera$26$get_lod_scale', 'p'), []),
    ]
    c.ct['get_num_display_regions'] = [
        ('d', 'l', 0, ('l', 'Camera$11$get_num_display_regions', 'p'), []),
    ]
    c.ct['get_scene'] = [
        ('d', 17, 0, ('p', 'Camera$10$get_scene', 'p'), []),
    ]
    c.ct['get_tag_state'] = [
        ('d', 79, 1, ('p', 'Camera$31$get_tag_state', 'ps'), ['std::string const&']),
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
        ('d', 86, 0, ('p', 'Camera$4$make_copy', 'p'), []),
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
        ('s', 89, 1, ('p', 'GeomNode$1$GeomNode', 's'), ['std::string const&']),
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
        ('d', 84, 1, ('p', 'GeomNode$12$get_geom', 'pi'), ['int']),
    ]
    c.ct['get_geom_state'] = [
        ('d', 79, 1, ('p', 'GeomNode$14$get_geom_state', 'pi'), ['int']),
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
        ('d', 84, 1, ('p', 'GeomNode$13$modify_geom', 'pi'), ['int']),
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



class Fog(PandaNode):
    __bases__ = tuple([PandaNode])
    c = cxx.cstructs()
    c.register("Fog", "upanda3d", """libupanda3d_c.so""")

    # enum Mode

    M_exponential = const(1)
    M_exponential_squared = const(2)
    M_linear = const(0)


    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 90, 1, ('p', 'Fog$1$Fog', 's'), ['std::string const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'Fog$21$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'Fog$22$init_type', ''), []),
    ]
    c.ct['register_with_read_factory'] = [
        ('s', 'v', 0, ('v', 'Fog$19$register_with_read_factory', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(Fog, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(Fog, 'init_type', None) )(*args,**kw)

    @classmethod
    def register_with_read_factory(cls, *args,**kw):
        return ( cls.c.get('register_with_read_factory', None) or cls.c.call(Fog, 'register_with_read_factory', None) )(*args,**kw)

    # instance method type calls

    c.ct['adjust_to_camera'] = [
        ('d', 'v', 1, ('v', 'Fog$18$adjust_to_camera', 'pp'), ['TransformState const*']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'Fog$24$force_init_type', 'p'), []),
    ]
    c.ct['get_color'] = [
        ('d', 'p', 0, ('p', 'Fog$5$get_color', 'p'), []),
    ]
    c.ct['get_exp_density'] = [
        ('d', 'f', 0, ('f', 'Fog$16$get_exp_density', 'p'), []),
    ]
    c.ct['get_linear_onset_point'] = [
        ('d', 33, 0, ('p', 'Fog$9$get_linear_onset_point', 'p'), []),
    ]
    c.ct['get_linear_opaque_point'] = [
        ('d', 33, 0, ('p', 'Fog$12$get_linear_opaque_point', 'p'), []),
    ]
    c.ct['get_mode'] = [
        ('d', 'p', 0, ('p', 'Fog$3$get_mode', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'Fog$23$get_type', 'p'), []),
    ]
    c.ct['set_color'] = [
        ('d', 'v', 1, ('v', 'Fog$6$set_color', 'pp'), ['LColor const&']),
        ('d', 'v', 3, ('v', 'Fog$7$set_color', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_exp_density'] = [
        ('d', 'v', 1, ('v', 'Fog$17$set_exp_density', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_linear_fallback'] = [
        ('d', 'v', 3, ('v', 'Fog$15$set_linear_fallback', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_linear_onset_point'] = [
        ('d', 'v', 1, ('v', 'Fog$10$set_linear_onset_point', 'pp'), ['LPoint3 const&']),
        ('d', 'v', 3, ('v', 'Fog$11$set_linear_onset_point', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_linear_opaque_point'] = [
        ('d', 'v', 1, ('v', 'Fog$13$set_linear_opaque_point', 'pp'), ['LPoint3 const&']),
        ('d', 'v', 3, ('v', 'Fog$14$set_linear_opaque_point', 'pfff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_linear_range'] = [
        ('d', 'v', 2, ('v', 'Fog$8$set_linear_range', 'pff'), ['PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_mode'] = [
        ('d', 'v', 1, ('v', 'Fog$4$set_mode', 'pp'), ['Fog::Mode']),
    ]
    c.ct['write_datagram'] = [
        ('d', 'v', 2, ('v', 'Fog$20$write_datagram', 'ppp'), ['BamWriter*', 'Datagram&']),
    ]
    c.ct['xform'] = [
        ('d', 'v', 1, ('v', 'Fog$2$xform', 'pp'), ['LMatrix4 const&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(Fog, attr, self)

Fog.c.link(Fog)



class TextNode(PandaNode, TextEncoder, TextProperties):
    __bases__ = tuple([PandaNode, TextEncoder, TextProperties])
    c = cxx.cstructs()
    c.register("TextNode", "upanda3d", """libupanda3d_c.so""")

    # enum FlattenFlags

    FF_dynamic_merge = const(8)
    FF_light = const(1)
    FF_medium = const(2)
    FF_none = const(0)
    FF_strong = const(4)


    # ctor/dtor

    c.ct['ctor'] = [
        ('s', 91, 1, ('p', 'TextNode$4$TextNode', 's'), ['std::string const&']),
        ('s', 91, 2, ('p', 'TextNode$5$TextNode', 'sp'), ['std::string const&', 'TextProperties const&']),
    ]

    # classmethod type calls

    c.ct['get_class_type'] = [
        ('s', 'i', 0, ('i', 'TextNode$142$get_class_type', ''), []),
    ]
    c.ct['init_type'] = [
        ('s', 'v', 0, ('v', 'TextNode$143$init_type', ''), []),
    ]

    @classmethod
    def get_class_type(cls, *args,**kw):
        return ( cls.c.get('get_class_type', None) or cls.c.call(TextNode, 'get_class_type', None) )(*args,**kw)

    @classmethod
    def init_type(cls, *args,**kw):
        return ( cls.c.get('init_type', None) or cls.c.call(TextNode, 'init_type', None) )(*args,**kw)

    # instance method type calls

    c.ct['apply_attribs_to_vertices'] = [
        ('d', 'v', 3, ('v', 'TextNode$138$apply_attribs_to_vertices', 'ppip'), ['AccumulatedAttribs const&', 'int', 'GeomTransformer&']),
    ]
    c.ct['calc_width'] = [
        ('d', 'f', 1, ('f', 'TextNode$90$calc_width', 'ps'), ['std::string const&']),
        ('d', 'f', 1, ('f', 'TextNode$91$calc_width', 'ps'), ['std::wstring const&']),
        ('d', 'f', 1, ('f', 'TextNode$92$calc_width', 'pp'), ['wchar_t']),
    ]
    c.ct['clear_align'] = [
        ('d', 'v', 0, ('v', 'TextNode$65$clear_align', 'p'), []),
    ]
    c.ct['clear_bin'] = [
        ('d', 'v', 0, ('v', 'TextNode$80$clear_bin', 'p'), []),
    ]
    c.ct['clear_card'] = [
        ('d', 'v', 0, ('v', 'TextNode$41$clear_card', 'p'), []),
    ]
    c.ct['clear_card_border'] = [
        ('d', 'v', 0, ('v', 'TextNode$16$clear_card_border', 'p'), []),
    ]
    c.ct['clear_card_texture'] = [
        ('d', 'v', 0, ('v', 'TextNode$24$clear_card_texture', 'p'), []),
    ]
    c.ct['clear_draw_order'] = [
        ('d', 'v', 0, ('v', 'TextNode$82$clear_draw_order', 'p'), []),
    ]
    c.ct['clear_font'] = [
        ('d', 'v', 0, ('v', 'TextNode$57$clear_font', 'p'), []),
    ]
    c.ct['clear_frame'] = [
        ('d', 'v', 0, ('v', 'TextNode$29$clear_frame', 'p'), []),
    ]
    c.ct['clear_glyph_scale'] = [
        ('d', 'v', 0, ('v', 'TextNode$86$clear_glyph_scale', 'p'), []),
    ]
    c.ct['clear_glyph_shift'] = [
        ('d', 'v', 0, ('v', 'TextNode$88$clear_glyph_shift', 'p'), []),
    ]
    c.ct['clear_indent'] = [
        ('d', 'v', 0, ('v', 'TextNode$67$clear_indent', 'p'), []),
    ]
    c.ct['clear_max_rows'] = [
        ('d', 'v', 0, ('v', 'TextNode$8$clear_max_rows', 'p'), []),
    ]
    c.ct['clear_shadow'] = [
        ('d', 'v', 0, ('v', 'TextNode$78$clear_shadow', 'p'), []),
    ]
    c.ct['clear_shadow_color'] = [
        ('d', 'v', 0, ('v', 'TextNode$75$clear_shadow_color', 'p'), []),
    ]
    c.ct['clear_slant'] = [
        ('d', 'v', 0, ('v', 'TextNode$63$clear_slant', 'p'), []),
    ]
    c.ct['clear_small_caps'] = [
        ('d', 'v', 0, ('v', 'TextNode$59$clear_small_caps', 'p'), []),
    ]
    c.ct['clear_small_caps_scale'] = [
        ('d', 'v', 0, ('v', 'TextNode$61$clear_small_caps_scale', 'p'), []),
    ]
    c.ct['clear_tab_width'] = [
        ('d', 'v', 0, ('v', 'TextNode$84$clear_tab_width', 'p'), []),
    ]
    c.ct['clear_text_color'] = [
        ('d', 'v', 0, ('v', 'TextNode$72$clear_text_color', 'p'), []),
    ]
    c.ct['clear_wordwrap'] = [
        ('d', 'v', 0, ('v', 'TextNode$69$clear_wordwrap', 'p'), []),
    ]
    c.ct['cull_callback'] = [
        ('d', 'B', 2, ('B', 'TextNode$139$cull_callback', 'ppp'), ['CullTraverser*', 'CullTraverserData&']),
    ]
    c.ct['force_init_type'] = [
        ('d', 'i', 0, ('i', 'TextNode$145$force_init_type', 'p'), []),
    ]
    c.ct['force_update'] = [
        ('d', 'v', 0, ('v', 'TextNode$111$force_update', 'p'), []),
    ]
    c.ct['generate'] = [
        ('d', 86, 0, ('p', 'TextNode$109$generate', 'p'), []),
    ]
    c.ct['get_align'] = [
        ('d', 'p', 0, ('p', 'TextNode$121$get_align', 'p'), []),
    ]
    c.ct['get_bin'] = [
        ('d', 's', 0, ('s', 'TextNode$129$get_bin', 'p'), []),
    ]
    c.ct['get_bottom'] = [
        ('d', 'f', 0, ('f', 'TextNode$102$get_bottom', 'p'), []),
    ]
    c.ct['get_card_actual'] = [
        ('d', 12, 0, ('p', 'TextNode$46$get_card_actual', 'p'), []),
    ]
    c.ct['get_card_as_set'] = [
        ('d', 12, 0, ('p', 'TextNode$45$get_card_as_set', 'p'), []),
    ]
    c.ct['get_card_border_size'] = [
        ('d', 'f', 0, ('f', 'TextNode$17$get_card_border_size', 'p'), []),
    ]
    c.ct['get_card_border_uv_portion'] = [
        ('d', 'f', 0, ('f', 'TextNode$18$get_card_border_uv_portion', 'p'), []),
    ]
    c.ct['get_card_color'] = [
        ('d', 'p', 0, ('p', 'TextNode$22$get_card_color', 'p'), []),
    ]
    c.ct['get_card_decal'] = [
        ('d', 'B', 0, ('B', 'TextNode$43$get_card_decal', 'p'), []),
    ]
    c.ct['get_card_texture'] = [
        ('d', 64, 0, ('p', 'TextNode$26$get_card_texture', 'p'), []),
    ]
    c.ct['get_card_transformed'] = [
        ('d', 12, 0, ('p', 'TextNode$47$get_card_transformed', 'p'), []),
    ]
    c.ct['get_coordinate_system'] = [
        ('d', 'p', 0, ('p', 'TextNode$51$get_coordinate_system', 'p'), []),
    ]
    c.ct['get_draw_order'] = [
        ('d', 'i', 0, ('i', 'TextNode$130$get_draw_order', 'p'), []),
    ]
    c.ct['get_flatten_flags'] = [
        ('d', 'i', 0, ('i', 'TextNode$55$get_flatten_flags', 'p'), []),
    ]
    c.ct['get_font'] = [
        ('d', 59, 0, ('p', 'TextNode$113$get_font', 'p'), []),
    ]
    c.ct['get_frame_actual'] = [
        ('d', 12, 0, ('p', 'TextNode$33$get_frame_actual', 'p'), []),
    ]
    c.ct['get_frame_as_set'] = [
        ('d', 12, 0, ('p', 'TextNode$32$get_frame_as_set', 'p'), []),
    ]
    c.ct['get_frame_color'] = [
        ('d', 'p', 0, ('p', 'TextNode$14$get_frame_color', 'p'), []),
    ]
    c.ct['get_frame_corners'] = [
        ('d', 'B', 0, ('B', 'TextNode$37$get_frame_corners', 'p'), []),
    ]
    c.ct['get_frame_line_width'] = [
        ('d', 'f', 0, ('f', 'TextNode$35$get_frame_line_width', 'p'), []),
    ]
    c.ct['get_glyph_scale'] = [
        ('d', 'f', 0, ('f', 'TextNode$132$get_glyph_scale', 'p'), []),
    ]
    c.ct['get_glyph_shift'] = [
        ('d', 'f', 0, ('f', 'TextNode$133$get_glyph_shift', 'p'), []),
    ]
    c.ct['get_height'] = [
        ('d', 'f', 0, ('f', 'TextNode$104$get_height', 'p'), []),
    ]
    c.ct['get_indent'] = [
        ('d', 'f', 0, ('f', 'TextNode$122$get_indent', 'p'), []),
    ]
    c.ct['get_internal_geom'] = [
        ('d', 86, 0, ('p', 'TextNode$112$get_internal_geom', 'p'), []),
    ]
    c.ct['get_left'] = [
        ('d', 'f', 0, ('f', 'TextNode$100$get_left', 'p'), []),
    ]
    c.ct['get_line_height'] = [
        ('d', 'f', 0, ('f', 'TextNode$6$get_line_height', 'p'), []),
    ]
    c.ct['get_lower_right_3d'] = [
        ('d', 33, 0, ('p', 'TextNode$107$get_lower_right_3d', 'p'), []),
    ]
    c.ct['get_max_rows'] = [
        ('d', 'i', 0, ('i', 'TextNode$10$get_max_rows', 'p'), []),
    ]
    c.ct['get_num_rows'] = [
        ('d', 'i', 0, ('i', 'TextNode$108$get_num_rows', 'p'), []),
    ]
    c.ct['get_preserve_trailing_whitespace'] = [
        ('d', 'B', 0, ('B', 'TextNode$124$get_preserve_trailing_whitespace', 'p'), []),
    ]
    c.ct['get_right'] = [
        ('d', 'f', 0, ('f', 'TextNode$101$get_right', 'p'), []),
    ]
    c.ct['get_shadow'] = [
        ('d', 39, 0, ('p', 'TextNode$128$get_shadow', 'p'), []),
    ]
    c.ct['get_shadow_color'] = [
        ('d', 'p', 0, ('p', 'TextNode$127$get_shadow_color', 'p'), []),
    ]
    c.ct['get_slant'] = [
        ('d', 'f', 0, ('f', 'TextNode$116$get_slant', 'p'), []),
    ]
    c.ct['get_small_caps'] = [
        ('d', 'B', 0, ('B', 'TextNode$114$get_small_caps', 'p'), []),
    ]
    c.ct['get_small_caps_scale'] = [
        ('d', 'f', 0, ('f', 'TextNode$115$get_small_caps_scale', 'p'), []),
    ]
    c.ct['get_tab_width'] = [
        ('d', 'f', 0, ('f', 'TextNode$131$get_tab_width', 'p'), []),
    ]
    c.ct['get_text_color'] = [
        ('d', 'p', 0, ('p', 'TextNode$126$get_text_color', 'p'), []),
    ]
    c.ct['get_text_scale'] = [
        ('d', 'f', 0, ('f', 'TextNode$134$get_text_scale', 'p'), []),
    ]
    c.ct['get_top'] = [
        ('d', 'f', 0, ('f', 'TextNode$103$get_top', 'p'), []),
    ]
    c.ct['get_transform'] = [
        ('d', 'p', 0, ('p', 'TextNode$49$get_transform', 'p'), []),
    ]
    c.ct['get_type'] = [
        ('d', 'i', 0, ('i', 'TextNode$144$get_type', 'p'), []),
    ]
    c.ct['get_underscore'] = [
        ('d', 'B', 0, ('B', 'TextNode$117$get_underscore', 'p'), []),
    ]
    c.ct['get_underscore_height'] = [
        ('d', 'f', 0, ('f', 'TextNode$119$get_underscore_height', 'p'), []),
    ]
    c.ct['get_unsafe_to_apply_attribs'] = [
        ('d', 'i', 0, ('i', 'TextNode$137$get_unsafe_to_apply_attribs', 'p'), []),
    ]
    c.ct['get_upper_left_3d'] = [
        ('d', 33, 0, ('p', 'TextNode$106$get_upper_left_3d', 'p'), []),
    ]
    c.ct['get_usage_hint'] = [
        ('d', 'p', 0, ('p', 'TextNode$53$get_usage_hint', 'p'), []),
    ]
    c.ct['get_width'] = [
        ('d', 'f', 0, ('f', 'TextNode$105$get_width', 'p'), []),
    ]
    c.ct['get_wordwrap'] = [
        ('d', 'f', 0, ('f', 'TextNode$123$get_wordwrap', 'p'), []),
    ]
    c.ct['get_wordwrapped_text'] = [
        ('d', 's', 0, ('s', 'TextNode$89$get_wordwrapped_text', 'p'), []),
    ]
    c.ct['get_wordwrapped_wtext'] = [
        ('d', 's', 0, ('s', 'TextNode$96$get_wordwrapped_wtext', 'p'), []),
    ]
    c.ct['has_card'] = [
        ('d', 'B', 0, ('B', 'TextNode$42$has_card', 'p'), []),
    ]
    c.ct['has_card_border'] = [
        ('d', 'B', 0, ('B', 'TextNode$19$has_card_border', 'p'), []),
    ]
    c.ct['has_card_texture'] = [
        ('d', 'B', 0, ('B', 'TextNode$25$has_card_texture', 'p'), []),
    ]
    c.ct['has_character'] = [
        ('d', 'B', 1, ('B', 'TextNode$94$has_character', 'pp'), ['wchar_t']),
    ]
    c.ct['has_exact_character'] = [
        ('d', 'B', 1, ('B', 'TextNode$93$has_exact_character', 'pp'), ['wchar_t']),
    ]
    c.ct['has_frame'] = [
        ('d', 'B', 0, ('B', 'TextNode$30$has_frame', 'p'), []),
    ]
    c.ct['has_max_rows'] = [
        ('d', 'B', 0, ('B', 'TextNode$9$has_max_rows', 'p'), []),
    ]
    c.ct['has_overflow'] = [
        ('d', 'B', 0, ('B', 'TextNode$11$has_overflow', 'p'), []),
    ]
    c.ct['is_card_as_margin'] = [
        ('d', 'B', 0, ('B', 'TextNode$44$is_card_as_margin', 'p'), []),
    ]
    c.ct['is_frame_as_margin'] = [
        ('d', 'B', 0, ('B', 'TextNode$31$is_frame_as_margin', 'p'), []),
    ]
    c.ct['is_renderable'] = [
        ('d', 'B', 0, ('B', 'TextNode$140$is_renderable', 'p'), []),
    ]
    c.ct['is_whitespace'] = [
        ('d', 'B', 1, ('B', 'TextNode$95$is_whitespace', 'pp'), ['wchar_t']),
    ]
    c.ct['output'] = [
        ('d', 'v', 1, ('v', 'TextNode$97$output', 'pp'), ['std::ostream&']),
    ]
    c.ct['r_prepare_scene'] = [
        ('d', 'v', 4, ('v', 'TextNode$141$r_prepare_scene', 'ppppp'), ['GraphicsStateGuardianBase*', 'RenderState const*', 'GeomTransformer&', 'Thread*']),
    ]
    c.ct['set_align'] = [
        ('d', 'v', 1, ('v', 'TextNode$64$set_align', 'pp'), ['TextProperties::Alignment']),
    ]
    c.ct['set_bin'] = [
        ('d', 'v', 1, ('v', 'TextNode$79$set_bin', 'ps'), ['std::string const&']),
    ]
    c.ct['set_card_actual'] = [
        ('d', 'v', 4, ('v', 'TextNode$39$set_card_actual', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_card_as_margin'] = [
        ('d', 'v', 4, ('v', 'TextNode$38$set_card_as_margin', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_card_border'] = [
        ('d', 'v', 2, ('v', 'TextNode$15$set_card_border', 'pff'), ['PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_card_color'] = [
        ('d', 'v', 1, ('v', 'TextNode$20$set_card_color', 'pp'), ['LColor const&']),
        ('d', 'v', 4, ('v', 'TextNode$21$set_card_color', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_card_decal'] = [
        ('d', 'v', 1, ('v', 'TextNode$40$set_card_decal', 'pB'), ['bool']),
    ]
    c.ct['set_card_texture'] = [
        ('d', 'v', 1, ('v', 'TextNode$23$set_card_texture', 'pp'), ['Texture*']),
    ]
    c.ct['set_coordinate_system'] = [
        ('d', 'v', 1, ('v', 'TextNode$50$set_coordinate_system', 'pp'), ['CoordinateSystem']),
    ]
    c.ct['set_draw_order'] = [
        ('d', 'i', 1, ('i', 'TextNode$81$set_draw_order', 'pi'), ['int']),
    ]
    c.ct['set_flatten_flags'] = [
        ('d', 'v', 1, ('v', 'TextNode$54$set_flatten_flags', 'pi'), ['int']),
    ]
    c.ct['set_font'] = [
        ('d', 'v', 1, ('v', 'TextNode$56$set_font', 'pp'), ['TextFont*']),
    ]
    c.ct['set_frame_actual'] = [
        ('d', 'v', 4, ('v', 'TextNode$28$set_frame_actual', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_frame_as_margin'] = [
        ('d', 'v', 4, ('v', 'TextNode$27$set_frame_as_margin', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_frame_color'] = [
        ('d', 'v', 1, ('v', 'TextNode$12$set_frame_color', 'pp'), ['LColor const&']),
        ('d', 'v', 4, ('v', 'TextNode$13$set_frame_color', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_frame_corners'] = [
        ('d', 'v', 1, ('v', 'TextNode$36$set_frame_corners', 'pB'), ['bool']),
    ]
    c.ct['set_frame_line_width'] = [
        ('d', 'v', 1, ('v', 'TextNode$34$set_frame_line_width', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_glyph_scale'] = [
        ('d', 'v', 1, ('v', 'TextNode$85$set_glyph_scale', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_glyph_shift'] = [
        ('d', 'v', 1, ('v', 'TextNode$87$set_glyph_shift', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_indent'] = [
        ('d', 'v', 1, ('v', 'TextNode$66$set_indent', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_max_rows'] = [
        ('d', 'v', 1, ('v', 'TextNode$7$set_max_rows', 'pi'), ['int']),
    ]
    c.ct['set_preserve_trailing_whitespace'] = [
        ('d', 'v', 1, ('v', 'TextNode$125$set_preserve_trailing_whitespace', 'pB'), ['bool']),
    ]
    c.ct['set_shadow'] = [
        ('d', 'v', 1, ('v', 'TextNode$76$set_shadow', 'pp'), ['LVecBase2 const&']),
        ('d', 'v', 2, ('v', 'TextNode$77$set_shadow', 'pff'), ['PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_shadow_color'] = [
        ('d', 'v', 1, ('v', 'TextNode$73$set_shadow_color', 'pp'), ['LColor const&']),
        ('d', 'v', 4, ('v', 'TextNode$74$set_shadow_color', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_slant'] = [
        ('d', 'v', 1, ('v', 'TextNode$62$set_slant', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_small_caps'] = [
        ('d', 'v', 1, ('v', 'TextNode$58$set_small_caps', 'pB'), ['bool']),
    ]
    c.ct['set_small_caps_scale'] = [
        ('d', 'v', 1, ('v', 'TextNode$60$set_small_caps_scale', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_tab_width'] = [
        ('d', 'v', 1, ('v', 'TextNode$83$set_tab_width', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_text_color'] = [
        ('d', 'v', 1, ('v', 'TextNode$70$set_text_color', 'pp'), ['LColor const&']),
        ('d', 'v', 4, ('v', 'TextNode$71$set_text_color', 'pffff'), ['PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat', 'PN_stdfloat']),
    ]
    c.ct['set_text_scale'] = [
        ('d', 'v', 1, ('v', 'TextNode$135$set_text_scale', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_transform'] = [
        ('d', 'v', 1, ('v', 'TextNode$48$set_transform', 'pp'), ['LMatrix4 const&']),
    ]
    c.ct['set_underscore'] = [
        ('d', 'v', 1, ('v', 'TextNode$118$set_underscore', 'pB'), ['bool']),
    ]
    c.ct['set_underscore_height'] = [
        ('d', 'v', 1, ('v', 'TextNode$120$set_underscore_height', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['set_usage_hint'] = [
        ('d', 'v', 1, ('v', 'TextNode$52$set_usage_hint', 'pp'), ['GeomEnums::UsageHint']),
    ]
    c.ct['set_wordwrap'] = [
        ('d', 'v', 1, ('v', 'TextNode$68$set_wordwrap', 'pf'), ['PN_stdfloat']),
    ]
    c.ct['text_changed'] = [
        ('d', 'v', 0, ('v', 'TextNode$136$text_changed', 'p'), []),
    ]
    c.ct['upcast_to_PandaNode'] = [
        ('d', 86, 0, ('p', 'TextNode$1$upcast_to_PandaNode', 'p'), []),
    ]
    c.ct['upcast_to_TextEncoder'] = [
        ('d', 22, 0, ('p', 'TextNode$2$upcast_to_TextEncoder', 'p'), []),
    ]
    c.ct['upcast_to_TextProperties'] = [
        ('d', 23, 0, ('p', 'TextNode$3$upcast_to_TextProperties', 'p'), []),
    ]
    c.ct['update'] = [
        ('d', 'v', 0, ('v', 'TextNode$110$update', 'p'), []),
    ]
    c.ct['write'] = [
        ('d', 'v', 2, ('v', 'TextNode$98$write', 'ppi'), ['std::ostream&', 'int']),
        ('d', 'v', 1, ('v', 'TextNode$99$write', 'pp'), ['std::ostream&']),
    ]


    # c++ instance methods

    def __del__(self):
        self.c.destroy(self)

    def __getattr__(self, attr):
        return self.c.get(attr,None) or  self.c.call(TextNode, attr, self)

TextNode.c.link(TextNode)




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

    #print("--- test3 with refcounting ----")
    #test()

    if len(sys.argv) and sys.argv[-1].endswith('.py'):
        code = compile( open( sys.argv[-1], 'r').read(), sys.argv[-1] , 'exec' )
        exec( code, globals() , globals() )




    del test
    gc.collect()
    gc.collect()

    cxx.gc()


