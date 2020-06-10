def pig(text):
        return ' '.join([word[1:]+word[0]+'AY' if word.isupper() else word[1:]+word[0]+'ay' for word in text.split()])
    
print(pig('I SLEPT MOST OF THE NIGHT'))
print(pig('I SLEPT MOST OF THE night'))