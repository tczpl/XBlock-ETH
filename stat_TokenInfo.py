import zipfile

fileDir = "./"	
files = [
	"ERC20TokenInfo",
	"ERC721TokenInfo"
]	

def ToInt(str):
	return None if str=="None" else int(str)

line_count = 0

# ERC20TokenInfo
file = files[0]
theZIP = zipfile.ZipFile(fileDir+file+".zip", 'r')
theCSV = theZIP.open(file+".csv")	
head = theCSV.readline()	

oneLine = theCSV.readline().decode("utf-8").strip()
while (oneLine!=""):
	oneArray = oneLine.split(",")	

	# address,name,symbol,totalSupply,decimal
	address	 = oneArray[0]	
	name		= oneArray[1]	
	symbol	  = oneArray[2]	
	totalSupply = ToInt(oneArray[3])	
	decimal	 = ToInt(oneArray[4])	

	print(address, name)
	line_count += 1	
	oneLine = theCSV.readline().decode("utf-8").strip()	
  
theCSV.close()
theZIP.close()	


# ERC721TokenInfo
file = files[1]
theZIP = zipfile.ZipFile(fileDir+file+".zip", 'r')	
theCSV = theZIP.open(file+".csv")	
head = theCSV.readline()	

oneLine = theCSV.readline().decode("utf-8").strip()	
while (oneLine!=""):
	oneArray = oneLine.split(",")	

	# address,name,symbol,totalSupply
	address	 = oneArray[0]
	name		= oneArray[1]
	symbol	  = oneArray[2]
	totalSupply = ToInt(oneArray[3])

	print(address, name)
	line_count += 1	
	oneLine = theCSV.readline().decode("utf-8").strip()	

theCSV.close()	
theZIP.close()

print(line_count) # 254761