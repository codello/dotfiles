---
name: pr-sanity-check
description: Quick sanity-check review of a GitHub pull request, for PRs that do not need a thorough review. Approves clean PRs with at most brief stylistic remarks. For required changes, opens a pending review that is not submitted.
disable-model-invocation: true
---

# PR Sanity Check

Review one GitHub pull request as a quick sanity check. This is not a thorough review. Use this skill for PRs where a quick check is enough; deeper reviews follow a different process. The input is usually a PR URL, or an owner, repo, and PR number. Extract owner, repo, and PR number from the URL.

Running this skill means the user sees no obvious issues with the PR. Do not summarize what the PR does.

In many cases the user has already done a preliminary review of the PR. Read that feedback first and build on it.

## Reading the PR

1. Get the PR details: title, description, target branch, author.
2. Get the changed files and the diff.
3. Read the existing feedback on the PR: reviews, review comments, and issue comments. Note what is already raised and what is already answered.
4. Read the touched files in full when the diff alone is not enough to judge them.
5. If the PR description does not state the intent and the change does not make the intent obvious, ask the user. Do not guess the intent.

Do not repeat feedback that is already on the PR. When an existing comment raises a valid issue, your review reflects it without restating it in detail.

## What to check

This is a sanity check, not a deep audit. Read the whole diff, then verify:

- The change does what the PR says it does.
- No obvious bugs, logic errors, or regressions in the touched code.
- No breaking changes to documented behavior, public interfaces, or configuration.
- No secrets, credentials, or debugging leftovers.
- Tests exist, or the change does not need them (docs, config, pure refactor).

Do not review code outside the diff. Do not demand improvements beyond the PR's scope. Doubts about risk or scope are a reason to ask the user, not to add review comments.

## Decision

- Everything checks out → approve the PR.
- The change is wrong, unsafe, or incomplete → request changes.

If the change looks right for a sanity check but the PR is too large or too risky for this process, stop and tell the user. Do not silently switch to a deeper review.

## Approval

Submit an approval on the PR.

- Omit the body when you have nothing to add. An empty approval is a valid result.
- Add a body only for stylistic recommendations. Keep it to short bullets, one line each.
- Never write a report. Do not narrate what you checked or why it works, for example "I checked X and it works because ...".

## Changes required

1. Start a pending review on the PR. Do not submit it.
2. Add one comment per required change, anchored to the relevant file and line.
3. Write comments that are short, direct, and actionable: state the problem and the fix. No praise, no narration of what you verified.
4. Stop. Do not submit the pending review. Tell the user the pending review is ready for them to read and submit.

Never submit a review that requests changes. Submission is always the user's decision.
