# URLCheck

![GitHub last commit](https://img.shields.io/github/last-commit/thehackermonk/URLCheck?style=flat-square) ![GitHub](https://img.shields.io/github/license/thehackermonk/URLCheck?style=flat-square) ![GitHub issues](https://img.shields.io/github/issues/thehackermonk/URLCheck?style=flat-square) ![GitHub language count](https://img.shields.io/github/languages/count/thehackermonk/URLCheck?style=flat-square) ![GitHub top language](https://img.shields.io/github/languages/top/thehackermonk/URLCheck?logo=python&style=flat-square) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/thehackermonk/URLCheck?style=flat-square) ![Twitter Follow](https://img.shields.io/twitter/follow/thehackermonk?style=flat-square)

To take a list of domains (URLs) and check if they are accessible from the browser.

## Basic Usage
URLCheck accepts line-delimited URLs in a text file. This script will show you if the URL is accessible or not in the terminal and also print the list of all the accessible URLs to a new text file.

### Input File
> example.com
>
> example.net

### Usage example
> ▶ python urlcheck.py
>
> Enter path of the input file:
>
> ▶ /home/Users/Bug Bounty/domains.txt
>
> Success: https://example.com
>
> Success: http://example.com
>
> Error: https://example.net
>
> Error: http://example.net
>

## Extra Probes
Protocols are not mandatory. You can include or exclude them in the URL.
Both https://example.com and example.com will work fine.
