import zipfile

fileDir = "./"
files = [
	"0to999999_Block",
	"1000000to1999999_Block",
	"2000000to2999999_Block",
	"3000000to3999999_Block",
	"4000000to4999999_Block",
	"5000000to5999999_Block",
	"6000000to6999999_Block",
	"7000000to7999999_Block",
	"8000000to8999999_Block",
	"9000000to9999999_Block",
	"10000000to10999999_Block",
	"11000000to11999999_Block",
	"12000000to12999999_Block",
	"13000000to13249999_Block",
]

def ToInt(str):
	return None if str=="None" else int(str)
def ToFloat(str):
	return None if str=="None" else float(str)

line_count1 = 0
tx_count = 0
total_burnt = 0
total_tips = 0

line_count2 = 0
reward_count = 0

for file in files:
	print(file)
	theZIP = zipfile.ZipFile(fileDir+file+".zip", 'r')

	# Info
	theCSV = theZIP.open(file+"_Info.csv")
	head = theCSV.readline()

	oneLine = theCSV.readline().decode("utf-8").strip()
	while (oneLine!=""):
		oneArray = oneLine.split(",")

		# blockNumber,timestamp,size,difficulty,transactionCount,internalTxCntSimple,internalTxCntAdvanced,erc20TxCnt,erc721TxCnt,minerAddress,minerExtra,gasLimit,gasUsed,minGasPrice,maxGasPrice,avgGasPrice,txFees,baseFeePerGas,burntFees,tipsFees
		blockNumber 			= int(oneArray[0])
		timestamp				= int(oneArray[1])
		size					= int(oneArray[2])
		difficulty				= int(oneArray[3])
		transactionCount		= int(oneArray[4])
		internalTxCntSimple		= int(oneArray[5])
		internalTxCntAdvanced	= int(oneArray[6])
		erc20TxCnt				= int(oneArray[7])
		erc721TxCnt				= int(oneArray[8])
		minerAddress			= oneArray[9]
		minerExtra				= oneArray[10]
		gasLimit				= int(oneArray[11])
		gasUsed					= int(oneArray[12])
		minGasPrice				= ToInt(oneArray[13])
		maxGasPrice				= ToInt(oneArray[14])
		avgGasPrice				= ToFloat(oneArray[15])
		txFees					= ToInt(oneArray[16])
		baseFeePerGas			= ToInt(oneArray[17])
		burntFees				= ToInt(oneArray[18])
		tipsFees				= ToInt(oneArray[19])

		tx_count += transactionCount
		if blockNumber >= 12965000:
			total_burnt += burntFees
			total_tips += tipsFees
		line_count1 += 1
		oneLine = theCSV.readline().decode("utf-8").strip()
		if line_count1 % 100000 == 0 :
			print("Info", line_count1, tx_count)

	theCSV.close()

	# MinerReward
	theCSV = theZIP.open(file+"_MinerReward.csv")
	head = theCSV.readline()

	oneLine = theCSV.readline().decode("utf-8").strip()
	while (oneLine!=""):
		oneArray = oneLine.split(",")
		
		# blockNumber,timestamp,miner,reward
		blockNumber	= int(oneArray[0])
		timestamp	= int(oneArray[1])
		miner		= oneArray[2]
		reward		= int(oneArray[3])

		reward_count += reward
		line_count2 += 1
		oneLine = theCSV.readline().decode("utf-8").strip()
		if line_count2 % 100000 == 0:
			print("MinerReward", line_count2, reward_count/1e+18)

	theCSV.close()
	theZIP.close()


print("Info", line_count1, tx_count) # 13250000 1287874866
print("MinerReward", line_count2, reward_count/1e+18) # 14430085 45564803.40625
print("EIP1559", total_burnt/1e+18, total_tips/1e+18) # 318511.27812318946 84794.48365360587
