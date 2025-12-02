# arr = list(map(str,input().split()))
dial = 50
cnt = 0
# arr = [
#         "L68", "L30", "R48", "L5",
#         "R60", "L55",
#         "L1", "L99", "R14", "L82"
#         ]
arr = []
with open("input.txt") as f:
    arr = [line.strip() for line in f]
# print(arr)
for move in arr:
    num = int(move[1:])
    if move[0] == "L":
        new_dial = dial-num
        left = move[0]
        if new_dial == 0:
            dial = new_dial
            cnt += 1
        if new_dial < 0:
            n = abs(new_dial) - 1
            dial = 99 - n
        else:
            dial = new_dial
    elif move[0] == 'R':
        new_dial = dial + num
        if new_dial > 99:
            n = new_dial - 99
            dial = n - 1
            if dial == 0:
                cnt += 1
        else:
            dial = new_dial
print(cnt)