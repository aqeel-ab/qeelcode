def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [""] * numRows
    cur_row = 0
    direction = 1

    for char in s:
        rows[cur_row] += char

        if cur_row == 0:
            direction = 1
        elif cur_row == numRows - 1:
            direction = -1

        cur_row += direction

    return "".join(rows)

#Manual test cases
print(convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
print(convert("PAYPALISHIRING", 4))  # PINALSIGYAHRPI
print(convert("ABCDE", 3))           # AEBDC
print(convert("ABCDE", 1))           # ABCDE