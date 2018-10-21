def split_and_join(line):
    k=line.split()
    k="-".join(k)
    return k

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result