from flask import Flask, render_template
import time
from paho.mqtt import client as mqtt_client

app = Flask(__name__)
#Set the Hostname, Port & TopicName

broker = 'broker.emqx.io'
port = 1883
topic = 'topicName/iot'
client_id = 'test'
username = 'emqx'
password = ''

def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main', methods = ['POST'])
def main():
    return render_template('main.html')

@app.route('/1', methods = ['POST'])
def drive():
    test_drive()
    return render_template('1.html')

def test_drive():
    client = connect_mqtt()
    client.loop_start()
    start_driving(client)

def start_driving(client):
    msg = '1'
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print("Send '{msg}' to topic '{topic}'")

@app.route('/2', methods = ['POST'])
def tunnel():
    tunnel_drive()
    return render_template('2.html')

def tunnel_drive():
    client = connect_mqtt()
    client.loop_start()
    tunnel_driving(client)

def tunnel_driving(client):
    msg = '2'
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print("Send '{msg}' to topic '{topic}'")

if __name__ == '__main__':
    app.run(port = 5001)