# coding: utf-8

# ---------------------- Código MapReduceLib
#Imports da MapReduceLib
from map_reduce_lib import hadoop as h
from map_reduce_lib import hdfs as dfs

hadoop = h()
hdfs = dfs()
hadoop.dfs_start() #inicia o HDFS

hdfs.put("/home/eduardo/Dropbox/Programando/Python/Hadoop/Projetos/Linguistica/arquivos/s_1000000.txt",
        "/contador/input")
# ---------------------- biLecudeRpaM ogidpóC

# ---------------------- Código Spark
noticias = sc.textFile("/contador/input/s_1000000.txt") #Carrega o arquivo do HDFS para o RDD

resposta = noticias.map(lambda x: x.replace(',',' , ').replace('.',' . ')\
                        .replace('-',' - ').replace("!"," ! ")\
                        .replace("?"," ? ").replace("\""," \" ")\
                        .replace(")"," ) ").replace("("," ) ")\
                        .replace("..."," ... ").replace(":"," : ")\
                        .replace(";"," ; ").replace("“", " “ ")\
                        .replace("”"," ” ").replace("'"," ' ")\
                        .lower()).flatMap(lambda line: line.split())\
                        .map(lambda word: (word, 1))\
                        .reduceByKey(lambda x,y:x+y)\
                        .sortByKey()\
                        .map(lambda x: str("%s\t\t%s")%(x[0],x[1]))

hdfs.rm_dir("/contador/output") #Remove o dir output, caso ele exista

resposta.saveAsTextFile("/contador/output") #Retorna do RDD para o HDFS

# ---------------------- krapS ogidpóC

hdfs.get("/contador/output") #Retira o arquivo do HDFS e insere no sistema local
