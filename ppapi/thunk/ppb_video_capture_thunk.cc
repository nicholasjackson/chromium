// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "ppapi/c/pp_errors.h"
#include "ppapi/shared_impl/ppb_device_ref_shared.h"
#include "ppapi/thunk/enter.h"
#include "ppapi/thunk/ppb_device_ref_api.h"
#include "ppapi/thunk/ppb_video_capture_api.h"
#include "ppapi/thunk/resource_creation_api.h"
#include "ppapi/thunk/thunk.h"

namespace ppapi {
namespace thunk {

namespace {

typedef EnterResource<PPB_VideoCapture_API> EnterVideoCapture;

PP_Resource Create(PP_Instance instance) {
  EnterResourceCreation enter(instance);
  if (enter.failed())
    return 0;
  return enter.functions()->CreateVideoCapture(instance);
}

PP_Bool IsVideoCapture(PP_Resource resource) {
  EnterVideoCapture enter(resource, false);
  return PP_FromBool(enter.succeeded());
}

int32_t EnumerateDevices(PP_Resource video_capture,
                         PP_Resource* devices,
                         PP_CompletionCallback callback) {
  EnterVideoCapture enter(video_capture, callback, true);
  if (enter.failed())
    return enter.retval();

  return enter.SetResult(enter.object()->EnumerateDevices(devices, callback));
}

int32_t Open(PP_Resource video_capture,
             PP_Resource device_ref,
             const PP_VideoCaptureDeviceInfo_Dev* requested_info,
             uint32_t buffer_count,
             PP_CompletionCallback callback) {
  EnterVideoCapture enter(video_capture, callback, true);
  if (enter.failed())
    return enter.retval();

  std::string device_id;
  // |device_id| remains empty if |device_ref| is 0, which means the default
  // device.
  if (device_ref != 0) {
    EnterResourceNoLock<PPB_DeviceRef_API> enter_device_ref(device_ref, true);
    if (enter_device_ref.failed())
      return enter.SetResult(PP_ERROR_BADRESOURCE);
    device_id = enter_device_ref.object()->GetDeviceRefData().id;
  }

  return enter.SetResult(enter.object()->Open(
      device_id, *requested_info, buffer_count, callback));
}

int32_t StartCapture(PP_Resource video_capture) {
  EnterVideoCapture enter(video_capture, true);
  if (enter.failed())
    return enter.retval();
  return enter.object()->StartCapture();
}

int32_t ReuseBuffer(PP_Resource video_capture,
                    uint32_t buffer) {
  EnterVideoCapture enter(video_capture, true);
  if (enter.failed())
    return enter.retval();
  return enter.object()->ReuseBuffer(buffer);
}

int32_t StopCapture(PP_Resource video_capture) {
  EnterVideoCapture enter(video_capture, true);
  if (enter.failed())
    return enter.retval();
  return enter.object()->StopCapture();
}

void Close(PP_Resource video_capture) {
  EnterVideoCapture enter(video_capture, true);
  if (enter.succeeded())
    enter.object()->Close();
}

int32_t StartCapture0_1(PP_Resource video_capture,
                        const PP_VideoCaptureDeviceInfo_Dev* requested_info,
                        uint32_t buffer_count) {
  EnterVideoCapture enter(video_capture, true);
  if (enter.failed())
    return enter.retval();

  return enter.object()->StartCapture0_1(*requested_info, buffer_count);
}

const PPB_VideoCapture_Dev_0_1 g_ppb_video_capture_0_1_thunk = {
  &Create,
  &IsVideoCapture,
  &StartCapture0_1,
  &ReuseBuffer,
  &StopCapture
};

const PPB_VideoCapture_Dev_0_2 g_ppb_video_capture_0_2_thunk = {
  &Create,
  &IsVideoCapture,
  &EnumerateDevices,
  &Open,
  &StartCapture,
  &ReuseBuffer,
  &StopCapture,
  &Close
};

}  // namespace

const PPB_VideoCapture_Dev_0_1* GetPPB_VideoCapture_Dev_0_1_Thunk() {
  return &g_ppb_video_capture_0_1_thunk;
}

const PPB_VideoCapture_Dev_0_2* GetPPB_VideoCapture_Dev_0_2_Thunk() {
  return &g_ppb_video_capture_0_2_thunk;
}

}  // namespace thunk
}  // namespace ppapi
