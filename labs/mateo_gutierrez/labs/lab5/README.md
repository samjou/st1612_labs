# Primera parte:
## LAB 5 - Logs Agent -> Kinesis Firehose -> S3 -> Glue -> Athena

1. Crear un servicio de Kinesis Firehose con los siguientes datos:

        Create: Kinesis Data Firehose
        Name: purchaseLogs
        Source: Direct PUT or other sources
        Use: Kinesis Agent
        Destination: Amazon S3 - select or create a bucket
        Buffer interval: 60 segs
        Create new: ‘firehose_delivery_role’ with defaults
Se debería ver así: ![Kinesis Firehose](../evidences/lab5/part%201/Evidence%201.png)

2. Crear una máquina en EC2:
   1. Crear un IAM Role llamado 'MyEC2Kinesis' y adicionarlo a esta instancia EC2 con los permisos: `AmazonKinesisFullAccess` y `AmazonKinesisFirehoseFullAccess`
   
   Se debería ver así: ![Kinesis Firehose](../evidences/lab5/part%201/Evidence%202.png)

3. Instalar el agente kinesis:
   1. `sudo yum install -y aws-kinesis-agent`

4. Descargar los logs:
   1. [OnlineRetail.csv](https://github.com/st1612eafit/st1612_20212/raw/main/kinesis/OrderHistory/OnlineRetail.csv.gz)
   2. [LogsGenerator.py](https://raw.githubusercontent.com/st1612eafit/st1612_20212/main/kinesis/OrderHistory/LogGenerator.py)

5. Cambiar permisos y crear directorios:
    ```bash
    gunzip OnlineRetail.csv.gz
    chmod a+x LogGenerator.py
    sudo mkdir /var/log/acmeco
    ```

6. Modifique el archivo `agent.json` con el siguiente contenido:
      
      `sudo vim /etc/aws-kinesis/agent.json`
      ```json
      {
        "cloudwatch.emitMetrics": false,
        "kinesis.endpoint": "",
        "firehose.endpoint": "firehose.us-east-1.amazonaws.com",

        "flows": [
          {
            "filePattern": "/var/log/acmeco/*.log",
            "deliveryStream": "purchaseLogs"
          }
        ]
      }
      ```    

7. Iniciar el agente:
   1. `sudo systemctl start aws-kinesis-agent`

8.  Ejecutar un envio de logs:
   2. `sudo ./LogGenerator.py 1000`

9.  Al revisar el bucket S3 creado anteriormente se ve lo siguiente:
    ![Bucket S3](../evidences/lab5/part%201/Evidence%203.png)

10. Ejecute AWS Glue y consulte con AWS Athena los datos de S3
    1.  AWS Glue:
        ![AWS Glue](../evidences/lab5/part%201/Evidence%204.png)
    2. AWS Athena:
       ![AWS Athena](../evidences/lab5/part%201/Evidence%205.png)


# Segunda parte:
## LAB 5 - Logs Agent -> Kinesis Data Streams -> Lambda -> DynamoDB:

1. Crear un Kinesis Data Stream en AWS con la siguiente configuración:
    ```
    Name: acmecoOrders
    Nro shards: 1
    ```
Se debería ver así: ![Kinesis data stream](../evidences/lab5/part%202/Evidence%201.png)

2. Crear la tabla en DynamoDB:
    ```
    Table Name: acmecoOrders
    Partition Key: CustomerID (type: Number)
    Sort key: OrderID (type: String)
    Use defaults settings
    ```
Se debería ver así: ![DynamoDB](../evidences/lab5/part%202/Evidence%202.png)

3. Configurar el archivo `kinesis-agent` con la siguiente configuración:
   `sudo vim /etc/aws-kinesis/agent.json`
   ```json 
   "flows": [
        {
            "filePattern": "/var/log/acmeco/*.log",
            "kinesisStream": "acmecoOrders",
            "partitionKeyOption": "RANDOM",
            "dataProcessingOptions": [
                    {
                        "optionName": "CSVTOJSON",
                        "customFieldNames": [
                            "InvoiceNo",
                            "StockCode",
                            "Description",
                            "Quantity",
                            "InvoiceDate",
                            "UnitPrice",
                            "Customer",
                            "Country"
                        ]
                    }
            ]
        }
   ]
    ```

4. Reiniciar el servicio:
    1. `sudo systemctl restart aws-kinesis-agent`

5. Generar logs de prueba:
    1. `sudo ./LogGenerator.py 1000`

6. Ir a la instancia EC2 donde tenemos `kinesis-agent` para consumir los datos manualmente y almacenarlos en la base de datos DynamoDB:

    ```bash
    sudo yum install -y python3-pip
    sudo pip3 install boto3
    mkdir .aws
    cd .aws
    touch credentials
    ```
*Nota*: Copie las credenciales de AWS educate en el archivo `credentials`.

7. Configurar un Kinesis consumer, mediente un cliente standalone descargarlo de: [Consumer.py](https://github.com/st1612eafit/st1612_20212/raw/main/kinesis/OrderHistory/Consumer.py)
    1. ```bash
        chmod a+x Consumer.py
        python3 Consumer.py
       ```
    2. *Nota:* En otra terminal, generar nuevos registros usando `LogGenerator.py` para que el consumer los adquiera de Kinesis y los inserte en DynamoDB

8. Crear una funcion AWS Lambda para consumir de Kinesis e insertar en una tabla DynamoDB:
    1. Crear un IAM Role Lambda llamado 'acmecoOrders' con los permisos: `AmazonKinesisReadOnlyAccess` y `AmazonDynamoDBFullAccess`
    2. Crear la function lambda con la siguiente configuración:
    ```
    Author from scratch
    Function name: ProcessOrders
    Runtime: python 3.9
    Use an existing role: acmecoOrders
    ```
    3. Agregar un trigger del tipo `Kinesis Data Stream`

Se debería ver así: ![Lambda](../evidences/lab5/part%202/Evidence%203.png)

9. Revisar en la base de datos DynamoDB la inserción de los datos.

![Tabla de DynamoDB](../evidences/lab5/part%202/Evidence%204.png)

Con esto se concluiría el laboratorio 5