## Handcrafted MicroPython asyncio stubs for the standard library

The asyncio module in this folder was hand tuned based on ascuncio from _typeshed, and updated for MicroPython 1.24.1.
It has received limited testing, but seems to do quite okay in the quick QA testing that I've been running on a bunch of MicroPython AsyncIO samples ( Thanks Peter Hinch).


### Goal and rationale:
It proved complex to impossible to generate good functioning async IO type stops based on the limited information available in the Python implementation of AC IO.Or based on the documentation rather.than try and rebuild the work that has been done in type chat. I took the opposite approach and tried to enhance time chat with some of the MicroPython capabilities and features and try to remove the features that were not available in MicroPython.


### TODO:
- Move to '/reference' folder ?
- There are likely capability.'s document in these type stubs that are not actually available on MicroPython. These will need to be found and subsequently removed.
- Automatic, updates the MicroPython dock strings and type references based on the docs tabs or the reference stubs.
- Ability to update this to a newer version of typeshed stubs
- Check if there is additional work needed for WASM 

### Overview of changes made : 
- Add backlog parameter to asyncio streams and update StreamWriter.awrite signature
- add ThreadSafeFlag
- fix StreamWriter.write , add .awrite
- fixup for sleep_ms

See the [changes.patch](./changes.patch) file for a summary of all changes made to the original stubs.