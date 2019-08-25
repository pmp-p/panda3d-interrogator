// #include <dlfcn.h>
#include <stdio.h>

#define MAX_em_steps 160

#include "em.h"


#define PT char
#define WindowFramework char
#define PandaFramework char
#define Engine char
#define NodePath char
#define Filename char


static Engine * E;
static NodePath * np;
static Filename * fn;

extern Engine * Engine_C_Engine_p_v();
extern NodePath * NP_C_NP_p_v();

extern void Engine_C_build_v_p(Engine *param0);
extern void Engine_C_step_v_p(Engine *param0);
extern PandaFramework * Engine_C_get_framework_p_p(Engine const *param0);

extern void NP_C_reparent_to_v_p(NodePath *param0, NodePath const *param1);
extern NodePath * WindowFramework_C_get_render_p_p(WindowFramework *param0);

extern PT * Engine_C_get_wframe_p_p(Engine const *param0);

extern Filename * Filename_C_Filename_2_p_p(char const *param0);
extern Filename * Filename_C_Filename_3_p_p(char const *param0);

extern char const * Filename_C_c_str_p_p(Filename const *param0);


// not original helpers
extern NodePath * Engine_C_load_model_p_p(Engine *param0, char const *param1);
extern void Engine_C_attach_v_p(Engine *param0, NodePath *param1);



void
main_loop_or_step(){
	if (!em_steps++) {
		puts("Step 1 : You are likely to be eaten by a grue.");


        const char *filename = "boris.bam" ;
/*
        fn = Filename_C_Filename_3_p_p(filename);
        puts("-----------------------------");
        fprintf(stdout,"FILENAME[%s]\n", Filename_C_c_str_p_p(fn) );
        puts("-----------------------------");
*/

        E = Engine_C_Engine_p_v();
        Engine_C_build_v_p(E);

        PandaFramework * pf = Engine_C_get_framework_p_p(E);
        WindowFramework * wf = Engine_C_get_wframe_p_p(E) ;



		// np = NP_C_NP_p_v(); should have been ->get_models() !

        NodePath * mdl = Engine_C_load_model_p_p(E, filename); // WindowFramework_C_load_model_p_pp(pf, np, fn );

        Engine_C_attach_v_p(E, mdl);

        //NP_C_reparent_to_v_p(mdl, wf );

/*
		environ.reparent_to(ewin->get_render());
		environ.set_scale(3,3,3);
		environ.set_pos(0, 42, 0);
*/


    }

    if (em_steps>MAX_em_steps)
        emscripten_loop_run=0;
    else
        Engine_C_step_v_p(E);

}


int main(int argc, char *argv[]) {


	g_argc = argc;
	g_argv = (void*)argv;

    emscripten_set_main_loop(main_loop_or_step, 0, 1);     // <= this will exit to js now.
    puts("exit");
    return 0; // success
}


