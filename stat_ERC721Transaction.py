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
    "11000000to11999999_ERC721Transaction",
    "12000000to12999999_ERC721Transaction",
    "13000000to13249999_ERC721Transaction",
    "13250000to13499999_ERC721Transaction",
    "13500000to13749999_ERC721Transaction",
    "13750000to13999999_ERC721Transaction",
    "14000000to14249999_ERC721Transaction",
    "14250000to14499999_ERC721Transaction",
    "14500000to14749999_ERC721Transaction",
    "14750000to14999999_ERC721Transaction",
    "15000000to15249999_ERC721Transaction",
    "15250000to15499999_ERC721Transaction",
    "15500000to15749999_ERC721Transaction",
    "15750000to15999999_ERC721Transaction",
    "16000000to16249999_ERC721Transaction",
    "16250000to16499999_ERC721Transaction",
    "16500000to16749999_ERC721Transaction",
    "16750000to16999999_ERC721Transaction",
    "17000000to17249999_ERC721Transaction",
    "17250000to17499999_ERC721Transaction",
    "17500000to17749999_ERC721Transaction",
    "17750000to17999999_ERC721Transaction",
    "18000000to18249999_ERC721Transaction",
    "18250000to18499999_ERC721Transaction",
    "18500000to18749999_ERC721Transaction",
    "18750000to18999999_ERC721Transaction",
    "19000000to19249999_ERC721Transaction",
    "19250000to19499999_ERC721Transaction",
    "19500000to19749999_ERC721Transaction",
    "19750000to19999999_ERC721Transaction",
    "20000000to20249999_ERC721Transaction",
    "20250000to20499999_ERC721Transaction",
    "20500000to20749999_ERC721Transaction",
    "20750000to20999999_ERC721Transaction",
    "21000000to21249999_ERC721Transaction",
    "21250000to21499999_ERC721Transaction",
    "21500000to21749999_ERC721Transaction",
    "21750000to21999999_ERC721Transaction",
    "22000000to22249999_ERC721Transaction"
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
        blockNumber     = int(oneArray[0])
        timestamp       = int(oneArray[1])
        transactionHash = oneArray[2]
        tokenAddress    = oneArray[3]
        sender          = oneArray[4]
        to              = oneArray[5]
        fromIsContract  = int(oneArray[6])
        toIsContract    = int(oneArray[7])
        tokenId         = int(oneArray[8])

        tx_count += 1
        tokens[tokenAddress] = True
        if(tx_count%100000==0):
            print(tx_count, len(tokens))
        oneLine = theCSV.readline().decode("utf-8").strip()

    theCSV.close()
    theZIP.close()

print(tx_count, len(tokens))
# 263779756 249226