import asyncio
import json

import aiohttp as aiohttp
from bs4 import BeautifulSoup
from lxml import html

from Lecture_12_Concurrency_homework.company import Company


def format_number(x):
    return x.strip().replace(",", "")


async def get_exchange_rate():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://www.cbr.ru/scripts/XML_daily.asp") as response:
            response = await response.text()
            soup_cbr = BeautifulSoup(response, features="html.parser")
            dollar_currency = next(
                filter(lambda x: x.attrs["id"] == "R01235", soup_cbr.find_all("valute"))
            )
            return float(dollar_currency.find("value").text.replace(",", "."))


async def get_page(session, url):
    async with session.get(url) as resp:
        return await resp.text()


async def get_companies_pages():
    responses = []
    sp_main_url = "https://markets.businessinsider.com/index/components/s&p_500?p="
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, 11):
            tasks.append(asyncio.ensure_future(get_page(session, sp_main_url + str(i))))
        pages = await asyncio.gather(*tasks)
        for page in pages:
            responses.append(page)
    return responses


async def get_company(session, tr, rate):
    cost = float(format_number(tr.contents[3].contents[0])) * rate
    year_growth = tr.findAll("span").pop().text.replace("%", "")
    company_link = "https://markets.businessinsider.com" + tr.find("a")["href"]
    async with session.get(company_link) as resp:
        response = await resp.text()
        soup_company = BeautifulSoup(response, features="html.parser")
        name = soup_company.select_one("span.price-section__label").text.strip()
        code = (
            format_number(soup_company.select_one(".price-section .price-section__category span").text)
        )
        tree = html.fromstring(response)
        try:
            p_e = float(format_number(tree.xpath("//div[text()='P/E Ratio']/..")[0].text))
            low = float(format_number(tree.xpath("//div[text()='52 Week Low']/..")[0].text))
            high = float(format_number(tree.xpath("//div[text()='52 Week High']/..")[0].text))
        except IndexError:
            p_e = 0
            income = 0
        else:
            income = (high - low) / low * 100
        return Company(name, cost, code, p_e, year_growth, income)


async def get_companies(pages, exchange_rate):
    companies = []
    for page in pages:
        soup = BeautifulSoup(page, features="html.parser")
        table_lines = soup.find_all("tr")
        table_lines.pop(0)
        async with aiohttp.ClientSession() as session:
            tasks = []
            for line in table_lines:
                tasks.append(asyncio.ensure_future(get_company(session, line, exchange_rate)))
            companies_response = await asyncio.gather(*tasks)
            for company in companies_response:
                companies.append(company)
    return companies


def write_top_to_json(file_name, companies, field_name, get_field, is_reverse):
    top_companies = sorted(companies, key=get_field, reverse=is_reverse)[:10]
    with open(file_name, mode="w") as file_output:
        companies_json = []
        for company in top_companies:
            company_dict = {"code": company.code, "name": company.name, field_name: get_field(company)}
            companies_json.append(company_dict)
        json.dump(companies_json, file_output)


ioloop = asyncio.get_event_loop()
exchange_rate = ioloop.run_until_complete(get_exchange_rate())
companies_pages = ioloop.run_until_complete(get_companies_pages())
companies = ioloop.run_until_complete(get_companies(companies_pages, exchange_rate))

write_top_to_json("max_cost.json", companies, "price", lambda x: x.price, True)
write_top_to_json("min_pe.json", companies, "p/e", lambda x: x.p_e, False)
write_top_to_json("max_growth.json", companies, "growth", lambda x: x.year_growth, True)
write_top_to_json("max_income.json", companies, "potential income", lambda x: x.income, True)
