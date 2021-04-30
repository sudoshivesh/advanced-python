class String:

    def __init__(self):
        self.vowels=0
        self.consonants=0
        self.spaces=0
        self.uppercase=0
        self.lowercase=0
        self.string=str(input("Enter a String: "))

    def count_vowels(self):
        for i in self.string:
            if i in ('a','e','i','o','u','A','E','I','O','U'):
                self.vowels+=1


    def count_consonants(self):
        for i in self.string:
            if i not in ('a','e','i','o','u','A','E','I','O','U',' '):
                self.consonants+=1

    def count_uppercase(self):
        for i in self.string:
            if i.isupper():
                self.uppercase+=1

    def count_lowercase(self):
        for i in self.string:
            if i.islower():
                self.lowercase+=1

    def count_spaces(self):
        for i in self.string:
            if i==' ':
                self.spaces+=1

    def compute(self):
        self.count_vowels()
        self.count_consonants()
        self.count_spaces()
        self.count_uppercase()
        self.count_lowercase()
        
    def display(self):
        print('Vowels=',self.vowels)
        print('Consonants=',self.consonants)
        print('Spaces=',self.spaces)
        print('Uppercase=',self.uppercase)
        print('Lowercase=',self.lowercase)
s=String()
s.compute()
s.display()
        
        
