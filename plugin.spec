---
plugin_type: install
description: Build packages from source
subparsers:
    build-packages:
        help: Build the specified packages from source
        include_groups: ['Ansible options', 'Inventory', 'Common options', 'Answers file']
        groups:
            - title: Build Openvswitch from source
              options:
                  build-ovs:
                      type: Bool
                      help: 'Build OVS from source and inject it into the deployment'
                      required: False
                      default: True
