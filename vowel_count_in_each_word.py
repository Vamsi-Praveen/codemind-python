def vowel_count(str):
    vowel = set("aeiouAEIOU")
    for alphabet in str.split():
        count=0
        for i in alphabet:
            if i in vowel:
                count = count + 1
        print(count,end=" ")
str = input()
vowel_count(str)