#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " <save.qca>")
    else:
        save_f = ""
        with open(sys.argv[1], "r") as f_in:
            save_f = f_in.read()
        save_f = save_f.replace(",", ".")
        with open(sys.argv[1], "w") as f_out:
            f_out.write(save_f)
