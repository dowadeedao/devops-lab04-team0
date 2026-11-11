def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("ห้ามหารด้วยศูนย์")
    return a / b

def power(a, b):
    return a ** b
def average(numbers):
    if len(numbers) == 0:
        raise ValueError("ต้องมีตัวเลขอย่างน้อย 1 ตัว")
    return sum(numbers) / len(numbers)
