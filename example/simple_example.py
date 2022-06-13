"""
=======
Copyright, 2021, LogicMonitor, Inc.
This Source Code Form is subject to the terms of the 
Mozilla Public License, v. 2.0. If a copy of the MPL 
was not distributed with this file, You can obtain 
one at https://mozilla.org/MPL/2.0/.
=======
"""

import time
from random import seed, random

import logicmonitor_data_sdk

# LogicMonitor metric data model is as below
#
#Company 
#  |--- Resource (like device/service. Ex: VM) 
#  |--- Data Source   (Ex. CPU)   
#         |--- Instance (of a Data Source on a resource. Ex. CPU-1)
#               |--- Data Point (the metric which is being monitored. Ex. %Used)
#                     |- <Time> : <Metric Value>
#                     |- <Time> : <Metric Value>
#                     |... 
#
from logicmonitor_data_sdk.api.metrics import Metrics
from logicmonitor_data_sdk.models import DataSource, \
  Resource, DataSourceInstance, DataPoint

# Configure SDK with Account and access information
# On your LogicMonitor portal, create API token (LMv1) for user and get
# Access Id and Access Key
configuration = logicmonitor_data_sdk.Configuration(company='your_company',
                                                    id='4kGr8YGG86u8UM83sUi8',
                                                    key='4[73hMj5}6%TUz^83PFkz_k7349](M[a}[8NC6Y]')

# Create api handle for Metrics use case (we also support Logs)
metric_api = Metrics()

return_val = metric_api.send_metrics(
               resource=Resource(
                   ids={"system.hostname": "SampleDevice"},  #Core Properties of the Resource 
                   create=True,                              #Auto-create resource if does not exist
                   name="SampleDevice",                      #Name of the resource
                   properties={"using.sdk": "true"}),        #Additional Properties [Optional]
               datasource=DataSource(
                   name="SampleDS"),                         #Name of data source is must. Rest optional
               instance=DataSourceInstance(
                   name="SampleInstance"),                   #Name of instance is must. Rest optional
               datapoint=DataPoint(
                   name="SampleDataPoint"),                  #The metric 
               values={str(int(time.time())): str(random())} #Values at specific time(s)
)
print("Return Value = ",return_val)
