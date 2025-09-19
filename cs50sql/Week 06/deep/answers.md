# From the Deep

In this problem, you'll write freeform responses to the questions provided in the specification.

## Random Partitioning

The data is evenly distributed among the boats, which equalizes their load.
Querying the data will require searching all boats, which may take more time.

## Partitioning by Hour

The data is organized by hour, which makes hour-based queries easier.
The data is not distributed equally among the boats, which may eventually overload one or the other.

## Partitioning by Hash Value

Using hashes allows the load to be distributed evenly among the boats, and it enables knowing which boat a specific timestamp belongs to. However, searching by ranges will still require searching all boats.
