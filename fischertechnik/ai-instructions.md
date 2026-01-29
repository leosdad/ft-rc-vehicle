
# AI editing notes (project-specific)

Use these instructions for the fischertechnik folder.

- Put function docstrings as the first statement in the function (triple-quoted).
- Use one-line concise docstrings; add a short second sentence only if needed.
- Preserve parameter type info using `@param` tags (one line each).
- Keep ONE blank line between the description and the `@param`/`@return` block.
- Omit `@return: None`; include `@return` only for non-None returns.
- Prefer minimal changes: move misplaced strings, add concise docs, avoid refactors.
- When helpful, add lightweight Python type hints (keep edits small).

## Style notes

- Keep edits surgical and consistent with surrounding code style.
- Do not remove useful comments or types unless replacing them with equivalent info.

## Examples

- Good: """Set motor speed.

  @param speed: int (0-512)
  """
- Bad: placement after function body or vague return-only docstrings.
