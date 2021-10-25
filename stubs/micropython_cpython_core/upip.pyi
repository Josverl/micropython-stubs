from typing import Any

debug: bool
install_path: Any
cleanup_files: Any
gzdict_sz: Any
gzdict_buf: Any
file_buf: Any
simple_lst_re: Any

class NotFoundError(Exception): ...

def op_split(path): ...
def op_basename(path): ...
def _makedirs(name, mode: int = ...): ...
def save_file(fname, subf) -> None: ...
def install_tar(f, prefix): ...
def expandhome(s): ...

warn_ussl: bool

def url_open(url): ...
def get_pkg_metadata(name): ...
def get_latest_url_json(name): ...
def get_latest_url_simple(name): ...
def fatal(msg, exc: Any | None = ...) -> None: ...
def install_pkg(pkg_spec, install_path): ...
def install(to_install, install_path: Any | None = ...) -> None: ...
def get_install_path(): ...
def cleanup() -> None: ...
def help() -> None: ...
def main() -> None: ...
