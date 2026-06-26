# [title:test]#!/usr/bin/env bash
# Replaces hardcoded passwords in DEFINE statements with a placeholder

files=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.sql$')
[ -z "$files" ] && exit 0

modified=0
for f in $files; do
  if grep -Eq 'DEFINE[[:space:]]+\w*Password\w*[[:space:]]*=' "$f"; then
    perl -pi -e 's/(DEFINE\s+\w*Password\w*\s*=\s*)(["\x27])[^"\x27]*\2/$1$2<DeletedPassword>$2/g' "$f"
    git add "$f"
    modified=1
    echo "Scrubbed password(s) in $f"
  fi
done

[ "$modified" -eq 1 ] && echo "⚠️  Passwords replaced with <DeletedPassword>. Review staged diff before pushing."
exit 0
