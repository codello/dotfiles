---
name: parallel-agents
description: Coordinate multiple agents editing the same repository via a file-based message board at .agents/board/. Activate when the user mentions parallel agents, when you notice signs of concurrent edits (unexpected git status/diff changes, file contents changing between reads, tests failing without related code changes), or before multi-file work when .agents/board/ already has entries. One file per task with a claim-before-edit protocol, plus directed messages between agents; also covers changes that were never announced on the board.
---

# Parallel Agents: Message Board

Multiple agents may work in the same repository at the same time. Coordinate
through a message board: a folder of small markdown files, one per task, plus
short message files for notes to one specific agent. Each agent writes only
its own task files, creates its outgoing messages, and deletes its incoming
messages, so write conflicts cannot happen.

The board holds current coordination state only — it is not a log or shared
memory. Other agents do not need context about your finished tasks: anything
they must know about your changes belongs in the code, commit messages, or PR
description.

## When to activate

Register on the board as soon as you suspect parallel work:

- The user mentions other agents running in parallel.
- `git status` or `git diff` shows changes you did not make.
- A file's content differs from what you read earlier in this session.
- Tests or builds fail without you having touched related code.
- `.agents/board/` exists and is not empty.

## Board conventions

- Location: `.agents/board/` in the repository root; create it if missing.
  Task files live directly in this folder, messages in
  `.agents/board/messages/`. It is excluded via the global gitignore.
- Identity: pick a short handle of 2-8 characters, lowercase letters and
  digits only (e.g. `red`). Keep it for the whole session. It must not match
  an identity already on the board; check before you register. If two active
  agents share an identity, the one with the later `started` time renames its
  task file and picks a new identity.
- One file per task; the file name is the task's unique identifier. Name it
  `<task-slug>-<identity>.md` (e.g. `auth-refactor-red.md`). If the name
  already exists, pick a different slug. A file exists exactly while its task
  is in progress — a missing file means nobody is working on that task
  anymore.
- One file per message in `.agents/board/messages/`. Name it
  `<recipient>-<sender>-<topic>.md` (e.g. `blue-red-auth-handoff.md`). If the
  name already exists, change the topic. The sender creates the file once and
  never edits it; the recipient deletes it after reading.
- Write only to your own task files. You also create the messages you send
  and delete the messages addressed to you. Read all others.
- Keep files short — under ~15 lines. They describe the current state only:
  the task, the claimed files, and broadcast notes. Update fields in place
  instead of appending, and drop entries that no longer apply. Never append
  progress logs, results, or summaries of completed work.

### Task file format

```markdown
started: 2026-10-08T14:30:00Z
updated: 2026-10-08T14:30:00Z
agent: red
task: Fix flaky checkout tests

## Files

- `src/checkout.ts` — rewriting retry logic
- `src/checkout.test.ts` — updating tests

## Messages

- (none)
```

- `agent`: your identity. Other agents use it to address messages to you.
- `Files`: every file you intend to edit; keep it current as your scope changes.
- `Messages`: broadcast notes for anyone scanning the board. Notes to one
  specific agent go in a message file instead. Remove notes once they no
  longer apply.

### Message file format

```markdown
from: red
to: blue
sent: 2026-10-18T09:30:00Z

`src/auth.ts` is free to claim now. Tests are green on main.
```

- `from` and `to` are agent identities; `sent` is an RFC 3339 timestamp.
- The body is free text; a few lines are enough.
- Send a message when one specific agent must act on it: a file handoff, a
  conflict, a request, or an answer. Broadcast notes belong in your task
  file's `Messages` section.

## Protocol

1. **Check in.** List `.agents/board/` and read every task file. List
   `.agents/board/messages/` and read every message addressed to your
   identity. Note claims and broadcast notes. Act on your messages, then
   delete them.
2. **Register.** Pick an identity that is not in use and create your task's
   file before your first edit.
3. **Claim before editing.** Before editing a file you have not claimed yet,
   re-check the board. If another task claims it, do not edit that
   file — wait, choose different work, or narrow your scope. Send the owning
   agent a message that describes the conflict.
4. **Stay current.** Update `updated` and `Files` whenever your scope changes,
   and re-check the board and your messages periodically during long tasks.
5. **Check out.** When the task is completed, delete your file — do not keep
   it as a record.
6. **Housekeeping.** You may delete task files whose `updated` timestamp is
   more than 24 hours old — their task was abandoned. To take over such a
   task, delete its file and register your own. You may delete a message
   whose recipient has no task file on the board and whose `sent` time is
   more than one hour old — nobody will consume it. Do not delete a message
   because its sender is gone: handoff messages are sent when the sender
   checks out.

## Changes outside the board

The board only coordinates agents that follow it. The user — and agents that
ignore the board — can change files at any time without announcing it.

- Never treat "not on the board" as "unchanged". Verify with `git diff` or a
  fresh read before editing.
- If a file changed unexpectedly since you last read it, re-read it and adapt
  your change. Never revert or rework changes you did not make.
- If unexplained changes conflict with your task, stop and ask the user before
  proceeding.
