#!/bin/sh

rm -rf solutions/
mkdir solutions/
python3 solution.py inputs/kittens.in > solutions/kittens.txt
python3 solution.py inputs/me_at_the_zoo.in > solutions/me_at_the_zoo.txt
python3 solution.py inputs/trending_today.in > solutions/trending_today.txt
python3 solution.py inputs/videos_worth_spreading.in > solutions/videos_worth_spreading.txt

zip solutions/sol.zip parse.py solution.py
