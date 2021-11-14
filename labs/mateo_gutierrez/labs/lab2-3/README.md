# LAB 2/3 – Despliegue de una solución Hadoop/Spark en AWS EMR (procesamiento) + S3 (datalake)


## Objetivo General:
Diseñar e implementar un ecosistema de almacenamiento y procesamiento de datos relacionados con el Covid-19 en Colombia y el mundo (contagios y vacunación). Para esto debe diseñar e implementar un datalake para almacenar los datos, debe catalogarlos (con glue), debe poderlos consultar con SQL (Athena y Hive) y hacer un análisis exploratorio de datos con spark (jupyter/pyspark). Para esto mínimo utilizará los servicios de cluster EMR, de almacenamiento S3, de catalogación Glue y de consulta SQL con Athena.

## Desarrollo:

1. Descargar los datos de trabajo en formato CSV desde: [Casos positivos Covid-19 Colombia](https://www.datos.gov.co/Salud-y-Protecci-n-Social/Casos-positivos-de-COVID-19-en-Colombia/gt2j-8ykr/data) los datos se ven así: ![Datos Covid 19](../evidences/lab2-3/Evidence%201%20-%20lab%202-3.png)

2. Crear un bucket S3 con el nombre que se desee y dentro de este crear las carpetas `raw`. `refined` y `trusted`, una vez se tengan estas carpetas subir los datos crudos en formato CSV en la carpeta `raw` de tal forma que se vean así: ![Datos cargados en S3](../evidences/lab2-3/Evidence%202%20-%20lab2-3.png)

3. Crear un crawler en AWS Glue, con esto se relizará el procesamiento de los datos en la carpeta `raw` y estos serán procesados en una tabla que luego será procesada por Athena, el crawler y los datos se deberían ver así: ![Crawler y datos AWS Glue](../evidences/lab2-3/Evidence%203%20-%20lab%202-3.png)

4. En el servicio AWS Athena se realizará todo el proceso de análisis de datos, para esto se comienza explorando el `Query editor` una vez allí se selecciona `AWSDataCatalog` en la opción llamada `Data Source` y en la opción `Database` se selecciona la base de datos creada por AWS Glue. Para realizar una consulta se deben usar sentencias SQL en el editor que se encuentra en la izquierda, para este caso vamos a usar la sentencia: `SELECT * FROM "default"."raw" limit 10;` para visualizar los primeros 10 datos de la tabla. Se debería de ver así: ![Tabla AWS Athena](../evidences/lab2-3/Evidence%204%20-%20lab%202-3.png)

5. Crear un cluster EMR, con la siguientes configuraciones, todo esto será usado para realizar el proceso de transformación de los datos. 
   1. ![Primera configuración cluster EMR](../evidences/lab2-3/Evidence%205.0%20-%20lab%202-3.png)
   2. ![Segunda configuración cluster EMR](../evidences/lab2-3/Evidence%205.1%20-%20lab%202-3.png)
   3. ![Tercera configuración cluster EMR](../evidences/lab2-3/Evidence%205.3%20-%20lab%202-3.png)

6. Una vez el cluster fue creado se puede acceder a la dirección que nos da AWS en los puertos `8888` Hue, `9443` JupyterHub y `8890` Zeppelin lo cual se vería así:
   1. Tranformaciones de datos en Jupyter:
        ![Jupyter](../evidences/lab2-3/Evidence%206.0%20-%20lab%202-3.png)
   2. Tranformaciones de datos en Hive:
        ![Hive](../evidences/lab2-3/Evidence%206.1%20-%20lab%202-3.png)

Con esto se dar por finalizado el laboratorio 2-3.