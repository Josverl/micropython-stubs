from typing import Tuple
from typing_extensions import TypeAlias

# TODO ? Move into OS or vfs module ?

stat_result : TypeAlias = Tuple[int, int, int, int, int, int, int, int, int, int]
"""A 10-tuple containing the result of an os.stat() call.
The tuple contains the following values:
- 0 st_mode: File mode (permissions and type)
- 1 st_ino: always 0
- 2 st_dev: always 0
- 3 st_nlink: always 0
- 4 st_uid: always 0
- 5 st_gid: always 0
- 6 st_size: Size of file in bytes
- 7 st_atime: Last access time (in seconds since epoch)
- 8 st_mtime: Last modification time (in seconds since epoch)
- 9 st_ctime: Last status change time (in seconds since epoch)

https://docs.micropython.org/en/latest/library/os.html#os.stat
https://docs.python.org/3/library/os.html#os.stat_result
"""
statvfs_result : TypeAlias = Tuple[int, int, int, int, int, int, int, int, int, int]
"""A 10-tuple containing the result of an os.statvfs() call.
The tuple contains the following values:
f_bsize – file system block size
f_frsize – fragment size
f_blocks – size of fs in f_frsize units
f_bfree – number of free blocks
f_bavail – number of free blocks for unprivileged users
f_files – number of inodes
f_ffree – number of free inodes
f_favail – number of free inodes for unprivileged users
f_flag – mount flags
f_namemax – maximum filename length

https://docs.micropython.org/en/latest/library/os.html#os.statvfs
https://docs.python.org/3/library/os.html#os.statvfs
"""

# defined in extmod/vfs_posix.c 

#  function vfs_posix_stat

static mp_obj_t vfs_posix_stat(mp_obj_t self_in, mp_obj_t path_in) {
    mp_obj_vfs_posix_t *self = MP_OBJ_TO_PTR(self_in);
    struct stat sb;
    const char *path = vfs_posix_get_path_str(self, path_in);
    int ret;
    MP_HAL_RETRY_SYSCALL(ret, stat(path, &sb), mp_raise_OSError(err));
    mp_obj_tuple_t *t = MP_OBJ_TO_PTR(mp_obj_new_tuple(10, NULL));
    t->items[0] = MP_OBJ_NEW_SMALL_INT(sb.st_mode);
    t->items[1] = mp_obj_new_int_from_uint(sb.st_ino);
    t->items[2] = mp_obj_new_int_from_uint(sb.st_dev);
    t->items[3] = mp_obj_new_int_from_uint(sb.st_nlink);
    t->items[4] = mp_obj_new_int_from_uint(sb.st_uid);
    t->items[5] = mp_obj_new_int_from_uint(sb.st_gid);
    t->items[6] = mp_obj_new_int_from_uint(sb.st_size);
    t->items[7] = mp_obj_new_int_from_uint(sb.st_atime);
    t->items[8] = mp_obj_new_int_from_uint(sb.st_mtime);
    t->items[9] = mp_obj_new_int_from_uint(sb.st_ctime);
    return MP_OBJ_FROM_PTR(t);
}


#  function vfs_posix_statvfs
#define F_FAVAIL sb.f_favail
#define F_NAMEMAX sb.f_namemax
#define F_FLAG sb.f_flag


static mp_obj_t vfs_posix_statvfs(mp_obj_t self_in, mp_obj_t path_in) {
    mp_obj_vfs_posix_t *self = MP_OBJ_TO_PTR(self_in);
    STRUCT_STATVFS sb;
    const char *path = vfs_posix_get_path_str(self, path_in);
    int ret;
    MP_HAL_RETRY_SYSCALL(ret, STATVFS(path, &sb), mp_raise_OSError(err));
    mp_obj_tuple_t *t = MP_OBJ_TO_PTR(mp_obj_new_tuple(10, NULL));
    t->items[0] = MP_OBJ_NEW_SMALL_INT(sb.f_bsize);
    t->items[1] = MP_OBJ_NEW_SMALL_INT(sb.f_frsize);
    t->items[2] = MP_OBJ_NEW_SMALL_INT(sb.f_blocks);
    t->items[3] = MP_OBJ_NEW_SMALL_INT(sb.f_bfree);
    t->items[4] = MP_OBJ_NEW_SMALL_INT(sb.f_bavail);
    t->items[5] = MP_OBJ_NEW_SMALL_INT(sb.f_files);
    t->items[6] = MP_OBJ_NEW_SMALL_INT(sb.f_ffree);
    t->items[7] = MP_OBJ_NEW_SMALL_INT(F_FAVAIL);
    t->items[8] = MP_OBJ_NEW_SMALL_INT(F_FLAG);
    t->items[9] = MP_OBJ_NEW_SMALL_INT(F_NAMEMAX);
    return MP_OBJ_FROM_PTR(t);
}





# def foo() -> stat_result:
#     return (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


# x = foo