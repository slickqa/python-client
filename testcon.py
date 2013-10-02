from slickqa import SlickQA
from slickqa import SlickConnection, ResultStatus, Configuration
from slickqa.queries import ConfigurationQuery

url = 'http://localhost:8080'

# sample of how to use the lower level api
slick = SlickConnection(url)
all_projects = slick.projects.find()
print(("Here are all the projects: {}".format(all_projects)))
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

# sample of how to use the higher level api
# this is good if you just need to shove the results up to slick and don't need to do anything tricky
slick_kahn = SlickQA(url, "test1", "1.0", "311", 'Smoke', 'smoky the bear')
if slick_kahn.is_connected:
    slick_kahn.add_log_entry("One message")
    slick_kahn.add_log_entry("two message")
    slick_kahn.file_result("tc1", ResultStatus.PASS, "I wanted it to pass", 2)
    slick_kahn.add_log_entry("new message")
    slick_kahn.add_log_entry("few message")
    slick_kahn.add_log_entry("dew message")
    slick_kahn.file_result("tc2", ResultStatus.FAIL, "I said FAIL!", 5)
    slick_kahn.add_log_entry("the sky is falling")
    slick_kahn.add_log_entry("so is my hair")
    slick_kahn.file_result("tc3", ResultStatus.SKIPPED, "darn straight Skippy!", 11)
    slick_kahn.add_log_entry("1")
    slick_kahn.add_log_entry("2")
    slick_kahn.add_log_entry("3")
    slick_kahn.add_log_entry("4")
    slick_kahn.file_result("tc4", ResultStatus.BROKEN_TEST, "THERE ARE FOUR LIGHTS!!!", 4)
    slick_kahn.finish_testrun()