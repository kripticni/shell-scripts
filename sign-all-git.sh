#!/usr/bin/env bash

git rebase --interactive --root

while [ $? -eq 0 ]; do
        git commit --amend --no-edit -S
        git rebase --continue
done

echo "All commits have been verified."
