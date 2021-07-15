# URLCheck

![GitHub last commit](https://img.shields.io/github/last-commit/thehackermonk/URLCheck?style=flat-square) ![GitHub](https://img.shields.io/github/license/thehackermonk/URLCheck?style=flat-square) ![GitHub issues](https://img.shields.io/github/issues/thehackermonk/URLCheck?style=flat-square) ![GitHub language count](https://img.shields.io/github/languages/count/thehackermonk/URLCheck?style=flat-square) ![GitHub top language](https://img.shields.io/github/languages/top/thehackermonk/URLCheck?logo=python&style=flat-square) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/thehackermonk/URLCheck?style=flat-square) ![Twitter Follow](https://img.shields.io/twitter/follow/thehackermonk?style=flat-square)

URLCheck tests which of the URLs are accessible.

## Basic Usage
URLCheck accepts a single URL or multiple URLs (line-delimited in a text file). This script will show you if the URL(s) is accessible or not in the terminal. You can also print the URLs which are working to an output file.

### Command
> python urlcheck.py -u `<domain>` -p http -o

### Usage example
> ▶ python urlcheck.py -u examplecom -p http
>Success:  http://example.com

> ▶ python urlcheck.py -l '/home/thehackermonk/domains.txt' --fullcheck
> Success:  https://example.com
> Success:  http://example.com
> Error: ftp://example.com
> Success:  https://example.net
> Success:  http://example.net
> Error: ftp://example.net

### Input File
> example.com
>
> example.net

## Extra Probes
Do not include protocols directly into the URL.
google.com ✅
https://google.com ❌
