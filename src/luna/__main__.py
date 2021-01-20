"""
Buggy entry point
"""
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "buggy:APP",
        host="0.0.0.0",
        port=3030,
        log_level="info",
    )
