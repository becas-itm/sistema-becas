import scrapy
from scrapy.shell import inspect_response

from etl.common import Language
from etl.common.entities import EntityName

from scraper.item_builder import ItemBuilder


class Daad(scrapy.Spider):
    name = EntityName.DAAD.value

    allowed_domains = ['www.daad.co']

    start_urls = ['https://www.daad.co/es/becas/buscador-de-becas/']

    def parse(self, response):
        yield from self.visit_current_page(response)

    def visit_current_page(self, response):
        for scholarship in response.css('#main > ul > li'):
            details_link = scholarship.css('h3 > a::attr(href)').get()
            yield response.follow(details_link, callback=self.parse_item)

        yield self.visit_next_page(response)

    def visit_next_page(self, response):
        next_page = '#main > nav > ul.pagination.hidden-md.hidden-lg > li:nth-child(2):not(.disabled) > a::attr(href)'  # noqa: E501
        next_page = response.css(next_page).get()
        if next_page:
            return response.follow(next_page, callback=self.visit_current_page)

    def parse_item(self, response):
        return ItemBuilder.from_spider(self) \
            .add_language(Language.ENGLISH) \
            .add_name(response.css('.scholarship-detail-header > h2::text').get()) \
            .add_academic_level(self.prepare_academic_level(response.css('.scholarship-sidebar > div > dl > dd:nth-child(2)::text').extract()))\
            .add_url(response.request.url) \
            .add_description(response.css('#overview > div::text').get()) \
            .build()

    def prepare_academic_level(self, levels):
        return ';'.join([level.strip() for level in levels if level.strip()])
