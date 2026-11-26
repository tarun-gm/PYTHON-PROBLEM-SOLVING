import heapq
import itertools
import time


class TaskScheduler:
    def __init__(self):
        self.queue = []
        self.sequence = itertools.count()

    def schedule(self, delay_seconds, callback, *args, **kwargs):
        run_at = time.monotonic() + max(0, delay_seconds)
        task_id = next(self.sequence)
        heapq.heappush(self.queue, (run_at, task_id, callback, args, kwargs))
        return task_id

    def run(self, wait=True):
        while self.queue:
            run_at, task_id, callback, args, kwargs = self.queue[0]
            remaining = run_at - time.monotonic()
            if remaining > 0:
                if not wait:
                    break
                time.sleep(remaining)
            heapq.heappop(self.queue)
            callback(*args, **kwargs)


if __name__ == "__main__":
    scheduler = TaskScheduler()
    scheduler.schedule(1, print, "First task")
    scheduler.schedule(2, print, "Second task")
    scheduler.run()
