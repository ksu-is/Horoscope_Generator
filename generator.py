import requests
from bs4 import BeautifulSoup
  
  
def horoscope(zodiac_sign: int, day: str) -> str:
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    )
    soup = BeautifulSoup(requests.get(url).content,
                         "html.parser")
  
    # print(soup.find("div", class_="main-horoscope").p.text)
    return soup.find("div", class_="main-horoscope").p.text
  
  
if __name__ == "__main__":
    dic = {'Aries': 1, 'Taurus': 2, 'Gemini': 3,
           'Cancer': 4, 'Leo': 5, 'Virgo': 6,
           'Libra': 7, 'Scorpio': 8, 'Sagittarius': 9,
           'Capricorn': 10, 'Aquarius': 11, 'Pisces': 12}
      
    print('Choose your zodiac sign from below list: \n',
          '[Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces]')
  
    zodiac_sign = dic[input("Input your zodiac sign: ")]

    print("What day would you like your horoscope for? \n",
          "Yesterday\n", "Today\n", "Tomorrow\n")
  
    day = input("Input the day: ").lower()
    horoscope_text = horoscope(zodiac_sign, day)
    print(horoscope_text)