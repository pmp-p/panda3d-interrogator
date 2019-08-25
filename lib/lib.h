#ifndef MVIEW_H


#include "pandabase.h"
#include "notifyCategoryProxy.h"
#include "dconfig.h"
#include "dtoolbase.h"

//NotifyCategoryDecl(lib, EXPCL_LIB, EXPTP_LIB);


#include "pandaFramework.h"
#include "pandaSystem.h"



class EXPORT_CLASS NP : public NodePath::NodePath
{
    PUBLISHED:
        void reparent_to(const NodePath &other);
};


#define FRAMEWORK PandaFramework


class EXPORT_CLASS Engine
{

    PUBLISHED:

        Engine();
        ~Engine();

        int HelloEngine();

        int casetest(int i,std::string s,bool b);

        void build(); //WindowFramework* window_framework);

        void step();

        static void call_exit(const Event* event, void* data);


        PT(WindowFramework) wframe;

        FRAMEWORK * framework;
};



#define MVIEW_H
#endif
