num = 0
import time
lyric_list = []
# while True:
#     a = input()
#     if a == '':
#         b = input()
#         if b == '':
#             c = input()
#             if c == '':
#                 break
#             else:
#                 lyric_list.append(c)
#         else:
#             lyric_list.append(b)
#             continue
#     else:
#         lyric_list.append(a)

sentinel = 0
while True:
    a = input()
    if not a: sentinel += 1
    else:     sentinel = 0

    if sentinel == 3:
        break

    lyric_list.append(a)

print('입력 끝')

time.sleep(1)
length_ll = len(lyric_list)
word = input('찾을 글자는? : ')

time.sleep(1)
for i in range(length_ll):
    if word in lyric_list[i]:
        num += lyric_list[i].count(word)

print(f'이 가사에 {word}라는 단어는 총 {num}개가 있어!')

