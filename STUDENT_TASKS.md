A local CloudNotes service is unreachable by its documented hostname, cannot write logs, has unusable structured events and is invisible to its monitoring query. Diagnose these failures, repair observability and produce an evidence-based incident report. The working local container environment is supplied and is not assessed.

You are the cloud engineer. Repair the supplied repository, validate the results locally and document the evidence in one PDF. All five tasks are compulsory. No cloud account, billing, paid registry, hosted CI or real secret is needed.

## Broken repository: fork and clone first

**Repository:** `https://github.com/kalviumcommunity/Incident-diagnostics`

1. Open the repository and click **Fork**, or use the instructor-provided offline starter.
2. Clone your fork and create a branch:

```bash
git clone https://github.com/<your-username>/Incident-diagnostics.git
cd Incident-diagnostics
git checkout -b fix/assessment
```

3. Read `README.md` for the tested local setup, commands and checks.
4. Capture the initial failures before editing. Do not delete or bypass checks.

## Task 1 - Repair application reachability

Use the supplied verbose curl and listening-socket checks to identify why host requests cannot reach CloudNotes. Correct the application listen address while preserving the documented host/container port mapping. Show failure, diagnostic reasoning and successful /health response; distinguish loopback binding from DNS failure.

**Evidence:** Original failure, relevant corrected file/diff, actual verification output and a short explanation.

## Task 2 - Repair name resolution mapping

Read network/resolve.env. Correct the hostname used by the project-provided curl --resolve wrapper so notes.test resolves to the documented localhost endpoint for this exercise. Show the failed request and corrected HTTP response, explain DNS name/IP/port roles, and provide a layered troubleshooting sequence. Do not edit system DNS files.

**Evidence:** Original failure, relevant corrected file/diff, actual verification output and a short explanation.

## Task 3 - Repair structured logging

Compare application output with the supplied JSON log schema. Fix the log-level field mapping in app/log-schema.json so request id, timestamp, level and message can be searched by the local Python log-query tool. Generate a known failing request and retrieve its correlated error record. Include original/mended JSON and command output. Do not log note bodies or credentials.

**Evidence:** Original failure, relevant corrected file/diff, actual verification output and a short explanation.

## Task 4 - Repair monitoring visibility

Inspect the supplied monitoring configuration and actual metrics endpoint. Fix the query to use the emitted request counter name. Run the local monitoring script against timestamped traffic samples, show request/error results and select a sensible user-impact alert condition. This task uses provided scripts, not a new monitoring-stack installation.

**Evidence:** Original failure, relevant corrected file/diff, actual verification output and a short explanation.

## Task 5 - Repair write permissions and close the incident

Diagnose the log directory write failure using id, ls -ld and the provided non-root permission check. Fix owner-write mode in the documented image setup, not chmod 777 or root runtime. Verify restart, reachable endpoint and readable structured logs. Submit timeline, root cause chain, before/after evidence and one preventive action. Explain Linux/network diagnosis and log/incident evidence.

**Evidence:** Original failure, relevant corrected file/diff, actual verification output and a short explanation.

## Submission guidelines

Upload one PDF containing:

- name, section, environment/tool versions and forked repository URL or offline starter identifier;
- one labelled architecture or request-path diagram;
- Task 1 to Task 5 evidence, readable code/configuration excerpts and actual command output;
- original issue -> diagnosis -> fix -> verification summary;
- remaining limitations and the rebuild/cleanup procedure.

Use fake values only. Do not include real credentials, tokens, private keys, raw Terraform state or local secret files. A screenshot is not sufficient without the diagnosis and explanation. Equivalent valid commands are accepted. If a tool is unavailable, show the actual error and corrected files; static reasoning can earn applicable partial credit, but must not be presented as a passed runtime test.

## Simple evaluation rubric - 40 marks

| Marks | Criterion | Award marks for |
|---:|---|---|
| 8 | Reachability diagnosis | Correct interface binding, meaningful process/socket checks and successful host request. |
| 8 | Name resolution | Consistent local hostname override, successful request and layered diagnosis. |
| 8 | Structured logging | Correct log schema and real error event retrievable by request id. |
| 8 | Monitoring query | Query matches emitted request metric; real samples and justified user-impact alert. |
| 8 | Permissions and incident | Least-required non-root write permission, working log output and evidence-based incident report. |

Award partial credit for correct diagnosis, repair and verification even when another task remains incomplete. Assess technical correctness and evidence of working behavior, not grammar, screenshot aesthetics or one prescribed wording. Task 5 has equal module shares; accept equivalent technically valid solutions.
