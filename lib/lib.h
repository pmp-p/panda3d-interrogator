#ifndef MVIEW_H


#include "pandabase.h"
#include "notifyCategoryProxy.h"
#include "dconfig.h"
#include "dtoolbase.h"

//NotifyCategoryDecl(lib, EXPCL_LIB, EXPTP_LIB);


#include "pandaFramework.h"
#include "pandaSystem.h"


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
#else
#pragma message "hiding I_ inherited"
#endif



#define FRAMEWORK PandaFramework

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

        void attach(NodePath *mdl);

        void op_pos(NodePath *np, LVecBase3f *v3f);
        void op_scale(NodePath *np, LVecBase3f *v3f);


        void build(); //WindowFramework* window_framework);

        void step();

        static std::string get_version_string();
        MAKE_PROPERTY(version_string, get_version_string);


        static void call_exit(const Event* event, void* data);


        PT(WindowFramework) wframe;

        FRAMEWORK * framework;
};



#define MVIEW_H
#endif
