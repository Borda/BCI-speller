#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

celery -A bci_challenge.taskapp worker -l INFO
