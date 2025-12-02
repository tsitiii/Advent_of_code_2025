# arr = list(map(str,input().split()))
dial = 50
cnt = 0
# arr = [
#         "L68", "L30", "R48", "L5",
#         "R60", "L55",
#         "L1", "L99", "R14", "L82"
#         ]dial = 50
cnt = 0

arr = []
with open("input.txt") as f:
    arr = [line.strip() for line in f]
dial = 50
cnt = 0

for move in arr:
    num = int(move[1:])
    if move[0] == "L":
        for _ in range(num):
            dial -= 1
            if dial < 0:
                dial = 99
            if dial == 0:
                cnt += 1
    else:
        for _ in range(num):
            dial += 1
            if dial > 99:
                dial = 0
            if dial == 0:
                cnt += 1

print(cnt)
