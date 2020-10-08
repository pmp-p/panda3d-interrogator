#include <iostream>
#include <vector>

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

#include "texture.h"
#include "texturePeeker.h"

#include "showBase.h"

#include "loader.h"


#include "collisionBox.h"
#include "collisionCapsule.h"
#include "collisionEntry.h"
#include "collisionFloorMesh.h"
#include "collisionGeom.h"
#include "collisionHandler.h"
#include "collisionHandlerEvent.h"
#include "collisionHandlerFloor.h"
#include "collisionHandlerFluidPusher.h"
#include "collisionHandlerGravity.h"
#include "collisionHandlerHighestEvent.h"
#include "collisionHandlerPhysical.h"
#include "collisionHandlerPusher.h"
#include "collisionHandlerQueue.h"
#include "collisionInvSphere.h"
#include "collisionLevelState.h"
#include "collisionLevelStateBase.h"
#include "collisionLine.h"
#include "collisionNode.h"
#include "collisionParabola.h"
#include "collisionPlane.h"
#include "collisionPolygon.h"
#include "collisionRay.h"
#include "collisionRecorder.h"
#include "collisionSegment.h"
#include "collisionSolid.h"
#include "collisionSphere.h"
#include "collisionTraverser.h"
#include "collisionTube.h"
#include "collisionVisualizer.h"



#include "lib.h"

//-------------------------- Actor ----------------------------------------------------------------

CActor::CActor() {
    ;
}

CActor::~CActor() {
    ;
}

void
CActor::add(str path,str name) {
    this->anim_map[dict_slot( path, name )] = 0;
}


// This function loads an actor model and its animations, letting the user specify the name of each animation.
//
// Return value:
// The actor, parented to the framework's models node (to render the actor, reparent it to the render node)
//
// Parameters:
//    windowFrameworkPtr : the WindowFramework for this actor
//    actorFilename      : the actor's egg file
//    animMap            : a map of the desired name (first) of each animation and its associated file (second).
//                         Set this parameter to NULL if there are no animations to bind to the actor.
//    hierarchyMatchFlags: idem as the same parameter from auto_bind().
void
CActor::load_actor(WindowFramework * windowFrameworkPtr,
                   const std::string & actorFilename, const AnimMap * animMapPtr, int hierarchyMatchFlags) {
    // preconditions
    if (windowFrameworkPtr == NULL) {
        nout << "ERROR: windowFrameworkPtr cannot be NULL." << std::endl;
        return;
    }
    if (!is_empty()) {
        nout << "ERROR: cannot call load_actor() because this instance is not empty anymore." << std::endl;
        return;
    }
    // first load the actor model
    NodePath modelsNp = windowFrameworkPtr->get_panda_framework()->get_models();
    NodePath::operator=(windowFrameworkPtr->load_model(modelsNp, actorFilename));

    // If there are no animations to bind to the actor, we are done here.
    if (animMapPtr == NULL) {
        return;
    }
    // load anims from the actor model first
    load_anims(animMapPtr, actorFilename, hierarchyMatchFlags);

    NodePathVec animNpVec;
    animNpVec.reserve(animMapPtr->size());

    // then for each animations specified by the user
    for (AnimMap::const_iterator animMapItr = animMapPtr->begin(); animMapItr != animMapPtr->end(); ++animMapItr) {
        const std::string & filename = (*animMapItr).first;
        if (filename != actorFilename) {
            // load the animation as a child of the actor
            NodePath animNp = windowFrameworkPtr->load_model(*this, filename);

            // load anims from that file
            load_anims(animMapPtr, filename, hierarchyMatchFlags);

            // detach the node so that it will not appear in a new call to auto_bind()
            animNp.detach_node();
            // keep it on the side
            animNpVec.push_back(animNp);
        }
    }

    // re-attach the animation nodes to the actor
    for (NodePathVec::iterator npItr = animNpVec.begin(); npItr < animNpVec.end(); ++npItr) {
        (*npItr).reparent_to(*this);
    }
}

