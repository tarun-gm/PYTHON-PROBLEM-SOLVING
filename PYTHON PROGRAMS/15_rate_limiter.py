import time
from collections import defaultdict, deque


class SlidingWindowRateLimiter:
    def __init__(self, limit, window_seconds):
        if limit < 1 or window_seconds <= 0:
            raise ValueError("limit and window must be positive")
        self.limit = limit
        self.window = window_seconds
        self.events = defaultdict(deque)

    def allow(self, client_id, now=None):
        now = time.monotonic() if now is None else now
        events = self.events[client_id]
        while events and events[0] <= now - self.window:
            events.popleft()
        if len(events) >= self.limit:
            return False
        events.append(now)
        return True


if __name__ == "__main__":
    limiter = SlidingWindowRateLimiter(3, 10)
    for moment in (1, 2, 3, 4, 12):
        print(moment, limiter.allow("client-1", moment))
