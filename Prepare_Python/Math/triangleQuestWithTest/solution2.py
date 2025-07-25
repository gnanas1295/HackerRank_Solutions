def triangleQuest(n: int) -> list:
    triangle = []
    for i in range(1, n):
        triangle.append((((10**i) - 1) // 9) * i)
    return triangle


if __name__ == "__main__":
    triangleValue = int(input())
    values = triangleQuest(triangleValue)
    for i in values:
        print(i)
