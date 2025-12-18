from _typeshed import Incomplete

_RE_IMPORT: Incomplete
_RE_FROM_IMPORT: Incomplete
_RE_GLOBAL: Incomplete
_RE_ASSIGN: Incomplete
_HISTORY_LIMIT: Incomplete
CHAR_CTRL_A: int
CHAR_CTRL_B: int
CHAR_CTRL_C: int
CHAR_CTRL_D: int
CHAR_CTRL_E: int

async def execute(code, g, s): ...
async def task(g=None, prompt: str = "--> ") -> None: ...
def raw_paste(s, window: int = 512): ...
def raw_repl(s, g: dict):
    """
    This function is blocking to prevent other
    async tasks from writing to the stdio stream and
    breaking the raw repl session.
    """
