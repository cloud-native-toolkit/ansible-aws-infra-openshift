# IBM AWS Reference Architecture
 This repository is to document the build of a cloud reference architecture on AWS that support OpenShift ROSA with automation from Red Hat Ansible.

 The environments are built using AWS components with Ansible automation (see the [Red Hat Ansible collection repository](https://console.redhat.com/ansible/automation-hub)).

 ## Instructions

Choose the reference architecture to build for further instructions:

- [Quick Start reference architecture instuctions](./quickstart.md)
- [Standard reference architecture instructions](./standard.md)
- [Advanced reference architecture instructions](./advanced.md)

Post installation, optionally add an AWS provided client VPN endpoint for access to the environment per the instructions [here](./cvpn-readme.md).

### How to Run Ansible Playbook

```
$ ansible-playbook -vvv quickstart.yaml
```
