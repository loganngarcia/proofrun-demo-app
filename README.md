# proofrun-demo-app

Tiny customer-import service used to demo ProofRun. After upgrading Pydantic 1.x to 2.x,
rows that omit `nickname` are rejected even though customers are allowed to omit it.

Run: `pip install -r requirements.txt && pytest`  (one test fails).
