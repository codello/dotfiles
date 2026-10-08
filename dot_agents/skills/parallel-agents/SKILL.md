---
name: parallel-agents
description: Coordinate multiple agents editing the same repository via a file-based message board at .agents/board/. Activate when the user mentions parallel agents, when you notice signs of concurrent edits (unexpected git status/diff changes, file contents changing between reads, tests failing without related code changes), or before multi-file work when .agents/board/ already has entries. One file per task with a claim-before-edit protocol; also covers changes that were never announced on the board.
---

# Parallel Agents: Message Board

Multiple agents may work in the same repository at the same time. Coordinate
through a message board: a folder of small markdown files, one per task. Each
file belongs to exactly one task; writing only your own task's file and reading
everyone else's avoids write conflicts entirely.

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
  It is excluded via the global gitignore.
- One file per task; the file name is the task's unique identifier. Name it
  `<task-slug>-<4 random characters>.md` (e.g. `auth-refactor-x7k2.md`). If the
  name already exists, pick a different suffix. A file exists exactly while
  its task is in progress — a missing file means nobody is working on that
  task anymore.
- Write only to files of your own tasks. Read all others.
- Keep files short — under ~15 lines. They describe the current state only:
  the task, the claimed files, and open conflicts. Update fields in place
  instead of appending, and drop entries that no longer apply. Never append
  progress logs, results, or summaries of completed work.

### Message file format

```markdown
started: 2026-10-08T14:30:00Z
updated: 2026-10-08T14:30:00Z
task: Fix flaky checkout tests

## Files

- `src/checkout.ts` — rewriting retry logic
- `src/checkout.test.ts` — updating tests

## Messages

- (none)
```

- `Files`: every file you intend to edit; keep it current as your scope changes.
- `Messages`: notes to other tasks (address them by task ID, i.e. file name)
  or broadcast notes. Remove notes once they no longer apply.

## Protocol

1. **Check in.** List `.agents/board/` and read every file. Note claims and
   messages addressed to your tasks.
2. **Register.** Create your task's file before your first edit.
3. **Claim before editing.** Before editing a file you have not claimed yet,
   re-check the board. If another task claims it, do not edit that
   file — wait, choose different work, or narrow your scope. Record the
   conflict in your `Messages` section.
4. **Stay current.** Update `updated` and `Files` whenever your scope changes,
   and re-check the board periodically during long tasks.
5. **Check out.** When the task is completed, delete your file — do not keep
   it as a record.
6. **Housekeeping.** You may delete files whose `updated` timestamp is more
   than 24 hours old — their task was abandoned. To take over such a task,
   delete its file and register your own.

## Changes outside the board

The board only coordinates agents that follow it. The user — and agents that
ignore the board — can change files at any time without announcing it.

- Never treat "not on the board" as "unchanged". Verify with `git diff` or a
  fresh read before editing.
- If a file changed unexpectedly since you last read it, re-read it and adapt
  your change. Never revert or rework changes you did not make.
- If unexplained changes conflict with your task, stop and ask the user before
  proceeding.
