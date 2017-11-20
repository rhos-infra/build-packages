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
                      help: 'OpenStack Release (5,6,7,8,9,10,11)'
                      required: True
            - title: Download specified packages
              options:
                  download-pkgs:
                      type: ListValue
                      help: 'Comma seperated list of packages to download'
