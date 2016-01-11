#### Jupyter + python3 + pySpark

Para iniciar o Pyspark usando o terminal do python3 em conjunto ao jupyter, você deve rodar o seguinte comando:

`PYSPARK_PYTHON=python3 PYSPARK_DRIVER_PYTHON=ipython PYSPARK_DRIVER_PYTHON_OPTS="notebook --browser=firefox"\
/usr/local/spark/bin/pyspark`
