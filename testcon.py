from slickqa import SlickQA
from slickqa import SlickConnection, ResultStatus, Configuration, Project
from slickqa.queries import ConfigurationQuery

url = 'http://localhost:8080'

slick = SlickConnection(url)
all_projects = slick.projects.find()
print(("Here are all the projects: {}".format(all_projects)))
high = SlickQA(url, "test1", "1.0", "311", "Smoke")
if high.is_connected:
    high.add_log_entry("One message")
    high.add_log_entry("two message")
    high.file_result("tc1", ResultStatus.PASS, "I wanted it to pass", 2)
    high.add_log_entry("new message")
    high.add_log_entry("few message")
    high.add_log_entry("dew message")
    high.file_result("tc2", ResultStatus.FAIL, "I said FAIL!", 5)
    high.add_log_entry("the sky is falling")
    high.add_log_entry("so is my hair")
    high.file_result("tc3", ResultStatus.SKIPPED, "darn straight Skippy!", 11)
    high.add_log_entry("1")
    high.add_log_entry("2")
    high.add_log_entry("3")
    high.add_log_entry("4")
    high.file_result("tc4", ResultStatus.BROKEN_TEST, "THERE ARE FOUR LIGHTS!!!", 4)

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
