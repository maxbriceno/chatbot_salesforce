import subprocess
import sys
import os
import click
from colorama import init
from logger.my_logger import ColorEnum, MyLogger

#* Logger Setup
init(autoreset=True)
logger = MyLogger.get_instance()
logger.log(message="1/4 Initializing...", level=0)

has_to_create_index = click.prompt(
        "Do you want to (re)create the index?",
        type=click.Choice(["yes", "no"], case_sensitive=False)
    )

def run_and_wait(command):
    logger.log(f"Running: {' '.join(command)}", level=1)
    proc = subprocess.Popen(command)
    proc.wait()
    return proc

def run_in_background(command):
    try:
        logger.log(message=f"Running in background: {' '.join(command)}", level=1, color=ColorEnum.CYAN)
        proc = subprocess.Popen(command)
        logger.log(message=f"✅ Subproces {command} correctly launched", level=1, color=ColorEnum.GREEN)
        return proc
    except Exception as e:
        logger.log(message=f"❌ Error in subprocess {command}: with error {e}", level=1, color=ColorEnum.RED)
        raise e

python_exe = sys.executable

if has_to_create_index.lower() == "yes":
    logger.log(message="2/4 Creating index...", level=1)
    run_and_wait([python_exe, os.path.join("src", "ingestion", "ingest.py")])
else:
    logger.log(message="2/4 Skipped creating index as requested...", level=1)

logger.log(message="3/4 Running BE...", level=1)
fastapi_proc = run_in_background([python_exe, "-m", "uvicorn", "src.app.app:app", "--reload"])

logger.log(message="4/4 Running FE...", level=1)
streamlit_proc = run_in_background([python_exe, "-m", "streamlit", "run", os.path.join("src", "ui", "ui.py")])

try:
    fastapi_proc.wait()
    streamlit_proc.wait()
except KeyboardInterrupt:
    print("Stopping all processes...")
    fastapi_proc.terminate()
    streamlit_proc.terminate()
