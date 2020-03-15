import scrapy

from etl.common import Language
from scraper.item_builder import ItemBuilder

from . import SpiderName


class Icetex(scrapy.Spider):
    name = SpiderName.ICETEX.value

    allowed_domains = ['icetex.gov.co']

    start_urls = [
        'https://www.icetex.gov.co/SIORI_WEB/Convocatorias.aspx?aplicacion=1&vigente=true',
    ]

    def parse(self, response):
        return self.visit_menu(response)

    def visit_menu(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formid='form1',
            formdata={
                'RBLOpcionBuscar': 'Todas',
                '__EVENTTARGET': 'RBLOpcionBuscar$2',
                '__EVENTARGUMENT': '',
                '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first(),
            },
            callback=self.visit_first_page,
        )

    def visit_first_page(self, response):
        yield from self.visit_preview_page(response)
        yield from self.follow_pagination(response)

    def visit_preview_page(self, response):
        details_page_link = response.css(
            'table#GVConvocatorias > tr > td > a::attr(href)').re(",'(.+)'")
        for link in details_page_link:
            yield scrapy.FormRequest.from_response(
                response,
                formid='form1',
                formdata={
                    '__EVENTTARGET': 'GVConvocatorias',
                    '__EVENTARGUMENT': link,
                },
                callback=self.parse_item,
            )

    def follow_pagination(self, response):
        next_page_links = response.css('table#GVConvocatorias table a::attr(href)').re(",'(.+)'")
        for link in next_page_links:
            yield scrapy.FormRequest.from_response(
                response,
                formid='form1',
                formdata={
                    '__EVENTTARGET': 'GVConvocatorias',
                    '__EVENTARGUMENT': link,
                },
                callback=self.visit_preview_page,
            )

    def parse_item(self, response):
        item = ItemBuilder.from_spider(self)

        item.add_language(Language.SPANISH)
        item.add_name(response.css('#LblInfoPrograma::text').get())
        item.add_original_id(response.css('#LblInfoConvocatoria::text').get())
        item.add_url(response.request.url)
        item.add_description(response.css('#LblInfoPerfilAspirante::text').get())
        item.add_deadline(response.css('#LblInfoFechaRecepcion::text').get())
        item.add_country(response.css('#LblInfoPais::text').get())
        item.add_funding_type(response.css(
            '#GVNumeroBecas .celdaOscura2 td:nth-child(3)::text').get())

        return item.build()
