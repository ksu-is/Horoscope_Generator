import requests
from bs4 import BeautifulSoup
  
## define function using parameters day & zodiac_sign
def horoscope(zodiac_sign: int, day: str) -> str:
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    )
    soup = BeautifulSoup(requests.get(url).content,
                         "html.parser") ## call URL for output


    return soup.find("div", class_="main-horoscope").p.text
  
  
if __name__ == "__main__": ## give program zodiac signs
    dic = {'Aries': 1, 'Taurus': 2, 'Gemini': 3,
           'Cancer': 4, 'Leo': 5, 'Virgo': 6,
           'Libra': 7, 'Scorpio': 8, 'Sagittarius': 9,
           'Capricorn': 10, 'Aquarius': 11, 'Pisces': 12}
      
    print('Choose your zodiac sign from below list: \n', ## statement to receive input
          '[Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces]')
  
    zodiac_sign = dic[input("Input your zodiac sign: ")] ## input choice

    print("What day would you like your horoscope for? \n", 
          "Yesterday\n", "Today\n", "Tomorrow\n") ## second choice statement to receive input
  
    day = input("Input the day: ").lower() ## input choice
    horoscope_text = horoscope(zodiac_sign, day) ## format date & horoscope output into a single str
    print(horoscope_text) ## prints horoscope output