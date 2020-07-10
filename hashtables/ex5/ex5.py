import os

def finder(files, queries):
    cache = {}
    for f in files:
        base = os.path.split(f)[-1]
        if base in cache:
            cache[base].append(f)
        else:
            cache[base] = [f]
    result = []
    for q in queries:
        if q in cache:
            result += cache[q]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
