#!/usr/bin/env bash
set -euo pipefail

LABEL="com.polyalphabot"
PLIST_TEMPLATE="com.polyalphabot.plist"
LAUNCH_AGENTS_DIR="${HOME}/Library/LaunchAgents"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET_PLIST="${LAUNCH_AGENTS_DIR}/${LABEL}.plist"

mkdir -p "${LAUNCH_AGENTS_DIR}"
mkdir -p "${SCRIPT_DIR}/logs"

PYTHON_BIN="/usr/bin/python3"
if [[ -x "${SCRIPT_DIR}/.venv/bin/python3" ]]; then
  PYTHON_BIN="${SCRIPT_DIR}/.venv/bin/python3"
elif [[ -x "${SCRIPT_DIR}/.venv/bin/python" ]]; then
  PYTHON_BIN="${SCRIPT_DIR}/.venv/bin/python"
elif [[ -x "${SCRIPT_DIR}/venv/bin/python3" ]]; then
  PYTHON_BIN="${SCRIPT_DIR}/venv/bin/python3"
elif [[ -x "${SCRIPT_DIR}/venv/bin/python" ]]; then
  PYTHON_BIN="${SCRIPT_DIR}/venv/bin/python"
fi

if [[ ! -f "${SCRIPT_DIR}/${PLIST_TEMPLATE}" ]]; then
  echo "Missing ${PLIST_TEMPLATE} in ${SCRIPT_DIR}"
  exit 1
fi

if launchctl list | grep -q "${LABEL}"; then
  launchctl unload "${TARGET_PLIST}" >/dev/null 2>&1 || true
fi

cp "${SCRIPT_DIR}/${PLIST_TEMPLATE}" "${TARGET_PLIST}"

# Replace python interpreter
sed -i '' "s|<string>/usr/bin/python3</string>|<string>${PYTHON_BIN}</string>|" "${TARGET_PLIST}"

# Replace all template paths
sed -i '' "s|/REPLACE_WITH_PROJECT_PATH|${SCRIPT_DIR}|g" "${TARGET_PLIST}"

launchctl load "${TARGET_PLIST}"

echo "✅ Installed LaunchAgent: ${LABEL}"
echo "Plist: ${TARGET_PLIST}"
echo "Logs:"
echo "  ${SCRIPT_DIR}/logs/polyalphabot.out.log"
echo "  ${SCRIPT_DIR}/logs/polyalphabot.err.log"
echo ""
echo "Manage:"
echo "  launchctl list | grep ${LABEL}"
echo "  launchctl unload ${TARGET_PLIST}"
echo "  launchctl load ${TARGET_PLIST}"
