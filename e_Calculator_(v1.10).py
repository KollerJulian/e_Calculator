import decimal
import time

print("""
=============================================================
|  .ooooo.                                                  |
| d88' `88b       e_Calculator by julien_Blue               |
| 888ooo888       v1.10   <2018>                            |
| 888    .o                                                 |
| `Y8bod8P'                                                 |
=============================================================
""")


def main():
    decimal.getcontext().prec = int(input("Set decimal precision of e: ")) + 1

    d = open("e_" + str(decimal.getcontext().prec - 1) + ".txt", "w")

    try:
        d.write(str(euler()))   # calls euler() function and writes its return value to external file
    except PermissionError:  # import sys to exit program with sys.exit to avoid program crash
        import sys
        input("Failed to create or open external file... (PermissionError)\nPress Enter to Exit")
        sys.exit(0)
    finally:
        d.close()  # closes external file to ensure its consistence

    print("Value successfully written to external file (e_" + str(decimal.getcontext().prec - 1) + ".txt)")
    input("Press Enter to Exit")


def euler():
    start = time.time()
    decimal.getcontext().prec += 2  # extra digits for intermediate steps
    e, prev, n = decimal.Decimal(), 1, 0  # initialize variables, e has to be unequal to prev to enter while loop

    print("Calculating...")

    while e != prev:
        prev = e
        e += decimal.Decimal(1) / factorial(n)  # calls factorial(), return value is n factorial
        n += 1

    decimal.getcontext().prec -= 2  # remove extra digits to restore original precision
    finish = time.time()
    print("Done", '(' + str(round(finish - start, 3)) + 's)!')
    return +e


def factorial(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


main()  # calls the main function

# end
