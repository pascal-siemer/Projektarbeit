import asyncio


class Debouncer:

    def __init__(self, delay_in_seconds):
        self.task: asyncio.Task | None = None
        self.delay_in_seconds = delay_in_seconds

    def debounce(self, coro):
        try:
            if self.task is not None:
                self.task.cancel()
            self.task = self.wait_then_execute(coro)
        except Exception:
            pass

    async def wait_then_execute(self, coro):
        await asyncio.sleep(self.delay_in_seconds)
        await asyncio.create_task(coro)
