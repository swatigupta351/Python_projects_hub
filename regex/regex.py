import re  # regex is a pattern who search the things in the text
# # result = re.search("cat", "I have a cat")  # search cat 
# # print(result) # show object with start and end index of cat
# # print(result.group()) # group() method se hum matched text ko dekh sakte hai only matched text screen pr hota h and or koi span ye vo show nhi hota, agar match nahi mila to error aayega
# # result = re.search("dog" , "I have a cat")
# # print(result)
# # # print(result.group()) # show error none pr group nhi hota h 

# # text  = " Hii , I love my country India. It is a beatiful place"
# # print(re.search("Hii" , text))
# # print(re.search("python", text))
# # print(re.search("country", text))
# # print(re.search("place", text))
# # print(re.search("java", text))


# # # . matlab "koi bhi ek character"
# # # .. mtlb koi 2 character bich m 

# # print(re.search("c.t", "I have a cat")) # cat match hoga
# # print(re.search("c.t", "I have a cot")) # cot match hoga
# # print(re.search("c.t", "I have a cut")) # cut match hoga
# # print(re.search("c.t", "I have a ct")) # match nhi hoga,kunky bich me koi character nhi h
# # print(re.search("c.t", "I have a cct")) # match hoga 
# # print(re.search("c.t", "I have a c-t")) # match hoga, kyunki - bhi ek character hai
# # print(re.search("c.t", "I have a c t")) # match hoga, kyunki space bhi ek character hai
# # print(re.search("c.t", "I have a c\nt")) # match nhi hoga new line nhi h 
# # print(re.search("h.t", "heat")) # match nhi hoga 2 character bich m  h 

# # . ek character
# # .* matlab "koi bhi character, kitni bhi baar"
# # * hamesha uske pehle wale character pe apply hota hai!
# print(re.search("ca*t", "ct"))      # ✅ — 0 'a'
# print(re.search("ca*t", "cat"))     # ✅ — 1 'a'
# print(re.search("ca*t", "caat"))    # ✅ — 2 'a'
# print(re.search("ca*t", "caaaat"))  # ✅ — 4 'a'

# # .  = koi bhi character
# # *  = kitni bhi baar

# # .*  = koi bhi character, kitni bhi baar

# print(re.search("h.*t", "hat"))         # ✅
# print(re.search("h.*t", "heat"))        # ✅
# print(re.search("h.*t", "he123@#$t"))  # ✅ — kuch bhi beech me ho!

# # + — 1 ya zyada baar
# # * = 0 ya zyada (bina character ke bhi chalta)
# # + = 1 ya zyada (kam se kam ek toh hona chahiye!)

# # print(re.search("ca+t", "ct"))      # ❌ — 0 'a' — nahi chalega!
# # print(re.search("ca+t", "cat"))     # ✅ — 1 'a'
# # print(re.search("ca+t", "caat"))    # ✅ — 2 'a'
# # print(re.search("ca+t", "caaaat"))  # ✅ — 4 'a'


# # # ? — 0 ya 1 baar (Optional!)
# # # ? matlab — "ho toh bhi chalta, na ho toh bhi chalta"
# # # ? ka matlab — ek se zyada nahi!
# # print(re.search("ca?t", "ct"))    # ✅ — 0 'a' — chalta hai
# # print(re.search("ca?t", "cat"))   # ✅ — 1 'a' — chalta hai
# # print(re.search("ca?t", "caat"))  # ❌ — 2 'a' — nahi chalega!


# # *  →  0 ya zyada   →  ct, cat, caat, caaaat  ✅
# # +  →  1 ya zyada   →  cat, caat, caaaat       ✅  (ct ❌)
# # ?  →  0 ya 1       →  ct, cat                 ✅  (caat ❌)


# # example 

# # Sahi example
# print(re.search("colou?r", "color"))    # ✅ — 'u' optional hai
# print(re.search("colou?r", "colour"))   # ✅ — 'u' hai toh bhi chalta
# #                     ↑
# #                'u' pe ? laga hai

# # ^ — Line ki shuruaat
# print(re.search("^Hello" , "Hello World")) # match 
# print(re.search("^World" , "Hello World")) # None


# # $ — Line ka end
# print(re.search("World$", "Hello World")) # Match 
# print(re.search("Hello$", "Hello World")) # None

# #  ^ aur $ saath matlab — poori string exactly yahi honi chahiye

# print(re.search("^Hello$" , "Hello")) # match 
# print(re.search("^Hello$", "Hello World")) # None

# [] (Character Class) — ye ek set hota hai!
# [] — In me se koi ek character
# print(re.search("[abc]", "apple") ) # a match 
# print(re.search("[abc]", "ball")) # b match 
# print(re.search("[abc]", "owl")) # no match (None)

