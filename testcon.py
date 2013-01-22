from slickqa import SlickConnection, Configuration, Project
from slickqa.queries import ConfigurationQuery

slick = SlickConnection('http://localhost:8080')
allconfigs = slick.configurations.find()
print("All Configurations (there are " + str(len(allconfigs)) + " of them):")
for config in allconfigs:
    assert(isinstance(config, Configuration))
    print("\t Name: " + config.name + ", type: " + config.configurationType + ", id: " + config.id)

configs = slick.configurations.find(ConfigurationQuery(configurationType="ENVIRONMENT"))

print("\nThere are " + str(len(configs)) + " ENVIRONMENT configurations in slick:\n")
for config in configs:
    assert(isinstance(config, Configuration))
    print("\t Name: " + config.name + ", type: " + config.configurationType + ", filename: " + config.filename + ", id: " + config.id)

proj = slick.projects.findByName("Slickij Developer Project")
print("\nFound Project '%s' with %d components." % (proj.name, len(proj.components)))
