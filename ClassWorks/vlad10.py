def year_to_century(year: int) -> int:
    return (year - 1) // 100 + 1


print(year_to_century(1501))
