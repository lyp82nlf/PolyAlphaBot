#!/usr/bin/env bash
set -euo pipefail

LABEL="com.polyalphabot"
LAUNCH_AGENTS_DIR="${HOME}/Library/LaunchAgents"
TARGET_PLIST="${LAUNCH_AGENTS_DIR}/${LABEL}.plist"

if [[ -f "${TARGET_PLIST}" ]]; then
  launchctl unload "${TARGET_PLIST}" >/dev/null 2>&1 || true
  rm -f "${TARGET_PLIST}"
  echo "✅ Uninstalled LaunchAgent: ${LABEL}"
else
  echo "LaunchAgent not found: ${LABEL}"
fi
