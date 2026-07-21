# Global Agent Instructions

## GitHub MCP

When accessing GitHub, always use MCP tools (e.g. `github`-prefixed tools). Do not use `curl`, `gh`, `git`, `fetch`, or any other non-MCP mechanism to reach GitHub. If no GitHub MCP tools are available, pause and inform the user so that MCP access can be restored.

There is one exception: the `get_file_contents` tool returns the file as an attachment. If you only see "successfully downloaded text file" but not the file contents, you can try the following alternatives:

- Use the `fetch` tool, to access the file contents via raw.githubusercontent.com
- Use `gh repo read-file --repo <owner>/<repo> <path>` to read the file contents

Before reading potentially large files from GitHub, check the file size by using the `get_file_contents` tool on the parent directory of the file. The result will contain the file size in bytes. For large files you may use the `gh` CLI as part of a shell pipeline (grep, sed, ...) to only read relevant parts of the file.

Do not use GitHub MCP tools for standard Git operations (committing, pushing, pulling, etc.) unless explicitly instructed to do so. Use GitHub MCP tools only for tasks that require direct interaction with GitHub's API.
