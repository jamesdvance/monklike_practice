# Design A Distributed Message Queue

## Requirements
### Functional Requirements
1. Producers send a message to a queue, and consumers consume messages from it
2. Messages can be repeatedly consumed by different consumers. This is different than in a traditional message queue, where messages disappear after being delivered
3. Messages should be consumed in the same order they were produced. Different than traditional message queue, which doesn't guarantee order
4. Data needs to be persisted for two weeks. Different than a traditional queue, which doesn't persist
5. Should have unbound scaleability
6. Want to support at least once, and also at-most-once and exactly once, and make them configurable
7. Message size in kilobyte range

### Non Functional 
High throughput for some use cases like log aggregation
Low latency for traditional message queue use cases
Scaleable. Distributed and can handle a sudden surge in volume

### Partitioning
* Partitions can be evenly distributed across different servers, called brokers
* To keep the overall order within a partition, the position of a message is called an offset
* Messages can be sent to one of the partitions by the producer using a message key, that maps to a partition. Or can be randomly assigned
* When multiple consumers are subscribing to a topic, each consumer is responsible for a subset of the partitions for the topic. Together they form a  consumer group for the topic

### Consumer Group
* Each consumer group can subscribe to multiple topics and maintain its own consuming offsets. So order is preserved with a group, not above it
* The offset preserves order across partitions 
* However, order cannot be guaranteed if two different consumers in a consumer group are reading from the same partition
* Can fix with a constraint that a single partition can only be consumed by one consumer in a group
 

### High Level Components

Producers
* Send messages to the brokers

Brokers
* Are partitioned
* Each partition holds a subset of messages for a topic
* Store the data in a queue on disk in partitions
* Also store state variables on disk 

Consumer Groups
* Subscribes to topics and consumes messages

Metadata storage
* Store configuration and properties of topics on disk

Coordination Service
* Service discovery - aka which brokers are alive
* Leader election - one broker needs to be responsible for assigning partitions (the active controller) and there can be only one. This service chooses
* Apache Zookeeper or etcd for leader election

### Deep Dive

#### Data Storage
* needs to support our high-write and high-read requirements
* takes advantage of sequentional access performance of modern rotational disks
* allows message to be passed to producer to queue and consumer with no modiciations 
* Favors batching

Choosing Storage
* Not choosing database (either relational or NoSQL) because few exist that are ideal for both high write and high read loads
* A Write Ahead Log is an option where we append only to a logfile. WAL has a pure sequential read/write access pattern 
** The sequential pattern takes advantage of modern rotational disks with RAID configs that can support hundreds of MB read/write per second

