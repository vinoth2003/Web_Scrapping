from bs4 import BeautifulSoup
import requests

try:
    # Adding headers to simulate a Chrome browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36"
    }

    response = requests.get("https://www.imdb.com/chart/top/", headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup)  # Optional: To display the structured HTML content
        movie_info_blocks = soup.find_all('div', class_="sc-c8984160-3 jAYdME ipc-page-grid__item ipc-page-grid__item--span-2")
        for movie in movie_info_blocks:
            # print(movie.prettify())
            movie_name=movie.find('h3',class_="ipc-title__text").get_text(strip=True)
            movie_name=movie_name.replace('.',"").strip()
            movie_rating=movie.find('span',class_="ipc-rating-star--rating").get_text(strip=True)
            movie_year=movie.find('span',class_="sc-ab348ad5-8 cSWcJI cli-title-metadata-item").get_text(strip=True)
            print(movie_name,movie_rating,movie_year)

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

except Exception as e:
    print(f"Error: {e}")

