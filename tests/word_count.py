# coding: utf-8

# ---------------------- Código MapReduceLib
#Imports da MapReduceLib
from map_reduce_lib import hadoop as h
from map_reduce_lib import hdfs as dfs

hadoop = h()
hdfs = dfs()

hadoop.start_all() #inicia todo o cluster Hadoop

hdfs.mkdir("/contador")
hdfs.mkdir("/contador/input")
hdfs.put("/home/eduardo/Dropbox/Programando/Python/spark/noticias.txt",
        "/contador/input") #Insere o arquivo noticias.txt no HDFS

# ---------------------- biLecudeRpaM ogidpóC

# ---------------------- Código Spark
noticias = sc.textFile("/contador/input/noticias.txt") #Carrega o arquivo do HDFS para o RDD

resposta = noticias.flatMap(lambda line: line.split(" "))\
                        .map(lambda word: (word, 1))\
                        .reduceByKey(lambda a, b: a + b) #Executa as operações de MapReduce

resposta.saveAsTextFile("/contador/output") #Retorna do RDD para o HDFS

# ---------------------- krapS ogidpóC

hdfs.get("/contador/output") #Retira o arquivo do HDFS e insere no sistema local
