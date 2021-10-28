import zipfile

fileDir = "./"	
files = [
	"0to999999_BlockTransaction",
	"1000000to1999999_BlockTransaction",
	"2000000to2999999_BlockTransaction",
	"3000000to3999999_BlockTransaction",
	"4000000to4999999_BlockTransaction",
	"5000000to5999999_BlockTransaction",
	"6000000to6999999_BlockTransaction",
	"7000000to7999999_BlockTransaction",
	"8000000to8999999_BlockTransaction",
	"9000000to9999999_BlockTransaction",
	"10000000to10999999_BlockTransaction",
	"11000000to11999999_BlockTransaction",
	"12000000to12999999_BlockTransaction",
	"13000000to13249999_BlockTransaction",
]

def ToInt(str):
	return None if str=="None" else int(str)
def ToStr(str):
	return None if str=="None" else str

tx_count = 0
total_fees = 0

for file in files:
	print(file)	
	theZIP = zipfile.ZipFile(fileDir+file+".zip", 'r')
	theCSV = theZIP.open(file+".csv")
	head = theCSV.readline()

	oneLine = theCSV.readline().decode("utf-8").strip()	
	while (oneLine!=""):
		oneArray = oneLine.split(",")

		# blockNumber,timestamp,transactionHash,from,to,toCreate,fromIsContract,toIsContract,value,gasLimit,gasPrice,gasUsed,callingFunction,isError,eip2718type,baseFeePerGas,maxFeePerGas,maxPriorityFeePerGas

		blockNumber 		= int(oneArray[0])
		timestamp			= int(oneArray[1])
		transactionHash 	= oneArray[2]
		sender				= oneArray[3]
		to					= oneArray[4]
		toCreate			= oneArray[5]
		fromIsContract		= oneArray[6]
		toIsContract		= oneArray[7]
		value				= int(oneArray[8])
		gasLimit			= int(oneArray[9])
		gasPrice			= int(oneArray[10])
		gasUsed				= int(oneArray[11])
		callingFunction		= oneArray[12]
		isError				= ToStr(oneArray[13])
		eip2718type			= ToInt(oneArray[14])
		baseFeePerGas		= ToInt(oneArray[15])
		maxFeePerGas		= ToInt(oneArray[16])
		maxPriorityFeePerGas= ToInt(oneArray[17])

		total_fees += gasPrice*gasUsed
		tx_count += 1	
		if tx_count % 100000 == 0:
			print(tx_count, total_fees/1e+18)	
		oneLine = theCSV.readline().decode("utf-8").strip()	

	theCSV.close()	
	theZIP.close()	

print(tx_count, total_fees/1e+18)
# 1287874866 4401721.905001937