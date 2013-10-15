#!/usr/bin/env python

from slickqa import SlickQA, ResultStatus, RunStatus
import datetime
import time

slick = SlickQA('http://localhost:8080', 'EP', '10.7', '5', 'My Testplan')

results = []
results.append(slick.file_result("First Test", status=ResultStatus.NO_RESULT, runstatus=RunStatus.TO_BE_RUN))
results.append(slick.file_result("Second Test", status=ResultStatus.NO_RESULT, runstatus=RunStatus.TO_BE_RUN))
results.append(slick.file_result("Third Test", status=ResultStatus.NO_RESULT, runstatus=RunStatus.TO_BE_RUN))
results.append(slick.file_result("Fourth Test", status=ResultStatus.NO_RESULT, runstatus=RunStatus.TO_BE_RUN))
results.append(slick.file_result("Fifth Test", status=ResultStatus.NO_RESULT, runstatus=RunStatus.TO_BE_RUN))

# Now to run the tests

for result in results:
    result.started = datetime.datetime.now()
    result.runstatus = RunStatus.RUNNING

    # I will fix this, I promise
    if hasattr(result, 'config') and not hasattr(result.config, 'configId'):
        del result.config
    if hasattr(result, 'component') and not hasattr(result.component, 'id'):
        del result.component

    # this updates slick with those properties we just set
    result.update()

    # pretend the test is running
    time.sleep(10)

    # add a log entry (will not automatically update the result in slick)
    result.add_log_entry("Log Entry, isn't it nice?", level="INFO", loggername="example.test")
    result.add_log_entry("Log Entry, isn't it nice?", level="ERROR", loggername="example.test")

    # do an update
    # I will fix this, I promise
    if hasattr(result, 'config') and not hasattr(result.config, 'configId'):
        del result.config
    if hasattr(result, 'component') and not hasattr(result.component, 'id'):
        del result.component

    # this updates slick with those properties we just set
    result.update()

    # add a file (will automatically update result in slick)
    result.add_file('example.py')

    result.finished = datetime.datetime.now()

    # give the runlength in total milliseconds
    result.runlength = int((result.finished - result.started).total_seconds() * 1000)

    result.status = ResultStatus.PASS
    result.reason = "Because I said"
    result.runstatus = RunStatus.FINISHED

    # I will fix this, I promise
    if hasattr(result, 'config') and not hasattr(result.config, 'configId'):
        del result.config
    if hasattr(result, 'component') and not hasattr(result.component, 'id'):
        del result.component

    # this updates slick with those properties we just set
    result.update()

slick.finish_testrun()

