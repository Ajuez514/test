"""简单的成绩统计工具。"""


def mean(numbers):
    """平均值。空列表抛 ValueError。"""
    if not numbers:
        raise ValueError("empty list")
    return sum(numbers) / len(numbers)


def median(numbers):
    """中位数。空列表抛 ValueError。"""
    if not numbers:
        raise ValueError("empty list")
    s = sorted(numbers)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2


def pass_rate(grades, threshold=60):
    """及格率，返回 0~1 的小数。空列表抛 ValueError。"""
    if not grades:
        raise ValueError("empty list")
    passed = [g for g in grades if g >= threshold]
    return len(passed) / len(grades)


def letter_grade(avg):
    """根据平均分返回等级。"""
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    if avg >= 60:
        return "D"
    return "F"


def broken():
    unused = 42
    return "ok"
