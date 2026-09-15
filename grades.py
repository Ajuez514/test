import sys


def calc_average(grades):
    total = 0
    for g in grades:
        total = total + g
    return total / len(grades)


def letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def main():
    grades = [85, 92, 78, 90, 88]
    avg = calc_average(grades)
    print("平均分:", avg)
    print("等级:", letter_grade(avg))
    return 0


if __name__ == "__main__":
    sys.exit(main())
