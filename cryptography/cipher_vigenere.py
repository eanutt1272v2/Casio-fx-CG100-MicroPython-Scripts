from matplotlib.pyplot import bar, axis, text, show, grid

def vigenere(text, key, decode=False):
    key=key.upper(); result=""; ki=0
    for ch in text.upper():
        if ch.isalpha():
            shift=ord(key[ki%len(key)])-65
            if decode: shift=-shift
            result+=chr((ord(ch)-65+shift)%26+65)
            ki+=1
        else:
            result+=ch
    return result

def freq_analysis(text):
    text=text.upper()
    counts=[text.count(chr(65+i)) for i in range(26)]
    total=sum(counts); freqs=[c/total*100 if total else 0 for c in counts]
    return freqs

def index_of_coincidence(text):
    text=''.join(c for c in text.upper() if c.isalpha())
    n=len(text)
    if n<2: return 0
    counts=[text.count(chr(65+i)) for i in range(26)]
    return sum(c*(c-1) for c in counts)/(n*(n-1))

while True:
    print("1=Encode  2=Decode  3=Freq analysis  4=Index of coincidence  0=quit")
    m=input("> ")
    if m=="0": break
    if m in("1","2"):
        txt=input("Text: "); key=input("Key: ")
        out=vigenere(txt,key,decode=(m=="2"))
        print("Result:",out)
    elif m=="3":
        txt=input("Ciphertext: ")
        freqs=freq_analysis(txt)
        letters=[chr(65+i) for i in range(26)]
        xs=list(range(26))
        bar(xs,freqs,"blue")
        axis([-1,26,0,max(freqs)*1.2]); grid("on")
        text(0,max(freqs),"Letter frequencies (%)")
        show()


        pairs = []
        for idx in range(26):
            pairs.append((freqs[idx], letters[idx]))
        for a in range(len(pairs)):
            for b in range(a+1, len(pairs)):
                if pairs[b][0] > pairs[a][0]:
                    pairs[a], pairs[b] = pairs[b], pairs[a]
        top = pairs[:5]
        print("Top 5:", [(top[i][1], round(top[i][0],1)) for i in range(5)])
        print("English IC~0.065. Random~0.038")
    elif m=="4":
        txt=input("Ciphertext: ")
        ic=index_of_coincidence(txt)
        print("IC =",round(ic,5))
        print("English IC ~ 0.0650")
        print("Random IC  ~ 0.0385")
        print("Likely key length estimate:")

        for kl in range(1,15):
            sub=''.join(txt[i] for i in range(0,len(txt),kl) if txt[i].isalpha())
            ic_sub=index_of_coincidence(sub)
            if ic_sub>0.055:
                print("  Key length",kl,"IC=",round(ic_sub,4),"<-- likely")
                break
    input("EXE")

input("\nPress any key to exit: ")

