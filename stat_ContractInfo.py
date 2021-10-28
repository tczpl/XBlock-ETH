import zipfile

fileDir = "./"
files = [
	"0to999999_ContractInfo",
	"1000000to1999999_ContractInfo",
	"2000000to2999999_ContractInfo",
	"3000000to3999999_ContractInfo",
	"4000000to4999999_ContractInfo",
	"5000000to5999999_ContractInfo",
	"6000000to6999999_ContractInfo",
	"7000000to7999999_ContractInfo",
	"8000000to8999999_ContractInfo",
	"9000000to9999999_ContractInfo",
	"10000000to10999999_ContractInfo",
	"11000000to11999999_ContractInfo",
	"12000000to12999999_ContractInfo",
	"13000000to13249999_ContractInfo",
]

line_count = 0
creators = {}


for file in files:
	print(file)
	theZIP = zipfile.ZipFile(fileDir+file+".zip", 'r')
	theCSV = theZIP.open(file+".csv")
	head = theCSV.readline()

	oneLine = theCSV.readline().decode("utf-8").strip()
	while (oneLine!=""):
		oneArray = oneLine.split(",")
		
		# address,createdBlockNumber,createdTimestamp,createdTransactionHash,creator,creatorIsContract,createValue,creationCode,contractCode
		address					= oneArray[0]
		createdBlockNumber		= int(oneArray[1])
		createdTimestamp		= int(oneArray[2])
		createdTransactionHash	= oneArray[3]
		creator					= oneArray[4]
		creatorIsContract		= int(oneArray[5])
		createValue				= int(oneArray[6])
		creationCode			= oneArray[7]
		contractCode			= oneArray[8]

		line_count += 1
		creators[creator] = True

		oneLine = theCSV.readline().decode("utf-8").strip()
		if line_count % 100000 == 0:
			print(line_count, len(creators))

	theCSV.close()
	theZIP.close()

print(line_count, len(creators))
# 46784067 247929
