import time
from contextlib import contextmanager
import logging

logger = logging.getLogger("PipelineTimer")

class CodeTimer:
    def __init__(self, name: str="Execution"):
        self.name = name
        self.start_time = 0.0
        self.elapsed_time = 0.0

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_time = time.perf_counter() - self.start_time
        logger.info(f"\nCode block [{self.name}] executed in {self.elapsed_time:.4f} seconds.")    