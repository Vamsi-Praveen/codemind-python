l=[]
st=input()
st=st.lower()
for word in st.split():
    if word==word[::-1]:
        l.append(word) 

print(len(l))