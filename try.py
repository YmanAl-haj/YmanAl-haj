import random


Words_list=[
{"word":"march","question":"What is third month a year? "},
{"word":"cancer","question":"Very dangerous disease? "},
{"word":"mania","question":"What is a five-letter word meaning 'insanity'? "},
{"word":"january","question":"What is first month in a year? "},
{"word":"camera","question":"Somthing taking a photo with? "},
{"word":"clock","question":"Smoething shows the time? "},
{"word":"mantle","question":"What is a six-letter word meaning 'a cloak'? "},
{"word":"car","question":"Sonmethinge you drive? "},
{"word":"mallet","question":"What is a six-letter word meaning 'a wooden hammer'? "},
{"word":"manor","question":"What is a five-letter word meaning 'the landed estate of a lord or nobleman'? "}
]

rand_question=[]
our_words=[]
for i in range(1,7):
    rand_question.append(random.choice(Words_list))

for i in range(len(rand_question)):
   our_words.append(Words_list[i]['word'])

our_words_len = list((sorted(our_words, key = len,reverse=True)))
s=0
first_word=our_words_len[s]

prob_lst=[]
for i in our_words_len:
    if len(i) < 7:
        prob_lst.append(i)

prob_lst_max_value=max(prob_lst, key=len)
h_1=prob_lst_max_value

search= list(filter(lambda x: x.lower().startswith(h_1[0]), our_words)) 

list_v_1=[]
for x in search:
    if len(x) < 7 and x !=h_1:
        list_v_1.append(x)

v_1=max(list_v_1, key=len)

h_r=[]
for i in range(1,6):
    h= list(filter(lambda x: x.lower().startswith(v_1[i]), our_words)) 
    h_r.append(h)

h_2=h_r[0]
h_3=h_r[1]
h_4=h_r[2]
h_5=h_r[3]
h_6=h_r[4]



print("        ".join(h_1),"\n")
print("\n\n".join(v_1[1:]))



# a = [h_1,v_1,h_2,h_3[0],h_4,h_5,h_6]
# for row in a:
#     print(" ".join(row))








    

print()
# n = 0
# for leftmost in range(1,7):
#     for value in range(leftmost,leftmost + 5):
#         print("{0:2d}".format(value), end=" ")
#     print("{0:2d}".format(leftmost+5))

