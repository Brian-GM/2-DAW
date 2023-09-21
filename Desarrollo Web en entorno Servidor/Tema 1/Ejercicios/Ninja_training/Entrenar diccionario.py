#data: list[float] = [3.65, 34.8, 2.8 ,68.0 ,4.1]

#max: float = data[0]
#min: float = data[0]
#sum: float = 0.0

#for n in data:
#   if n > max:
#        max = n
#    if n < min:
#        min = n 
#    sum += n
#print(max)
#print(min)  
#print(sum/len(data))

from collections import namedtuple

Dog = namedtuple("Dog", ["name","breed","color"])
bobby: Dog = Dog("Booby", "Pastor", "Brown")
data: list[Dog] = [
    Dog("Otto","Labrador","White"),    
    Dog("Oriol","Chuhuahua","Black"),
    Dog("Pepe","Pitbull","White"),
    Dog("Pepa","Pitbull","Black")
]
for dog in data:
     if dog.color.lower() == "black":
         print(dog.name)

for name,raza,color in data: 
    if color == "Black":
        print(name)

games: list[dict[str, str]] = [

{
    "team1":"A",
    "team2":"B",
    "result":"1-0"
},

{
   "team1":"C",
    "team2":"D",
    "result":"1-1"  
},

{
   "team1":"E",
    "team2":"F",
    "result":"2-3"  
}
]

for p in games:
    print(f" {p['team1']} vs {p['team2']}:{p['result']} ")



txt: str = input("Escriba una palabra: ")
for c in txt:
    print(c)
    