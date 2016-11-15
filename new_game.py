from random import *
def game():
    movie_list = ['terminator','cars','madagascar','avengers','superman' ,'interstellar','inception','hulk','frozen','twilight','dracula','wanted','cinderella','tangled','hancock','titanic','ratatouille','transformers','thor','taken','avatar','jumanji']
    w = movie_list[randint(0,len(movie_list)-1)]
    word = list(w)
    new1 = ''
    for k in range(len(w)):
        new1 += '_'
    new = list(new1)
    chances = len(w) - 1
    j = chances
    print ('guess the word : ' +  ' '.join(new))
    while j != 0:
        print('chances left :' + str(j))
        print('enter a letter')
        l = input()
        c = 0
        for i in range(len(w)):
            if l == word[i]:
                new[i] = l
                c = 1
        print(' '.join(new))
        if l == ' ':
            c =1
            print('please do not enter space')
        if c == 0:
            j = j-1
        if new == word:
            print('congrats you guessed the word ' + ''.join(word))
            break
            
        if j == 0:
            print('out of chances Sorry word is ' + w)
            break
        
                
    
        
def main():
    game()
if __name__ == '__main__':
    main()
