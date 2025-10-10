import scrapy

class LightnewparsSpider(scrapy.Spider):
    name = "lightnewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/kazan/category/svet"]

    def parse(self, response):
        # Находим все карточки товаров на странице
        lights = response.css('div.WdR1o')

        # Перебираем найденные элементы и извлекаем данные
        for light in lights:
            yield {
                # Название товара
                'name': light.css('div.lsooF span::text').get(),
                # Цена
                'price': light.css('div.pY3d2 span::text').get(),
                # Ссылка на товар (делаем абсолютной)
                'url': response.urljoin(light.css('a::attr(href)').get())
            }
