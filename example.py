from carbontracker.tracker import CarbonTracker
import time

NUM_TRIAL = 3
tracker = CarbonTracker(epochs=NUM_TRIAL, monitor_epochs=NUM_TRIAL, update_interval=1,
            components='all', epochs_before_pred=NUM_TRIAL)

for i in range(NUM_TRIAL):
    tracker.epoch_start()

    time.sleep(10)
    tracker.epoch_end()

tracker.stop()