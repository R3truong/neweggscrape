import requests
from bs4 import BeautifulSoup
import re

# Implementation of BeautifulSoup and Requests modules to scrape newegg's event sale 
# for prices that are comparable to a given input of minimum comparison


#Header so my request is fulfilled
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

#User input for wanted discount
max_discount = input("Write your minimum discount in percentage, such as 50% or 30%\n")
max_discount = int(max_discount.strip('%'))

discount_html = requests.get('https://www.newegg.com/Techtober/EventSaleStore/ID-1133', headers=headers).text

soup = BeautifulSoup(discount_html, 'lxml')

#Iterate through each item, receive item variables
discounted_goods = soup.find_all('div', class_='goods-container')
for good in discounted_goods:
    good_name = good.find('div', class_='goods-info').find('a', class_='goods-title').text
    discount = good.find('div', class_='goods-info').find('div', class_='tag-list')
    goods_cost_dollars = good.find('div', class_='goods-info').find('div', class_='goods-price').find('span', class_='goods-price-value').strong.text
    goods_cost_cents = good.find('div', class_='goods-info').find('div', class_='goods-price').find('span', class_='goods-price-value').sup.text
    #Conditional in the case if there is not a discount, if there is turn the discount amount into a comparable integer
    if(discount is not None):
        discount = discount.div.div.text
        discount_expression = re.search(r'\d+', discount)
        discount_comp = int(discount_expression.group())
        #Compare discount to your inputted discount minimum and print out available products
        if(discount_comp >= max_discount):
            print('Name: ',good_name)
            print('Discount: ',discount)
            print('Cost: ${}{:02}'.format(goods_cost_dollars, goods_cost_cents))
            print('')
            print('')
            print('________________________________________________________________________________________________')
