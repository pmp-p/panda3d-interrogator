// #include <dlfcn.h>
#include <stdio.h>

#define MAX_em_steps 160

#include "em.h"

#include "lib/interrogate_wrapper.h"



static Engine * E;
static NodePath * np;
static Filename * fn;


/*
void
NodePath_C_set_pos_v_pp(NodePath *param0, LVecBase3f const *param1) {

  (*param0).set_pos(  static_cast<LVecBase3f const&>(*param1));
}

void
NodePath_C_set_scale_v_pp(NodePath *param0, LVecBase3f const *param1) {
  (*param0).set_scale( static_cast<LVecBase3f const&>(*param1));
}
*/

void
main_loop_or_step(){
	if (!em_steps++) {
		puts("Step 1 : You are likely to be eaten by a grue.");


        const char *filename = "boris.bam" ;
/*
        fn = Filename_C_Filename_3_p_p(filename);
        puts("-----------------------------");
        fprintf(stdout,"VERSION[%s] FILENAME[%s]\n", Engine_C_get_version_string_s_v(), Filename_C_c_str_p_p(fn) );
        puts("-----------------------------");
*/

    puts("-----------------------------");
        fprintf(stdout,"VERSION = %s\n", Engine_C_get_version_string_s_v());
    puts("-----------------------------");
        E = Engine_C_ctor_p_v();
        Engine_C_build_v_p(E);

        PandaFramework * pf = Engine_C_get_framework_p_p(E);
        WindowFramework * wf = Engine_C_get_wframe_p_p(E) ;



		// np = NP_C_NP_p_v(); should have been ->get_models() !

        NodePath * mdl = Engine_C_load_model_p_ps(E, filename);
        Engine_C_attach_v_pp(E, mdl);


        //NP_C_reparent_to_v_p(mdl, rd );

/*
		environ.reparent_to(ewin->get_render());
		environ.set_scale(3,3,3);
		environ.set_pos(0, 42, 0);
*/
        //NodePath_C_set_scale_v_pfff( mdl, 2,2,2);
        //NodePath_C_set_pos_v_pfff( mdl, 0,42,0);


/* OK
        LVecBase3f * s3f = LVecBase3f_C_ctor_p_fff(2,2,2);
        Engine_C_op_scale_v_ppp(E, mdl, s3f );

        LVecBase3f * v3f = LVecBase3f_C_ctor_p_fff(0,42,0);
        Engine_C_op_pos_v_ppp(E, mdl, v3f );
*/




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


