from stats import count_words

result = count_words("sample.txt")

#输出到屏幕
print("TOP10 单词:")
for word,count in result[:10]:
    print(f"{word}:{count}次")

#写入文件
with open("result.txt","w",encoding="utf-8") as f:
    f.write("TOP10 单词:\n")
    for word,count in result[:10]:
        f.write(f"{word}:{count}次\n")  

print("结果已写入 result.txt")