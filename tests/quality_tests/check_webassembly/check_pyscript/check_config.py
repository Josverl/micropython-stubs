# PyScript 2026.7.3: context and display contracts.
from pyscript import RUNNING_IN_WORKER, config, current_target, display, document, js_modules, window
from pyscript.context import current_target as context_target

interpreter_type: object = config["type"]
target: object = current_target()
same_target: object = context_target()
display("PyScript", target="my-h2", append=False)
print(RUNNING_IN_WORKER, interpreter_type, target, same_target, document, js_modules, window)
