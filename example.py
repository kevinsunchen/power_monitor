from carbontracker.tracker import CarbonTracker, CarbonTrackerManual
import time

tracker = CarbonTrackerManual(epochs=1, monitor_epochs=1, update_interval=1,
        components='all', epochs_before_pred=1, verbose=2)
tracker.tracker.pue_manual=1.59
tracker.intensity_updater.ci_manual = 294
# tracker = CarbonTracker(epochs=1, monitor_epochs=1, update_interval=1,
#         components='all', epochs_before_pred=1, verbose=2)

tracker.epoch_start()

time.sleep(10)
pass

# energy, acc = tracker.epoch_end('')
tracker.epoch_end('test')
pass
# NUM_TRIAL = 3
# tracker = CarbonTracker(epochs=NUM_TRIAL, monitor_epochs=NUM_TRIAL, update_interval=1,
#             components='all', epochs_before_pred=NUM_TRIAL)

# for i in range(NUM_TRIAL):
#     tracker.epoch_start()

#     time.sleep(10)
#     tracker.epoch_end()

# tracker.stop()