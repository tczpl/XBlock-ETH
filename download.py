import time
import requests
import os

def download(localFile):
	srcUrl = "https://zhengpeilin.com/download.php?file="+localFile
	if os.path.exists(localFile+".temp"):
		os.remove(localFile+".temp")
	if os.path.exists(localFile):
		print(localFile+"exist!\n")
		return
	print("------------------------------------------------------------")
	print('Downloading %s' % localFile, end='\r')
	try:
		with requests.get(srcUrl, stream=True) as r:
			if r.status_code != 200:
				print("retrying", srcUrl, r.status_code)
				time.sleep(10)
				return download(localFile)
			contentLength = int(r.headers['content-length'])
			print('Downloading %s %.2f MB' % (localFile, contentLength/1024/1024))
			downSize = 0
			startTime = time.time()
			with open(localFile+".temp", 'wb') as f:
				for chunk in r.iter_content(8192):
					if chunk:
						f.write(chunk)
					downSize += len(chunk)
					line = '%.1f%% - %.2f MB/s - %.2f MB          '
					line = line % (downSize/contentLength*100, downSize/1024/1024/(time.time()-startTime), downSize/1024/1024)
					print(line, end='\r')
					if downSize >= contentLength:
						break
			os.rename(localFile+".temp", localFile)
			print()
	except:
		print("exception wait 180s\n")
		time.sleep(360)
		print("retry\n")
		return download(localFile)



blocks = ["0to999999", "1000000to1999999", "2000000to2999999", "3000000to3999999", "4000000to4999999", "5000000to5999999", "6000000to6999999", "7000000to7999999", "8000000to8999999", "9000000to9999999", "10000000to10999999", "11000000to11999999", "12000000to12999999", "13000000to13249999", "13250000to13499999", "13500000to13749999", "13750000to13999999", "14000000to14249999", "14250000to14499999", "14500000to14749999", "14750000to14999999", "15000000to15249999", "15250000to15499999", "15500000to15749999", "15750000to15999999","16000000to16249999", "16250000to16499999"]

Block_Files = ["{}_Block.zip".format(i) for i in blocks] + ["stat_Block.py"]
BlockTransaction_Files = ["{}_BlockTransaction.zip".format(i) for i in blocks] + ["stat_BlockTransaction.py"]
InternalTransaction_Files = ["{}_InternalTransaction.zip".format(i) for i in blocks] + ["stat_InternalTransaction.py"]
ContractInfo_Files = ["{}_ContractInfo.zip".format(i) for i in blocks] + ["stat_ContractInfo.py"]
ERC20Transaction_Files = ["{}_ERC20Transaction.zip".format(i) for i in blocks] + ["stat_ERC20Transaction.py"]
ERC721Transaction_Files = ["{}_ERC721Transaction.zip".format(i) for i in blocks] + ["stat_ERC721Transaction.py"]

TokenInfo_Files = ["ERC20TokenInfo.zip", "ERC721TokenInfo.zip", "stat_TokenInfo.py"]

All = [Block_Files, BlockTransaction_Files, InternalTransaction_Files, ContractInfo_Files, ERC20Transaction_Files, ERC721Transaction_Files, TokenInfo_Files]


def start():
	print("Select the datasets to download:")
	print("0. All")
	print("1. Block")
	print("2. Block Transaction")
	print("3. Internal Transaction ")
	print("4. Contract Info")
	print("5. ERC20 Transaction")
	print("6. ERC721 Transaction")
	print("7. Token Info")
	select = input("Please input a number (0~6): ")

	if select == "0":
		for Files in All:
			for localFile in Files:
				download(localFile)
	elif select == "1":
		for localFile in Block_Files:
			download(localFile)
	elif select == "2":
		for localFile in BlockTransaction_Files:
			download(localFile)
	elif select == "3":
		for localFile in InternalTransaction_Files:
			download(localFile)
	elif select == "4":
		for localFile in ContractInfo_Files:
			download(localFile)
	elif select == "5":
		for localFile in ERC20Transaction_Files:
			download(localFile)
	elif select == "6":
		for localFile in ERC721Transaction_Files:
			download(localFile)
	elif select == "7":
		for localFile in TokenInfo_Files:
			download(localFile)
	else:
		return start()

start()
print("finish")
