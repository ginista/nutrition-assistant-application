import ibm_db

hostname="125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
uid = "vcr98026"
pwd="TJRDiXCGyZVp0dwl"
driver="{IBM DB2 ODBC DRIVER}"
db="bludb"
port="30426"
protocol="TCPIP"
cert="Certificate.crt"
connection=(
    "DATABASE={0};"
    "HOSTNAME={1};"
    "PORT={2};"
    "UID={3};"
    "SECURITY=SSL;"
    "SSLServerCertificate={4};"
    "PWD={5};"
).format(db,hostname,port,uid,cert,pwd)

print(connection)
print("Connection Successfull !\n\n")

sql = "SELECT EMAIL,PASSWORD FROM logins"
stmt = ibm_db.exec_immediate(connection, sql)
dictionary = ibm_db.fetch_assoc(stmt)
while dictionary != False:
    # printing
    print("Full Row : ", dictionary)
    dictionary = ibm_db.fetch_assoc(stmt)