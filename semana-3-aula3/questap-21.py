frase = input('Digite uma frase')
letra = input('Digite uma letra')
count_er=0
start_index=0
for i in range(len(frase)):
j = frase.find(letra,start_index)
if(j!=-1):
	start_index = j+1
	count_er+=1
print("Total occurrences are: ", count_er)
