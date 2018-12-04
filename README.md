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
