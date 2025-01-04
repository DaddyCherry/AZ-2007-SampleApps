# ここに足し算の関数を作成する
def add(a, b):
    return a + b

# ここに引き算の関数を作成する
def subtract(a, b):
    return a - b

# ここに割り算の関数を作成する
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def main():
    print("Hello world")
    print(add(1, 2))
    print(subtract(5, 3))
    print(divide(10, 2))


if __name__ == "__main__":
    main()