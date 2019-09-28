import base64
import time

def ToBase64(file, txt):
	with open(file, 'rb') as fileObj:
		image_data = fileObj.read()
		base64_data = base64.b64encode(image_data)
		fout = open(txt, 'w')
		fout.write(base64_data.decode())
		fout.close()
		print("Complete!")


def ToFile(txt, file):
	with open(txt, 'r') as fileObj:
		base64_data = fileObj.read()
		file_info = base64_data[0:5]
		if file_info == "data:":
			print("Err: base64文件格式错误：不应存在data:头")
			return True
		else:
			ori_image_data = base64.b64decode(base64_data)
			fout = open(file, 'wb')
			fout.write(ori_image_data)
			fout.close()
			print("Complete!")
			return False


go = True
while go:
	filename = input("请输入欲转换文件名：")
	filebase = eval(input("请输入转换类型（1为到base64，2为到二进制，其余数字无效）："))
#	input_suffix = filename[-3:]  # 读取文件名最后三位

	if filebase == 2:
		file_suffix_name = input("请输入转换后文件后缀名：")
		go = ToFile(f"./{filename}", f'{filename}_decode.{file_suffix_name}')  # base64编码转换为二进制文件
		time.sleep(5)
	elif filebase == 1: 
		ToBase64(f"./{filename}", f'{filename}_base64.txt')  # 文件转换为base64
		go = False
		time.sleep(5)
	else:
		print("无效输入，请重新输入")
