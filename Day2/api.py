import urllib2
import json
import optparse


def main():
	battle_api =  'bsff6mqueszapzzt3v396hcwuhjrhcbx'

	url = 'https://us.api.battle.net/wow/achievement/2144?locale=en_US&apikey=bsff6mqueszapzzt3v396hcwuhjrhcbx'
	json_obj = urllib2.urlopen(url)

	data = json.load(json_obj)

	parse = optparse.OptionParser()
	parse.add_option(api = data, help = "prints out the data consumed"
	opt,args = parse.parse_args()
	print "DATA COLLECT: " + opt.api

if __name__ == "__main__":
	main()
