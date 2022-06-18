import cv2 
import numpy as np

images = ['SECOMP - c38.png',
'SECOMP - c39.png',
'SECOMP - c40.png',
'SECOMP - c41.png',
'SECOMP - c42.png',
'SECOMP - c43.png',
'SECOMP - c44.png',
'SECOMP - c45.png',
'SECOMP - c46.png',
'SECOMP - c47.png',
'SECOMP - c48.png',
'SECOMP - c54.png',
'SECOMP - c55.png',
'SECOMP - c62.png',
'SECOMP - c63.png',
'SECOMP - c64.png',
'SECOMP - c65.png',
'SECOMP - c67.png',
'SECOMP - c68.png',
'SECOMP - c69.png',
'SECOMP - c70.png',
'SECOMP - c71.png',
'SECOMP - c72.png',
'SECOMP - c107.png',
'SECOMP - c108.png',
'SECOMP - c109.png']

for image in images:
	# Imagem original
	img = cv2.imread('Capas/' + image)
	img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)

	#BACKGROUND
	#Resize image
	back = cv2.resize(img, (1920, 2400), interpolation = cv2.INTER_NEAREST)
	back = back[420:1500, 0:1920]

	img = cv2.resize(img, (864, 1080), interpolation = cv2.INTER_NEAREST)

	#Blur
	back = cv2.GaussianBlur(back, (101,101), sigmaX=40, sigmaY=30)
	back[:,:,0:3] = back[:,:,0:3] / 2

	#Color
	greenBack = cv2.imread('SECOMP-linhas.png', cv2.IMREAD_UNCHANGED)
	greenBack = greenBack[0:1080, 0:1920, 0:4]

	for i in range(back.shape[0]):
		for j in range(back.shape[1]):
			if greenBack[i][j][3] != 0:
				back[i][j] = greenBack[i][j]

	#GERAL
	#Sobrepor imagens
	x_offset = 528
	y_offset = 0
	back[y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1]] = img

	cv2.imwrite(image, back)
	print(image + " pronta!")





