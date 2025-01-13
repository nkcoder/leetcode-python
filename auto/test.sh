#!/usr/bin/env bash

ENV_NAME="leetcode_python"
REQUIREMENTS_FILE="requirements.txt"

env_exists() {
  conda env list | grep -q "${ENV_NAME}"
}

# Create env if it doesn't exist and install requirements
if ! env_exists; then
  echo "Creating conda env ${ENV_NAME}"
  conda create -n "${ENV_NAME}" python=3.13 -y
  conda run -n "${ENV_NAME}" pip install -r "${REQUIREMENTS_FILE}"
fi

# Run tests with PYTHONPATH set
conda run -n "${ENV_NAME}" bash -c "PYTHONPATH=./src pytest -vv"