void
CActor::load_anims(const AnimMap * animMapPtr, const std::string & filename, int hierarchyMatchFlags) {
    // precondition
    if (animMapPtr == NULL) {
        nout << "ERROR: parameter animMapPtr cannot be NULL." << std::endl;
        return;
    }
    // use auto_bind() to gather the anims
    AnimControlCollection tempCollection;
    auto_bind(this->node(), tempCollection, hierarchyMatchFlags);

    // get the anim names for the current file
    AnimMap::const_iterator animMapItr = animMapPtr->find(filename);
    if (animMapItr != animMapPtr->end()) {
        // first, test the anim names
        for (NameVec::const_iterator nameItr = (*animMapItr).second.begin(); nameItr != (*animMapItr).second.end(); ++nameItr) {
            // make sure this name is not currently stored by the actor
            if (find_anim(*nameItr) == NULL) {
                // check if auto_bind() found an animation with the right name
                PT(AnimControl) animPtr = tempCollection.find_anim(*nameItr);
                if (animPtr != NULL) {
                    store_anim(animPtr, *nameItr);
                    tempCollection.unbind_anim(*nameItr);
                    nout << "Stored animation `" << *nameItr << "' from file `" << (*animMapItr).first << "'" << std::endl;
                }
            }
        }

        // deal the remaining anims
        int animIdx = 0;
        for (NameVec::const_iterator nameItr = (*animMapItr).second.begin(); nameItr != (*animMapItr).second.end(); ++nameItr) {
            // make sure this name is not currently stored by the actor
            if (find_anim(*nameItr) == NULL) {
                // make sure there is at least one anim left to store
                PT(AnimControl) animPtr = tempCollection.get_anim(animIdx);
                if (animPtr != NULL) {
                    store_anim(animPtr, *nameItr);
                    ++animIdx;
                    nout << "Stored animation `" << *nameItr << "' from file `" << (*animMapItr).first << "'" << std::endl;
                }
            }
        }
    }
}

bool
CActor::is_stored(const AnimControl * animPtr) {
    for (int i = 0; i < get_num_anims(); ++i) {
        PT(AnimControl) storedAnimPtr = get_anim(i);

        if ((animPtr->get_anim() == storedAnimPtr->get_anim())
            && (animPtr->get_part() == storedAnimPtr->get_part())
            ) {
            return true;
        }
    }
    return false;
}

// This function gives access to a joint that can be controlled via its NodePath handle.
// Think of it as a write to that joint interface.
//
// Return value:
// The joint's NodePath, parented to the actor.
//
// Parameter:
//    jointName: the joint's name as found in the model file.
NodePath
CActor::control_joint(const std::string & jointName) {
    bool foundJoint = false;
    NodePath jointNp = attach_new_node(jointName);
    NodePath characterNP = find("**/+Character");
    PT(Character) characterPtr = DCAST(Character, characterNP.node());
    if (characterPtr != NULL) {
        PT(CharacterJoint) characterJointPtr = characterPtr->find_joint(jointName);
        if (characterJointPtr != NULL) {
            for (int i = 0; !foundJoint && i < characterPtr->get_num_bundles(); ++i) {
                if (characterPtr->get_bundle(i)->control_joint(jointName, jointNp.node())) {
                    foundJoint = true;
                    jointNp.set_mat(characterJointPtr->get_default_value());
                }
            }
        }
    }
    if (!foundJoint) {
        nout << "ERROR: cannot control joint `" << jointName << "'." << std::endl;
        jointNp.remove_node();
    }
    return jointNp;
}

