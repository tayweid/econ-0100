#!/bin/sh
# Optional. Every part page also opens by double-clicking it: course-content.yaml.js
# is a <script>, which a page opened from disk may load, and the conventional PDFs are
# found with the same kind of element load. Serve the folder instead when you want the
# exact deployed behaviour -- over HTTP the PDFs are discovered with HEAD requests, which
# see only what is actually published, not untracked files sitting in the working tree.
#
# Double-click this in Finder, or run it from a terminal.
set -e
ROOT=$(cd "$(dirname "$0")/.." && pwd)
PORT=${1:-8765}
URL="http://127.0.0.1:$PORT/part-a.html"

cd "$ROOT"
printf 'Serving %s\n  %s\n\nPress Ctrl-C to stop.\n\n' "$ROOT" "$URL"
(sleep 1; open "$URL" >/dev/null 2>&1 || true) &
exec python3 -m http.server "$PORT" --bind 127.0.0.1
