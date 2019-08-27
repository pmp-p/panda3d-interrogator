reset
rm lib/interrogate_*
if black -S -l 132 interrogator/__main__.py
then
    PYTHONPATH=. python3.7 -m interrogator lib 1
fi
