#!/bin/sh
CONF=$(dirname $(realpath "$0"))
SCR=$(realpath "$1")
CONFIG=${CONFIG:-${CONF}/config.env}
. $CONFIG

echo "Panda: $ROOT"
echo "Target: $SCR"

PRC_PATH=${CONF} PYTHONPATH=${ROOT} "$@"

