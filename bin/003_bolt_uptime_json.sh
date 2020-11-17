#!/usr/bin/env bash
bolt command --format json run 'uptime' \
  --nodes $main
