from re import search
import bs4 as BeautifulSoup


#### Initialize Software url locations
# Viper 4
Url_viper = "https://portal.ravenprecision.com/ProductDocumentation/Category?categoryId=18"
# RS1
Url_rs1 = "https://portal.ravenprecision.com/ProductDocumentation/Category?categoryId=40"
# Hawkeye
Url_hawk = "https://portal.ravenprecision.com/ProductDocumentation/Category?categoryId=56"
# Hawkeye 2
Url_hawk2 = "https://portal.ravenprecision.com/ProductDocumentation/Category?categoryId=199"
# XRT
Url_xrt = "https://portal.ravenprecision.com/ProductDocumentation/Category?categoryId=195"

#### Request user to input current version


#### Add input to string

current_ver = 0

#### Get latest version from website

latest_ver = 0


#### Compare versions

##### IF latest_ver != current_ver
####    THEN open website to download latest ver for testing
##### ELSE output that it is up to date