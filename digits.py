ar = [
    " HH   H  HH  HH   H HHHH HH HHHH HH  HH ",
    "H  H HH H  HH  H H  H   H     H H  HH  H",
    "H  H  H   H   H HHHH HH HHH  H   HH  HHH",
    "H  H  H  H  H  H   H   HH  H H  H  H   H",
    " HH   H HHHH HH    HHHH  HH H    HH  HH "
]

for i in range(5):
    for n in "5134634":
        print(ar[i][(int(n))*4:(int(n)+1)*4], end="  ")
    print()
