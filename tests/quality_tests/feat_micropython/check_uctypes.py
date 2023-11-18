"""
Sample from micropython documentaton
ref: https://docs.micropython.org/en/latest/library/uctypes.html
"""

# make it work
f = open("elf_file.bin")
# --------------------------------

import uctypes

#------------------------------------------------------------------------------------
# Example 1: Subset of ELF file header
# https://wikipedia.org/wiki/Executable_and_Linkable_Format#File_header
ELF_HEADER = {
    "EI_MAG": (0x0 | uctypes.ARRAY, 4 | uctypes.UINT8),
    "EI_DATA": 0x5 | uctypes.UINT8,
    "e_machine": 0x12 | uctypes.UINT16,
}

# "f" is an ELF file opened in binary mode
buf = f.read(uctypes.sizeof(ELF_HEADER, uctypes.LITTLE_ENDIAN))
header = uctypes.struct(
    uctypes.addressof(buf),
    ELF_HEADER,
    uctypes.LITTLE_ENDIAN,
)
# TODO: uctypes - known member does not work
assert header.EI_MAG == b"\x7fELF" # type: ignore #  uctypes - known member does not work
assert header.EI_DATA == 1, "Oops, wrong endianness. Could retry with uctypes.BIG_ENDIAN." # type: ignore #  uctypes - known member does not work
print("machine:", hex(header.e_machine))# type: ignore #  uctypes - known member does not work


#------------------------------------------------------------------------------------
# Example 2: In-memory data structure, with pointers
COORD = {
    "x": 0 | uctypes.FLOAT32,
    "y": 4 | uctypes.FLOAT32,
}

STRUCT1 = {
    "data1": 0 | uctypes.UINT8,
    "data2": 4 | uctypes.UINT32,
    "ptr": (8 | uctypes.PTR, COORD),
}

# Suppose you have address of a structure of type STRUCT1 in "addr"
addr = uctypes.struct(
    uctypes.addressof(buf),
    STRUCT1
)
# uctypes.NATIVE is optional (used by default)
struct1 = uctypes.struct(
    addr,
    STRUCT1,
    uctypes.NATIVE,
)
print("x:", struct1.ptr[0].x) # type: ignore # uctypes - known member does not work

#------------------------------------------------------------------------------------
# Example 3: Access to CPU registers. Subset of STM32F4xx WWDG block
WWDG_LAYOUT = {
    "WWDG_CR": (
        0,
        {
            # BFUINT32 here means size of the WWDG_CR register
            "WDGA": 7 << uctypes.BF_POS | 1 << uctypes.BF_LEN | uctypes.BFUINT32,
            "T": 0 << uctypes.BF_POS | 7 << uctypes.BF_LEN | uctypes.BFUINT32,
        },
    ),
    "WWDG_CFR": (
        4,
        {
            "EWI": 9 << uctypes.BF_POS | 1 << uctypes.BF_LEN | uctypes.BFUINT32,
            "WDGTB": 7 << uctypes.BF_POS | 2 << uctypes.BF_LEN | uctypes.BFUINT32,
            "W": 0 << uctypes.BF_POS | 7 << uctypes.BF_LEN | uctypes.BFUINT32,
        },
    ),
}

WWDG = uctypes.struct(0x40002C00, WWDG_LAYOUT)

WWDG.WWDG_CFR.WDGTB = 0b10  # type: ignore #  uctypes - known member does not work
WWDG.WWDG_CR.WDGA = 1  # type: ignore #  uctypes - known member does not work
print("Current counter:", WWDG.WWDG_CR.T) # type: ignore # uctypes - known member does not work

