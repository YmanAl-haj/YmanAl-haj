import random


Words_list=[  {'word': 'Yemen', 'question': 'Country?'}, {'word': 'Forg', 'question': 'Country?'},
              {'word': 'yes', 'question': 'Anser?'}, {'word': 'July', 'question': 'The seventh month of the year'},
              {'word': 'Python', 'question': 'A programming language'},
              {'word': 'Happy', 'question': 'Opposite of sad'},
              {'word': 'Manila', 'question': 'The capital of the Philippines'},
              {'word': 'Tigris', 'question': 'ِA river in Iraq'},
              {'word': 'S400', 'question': 'Air missile system'}, {'word': 'orang', 'quest': 'what is orang color?'},
              {'word': 'red', 'quest': 'what is appale color?'}, {'word': 'yallow', 'quest': 'what is banana color?'},
              {'word': 'rose', 'quest': 'what is Strawberry color?'},
              {'word': 'green', 'quest': 'what is watermelon color?'},
              {'word': 'black', 'quest': 'what is Grape color?'},
              {'word': 'blue', 'quest': 'what is Cranberries color?'},
              {'word': 'white', 'quest': 'what is fig color?'}, {'word': 'browen', 'quest': 'what is Kiwi color?'},
              {'word': 'songs', 'question': 'which You listen everyday?'},
              {'word': 'nliy', 'question': 'Her most important work is a movie and men.?'},
              {'word': 'pm', 'question': 'night time?'}, {'word': 'gta', 'question': ' still car  game?'},
              {'word': 'china', 'question': 'From Southeast Asian countries?'},
              {'word': 'go', 'question': 'form somewhere?'},
              {'word': 'Sun', 'question': 'the biggest start in our galaxy?'},
              {'word': 'okay', 'question': 'when everything is fain?'},
              {'word': 'left', 'question': 'Which way is anti-clockwise, left or righ?'},
              {'word': 'lgloo', 'question': ' What do you call a house made of ice?'},
              {'word': 'nile', 'question': ' Which is the longest river on the earth?'},
              {'word': 'Japan', 'question': 'Which country is called the land of rising sun?'},
              {'word': 'mars', 'question': ' Which planet is known as the Red Planet?'},
              {'word': 'skin', 'question': ' Which is the most sensitive organ in our body?'},
              {'word': 'India', 'question': " The largest 'Democracy' in the world?"},
              {'word': 'water', 'question': "What makes up (approx.) 80% of our brain's volume?"},
              {'word': 'Ghana', 'question': ' Which African nation is famous for chocolate?'},
              {'word': 'red', 'question': 'What is the top color in a rainbow?'},
              {'word': 'lago', 'question': ' What is the name of the main antagonist in the Shakespeare play Othello '},
              {'word': 'four', 'question': 'How many human players are there on each side in a polo match ?'},
              {'word': 'feb', 'question': ' Which month of the year has the least number of days'},
              {'word': 'sty', 'question': ' Where does a pig live?'},
              {'word': 'nose', 'question': ' We smell with our?'},
              {'word': 'tibet', 'question': ' Which place is known as the roof of the world?'},
              {'word': 'tin', 'question': ' What element is denoted by the chemical symbol Sn in the periodic table?'},
              {'word': 'krone', 'question': ' What is the currency of Denmark?'},
              {'word': 'knee', 'question': ' In which part of your body would you find the cruciate ligament?'},
              {'word': 'east', 'question': ' In which direction does the sun rise ?'},
              {'word': 'Sky', 'question': "something is starting with s 'b'"},
              {'word': 'Sedney', 'question': 'A capital city of Australia'},
              {'word': 'Popup', 'question': 'Alert message'},
              {'word': 'FTP', 'question': 'standard for File Transfer Protocol'},
              {'word': 'Taxes', 'question': 'The position of Dallas'},
              {'word': 'Islam', 'question': 'What your religion'},
              {'word': 'Team', 'question': 'meaning of co-workers'},
              {'word': 'Koyoto', 'question': "The name of Japan anime city 'C'"},
              {'word': 'Dark', 'question': "The opposite of 'light'"},
              {'word': 'songs', 'question': 'which You listen everyday?'},
              {'word': 'lion', 'question': 'who is the king of the jungle?'},
              {'word': 'Oval', 'question': 'Shape of Egg is?'},
              {'word': 'Pluto', 'question': ' It is one of the planets of the solar system?'},
              {'word': 'china', 'question': 'From Southeast Asian countries?'},
              {'word': 'purple', 'question': 'it is mean I trust You?'},
              {'word': 'Sun', 'question': 'the biggest start in our galaxy?'},
              {'word': 'Roma', 'question': 'one of Italia country?'},
              {'word': 'Tokyo', 'question': "Asia's largest city"},
              {'word': 'Nile', 'question': 'The longest river in the world'},
              {'word': 'Whale', 'question': 'The heaviest animal on earth'},
              {'word': 'Asia', 'question': 'Largest continents'},
              {'word': 'London', 'question': 'The city is located the famous Big Ben Watch'},
              {'word': 'Friday', 'question': 'the last day from week?'},
              {'word': 'seven', 'question': 'number of days in week'},
              {'word': 'france', 'question': 'where is effil tower'},
              {'word': 'sanaa', 'question': 'the capital of yemen'},
              {'word': 'Cairo', 'question': 'the capital of Egypt'},
              {'word': 'iraq', 'question': 'Baghdad is a capital of'},
              {'word': 'cars', 'question': 'a taxi is a type of?'},
              {'word': 'Egypt', 'question': " where is The Nile River'"},
              {'word': 'Yemen', 'question': 'where is Socotra Island'},
              {'word': 'Amina', 'question': ' mother of our massenger'},
              {'word': 'Brazil', 'question': 'A country that hosted World Cup in 2014'},
              {'word': 'Cheap', 'question': 'Opposite of expensive'},
              {'word': 'Ready', 'question': 'A word describing a state'},
              {'word': 'Nivada', 'question': 'The state where Las Vegas is located'},
              {'word': 'House', 'question': 'Where you live'},
              {'word': 'Bus', 'question': 'A form of public transportation'},
              {'word': 'Canada', 'question': "A country in South America that starts with the letter 'C'"},
              {'word': 'Need', 'question': 'A word similar to require'},
              {'word': 'Die', 'question': "The opposite of 'live'"},
              {'word': 'CPU', 'question': 'Brain of computer is?'},
              {'word': 'Camel', 'question': 'Which animal has hump on its back?'},
              {'word': 'Oval', 'question': 'Shape of Egg is?'},
              {'word': 'Winter', 'question': ' In which season we wear warm clothes?'},
              {'word': 'Seven', 'question': 'colors are there in a rainbow?'},
              {'word': 'Red', 'question': 'primary color?'},
              {'word': 'Sun', 'question': 'principal source of energy for earth?'},
              {'word': 'Africa', 'question': "continent is known as 'Dark' continent?"},
              {'word': 'Asia', 'question': 'the largest continent in the world?'},
              {'word': 'after', 'question': 'Behind in place or order'},
              {'word': 'draft', 'question': 'A current of air in an enclosed area.'},
              {'word': 'call', 'question': 'To say in a loud voice'}, {'word': 'little', 'question': 'Small in size'},
              {'word': 'option', 'question': 'The act of choosing'},
              {'word': 'signal', 'question': 'A message communicated by such means.'},
              {'word': 'writer', 'question': 'a person engaged in writing books'},
              {'word': 'follow', 'question': 'To come or go after'},
              {'word': 'camera', 'question': ' a hand-held photographic device'},
              {'word': 'detail', 'question': 'An individual part or item'},
              {'word': 'action', 'question': 'process of being active'},
              {'word': 'beauty', 'question': 'One that is beautiful, especially a beautiful woman.'},
              {'word': 'center', 'question': 'A point or place that is equally distant from the sides '},
              {'word': 'detect', 'question': 'To learn something hidden and'},
              {'word': 'orange', 'question': 'Of the color orange.'}, {'word': 'finish', 'question': 'to stop'},
              {'word': 'online', 'question': 'Connected to a central computer or to a computer network'},
              {'word': 'player', 'question': 'A gambler.'}, {'word': 'later', 'question': 'afterwards'},
              {'word': 'dog', 'question': ' A male animal of the family Canidae'},
              {'word': 'Sanaa', 'question': 'The capital of the state of Yemen is?'},
              {'word': 'Athena', 'question': 'the capital of Greece'},
              {'word': 'Cairo', 'question': 'The capital of Egypt'},
              {'word': 'Paris', 'question': 'the capital of France '},
              {'word': 'Ottawa', 'question': "Canada's capital"},
              {'word': 'Beirut', 'question': 'the capital of Lebanon'},
              {'word': 'S400', 'question': 'The capital of Tunisia is:'},
              {'word': 'nine', 'question': 'One of the numbers'}, {'word': 'red', 'question': 'A color'},
              {'word': 'ِdone', 'question': 'We say it when we have finished'}, {'word': 'sad', 'question': 'Feeling'},
              {'word': 'rice', 'question': 'Kind of food'}, {'word': 'suger', 'question': 'ِWhat makes sweets sweety?'},
              {'word': 'salt', 'question': 'Very similer to suger'},
              {'word': 'mark', 'question': 'Who created facebook'},
              {'word': 'bad', 'question': 'The opposite of good'},
              {'word': 'dirty', 'question': 'The opposite of cleen'},
              {'word': 'march', 'question': 'What is third month a year? '},
              {'word': 'cancer', 'question': 'Very dangerous disease? '},
              {'word': 'Mania', 'question': "What is a five-letter word meaning 'insanity'? "},
              {'word': 'Mallet', 'question': "What is a six-letter word meaning 'a wooden hammer'? "},
              {'word': 'clock', 'question': 'Smoething shows the time? '},
              {'word': 'Mantle', 'question': "What is a six-letter word meaning 'a cloak'? "},
              {'word': 'car', 'question': 'Sonmethinge you drive? '},
              {'word': 'Manor',
               'question': "What is a five-letter word meaning 'the landed estate of a lord or nobleman'? "}]


rand_question=[]
our_words=[]
for i in range(12):
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

if search:

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
else:
	s+=1
	first_wor=our_words_len[s]

	search= list(filter(lambda x: x.lower().startswith(first_word[0]), our_words)) 


