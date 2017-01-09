Ansible network interface configuration
=======================================
[![Ansible Galaxy](https://img.shields.io/badge/Ansible%20Galaxy-dresden--weekly.network--interfaces-blue.svg)](https://galaxy.ansible.com/dresden-weekly/network-interfaces/)

This is an Ansible role that manages network interface configuration as it is found on Debian/Ubuntu servers

Requirements
------------

Ubuntu 12.04 (Precise), Ubuntu 14.04 (Trusty) or Ubuntu 16.04 (Xenial)

May work with other versions, but has never been tested.

Dependencies
------------

none

Example Playbook
----------------

```yml
- hosts: all
  become: true
  become_user: root

  roles:
  - role: dresden-weekly.network-interfaces

    network_interfaces:
    - device: eth0
      description: just a description for humans to understand
      auto: true
      family: inet
      method: static
      address: 192.168.1.11
      network: 192.168.1.0
      netmask: 193.168.1.255
      gateway: 192.168.1.1
      mtu: 9000
      nameservers:
      - 8.8.8.8
      - 8.8.4.4
      subnets:
      - 192.168.1.12/32

    - device: eth1
      description: simple dhcp client interface
      auto: true
      family: inet
      method: dhcp

    - device: vlan123
      description: sample vlan interface using eth0 and tagged for VLAN 123.
      method: static
      address: 1.2.3.4
      netmask: 24
      broadcast: 1.2.3.255
      vlan:
        raw-device: eth0
      up:
      - route add default gw 1.2.3.254

    - device: eth2
      description: First bonding device
      auto: true
      family: inet
      method: manual
      bond:
        master: bond0

    - device: eth3
      description: Second bonding device
      auto: true
      family: inet
      method: manual
      bond:
        master: bond0

    - device: bond0
      description: This bonding device only has one interface
      allow:
      - hotplug
      family: inet
      method: static
      bond:
        mode: 802.3ad
        xmit-hash-policy: layer3+4
        miimon: 100
        slaves: eth2 eth3
      address: 192.160.50.1
      netmask: 255.255.255.0
      dns_search: "localdomain"
      up:
      - ip route add 172.16.0.0/24 via 192.168.50.254 dev bond0
```

Changelog
---------

**1.1** (*TODO*)

* [✓] support `xmit_hash_policy` for bond (thanks @benner)
* [✓] bugfix `ifenslave` should triggers vlan package install (thanks @linuxsimba)
* [✓] support for custom `mtu` settings (thanks @benner)
* [ ] open for your ideas, fixes and pull requests

**1.0** (Ansible 2 release) 2016-03-30

* [✓] compatible with Ansible 2.x
* [✓] support all hook aliases
* [✓] support for all allow stanzas
* [✓] full device restart control
* [✓] improved support for bonding
* [✓] one config file per device

**0.1** (first release) 2015-02-01

* [✓] ipv6 & ipv4 support
* [✓] support for multiple network devices
* [✓] dhcp and static configuration
* [✓] support for bridges
* [✓] support for bonding
* [✓] additional subnets and ips
* [✓] custom hook scripts
* [✓] remove old interfaces

License
-------

The MIT License (MIT)

Copyright (c) 2015 dresden-weekly

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
