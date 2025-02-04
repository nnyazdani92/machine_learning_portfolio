#!/bin/bash

# Wait for required file if specified
if [ -n "$WAIT_FOR_FILE" ]; then
    echo "Waiting for file: $WAIT_FOR_FILE"
    while [ ! -f "$WAIT_FOR_FILE" ]; do
        sleep 10
        echo "Still waiting..."
    done
fi

# Execute the command
exec "$@"