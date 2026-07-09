# Environment Check

Date: 2026-07-09

Working directory: `/Users/xuq/Documents/Research`

## Required Commands

| Command | Status | Observed output | Impact |
| --- | --- | --- | --- |
| `git --version` | available | `git version 2.50.1 (Apple Git-155)` | Git operations are available. |
| `python --version` | missing | `zsh:1: command not found: python` | Use `python3` instead. Some upstream scripts may require a `python` alias. |
| `pip --version` | missing | `zsh:1: command not found: pip` | Use `pip3` instead. Some install docs may need command substitution. |
| `node --version` | missing | `zsh:1: command not found: node` | Node-based frontends or tooling cannot run until Node.js is installed. |
| `npm --version` | missing | `zsh:1: command not found: npm` | Node package installation cannot run until Node.js/npm is installed. |
| `docker --version` | missing | `zsh:1: command not found: docker` | Docker-based systems, including possible DeepEye deployment, cannot be started locally. |
| `docker compose version` | missing | `zsh:1: command not found: docker` | Docker Compose workflows cannot run locally. |

## Additional Checks

| Command | Status | Observed output |
| --- | --- | --- |
| `python3 --version` | available | `Python 3.9.6` |
| `pip3 --version` | available | `pip 21.2.4 from /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/site-packages/pip (python 3.9)` |

## Installation Suggestions

- Install Python command aliases if upstream scripts require `python`/`pip`: use pyenv, conda, or shell aliases to point to Python 3.
- Install Node.js/npm before attempting any frontend or web UI workflows.
- Install Docker Desktop before attempting containerized systems or `docker compose` examples.

