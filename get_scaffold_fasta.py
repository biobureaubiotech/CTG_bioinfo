import os

file_name = input("Qual o nome do arquivo do genoma?")
contig = input("Qual o número do contig?")

curr_path = os.getcwd()
file_path = "".join((curr_path,r'/',file_name))
file2_path = "".join((curr_path,r'/scaffold_',contig,".fasta"))
print(file_path)

boleana = False

file = open(file_path, "r")
file2 = open(file2_path, "w")
             
for line in file:
    if '>' in line:
        boleana = False
    if "".join(("itr6_",contig)) in line:
        boleana = True
    if boleana:
        file2.write(line)
    
