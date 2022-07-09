from shared.Domain.ProgressBar.progress_bar import ProgressBar

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l = 10

result = []


def push():
    result.append(1)


ProgressBar(l, "〇〇の処理中です").run(push)

print(result)

print("debug")
