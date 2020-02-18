class T(object):
    def __init__ (self,text):
        self.text =text
    def __str__ (self):
        return 'word!'
    def __len__(self):
        return len(self.text)
    def __eq__ (self,word):
        return self.text == word.text

a = T('yong')
b = T('yong')

print(a)
print(len(a))
print(a==b) # 신기하네...