// This function exposes a joint via its NodePath handle.
// Think of it as a read from that joint interface.
//
// Return value:
// The joint's NodePath, parented to the actor.
//
// Parameter:
//    jointName: the joint's name as found in the model file.
NodePath
CActor::expose_joint(const std::string & jointName) {
    bool foundJoint = false;
    NodePath jointNp = attach_new_node(jointName);
    NodePath characterNP = find("**/+Character");
    PT(Character) characterPtr = DCAST(Character, characterNP.node());
    if (characterPtr != NULL) {
        PT(CharacterJoint) characterJointPtr = characterPtr->find_joint(jointName);
        if (characterJointPtr != NULL) {
            foundJoint = true;
            characterJointPtr->add_net_transform(jointNp.node());
        }
    }
    if (!foundJoint) {
        nout << "ERROR: no joint named `" << jointName << "'." << std::endl;
        jointNp.remove_node();
    }
    return jointNp;
}


//-----------------------------------------------------------------------------------------




























































#define MAX_em_steps 160

#include "em.h"

using namespace std;


//-----------------------------------------------------------------------------------------





static FRAMEWORK panda_framework;


/*
GeomT::~GeomT(){
    cout << "GeomT->Destructor" <<endl;
}
*/
PT(GeomTriangles)
    Engine::new_GeomTriangles() {
    return new GeomTriangles(GeomEnums::UH_static);
}

GeomVertexWriter *
Engine::new_GeomVertexWriter(GeomVertexData * data, const char *gvw_name) {
    return new GeomVertexWriter(data, CPT_InternalName(gvw_name));      //InternalName::get_vertex()
}

void
Engine::add_primitive(Geom * geom, GeomTriangles * pri) {
    cout << "->add_primitive" << std::endl;
    cout << geom << endl;
    geom->add_primitive(pri);
}

void
Engine::close_primitive(GeomTriangles * pri) {
    cout << "->close_primitive(begin)" << std::endl;
    cout << pri << endl;
    pri->close_primitive();
    cout << "->close_primitive(end)" << std::endl;
}

void
Engine::prc(const Filename & filename) {
//    return
    load_prc_file(filename);
}

void
Engine::prc(str name, str data) {
//    return
    load_prc_file_data(name, data);
}


Engine::Engine() {
    cout << "->Constructor\n";
    this->framework = &panda_framework;
}

int
Engine::inc_ref(ReferenceCount * rc) {
    rc->ref();
    return rc->get_ref_count();
}

int
Engine::dec_ref(ReferenceCount * rc) {
    rc->unref();
    return rc->get_ref_count();
}


void
Engine::build() {
    cout << "->build()\n";
    // setup Panda3d
    this->framework->open_framework(g_argc, (char **&) g_argv);
    this->framework->set_window_title("My Panda3D Window");
    wframe = this->framework->open_window();

    wframe->ref();

    if (wframe == NULL) {
        nout << "ERROR: could not open the WindowFramework." << std::endl;
        emscripten_force_exit(0);
        return;                 // error
    }
    // Escape quits
    wframe->enable_keyboard();
    wframe->get_panda_framework()->define_key("escape", "escapeQuits", call_exit, NULL);
}


void
Engine::step() {
    Thread *current_thread = Thread::get_current_thread();

    if (!this->framework->do_frame(current_thread)) {
        // quit Panda3d
        cout << "->step : render error" << std::endl;
        this->stop();
    }
}

int
Engine::HelloEngine() {
    cout << "Hello Engine !" << std::endl;
    return 42;
}

NodePath *
Engine::load_model(const char *filename) {
    return new NodePath(this->wframe->load_model(this->framework->get_models(), Filename(filename)));
}

std::string Engine::get_version_string() {
    static
        std::string
        version = "0.0.1";
    return version;
}

int
Engine::is_alive() {
    return alive;
}


void
Engine::attach(NodePath * mdl) {
    mdl->reparent_to(this->wframe->get_render());
}


int
Engine::casetest(int i, std::string s, bool b) {
    return 0;
}

void
Engine::stop() {
    cout << "->stop\n";
    em_steps = MAX_em_steps;
    alive = 0;
}

void
Engine::call_exit(const Event * event, void *data) {
    stop();
    cout << "->call_exit (WM)" << std::endl;
}

