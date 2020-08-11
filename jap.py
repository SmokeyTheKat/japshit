import sys
import pyperclip

inp = ""
sa = sys.argv
if len(sys.argv) > 1:
	for i in range(len(sa)):
		if i > 0:
			inp += sa[i] + " "
else:
	inp = input("TO CONVERT: ")

inp = inp.lower()

japchar = []

with open("/usr/share/japshit/japchars.txt", "r") as f:
		japchar = [line.split(" ")[1].replace('\n', "").replace("\r", "") for line in f]


conv = {}
conv["a"] = japchar[0] 
conv["b"] = japchar[1] 
conv["c"] = japchar[2] 
conv["d"] = japchar[3] 
conv["e"] = japchar[4] 
conv["f"] = japchar[5] 
conv["g"] = japchar[6] 
conv["h"] = japchar[7] 
conv["i"] = japchar[8] 
conv["j"] = japchar[8] 
conv["k"] = japchar[10] 
conv["l"] = japchar[11] 
conv["m"] = japchar[12] 
conv["n"] = japchar[13] 
conv["o"] = japchar[14] 
conv["p"] = japchar[15] 
conv["q"] = japchar[16] 
conv["r"] = japchar[17] 
conv["s"] = japchar[18] 
conv["t"] = japchar[19] 
conv["u"] = japchar[20] 
conv["v"] = japchar[21] 
conv["w"] = japchar[22] 
conv["x"] = japchar[23] 
conv["y"] = japchar[24] 
conv["z"] = japchar[25] 
conv[" "] = "    "
conv["'"] = "'"
conv["."] = "."
conv["\""] = "\""
conv["’"] = "’"
conv[","] = ","

conv["!"] = "!"
conv["@"] = "@"
conv["#"] = "#"
conv["$"] = "$"
conv["%"] = "%"
conv["^"] = "^"
conv["&"] = "&"
conv["*"] = "*"
conv["("] = "("
conv[")"] = ")"
conv["_"] = "_"
conv["-"] = "-"
conv["+"] = "+"
conv["="] = "="
conv["`"] = "`"
conv["~"] = "~"
conv["<"] = "<"
conv[">"] = ">"
conv["/"] = "/"
conv["\\"] = "\\"
conv["["] = "]"
conv["]"] = "]"
conv["{"] = "{"
conv["}"] = "}"
conv["|"] = "|"

outt = ""

for c in inp:
	outt += conv[c]

print(outt)
pyperclip.copy(outt)
print("HAS BEEN COPYED TO CLIP BOARD YO")
