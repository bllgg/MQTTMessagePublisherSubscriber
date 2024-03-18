# MQTT Subscriber-Publisher

This project demonstrates how to implement an MQTT subscriber and publisher using Python and the Paho MQTT client library. MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol commonly used for IoT (Internet of Things) and real-time communication between devices.

## Requirements

- Python 3.x
- Paho MQTT client library (`paho-mqtt`)

## Installation

1. Ensure you have Python 3.x installed on your system. If not, download and install it from the official Python website: [python.org](https://www.python.org/).

2. Install the Paho MQTT client library using pip:

    ```
    pip install paho-mqtt
    ```

## Usage

### Publisher

The publisher sends messages to a specific MQTT topic.

To run the publisher, execute the `mqtt_publisher.py` script:

Edit the `mqtt_publisher.py` script to adjust the MQTT broker address, port, topic, username, password, and message payload as needed.

### Subscriber

The subscriber listens for messages on a specific MQTT topic.

To run the subscriber, execute the `mqtt_subscriber.py` script:

Edit the `mqtt_subscriber.py` script to adjust the MQTT broker address, port, topic, username, and password as needed.

## Configuration

- The MQTT broker address and port should be set according to your MQTT broker configuration.
- If your MQTT broker requires authentication, provide the username and password in the scripts.
- Adjust the MQTT topic in both the publisher and subscriber scripts to match the topic you want to publish to and subscribe to, respectively.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).
