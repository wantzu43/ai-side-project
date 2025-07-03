# Deployment Guide: Flask + MySQL + Nginx Project

## Overview
This guide provides step-by-step instructions to deploy the Flask application with MySQL and Nginx using Docker and Ansible.

## Prerequisites
- Ansible installed on your local machine.
- Docker and Docker Compose installed on the target server.
- SSH access to the target server.

## Deployment Steps
### Step 1: Configure Ansible Inventory
Edit the `inventory.ini` file to specify your target server's IP address and SSH user:
```ini
[web]
server ansible_host=your.server.ip ansible_user=your_ssh_user
```
### Step 2: Execute Ansible Playbook
Run the following command to execute the Ansible playbook:
```bash
ansible-playbook -i inventory.ini deploy.yml
```

