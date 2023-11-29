from carbontracker.tracker import CarbonTracker, CarbonTrackerManual
import time

tracker = CarbonTracker(epochs=1, monitor_epochs=1, update_interval=1,
        components='all', epochs_before_pred=1, log_dir='logs', verbose=2)
# tracker.tracker.pue_manual=1.59
# tracker.intensity_updater.ci_manual = 294

max_epochs = 3
for epoch in range(max_epochs):
    tracker.epoch_start()

    time.sleep(10)

    tracker.epoch_end('test')