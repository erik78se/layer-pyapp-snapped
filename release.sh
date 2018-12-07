cd builds
# Below gets the charm url
charm=$(charm push ./pyapp-snapped | grep -Po "(?<=^url: ).*")
touch pyapp.snap core.snap
charm attach $charm pyapp-snap=pyapp.snap                                             
charm release $charm --resource pyapp-snap-0
