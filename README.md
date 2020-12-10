1. Spin up 12 EC2 instances on AWS on 3 different region (4 EC2 on each region)
2. Update the constant.py, app.py to have the path for these EC2 instances
3. You will have to generate a public key to connect to the EC2 instances.
4. SSH to your EC2 instances and move the required files to each EC2 and run below steps (from 1-4) on each EC2 instance. You can now run step 5 and 6 from your local or have it run from another EC2 in the same cluster.

# ScalablePBFT_New
As per the below order run the below commands (each command per new terminal): 
1. python3 init4.py
2. python3 init3.py
3. python3 init2.py
4. python3 init1.py
5. python3 client_node.py
6. python3 initiate.py


# Paxos
Run app.py, app1.py and app2.py on EC2 of the leader node for each cluster.


