import sys


def _rewind_stream(stream):
    for _ in stream:
        pass


def mapper():
    for row in sys.stdin:
        key, value = row.split('\t')
        print("{}+{}\t".format(key, value.strip()))


def reducer():
    for _ in range(20):
        key, _ = next(sys.stdin).split('\t')
        word, count = key.split("+")
        print("{}\t{}".format(word, count))
    _rewind_stream(sys.stdin)

if __name__ == '__main__':
    mr_command = sys.argv[1]
    {
        'map': mapper,
        'reduce': reducer
    }[mr_command]()