# # can be use range 
# # [a-z]   # koi bhi lowercase letter
# # [A-Z]   # koi bhi uppercase letter
# # [0-9]   # koi bhi digit
# # [a-zA-Z] # koi bhi letter

# # \ (Backslash) — Special characters ko escape karna!
# # Problem — Kuch characters ka special matlab hota hai:
# # $ ka matlab hota hai "line ka end"
# # agar hume literal $ dhundhna ho toh?
# print(re.search("$" , "price $50")) # no match bcs line ki end search krega 
# print(re.search("\$" , "price $50" )) # ✅ — literal $ dhundh raha hai match 

# Commonly escaped characters:
# \.   →  literal dot        (warna . = koi bhi character)
# \$   →  literal $          (warna $ = line end)
# \^   →  literal ^          (warna ^ = line start)
# \[   →  literal [          (warna [ = class start)
# \]   →  literal ]          (warna ] = class end)
# \?   →  literal ?          (warna ? = optional)
# \+   →  literal +          (warna + = 1 ya zyada)
# \*   →  literal *          (warna * = 0 ya zyada)


#  \s, \d, \w — Shorthand Classes!
# \d — Digit (0-9)
# \d = [0-9] ka shortcut
# print(re.search("\d", "mera number 5 hai"))  # ✅ — '5' mila
# print(re.search("\d", "koi number nahi"))     # ❌

# \s — Space/Tab/Newline
# \s = koi bhi whitespace
# print(re.search("\s", "hello world"))  # ✅ — space mila
# print(re.search("\s", "helloworld"))   # ❌ — koi space nahi

# # \w — Word Character (a-z, A-Z, 0-9, _)

# # \w = letter ya digit ya underscore
# print(re.search("\w", "hello"))   # ✅
# print(re.search("\w", "123"))     # ✅
# print(re.search("\w", "!@#"))     # ❌ — koi word character nahi

# # Capital letters — Ulta kaam karte hain!

# # # \D  →  digit NAHI   →  [^0-9]
# # # \S  →  space NAHI   →  [^ \t\n]
# # # \W  →  word NAHI    →  [^a-zA-Z0-9_]

# # print(re.search("\D", "abc"))   # ✅ — 'a' digit nahi hai
# # print(re.search("\D", "123"))   # ❌ — sab digit hain


# print(re.search("\d", "age 25"))     # match 
# print(re.search("\D", "123"))        # no match 
# print(re.search("\s", "hello"))      # no match
# print(re.search("\w", "!@#$"))       # no match
# print(re.search("\W", "hello"))      # match 
# print(re.search("\S", "hello"))      # match

# # .group():
# result = re.search("(cat)(dog)", "catdog")
# print(result.group(0))  # catdog — poora match
# print(result.group(1))  # cat    — pehla group
# print(result.group(2))  # dog    — doosra group

# # example 
# # Date me se din, mahina, saal alag nikalo
# result = re.search("(\d+)-(\d+)-(\d+)", "2024-05-11")

# print(result.group(0))  # 2024-05-11 — poora
# print(result.group(1))  # 2024       — saal
# print(result.group(2))  # 05         — mahina
# print(result.group(3))  # 11         — din

# #\d  →  ek digit
# # \d+ →  ek ya zyada digits

# # OR | — Ya toh ye, ya woh

# # cat ya dog dhundho
# print(re.search("cat|dog", "I have a cat"))  # ✅ — cat mila
# print(re.search("cat|dog", "I have a dog"))  # ✅ — dog mila
# print(re.search("cat|dog", "I have a fish")) # ❌ — koi nahi mila

# re.sub() — Pattern dhundho aur replace karo
# re.sub(pattern, replacement, text)
text = "My number is 12345"
result = re.sub("\d" , '*' , text)
print(result)

# re.sub(pattern, replace_se, kahan)
# #         ↑          ↑         ↑
# #      kya dhundho  kisse     kahan
# #                  badlo

# example 
# Saari digits hatao
print(re.sub("\d", "", "hello 123 world"))  # "hello  world"

# Saare spaces hatao  
print(re.sub("\s", "", "hello world"))       # "helloworld"

# Ek word badlo
print(re.sub("cat", "dog", "I have a cat")) # "I have a dog"


 # Ab re.compile() — Pattern save karna!

# Pattern ek baar save karo
pattern = re.compile("\d+")

# Ab seedha use karo
print(pattern.search("age 25"))    # ✅
print(pattern.search("hello"))     # ❌
print(pattern.sub("X", "a1b2c3")) # aXbXcX

# \d    →  0-9 koi bhi digit
# \w    →  a-z, A-Z, 0-9, _
# \s    →  space, tab
# \x1b  →  ESC (hidden terminal character)
# \x07  →  BEL (hidden terminal character)