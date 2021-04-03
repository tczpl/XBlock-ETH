import zipfile

fileDir = "./"
files = [
	"0to999999_ERC721Transaction",
	"1000000to1999999_ERC721Transaction",
	"2000000to2999999_ERC721Transaction",
	"3000000to3999999_ERC721Transaction",
	"4000000to4999999_ERC721Transaction",
	"5000000to5999999_ERC721Transaction",
	"6000000to6999999_ERC721Transaction",
	"7000000to7999999_ERC721Transaction",
	"8000000to8999999_ERC721Transaction",
	"9000000to9999999_ERC721Transaction",
	"10000000to10999999_ERC721Transaction",
	"11000000to11999999_ERC721Transaction"
]

tx_count = 0
tokens = {}

for file in files:
	print(file)
	theZIP = zipfile.ZipFile(fileDir+file+".zip", 'r')
	theCSV = theZIP.open(file+".csv")
	head = theCSV.readline()

	oneLine = theCSV.readline().decode("utf-8").strip()
	while (oneLine!=""):
		oneArray = oneLine.split(",")

		# blockNumber,timestamp,transactionHash,tokenAddress,from,to,fromIsContract,toIsContract,tokenId
		blockNumber			= int(oneArray[0])
		timestamp			= int(oneArray[1])
		transactionHash		= oneArray[2]
		tokenAddress 		= oneArray[3]
		sender		 		= oneArray[4]
		to		 			= oneArray[5]
		fromIsContract		= int(oneArray[6])
		toIsContract		= int(oneArray[7])
		tokenId				= int(oneArray[8])

		tx_count += 1
		tokens[tokenAddress] = True
		if(tx_count%100000==0):
			print(tx_count, len(tokens))
		oneLine = theCSV.readline().decode("utf-8").strip()

	theCSV.close()
	theZIP.close()

print(tx_count, len(tokens))
# 29634892 8153
