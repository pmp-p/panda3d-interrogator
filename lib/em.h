#ifndef EM_H

static int em_steps=0;
static int g_argc=0;
#ifdef __cplusplus
    static void *g_argv= nullptr;
#else
    static void *g_argv= NULL;
#endif

#ifdef EMSCRIPTEN
    extern void emscripten_force_exit(int status);
#else
    static int emscripten_loop_run = 1;
    int check_timer(){ return 1;}
    void emscripten_cancel_main_loop(){
        emscripten_loop_run = 0;
    };

    typedef void (*funcptr)();

    void  main_loop_or_step(void);

    void emscripten_set_main_loop(funcptr emfunc, int a, int b){
        while(emscripten_loop_run){
            emfunc();
        }
    }
    void emscripten_force_exit(int status){ emscripten_cancel_main_loop(); }
#endif



#define EM_H
#endif
