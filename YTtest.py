from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


class Test_youtube_player(unittest.TestCase):

    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument('--start-maximized')
        self.browser = webdriver.Chrome(chrome_options=option)
        self.browser.get("https://www.youtube.com/watch?v=BqO0dFxUMtI")

    def test_setings(self):

        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//BUTTON[@class="ytp-button ytp-settings-button"]'))
        )
        ActionChains(self.browser).click(element).perform()

        temp_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//BUTTON[@class="ytp-play-button ytp-button"]'))
        )
        ActionChains(self.browser).move_to_element(temp_element).perform()

        element = self.browser.find_element(By.XPATH,
                                            '//BUTTON[@class="ytp-button ytp-settings-button"]').get_attribute(
            "aria-expanded")
        assert "true" in element

    def test_close_caption(self):

        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//BUTTON[@class="ytp-subtitles-button ytp-button"]'))
        )
        ActionChains(self.browser).click(element).perform()

        element = self.browser.find_element(By.XPATH,
                                            '//BUTTON[@class="ytp-subtitles-button ytp-button"]').get_attribute(
            "aria-pressed")

        if element is None:
            print("NoSuchElementFound!")
        else:
            assert "true" in element

    def test_play_button(self):

        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//BUTTON[@class="ytp-play-button ytp-button"]'))
        )
        left = ActionChains(self.browser).click(element)
        left.perform()
        element = self.browser.find_element(By.XPATH, '//BUTTON[@class="ytp-play-button ytp-button"]').get_attribute("aria-label")
        assert "Play" in element

    def test_mute_audio(self):

        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//BUTTON[@class="ytp-mute-button ytp-button"]'))
        )
        ActionChains(self.browser).click(element).perform()

        temp_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//BUTTON[@class="ytp-play-button ytp-button"]'))
        )
        ActionChains(self.browser).move_to_element(temp_element).perform()

        element = self.browser.find_element(By.XPATH,
                                                '//BUTTON[@class="ytp-mute-button ytp-button"]').get_attribute("title")
        time.sleep(2)
        print(element)
        assert "Unmute" in element

    def test_pause_button_and_right_page_presence(self):

        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//BUTTON[@class="ytp-play-button ytp-button"]'))
        )
        ActionChains(self.browser).click(element).perform()

        element = self.browser.find_element(By.XPATH,
                                                '//BUTTON[@class="ytp-play-button ytp-button"]').get_attribute("aria-label")
        time.sleep(5)
        assert "Play" in element
        assert "ASMR: Visual Sampler (no sound, only visuals, relaxing, calming, ASMR) - YouTube" in self.browser.title

    def test_next_button(self):

        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//A[@class="ytp-next-button ytp-button"]'))
        )
        time.sleep(2)
        ActionChains(self.browser).click(element).perform()

        time.sleep(5)
        print(self.browser.title)
        assert "[ASMR] Zen Garden Sleep AID (decreasing brightness) 45 min - NO TALKING - YouTube" in self.browser.title

    def test_teatar_mode(self):

        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//BUTTON[@class="ytp-size-button ytp-button"]'))
        )
        time.sleep(2)
        ActionChains(self.browser).click(element).perform()

        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//BUTTON[@class="ytp-play-button ytp-button"]'))
        )
        ActionChains(self.browser).click(element).perform()

        element = self.browser.find_element_by_xpath('//BUTTON[@class="ytp-size-button ytp-button"]').get_attribute(
            "title")
        time.sleep(2)
        assert "Default view" in element

    def test_Full_screen(self):

        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//BUTTON[@class="ytp-fullscreen-button ytp-button"]'))
        )
        ActionChains(self.browser).click(element).perform()

        title_check = self.browser.find_element(By.XPATH,
                                                    '//BUTTON[@class="ytp-fullscreen-button ytp-button"]').get_attribute(
            "title")
        assert "Exit full screen" in title_check

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
