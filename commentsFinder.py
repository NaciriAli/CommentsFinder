### NaciriAli ###
#CommentsFinder 
#still in process
lang = ["c","cplusplus","python","html","css"]
c = ["//","/*"]
cplusplus = ["//","/*"]
python = ["#",'"""']
html = ["<!--","<comment>"]
css = ["/*"]
print("Supported languages: ",' -- '.join(lang))
langchoisi = input("Entrer le language choisi : ")
f = lang.index(langchoisi.lower())
if f == 0:
	var = c
if f == 1:
	var = cplusplus
elif f == 2:
	var = python
elif f == 3:
	var = html
elif f == 4:
	var = css		
file = open(r"c:/Users/lenovo/Desktop/text.txt","r")
texto = file.read().split('\n')
indexes = []
#for elem in texto:
for i, elem in enumerate(texto,1):
	for symb in var:
		if symb in elem :
			indexes.append(str(i)+' - ' +elem)
print(indexes)
#for i, line in enumerate(texto, 1)


