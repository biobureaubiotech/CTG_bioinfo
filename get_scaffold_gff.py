import os

file_name = input("Qual o arquivo GFF?")
##file_name = "lfortunei_genome.gff"
contig = input("Qual o ID do gene?")

curr_path = os.getcwd()
file_path = "".join((curr_path,r'/',file_name))
file2_path = "".join((curr_path,r'/scaffold_',contig,".gff"))
print(file_path)

file = open(file_path, "r")
file2 = open(file2_path, "w")
             
for line in file:
    if ("".join(("itr6_", contig, "_"))) in line:
        file2.write(line)
        
file2.flush()
