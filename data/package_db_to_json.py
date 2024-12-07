# %%
# Configure logging to output to the notebook
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
log = logging.getLogger()

# %%
import sqlite3
from pathlib import Path

db_path = Path("../data/all_packages.db")
if not db_path.exists():
    raise FileNotFoundError("Database file not found")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# %%
SHORT_LIST = """
SELECT DISTINCT name, mpy_version, port, board, variant FROM packages 
    where publish == TRUE
    AND mpy_version NOT LIKE '%-preview%'
    order by mpy_version DESC, name
"""
cursor.execute(SHORT_LIST)
stublist = cursor.fetchall()

log.info(f"found {len(stublist)} unique stub/version combinations")

# %%
import json
from pathlib import Path

schema = "https://raw.githubusercontent.com/Josverl/micropython-stubber/main/data/schema/packages-v1.0.0.json"
output = {"$schema": schema, "packages": stublist}

with open("../data/stub-packages.json", "w") as f:
    json.dump(output, f, indent=4)

# %%
