## Build-Packages

Building RPMs out of a source of certain project

### How to use this project as an ansible playbook

Create virtual environment:

    virtualenv venv && source venv/bin/activate
    pip install ansible

Run:

    ansible-playbook -i hosts main.yml

### How to use this as an InfraRed plugin

Install InfraRed

    git clone https://github.com/redhat-openstack/infrared.git
    cd infrared && virtualenv venv && source venv/bin/activate && pip install -e .

Add build-packages as a plugin:

    infrared plugin add https://github.com/rhos-infra/build-packages.git

Run:
    infrared build-packages --host-ip 1.1.1.1 --host-username <user-name> --host-key_file ~/.ssh/id_rsa

### How to contribute

Contributions are done via GerritHub. Do not use pull requests or direct push :)
