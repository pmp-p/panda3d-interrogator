#ifndef MVIEW_H


#include "pandabase.h"
#include "notifyCategoryProxy.h"
#include "dconfig.h"
#include "dtoolbase.h"

#include "pandaFramework.h"
#include "pandaSystem.h"
#include "load_prc_file.h"

//NotifyCategoryDecl(lib, EXPCL_LIB, EXPTP_LIB);


#if 0 //.def CPPPARSER
class EXPORT_CLASS I_NodePath : public NodePath::NodePath
{
    PUBLISHED:
        void reparent_to(const NodePath &other);
        void look_at(PN_stdfloat x, PN_stdfloat y, PN_stdfloat z);
        //void set_scale(PN_stdfloat sx, PN_stdfloat sy, PN_stdfloat sz);
        //void set_pos(PN_stdfloat x, PN_stdfloat y, PN_stdfloat z);
        void set_pos(LVecBase3f const&);
        void set_scale(LVecBase3f const&);
};

class EXPORT_CLASS GeomT : public GeomTriangles
{
    PUBLISHED:
        ~GeomT();
};



#else
#pragma message "hiding I_ inherited"
#endif



#define FRAMEWORK PandaFramework


#define str const char*


static int alive = 1;

class EXPORT_CLASS Engine
{

    PUBLISHED:

        Engine();
        ~Engine();


        void dtor();

        static void stop();

        static int is_alive();

        int HelloEngine();

        int casetest(int i,std::string s,bool b);

        NodePath * load_model(const char *filename);

        GeomVertexWriter * new_GeomVertexWriter(GeomVertexData *data, const char *gvw_name);

        void add_primitive(Geom *geom, GeomTriangles *pri);

        void close_primitive(GeomTriangles *pri);

        PT(GeomTriangles) new_GeomTriangles();

        NodePath * new_Cube(float size, str geom_name, str gvd_name);

        void attach(NodePath *mdl);

        static int inc_ref(ReferenceCount * rc);
        static int dec_ref(ReferenceCount * rc);

        static void prc(const Filename &filename) ;
        static void prc(str name, str data);

        void build();

        void step();

        static std::string get_version_string();
        MAKE_PROPERTY(version_string, get_version_string);

        static void call_exit(const Event* event, void* data);

        WindowFramework * wframe;

        FRAMEWORK * framework;
};



#define MVIEW_H
#endif
