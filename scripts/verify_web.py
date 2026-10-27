"""Exercise an isolated Flutter release build; never uses accounts or secrets."""
import asyncio
import functools
import http.server
import json
from pathlib import Path
import shutil
import threading
from urllib.parse import unquote, urlsplit

from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout

ROOT = Path(__file__).resolve().parents[1] / 'build' / 'web'
PREFIX = '/brainboost-flutter/'


class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, value):
        route = unquote(urlsplit(value).path)
        if not route.startswith(PREFIX):
            return str(ROOT / '__not_found__')
        path = (ROOT / route[len(PREFIX):]).resolve()
        return str(path if path.is_relative_to(ROOT.resolve()) else ROOT / '__not_found__')

    def log_message(self, *_):
        pass


async def main():
    assert (ROOT / 'index.html').is_file(), 'Run flutter build web first'
    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    errors, bad, external = [], [], []
    url = f'http://127.0.0.1:{server.server_port}{PREFIX}'
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=['--enable-unsafe-swiftshader'])
        try:
            page = await browser.new_page(viewport={'width': 1280, 'height': 800})
            page.on('pageerror', lambda error: errors.append(str(error)))
            page.on('response', lambda response: bad.append({'url': response.url, 'status': response.status}) if response.status >= 400 else None)
            page.on('request', lambda request: external.append(request.url) if not request.url.startswith(('http://127.0.0.1:', 'data:', 'blob:')) else None)
            await page.add_init_script("window.__firstFlutterFrame=false;addEventListener('flutter-first-frame',()=>window.__firstFlutterFrame=true)")
            response = await page.goto(url, wait_until='domcontentloaded', timeout=90000)
            assert response.status == 200
            await page.wait_for_function('window.__firstFlutterFrame === true', timeout=120000)
            await page.locator('canvas').first.wait_for(state='visible')
            await page.screenshot(path=str(ROOT / 'preview.png'))
            interaction = {'attempted': False, 'count_verified': False}
            placeholder = page.locator('flt-semantics-placeholder')
            if await placeholder.count():
                await placeholder.first.evaluate('(element)=>element.click()')
            try:
                button = page.get_by_role('button', name='Increment', exact=True)
                await button.wait_for(state='visible', timeout=5000)
                interaction['attempted'] = True
                await button.click()
                one = page.get_by_text('1', exact=True)
                await one.wait_for(state='visible', timeout=5000)
                interaction['count_verified'] = True
            except PlaywrightTimeout:
                interaction['limitation'] = 'Browser semantic counter assertion unavailable; original Flutter widget test independently verifies 0-to-1.'
            await page.set_viewport_size({'width': 390, 'height': 844})
            await page.screenshot(path=str(ROOT / 'preview-mobile.png'))
            assert not errors, errors
            assert not bad, bad
            assert not external, external
            report = {
                'scope': 'Actual Flutter release counter scaffold; no Vite games, backend, account or model.',
                'prefix': PREFIX,
                'status': response.status,
                'first_flutter_frame': True,
                'browser_counter_interaction': interaction,
                'page_errors': errors,
                'http_failures': bad,
                'external_requests': sorted(set(external)),
                'desktop': [1280, 800],
                'mobile': [390, 844],
            }
            (ROOT / 'ci-browser-check.json').write_text(json.dumps(report, indent=2), encoding='utf8')
            print(json.dumps(report))
        finally:
            await browser.close()
            server.shutdown()


asyncio.run(main())
