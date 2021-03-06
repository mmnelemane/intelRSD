"""
 * @section LICENSE
 *
 * @copyright
 * Copyright (c) 2016 Intel Corporation
 *
 * @copyright
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * @copyright
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * @copyright
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * @section DESCRIPTION
"""

from cts_framework.actions.action import Action
from cts_framework.db.dao.test_run_dao import TestRunDAO


class StatusListAction(Action):
    ACTION = "list"
    PARAM_NAME = "STATUS_TYPE"

    def process_action(self, configuration):
        test_runs = TestRunDAO().list_all_test_runs()
        print "ID\tDate"
        for test_run in test_runs:
            print "%s\t%s" % (test_run.test_run_id, test_run.test_run_datetime)
