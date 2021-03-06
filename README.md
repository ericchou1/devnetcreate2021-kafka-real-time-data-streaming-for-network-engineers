# DevNet Create 2021 Talk: Kafka Real Time Data Streaming for Network Engineers
DevNet Create 2021 Talk: Kafka Real Time Data Streaming for Network Engineers

This repository is provided as supplement for Cisco DevNet Create 2021 Talk

![Cisco DevNet Create 2021](/images/DevNet_Create_2021.png)
![Cisco DevNet Create 2021 Eric Chou Speaker](/images/Eric_Chou_Speaker.png)

## Useful links: 

- [Kafka Introduction](https://kafka.apache.org/intro)
- [Kafka Documentation](https://kafka.apache.org/documentation/)
- [Engineering Kafka for Secure Autonomous Operations](https://video.cisco.com/video/6258279442001)
- [Cisco's Real-time Ingestion Architecture with Kafka and Druid](https://imply.io/videos/ciscos-real-time-ingestion-architecture-with-kafka-and-druid)


## Full Playlist

- Clic image below for YouTube Playlist 

[![DevNet Create 2021 Full Playlist](/images/Example1_screenshot.png)](https://www.youtube.com/playlist?list=PLAaTeRWIM_ws4ySKWlq9nDpOptoMkRSW0)

## Example 1: Create Topic and Test

In this example, we will use the Kafka console commands to produce and consume messages. 

- Click image below for YouTube video

[![DevNet Create 2021 Exampple 1](/images/Example1_screenshot.png)](https://youtu.be/8agd1M-vafg)

## Example 2: Consumer Group and Key-Value Pair in Records

In this example, we will have multiple consumers in a consumer group as well as produce messages with key-value pairs. 

The key is important for offset sequence and which partition the data will live in. Basically when key=null, data is sent round robin, if the key is set, they will be sent to the same partition and order be guaranteed. The key can be a user, a device, a database id, etc. 

- Click image below for YouTube video

[![DevNet Create 2021 Exampple 2](/images/Example2_screenshot.png)](https://youtu.be/8qL98_7hB_k)

## Example 3: Topic Offsets

In this example, we will take a closer look at the concept of offsets. The offsets are kept a per-topic, per-consumer group level.  

- Click image below for YouTube video

[![DevNet Create 2021 Exampple 3](/images/Example3_screenshot.png)](https://youtu.be/BINK1Aex8Qs)

## Example 4: Simple Python Library Example

In this example, we will use the confluent-kafka Python library to produce and consume messages. 

- Click image below for YouTube video

[![DevNet Create 2021 Exampple 4](/images/Example4_screenshot.png)](https://youtu.be/2wyFaAJSZyU)



