# Ansible Lab 1

## Introduction
Welcome! This lab is intended to demonstrate the use of an automation platform (Ansible) with Check Point Management and Gateway components.

In this lab, we will establish an Ansible setup which 

## Requirements
  - Debian or Ubuntu ISO image
    - http://releases.ubuntu.com/16.04/ubuntu-16.04.3-server-amd64.iso
  - VMWare Workstation

## Installation

  1. Create a new VMWare Virtual Machine

  Guest Operating System: Linux
  Version: Ubuntu
  Maximum Disk Size: 10GB

  2. Boot the Virtual Machine

  3. Install the git package
  ```apt-get install git```

  4. Clone the git repository for 
  ```
    mkdir /etc/ansible
    cd /etc
    git clone https://github.com/ngardiner/ansible_demo.git ansible
  ```
