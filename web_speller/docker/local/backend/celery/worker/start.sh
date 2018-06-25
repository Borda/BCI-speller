#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

celery -A web_speller.taskapp worker -l INFO
