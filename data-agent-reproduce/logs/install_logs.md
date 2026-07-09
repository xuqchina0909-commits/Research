# Install and Clone Logs

Date: 2026-07-09

## Directory Structure

Created:

```text
data-agent-reproduce/
  repos/
  benchmarks/
  systems/
  adapters/
  datasets/
  runs/
  reports/
  logs/
```

## Repository Clone Attempts

All four requested repositories were attempted with shallow clone into `data-agent-reproduce/repos/`.

| Repository | Target path | Command | Result |
| --- | --- | --- | --- |
| KramaBench | `data-agent-reproduce/repos/KramaBench` | `git clone --depth 1 https://github.com/mitdbg/KramaBench.git data-agent-reproduce/repos/KramaBench` | Failed: `Recv failure: Operation timed out`; escalated retry failed with `Failed to connect to github.com port 443 after 75018 ms: Couldn't connect to server`. |
| KramaBench | `data-agent-reproduce/repos/KramaBench` | `git clone --depth 1 git@github.com:mitdbg/KramaBench.git data-agent-reproduce/repos/KramaBench` | Failed/interrupted after long stall: `fetch-pack: unexpected disconnect while reading sideband packet`. |
| KramaBench zip | `/private/tmp/KramaBench.zip` | `curl -L --connect-timeout 30 --max-time 120 -o /private/tmp/KramaBench.zip https://github.com/mitdbg/KramaBench/archive/refs/heads/main.zip` | Failed: `curl: (28) Operation timed out after 120003 milliseconds with 0 bytes received`. |
| DAComp | `data-agent-reproduce/repos/DAComp` | `git clone --depth 1 https://github.com/ByteDance-Seed/DAComp.git data-agent-reproduce/repos/DAComp` | Failed: `Recv failure: Operation timed out`. |
| DeepEye | `data-agent-reproduce/repos/DeepEye` | `git clone --depth 1 https://github.com/HKUSTDial/DeepEye.git data-agent-reproduce/repos/DeepEye` | Failed: `Recv failure: Operation timed out`. |
| DeepAnalyze | `data-agent-reproduce/repos/DeepAnalyze` | `git clone --depth 1 https://github.com/ruc-datalab/DeepAnalyze.git data-agent-reproduce/repos/DeepAnalyze` | Failed: `Recv failure: Operation timed out`. |

## Repository Structure Inspection

No repository checkout completed, so local checks for README, requirements, pyproject, docker-compose, examples, and tests could not be performed.

| Project | Local checkout exists | README | requirements / pyproject | docker-compose | examples | tests | Runnable condition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KramaBench | no | not locally inspectable | not locally inspectable | not locally inspectable | not locally inspectable | not locally inspectable | Blocked by GitHub download failure. |
| DAComp | no | not locally inspectable | not locally inspectable | not locally inspectable | not locally inspectable | not locally inspectable | Blocked by GitHub download failure. |
| DeepEye | no | not locally inspectable | not locally inspectable | not locally inspectable | not locally inspectable | not locally inspectable | Blocked by GitHub download failure; Docker is also missing. |
| DeepAnalyze | no | not locally inspectable | not locally inspectable | not locally inspectable | not locally inspectable | not locally inspectable | Blocked by GitHub download failure; model/API configuration likely required after checkout. |

## Current Blocker

The machine can authenticate to GitHub by SSH, but repository transfer and zip download from GitHub stalled or timed out during this run. No benchmark or system code was available locally, so no official install command was run and no benchmark baseline result should be claimed.

