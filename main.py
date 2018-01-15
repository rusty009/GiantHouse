import BeautifulSoup
import urllib2
import lxml.html
import urlparse
import tldextract


outputfile = ''
rootUrl = ""


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

def extract_urls(rootUrl,Url):
	output = list()
	try:
		connection = urllib2.urlopen(Url, timeout=5)
		soup = BeautifulSoup.BeautifulSoup(connection)
		for link in soup.findAll("a"):
			link = link.get("href")
			if not is_absolute(link):
				if "mailto:" not in link:
					link = rootUrl+link
					output.append(link)
			else :
				output.append(link)
		return output
	except urllib2.URLError, e:
		return output

	    
	return output

def main(outputfile,rootUrl):
	outputFile = open(outputfile, 'w')
	fullUrlList 	= list()
	dedupUrlList 	= list()
	rootUrlList 	= list()

	rootUrlList.append(rootUrl)

	rootUrlDomain = get_domain(rootUrl)

	for link in rootUrlList:
		# get full list of urls
		fullUrlList = extract_urls(rootUrl,link)
		#dedupUrlList.extend(dedup(fullUrlList))
		for i in fullUrlList :
			if i not in dedupUrlList :
				dedupUrlList.append(i)
				outputFile.write("%s\n" % i)
				domain = get_domain(i)
				if domain == rootUrlDomain:
					print "found "+i+" in "+link
					rootUrlList.append(i)
	outputFile.close()


		

	
if __name__ == "__main__":
	main(outputfile,rootUrl)


	    