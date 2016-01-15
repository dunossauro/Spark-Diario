# Configuração

Para que o Spark Reconheça um cluster Hadoop já em funcionamento, você deve adicionar a linha a baixo ao arquivo `spark/conf/spark-env.sh.template`:
  
  `HADOOP_CONF_DIR=<Caminho do seu /etc/hadoop>`
  
  Caso você tenha seguido os passos da instalação do [Hadoop Diario](https://github.com/z4r4tu5tr4/Hadoop-diario) o seu diretório se encontrará em  `/usr/local/hadoop/etc/hadoop/`
  
  o que resultará em:
  
  `HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/`
