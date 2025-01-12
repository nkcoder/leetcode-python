#!/usr/bin/env bash

conda init
conda activate base
PYTHONPATH=./src pytest -vv
