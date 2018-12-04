# layer-pyapp-snapped

This layer manages the lifecycle of the the snapped pyapp application.

[The pyapp snap repo](https://github.com/erik78se/snap-pyapp)

# Prep

See that you can install the "pyapp" snap from snapstore.io
```bash
sudo snap install pyapp --channel edge --devmode
```
If that works, so will the charm (You can remove the pyapp after your test)

# Building the charm

```bash
git clone git@github.com:erik78se/layer-pyapp-snapped.git
cd layer-pyapp-snapped
make clean
make build
```

# Deplopyment
Deployment command:
```bash
juju deploy ./builds/pyapp-snapped
```

```
Model    Controller           Cloud/Region         Version  SLA          Timestamp
default  localhost-localhost  localhost/localhost  2.4.7    unsupported  23:30:18+01:00

App            Version  Status  Scale  Charm          Store  Rev  OS      Notes
pyapp-snapped           active      1  pyapp-snapped  local    4  ubuntu  

Unit              Workload  Agent  Machine  Public address  Ports  Message
pyapp-snapped/1*  active    idle   1        10.218.68.210          pyapp AVAILABLE

Machine  State    DNS            Inst id        Series  AZ  Message
1        started  10.218.68.210  juju-4b8e5b-1  bionic      Running
```
