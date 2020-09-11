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
                  version:
                      type: Value
                      help: 'OpenStack release number'
            - title: Install packages
              options:
                  packages:
                      type: ListValue
                      help: 'Comma,separated list of packages to install'
            - title: Download packages
              options:
                  download-packages:
                      type: ListValue
                      help: 'Comma seperated list of packages to download'
