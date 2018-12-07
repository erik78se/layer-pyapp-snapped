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
