# TODO Найдите количество книг, которое можно разместить на дискете
symbol = 4
stroke = 25
list= 50
book = 100
kb = 1024
one_mb = 1024
a = symbol * stroke * list * book
book_in_mb = a/kb/one_mb
cout = 1
while book_in_mb <= 1.44:
    book_in_mb+=book_in_mb
    cout+=1
print("Количество книг, помещающихся на дискету:", cout)
