# CMPE 273 – Week 1 Lab 1:

## Submission

### GitHub Repository
[Add your repository link here]

### Running Instructions
Detailed instructions to run this project can be found in `python-http/README.md`

### Output Screenshots

#### Success Case
1
<img width="1452" height="466" alt="image" src="https://github.com/user-attachments/assets/12a02f13-7ee8-48d7-8202-81eadfbf7cf0" />

2
<img width="1462" height="87" alt="image" src="https://github.com/user-attachments/assets/a847a2b2-a4a2-4ac6-bc36-f9e36503f3b5" />

3
<img width="1475" height="482" alt="image" src="https://github.com/user-attachments/assets/f09beff3-6faa-416d-8ec6-219f76ca5fc9" />


#### Failure Case
1
<img width="1465" height="252" alt="image" src="https://github.com/user-attachments/assets/8f9f2ca4-5207-477b-87ff-89f74423f20f" />

2
<img width="1917" height="632" alt="image" src="https://github.com/user-attachments/assets/ea31bacd-86cf-47d0-ac28-c6c171348ba3" />


### What Makes This Distributed?
There are two services running independently, failure in one one service does not cause failure in the other. Service A and Service B are separate processes/containers, each with their own runtime environment and they communicate over HTTP. Additionally both containers need not been on the same physical machine, they can run seperately.
---
