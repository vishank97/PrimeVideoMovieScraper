from prompt_toolkit.keys import Keys
from selenium import webdriver
from flask_test import *

user_name = 'abc@gmail.com' # enter your email ID
password = 'your_actual_password' # enter your password
see_more_urls = []
movie_urls = []


def scroll(driver, timeout):
    director = ""
    starring = ""
    genres = ""
    subtitles = ""
    audio_languages = ""
    supporting_actors = ""
    producers = ""
    studio = ""
    amr = ""
    scroll_pause_time = timeout
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        break
        if new_height == last_height:
            break
    movie_urls_tags = []
    movie_urls_elements = driver.find_elements_by_class_name("av-beard-title-link")
    for movie in movie_urls_elements:
        movie_urls_tags.append(movie.get_attribute("href"))
    for movietag in movie_urls_tags:
        driver.get(movietag)
        time.sleep(2)

        title = driver.find_element_by_class_name('_1GTSsh').text
        element = driver.find_element_by_class_name('_3qsVvm')
        description = element.text
        attributes = driver.find_elements_by_class_name("_1ONDJH")[0].find_elements_by_tag_name("dl")
        more_attributes = driver.find_elements_by_class_name("_1ONDJH")[1].find_elements_by_tag_name("dl")

        try:
            for atr in attributes:
                if (atr.find_element_by_tag_name("dt").text == "Director"):
                    director = str(atr.find_element_by_tag_name("dd").text)
                elif (atr.find_element_by_tag_name("dt").text == "Starring"):
                    starring = str(atr.find_element_by_tag_name("dd").text)
                elif (atr.find_element_by_tag_name("dt").text == "Genres"):
                    genres = str(atr.find_element_by_tag_name("dd").text)
                elif (atr.find_element_by_tag_name("dt").text == "Subtitles"):
                    subtitles = str(atr.find_element_by_tag_name("dd").text)
                elif (atr.find_element_by_tag_name("dt").text == "Audio languages"):
                    audio_languages = str(atr.find_element_by_tag_name("dd").text)
                print("attribute: " + str(atr.find_element_by_tag_name("dt").text) + " value" + str(
                    atr.find_element_by_tag_name("dd").text))
            for atr in more_attributes:
                if (atr.find_element_by_tag_name("dt").text == "Producers"):
                    producers = str(atr.find_element_by_tag_name("dd").text)
                elif (atr.find_element_by_tag_name("dt").text == "Studio"):
                    studio = str(atr.find_element_by_tag_name("dd").text)
                elif (atr.find_element_by_tag_name("dt").text == "Amazon Maturity Rating"):
                    amr = str(atr.find_element_by_tag_name("dd").text)
                elif (atr.find_element_by_tag_name("dt").text == "Supporting actors"):
                    supporting_actors = str(atr.find_element_by_tag_name("dd").text)
        except:
            traceback.print_stack(file=sys.stdout)
        # break
        movie = Movie(title=title, description=description, director=director,
                      starring=starring, genre=genres, subtitles=subtitles, audio_languages=audio_languages,
                      producer=producers,
                      studio=studio, amazon_maturity_rating=amr, supporting_actors=supporting_actors)
        add_data(movie)


def start():
    driver = webdriver.Chrome(executable_path="C:\\Users\\Vishank\\Selenium Web Drivers\\chromedriver.exe")
    driver.get("https://www.primevideo.com")
    element = driver.find_element_by_id("pv-nav-sign-in")
    element.click()
    element = driver.find_element_by_id("ap_email")
    element.send_keys(user_name)
    element = driver.find_element_by_id("ap_password")
    element.send_keys(password)
    element.send_keys(Keys.RETURN)
    element = driver.find_element_by_id("pv-nav-movies")
    element.click()
    scroll_pause_time = 2
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        break
        if new_height == last_height:
            break
    pages = driver.find_elements_by_css_selector("._4XLGta")
    print(pages)

    see_more_urls = []
    for page in pages:
        if page.text.startswith("Movies genres"):
            see_more_urls = page.find_elements_by_css_selector("._2LQvA6 a")

    temp = []
    for a in see_more_urls:
        if a.get_attribute("href") not in temp:
            temp.append(a.get_attribute("href"))

    for url in temp:
        time.sleep(2)
        driver.get(url)
        time.sleep(2)
        scroll(driver, 2)
    driver.quit()


def test_func():
    # movie = Movie(title="English Medium", description="Best Movie", director="Aaad,Bdda,sva,",
    #               starring="Kvnasun asindd, asiudn as", genre="Thriller", imdb_rating="9.8",
    #               duration="1hr 20mins", year_released="2020", age_category="13+",
    #               subtitles="English, Hindi", audio_languages="Hindi", producer="Vishank Anuj",
    #               studio="Pascal API", amazon_maturity_rating="13+", supporting_actors="jwin sas")
    movie = Movie(title="English Medium", description="Best Movie", director="Aaad,Bdda,sva,",
                  starring="Kvnasun asindd, asiudn as", genre="Thriller",
                  subtitles="English, Hindi", audio_languages="Hindi")
    add_data(movie)


if __name__ == '__main__':
    start()
