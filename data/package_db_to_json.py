# %%
# Configure logging to output to the notebook
import logging
import sqlite3
from pathlib import Path

import jsons

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
log = logging.getLogger()

# %%

db_path = Path("../data/all_packages.db")
if not db_path.exists():
    db_path = Path("repos/micropython-stubs/data/all_packages.db")
    if not db_path.exists():
        raise FileNotFoundError("Database file not found")

conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row  # return rows as dicts
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


schema = "https://raw.githubusercontent.com/Josverl/micropython-stubber/main/data/schema/packages-v1.0.0.json"
output = {"$schema": schema, "packages": stublist}

with open(db_path.with_name("stub-packages.json"), "w") as f:
    text = jsons.dumps(output, jdkwargs={"indent": 4})
    f.write(text)


# %%
