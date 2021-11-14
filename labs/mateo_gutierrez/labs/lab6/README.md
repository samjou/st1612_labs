# Lab 6 Streaming Real-time con ElasticSearch-Kibana-LogStash-Kafka

## Desarrollo

## Primera parte (ElasticSearch)

1. Instalar ElasticSearch:

*Nota: Montar sobre una máquina t2.medium en AWS*
```bash
    wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.15.1-linux-x86_64.tar.gz

    tar -xzf elasticsearch-7.15.1-linux-x86_64.tar.gz

    cd elasticsearch-7.15.1
```
1. Iniciar el servidor:
   1. `bin/elasticsearch -d -p pid`
   
2. Terminar el servidor (cuando se deje de usar):
   1. `pkill -F pid`

## Segunda parte (Kibana)

1. Instalar Kibana:

*Nota: Montar sobre una máquina t2.medium en AWS (Preferiblemente la misma de ElasticSearch) y abrir el puerto 5601*
```bash
    curl -O https://artifacts.elastic.co/downloads/kibana/kibana-7.15.1-linux-x86_64.tar.gz

    tar -xzf kibana-7.15.1-linux-x86_64.tar.gz

    cd kibana-7.15.1-linux-x86_64/
```
2. Editar el archivo `config/kibana.yml`:
   1. Buscar la línea `elasticsearch.hosts: ["http://localhost:9200"]` y quitar el comentario.
   2. Buscar la línea `server.port: 5601` y quitar el comentario.
   3. Buscar la línea `server.host: "0.0.0.0"` y quitar el comentario.

3. Ejecutar el servidor de Kibana:
   1. `nohup bin/kibana &`

4. Ingresar a la dirección IP del servidor con el puerto `5601` desde un navegador para verificar la conexión a ElasticSearch

## Tercera parte (Logstash)

1. Instalar Logstash:

*Nota: Montar sobre una máquina t2.medium en AWS (Preferiblemente la misma de ElasticSearch)*
```bash
wget https://artifacts.elastic.co/downloads/logstash/logstash-7.15.1-linux-x86_64.tar.gz

tar -xzf logstash-7.15.1-linux-x86_64.tar.gz

cd logstash-7.15.1

bin/logstash -f etl-TESTfile.conf
```

2. Ejecutar Logstash con Twitter
   1. Descargar el archivo [etl-twitter.conf](https://github.com/st1612eafit/st1612_20212/raw/main/elk/etl-twitter.conf) en la carpeta de LogStash
   2. Modificar el archivo `etl-twitter.conf` con las credenciales personales de Twitter.
   3. (OPCIONAL) Se puede modificar el nombre que llega a ElasticSearch modificando el index dentro del mismo archivo.
   4. Ejecutar LogStash usando el comando `bin/logstash -f etl-twitter.conf`
3. En Kibana buscar la letra "D" en la parte superior izquierda y allí bajo la opción `Data` seleccionar `Index Management` con esto se confirma que Twitter está conectado correctamente y envíando datos a Kibana.
   1. En la opción `Kibana` seleccionar `Index Patterns` y en el botón `Create index pattern`
   2. En el campo `Name` buscar el nombre que se le dio a los datos de Twitter.
   3. Crear el index
   4. Para visualizar los datos se debe ir al menú de Kibana y seleccionar `Discover`
   
   Se debería ver algo así: ![Datos Kibana](../evidences/lab6/Evidence%201.png)

## Cuarta parte (Beats)

1. Instalar metric beat
   1. ```bash
       wget https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-7.15.1-linux-x86_64.tar.gz

       tar -xvf metricbeat-7.15.1-linux-x86_64.tar.gz

       cd metricbeat-7.15.1-linux-x86_64
       ```
   2. `sudo chown root metricbeat.yml`
   3. `sudo chown root modules.d/system.yml`
   4. `sudo ./metricbeat -e -c metricbeat.yml`
2. En Kibana buscar la letra "D" en la parte superior izquierda y allí bajo la opción `Data` seleccionar `Index Management` con esto se confirma que se están envíando datos de la máquina a Kibana.
   1. En la opción `Kibana` seleccionar `Index Patterns` y en el botón `Create index pattern`
   2. En el campo `Name` buscar el nombre `metricbeat-*`
   3. Crear el index
   4. Para visualizar los datos se debe ir al menú de Kibana y seleccionar `Discover`
   
   Se debería ver algo así: ![Datos Kibana](../evidences/lab6/Evidence%202.png)

Con esto se da por terminado el laboratorio 6