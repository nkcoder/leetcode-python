#!/usr/bin/env bash

conda activate base
PYTHONPATH=./src pytest -vv
