from selenium import webdriver
from PIL import Image
import operator
import sys
from gpiozero import LED
from time import sleep

def trigger(top,right,bottom,left):
	print "top:%s\nright:%s\nbottom:%s\nleft:%s\n" %(top[0][0],right[0][0],bottom[0][0],left[0][0])
	#FOR_TOP
	TOP_RED=LED(26)
	TOP_YELLOW=LED(5)
	TOP_GREEN=LED(13)
	
	#FOR_RIGHT
	RIGHT_RED=LED(9)
	RIGHT_YELLOW=LED(27)
	RIGHT_GREEN=LED(11)
	
	#FOR_BOTTOM
	BOT_RED=LED(14)
	BOT_YELLOW=LED(23)
	BOT_GREEN=LED(15)
	
	#FOR_LEFT
	LEFT_RED=LED(21)
	LEFT_YELLOW=LED(16)
	LEFT_GREEN=LED(12)
	
	#RESET
	TOP_RED.off()
	TOP_YELLOW.off()
	TOP_GREEN.off()
	
	RIGHT_RED.off()
	RIGHT_YELLOW.off()
	RIGHT_GREEN.off()
	
	BOT_RED.off()
	BOT_YELLOW.off()
	BOT_GREEN.off()
	
	LEFT_RED.off()
	LEFT_YELLOW.off()
	LEFT_GREEN.off()
	
	while True:
		if (top[0][0]== "RED" and bottom[0][0]== "RED") or (top[0][0]== "ORANGE" and bottom[0][0]== "RED") or (top[0][0]== "RED" and bottom[0][0]== "ORANGE"):
			v_time=120
		elif(top[0][0]== "ORANGE" and bottom[0][0]== "ORANGE") or (top[0][0]== "GREEN" and bottom[0][0]== "RED") or (top[0][0]== "RED" and bottom[0][0]== "GREEN"):
			v_time=60
		else:
			v_time=30
		
		TOP_YELLOW.off()
		TOP_GREEN.on()
		
		RIGHT_YELLOW.off()
		RIGHT_GREEN.on()
		
		BOT_YELLOW.off()
		BOT_GREEN.on()
		
		LEFT_YELLOW.off()
		LEFT_RED.on()
		
		print "V_TIME is %d" %v_time
		sleep(v_time)
		
		LEFT_YELLOW.off()
		LEFT_RED.on()
		
		print "v time is %d" %v_time
		
		TOP_GREEN.off()
		TOP_YELLOW.on()
		
		TOP_GREEN.off()
		TOP_YELLOW.on()
		
		RIGHT_RED.off()
		RIGHT_YELLOW.on()
		
		BOT_GREEN.off()
		BOT_YELLOW.on()
		
		LEFT_RED.off()
		LEFT_YELLOW.on()
		
		sleep(5)
		
		if(right[0] == "RED" and left[0][0] == "RED") or (right[0] == "RED" and left[0][0] == "ORANGE") or (right[0] == "ORANGE" and left[0][0] == "RED") : 
			h_time=120
		elif(right[0][0]== "ORANGE" and left[0][0]== "ORANGE") or (right[0] == "RED" and left[0][0] == "GREEN") or (right[0] == "GREEN" and left[0][0] == "RED"):
			h_time=60
		else	
			h_time=30
		
		TOP_YELLOW.off()
		TOP_RED.on()
		
		RIGHT_YELLOW.off()
		RIGHT_GREEN.on()
		
		BOT_YELLOW.off()
		BOT_RED.on()
		
		LEFT_YELLOW.off()
		LEFT_GREEN.on()
		
		print "H_time is %d" %h_time
		sleep(h_time)
		
		TOP_RED.off()
		TOP_YELLOW.on()
		
		RIGHT_GREEN.off()
		RIGHT_YELLOW.on()
		
		BOT_RED.off()
		BOT_YELLOW.on()
		
		LEFT_GREEN.off()
		LEFT_YELLOW.on()
		
		sleep(5)
		
def split(Image):
	width,heigth =Image.size
	
	#top segment
	required = height-(0.6*height)
	alter = Image.crop((0,0,width,int(required)))
	alter.save('top.png')
	
	#bottom
	required = (0.6*height)
	alter = Image.crop((0,int(required),width,height))
	alter.save('bottom.png')
		
	#left
	required = (0.4*width)
	alter = Image.crop((0,0,int(required),height))
	alter.save('left.png')
	
	#right
	required = width-(0.4*width)
	alter = Image.crop((int(required),0,width,height))
	alter.save('right.png')
		
def capture():
	br=webdriver.PhantonJS()
	br.get('http://sload.hol.es/map.php?lat=
	sleep(15)
	br.save_screenshot('screenshot.png')
	br.quit
def trafficIntensity(path):
	img = Image.open(path)
	img = img.convert("RGBA")
	datas = imag.getdata()
	
	green=red=orange=0
	
	for item in datas:
		if((item[0] >=140 and item[0]<=230) and (item[1] >=0 and item[0] <=90) and (item[2] >=0 and item[0] <=70):
			red=red+1
		if((item[0] >=230 and item[0]<=300) and (item[1] >=90 and item[0] <=190) and (item[2] >=0 and item[0] <=70):
			orange=orange+1
		if((item[0] >=70 and item[0]<=140) and (item[1] >=190 and item[0] <=90) and (item[2] >=0 and item[0] <=70):
			green=green+1
			
	signals =('RED':red,'ORANGE':orange,'GREEN':green)
	sorted_s=sorted(signals.items(), key=operator.itemgetter(1),reverse=True) [ item[0][0],item[1][0],item[2][0] ]
	return sorted_s
	
if __name__== "__main__":
	capture()
	trafficsImg = Image.open('screenshot.png')
	split(trafficImg)
	top = trafficIntensity('top.png')
	right = trafficIntensity('right.png')
	bottom = trafficIntensity('bottom.png')
	left = trafficIntensity('left.png')
	trigger(top,right,bottom,left)
	
			