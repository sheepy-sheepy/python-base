def past(h: int,
         m: int,
         s: int) -> int:
    ms = 1000 * (60 * (h * 60 + m) + s)
    return ms


print(past(0, 1, 1))  # 61000
