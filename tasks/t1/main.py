def printer_error(s):
    errors = 0
    for i in s:
        if i not in [chr(i) for i in range(97, 110)]:
            errors += 1
    return f"{errors}/{len(s)}"

s = "aaaxbbbbyyhwawiwjjjwwm"
print(printer_error(s))