// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "content/browser/system_message_window_win.h"

#include <dbt.h>
#include <string>
#include <vector>

#include "base/file_path.h"
#include "base/system_monitor/system_monitor.h"
#include "base/test/mock_devices_changed_observer.h"
#include "testing/gmock/include/gmock/gmock.h"
#include "testing/gtest/include/gtest/gtest.h"

class SystemMessageWindowWinTest : public testing::Test {
 public:
  virtual ~SystemMessageWindowWinTest() { }

 protected:
  virtual void SetUp() OVERRIDE {
    system_monitor_.AddDevicesChangedObserver(&observer_);
  }

  MessageLoop message_loop_;
  base::SystemMonitor system_monitor_;
  base::MockDevicesChangedObserver observer_;
  SystemMessageWindowWin window_;
};

TEST_F(SystemMessageWindowWinTest, DevicesChanged) {
  EXPECT_CALL(observer_, OnDevicesChanged()).Times(1);
  window_.OnDeviceChange(DBT_DEVNODES_CHANGED, NULL);
  message_loop_.RunAllPending();
}

TEST_F(SystemMessageWindowWinTest, RandomMessage) {
  window_.OnDeviceChange(DBT_DEVICEQUERYREMOVE, NULL);
  message_loop_.RunAllPending();
}
