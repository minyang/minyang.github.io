---
layout: post
title: How to add new systemd services in Linux
description: Tips on how to add a new systemd service in Linux
date: '2021-04-05 10:32:00'
tags:
- software
- linux
- system_management
---

## Basics on Systemd Services

Some articles on the basics of the systemd services in Linux:

* [Understanding Systemd Units and Unit Files](https://www.digitalocean.com/community/tutorials/understanding-systemd-units-and-unit-files)
* [How To Use Systemctl to Manage Systemd Services and Units](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)
* [systemd.service — Service unit configuration](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
* [How To Use Journalctl to View and Manipulate Systemd Logs](https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs)
* [Use systemd to Start a Linux Service at Boot](https://www.linode.com/docs/guides/start-service-at-boot)

## Notes

### Location of Service Unit Files

* `/lib/systemd/system`: The default place where service unit files are
    installed on the system.  Lowest priority.
* `/run/systemd/system`: The location for run-time unit definitions.  Higher
    priority than `/lib/systemd/system` but lower than `/etc/systemd/system`.
* `/etc/systemd/system`:  The system-wide unit definitions with the highest
    priority.  Can override unit files in the other locations on the filesystem.

### Editing and Testing Service Files

Check if a new service is enabled:
```
systemctl is-enabled my_new_app.service
```

Start a new service and verify it is successfully started:
```
sudo systemctl start my_new_app.service
systemctl status my_new_app.service
```

If it fails to start, use `journalctl` for detailed logs:
```
sudo journalctl -xe
```

After modifying a service file, the `systemd` process should be reloaded:
```
sudo systemctl daemon-reload
```

