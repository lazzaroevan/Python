import pywikibot as wiki
site = wiki.Site()
mammals_page = wiki.Page(site,u'donkey')
text = mammals_page.text
print(text.title())