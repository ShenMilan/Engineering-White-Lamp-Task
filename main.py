from bs4 import BeautifulSoup
import requests

url_1 = "https://coinmarketcap.com/currencies/uniswap/"
url_1A = "https://etherscan.io/token/0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984" # for information not found in url_1
url_2 = "https://coinmarketcap.com/currencies/internet-computer/"
url_3 = "https://coinmarketcap.com/currencies/lido-dao/"

for i in range(3):
    if (i == 0):
        url = url_1
        urlA = url_1A 
    elif (i == 1):
        url = url_2
    elif (i == 2):
        url = url_3

    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    html_text_A = requests.get(urlA).text
    soup_A = BeautifulSoup(html_text_A, 'lxml')

    dao_name = soup.find('span', class_ = 'coin-name-pc').text
    dao_price = soup.find('span', class_ = 'sc-f70bb44c-0 jxpCgO base-text').text
    dao_market_cap = soup.find('dd', class_ = 'sc-f70bb44c-0 bCgkcs base-text').text.replace('%', '% ')
    dao_volume = soup.find('dd', class_ = 'sc-f70bb44c-0 bCgkcs base-text').text.replace('%', '% ')
    # dao_holders = soup_A.find('div', class_ = 'd-flex flex-wrap gap-2').text
    # ^^^ this doesn't work

    print(f'''
        DAO Name: {dao_name}
            Current Price: {dao_price}
            Market Cap: {dao_market_cap}
            Holders: #
        
        ''')
    # Holders is a placeholder for when I figure out how to scrape the div from the website
    # since the div has no class or id so I don't know how to .find it


