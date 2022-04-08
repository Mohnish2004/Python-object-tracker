@@ -0,0 +1,137 @@
import cv2 
from tkinter import Label,Button,Tk,filedialog,IntVar,Checkbutton, Toplevel, Entry
import csv

def space(window,times = 1):
	for i in range(times):
		Label(window,text = "").pack()

def selectVid():

	filename = filedialog.askopenfilename(
		title = 'Select a video',
		filetypes=[('Videos','.mp4')]
		)

	img = filename

	dostuff(img)

def load():
	Dict = {}

	f = open('Config.cfg','r')
	cf = csv.reader(f)

	for i in cf:
		for x in i:
			if len(x) > 6:
				Dict[x] = int(i[1])

	f.close()
	return Dict

def save(Dict,window):
	f = open('Config.cfg','w')
	cf = csv.writer(f)

	for i in Dict:
		if i == 'Check boxes':
			for x in Dict[i]:
				cf.writerow([x,Dict[i][x].get()])

		if i == 'Values':
			for x in Dict[i]:
				cf.writerow([x,int(Dict[i][x].get())])

	f.close()
	window.destroy()

def settings():
	_masks = IntVar()
	_roi = IntVar()
	_cont = IntVar()
	_history = IntVar()
	_varThreshold = IntVar()

	newWin = Toplevel(window)
	newWin.geometry('400x600')
	newWin.title('Settings')

	Label(newWin,text = 'Settings',font = ('Candara',12)).pack()

	Dict = {'Check boxes':{'Show Masks':_masks,'Region of interest':_roi,'Show contours':_cont},'Values':{'History':_history,'varThreshold':_varThreshold}}
	for i in Dict:
		if i == 'Check boxes':
			for x in Dict[i]:
				Checkbutton(newWin,text=x,variable = Dict[i][x],font = ("Candara",14)).pack()
				space(newWin)

		if i == 'Values':
			for x in Dict[i]:
				Label(newWin, text=x,font = ('Candara',10)).pack()
				Dict[i][x] = Entry(newWin,bd = 1)
				Dict[i][x].pack()
				space(newWin)

	Button(newWin,text = 'Save',font = ("Candara",14),command = lambda: save(Dict,newWin)).pack()

def dostuff(path):
	d = load()

	cap = cv2.VideoCapture(path)

	object_detector = cv2.createBackgroundSubtractorKNN(history = d['History'])#,varThreshold = d['varThreshold'])

	while True:
		ret,frame = cap.read()
		h,w,_ = frame.shape

		mask = object_detector.apply(frame)
		_,mask = cv2.threshold(mask, 254,255,cv2.THRESH_BINARY)

		if d['Show Masks'] == 1:
			cv2.imshow('Mask',mask)
		contours,_ = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

		for cnt in contours:
			#Calculate area and remove small elements

			area = cv2.contourArea(cnt)

			if area > 100:	

				if d['Show contours'] == 1:
					cv2.drawContours(frame,[cnt],-1,(0,255,0),1)

				x,y,wid,hei = cv2.boundingRect(cnt)
				cv2.rectangle(frame,(x,y),(x+wid,y+hei),(0,255,0),1)


		cv2.imshow('Frame',frame)

		key = cv2.waitKey(30)

		if key == 27: break

	cap.release()
	cv2.destroyAllWindows()

window = Tk()
window.geometry('400x500')
window.configure(width = 400, height = 500)
window.resizable(False,False)
window.title('Either a terrible project or kinda good')

Label(window,text = "Motion detection",font = ("Candara",14)).pack()
space(window)

Button(window,text = 'Input video',font = ("Candara",14),command = selectVid).pack()
space(window)

Button(window,text = 'Settings',font = ("Candara",14),command = settings).pack()
space(window)

Button(window,text = 'Exit',font = ("Candara",14),command = exit).pack()
load()
window.mainloop()
