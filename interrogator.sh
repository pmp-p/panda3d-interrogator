reset
CONFIG=${CONFIG:-config.env}
. $CONFIG
rm lib/interrogate_*
if black -S -l 132 interrogator/__main__.py
then

    rm build/*.h build/*.in build/*.cpp build/*.so build/interrogate_* build/*.json

#    echo '{}' > build/tmp.json

    PYTHONPATH=.:${ROOT} $PYTHON -m interrogator --built ${ROOT} "$@"
    echo "===================================================================="
# cpython can pretty print json, not sure about upy
#    if which json_pp
#    then
#        json_pp < build/interrogate_wrapper.json > build/tmp.json
#    else
#        mv build/tmp.json build/interrogate_wrapper.json
#    fi
fi


