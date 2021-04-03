import zipfile

fileDir = "./"
files = [
    "0to999999_ERC20Transaction",
    "1000000to1999999_ERC20Transaction",
    "2000000to2999999_ERC20Transaction",
    "3000000to3999999_ERC20Transaction",
    "4000000to4999999_ERC20Transaction",
    "5000000to5999999_ERC20Transaction",
    "6000000to6999999_ERC20Transaction",
    "7000000to7999999_ERC20Transaction",
    "8000000to8999999_ERC20Transaction",
    "9000000to9999999_ERC20Transaction",
    "10000000to10999999_ERC20Transaction",
    "11000000to11999999_ERC20Transaction"
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

        # blockNumber,timestamp,transactionHash,tokenAddress,from,to,fromIsContract,toIsContract,value
        blockNumber     = int(oneArray[0])
        timestamp       = int(oneArray[1])
        transactionHash = oneArray[2]
        tokenAddress    = oneArray[3]
        sender          = oneArray[4]
        to              = oneArray[5]
        fromIsContract  = int(oneArray[6])
        toIsContract    = int(oneArray[7])
        value           = int(oneArray[8])

        tx_count += 1
        tokens[tokenAddress] = True
        if tx_count % 100000 == 0:
            print(tx_count, len(tokens))
        oneLine = theCSV.readline().decode("utf-8").strip()

    theCSV.close()
    theZIP.close()

print(tx_count, len(tokens))
# 601955094 246609
