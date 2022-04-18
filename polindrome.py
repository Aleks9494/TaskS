
def Palindrome (word):
    word_new=word
    for c in word:
        if c in '!@#$%^&*(),.? ':
            word_new = word_new.replace(c, '')
    flag = True
    for i in range (len(word_new)):
        if word_new[i].lower() == word_new[-i-1].lower():
            continue
        else:
            flag = False
            break
    if flag:
        print (f"{word} является палиндромом!")
    else:
        print (f"{word} не является палиндромом!")


Palindrome(input())