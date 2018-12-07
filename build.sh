make clean
make build
juju upgrade-charm --path=./builds/pyapp-snapped pyapp-snapped --force-units
