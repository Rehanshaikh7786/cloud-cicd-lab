# ⚡ CLOUD//NEXUS — Cloud CI/CD Lab

> Flask → pytest → Docker → Jenkins → AWS EC2

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker&logoColor=white) ![Jenkins](https://img.shields.io/badge/Jenkins-pipeline-D24939?logo=jenkins&logoColor=white)

A practical DevOps project demonstrating automated validation, container builds, smoke tests and deployment to a single EC2 Docker host.

## Architecture
```text
GitHub push / PR -> GitHub Actions (compile + pytest)
                 -> Jenkins on EC2
                    -> Checkout -> Python validation -> pytest
                    -> Docker build -> temporary container smoke test
                    -> Deploy running container -> health verification
```

## Stack
Python 3.11 · Flask · Gunicorn · pytest · Docker · Jenkins · AWS EC2 · GitHub Actions

## Run locally
```bash
git clone https://github.com/Rehanshaikh7786/cloud-cicd-lab.git
cd cloud-cicd-lab
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
python app.py
```
Windows: activate with `.venv\\Scripts\\activate`. Visit http://localhost:5000.

## Run Docker
```bash
docker build -t cloud-cicd-lab:local .
docker run --rm -p 5000:5000 cloud-cicd-lab:local
```

## Jenkins on EC2
1. Install Docker, Python 3, Git and Jenkins on Ubuntu EC2.
2. Ensure Jenkins can execute Docker commands. Docker-group membership is root-equivalent; secure this host carefully.
3. Install Pipeline, Git and Workspace Cleanup plugins.
4. Create Pipeline job → Pipeline script from SCM → Git.
5. Repository URL: `https://github.com/Rehanshaikh7786/cloud-cicd-lab`; Script Path: `Jenkinsfile`.
6. Save and Build Now.

The Jenkinsfile uses `sudo docker`. Configure narrowly scoped passwordless sudo for Docker commands, or remove `sudo` after granting Jenkins Docker access. Allow inbound TCP 5000 only from your IP for the demo. Restrict SSH 22 to your IP; do not expose Jenkins 8080 publicly.

## Pipeline stages
Checkout → Python compile → pytest/JUnit → Docker build → temporary container smoke test → EC2 deployment and health verification.

This is a single-host learning deployment, not zero-downtime orchestration. Next steps: Amazon ECR, ECS, HTTPS reverse proxy, rollback and blue/green releases.

## API
| Method | Route | Description |
|---|---|---|
| GET | `/` | Dashboard |
| GET | `/health` | Health status |
| GET | `/ready` | Readiness |
| GET | `/api/info` | Runtime metadata |
| GET | `/student` | Lab metadata |

## Roadmap
- [x] Dashboard and health endpoints
- [x] Docker non-root runtime
- [x] pytest suite
- [x] Jenkins build/test/smoke/deploy
- [x] GitHub Actions CI
- [ ] Amazon ECR publishing
- [ ] HTTPS and custom domain
- [ ] Rollback / blue-green deployment

**Author:** [Rehan Shaikh](https://github.com/Rehanshaikh7786)
