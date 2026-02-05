# CMPE 273 – Week 1 Lab 1:

## Submission

### GitHub Repository
[Add your repository link here]

### Running Instructions
Detailed instructions to run this project can be found in `python-http/README.md`

### Output Screenshots

#### Success Case
1
![alt text](image.png)
2
![alt text](image-1.png)
3
![alt text](image-2.png)

#### Failure Case
1
![alt text](image-3.png)
2
![alt text](image-4.png)

### What Makes This Distributed?
There are two services running independently, failure in one one service does not cause failure in the other. Service A and Service B are separate processes/containers, each with their own runtime environment and they communicate over HTTP. Additionally both containers need not been on the same physical machine, they can run seperately.
---
