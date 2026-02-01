# Databricks notebook source
server_name = "jdbc:sqlserver://mytrainingsqlserver.database.windows.net"
database_name = "mytrainingsqldb "
url = server_name + ";" + "databaseName=" + database_name + ";"

table_name = "dbo.ordersnew"
username = dbutils.secrets.get("adbdevscope","sqlusername")
password = dbutils.secrets.get("adbdevscope","sqlpassword")


 


# COMMAND ----------

df = (spark.read.format("jdbc")
        .option("url",url)
        .option("dbtable", table_name)
        .option("user", username) 
        .option("password", password).load()) 
display(df)

# COMMAND ----------

sqlquery = "select orderdate, productkey , country, salesamount from ordersnew"

df2 = (spark.read.format("jdbc")
        .option("url",url)
        .option("query", sqlquery)
        .option("user", username) 
        .option("password", password).load()) 
display(df2)

# COMMAND ----------

 (df.write
    .format("jdbc")
    .option("url", url) 
    .option("dbtable", "neworders2")
    .option("user", username) 
    .option("password", password) 
    .save())

# COMMAND ----------

 (df.write
    .format("jdbc")
    .option("url", url) 
    .mode("overwrite")
    .option("dbtable", "Orders2")
    .option("user", username) 
    .option("password", password) 
    .save())

# COMMAND ----------

 (df.write
    .format("jdbc")
    .option("url", url) 
    .mode("append")
    .option("dbtable", "Orders2")
    .option("user", username) 
    .option("password", password) 
    .save())

# COMMAND ----------

df3 = (spark.read.format("jdbc")
        .option("url",url)
        .option("dbtable", "ordersnew")
        .option("user", username) 
        .option("numpartitions",10)
        .option("password", password).load()) 
display(df3)

# COMMAND ----------

df4 = (spark.read.format("jdbc")
        .option("url",url)
        .option("dbtable", "ordersnew")
        .option("user", username) 
        .option("numpartitions",10)
        .option("fetchsize",20)
        .option("password", password).load()) 
display(df4)

# COMMAND ----------

df4 = (spark.read.format("jdbc")
        .option("url",url)
        .option("dbtable", "ordersnew")
        .option("user", username) 
        .option("numpartitions",5)
        .option("partitioncolumn","productkey")
        .option("lowerbound",1)
        .option("upperbound",1000)
        .option("password", password).load()) 
display(df4)

# COMMAND ----------

driver_manager = spark._sc._gateway.jvm.java.sql.DriverManager
con = driver_manager.getConnection(url, username, password)
statement =f"""TRUNCATE TABLE dbo.neworders2"""
exec_statement = con.prepareCall(statement)

exec_statement.execute()

exec_statement.close()
con.close()


# COMMAND ----------

driver_manager = spark._sc._gateway.jvm.java.sql.DriverManager
con = driver_manager.getConnection(url , username, password)
statement =f"""EXEC sp_InsertData3 '2023-04-01',310,'UK','TV',2000,200"""
exec_statement = con.prepareCall(statement)

exec_statement.execute()

exec_statement.close()
con.close()


# COMMAND ----------

orderdate = '2023-04-01'
productkey = 312
country = "UK"
product ="TV"
sales= 20000
tax = 2000

driver_manager = spark._sc._gateway.jvm.java.sql.DriverManager
con = driver_manager.getConnection(url, username, password)
statement =f"""EXEC sp_InsertData3 '{orderdate}',{productkey},'{country}','{product}',{sales},{tax}"""
print(statement)
exec_statement = con.prepareCall(statement)

exec_statement.execute()

exec_statement.close()
con.close()


# COMMAND ----------

