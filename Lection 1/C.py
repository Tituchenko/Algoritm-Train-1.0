
def get_phone(s:str)->int:
    s=s.replace("-","").replace("(","").replace(")","")
    if len(s)==7:
        s="8495"+s
    if s[:2]=="+7":
        s="8"+s[2:]
    return int(s)

new_phone=get_phone(input())
answer=["NO","YES"]
for _ in range (3):
    print (answer[new_phone==get_phone(input())])
