#!/usr/bin/env bash

for test in $(ls tests/array_hash/test_*.py); do
    echo "Running $test"
    python $test
done