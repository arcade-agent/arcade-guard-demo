# arcade-agent demo: orders service

A layered service written by a coding agent with the
[arcade-agent](https://github.com/arcade-agent/arcade-agent) guardrail.
`architecture.spec.json` states the intended architecture; the `Architecture`
workflow runs `arcade-guard check` on every pull request.

The open pull request adds a shortcut from `app/api` to `app/store`. Its check fails
with the rule and a fix, exactly as `arcade-guard check` reports it inside the
agent's loop.
