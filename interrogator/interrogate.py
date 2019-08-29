#!/usr/bin/env python3.7

"""

Runs the interrogate and interrogate_module commands from Panda3D.

"""

import sys,os
from os import listdir, chdir
from os.path import join, isfile, isdir
import re

from panda3d.core import PandaSystem
from .common import debug_out, get_panda_bin_path, get_panda_include_path
from .common import get_compiler_name, is_64_bit, try_execute, join_abs, get_script_dir



def check_ignore(source):
    """ This function checks if a file is on the ignore list """
    for f in ["interrogate_module.cpp","interrogate_temp.cpp", "interrogate_wrapper.cpp", "interrogate_wrapper.h"]:
        if f.lower() in source.lower():
            return False
    return True


def find_sources(base_dir):
    """ Collects all header files recursively """
    sources = []
    files = listdir(base_dir)
    p = re.compile(r'.*\.(h|c)((pp|xx)?)$', flags=re.I)
    for f in files:
        fpath = join(base_dir, f)

        if isfile(fpath) and check_ignore(f) and  p.match(f) is not None:
            if f.endswith(".pb.h"):
                continue # Skip protobuf
            sources.append(f)
        elif isdir(fpath):
            sources += find_sources(fpath)
    return sources


def interrogate(*cmd,includes=[]):
    """ Runs interrogate over the source directory """

    MAJ = PandaSystem.get_major_version() == 1
    MIN = PandaSystem.get_minor_version()

    print(f"Panda3D {MAJ}.{MIN}")


    cmd = list(cmd)

    if VERBOSE_LVL == 1:
        cmd.append("-v")

    elif VERBOSE_LVL == 2:
        cmd.append("-vv")

    for include in includes:
        cmd.append("-S")
        cmd.append(include)

    # Add all subdirectories
    for pth in listdir(MODULE_PATH):
        if isdir(pth):
            cmd.append(f"-I{pth}")

    cmd.append( "--oc" )

    if "-c" in cmd:
        cmd.append( f"{BUILD_PATH}/interrogate_temp.cpp" )
    else:
        cmd.append( f"{BUILD_PATH}/interrogate_wrapper.cpp" )

    cmd.append("-srcdir")
    cmd.append(MODULE_PATH)


    if MAJ > 1 or MIN > 9:
        # Add nomangle option, but only for recent builds
        cmd += ["-nomangle"]

    cmd += ["-od", f"{BUILD_PATH}/interrogate.in"]
    cmd += ["-module", MODULE_NAME]
    cmd += ["-library", MODULE_NAME]

    if MAJ==1 and MIN < 10:
        # Old interrogate options cant handle volatile
        cmd += ["-Dvolatile="]

    # Defines required to parse the panda source
    defines = ["INTERROGATE", "CPPPARSER", "__STDC__=1", "__cplusplus=201103L"]

    if get_compiler_name() == "MSC":
        print("Using MSC")
        defines += ["__inline", "_X86_", "WIN32_VC", "WIN32", "_WIN32"]
        if is_64_bit():
            defines += ["WIN64_VC", "WIN64", "_WIN64"]
        # NOTE: this 1600 value is the version number for VC2010.
        defines += ["_MSC_VER=1600", '"__declspec(param)="', "__cdecl", "_near",
                    "_far", "__near", "__far", "__stdcall"]
    elif get_compiler_name() == "GCC":
        print("Using gcc")
        defines += ['__attribute__\(x\)=']
        defines += ['__x86_64__','_LP64']
        if 0:
            defines += ['__i386__']

    for define in defines:
        cmd += ["-D" + define]


    # Collect source files and convert them to a relative path
    all_sources = find_sources(MODULE_PATH)

    cmd += all_sources

    print( ' '.join(cmd))
    print()

    try_execute(*cmd)


def interrogate_module():
    """ Runs the interrogate module command """

    # Create module command
    cmd = [join_abs(get_panda_bin_path(), "interrogate_module")]
    cmd += ["-python-native"]

    if PandaSystem.get_major_version() > 1 or PandaSystem.get_minor_version() > 9:
        # Older panda3d versions don't have this
        cmd += ["-import", "panda3d.core"]

    cmd += ["-module", MODULE_NAME]
    cmd += ["-library", MODULE_NAME]
    cmd += ["-oc", "interrogate_module.cpp"]
    cmd += ["interrogate.in"]
    try_execute(*cmd)



