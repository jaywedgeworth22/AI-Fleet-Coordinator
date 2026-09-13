#!/bin/bash
export BACKBLAZE_MASTER_KEY_ID=$(grep -m1 '^BACKBLAZE_MASTER_KEY_ID=' ~/.secrets/global-api-keys | cut -d= -f2- | tr -d '"')
export BACKBLAZE_MASTER_APPLICATION_KEY=$(grep -m1 '^BACKBLAZE_MASTER_APPLICATION_KEY=' ~/.secrets/global-api-keys | cut -d= -f2- | tr -d '"')
exec litestream replicate -config "$(dirname "$0")/litestream.yml"
