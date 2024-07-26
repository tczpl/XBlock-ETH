import zipfile

fileDir = "./"	
files = [
	"0to999999_InternalTransaction",
	"1000000to1999999_InternalTransaction",
	"2000000to2999999_InternalTransaction",
	"3000000to3999999_InternalTransaction",
	"4000000to4999999_InternalTransaction",
	"5000000to5999999_InternalTransaction",
	"6000000to6999999_InternalTransaction",
	"7000000to7999999_InternalTransaction",
	"8000000to8999999_InternalTransaction",
	"9000000to9999999_InternalTransaction",
	"10000000to10999999_InternalTransaction",
	"11000000to11999999_InternalTransaction",
	"12000000to12999999_InternalTransaction",
	"12000000to12999999_InternalTransaction",
	"13000000to13249999_InternalTransaction",
	"13250000to13499999_InternalTransaction",
	"13500000to13749999_InternalTransaction",
	"13750000to13999999_InternalTransaction",
	"14000000to14249999_InternalTransaction",
	"14250000to14499999_InternalTransaction",
	"14500000to14749999_InternalTransaction",
	"14750000to14999999_InternalTransaction",
	"15000000to15249999_InternalTransaction",
	"15250000to15499999_InternalTransaction",
	"15500000to15749999_InternalTransaction",
	"15750000to15999999_InternalTransaction",
	"16000000to16249999_InternalTransaction",
	"16250000to16499999_InternalTransaction",
	"16500000to16749999_InternalTransaction",
	"16750000to16999999_InternalTransaction",
	"17000000to17249999_InternalTransaction",
	"17250000to17499999_InternalTransaction",
    "17500000to17749999_InternalTransaction",
    "17750000to17999999_InternalTransaction",
    "18000000to18249999_InternalTransaction",
    "18250000to18499999_InternalTransaction",
    "18500000to18749999_InternalTransaction",
    "18750000to18999999_InternalTransaction",
    "19000000to19249999_InternalTransaction"
]	

def ToStr(str):
	return None if str=="None" else str

tx_count = 0
err_count = 0

for file in files:
	print(file)	
	theZIP = zipfile.ZipFile(fileDir+file+".zip", 'r')
	theCSV = theZIP.open(file+".csv")	
	head = theCSV.readline()	

	oneLine = theCSV.readline().decode("utf-8").strip()
	while (oneLine!=""):
		oneArray = oneLine.split(",")

		# blockNumber,timestamp,transactionHash,typeTraceAddress,from,to,fromIsContract,toIsContract,value,callingFunction,isError
		blockNumber			= int(oneArray[0])
		timestamp			= int(oneArray[1])
		transactionHash		= oneArray[2]
		typeTraceAddress	= oneArray[3]
		sender				= oneArray[4]
		to					= oneArray[5]
		fromIsContract		= int(oneArray[6])
		toIsContract		= int(oneArray[7])
		value				= int(oneArray[8])
		callingFunction		= oneArray[9]
		isError				= ToStr(oneArray[10])

		tx_count += 1
		if (isError!=None):
			err_count += 1
		if(tx_count%100000==0):
			print(blockNumber, tx_count, err_count)
		oneLine = theCSV.readline().decode("utf-8").strip()	

	theCSV.close()
	theZIP.close()

print(tx_count, err_count)
# 6713308333 436267119
