n=int(input())
book_list=[]

for i in range(n):
    book_list.append(input())

book_list.sort()    
m_book=book_list[0]
m_cnt=book_list.count(m_book)

for i in book_list:
    if book_list.count(i)>m_cnt:
        m_book=i
        m_cnt=book_list.count(i)

print(m_book)
