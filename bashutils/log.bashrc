#!/bin/bash
LOGGER_NAME="default"
LOGGER_FILE="default.log"

function set_logger_name {
    LOGGER_NAME="$1"
}
function set_log_file {
    LOGGER_FILE="$1"
}
function backup_log_file {
    if [[ -f "$LOGGER_FILE" ]]; then
        mv "$LOGGER_FILE" "prev_$LOGGER_FILE"
    fi
}

function kd_timestamp {
    # yoinked & tweaked from https://unix.stackexchange.com/a/85987
    echo "$(date '+%d/%m/%Y @ %H:%M:%S')"
}

function log {
    msg="[$LOGGER_NAME] [$(kd_timestamp)] $1"
    echo "$msg"
    echo "$msg" >> $LOGGER_FILE
}

function log_output {
    log "[!!!] Running '$(echo "$@")'"
    ORIG_NAME="$LOGGER_NAME"
    set_logger_name "$ORIG_NAME/$1"
    while read -r line; do
        log "$line"
    done <<< "$($@)"
    exitcode=$?
    set_logger_name "$ORIG_NAME"
    return $exitcode
}