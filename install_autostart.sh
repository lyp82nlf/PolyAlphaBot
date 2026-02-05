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

# Rebuild ProgramArguments to avoid stale or malformed entries
/usr/libexec/PlistBuddy -c "Delete :ProgramArguments" "${TARGET_PLIST}" >/dev/null 2>&1 || true
/usr/libexec/PlistBuddy -c "Add :ProgramArguments array" "${TARGET_PLIST}"
/usr/libexec/PlistBuddy -c "Add :ProgramArguments:0 string ${PYTHON_BIN}" "${TARGET_PLIST}"
/usr/libexec/PlistBuddy -c "Add :ProgramArguments:1 string -u" "${TARGET_PLIST}"
/usr/libexec/PlistBuddy -c "Add :ProgramArguments:2 string -m" "${TARGET_PLIST}"
/usr/libexec/PlistBuddy -c "Add :ProgramArguments:3 string polyalphabot.main" "${TARGET_PLIST}"
/usr/libexec/PlistBuddy -c "Add :ProgramArguments:4 string --config" "${TARGET_PLIST}"
/usr/libexec/PlistBuddy -c "Add :ProgramArguments:5 string ${SCRIPT_DIR}/config.json" "${TARGET_PLIST}"
/usr/libexec/PlistBuddy -c "Add :ProgramArguments:6 string --directory" "${TARGET_PLIST}"
/usr/libexec/PlistBuddy -c "Add :ProgramArguments:7 string ${SCRIPT_DIR}" "${TARGET_PLIST}"

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
