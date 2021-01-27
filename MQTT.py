from time import gmtime, strftime
import paho.mqtt.client as mqtt
import sqlite3

dbFile = "data.db"

timeArray = [0, 0]
dataArray = [0]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("out")

def on_message(client, userdata, msg):
    timeArray[0] = strftime("%d.%m.%y %H:%M")
    msg.payload = msg.payload.decode("utf-8")
    dataArray[0] = str(msg.payload)

    print("Recive data in topic " + "\"" + msg.topic + "\"")

    writeToDb(timeArray[0], dataArray[0])

def writeToDb(theTime, theData):
    conn = sqlite3.connect(dbFile)
    c = conn.cursor()
    print (timeArray[0] + "\t" + dataArray[0] + "\t" + "Writing to db...")
    c.execute('INSERT INTO date VALUES (?,?)', (theTime, theData))
    conn.commit()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()