# Incident-diagnostics

Local Cloud Computing assessment starter.


## Environment and zero-cost boundary

Use Python 3.10+, Git, curl and an instructor-preinstalled free OCI engine with Compose.
Canonical free route: Linux Docker Engine (or instructor-tested Podman compatibility).
macOS may use free Colima/Lima; Docker Desktop is optional only if free use is permitted
by its license. No paid account, cloud project, registry login, trial credits or hosted CI.
Application images use Python 3.12.12 and the standard library only. Base images are pinned
to verified multi-architecture digests. Initial public image downloads need internet; instructor
should preload/cache images for the exam to avoid rate limits. Local power, hardware and
internet are assumed, not supplied. Use a free text editor, diagrams.net/Excalidraw or plain
Markdown for diagrams; export PDF with a free browser/office suite. No paid PDF tool required.

Reference environment: macOS arm64, Docker Engine 29.4.3, kind 0.30.0 local Kubernetes
v1.34.0. Docker Desktop was the host engine, not a mandatory licensed dependency. This records the author's test environment, not a requirement to purchase Docker
Desktop. Other runtime/OS combinations need instructor validation. Linux/WSL2 recommended
for native CLI commands; use WSL paths for executable shell scripts. Run shell scripts from
repository root. chmod +x scripts/*.sh if an archive lost executable bits.

Practical host allowance: 4 CPU, 8 GB RAM, 8 GB free disk for container-only work; 4 CPU,
12 GB RAM, 12 GB free disk for Kubernetes work (allocate >=4 GB to the engine). These are
planning recommendations, not measured minimums. Instructor installs tools and warms caches
before the timed assessment. Allow a provisional 2-3 hour practical window, then calibrate
with a representative student; this is not a measured student completion time.

There are five planted assessment issues, one per task. Setup and tools are not extra faults.
Some symptoms interact. Use the task ordering below and static checks to diagnose tasks even
when earlier runtime work is incomplete. Do not delete checks, force success or change the
specified ports/contracts. Exercise cloud policy models are design validation only, not real
GCP enforcement. Keep your changes and evidence scoped to this repository.

Read [STUDENT_TASKS.md](STUDENT_TASKS.md) for the exact assessment and rubric.

## Evidence and safe cleanup

Start from reports/report-template.md and release-notes.md. Store local transcripts under
ignored evidence/. Never commit real secrets, generated plans/state or local .env. Fake demo
identity strings end in example.invalid. No real GCP operations are performed.
Run scripts/cleanup.sh when finished; it deletes only this exercise's services/namespace.
Do not run system-wide docker prune, reset Kubernetes or delete unrelated namespaces.

## Workflow

```bash
./scripts/check-prereqs.sh
docker compose up -d --build
docker compose logs --tail=30 app
curl -v --max-time 5 http://127.0.0.1:18084/health
docker compose exec -T app python3 -c "import os; print('uid',os.getuid())"
```

Task 1: inspect BIND_HOST in compose.yaml, startup process, listener behavior and host request.
If ss/netstat is unavailable in the minimal image use the supplied Python socket check:

```bash
docker compose exec -T app python3 -c "import socket; s=socket.create_connection(('127.0.0.1',8080),2); print('inside loopback reachable'); s.close()"
```

A working loopback-only container listener can still be unreachable through published ports.
After Compose configuration changes use docker compose up -d --build --force-recreate.
Task 2: network/resolve.env drives the project-local curl --resolve wrapper:

```bash
./scripts/request.sh
python3 checks/check.py resolve
```

It deliberately targets notes.test; do not edit global DNS or /etc/hosts. This is an override,
not authoritative DNS. Task 3: app/log-schema.json controls structured log field names.
Task 5 initially prevents file logging, but stderr remains usable. You can diagnose the schema
independently in docker compose logs and complete the file query after permission repair.

```bash
curl -s -H 'X-Request-ID: exam-error-1' http://127.0.0.1:18084/fail
docker compose logs --tail=30 app
python3 scripts/query-logs.py --request-id exam-error-1
```

Task 4: monitoring/queries.json must match actual emitted /metrics series. Generate traffic:

```bash
curl -s http://127.0.0.1:18084/health
curl -s http://127.0.0.1:18084/fail
python3 scripts/monitor.py
python3 checks/check.py queries
```

Task 5: Dockerfile creates /app/logs owned by UID10001; its incorrect owner-write mode is
repairable through the image setup. No host mount, chown/sudo, root runtime or chmod777 needed.
Build setup may create/chown directories in image layers; application and student permission
checks remain non-root. Rebuild/recreate after fixing mode; inspect:

```bash
docker compose exec -T app sh -c 'id; ls -ld /app/logs'
python3 checks/check.py permissions
```

Container logging is ephemeral in this local exercise; prove restart and new log generation,
not archival durability. Do not confuse restoring container file permissions with log retention.
