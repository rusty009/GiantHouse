import urllib
import lxml.html
import urlparse
import tldextract


outputfile = '/root/Desktop/scripts/output/output.txt'
rootUrl = "http://www.megacorpone.com/"


def is_absolute(url):
    return bool(urlparse.urlparse(url).netloc)
def get_domain(url):
	extracted = tldextract.extract(url)
	output = "{}.{}".format(extracted.domain, extracted.suffix)
	return output

def dedup(Urllist):
	output = []
	for i in Urllist :
		if i not in output :
			output.append(i)
	return output

def extract_urls(rootUrl):
	connection = urllib.urlopen(rootUrl)
	dom =  lxml.html.fromstring(connection.read())
	output = list()
	for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
	    
	    if not is_absolute(link):
	    	link = rootUrl+link
	    	output.append(link)
	    else :
	    	output.append(link)
	    
	return output

def main(outputfile,rootUrl):
	fullUrlList 	= list()
	dedupUrlList 	= list()
	rootUrlList 	= list()
	scannedUrls 	= list()

	rootUrlList.append(rootUrl)

	rootUrlDomain = get_domain(rootUrl)

	for link in rootUrlList:
		# get full list of urls
		print link
		fullUrlList = extract_urls(link)
		#dedupUrlList.extend(dedup(fullUrlList))
		for i in fullUrlList :
			if i not in dedupUrlList :
				dedupUrlList.append(i)
				domain = get_domain(i)
				if domain == rootUrlDomain:
					print "found "+i+" in "+link
					rootUrlList.append(i)

		
		#scannedUrls.append()
	
if __name__ == "__main__":
	main(outputfile,rootUrl)


	    