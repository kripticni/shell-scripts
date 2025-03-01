#!/usr/bin/env bash

# Function to verify a commit and re-sign if not verified
verify_and_sign_commit() {
        local commit_hash=$1
        echo "Checking commit $commit_hash..."

        verification_result=$(git verify-commit $commit_hash 2>&1)

        if [[ $verification_result == *"No signature"* || $verification_result == *"BAD signature"* ]]; then
                echo "Commit $commit_hash is not signed or has a bad signature. Re-signing..."

                # checkout and resign
                git checkout $commit_hash
                git commit --amend --no-edit -S

                # continue rebase
                git rebase --continue || exit 1
        else
                echo "Commit $commit_hash is signed and verified."
        fi

        echo
}

# start the process from the root commit
git rebase --interactive --root

# iterate through all commits in the repository and sign those that are not verified
git rev-list --all | while read commit_hash; do
        verify_and_sign_commit $commit_hash
done
