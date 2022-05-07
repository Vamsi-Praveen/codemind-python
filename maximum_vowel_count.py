def vowel_count(str):
    l=[]
    vowel = set("aeiouAEIOU")
    for alphabet in str.split():
        count=0
        for i in alphabet:
            if i in vowel:
                count = count + 1
            l.append(count)
    print(max(l))
str = input()
vowel_count(str)