#!/usr/bin/env bash

cd /ansible-network-interfaces/tests

echo "Installing ansible"
pip install --user ansible==2.3.0.0 ansible-lint==3.4.12

echo "Checking Ansible syntax"
ansible-playbook --inventory=localhost, --connection=local test.yml --syntax-check

echo "Running Ansible-Lint"
ansible-lint test.yml

echo "Running the test.yml playbook"
ansible-playbook --inventory=localhost, --connection=local test.yml -vvv
