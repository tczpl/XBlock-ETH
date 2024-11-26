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
    "13250000to13499999_ContractInfo",
    "13500000to13749999_ContractInfo",
    "13750000to13999999_ContractInfo",
    "14000000to14249999_ContractInfo",
    "14250000to14499999_ContractInfo",
    "14500000to14749999_ContractInfo",
    "14750000to14999999_ContractInfo",
    "15000000to15249999_ContractInfo",
    "15250000to15499999_ContractInfo",
    "15500000to15749999_ContractInfo",
    "15750000to15999999_ContractInfo",
    "16000000to16249999_ContractInfo",
    "16250000to16499999_ContractInfo",
    "16500000to16749999_ContractInfo",
    "16750000to16999999_ContractInfo",
    "17000000to17249999_ContractInfo",
    "17250000to17499999_ContractInfo",
    "17500000to17749999_ContractInfo",
    "17750000to17999999_ContractInfo",
    "18000000to18249999_ContractInfo",
    "18250000to18499999_ContractInfo",
    "18500000to18749999_ContractInfo",
    "18750000to18999999_ContractInfo",
    "19000000to19249999_ContractInfo",
    "19250000to19499999_ContractInfo",
    "19500000to19749999_ContractInfo",
    "19750000to19999999_ContractInfo",
    "20000000to20249999_ContractInfo",
    "20250000to20499999_ContractInfo",
    "20500000to20749999_ContractInfo",
    "20750000to20999999_ContractInfo",
    "21000000to21249999_ContractInfo"
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
        address                = oneArray[0]
        createdBlockNumber     = int(oneArray[1])
        createdTimestamp       = int(oneArray[2])
        createdTransactionHash = oneArray[3]
        creator                = oneArray[4]
        creatorIsContract      = int(oneArray[5])
        createValue            = int(oneArray[6])
        creationCode           = oneArray[7]
        contractCode           = oneArray[8]

        line_count += 1
        creators[creator] = True

        oneLine = theCSV.readline().decode("utf-8").strip()
        if line_count % 100000 == 0:
            print(line_count, len(creators))

    theCSV.close()
    theZIP.close()

print(line_count, len(creators))
# 68872332 862474