wow = [ 'lee' ,'Yong','hoon']

def change_words(words,func):
     for word in words:
         print(func(word))

def sample_func(word):
    return word.capitalize()

change_words(wow,sample_func)

#들여쓰기 잘하자 ; 바로 오류 뜨네 ;
