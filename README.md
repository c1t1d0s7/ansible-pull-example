# Ansible Pull Mode Example

Run `local.yml` playbook

```bash
ansible-pull -U https://github.com/c1t1d0s7/ansible-pull-example
```

Run `local.yml` playbook with python dynamic inventory

```bash
ansible-pull -U https://github.com/c1t1d0s7/ansible-pull-example -i inventory/hosts.py
```

Run 'webserver_install.yaml` playbook

```bash
ansible-pull -U https://github.com/c1t1d0s7/ansible-pull-example webserver_install.yml
```

