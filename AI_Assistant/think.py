print("hello!!")

your_order = ""
if your_order == "":
    AI_ans = "..."
elif your_order == "hi" or your_order == "hello":
    AI_ans = "Hello there!"
elif your_order == "today" or your_order == "day":
    AI_ans = "I don't know :)))"
else:
    AI_ans = "Something went wrong! Please try again"

print(AI_ans)
