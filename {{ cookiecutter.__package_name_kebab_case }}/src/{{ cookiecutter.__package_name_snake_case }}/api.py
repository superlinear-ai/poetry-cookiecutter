"""{{ cookiecutter.project_name }} REST API."""

import asyncio
import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import coloredlogs
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Handle FastAPI startup and shutdown events."""
    # Startup events:
    # - Remove all handlers associated with the root logger object.
    for handler in logging.root.handlers:
        logging.root.removeHandler(handler)
    # - Add coloredlogs' colored StreamHandler to the root logger.
    coloredlogs.install()
    yield
    # Shutdown events.


app = FastAPI(lifespan=lifespan)


@app.get("/compute")
async def compute(n: int = 42) -> int:
    """Compute the result of a CPU-bound function."""

    def fibonacci(n: int) -> int:
        return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

    result = await asyncio.to_thread(fibonacci, n)
    return result
