# No-Fuss Website Crawling and Extraction

This is a minimalistic but useful Python-based website crawler for Linux, and other OSs with `wget` available.

    wget + Python + PostgreSQL = win

## Motivation

There are dozens of frameworks for crawling and indexing the web, but they can require a lot of set up and tweaking. Examples of more approachable frameworks are [Scrapy](http://scrapy.org/) for Python and [Simplecrawler](https://www.npmjs.com/package/simplecrawler) for Node. At the other end of the scale is Apache's [Nutch](http://nutch.apache.org/) web crawler, backed by Hadoop.

This is an attempt to get something as _useful_ as the simple frameworks, while minimising lines of code and dependencies. The former require at least dozens if not hundreds of lines of code to achieve a typical pipeline:

1. Scrape a site for files matching a list of specific content types (e.g. `text/html`).
2. Filter these files based on a list of specific criteria (e.g. it looks like a legal document).
3. Persist the chosen files to indexed and replicated storage.

If you wish to follow this pipeline and keep things as straightforward as possible `py-simple-crawler` might be worth trying.

## Implementation

1. Wrap `wget` in a few lines of Python to add filtering and other post-processing. Hey presto a capable crawler.
2. For effortless persistence use the resulting function as a `plpythonu` procedure in PostgreSQL.
