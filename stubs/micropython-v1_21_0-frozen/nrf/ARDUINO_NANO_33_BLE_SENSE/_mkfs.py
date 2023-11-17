import os, nrf

try:
    pass

    os.VfsLfs1.mkfs(nrf.Flash())
except ImportError:
    try:
        pass

        os.VfsLfs2.mkfs(nrf.Flash())
    except ImportError:
        try:
            pass

            os.VfsFat.mkfs(nrf.Flash())
        except ImportError:
            pass
        except OSError as e:
            if e.args[0] == 5:  # I/O Error
                flashbdev_size = (nrf.Flash.ioctl(4, 0) * nrf.Flash.ioctl(5, 0)) // 1024
                print()
                print("Is `FS_SIZE=%iK` enough for FAT filesystem?" % flashbdev_size)
