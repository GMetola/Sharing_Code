from harvesters.core import Harvester
#[...]

self.h.add_file('[...]ids_gevgentlk_cam5.cti')
self.h.update()
self.ia = self.h.create_image_acquirer(serial_number='4103886517')
self.ia.remote_device.node_map.TriggerMode.value = 'Off'
self.ia.remote_device.node_map.AcquisitionFrameRateTargetEnable.set_value(False)
self.ia.remote_device.node_map.AcquisitionFrameRateTarget.set_value(framerate)
self.ia.remote_device.node_map.AcquisitionFrameRateTargetEnable.set_value(True)
self.ia.buffer_handling_mode = 'NewestOnly'
self.ia.remote_device.node_map.GevSCPD.value = 0
if not self.desired_exposure is None:
    self.ia.remote_device.node_map.ExposureTime.value = self.desired_exposure
if not self.desired_gain is None:
    self.ia.remote_device.node_map.Gain.value = self.desired_gain
self.ia.remote_device.node_map.DeviceLinkThroughputLimit.value = self.ia.remote_device.node_map.DeviceLinkThroughputLimit.max
self.ia.remote_device.node_map.PixelFormat.value = 'Mono8'
self.ia.remote_device.node_map.TriggerSelector.value = 'ExposureStart'
self.ia.remote_device.node_map.AcquisitionMode.value = 'Continuous'
self.ia.remote_device.node_map.TriggerMode.value = 'On'
self.ia.remote_device.node_map.TriggerSource.value = 'Software'
self.ia.start_acquisition()