void
Engine::dtor() {
    this->framework->close_framework();
    delete this;
    alive = 0;
    emscripten_force_exit(0);
}

Engine::~Engine() {
    cout << "->Destructor\n";
    for (int i = 0; i < 64; ++i) {
        //delete m_pieces[i];
    }
}


//-----------------------------------------------------------------------------



void
add_quad(GeomTriangles * triangles, int v0, int v1, int v2, int v3) {
    triangles->add_vertices(v0, v1, v2);
    triangles->add_vertices(v0, v2, v3);
    triangles->close_primitive();
}

NodePath *
Engine::new_Cube(float size, str geom_name, str gvd_name) {

    GeomTriangles *triangles;
//PT(GeomTriangles) triangles;
    GeomVertexFormat const *format;
    GeomVertexData *data;
    Geom *geom;
    GeomNode *node;
    GeomVertexWriter vertices;

    format = GeomVertexFormat::get_v3();

    data = new GeomVertexData(gvd_name, format, GeomEnums::UH_static);


    vertices = GeomVertexWriter(data, CPT_InternalName("vertex"));

    size /= 2.0;
    vertices.add_data3f(-size, -size, -size);
    vertices.add_data3f(+size, -size, -size);
    vertices.add_data3f(-size, +size, -size);
    vertices.add_data3f(+size, +size, -size);
    vertices.add_data3f(-size, -size, +size);
    vertices.add_data3f(+size, -size, +size);
    vertices.add_data3f(-size, +size, +size);
    vertices.add_data3f(+size, +size, +size);



    triangles = new GeomTriangles(GeomEnums::UH_static);

// ? lifetime of triangles ?
    Engine::inc_ref(triangles);


    add_quad(triangles, 4, 5, 7, 6);    // Z+
    add_quad(triangles, 0, 2, 3, 1);    // Z-
    add_quad(triangles, 3, 7, 5, 1);    // X+
    add_quad(triangles, 4, 6, 2, 0);    // X-
    add_quad(triangles, 2, 6, 7, 3);    // Y+
    add_quad(triangles, 0, 1, 5, 4);    // Y+


    geom = new Geom(data);
    geom->add_primitive(triangles);

    node = new GeomNode(geom_name);
    node->add_geom(geom);

    return new NodePath(node);

}


#define efram engine->framework
#define ewin engine->wframe
void
main_loop_or_step() {

    static Engine *engine = new Engine();


    if (!em_steps++) {
        cout << "You are likely to be eaten by a grue. step " << em_steps << "/2" << std::endl;
    }


    if (em_steps == 1) {


        // We now have everything we need. Make an instance of the class and start
        // 3D rendering

        engine->build();

/*
        NodePath mdl = ewin->load_model(efram->get_models(), "model.bam");
*/
        NodePath *mdl = engine->load_model("model.bam");
        engine->attach(mdl);
        //mdl->reparent_to(ewin->get_render());
        mdl->set_scale(3, 3, 3);
        mdl->set_pos(0, 42, 0);

        engine->attach(engine->new_Cube(1.0, "cm", "data"));

        cout << "sizeof(LVecBase3f) = " << sizeof(LVecBase3f) << endl;
        return;
    }

    if (em_steps > MAX_em_steps) {
        emscripten_loop_run = 0;
        engine->dtor();
        return;
    }

    if (!engine->is_alive()) {
        emscripten_loop_run = 0;
        engine->dtor();
        return;
    }

    if (em_steps > 1) {
        engine->step();
    }
}


int
main(int argc, char *argv[]) {

    cout << "dlhandle=" << dlopen("/lib/libpanda3d.js", RTLD_NOW | RTLD_GLOBAL) << endl;
    g_argc = argc;
    g_argv = (void *) argv;

    cout << "Geom::UH_static = " << int (Geom::UH_static) << endl;

    emscripten_set_main_loop(main_loop_or_step, 0, 1);  // <= this will exit to js now.
    cout << "exit" << std::endl;
    return 0;                   // success
}
