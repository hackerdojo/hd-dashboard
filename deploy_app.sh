#!/usr/bin/env bash
set -e # will exit script if command returns != 0
gcloud app deploy --project hd-dashboard app.yaml >&2
exit