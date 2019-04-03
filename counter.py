def counter(count):
    if count > 0:
        print(count, ", ", end="")
        counter(count - 1)
    else:
        print(count)
    return

counter(10)