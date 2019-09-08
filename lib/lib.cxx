#include <iostream>
#include <set>
#include <dlfcn.h>

#include "pandaFramework.h"
#include "pandaSystem.h"
#include "pandabase.h"

#include "nodePath.h"
#include "internalNameCollection.h"
#include "nodePathCollection.h"
#include "materialCollection.h"
#include "geomTriangles.h"
#include "geomVertexWriter.h"
#include "threadPriority.h"


#define MAX_em_steps 160

#include "em.h"

using namespace std;


//-----------------------------------------------------------------------------------------

#include "lib.h"




static FRAMEWORK panda_framework;


GeomT::~GeomT(){
    cout << "GeomT->Destructor" <<endl;
}

GeomVertexWriter *
Engine::new_GeomVertexWriter(GeomVertexData *data, const char *gvw_name) {
    return new GeomVertexWriter(data, CPT_InternalName(gvw_name) ); //InternalName::get_vertex()
}

void
Engine::add_primitive(Geom *geom, GeomTriangles *pri) {
    cout << "->add_primitive" << endl;
    cout << geom << endl;
    geom->add_primitive(pri);
}

void
Engine::close_primitive(GeomTriangles *pri) {
    cout << "->close_primitive(begin)" << endl;
    cout << pri << endl;
    pri->close_primitive();
    cout << "->close_primitive(end)" << endl;
}


Engine::Engine() {
    cout << "->Constructor\n";
    this->framework = &panda_framework;
};


void
Engine::build() {
    cout << "->build()\n";
	// setup Panda3d
	this->framework->open_framework(g_argc, (char **&)g_argv);

	WindowFramework *window = this->framework->open_window();

	PT(WindowFramework) window_framework = window;

	if(window_framework == NULL) {
		nout << "ERROR: could not open the WindowFramework." << endl;
        emscripten_force_exit(0);
		return ; // error
	}


    // Escape quits
    wframe=    window_framework;
    wframe->enable_keyboard();
    wframe->get_panda_framework()->define_key("escape", "escapeQuits", call_exit, NULL);
}


int
Engine::step() {
	Thread *current_thread = Thread::get_current_thread();

	if (!this->framework->do_frame(current_thread)) {
	    // quit Panda3d
        cout << "->step : render error" << endl;
        this->stop();
	}
    return 666;
}

int
Engine::HelloEngine() {
    cout << "Hello Engine !" << endl;
    return 42;
}

NodePath *
Engine::load_model(const char *filename) {
    return new NodePath( this->wframe->load_model( this->framework->get_models() , Filename(filename) ) );
}

std::string
Engine::get_version_string() {
    static std::string version = "0.0.1";
    return version;
}

int
Engine::is_alive() {
    return alive;
}


void
Engine::attach(NodePath *mdl) {
    mdl->reparent_to( this->wframe->get_render() );
}


int
Engine::casetest(int i,std::string s,bool b) {
    return 0;
}

void
Engine::stop() {
    cout << "->stop\n";
    em_steps = MAX_em_steps ;
    alive = 0;
}
void
Engine::call_exit(const Event* event, void* data) {
    stop();
    cout << "->call_exit (WM)" << endl;
}

void
Engine::dtor(){
    this->framework->close_framework();
    delete this;
    alive = 0;
	emscripten_force_exit(0);
}

Engine::~Engine() {
    cout << "->Destructor\n";
    for(int i = 0; i < 64; ++i)
    {
    //delete m_pieces[i];
    }
}


//-----------------------------------------------------------------------------



#define efram engine->framework
#define ewin engine->wframe
void
main_loop_or_step(){

    static Engine *engine = new Engine();


	if (!em_steps++) {
		cout << "You are likely to be eaten by a grue. step " << em_steps << "/2" << endl;
    }


	if (em_steps==1) {


		// We now have everything we need. Make an instance of the class and start
		// 3D rendering

        engine->build();

/*
		NodePath mdl = ewin->load_model(efram->get_models(), "boris.bam");
*/
        NodePath * mdl = engine->load_model("boris.bam");
        engine->attach(mdl);
		//mdl->reparent_to(ewin->get_render());
		mdl->set_scale(3,3,3);
		mdl->set_pos(0, 42, 0);

        cout << "sizeof(LVecBase3f) = " << sizeof(LVecBase3f) << endl;
		return;
	}

    if (em_steps>MAX_em_steps) {
        emscripten_loop_run=0;
        engine->dtor();
        return;
    }

    if (!engine->is_alive())  {
        emscripten_loop_run=0;
        engine->dtor();
        return;
    }

	if (em_steps>1) {
        engine->step();
	}
}


int main(int argc, char *argv[]) {

	cout << "dlhandle=" << dlopen("/lib/libpanda3d.js", RTLD_NOW | RTLD_GLOBAL) << endl;
	g_argc = argc;
	g_argv = (void*)argv;

    cout << "Geom::UH_static = " << int(Geom::UH_static) << endl;

    emscripten_set_main_loop(main_loop_or_step, 0, 1);     // <= this will exit to js now.
    cout << "exit" << endl;
    return 0; // success
}




