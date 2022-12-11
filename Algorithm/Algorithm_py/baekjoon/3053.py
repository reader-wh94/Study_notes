# https://yoonsang-it.tistory.com/15
import math

r = int(input())

uclid = r * r * math.pi
taxi = 2 * r * r

print(f"{format(uclid, '.6f')}")
print(f"{format(taxi, '.6f')}")