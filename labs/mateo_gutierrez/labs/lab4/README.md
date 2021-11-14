# Lab 4 - Amazon MFSK y Apache Kafka

## Desarrollo:

1. Crear una máquina linux EC2
   1. Instalar java y Kafka:
       ```bash
       sudo yum install java-1.8.0
       wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz
       tar -xzf kafka_2.12-2.8.0.tgz
       cd kafka_2.12-2.8.0
       ```
   2. Editar el archivo: `config/zookeeper.properties` (Opcional)
      ```bash
      vim config/zookeeper.properties
      # Actualizar la variable: (lo puede dejar en el /tmp)
      dataDir=/tmp/zookeeper -> dataDir=/home/user/bin/kafka_2.12-2.8.0/data/zookeeper
      ```
      ```bash
      vim config/server.properties
      # Actualizar la variable: Actualizar la variable: (lo puede dejar en el /tmp)
      log.dirs=/tmp/kafka-logs -> dataDir=/home/user/bin/kafka_2.12-2.8.0/data/kafka-logs
      ```
3. Iniciar zookeeper:
   1. `bin/zookeeper-server-start.sh -daemon config/zookeeper.properties`
      ![Iniciando zookeper](../evidences/lab4/Evidence%201.png)
4. Iniciar el servidor de Kafka:
   1. `bin/kafka-server-start.sh -daemon config/server.properties`
      ![Iniciando el servidor Kafka](../evidences/lab4/Evidence%202.png)
5. Crear un tópico (será creado como sample-topic):
   1. `bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sample-topic`
      ![Creando un topico](../evidences/lab4/Evidence%203.png)
6. Listar los tópicos:
   1. `bin/kafka-topics.sh --list --zookeeper localhost:2181`
      ![Listar topicos en Kafka](../evidences/lab4/Evidence%204.png)
7. Borrar un tópico:
   1. `bin/kafka-topics.sh --delete --zookeeper localhost:2181 --topic sample-topic`
      ![Listar topicos en Kafka](../evidences/lab4/Evidence%205.png)
8. *PRODUCERS:*
   1. `bin/kafka-console-producer.sh --broker-list localhost:9092 --topic sample-topicconfig/zookeeper.properties`
      ![Listar topicos en Kafka](../evidences/lab4/Evidence%206.png)
9. *CONSUMERS:* 
   1.  `bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sample-topic --from-beginning`
       ![Listar topicos en Kafka](../evidences/lab4/Evidence%207.png)
10. Resultado final:
   ![Listar topicos en Kafka](../evidences/lab4/Evidence%208.png)
11. Detener el servidor de Kafka:
    1. `bin/kafka-server-stop.sh`
12. Detener zookeeper:
    1. `bin/zookeeper-server-stop.sh`

Con esto se daría por terminado el laboratorio 4