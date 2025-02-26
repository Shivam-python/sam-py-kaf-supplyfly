# sam-py-kaf-supplyfly

### Prerequisites

Ensure you have the following installed on your system:

- Python (>=3.8)

- pip

- Java (>=8, required for Kafka & Zookeeper)

- Apache Kafka (latest version)

## Step 1: Set Up a Virtual Environment for Flask

- Create a virtual environment : ```python -m venv venv```

- Activate the virtual environment

    - On macOS/Linux :  ```source venv/bin/activate```
    - On Windows : ```venv\Scripts\activate```

- Install dependencies : ```pip install -r requirements.txt```

## Step 2: Install and Set Up Kafka

1. Download Apache Kafka

```
curl -O https://downloads.apache.org/kafka/3.6.0/kafka_2.13-3.6.0.tgz
```

2. Extract Kafka

```
tar -xzf kafka_2.13-3.6.0.tgz
cd kafka_2.13-3.6.0
```

3. Start Zookeeper

    - Kafka requires Zookeeper to manage brokers. Start it with: ```bin/zookeeper-server-start.sh config/zookeeper.properties```

    - (For Windows, use:  ```bin\windows\zookeeper-server-start.bat config\zookeeper.properties```)

4. Start Kafka Broker

    - In a new terminal window: ```bin/kafka-server-start.sh config/server.properties```

    - (For Windows: ```bin\windows\kafka-server-start.bat config\server.properties```)

5. Create a Kafka Topic

    ```
    bin/kafka-topics.sh --create --topic geodata --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
    ```

6. Verify Topic Creation

    ```
    bin/kafka-topics.sh --list --bootstrap-server localhost:9092
    ```

## Step 3: Run the Flask App with Kafka producer

```
python bus1.py # runs consumer to simulate real-time movement

python app.py # runs python flask app

```

Now go to ```http://127.0.0.1:5001``` to see the results

> If you changed kafka topic name from the one given in example, please update the same in file <b>static/leaf.js<b>

```
var source = new EventSource('/topic/<your_topic_name>');
```