# Tutorial: Charms with layer-snap

Difficulty: Intermediate
Author: [Erik Lönroth](http://eriklonroth.com)

## Warning: Work In Progress
This tutorial is in the making, feel to test and help me to improve it.

Note! Currently, [layer-snap] also need patching. I have made a PR to make this all work nicely. See: https://github.com/stub42/layer-snap/pull/19  @stub  *hint*

All code for the charm can be found here: https://github.com/erik78se/layer-pyapp-snapped

## Preparations
1. You should have completed the first beginner tutorial [Part 1], [Part 2], [Part 3] before taking this tutorial. 
2. Use juju 2.4 or greater.
3. charm-tools 2.4.4 or above or builds will fail.

Its good if you know how to create your own SNAP, but its not needed. [You can learn SNAP:ing here].

## What you will learn
* Understand why [SNAP:s] are useful in a JUJU context.
* Create a simple juju charm with "[layer-snap]"

## Why juju charms + SNAP ?
SNAP packages are universal to any linux distribution. This means that you can deploy your application on ANY linux distribution without having to re-package for each distro.

A specifically interesting use-case of [SNAP:s] and JUJU are for "IoT applications". IoT benefit heavily from the SNAP format and having a good means to deploy them: 

1. SNAPs do atomic upgrades.
2. SNAPs are OS agnostic.
3. SNAPs has a very secure confinement.
4. IoT lives often in complex systems where service orchestration is needed (juju).

All in all, SNAP:s and deployment with JUJU makes life easier any development scenario.

## The SNAP
You will use a training SNAP I have created for you: [pyapp]. The pyapp application is a python3 application that writes a simple message to stdout and loggs a few messages to syslog.

The code for [pyapp] is available here: [snap-pyapp]

You can easily install it to test it if you like:
```bash
sudo snap install pyapp --devmode
pyapp.run
```

## Create a charm & include "layer-snap".
I call my charm "pyapp-snapped" (Recall from earlier tutorials that the layer- prefix is to indicate this is a reactive charm.) Feel free to use your own cooler name.

```bash
snapcaft create layer-pyapp-snapped
```
## Create your **layer.yaml** and modify the repo value as needed. 

_Pay some attention to that we are in fact installing two snaps here. "core" and "snap". The reason for pulling in the "core" snap is that there seems to be a bug that occasionally leaves out this. I think this might go away in the future. For now, see it as a bonus._
 
```yaml
includes:
  - 'layer:basic'
  - 'layer:snap'
options:
  snap:
    core:
      channel: stable
      devmode: false
      jailmode: false
      dangerous: false
      classic: false
      revision: null
    pyapp:
      channel: edge
      devmode: true
      jailmode: false
      dangerous: false
      classic: false
      revision: null
repo: 'https://github.com/erik78se/layer-pyapp-snapped'
```
## Create your **metadata.yaml**

```yaml
name: pyapp-snapped
display-name: pyapp-snapped
summary: Simple charm for the pyapp snap
maintainer: Erik Lonroth <erik.lonroth@gmail.com>
description: |
  This charm deploys the pyapp  application, just add it as a resource and you are off to the races!
tags:
  - example
  - snap
  - pyapp
series:
  - bionic
resources:
  pyapp-snap:
    type: file
    filename: pyapp.snap
    description: A pyapp snap
```
What you should notice here, is the included [charm-resource]. This makes the [layer-snap] aware that you _may_ attach a package along with your deployment (It will be uploaded to the juju controller who then distributes it). We won't do this in this tutorial, but feel free to try it on your own.  

The resource is just going to be a placeholder in this case. [layer-snap] will automatically download our snap from snapstore.io if it is not uploaded to the controller along with the deploy.


## Create the **reactive/layer_pyapp_snapped.py**
```yaml
from charmhelpers.core.hookenv import (
    open_port,
    status_set,
)
from charmhelpers.core.hookenv import application_version_set
from charms.reactive import (
    when,when_not,
    set_flag,clear_flag
)
from charms.layer import snap

@when('snap.installed.pyapp')
def set_pyapp_snapped_available():
    """
    When snap is installed, just keep on updating.
    """
    version = snap.get_installed_version('pyapp')
    channel = snap.get_installed_channel('pyapp')
    application_version_set(version)
    status_set('active', "Ready pyapp-{} ({})".format(version,channel))
    set_flag('my.pyapp.application.available')

@when_not('snap.installed.pyapp')
def pyapp_not_installed():
    """
    Whenever the snap is not installed, clear statuses and flags.
    """
    application_version_set("")
    clear_flag('my.pyapp.application.available')
    status_set('waiting', "Pyapp snap not installed.")
```

## Proof, Build and Deploy
```bash
charm proof
charm build
```
Deploy from your local build.
```bash
juju deploy /home/erik/charms/builds/pyapp-snapped
Deploying charm "local:bionic/pyapp-snapped-0".
```

## Test it
Lets see if the snap was installed and works.
```bash
juju ssh pyapp-snapped/0 /snap/bin/pyapp.run
```

Great! You have just created a juju charm that deploys a snap!

## Next lesson
Next we will learn to add in a [juju-action] and relate our charm to a logging and search facility - the [ELK] (Elasticsearch, Logstash, Kibana) stack.

[Part 1]: https://discourse.jujucharms.com/t/tutorial-charm-development-beginner-part-1/377
[Part 2]: https://discourse.jujucharms.com/t/tutorial-charm-development-beginner-part-2/378
[Part 3]: https://discourse.jujucharms.com/t/tutorial-charm-development-beginner-part-3/379
[layer-snap]: https://github.com/stub42/layer-snap
[charm-tools]: https://docs.jujucharms.com/devel/en/tools-charm-tools
[juju-action]: https://docs.jujucharms.com/2.4/en/actions
[SNAP:s]: https://snapcraft.io/
[pyapp]: https://snapcraft.io/pyapp/listing
[snap-pyapp]: https://github.com/erik78se/snap-pyapp
[ELK]: https://jujucharms.com/u/omnivector/elk/bundle/
[You can learn SNAP:ing here]: https://docs.snapcraft.io/getting-started/3876
[charm-resource]: https://docs.jujucharms.com/2.4/en/charms-resources

## Contributors
@jamesbeedy - For teaching me about juju 
@stub - Author of the layer-snap
