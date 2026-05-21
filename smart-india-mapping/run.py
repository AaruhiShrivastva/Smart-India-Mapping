#!/usr/bin/env python
import os
import sys
import subprocess

# Set working directory to smart-india-mapping
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Run uvicorn
subprocess.run([
    sys.executable, "-m", "uvicorn",
    "backend.main:app",
    "--reload",
    "--host", "0.0.0.0",
    "--port", "8000"
])
