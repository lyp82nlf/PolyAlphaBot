#!/usr/bin/env bash
set -euo pipefail

LABEL="com.polyalphabot"
PLIST_TEMPLATE="com.polyalphabot.plist"
LAUNCH_AGENTS_DIR="${HOME}/Library/LaunchAgents"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET_PLIST="${LAUNCH_AGENTS_DIR}/${LABEL}.plist"

mkdir -p "${LAUNCH_AGENTS_DIR}"
mkdir -p "${SCRIPT_DIR}/logs"

if [[ ! -f "${SCRIPT_DIR}/${PLIST_TEMPLATE}" ]]; then
  echo "Missing ${PLIST_TEMPLATE} in ${SCRIPT_DIR}"
  exit 1
fi

if launchctl list | grep -q "${LABEL}"; then
  launchctl unload "${TARGET_PLIST}" >/dev/null 2>&1 || true
fi

cp "${SCRIPT_DIR}/${PLIST_TEMPLATE}" "${TARGET_PLIST}"

# Replace WorkingDirectory
sed -i '' "/<key>WorkingDirectory<\/key>/,/<string>/ s|<string>.*</string>|<string>${SCRIPT_DIR}</string>|" "${TARGET_PLIST}"

# Replace --directory argument
sed -i '' "/<string>--directory<\/string>/,/<string>/ {
  /<string>--directory<\/string>/n
  s|<string>.*</string>|<string>${SCRIPT_DIR}</string>|
}" "${TARGET_PLIST}"

# Replace --config argument
sed -i '' "/<string>--config<\/string>/,/<string>/ {
  /<string>--config<\/string>/n
  s|<string>.*</string>|<string>${SCRIPT_DIR}/config.json</string>|
}" "${TARGET_PLIST}"

# Replace log paths
sed -i '' "/<key>StandardOutPath<\/key>/,/<string>/ s|<string>.*</string>|<string>${SCRIPT_DIR}/logs/polyalphabot.out.log</string>|" "${TARGET_PLIST}"
sed -i '' "/<key>StandardErrorPath<\/key>/,/<string>/ s|<string>.*</string>|<string>${SCRIPT_DIR}/logs/polyalphabot.err.log</string>|" "${TARGET_PLIST}"

# Replace PYTHONPATH
sed -i '' "/<key>PYTHONPATH<\/key>/,/<string>/ s|<string>.*</string>|<string>${SCRIPT_DIR}/src</string>|" "${TARGET_PLIST}"

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
