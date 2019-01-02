#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
STARTING: plot-code/bar
USAGE: If you want to plot with gender, enter type1 type2 type3 WITH Y, like this:
       ./joint.py cin ebv gs mis 
       Y
       If not, replace Y by N
"""
      
import PIL.Image as im
import sys


im.MAX_IMAGE_PIXELS = 1000000000

def joint_image(input_image1, input_image2, label_img, output_image):

	joint_image = im.new('RGBA',(16384,20000))
	image1 = im.open(input_image1)
	img1 = image1.crop((0,1400,16384,11500))
	image2 = im.open(input_image2)
	img2 = image2.crop((0,1300,16384,11500))
	image3 = im.open(label_img)
	img3 = image3.resize((2000,2800), im.ANTIALIAS)
	joint_image.paste(img1,(0,0))
	joint_image.paste(img2,(0,9800))
	joint_image.paste(img3,(12700,140))
	joint_image.save(output_image)
	#joint_image.show()

tumor_type = sys.argv[1:]
gender = ['male', 'female']
gd = input("\nIf you plot WITH gender?(Y for yes and N for not): ")

if gd.lower() == 'y':
	for tt in tumor_type:
		for gen in gender:
			ii_upper = "../../../bar-plot/gender/bar-{}-{}.png".format(tt, gen)
			ii_lower = "../../../bar-plot/gender/{}-{}-hla-frequency.png".format(tt, gen)
			li = "../../../bar-plot/{}-label.png".format(gen) # made by PPT
			oi = "../../../bar-plot/gender/{}-{}.png".format(tt.upper(), gen.upper())
			joint_image(ii_upper, ii_lower,li, oi)
else:
	for tt in tumor_type:
		ii_upper = "../../bar-plot/bar-{}.png".format(tt)
		ii_lower = "../../bar-plot/{}-hla-frequency.png".format(tt)
		li = "../../bar-plot/{}-label.png".format(tt)
		oi = "../../bar-plot/{}.png".format(tt.upper())
		joint_image(ii_upper, ii_lower,li, oi)
