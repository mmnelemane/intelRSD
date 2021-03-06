/*!
 * @section LICENSE
 *
 * @copyright
 * Copyright (c) 2015-2016 Intel Corporation
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
 *
 * @brief Main entry for all AGENT_FRAMEWORK Agent Framework tests
 *
 * Initialize Google C++ Mock and Google C++ Testing Framework
 * Do general cleanup after tests like delete resources from singletons
 * */

#include "gmock/gmock.h"
#include "gtest/gtest.h"

#include "agent-framework/command/command.hpp"
#include "agent-framework/command/command_json.hpp"

using agent_framework::command::Command;
using agent_framework::command::CommandJson;

int main(int argc, char* argv[]) {
    testing::InitGoogleMock(&argc, argv);
    int test_result = RUN_ALL_TESTS();

    /* After tests, do general cleanup here */
    Command::Map::cleanup();
    CommandJson::Map::cleanup();

    return test_result;
}
