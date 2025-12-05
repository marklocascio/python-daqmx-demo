import logging

from nidaqmx.errors import DaqError
from nidaqmx.system.storage import PersistedTask
from nidaqmx.constants import AcquisitionType, WAIT_INFINITELY


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def main(task_name, sample_rate=1000, acq_rate=2, buffer_multiplier=10):
    samples_per_acq = int(sample_rate / acq_rate)
    buffer_size = samples_per_acq * buffer_multiplier
    task = None
    
    try:
        task = PersistedTask(task_name).load()
    except DaqError:
        logger.error("Task '{0}' doesn't exist".format(task_name))
        return False

    task.timing.cfg_samp_clk_timing(sample_rate,
                                    sample_mode=AcquisitionType.CONTINUOUS,
                                    samps_per_chan=buffer_size)

    logger.info(f"Starting task '{task_name}'")
    task.start()
    all_data = []
    while True:
        new_data = task.read(samples_per_acq, timeout=WAIT_INFINITELY)
        all_data = all_data + new_data

        logger.debug(f"Acquired {len(new_data)} samples")

        abs_zero = -273.15
        if max(new_data) > abs_zero:
            logger.info(f"Temperature finally got above absolute zero. Phew!")
            break

    logger.info(f"Stopping task '{task_name}'")
    task.stop()
    task.close()


if __name__ == "__main__":
    main("MyTemperatureTask")
