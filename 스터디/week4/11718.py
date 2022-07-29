import sys

# 반복문과 try문을 통해 입력을 받는다.
while True:
    try:
        word = str(sys.stdin.readline().rstrip("\n"))
        print(word)

        # 입력이 없으면 반복문을 멈춘다.
        if word == "":
            break

    # 그 외 오류가 있으면 멈춘다.
    except:
        break