with open("binary", "bw") as bin_file:
    for i in range(1, 17):
        bin_file.write(bytes([i]))

with open("binary", "br") as binFile:
    for b in binFile:
        print(b)
