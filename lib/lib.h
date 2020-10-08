#ifndef LIB_H



#include "pandabase.h"
#include "notifyCategoryProxy.h"
#include "dconfig.h"
#include "dtoolbase.h"

#include "pandaFramework.h"
#include "pandaSystem.h"
#include "load_prc_file.h"




//-------------------------- dict -----------------------------------------------------------------
typedef std::pair<std::string, std::string> Pair;

typedef std::map<std::pair<std::string, std::string>, int> Dict;

typedef Dict::const_iterator It;
/*
PARSE ERROR in interrogator/igate_to_json.py : 34
Pair dict_slot( std::string k , std::string v ) {
    return std::make_pair(k,v);
}
*/

Pair dict_slot( const char * k , const char * v ) {
    return std::make_pair(std::string(k),std::string(v));
}



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



#define LIB_H
#endif








#ifndef CACTOR_H_
#define CACTOR_H_

#include "auto_bind.h"
#include "character.h"
#include "pandaFramework.h"

typedef std::vector < std::string > NameVec;
typedef std::map < std::string, NameVec > AnimMap;

class EXPORT_CLASS CActor:public NodePath, public AnimControlCollection {
  PUBLISHED:



    CActor();
    virtual ~ CActor();

    Dict anim_map ;
//    AnimMap * new_map();

    void add(str path,str name);

    void load_actor(WindowFramework * windowFrameworkPtr,
                                const std::string & actorFilename, const AnimMap * animMapPtr, int hierarchyMatchFlags);
    NodePath control_joint(const std::string & jointName);
    NodePath expose_joint(const std::string & jointName);

  private:

    typedef std::vector < NodePath > NodePathVec;

    void load_anims(const AnimMap * animMapPtr, const std::string & filename, int hierarchyMatchFlags);

    bool is_stored(const AnimControl * animPtr);
};

#endif /* CACTOR_H_ */

