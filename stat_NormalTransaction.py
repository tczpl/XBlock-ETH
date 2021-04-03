import zipfile

fileDir = "./"	
files = [
	"0to999999_NormalTransaction",
	"1000000to1999999_NormalTransaction",
	"2000000to2999999_NormalTransaction",
	"3000000to3999999_NormalTransaction",
	"4000000to4999999_NormalTransaction",
	"5000000to5999999_NormalTransaction",
	"6000000to6999999_NormalTransaction",
	"7000000to7999999_NormalTransaction",
	"8000000to8999999_NormalTransaction",
	"9000000to9999999_NormalTransaction",
	"10000000to10999999_NormalTransaction",
	"11000000to11999999_NormalTransaction"
]	

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

		# blockNumber,timestamp,transactionHash,from,to,creates,value,gasLimit,gasPrice,gasUsed,callingFunction,isError
		blockNumber 	= int(oneArray[0])
		timestamp		= int(oneArray[1])
		transactionHash = oneArray[2]
		sender			= oneArray[3]
		to				= oneArray[4]
		creates			= oneArray[5]
		value			= int(oneArray[6])
		gasLimit		= int(oneArray[7])
		gasPrice		= int(oneArray[8])
		gasUsed			= int(oneArray[9])
		callingFunction	= oneArray[10]
		isError			= ToStr(oneArray[11])

		total_fees += gasPrice*gasUsed
		tx_count += 1	
		if tx_count % 100000 == 0:
			print(tx_count, total_fees/1e+18)	
		oneLine = theCSV.readline().decode("utf-8").strip()	

	theCSV.close()	
	theZIP.close()	

print(tx_count, total_fees/1e+18)
# 1038965664 2890656.834657312