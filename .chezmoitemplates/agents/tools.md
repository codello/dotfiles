## Web Research

- Use the GitHub MCP for searches about GitHub repositories, issues, pull requests, workflows, and code.
- Use Tavily for general web search. Typical queries: error messages, known bugs, release notes, best practices, and community discussions.
- Use Exa when you do not know the exact search terms. Typical queries: libraries, alternatives, and concepts.
- Use Firecrawl Developer Search for known problems with libraries, tools, and workflows.
- Read a known URL with Tavily Extract. Use Firecrawl Scrape only when a page needs JavaScript to show its content.
- Do not send the same query to more than one provider by default. If the results are weak, make the query more precise and search again. Change the provider only when the first provider fails to give useful results.
- Verify important claims in the original source. Do not trust search snippets or generated summaries.
- Use advanced search tools sparingly (if available). Prefer low-effort options first, e.g. `tavily_research` (mini), Exa `agent_run` (low)

## CLI Tools

Prefer using `jq` and `yq` over custom python code or other scripts, especially for validation and other one-off tasks.
For validating JSON or YAML syntax only `jq` and `yq` are permitted. Do not use python, ruby, or other tools for this purpose.

## OrbStack

Docker is running locally on OrbStack. In addition to the `docker` command, you can use the `orb` command to manage containers and images. The command `orb debug [CONTAINER_NAME_OR_ID_OR_IMAGE] [COMMAND] [ARGS]...` can be used to inspect running containers or images, even if the image doesn't contain a working shell. Use this instead of `docker exec` or `docker run` for inspecting containers or images.
