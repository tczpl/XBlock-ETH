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
    "13250000to13499999_BlockTransaction",
    "13500000to13749999_BlockTransaction",
    "13750000to13999999_BlockTransaction",
    "14000000to14249999_BlockTransaction",
    "14250000to14499999_BlockTransaction",
    "14500000to14749999_BlockTransaction",
    "14750000to14999999_BlockTransaction",
    "15000000to15249999_BlockTransaction",
    "15250000to15499999_BlockTransaction",
    "15500000to15749999_BlockTransaction",
    "15750000to15999999_BlockTransaction",
    "16000000to16249999_BlockTransaction",
    "16250000to16499999_BlockTransaction",
    "16500000to16749999_BlockTransaction",
    "16750000to16999999_BlockTransaction",
    "17000000to17249999_BlockTransaction",
    "17250000to17499999_BlockTransaction",
    "17500000to17749999_BlockTransaction",
    "17750000to17999999_BlockTransaction",
    "18000000to18249999_BlockTransaction",
    "18250000to18499999_BlockTransaction",
    "18500000to18749999_BlockTransaction",
    "18750000to18999999_BlockTransaction",
    "19000000to19249999_BlockTransaction",
    "19250000to19499999_BlockTransaction",
    "19500000to19749999_BlockTransaction",
    "19750000to19999999_BlockTransaction",
    "20000000to20249999_BlockTransaction",
    "20250000to20499999_BlockTransaction"
]

def ToInt(str):
    return None if str=="None" else int(str)
def ToStr(str):
    return None if str=="None" else str

tx_count = 0
total_fees = 0
total_blobs = 0

for file in files:
    print(file)    
    theZIP = zipfile.ZipFile(fileDir+file+".zip", 'r')
    theCSV = theZIP.open(file+".csv")
    head = theCSV.readline()

    oneLine = theCSV.readline().decode("utf-8").strip()    
    while (oneLine!=""):
        oneArray = oneLine.split(",")

        # blockNumber,timestamp,transactionHash,from,to,toCreate,fromIsContract,toIsContract,value,gasLimit,gasPrice,gasUsed,callingFunction,isError,eip2718type,baseFeePerGas,maxFeePerGas,maxPriorityFeePerGas,blobHashes,blobBaseFeePerGas,blobGasUsed

        blockNumber           = int(oneArray[0])
        timestamp             = int(oneArray[1])
        transactionHash       = oneArray[2]
        sender                = oneArray[3]
        to                    = oneArray[4]
        toCreate              = oneArray[5]
        fromIsContract        = oneArray[6]
        toIsContract          = oneArray[7]
        value                 = int(oneArray[8])
        gasLimit              = int(oneArray[9])
        gasPrice              = int(oneArray[10])
        gasUsed               = int(oneArray[11])
        callingFunction       = oneArray[12]
        isError               = ToStr(oneArray[13])
        eip2718type           = ToInt(oneArray[14])
        baseFeePerGas         = ToInt(oneArray[15])
        maxFeePerGas          = ToInt(oneArray[16])
        maxPriorityFeePerGas  = ToInt(oneArray[17])

        if eip2718type == 3:
            blobHashes        = oneArray[18].split(":")
            blobBaseFeePerGas = int(oneArray[19])
            blobGasUsed       = int(oneArray[20])

            total_blobs += len(blobHashes)
            total_fees  += blobBaseFeePerGas*blobGasUsed


        total_fees += gasPrice*gasUsed
        tx_count += 1    
        if tx_count % 100000 == 0:
            print(tx_count, total_fees/1e+18, total_blobs)    
        oneLine = theCSV.readline().decode("utf-8").strip()    

    theCSV.close()    
    theZIP.close()    

print(tx_count, total_fees/1e+18, total_blobs)
# 2470448664 9206232.9680935 2222401
