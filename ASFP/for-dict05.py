mos_qty = {
    "2020년 6월": [9, 5, 14, 8],
    "2020년 7월": [15, 6, 17,15],
    "2020년 8월": [26, 18, 26, 10]
}

month = "2020년 6월"
total = sum(mos_qty[month])
print(month + " 판매량: " + str(total))

month = "2020년 7월"
total = sum(mos_qty[month])
print(month + " 판매량: " + str(total))

month = "2020년 8월"
total = sum(mos_qty[month])
print(month + " 판매량: " + str(total))