#!/bin/sh
# Double-click this in Finder, or run it from a terminal.
#
# Serving the folder is what makes the -yaml.html pages behave exactly as they do once
# deployed: they read course-content.yml live and find the conventional PDFs with HEAD
# requests, so an edit or a newly dropped file shows up on the next refresh with no build.
#
# Opening a page by double-clicking it instead gives it an opaque origin, where browsers
# refuse every local read -- fetch, XHR and HEAD alike. That route can only fall back to
# what scripts/build-course last wrote into course-content.js, which is why it needs a build.
set -e
ROOT=$(cd "$(dirname "$0")/.." && pwd)
PORT=${1:-8765}
URL="http://127.0.0.1:$PORT/part-a-yaml.html"

cd "$ROOT"
printf 'Serving %s\n  %s\n\nPress Ctrl-C to stop.\n\n' "$ROOT" "$URL"
(sleep 1; open "$URL" >/dev/null 2>&1 || true) &
exec python3 -m http.server "$PORT" --bind 127.0.0.1
