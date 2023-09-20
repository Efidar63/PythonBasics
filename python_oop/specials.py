# myList=[1,2,3]
# myString='my String'

# print(len(myList))
# print(len(myString))
# print(type(myList))
# print(type(myString))

class Movie:
    def __init__(self, title, director, duration):
        self.title=title
        self.director=director
        self.duration=duration
        print('movie object created')

    def __str__(self):
        return f"{self.title} by {self.director}"
    def __len__(self):
        return self.duration
    def __del__(self):
        print('film object deleted')

m=Movie('film name ', 'director name ', 120)

print(str(m))
print(len(m))