#!/usr/bin/env python3
"""news-image-20261123 entrypoint: copy entry.png to MAKEFUN_OUTPUT_DIR.

Stdlib only. Reads the PNG header manually (struct) to verify the source
is a whole 1024x1024 PNG before copying; writes nothing beside this file.
"""
import hashlib
import os
import shutil
import struct
import sys

SRC_NAME = "entry.png"
EXPECTED_W, EXPECTED_H = 1024, 1024
MAX_BYTES = 1048576  # 1 MiB gate limit


def png_size(path):
    """Return (width, height) from the PNG IHDR chunk, or raise."""
    with open(path, "rb") as fh:
        head = fh.read(33)
    if len(head) < 33 or head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("source is not a PNG file")
    length, ctype = struct.unpack(">I4s", head[8:16])
    if ctype != b"IHDR" or length != 13:
        raise ValueError("source has no valid IHDR chunk")
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SRC_NAME)
    width, height = png_size(src)
    if (width, height) != (EXPECTED_W, EXPECTED_H):
        raise ValueError(
            "unexpected source size %dx%d, expected %dx%d"
            % (width, height, EXPECTED_W, EXPECTED_H)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, SRC_NAME)
    shutil.copyfile(src, dst)
    nbytes = os.path.getsize(dst)
    if nbytes > MAX_BYTES:
        raise ValueError("output %d bytes exceeds 1 MiB limit" % nbytes)
    src_hash = sha256_file(src)
    dst_hash = sha256_file(dst)
    if src_hash != dst_hash:
        raise ValueError("copy mismatch: %s != %s" % (src_hash, dst_hash))
    dwidth, dheight = png_size(dst)
    if (dwidth, dheight) != (EXPECTED_W, EXPECTED_H):
        raise ValueError("output size mismatch after copy")
    print("OK entry.png %dx%d %d bytes sha256=%s" % (dwidth, dheight, nbytes, dst_hash))
    return 0


if __name__ == "__main__":
    sys.exit(main())
