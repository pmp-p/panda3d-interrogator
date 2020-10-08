reset
CONFIG=${CONFIG:-config.env}
. $CONFIG
rm lib/interrogate_*
if black -S -l 132 interrogator/__main__.py
then

    rm build/*.h build/*.in build/*.cpp build/*.so build/interrogate_* build/*.json

    PYTHONPATH=.:${ROOT} $PYTHON -m interrogator --built ${ROOT} "$@"
    echo "===================================================================="
fi


