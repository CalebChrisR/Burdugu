import os


def bdo_file_read():

	for x in os.listdir():
		if x.endswith(".pdf"):
			filename = x


	with open('bdo.pdf', 'r') as file:
		data = file.readlines()
		
		i = 0
		for line in data:
			if not (i < 38):
				print(line)
			i += 1
			if i == 50:
				break







def main():
	bdo_file_read()


if __name__ == "__main__":
	main()