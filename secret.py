import os
def rename():
	file_list=os.listdir(r"C:\Users\Rahul\ITP\pyth\secretMSG\prank")
	saved_path=os.getcwd()
	os.chdir("C:\Users\Rahul\ITP\pyth\secretMSG\prank")
	for file_name in file_list:
		os.rename(file_name,file_name.translate(None,"0123456789"))
rename()
