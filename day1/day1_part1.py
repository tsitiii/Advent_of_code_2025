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

for move in arr:
    num = int(move[1:])
    if move[0] == "L":
        new_dial = dial - num
        while new_dial < 0:
            cnt += 1
            new_dial += 100
    else:
        new_dial = dial + num
        while new_dial > 99:
            cnt += 1
            new_dial -= 100
    dial = new_dial
    if dial == 0:
        cnt += 1

print(cnt)
