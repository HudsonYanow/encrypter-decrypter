import copy

deencrypter = {
    "b":"a",
    "c":"b",
    "d":"c",
    "e":"d",
    "f":"e",
    "g":"f",
    "h":"g",
    "i":"h",
    "j":"i",
    "k":"j",
    "l":"k",
    "m":"l",
    "n":"m",
    "o":"n",
    "p":"o",
    "q":"p",
    "r":"q",
    "s":"r",
    "t":"s",
    "u":"t",
    "v":"u",
    "w":"v",
    "x":"w",
    "y":"x",
    "z":"y",
    "a":"z",
    " ":" "
}

encrypter = {
    "a":"b",
    "b":"c",
    "c":"d",
    "d":"e",
    "e":"f",
    "f":"g",
    "g":"h",
    "h":"i",
    "i":"j",
    "j":"k",
    "k":"l",
    "l":"m",
    "m":"n",
    "n":"o",
    "o":"p",
    "p":"q",
    "q":"r",
    "r":"s",
    "s":"t",
    "t":"u",
    "u":"V",
    "v":"w",
    "w":"x",
    "x":"y",
    "y":"z",
    "z":"a",
    " ":" "
}
def encrypt(string, encrypter):
    newstring=[]
    sc=""
    sc = copy.copy(string)
    for char in sc:
        if char in encrypter:
            newstring.append(encrypter[char])
    return str(newstring)
def reverse(string):
    # slen=len(string)
    # for range(slen) in
    return string[::-1]

f="uwu"
strr=encrypt(f,encrypter)
print(strr)
reverse(f)