import subprocess


def average(values):
    if not values:
        return 0.0
    total = 0
    for v in values:
        total += v
    return total / len(values)


def last_n(items, n):
    return items[len(items) - n :]


def archive(path):
    subprocess.run(["tar", "-czf", path + ".tgz", path], check=True)
