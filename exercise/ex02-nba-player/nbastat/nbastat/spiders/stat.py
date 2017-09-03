# -*- coding: utf-8 -*-
import scrapy


class StatSpider(scrapy.Spider):
    name = 'stat'
    start_urls = ['http://www.foxsports.com/nba/stats?season=2014&category=SCORING&group=1&sort=3&time=0&pos=0&team=0&qual=1&sortOrder=0&opp=0&page=1']

    def parse(self, response):
        headers = response.css('table th a::text').extract()
        for player in response.css('table tbody tr'):
            result = {
                'fullname': player.css('.wisbb_fullPlayer span::text').extract_first(),
            }
            stat = player.css('td:not(:first-child)::text').extract()
            assert len(stat) == len(headers), '%d stat items but %d header items' % (len(stat), len(headers))
            for k, v in zip(headers, stat):
                result[k] = v
            yield result

        next_link = response.css('.wisbb_paginator a:last-child')
        if next_link and 'next' in next_link.css('::text').extract_first().lower():
            yield response.follow(next_link[0])
