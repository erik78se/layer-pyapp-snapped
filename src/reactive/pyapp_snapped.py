from charmhelpers.core.hookenv import (
    open_port,
    status_set,
)

from charms.reactive import (
    when,
    when_not,
    set_flag,
)



@when('snap.installed.pyapp')
@when_not('my.pyapp.application.available')
def set_django_snapped_available():
    status_set('active', "pyapp AVAILABLE")
    set_flag('my.pyapp.application.available')
