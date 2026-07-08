def count_words(filepath):
    #读取文件
    with open(filepath,"r",encoding="utf-8") as f:
        text = f.read()

    #全部转小写，按空格拆分单词
    words = text.lower().split()

    #去除标点符号（简单处理：把末尾的逗号、句号切掉）
    words =[w.strip(".,!?;:") for w in words]

    #统计问题
    freq = {}
    for w in words:
        freq[w] = freq.get(w,0) + 1

    #按出现次数从高到低排序
    sorted_words = sorted(freq.items(),key=lambda x:x[1],reverse=True)

    return sorted_words