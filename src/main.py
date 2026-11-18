from fastapi import FastAPI

app = FastAPI(title="mini_api")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
