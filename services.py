from playwright.async_api import async_playwright


class PlaywrightService:
    def __init__(self, playwright):
        self.playwright = playwright
        self.browser = None

    @classmethod
    async def create(cls):
        playwright = await async_playwright().start()
        return cls(playwright=playwright)

    async def start_browser(self, engine):
        if engine == "firefox":
            self.browser = await self.playwright.firefox.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
            return self
        elif engine == "webkit":
            self.browser = await self.playwright.webkit.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
            return self
        self.browser = await self.playwright.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        return self

    async def stop(self):
        if self.browser:
            await self.browser.close()
            self.browser = None

        await self.playwright.stop()

    async def new_context(self, **kwargs):
        return await self.browser.new_context(**kwargs)


async def remove_sec_ch_ua(route):
    headers = {k: v for k, v in route.request.headers.items() if not k.lower().startswith("sec-ch-ua")}
    await route.continue_(headers=headers)
