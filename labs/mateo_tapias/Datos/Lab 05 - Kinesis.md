# Lab 05
## Guide
- [Lab 05 AWS Kinesis](../_resources/Lab5-aws-kinesis-20212.docx)
- [Lab 05 Repository](https://github.com/st1612eafit/st1612_20212/tree/main/kinesis)

## Resources
- EC2 Instance
**NOTE: Instead of creating a new role, I modified the default role that AWS creates for new EC2 machines with the appropriated permissions from the lab guide.**

<img src="../_resources/a2bb4bab06cefd0aa23a540ee8a72024.png" alt="" width="615" height="251" class="jop-noMdConv">

- Dynamo DB
![e779320cb953ba3bac88ddecf15163ee.png](../_resources/e779320cb953ba3bac88ddecf15163ee.png)
    
- Lambda with Kinesis trigger
![fe74f9f72edd67a6dc43fe44ded2bab8.png](../_resources/fe74f9f72edd67a6dc43fe44ded2bab8.png)
    
- AWS Kinesis Delivery Stream
![d62e50f6740ab319a2bd9c008c988f31.png](../_resources/d62e50f6740ab319a2bd9c008c988f31.png)
- AWS Kinesis Data Stream
![8a52f7382dbedfcb89055e393d61a8c4.png](../_resources/8a52f7382dbedfcb89055e393d61a8c4.png)
    
- S3 Bucket
![ac000ec4e7e48dc4cf52fff54759c097.png](../_resources/ac000ec4e7e48dc4cf52fff54759c097.png)
    

## Kinesis Configuration
### Local
- Kinesis Agent
![ba0cc502a54e1ea0770b019d48318733.png](../_resources/ba0cc502a54e1ea0770b019d48318733.png)
    
- logs:
![21beb46b94df5b89b94cef86c69262b9.png](../_resources/21beb46b94df5b89b94cef86c69262b9.png)
    
- Local Consumer to DynamoDB
![88eb7cbcdddc337fd0e60a03255532ae.png](../_resources/88eb7cbcdddc337fd0e60a03255532ae.png)
    

### Lambda
1.  Lambda Source Code
![1a0d909e85699135ce358806b04ae43d.png](../_resources/1a0d909e85699135ce358806b04ae43d.png)
    
2.  Delete items for lambda upload
![0d222c1e837a1c3aa4a9a3edbb7a54a5.png](../_resources/0d222c1e837a1c3aa4a9a3edbb7a54a5.png)
    
3.  Dynamo Items from Lambda
![f4b6351f0b88af52c870cfa54802b877.png](../_resources/f4b6351f0b88af52c870cfa54802b877.png)
![3503e177b35ebbc0aa43d4b6b1dcc908.png](../_resources/3503e177b35ebbc0aa43d4b6b1dcc908.png)
![eba49805bec7248293f8686c17851295.png](../_resources/eba49805bec7248293f8686c17851295.png)