# layer-pyapp-snapped

This juju charm is meant to be a practice application to help you understand how to
work with DevOps and CI/CD in a juju context. 

Its purpose is get you going using juju to deploy applications packaged with snap.

This charm deploys the snap "pyapp", a practice python3 application.

It is available in snapstore, so you dont need to build it if you don't want to.

Go have a look ar [The pyapp snap repo](https://github.com/erik78se/snap-pyapp)

# Prepare

See that you can install the "pyapp" snap from snapstore.io
```bash
sudo snap install pyapp --channel edge --devmode
```
Then run pyapp.run and look for its messages in syslog:
```
$ pyapp.run 
$ tail -n 2 /var/log/syslog 
Dec  7 13:53:37 juju-4b8e5b-3 app.hello: this is debug
Dec  7 13:53:37 juju-4b8e5b-3 app.hello: this is critical
```
If that works, so will this charm.

# Deploy with juju
Just go ahead and deploy the latest verion of it:
```bash
juju deploy cs:~erik-lonroth/pyapp-snapped
```

# Building this charm
Clone this repo and build the charm.
```bash
git clone git@github.com:erik78se/layer-pyapp-snapped.git
cd layer-pyapp-snapped
make clean
make build
```

# Pushing to Charmstore
For the world to use.
```bash
cd builds
charm push ./pyapp-snapped
charm attach cs:~erik-lonroth/pyapp-snapped-0 pyapp-snap=pyapp.snap
charm release cs:~erik-lonroth/pyapp-snapped-0 --resource pyapp-snap-0
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
