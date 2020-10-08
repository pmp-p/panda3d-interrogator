// #include <dlfcn.h>
#include <stdio.h>

#define MAX_em_steps 160

#include "em.h"

#include "upanda3d.h"



static Engine * E;
static NodePath * np;
static Filename * fn;





extern char const * Engine_C_get_version_string_s_v();
extern int Engine_C_HelloEngine_i_p(Engine *self);




void
main_loop_or_step(){
	if (!em_steps++) {
		puts("Step 1 : You are likely to be eaten by a grue.");


        const char *filename = "boris.bam" ;

    puts("-----------------------------");
        fprintf(stdout,"VERSION = %s\n", Engine_C_get_version_string_s_v());
    puts("-----------------------------");
        E = Engine_C_ctor_p_v();

        fprintf(stdout,"ANSWER = %d\n",    Engine_C_HelloEngine_i_p(E));
    puts("-----------------------------");

        Engine_C_build_v_p(E);

        PandaFramework * pf = Engine_C_get_framework_p_p(E);
        WindowFramework * wf = Engine_C_get_wframe_p_p(E) ;

        NodePath * mdl = Engine_C_load_model_p_ps(E, filename);
        Engine_C_attach_v_pp(E, mdl);

        //NodePath_C_reparent_to_v_pp(mdl, WindowFramework_C_get_render_p_p(wf) );

/*
		environ.reparent_to(ewin->get_render());
		environ.set_scale(3,3,3);
    	environ.set_pos(0, 42, 0);
    // OK
        LVecBase3f * s3f = LVecBase3f_C_ctor_p_fff(2,2,2);
        Engine_C_op_scale_v_ppp(E, mdl, s3f );

        LVecBase3f * v3f = LVecBase3f_C_ctor_p_fff(0,42,0);
        Engine_C_op_pos_v_ppp(E, mdl, v3f );
*/

        NodePath_C_set_scale_v_pfff( mdl, 2,2,2);
        NodePath_C_set_pos_v_pfff( mdl, 0,42,0);


















    }

    if (em_steps>MAX_em_steps) {
        emscripten_loop_run=0;
        Engine_C_dtor_v_p(E);
        return;
    }

    if (!Engine_C_is_alive_i_v())  {
        emscripten_loop_run=0;
        Engine_C_dtor_v_p(E);
        return;
    }

    Engine_C_step_v_p(E);

}


int main(int argc, char *argv[]) {


	g_argc = argc;
	g_argv = (void*)argv;

    emscripten_set_main_loop(main_loop_or_step, 0, 1);     // <= this will exit to js now.
    puts("exit");
    return 0; // success
}


