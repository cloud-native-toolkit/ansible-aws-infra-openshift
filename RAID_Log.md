# Risks


# Assumptions

| id | Description | Owner | Status |
| ------- | --------------------------------------------------- | ----------- | ------- |
| AS-01 | Use of Amazon.Aws Ansible collection is permitted | RE | Open | 


# Issues

| id | Description | Owner | Status |
| ------- | --------------------------------------------------- | ----------- | ------- |
| IS-01 | What is the VPE ACL utilized for? Same as VPC Endpoint? | RE | CLOSED |
| IS-02  | Is a VPN Endpoint AND VPN Gateway required in AWS? | RE | CLOSED (No, VPN endpoint for inbound and need Internet GW for outbound) |
| IS-03 | What is the equivalent of a Virtual Private Endpoint (VPE) in AWS? | RE | CLOSED |
| IS-04 | How to automate entry of ROSA parameters like VPC? | RE | OPEN | 
| IS-05 | Are we able to use community Ansible modules? If so, is there additional open source actions to take? | RE | OPEN |
| IS-06 | What are the network port requirements between the ingress and bastion tiers? | RE | OPEN |



# Dependencies

| id | Description |
| ------- | --------------------------------------------------- | 
| DP-01 | Ansible | 
| DP-02 | Ansible built-in module collection (ansible.builtin) |
| DP-03 | Ansible utils module collection (ansible.utils) |
| DP-03 | Amazon.Aws Ansible module collection |
| DP-04 | AWS community module collection (community.aws) |