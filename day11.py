#STRING METHODS
#indexing
#text="GOOD MORNING"
#index-01234567891011
      #-11-10-9-8-7-6-5-4-3-2-1


#slicing
text="GOOD MORNING"
print(text[3])#D
print(text[1:8])#OOD MOR
print(text[::-1])#GNINROM DOOG
print(text[-1])#G




#STRING METHODS

#str.capitalize()
x="codeme"
print(x.capitalize())#Codeme

#str.upper()
x="helloworld"
print(x.upper())#HELLOWORLD

x="HELLOWORLD"
print(x.lower())#helloworld

#str.swapcase
x="HeLLoWorlD"
print(x.swapcase())#hEllOwORLd


#str.count()
x="this is a text and this is another text"
print(x.count("text"))#2
print(x.count("text",0,15))#1

#str.find()
x="this is a text and this is another text"
print(x.find("text"))#10
print(x.find("text",15))#35


#str.split() (default is space)

string="one two three four five"
#print(string)#one two three four five
#print(string.split())#['one', 'two', 'three', 'four', 'five']

x=string.split()#['one', 'two', 'three', 'four', 'five']
x.append("six")#['one', 'two', 'three', 'four', 'five', 'six']
print(x)


#str.join() #seperator.join(list)

string="one two three four five"
print(string)#one two three four five
print(string.split())#['one', 'two', 'three', 'four', 'five']
x=string.split()#['one', 'two', 'three', 'four', 'five']
x.append("six")
print(x)#['one', 'two', 'three', 'four', 'five', 'six']

string="".join(x)
print(string)#onetwothreefourfivesix

string=" ".join(x)
print(string)#one two three four five six



string="one$two$three$four$five"
print(string)#one$two$three$four$five

print(string.split("$"))#['one', 'two', 'three', 'four', 'five']

string="one$two$three$four$five"
print(string)#one$two$three$four$five

print(string.split("t"))#['one$', 'wo$', 'hree$four$five']

x=string.split("$")
x.insert(2,"six")
print(x)#['one', 'two', 'six', 'three', 'four', 'five']

x.append("seven")#['one', 'two', 'six', 'three', 'four', 'five', 'seven']
print(x)

sep="$"
string=sep.join(x)
print(string)#one$two$six$three$four$five$seven


string="$".join(x)
print(string)#one$two$six$three$four$five$seven

string="".join(x)
print(string)#onetwosixthreefourfiveseven

string=" ".join(x)
print(string)#one two six three four five seven

string="d".join(x)
print(string)#onedtwodsixdthreedfourdfivedseven

string=" d "
print(string)#one d two d six d three d four d five d seven




poem="""Twinkle, twinkle, little star,
How I wonder what you are.
Up above the world so high,
Like a diamond in the sky."""
x=poem.split('\n')
x.append("edited by codeme")
poem='\n'.join(x)
print(poem)
#o/p:
#Twinkle, twinkle, little star,
#How I wonder what you are.
#Up above the world so high,
#Like a diamond in the sky.
#edited by codeme



poem="""Twinkle, twinkle, little star,
How I wonder what you are.
Up above the world so high,
Like a diamond in the sky."""
x=poem.split('\n')
x.append("        -written by author name")
poem='\n'.join(x)
print(poem)
#o/p
#Twinkle, twinkle, little star,
#How I wonder what you are.
#Up above the world so high,
#Like a diamond in the sky.
#       -written by author name


poem="""Twinkle, twinkle, little star,
How I wonder what you are.
Up above the world so high,
Like a diamond in the sky."""
x=poem.splitlines()
x.append("edited by codeme")
poem="\n".join(x)
print(poem)

#o/p

#Twinkle, twinkle, little star,
#How I wonder what you are.
#Up above the world so high,
#Like a diamond in the sky.
#edited by codeme





#str.replace()
sample="this is a string,string,string"
print(sample.replace("string","text"))#this is a text,text,text
print(sample.replace("string","text",1))#this is a text,string,string


#str.strip()
sample='#####hello####'
print(sample.strip('#'))hello

#str.lstrip()
print(sample.lstrip('#'))hello####

#str.rstrip()
print(sample.rstrip('#'))#####hello





