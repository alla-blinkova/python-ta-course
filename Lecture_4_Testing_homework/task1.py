def get_continued_fraction(inp_fraction: str) -> str:
    fraction_parts = inp_fraction.split("/")
    numerator = int(fraction_parts[0])
    denominator = int(fraction_parts[1])
    result = []
    if denominator < 0:
        raise ValueError("Wrong input string format")
    while True:
        integer_part = numerator // denominator
        numerator = numerator % denominator
        result.append(integer_part)
        if numerator == 0:
            break
        numerator, denominator = denominator, numerator
    return " ".join(str(i) for i in result)
