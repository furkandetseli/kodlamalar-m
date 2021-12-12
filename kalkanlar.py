import time
import random

şehirler=["Kuban","Gümüşvadi","Tekinhan","Grigon","Selaken","Konstiten"]
oşehir=["Kuban","Gümüşvadi","Tekinhan"]
botşehir=["Grigon","Selaken","Konstiten"]
botbaşkan="Julios"
yerelordu=[200,200,200,0,0,0]
düşmanordu=[0,0,0,200,200,200]
liste=[]
liste2=[]
						
class oyun():
	global şehirler
	global oşehir
	global botşehir
	global botbaşkan
	global yerelordu
	global savaş
	global liste
	global liste2
	def __init__(self,başkan="Bilgi yok",toplamordu=0,ordubölge=0,teknoloji=1,para=1000,gün=1,ilişki=0,aga="-",savaşdurumu="Barış",diplomasi="Kapalı",\
		düşmanpara=1000,düşmanordu=0):	
		self.ordubölge=ordubölge
		self.diplomasi=diplomasi
		self.savaşdurumu=savaşdurumu
		self.aga=aga
		self.toplamordu=toplamordu
		self.teknoloji=teknoloji
		self.para=para
		self.gün=gün
		self.başkan=başkan
		self.ilişki=ilişki
		self.düşmanpara=düşmanpara
		self.düşmanordu=düşmanordu
		self.şehirsistem=self.şehirsistemoluştur()
		self.bot=self.botoluştur()
	def botoluştur(self):
		return oyun.bot(self)	
	def şehirsistemoluştur(self):
		return oyun.şehirsistem(self)	
	class bot():
		def __init__(self,oyun):
			self.oyun=oyun

		def botgüngeç(self):
			if len(botşehir)==1:
				self.oyun.düşmanpara += 100
			elif len(botşehir)==2:
				self.oyun.düşmanpara += 200
			elif len(botşehir)==3:
				self.oyun.düşmanpara += 300
				print(self.oyun.düşmanpara)
			elif len(botşehir)==4:
				self.oyun.düşmanpara += 400
				print(self.oyun.düşmanpara)
			elif len(botşehir)==5:
				self.oyun.düşmanpara += 500
				print(self.oyun.düşmanpara)
			else:
				print(":D")
			self.rastgelesaldır()
		
		def rastgelesaldır(self):
			if self.oyun.savaşdurumu=="Savaş":
				if şehirler[0] in oşehir:
					if yerelordu[0]<düşmanordu[1]*2:
						asker=düşmanordu[1]
						düşmanordu[1]-=asker
						düşmanordu[0]+=asker
						self.oyun.savaşş(yerelordu[0],düşmanordu[0])
						g=liste[0]
						yerelordu.pop(0)
						yerelordu.insert(0,g)
						h=liste[1]
						düşmanordu.pop(0)
						düşmanordu.insert(0,h)
						if düşmanordu[0]>0:
							oşehir.remove("Kuban")
							botşehir.append("Kuban")
						if yerelordu[0]==0:
							if şehirler[0] in oşehir:
								asker=düşmanordu[1]
								düşmanordu[1]-=asker
								düşmanordu[0]+=asker
								oşehir.remove("Kuban")
								botşehir.append("Kuban")
					elif yerelordu[0]<düşmanordu[2]*2:
						asker=düşmanordu[2]
						düşmanordu[2]-=asker
						düşmanordu[0]+=asker
						self.oyun.savaşş(yerelordu[0],düşmanordu[0])
						g=liste[0]
						yerelordu.pop(0)
						yerelordu.insert(0,g)
						h=liste[1]
						düşmanordu.pop(0)
						düşmanordu.insert(0,h)
						if düşmanordu[0]>0:
							oşehir.remove("Kuban")
							botşehir.append("Kuban")
						if yerelordu[0]==0:
							if şehirler[0] in oşehir:
								asker=düşmanordu[2]
								düşmanordu[2]-=asker
								düşmanordu[0]+=asker
								oşehir.remove("Kuban")
								botşehir.append("Kuban")
					elif yerelordu[0]<düşmanordu[3]*2:
						asker=düşmanordu[3]
						düşmanordu[3]-=asker
						düşmanordu[0]+=asker
						self.oyun.savaşş(yerelordu[0],düşmanordu[0])
						g=liste[0]
						yerelordu.pop(0)
						yerelordu.insert(0,g)
						h=liste[1]
						düşmanordu.pop(0)
						düşmanordu.insert(0,h)
						if düşmanordu[0]>0:
							oşehir.remove("Kuban")
							botşehir.append("Kuban")
						if yerelordu[0]==0:
							if şehirler[0] in oşehir:
								asker=düşmanordu[3]
								düşmanordu[3]-=asker
								düşmanordu[0]+=asker
								oşehir.remove("Kuban")
								botşehir.append("Kuban")
					elif yerelordu[0]<düşmanordu[4]*2:
						asker=düşmanordu[4]
						düşmanordu[4]-=asker
						düşmanordu[0]+=asker
						self.oyun.savaşş(yerelordu[0],düşmanordu[0])
						g=liste[0]
						yerelordu.pop(0)
						yerelordu.insert(0,g)
						h=liste[1]
						düşmanordu.pop(0)
						düşmanordu.insert(0,h)
						if düşmanordu[0]>0:
							oşehir.remove("Kuban")
							botşehir.append("Kuban")
						if yerelordu[0]==0:
							if şehirler[0] in oşehir:
								asker=düşmanordu[4]
								düşmanordu[4]-=asker
								düşmanordu[0]+=asker
								oşehir.remove("Kuban")
								botşehir.append("Kuban")
					elif yerelordu[0]<düşmanordu[5]*2:
						asker=düşmanordu[5]
						düşmanordu[5]-=asker
						düşmanordu[0]+=asker
						self.oyun.savaşş(yerelordu[0],düşmanordu[0])
						g=liste[0]
						yerelordu.pop(0)
						yerelordu.insert(0,g)
						h=liste[1]
						düşmanordu.pop(0)
						düşmanordu.insert(0,h)
						if düşmanordu[0]>0:
							oşehir.remove("Kuban")
							botşehir.append("Kuban")
						if yerelordu[0]==0:
							if şehirler[0] in oşehir:
								asker=düşmanordu[5]
								düşmanordu[5]-=asker
								düşmanordu[0]+=asker
								oşehir.remove("Kuban")
								botşehir.append("Kuban")								
				if şehirler[1] in oşehir:
					if yerelordu[1]<düşmanordu[0]*2:
						asker=düşmanordu[0]
						düşmanordu[0]-=asker
						düşmanordu[1]+=asker
						self.oyun.savaşş(yerelordu[1],düşmanordu[1])
						g=liste[0]
						yerelordu.pop(1)
						yerelordu.insert(1,g)
						h=liste[1]
						düşmanordu.pop(1)
						düşmanordu.insert(1,h)
						if düşmanordu[1]>0:
							oşehir.remove("Gümüşvadi")
							botşehir.append("Gümüşvadi")
						if yerelordu[1]==0:
							if şehirler[1] in oşehir:
								asker=düşmanordu[0]
								düşmanordu[0]-=asker
								düşmanordu[1]+=asker
								oşehir.remove("Gümüşvadi")
								botşehir.append("Gümüşvadi")
					elif yerelordu[1]<düşmanordu[2]*2:
						asker=düşmanordu[2]
						düşmanordu[2]-=asker
						düşmanordu[1]+=asker
						self.oyun.savaşş(yerelordu[1],düşmanordu[1])
						g=liste[0]
						yerelordu.pop(1)
						yerelordu.insert(1,g)
						h=liste[1]
						düşmanordu.pop(1)
						düşmanordu.insert(1,h)
						if düşmanordu[1]>0:
							oşehir.remove("Gümüşvadi")
							botşehir.append("Gümüşvadi")
						if yerelordu[1]==0:
							if şehirler[1] in oşehir:
								asker=düşmanordu[2]
								düşmanordu[2]-=asker
								düşmanordu[1]+=asker
								oşehir.remove("Gümüşvadi")
								botşehir.append("Gümüşvadi")
					elif yerelordu[1]<düşmanordu[3]*2:
						asker=düşmanordu[3]
						düşmanordu[3]-=asker
						düşmanordu[1]+=asker
						self.oyun.savaşş(yerelordu[1],düşmanordu[1])
						g=liste[0]
						yerelordu.pop(1)
						yerelordu.insert(1,g)
						h=liste[1]
						düşmanordu.pop(1)
						düşmanordu.insert(1,h)
						if düşmanordu[1]>0:
							oşehir.remove("Gümüşvadi")
							botşehir.append("Gümüşvadi")
						if yerelordu[1]==0:
							if şehirler[1] in oşehir:
								asker=düşmanordu[3]
								düşmanordu[3]-=asker
								düşmanordu[1]+=asker
								oşehir.remove("Gümüşvadi")
								botşehir.append("Gümüşvadi")
					elif yerelordu[1]<düşmanordu[4]*2:
						asker=düşmanordu[4]
						düşmanordu[4]-=asker
						düşmanordu[1]+=asker
						self.oyun.savaşş(yerelordu[1],düşmanordu[1])
						g=liste[0]
						yerelordu.pop(1)
						yerelordu.insert(1,g)
						h=liste[1]
						düşmanordu.pop(1)
						düşmanordu.insert(1,h)
						if düşmanordu[1]>0:
							oşehir.remove("Gümüşvadi")
							botşehir.append("Gümüşvadi")
						if yerelordu[1]==0:
							if şehirler[1] in oşehir:
								asker=düşmanordu[4]
								düşmanordu[4]-=asker
								düşmanordu[1]+=asker
								oşehir.remove("Gümüşvadi")
								botşehir.append("Gümüşvadi")
					elif yerelordu[1]<düşmanordu[5]*2:
						asker=düşmanordu[5]
						düşmanordu[5]-=asker
						düşmanordu[1]+=asker
						self.oyun.savaşş(yerelordu[1],düşmanordu[1])
						g=liste[0]
						yerelordu.pop(1)
						yerelordu.insert(1,g)
						h=liste[1]
						düşmanordu.pop(1)
						düşmanordu.insert(1,h)
						if düşmanordu[1]>0:
							oşehir.remove("Gümüşvadi")
							botşehir.append("Gümüşvadi")
						if yerelordu[1]==0:
							if şehirler[1] in oşehir:
								asker=düşmanordu[5]
								düşmanordu[5]-=asker
								düşmanordu[1]+=asker
								oşehir.remove("Gümüşvadi")
								botşehir.append("Gümüşvadi")
				if şehirler[2] in oşehir:
					if yerelordu[2]<düşmanordu[0]*2:
						asker=düşmanordu[0]
						düşmanordu[0]-=asker
						düşmanordu[2]+=asker
						self.oyun.savaşş(yerelordu[2],düşmanordu[2])
						g=liste[0]
						yerelordu.pop(2)
						yerelordu.insert(2,g)
						h=liste[1]
						düşmanordu.pop(2)
						düşmanordu.insert(2,h)
						if düşmanordu[2]>0:
							oşehir.remove("Tekinhan")
							botşehir.append("Tekinhan")
						if yerelordu[2]==0:
							if şehirler[2] in oşehir:
								asker=düşmanordu[0]
								düşmanordu[0]-=asker
								düşmanordu[2]+=asker
								oşehir.remove("Tekinhan")
								botşehir.append("Tekinhan")
					elif yerelordu[2]<düşmanordu[1]*2:
						asker=düşmanordu[2]
						düşmanordu[1]-=asker
						düşmanordu[2]+=asker
						self.oyun.savaşş(yerelordu[2],düşmanordu[2])
						g=liste[0]
						yerelordu.pop(2)
						yerelordu.insert(2,g)
						h=liste[1]
						düşmanordu.pop(2)
						düşmanordu.insert(2,h)
						if düşmanordu[2]>0:
							oşehir.remove("Tekinhan")
							botşehir.append("Tekinhan")
						if yerelordu[2]==0:
							if şehirler[2] in oşehir:
								asker=düşmanordu[1]
								düşmanordu[1]-=asker
								düşmanordu[2]+=asker
								oşehir.remove("Tekinhan")
								botşehir.append("Tekinhan")
					elif yerelordu[2]<düşmanordu[3]*2:
						asker=düşmanordu[3]
						düşmanordu[3]-=asker
						düşmanordu[2]+=asker
						self.oyun.savaşş(yerelordu[2],düşmanordu[2])
						g=liste[0]
						yerelordu.pop(2)
						yerelordu.insert(2,g)
						h=liste[1]
						düşmanordu.pop(2)
						düşmanordu.insert(2,h)
						if düşmanordu[2]>0:
							oşehir.remove("Tekinhan")
							botşehir.append("Tekinhan")
						if yerelordu[2]==0:
							if şehirler[2] in oşehir:
								asker=düşmanordu[3]
								düşmanordu[3]-=asker
								düşmanordu[2]+=asker
								oşehir.remove("Tekinhan")
								botşehir.append("Tekinhan")
					elif yerelordu[2]<düşmanordu[4]*2:
						asker=düşmanordu[4]
						düşmanordu[4]-=asker
						düşmanordu[2]+=asker
						self.oyun.savaşş(yerelordu[2],düşmanordu[2])
						g=liste[0]
						yerelordu.pop(2)
						yerelordu.insert(2,g)
						h=liste[1]
						düşmanordu.pop(0)
						düşmanordu.insert(0,h)
						if düşmanordu[2]>0:
							oşehir.remove("Tekinhan")
							botşehir.append("Tekinhan")
						if yerelordu[2]==0:
							if şehirler[2] in oşehir:
								asker=düşmanordu[4]
								düşmanordu[4]-=asker
								düşmanordu[2]+=asker
								oşehir.remove("Tekinhan")
								botşehir.append("Tekinhan")
					elif yerelordu[2]<düşmanordu[5]*2:
						asker=düşmanordu[5]
						düşmanordu[5]-=asker
						düşmanordu[2]+=asker
						self.oyun.savaşş(yerelordu[2],düşmanordu[2])
						g=liste[0]
						yerelordu.pop(2)
						yerelordu.insert(2,g)
						h=liste[1]
						düşmanordu.pop(2)
						düşmanordu.insert(2,h)
						if düşmanordu[2]>0:
							oşehir.remove("Tekinhan")
							botşehir.append("Tekinhan")
						if yerelordu[2]==0:
							if şehirler[2] in oşehir:
								asker=düşmanordu[5]
								düşmanordu[5]-=asker
								düşmanordu[2]+=asker
								oşehir.remove("Tekinhan")
								botşehir.append("Tekinhan")
				if şehirler[3] in oşehir:
					if yerelordu[3]<düşmanordu[0]*2:
						asker=düşmanordu[0]
						düşmanordu[0]-=asker
						düşmanordu[3]+=asker
						self.oyun.savaşş(yerelordu[3],düşmanordu[3])
						g=liste[0]
						yerelordu.pop(3)
						yerelordu.insert(3,g)
						h=liste[1]
						düşmanordu.pop(3)
						düşmanordu.insert(3,h)
						if düşmanordu[3]>0:
							oşehir.remove("Grigon")
							botşehir.append("Grigon")
						if yerelordu[3]==0:
							if şehirler[3] in oşehir:
								asker=düşmanordu[0]
								düşmanordu[0]-=asker
								düşmanordu[3]+=asker
								oşehir.remove("Grigon")
								botşehir.append("Grigon")
					elif yerelordu[3]<düşmanordu[2]*2:
						asker=düşmanordu[2]
						düşmanordu[2]-=asker
						düşmanordu[3]+=asker
						self.oyun.savaşş(yerelordu[3],düşmanordu[3])
						g=liste[0]
						yerelordu.pop(3)
						yerelordu.insert(3,g)
						h=liste[1]
						düşmanordu.pop(3)
						düşmanordu.insert(3,h)
						if düşmanordu[3]>0:
							oşehir.remove("Grigon")
							botşehir.append("Grigon")
						if yerelordu[3]==0:
							if şehirler[3] in oşehir:
								asker=düşmanordu[2]
								düşmanordu[2]-=asker
								düşmanordu[3]+=asker
								oşehir.remove("Grigon")
								botşehir.append("Grigon")
					elif yerelordu[3]<düşmanordu[1]*2:
						asker=düşmanordu[1]
						düşmanordu[1]-=asker
						düşmanordu[3]+=asker
						self.oyun.savaşş(yerelordu[3],düşmanordu[3])
						g=liste[0]
						yerelordu.pop(3)
						yerelordu.insert(3,g)
						h=liste[1]
						düşmanordu.pop(3)
						düşmanordu.insert(3,h)
						if düşmanordu[3]>0:
							oşehir.remove("Grigon")
							botşehir.append("Grigon")
						if yerelordu[3]==0:
							if şehirler[3] in oşehir:
								asker=düşmanordu[1]
								düşmanordu[1]-=asker
								düşmanordu[3]+=asker
								oşehir.remove("Grigon")
								botşehir.append("Grigon")
					elif yerelordu[3]<düşmanordu[4]*2:
						asker=düşmanordu[4]
						düşmanordu[4]-=asker
						düşmanordu[3]+=asker
						self.oyun.savaşş(yerelordu[3],düşmanordu[3])
						g=liste[0]
						yerelordu.pop(3)
						yerelordu.insert(3,g)
						h=liste[1]
						düşmanordu.pop(3)
						düşmanordu.insert(3,h)
						if düşmanordu[3]>0:
							oşehir.remove("Gümüşvadi")
							botşehir.append("Gümüşvadi")
						if yerelordu[3]==0:
							if şehirler[3] in oşehir:
								asker=düşmanordu[4]
								düşmanordu[4]-=asker
								düşmanordu[3]+=asker
								oşehir.remove("Gümüşvadi")
								botşehir.append("Gümüşvadi")
					elif yerelordu[3]<düşmanordu[5]*2:
						asker=düşmanordu[5]
						düşmanordu[5]-=asker
						düşmanordu[3]+=asker
						self.oyun.savaşş(yerelordu[3],düşmanordu[3])
						g=liste[0]
						yerelordu.pop(3)
						yerelordu.insert(3,g)
						h=liste[1]
						düşmanordu.pop(3)
						düşmanordu.insert(3,h)
						if düşmanordu[3]>0:
							oşehir.remove("Grigon")
							botşehir.append("Grigon")
						if yerelordu[3]==0:
							if şehirler[3] in oşehir:
								asker=düşmanordu[5]
								düşmanordu[5]-=asker
								düşmanordu[3]+=asker
								oşehir.remove("Grigon")
								botşehir.append("Grigon")
				if şehirler[4] in oşehir:
					if yerelordu[4]<düşmanordu[0]*2:
						asker=düşmanordu[0]
						düşmanordu[0]-=asker
						düşmanordu[4]+=asker
						self.oyun.savaşş(yerelordu[4],düşmanordu[4])
						g=liste[0]
						yerelordu.pop(4)
						yerelordu.insert(4,g)
						h=liste[1]
						düşmanordu.pop(4)
						düşmanordu.insert(4,h)
						if düşmanordu[4]>0:
							oşehir.remove("Selaken")
							botşehir.append("Selaken")
						if yerelordu[4]==0:
							if şehirler[4] in oşehir:
								asker=düşmanordu[0]
								düşmanordu[0]-=asker
								düşmanordu[4]+=asker
								oşehir.remove("Selaken")
								botşehir.append("Selaken")
					elif yerelordu[4]<düşmanordu[2]*2:
						asker=düşmanordu[2]
						düşmanordu[2]-=asker
						düşmanordu[4]+=asker
						self.oyun.savaşş(yerelordu[4],düşmanordu[4])
						g=liste[0]
						yerelordu.pop(4)
						yerelordu.insert(4,g)
						h=liste[1]
						düşmanordu.pop(4)
						düşmanordu.insert(4,h)
						if düşmanordu[4]>0:
							oşehir.remove("Selaken")
							botşehir.append("Selaken")
						if yerelordu[4]==0:
							if şehirler[4] in oşehir:
								asker=düşmanordu[2]
								düşmanordu[2]-=asker
								düşmanordu[4]+=asker
								oşehir.remove("Selaken")
								botşehir.append("Selaken")
					elif yerelordu[4]<düşmanordu[3]*2:
						asker=düşmanordu[3]
						düşmanordu[3]-=asker
						düşmanordu[4]+=asker
						self.oyun.savaşş(yerelordu[4],düşmanordu[4])
						g=liste[0]
						yerelordu.pop(4)
						yerelordu.insert(4,g)
						h=liste[1]
						düşmanordu.pop(4)
						düşmanordu.insert(4,h)
						if düşmanordu[4]>0:
							oşehir.remove("Selaken")
							botşehir.append("Selaken")
						if yerelordu[4]==0:
							if şehirler[4] in oşehir:
								asker=düşmanordu[3]
								düşmanordu[3]-=asker
								düşmanordu[4]+=asker
								oşehir.remove("Selaken")
								botşehir.append("Selaken")
					elif yerelordu[4]<düşmanordu[1]*2:
						asker=düşmanordu[1]
						düşmanordu[1]-=asker
						düşmanordu[4]+=asker
						self.oyun.savaşş(yerelordu[4],düşmanordu[4])
						g=liste[0]
						yerelordu.pop(4)
						yerelordu.insert(4,g)
						h=liste[1]
						düşmanordu.pop(4)
						düşmanordu.insert(4,h)
						if düşmanordu[4]>0:
							oşehir.remove("Selaken")
							botşehir.append("Selaken")
						if yerelordu[4]==0:
							if şehirler[4] in oşehir:
								asker=düşmanordu[1]
								düşmanordu[1]-=asker
								düşmanordu[4]+=asker
								oşehir.remove("Selaken")
								botşehir.append("Selaken")
					elif yerelordu[4]<düşmanordu[5]*2:
						asker=düşmanordu[5]
						düşmanordu[5]-=asker
						düşmanordu[4]+=asker
						self.oyun.savaşş(yerelordu[4],düşmanordu[4])
						g=liste[0]
						yerelordu.pop(4)
						yerelordu.insert(4,g)
						h=liste[1]
						düşmanordu.pop(4)
						düşmanordu.insert(4,h)
						if düşmanordu[4]>0:
							oşehir.remove("Selaken")
							botşehir.append("Selaken")
						if yerelordu[4]==0:
							if şehirler[4] in oşehir:
								asker=düşmanordu[5]
								düşmanordu[5]-=asker
								düşmanordu[4]+=asker
								oşehir.remove("Selaken")
								botşehir.append("Selaken")
				if şehirler[5] in oşehir:
					if yerelordu[5]<düşmanordu[0]*2:
						asker=düşmanordu[0]
						düşmanordu[0]-=asker
						düşmanordu[5]+=asker
						self.oyun.savaşş(yerelordu[5],düşmanordu[5])
						g=liste[0]
						yerelordu.pop(5)
						yerelordu.insert(5,g)
						h=liste[1]
						düşmanordu.pop(5)
						düşmanordu.insert(5,h)
						if düşmanordu[5]>0:
							oşehir.remove("Konstiten")
							botşehir.append("Konstiten")
						if yerelordu[5]==0:
							if şehirler[5] in oşehir:
								asker=düşmanordu[0]
								düşmanordu[0]-=asker
								düşmanordu[5]+=asker
								oşehir.remove("Konstiten")
								botşehir.append("Konstiten")
					elif yerelordu[5]<düşmanordu[2]*2:
						asker=düşmanordu[2]
						düşmanordu[2]-=asker
						düşmanordu[5]+=asker
						self.oyun.savaşş(yerelordu[5],düşmanordu[5])
						g=liste[0]
						yerelordu.pop(5)
						yerelordu.insert(5,g)
						h=liste[1]
						düşmanordu.pop(5)
						düşmanordu.insert(5,h)
						if düşmanordu[5]>0:
							oşehir.remove("Konstiten")
							botşehir.append("Konstiten")
						if yerelordu[5]==0:
							if şehirler[5] in oşehir:
								asker=düşmanordu[2]
								düşmanordu[2]-=asker
								düşmanordu[5]+=asker
								oşehir.remove("Konstiten")
								botşehir.append("Konstiten")
					elif yerelordu[5]<düşmanordu[3]*2:
						asker=düşmanordu[3]
						düşmanordu[3]-=asker
						düşmanordu[5]+=asker
						self.oyun.savaşş(yerelordu[5],düşmanordu[5])
						g=liste[0]
						yerelordu.pop(5)
						yerelordu.insert(5,g)
						h=liste[1]
						düşmanordu.pop(5)
						düşmanordu.insert(5,h)
						if düşmanordu[5]>0:
							oşehir.remove("Konstiten")
							botşehir.append("Konstiten")
						if yerelordu[5]==0:
							if şehirler[5] in oşehir:
								asker=düşmanordu[3]
								düşmanordu[3]-=asker
								düşmanordu[5]+=asker
								oşehir.remove("Konstiten")
								botşehir.append("Konstiten")
					elif yerelordu[5]<düşmanordu[4]*2:
						asker=düşmanordu[4]
						düşmanordu[4]-=asker
						düşmanordu[5]+=asker
						self.oyun.savaşş(yerelordu[5],düşmanordu[5])
						g=liste[0]
						yerelordu.pop(5)
						yerelordu.insert(5,g)
						h=liste[1]
						düşmanordu.pop(5)
						düşmanordu.insert(5,h)
						if düşmanordu[5]>0:
							oşehir.remove("Konstiten")
							botşehir.append("Konstiten")
						if yerelordu[5]==0:
							if şehirler[5] in oşehir:
								asker=düşmanordu[4]
								düşmanordu[4]-=asker
								düşmanordu[5]+=asker
								oşehir.remove("Konstiten")
								botşehir.append("Konstiten")
					elif yerelordu[5]<düşmanordu[1]*2:
						asker=düşmanordu[1]
						düşmanordu[1]-=asker
						düşmanordu[5]+=asker
						self.oyun.savaşş(yerelordu[5],düşmanordu[5])
						g=liste[0]
						yerelordu.pop(5)
						yerelordu.insert(5,g)
						h=liste[1]
						düşmanordu.pop(5)
						düşmanordu.insert(5,h)
						if düşmanordu[5]>0:
							oşehir.remove("Konstiten")
							botşehir.append("Konstiten")
						if yerelordu[5]==0:
							if şehirler[5] in oşehir:
								asker=düşmanordu[1]
								düşmanordu[1]-=asker
								düşmanordu[5]+=asker
								oşehir.remove("Konstiten")
								botşehir.append("Konstiten")
		def düşmanordular(self):
			if self.oyun.düşmanpara>0:
				if self.oyun.toplamordu>self.oyun.düşmanordu:
					if şehirler[0] in botşehir:
						if düşmanordu[0]<yerelordu[1]:
							while düşmanordu[0]!=yerelordu[1] or düşmanordu[0]<yerelordu[1]:
								eski=düşmanordu[0]
								düşmanordu.pop(0)
								düşmanordu.insert(0,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[0]<yerelordu[2]:
							while düşmanordu[0]!=yerelordu[2] or düşmanordu[0]<yerelordu[2]:
								eski=düşmanordu[0]
								düşmanordu.pop(0)
								düşmanordu.insert(0,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[0]<yerelordu[3]:
							while düşmanordu[0]!=yerelordu[3] or düşmanordu[0]<yerelordu[3]:
								eski=düşmanordu[0]
								düşmanordu.pop(0)
								düşmanordu.insert(0,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[0]<yerelordu[4]:
							while düşmanordu[0]!=yerelordu[4] or düşmanordu[0]<yerelordu[4]:
								eski=düşmanordu[0]
								düşmanordu.pop(0)
								düşmanordu.insert(0,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[0]<yerelordu[5]:
							while düşmanordu[0]!=yerelordu[5] or düşmanordu[0]<yerelordu[5]:
								eski=düşmanordu[0]
								düşmanordu.pop(0)
								düşmanordu.insert(0,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break			
					if şehirler[1] in botşehir:
						if düşmanordu[1]<yerelordu[0]:
							while düşmanordu[1]!=yerelordu[0] or düşmanordu[1]<yerelordu[0]:
								eski=düşmanordu[1]
								düşmanordu.pop(1)
								düşmanordu.insert(1,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[1]<yerelordu[2]:
							while düşmanordu[1]!=yerelordu[2] or düşmanordu[1]<yerelordu[2]:
								eski=düşmanordu[1]
								düşmanordu.pop(1)
								düşmanordu.insert(1,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[1]<yerelordu[3]:
							while düşmanordu[1]!=yerelordu[3] or düşmanordu[1]<yerelordu[3]:
								eski=düşmanordu[1]
								düşmanordu.pop(1)
								düşmanordu.insert(1,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[1]<yerelordu[4]:
							while düşmanordu[1]!=yerelordu[4] or düşmanordu[1]<yerelordu[4]:
								eski=düşmanordu[1]
								düşmanordu.pop(1)
								düşmanordu.insert(1,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[1]<yerelordu[5]:
							while düşmanordu[1]!=yerelordu[5] or düşmanordu[1]<yerelordu[5]:
								eski=düşmanordu[1]
								düşmanordu.pop(1)
								düşmanordu.insert(1,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break			
					if şehirler[2] in botşehir:
						if düşmanordu[2]<yerelordu[0]:
							while düşmanordu[2]!=yerelordu[0] or düşmanordu[2]<yerelordu[0]:
								eski=düşmanordu[2]
								düşmanordu.pop(2)
								düşmanordu.insert(2,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[2]<yerelordu[1]:
							while düşmanordu[2]!=yerelordu[1] or düşmanordu[2]<yerelordu[1]:
								eski=düşmanordu[2]
								düşmanordu.pop(2)
								düşmanordu.insert(2,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[2]<yerelordu[3]:
							while düşmanordu[2]!=yerelordu[3] or düşmanordu[2]<yerelordu[3]:
								eski=düşmanordu[2]
								düşmanordu.pop(2)
								düşmanordu.insert(2,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[2]<yerelordu[4]:
							while düşmanordu[2]!=yerelordu[4] or düşmanordu[2]<yerelordu[4]:
								eski=düşmanordu[2]
								düşmanordu.pop(2)
								düşmanordu.insert(2,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[2]<yerelordu[5]:
							while düşmanordu[2]!=yerelordu[5] or düşmanordu[2]<yerelordu[5]:
								eski=düşmanordu[2]
								düşmanordu.pop(2)
								düşmanordu.insert(2,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break				
					if şehirler[3] in botşehir:
						if düşmanordu[3]<yerelordu[0]:
							while düşmanordu[3]!=yerelordu[0] or düşmanordu[3]<yerelordu[0]:
								eski=düşmanordu[3]
								düşmanordu.pop(3)
								düşmanordu.insert(3,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[3]<yerelordu[2]:
							while düşmanordu[3]!=yerelordu[2] or düşmanordu[3]<yerelordu[2]:
								eski=düşmanordu[3]
								düşmanordu.pop(3)
								düşmanordu.insert(3,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[3]<yerelordu[1]:
							while düşmanordu[3]!=yerelordu[1] or düşmanordu[3]<yerelordu[1]:
								eski=düşmanordu[3]
								düşmanordu.pop(3)
								düşmanordu.insert(3,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[3]<yerelordu[4]:
							while düşmanordu[3]!=yerelordu[4] or düşmanordu[3]<yerelordu[4]:
								eski=düşmanordu[3]
								düşmanordu.pop(3)
								düşmanordu.insert(3,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[3]<yerelordu[5]:
							while düşmanordu[3]!=yerelordu[5] or düşmanordu[3]<yerelordu[5]:
								eski=düşmanordu[3]
								düşmanordu.pop(3)
								düşmanordu.insert(3,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
					if şehirler[4] in botşehir:
						if düşmanordu[4]<yerelordu[0]:
							while düşmanordu[4]!=yerelordu[0] or düşmanordu[4]<yerelordu[0]:
								eski=düşmanordu[4]
								düşmanordu.pop(4)
								düşmanordu.insert(4,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[4]<yerelordu[2]:
							while düşmanordu[4]!=yerelordu[2] or düşmanordu[4]<yerelordu[2]:
								eski=düşmanordu[4]
								düşmanordu.pop(4)
								düşmanordu.insert(4,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[4]<yerelordu[3]:
							while düşmanordu[4]!=yerelordu[3] or düşmanordu[4]<yerelordu[3]:
								eski=düşmanordu[4]
								düşmanordu.pop(4)
								düşmanordu.insert(4,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[4]<yerelordu[1]:
							while düşmanordu[4]!=yerelordu[1] or düşmanordu[4]<yerelordu[1]:
								eski=düşmanordu[4]
								düşmanordu.pop(4)
								düşmanordu.insert(4,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[4]<yerelordu[5]:
							while düşmanordu[4]!=yerelordu[5] or düşmanordu[4]<yerelordu[5]:
								eski=düşmanordu[4]
								düşmanordu.pop(4)
								düşmanordu.insert(4,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break									
					if şehirler[5] in botşehir:
						if düşmanordu[5]<yerelordu[0]:
							while düşmanordu[5]!=yerelordu[0] or düşmanordu[5]<yerelordu[0]:
								eski=düşmanordu[5]
								düşmanordu.pop(5)
								düşmanordu.insert(5,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[5]<yerelordu[2]:
							while düşmanordu[5]!=yerelordu[2] or düşmanordu[5]<yerelordu[2]:
								eski=düşmanordu[5]
								düşmanordu.pop(5)
								düşmanordu.insert(5,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[5]<yerelordu[3]:
							while düşmanordu[5]!=yerelordu[3] or düşmanordu[5]<yerelordu[3]:
								eski=düşmanordu[5]
								düşmanordu.pop(5)
								düşmanordu.insert(5,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[5]<yerelordu[4]:
							while düşmanordu[5]!=yerelordu[4] or düşmanordu[5]<yerelordu[4]:
								eski=düşmanordu[5]
								düşmanordu.pop(5)
								düşmanordu.insert(5,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
						elif düşmanordu[5]<yerelordu[1]:
							while düşmanordu[5]!=yerelordu[1] or düşmanordu[5]<yerelordu[1]:
								eski=düşmanordu[5]
								düşmanordu.pop(5)
								düşmanordu.insert(5,eski+100)
								self.oyun.düşmanpara-=100
								if self.oyun.düşmanpara>=0:
									if self.oyun.düşmanordu>self.oyun.toplamordu:
										break			
								else:
									break
		def düşmandüzenle(self):
			pass	
	class şehirsistem():
		def __init__(self,oyun,kubanordu=200,gümüşvadiordu=200,tekinhanordu=200,grigonordu=0,selakenordu=0,konstitenordu=0):
			self.oyun=oyun
			self.kubanordu=kubanordu
			self.gümüşvadiordu=gümüşvadiordu
			self.tekinhanordu=tekinhanordu
			self.selakenordu=selakenordu
			self.konstitenordu=konstitenordu
			self.grigonordu=grigonordu
		def ordugör(self):
				print(self.oyun.aga*60)
				for i,k in zip(şehirler,yerelordu):
					if i in oşehir:
						print(i,"Asker Sayısı:",k)
				print(self.oyun.aga*60)
		def orduekle(self):
			while True:
				print(self.oyun.aga*60)
				for i,k in zip(şehirler,yerelordu):
					if i in oşehir:
						print(i,"Asker Sayısı:",k)
				print(self.oyun.aga*60)
				şehirseç=input("Hangi şehire asker basmak istiyorsunuz : ")
				if şehirseç=="q" or şehirseç=="Q":
					print("Çıkılıyor...")
					break
				elif şehirseç in oşehir:
					if şehirseç==şehirler[0]:
						asker_miktar=int(input("Kaç Asker eklemek istiyorsunuz : "))
						if self.oyun.para<asker_miktar:
							print("Paranız Yetersiz...")
						else:
							print("Ekleniyor...")
							self.oyun.para-=asker_miktar
							yerelordu[0]+=asker_miktar
							break
					elif şehirseç==şehirler[1]:
						asker_miktar=int(input("Kaç Asker eklemek istiyorsunuz : "))
						if self.oyun.para<asker_miktar:
							print("Paranız Yetersiz...")
						else:
							print("Ekleniyor...")
							self.oyun.para-=asker_miktar
							yerelordu[1]+=asker_miktar
							break
					elif şehirseç==şehirler[2]:
						asker_miktar=int(input("Kaç Asker eklemek istiyorsunuz : "))
						if self.oyun.para<asker_miktar:
							print("Paranız Yetersiz...")
						else:
							print("Ekleniyor...")
							self.oyun.para-=asker_miktar
							yerelordu[2]+=asker_miktar
							break
					elif şehirseç==şehirler[3]:
						asker_miktar=int(input("Kaç Asker eklemek istiyorsunuz : "))
						if self.oyun.para<asker_miktar:
							print("Paranız Yetersiz...")
						else:
							print("Ekleniyor...")
							self.oyun.para-=asker_miktar
							yerelordu[3]+=asker_miktar
							break	
					elif şehirseç==şehirler[4]:
						asker_miktar=int(input("Kaç Asker eklemek istiyorsunuz : "))
						if self.oyun.para<asker_miktar:
							print("Paranız Yetersiz...")
						else:
							print("Ekleniyor...")
							self.oyun.para-=asker_miktar
							yerelordu[4]+=asker_miktar
							break	
					elif şehirseç==şehirler[5]:
						asker_miktar=int(input("Kaç Asker eklemek istiyorsunuz : "))
						if self.oyun.para<asker_miktar:
							print("Paranız Yetersiz...")
						else:
							print("Ekleniyor...")
							self.oyun.para-=asker_miktar
							yerelordu[5]+=asker_miktar
							break	
		def ordueşitleme(self):
			self.kubanordu=yerelordu[0]
			self.gümüşvadiordu=yerelordu[1] 
			self.tekinhanordu=yerelordu[2]
			self.grigonordu=yerelordu[3]
			self.selakenordu=yerelordu[4]
			self.konstitenordu=yerelordu[5]
		def ordueşitleme1(self):
			yerelordu[0]=self.kubanordu
			yerelordu[1]=self.gümüşvadiordu
			yerelordu[2]=self.tekinhanordu
			yerelordu[3]=self.grigonordu
			yerelordu[4]=self.selakenordu
			yerelordu[5]=self.konstitenordu					
		def orduoynat(self):
			while True:
				try:	
					print(self.oyun.aga*60)
					for i,k in zip(şehirler,yerelordu):
						if i in oşehir:
							print(i+"+ Asker Sayısı:",k)
						if i in botşehir:
							print(i)
					print(self.oyun.aga*60)
					anaalan=input("Neredeki askerin yerini değiştireceksiniz : ")
					if anaalan=="q" or anaalan=="Q":
						print("kapanıyor")
						break
					elif anaalan in oşehir:
						if anaalan==şehirler[0]:
							asker_miktar=int(input("{} içinden kaç Asker Oynattıracaksınız: ".format(yerelordu[0])))
							if asker_miktar<=yerelordu[0]:
								değişiklik=input("Değiştirmek istediğiniz şehrin adını giriniz: ")
								
								if self.oyun.savaşdurumu=="Barış" and değişiklik in botşehir:
									print("savaş durumunda olmadığınız ülkenin sınırlarına giremezsiniz... ")
									continue
								
								elif self.oyun.savaşdurumu=="Savaş" and değişiklik in botşehir:
									if değişiklik==şehirler[1]:
										if düşmanordu[1]>=1:
											if anaalan==şehirler[0]:
												yerelordu[0] -= asker_miktar
												yerelordu[1] += asker_miktar
											elif değişiklik==şehirler[0]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[1],düşmanordu[1])
											g=liste[0]
											yerelordu.pop(1)
											yerelordu.insert(1,g)
											h=liste[1]
											düşmanordu.pop(1)
											düşmanordu.insert(1,h)
											if düşmanordu[1]==0:
												botşehir.remove("Gümüşvadi")
												oşehir.append("Gümüşvadi")
										elif düşmanordu[1]==0:
											yerelordu[0] -= asker_miktar
											yerelordu[1] += asker_miktar
											botşehir.remove("Gümüşvadi")
											oşehir.append("Gümüşvadi")									
									elif değişiklik==şehirler[2]:
										if düşmanordu[2]>=1:
											if anaalan==şehirler[0]:
												yerelordu[0] -= asker_miktar
												yerelordu[2] += asker_miktar
											elif değişiklik==şehirler[0]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[2],düşmanordu[2])
											g=liste[0]
											yerelordu.pop(2)
											yerelordu.insert(2,g)
											h=liste[1]
											düşmanordu.pop(2)
											düşmanordu.insert(2,h)
											if düşmanordu[2]==0:
												botşehir.remove("Tekinhan")
												oşehir.append("Tekinhan")
										elif düşmanordu[2]==0:
											yerelordu[0] -= asker_miktar
											yerelordu[2] += asker_miktar
											botşehir.remove("Tekinhan")
											oşehir.append("Tekinhan")
									elif değişiklik==şehirler[3]:
										if düşmanordu[3]>=1:
											if anaalan==şehirler[0]:
												yerelordu[0] -= asker_miktar
												yerelordu[3] += asker_miktar
											elif değişiklik==şehirler[0]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[3],düşmanordu[3])
											g=liste[0]
											yerelordu.pop(3)
											yerelordu.insert(3,g)
											h=liste[1]
											düşmanordu.pop(3)
											düşmanordu.insert(3,h)
											if düşmanordu[3]==0:
												botşehir.remove("Grigon")
												oşehir.append("Grigon")
										elif düşmanordu[3]==0:
											yerelordu[0] -= asker_miktar
											yerelordu[3] += asker_miktar
											botşehir.remove("Grigon")
											oşehir.append("Grigon")		
									elif değişiklik==şehirler[4]:
										if düşmanordu[4]>=1:
											if anaalan==şehirler[0]:
												yerelordu[0] -= asker_miktar
												yerelordu[4] += asker_miktar
											elif değişiklik==şehirler[0]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[4],düşmanordu[4])
											g=liste[0]
											yerelordu.pop(4)
											yerelordu.insert(4,g)
											h=liste[1]
											düşmanordu.pop(4)
											düşmanordu.insert(4,h)
											if düşmanordu[4]==0:
												botşehir.remove("Selaken")
												oşehir.append("Selaken")
										elif düşmanordu[4]==0:
											yerelordu[0] -= asker_miktar
											yerelordu[4] += asker_miktar
											botşehir.remove("Selaken")
											oşehir.append("Selaken")
									elif değişiklik==şehirler[5]:
										if düşmanordu[5]>=1:
											if anaalan==şehirler[0]:
												yerelordu[0] -= asker_miktar
												yerelordu[5] += asker_miktar
											elif değişiklik==şehirler[0]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[5],düşmanordu[5])
											g=liste[0]
											yerelordu.pop(5)
											yerelordu.insert(5,g)
											h=liste[1]
											düşmanordu.pop(5)
											düşmanordu.insert(5,h)
											if düşmanordu[5]==0:
												botşehir.remove("Konstiten")
												oşehir.append("Konstiten")
										elif düşmanordu[5]==0:
											yerelordu[0] -= asker_miktar
											yerelordu[5] += asker_miktar
											botşehir.remove("Konstiten")
											oşehir.append("Konstiten")		
								elif değişiklik in oşehir:
									if değişiklik==şehirler[1]:
										yerelordu[0] -= asker_miktar
										yerelordu[1] += asker_miktar
									elif değişiklik==şehirler[0]:
										print("Aynı Şehire İlerleyemezsiniz.")
										continue	
									elif değişiklik==şehirler[2]:
										yerelordu[0] -= asker_miktar
										yerelordu[2] += asker_miktar
									elif değişiklik==şehirler[3]:
										yerelordu[0] -= asker_miktar
										yerelordu[3] += asker_miktar
									elif değişiklik==şehirler[4]:
										yerelordu[0] -= asker_miktar
										yerelordu[4] += asker_miktar
									elif değişiklik==şehirler[5]:
										yerelordu[0] -= asker_miktar
										yerelordu[5] += asker_miktar
									else:
										print("hatalı işlem")
						elif anaalan==şehirler[1]:
							asker_miktar=int(input("{} içinden kaç Asker Oynattıracaksınız: ".format(yerelordu[1])))
							if asker_miktar<=yerelordu[1]:
								değişiklik=input("Değiştirmek istediğiniz şehrin adını giriniz: ")
								if self.oyun.savaşdurumu=="Barış" and değişiklik in botşehir:
									print("savaş durumunda olmadığınız ülkenin sınırlarına giremezsiniz... ")
									continue
								elif self.oyun.savaşdurumu=="Savaş" and değişiklik in botşehir:
									if değişiklik==şehirler[0]:
										if düşmanordu[0]>=1:
											if anaalan==şehirler[1]:
												yerelordu[1] -= asker_miktar
												yerelordu[0] += asker_miktar
											elif değişiklik==şehirler[1]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[0],düşmanordu[0])
											g=liste[0]
											yerelordu.pop(0)
											yerelordu.insert(0,g)
											h=liste[1]
											düşmanordu.pop(0)
											düşmanordu.insert(0,h)
											if düşmanordu[0]==0:
												botşehir.remove("Gümüşvadi")
												oşehir.append("Gümüşvadi")
										elif düşmanordu[0]==0:
											yerelordu[1] -= asker_miktar
											yerelordu[0] += asker_miktar
											botşehir.remove("Gümüşvadi")
											oşehir.append("Gümüşvadi")									
									elif değişiklik==şehirler[2]:
										if düşmanordu[2]>=1:
											if anaalan==şehirler[1]:
												yerelordu[1] -= asker_miktar
												yerelordu[2] += asker_miktar
											elif değişiklik==şehirler[1]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[2],düşmanordu[2])
											g=liste[0]
											yerelordu.pop(2)
											yerelordu.insert(2,g)
											h=liste[1]
											düşmanordu.pop(2)
											düşmanordu.insert(2,h)
											if düşmanordu[2]==0:
												botşehir.remove("Tekinhan")
												oşehir.append("Tekinhan")
										elif düşmanordu[2]==0:
											yerelordu[1] -= asker_miktar
											yerelordu[2] += asker_miktar
											botşehir.remove("Tekinhan")
											oşehir.append("Tekinhan")
									elif değişiklik==şehirler[3]:
										if düşmanordu[3]>=1:
											if anaalan==şehirler[1]:
												yerelordu[1] -= asker_miktar
												yerelordu[3] += asker_miktar
											elif değişiklik==şehirler[1]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[3],düşmanordu[3])
											g=liste[0]
											yerelordu.pop(3)
											yerelordu.insert(3,g)
											h=liste[1]
											düşmanordu.pop(3)
											düşmanordu.insert(3,h)
											if düşmanordu[3]==0:
												botşehir.remove("Grigon")
												oşehir.append("Grigon")
										elif düşmanordu[3]==0:
											yerelordu[1] -= asker_miktar
											yerelordu[3] += asker_miktar
											botşehir.remove("Grigon")
											oşehir.append("Grigon")		
									elif değişiklik==şehirler[4]:
										if düşmanordu[4]>=1:
											if anaalan==şehirler[1]:
												yerelordu[1] -= asker_miktar
												yerelordu[4] += asker_miktar
											elif değişiklik==şehirler[1]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[4],düşmanordu[4])
											g=liste[0]
											yerelordu.pop(4)
											yerelordu.insert(4,g)
											h=liste[1]
											düşmanordu.pop(4)
											düşmanordu.insert(4,h)
											if düşmanordu[4]==0:
												botşehir.remove("Selaken")
												oşehir.append("Selaken")
										elif düşmanordu[4]==0:
											yerelordu[1] -= asker_miktar
											yerelordu[4] += asker_miktar
											botşehir.remove("Selaken")
											oşehir.append("Selaken")
									elif değişiklik==şehirler[5]:
										if düşmanordu[5]>=1:
											if anaalan==şehirler[1]:
												yerelordu[1] -= asker_miktar
												yerelordu[5] += asker_miktar
											elif değişiklik==şehirler[1]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[5],düşmanordu[5])
											g=liste[0]
											yerelordu.pop(5)
											yerelordu.insert(5,g)
											h=liste[1]
											düşmanordu.pop(5)
											düşmanordu.insert(5,h)
											if düşmanordu[5]==0:
												botşehir.remove("Konstiten")
												oşehir.append("Konstiten")
										elif düşmanordu[5]==0:
											yerelordu[1] -= asker_miktar
											yerelordu[5] += asker_miktar
											botşehir.remove("Konstiten")
											oşehir.append("Konstiten")
								elif değişiklik in oşehir:
									if değişiklik==şehirler[0]:
										yerelordu[1] -= asker_miktar
										yerelordu[0] += asker_miktar								
									elif değişiklik==şehirler[1]:
										print("Aynı Şehire İlerleyemezsiniz.")
										continue	
									elif değişiklik==şehirler[2]:
										yerelordu[1] -= asker_miktar
										yerelordu[2] += asker_miktar
									elif değişiklik==şehirler[3]:
										yerelordu[1] -= asker_miktar
										yerelordu[3] += asker_miktar								
									elif değişiklik==şehirler[4]:
										yerelordu[1] -= asker_miktar
										yerelordu[4] += asker_miktar				
									elif değişiklik==şehirler[5]:
										yerelordu[1] -= asker_miktar
										yerelordu[5] += asker_miktar
									else:
										print("hatalı işlem")
						elif anaalan==şehirler[2]:
							asker_miktar=int(input("{} içinden kaç Asker Oynattıracaksınız: ".format(yerelordu[2])))
							if asker_miktar<=yerelordu[2]:
								değişiklik=input("Değiştirmek istediğiniz şehrin adını giriniz: ")
								if self.oyun.savaşdurumu=="Barış" and değişiklik in botşehir:
									print("savaş durumunda olmadığınız ülkenin sınırlarına giremezsiniz... ")
									continue
								elif self.oyun.savaşdurumu=="Savaş" and değişiklik in botşehir:
									if değişiklik==şehirler[1]:
										if düşmanordu[1]>=1:
											if anaalan==şehirler[2]:
												yerelordu[2] -= asker_miktar
												yerelordu[1] += asker_miktar
											elif değişiklik==şehirler[0]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[1],düşmanordu[1])
											g=liste[0]
											yerelordu.pop(1)
											yerelordu.insert(1,g)
											h=liste[1]
											düşmanordu.pop(1)
											düşmanordu.insert(1,h)
											if düşmanordu[1]==0:
												botşehir.remove("Gümüşvadi")
												oşehir.append("Gümüşvadi")
										elif düşmanordu[1]==0:
											yerelordu[2] -= asker_miktar
											yerelordu[1] += asker_miktar
											botşehir.remove("Gümüşvadi")
											oşehir.append("Gümüşvadi")									
									elif değişiklik==şehirler[0]:
										if düşmanordu[0]>=1:
											if anaalan==şehirler[2]:
												yerelordu[2] -= asker_miktar
												yerelordu[0] += asker_miktar
											elif değişiklik==şehirler[2]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[0],düşmanordu[0])
											g=liste[0]
											yerelordu.pop(0)
											yerelordu.insert(0,g)
											h=liste[1]
											düşmanordu.pop(0)
											düşmanordu.insert(0,h)
											if düşmanordu[0]==0:
												botşehir.remove("Tekinhan")
												oşehir.append("Tekinhan")
										elif düşmanordu[0]==0:
											yerelordu[2] -= asker_miktar
											yerelordu[0] += asker_miktar
											botşehir.remove("Tekinhan")
											oşehir.append("Tekinhan")
									elif değişiklik==şehirler[3]:
										if düşmanordu[3]>=1:
											if anaalan==şehirler[2]:
												yerelordu[2] -= asker_miktar
												yerelordu[3] += asker_miktar
											elif değişiklik==şehirler[2]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[3],düşmanordu[3])
											g=liste[0]
											yerelordu.pop(3)
											yerelordu.insert(3,g)
											h=liste[1]
											düşmanordu.pop(3)
											düşmanordu.insert(3,h)
											if düşmanordu[3]==0:
												botşehir.remove("Grigon")
												oşehir.append("Grigon")
										elif düşmanordu[3]==0:
											yerelordu[2] -= asker_miktar
											yerelordu[3] += asker_miktar
											botşehir.remove("Grigon")
											oşehir.append("Grigon")		
									elif değişiklik==şehirler[4]:
										if düşmanordu[4]>=1:
											if anaalan==şehirler[2]:
												yerelordu[2] -= asker_miktar
												yerelordu[4] += asker_miktar
											elif değişiklik==şehirler[2]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[4],düşmanordu[4])
											g=liste[0]
											yerelordu.pop(4)
											yerelordu.insert(4,g)
											h=liste[1]
											düşmanordu.pop(4)
											düşmanordu.insert(4,h)
											if düşmanordu[4]==0:
												botşehir.remove("Selaken")
												oşehir.append("Selaken")
										elif düşmanordu[4]==0:
											yerelordu[2] -= asker_miktar
											yerelordu[4] += asker_miktar
											botşehir.remove("Selaken")
											oşehir.append("Selaken")
									elif değişiklik==şehirler[5]:
										if düşmanordu[5]>=1:
											if anaalan==şehirler[2]:
												yerelordu[2] -= asker_miktar
												yerelordu[5] += asker_miktar
											elif değişiklik==şehirler[0]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[5],düşmanordu[5])
											g=liste[0]
											yerelordu.pop(5)
											yerelordu.insert(5,g)
											h=liste[1]
											düşmanordu.pop(5)
											düşmanordu.insert(5,h)
											if düşmanordu[5]==0:
												botşehir.remove("Konstiten")
												oşehir.append("Konstiten")
										elif düşmanordu[5]==0:
											yerelordu[2] -= asker_miktar
											yerelordu[5] += asker_miktar
											botşehir.remove("Konstiten")
											oşehir.append("Konstiten")
								elif değişiklik in oşehir:
									if değişiklik==şehirler[1]:
										yerelordu[2] -= asker_miktar
										yerelordu[1] += asker_miktar
									elif değişiklik==şehirler[2]:
										print("Aynı Şehire İlerleyemezsiniz.")
										continue	
									elif değişiklik==şehirler[0]:
										yerelordu[2] -= asker_miktar
										yerelordu[0] += asker_miktar
									elif değişiklik==şehirler[3]:
										yerelordu[2] -= asker_miktar
										yerelordu[3] += asker_miktar
									elif değişiklik==şehirler[4]:
										yerelordu[2] -= asker_miktar
										yerelordu[4] += asker_miktar
									elif değişiklik==şehirler[5]:
										yerelordu[2] -= asker_miktar
										yerelordu[5] += asker_miktar
									else:
										print("hatalı işlem")
						elif anaalan==şehirler[3]:
							asker_miktar=int(input("{} içinden kaç Asker Oynattıracaksınız: ".format(yerelordu[3])))
							if asker_miktar<=yerelordu[3]:
								değişiklik=input("Değiştirmek istediğiniz şehrin adını giriniz: ")
								if self.oyun.savaşdurumu=="Barış" and değişiklik in botşehir:
									print("savaş durumunda olmadığınız ülkenin sınırlarına giremezsiniz... ")
									continue
								elif self.oyun.savaşdurumu=="Savaş" and değişiklik in botşehir:
									if değişiklik==şehirler[1]:
										if düşmanordu[1]>=1:
											if anaalan==şehirler[3]:
												yerelordu[3] -= asker_miktar
												yerelordu[1] += asker_miktar
											elif değişiklik==şehirler[3]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[1],düşmanordu[1])
											g=liste[0]
											yerelordu.pop(1)
											yerelordu.insert(1,g)
											h=liste[1]
											düşmanordu.pop(1)
											düşmanordu.insert(1,h)
											if düşmanordu[1]==0:
												botşehir.remove("Gümüşvadi")
												oşehir.append("Gümüşvadi")
										elif düşmanordu[1]==0:
											yerelordu[3] -= asker_miktar
											yerelordu[1] += asker_miktar
											botşehir.remove("Gümüşvadi")
											oşehir.append("Gümüşvadi")									
									elif değişiklik==şehirler[2]:
										if düşmanordu[2]>=1:
											if anaalan==şehirler[3]:
												yerelordu[3] -= asker_miktar
												yerelordu[2] += asker_miktar
											elif değişiklik==şehirler[0]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[2],düşmanordu[2])
											g=liste[0]
											yerelordu.pop(2)
											yerelordu.insert(2,g)
											h=liste[1]
											düşmanordu.pop(2)
											düşmanordu.insert(2,h)
											if düşmanordu[2]==0:
												botşehir.remove("Tekinhan")
												oşehir.append("Tekinhan")
										elif düşmanordu[2]==0:
											yerelordu[3] -= asker_miktar
											yerelordu[2] += asker_miktar
											botşehir.remove("Tekinhan")
											oşehir.append("Tekinhan")
									elif değişiklik==şehirler[0]:
										if düşmanordu[0]>=1:
											if anaalan==şehirler[3]:
												yerelordu[3] -= asker_miktar
												yerelordu[0] += asker_miktar
											elif değişiklik==şehirler[3]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[0],düşmanordu[0])
											g=liste[0]
											yerelordu.pop(0)
											yerelordu.insert(0,g)
											h=liste[1]
											düşmanordu.pop(0)
											düşmanordu.insert(0,h)
											if düşmanordu[0]==0:
												botşehir.remove("Grigon")
												oşehir.append("Grigon")
										elif düşmanordu[0]==0:
											yerelordu[3] -= asker_miktar
											yerelordu[0] += asker_miktar
											botşehir.remove("Grigon")
											oşehir.append("Grigon")		
									elif değişiklik==şehirler[4]:
										if düşmanordu[4]>=1:
											if anaalan==şehirler[3]:
												yerelordu[3] -= asker_miktar
												yerelordu[4] += asker_miktar
											elif değişiklik==şehirler[3]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[4],düşmanordu[4])
											g=liste[0]
											yerelordu.pop(4)
											yerelordu.insert(4,g)
											h=liste[1]
											düşmanordu.pop(4)
											düşmanordu.insert(4,h)
											if düşmanordu[4]==0:
												botşehir.remove("Selaken")
												oşehir.append("Selaken")
										elif düşmanordu[4]==0:
											yerelordu[3] -= asker_miktar
											yerelordu[4] += asker_miktar
											botşehir.remove("Selaken")
											oşehir.append("Selaken")
									elif değişiklik==şehirler[5]:
										if düşmanordu[5]>=1:
											if anaalan==şehirler[3]:
												yerelordu[3] -= asker_miktar
												yerelordu[5] += asker_miktar
											elif değişiklik==şehirler[0]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[5],düşmanordu[5])
											g=liste[0]
											yerelordu.pop(5)
											yerelordu.insert(5,g)
											h=liste[1]
											düşmanordu.pop(5)
											düşmanordu.insert(5,h)
											if düşmanordu[5]==0:
												botşehir.remove("Konstiten")
												oşehir.append("Konstiten")
										elif düşmanordu[5]==0:
											yerelordu[3] -= asker_miktar
											yerelordu[5] += asker_miktar
											botşehir.remove("Konstiten")
											oşehir.append("Konstiten")
								elif değişiklik in oşehir:
									if değişiklik==şehirler[1]:
										yerelordu[3] -= asker_miktar
										yerelordu[1] += asker_miktar
									elif değişiklik==şehirler[3]:
										print("Aynı Şehire İlerleyemezsiniz.")
										continue	
									elif değişiklik==şehirler[0]:
										yerelordu[3] -= asker_miktar
										yerelordu[0] += asker_miktar
									elif değişiklik==şehirler[2]:
										yerelordu[3] -= asker_miktar
										yerelordu[2] += asker_miktar
									elif değişiklik==şehirler[4]:
										yerelordu[3] -= asker_miktar
										yerelordu[4] += asker_miktar
									elif değişiklik==şehirler[5]:
										yerelordu[3] -= asker_miktar
										yerelordu[5] += asker_miktar
									else:
										print("hatalı işlem")
						elif anaalan==şehirler[4]:
							asker_miktar=int(input("{} içinden kaç Asker Oynattıracaksınız: ".format(yerelordu[4])))
							if asker_miktar<=yerelordu[4]:
								değişiklik=input("Değiştirmek istediğiniz şehrin adını giriniz: ")
								if self.oyun.savaşdurumu=="Barış" and değişiklik in botşehir:
									print("savaş durumunda olmadığınız ülkenin sınırlarına giremezsiniz... ")
									continue
								elif self.oyun.savaşdurumu=="Savaş" and değişiklik in botşehir:
									if değişiklik==şehirler[1]:
										if düşmanordu[1]>=1:
											if anaalan==şehirler[4]:
												yerelordu[4] -= asker_miktar
												yerelordu[1] += asker_miktar
											elif değişiklik==şehirler[4]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[1],düşmanordu[1])
											g=liste[0]
											yerelordu.pop(1)
											yerelordu.insert(1,g)
											h=liste[1]
											düşmanordu.pop(1)
											düşmanordu.insert(1,h)
											if düşmanordu[1]==0:
												botşehir.remove("Gümüşvadi")
												oşehir.append("Gümüşvadi")
										elif düşmanordu[1]==0:
											yerelordu[4] -= asker_miktar
											yerelordu[1] += asker_miktar
											botşehir.remove("Gümüşvadi")
											oşehir.append("Gümüşvadi")									
									elif değişiklik==şehirler[2]:
										if düşmanordu[2]>=1:
											if anaalan==şehirler[4]:
												yerelordu[0] -= asker_miktar
												yerelordu[2] += asker_miktar
											elif değişiklik==şehirler[4]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[2],düşmanordu[2])
											g=liste[0]
											yerelordu.pop(2)
											yerelordu.insert(2,g)
											h=liste[1]
											düşmanordu.pop(2)
											düşmanordu.insert(2,h)
											if düşmanordu[2]==0:
												botşehir.remove("Tekinhan")
												oşehir.append("Tekinhan")
										elif düşmanordu[2]==0:
											yerelordu[4] -= asker_miktar
											yerelordu[2] += asker_miktar
											botşehir.remove("Tekinhan")
											oşehir.append("Tekinhan")
									elif değişiklik==şehirler[3]:
										if düşmanordu[3]>=1:
											if anaalan==şehirler[4]:
												yerelordu[4] -= asker_miktar
												yerelordu[3] += asker_miktar
											elif değişiklik==şehirler[4]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[3],düşmanordu[3])
											g=liste[0]
											yerelordu.pop(3)
											yerelordu.insert(3,g)
											h=liste[1]
											düşmanordu.pop(3)
											düşmanordu.insert(3,h)
											if düşmanordu[3]==0:
												botşehir.remove("Grigon")
												oşehir.append("Grigon")
										elif düşmanordu[3]==0:
											yerelordu[4] -= asker_miktar
											yerelordu[3] += asker_miktar
											botşehir.remove("Grigon")
											oşehir.append("Grigon")		
									elif değişiklik==şehirler[0]:
										if düşmanordu[0]>=1:
											if anaalan==şehirler[4]:
												yerelordu[4] -= asker_miktar
												yerelordu[0] += asker_miktar
											elif değişiklik==şehirler[4]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[0],düşmanordu[0])
											g=liste[0]
											yerelordu.pop(0)
											yerelordu.insert(0,g)
											h=liste[1]
											düşmanordu.pop(0)
											düşmanordu.insert(0,h)
											if düşmanordu[0]==0:
												botşehir.remove("Selaken")
												oşehir.append("Selaken")
										elif düşmanordu[0]==0:
											yerelordu[4] -= asker_miktar
											yerelordu[0] += asker_miktar
											botşehir.remove("Selaken")
											oşehir.append("Selaken")
									elif değişiklik==şehirler[5]:
										if düşmanordu[5]>=1:
											if anaalan==şehirler[4]:
												yerelordu[4] -= asker_miktar
												yerelordu[5] += asker_miktar
											elif değişiklik==şehirler[4]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[5],düşmanordu[5])
											g=liste[0]
											yerelordu.pop(5)
											yerelordu.insert(5,g)
											h=liste[1]
											düşmanordu.pop(5)
											düşmanordu.insert(5,h)
											if düşmanordu[5]==0:
												botşehir.remove("Konstiten")
												oşehir.append("Konstiten")
										elif düşmanordu[5]==0:
											yerelordu[4] -= asker_miktar
											yerelordu[5] += asker_miktar
											botşehir.remove("Konstiten")
											oşehir.append("Konstiten")
								elif değişiklik in oşehir:
									if değişiklik==şehirler[1]:
										yerelordu[4] -= asker_miktar
										yerelordu[1] += asker_miktar
									elif değişiklik==şehirler[4]:
										print("Aynı Şehire İlerleyemezsiniz.")
										continue	
									elif değişiklik==şehirler[2]:
										yerelordu[4] -= asker_miktar
										yerelordu[2] += asker_miktar
									elif değişiklik==şehirler[0]:
										yerelordu[4] -= asker_miktar
										yerelordu[0] += asker_miktar
									elif değişiklik==şehirler[3]:
										yerelordu[4] -= asker_miktar
										yerelordu[3] += asker_miktar
									elif değişiklik==şehirler[5]:
										yerelordu[4] -= asker_miktar
										yerelordu[5] += asker_miktar
									else:
										print("hatalı işlem")
						elif anaalan==şehirler[5]:
							asker_miktar=int(input("{} içinden kaç Asker Oynattıracaksınız: ".format(yerelordu[5])))
							if asker_miktar<=yerelordu[5]:
								değişiklik=input("Değiştirmek istediğiniz şehrin adını giriniz: ")
								if self.oyun.savaşdurumu=="Barış" and değişiklik in botşehir:
									print("savaş durumunda olmadığınız ülkenin sınırlarına giremezsiniz... ")
									continue
								elif self.oyun.savaşdurumu=="Savaş" and değişiklik in botşehir:
									if değişiklik==şehirler[1]:
										if düşmanordu[1]>=1:
											if anaalan==şehirler[5]:
												yerelordu[5] -= asker_miktar
												yerelordu[1] += asker_miktar
											elif değişiklik==şehirler[5]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[1],düşmanordu[1])
											g=liste[0]
											yerelordu.pop(1)
											yerelordu.insert(1,g)
											h=liste[1]
											düşmanordu.pop(1)
											düşmanordu.insert(1,h)
											if düşmanordu[1]==0:
												botşehir.remove("Gümüşvadi")
												oşehir.append("Gümüşvadi")
										elif düşmanordu[1]==0:
											yerelordu[5] -= asker_miktar
											yerelordu[1] += asker_miktar
											botşehir.remove("Gümüşvadi")
											oşehir.append("Gümüşvadi")									
									elif değişiklik==şehirler[2]:
										if düşmanordu[2]>=1:
											if anaalan==şehirler[5]:
												yerelordu[5] -= asker_miktar
												yerelordu[2] += asker_miktar
											elif değişiklik==şehirler[5]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[2],düşmanordu[2])
											g=liste[0]
											yerelordu.pop(2)
											yerelordu.insert(2,g)
											h=liste[1]
											düşmanordu.pop(2)
											düşmanordu.insert(2,h)
											if düşmanordu[2]==0:
												botşehir.remove("Tekinhan")
												oşehir.append("Tekinhan")
										elif düşmanordu[2]==0:
											yerelordu[5] -= asker_miktar
											yerelordu[2] += asker_miktar
											botşehir.remove("Tekinhan")
											oşehir.append("Tekinhan")
									elif değişiklik==şehirler[3]:
										if düşmanordu[3]>=1:
											if anaalan==şehirler[5]:
												yerelordu[5] -= asker_miktar
												yerelordu[3] += asker_miktar
											elif değişiklik==şehirler[5]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[3],düşmanordu[3])
											g=liste[0]
											yerelordu.pop(3)
											yerelordu.insert(3,g)
											h=liste[1]
											düşmanordu.pop(3)
											düşmanordu.insert(3,h)
											if düşmanordu[3]==0:
												botşehir.remove("Grigon")
												oşehir.append("Grigon")
										elif düşmanordu[3]==0:
											yerelordu[5] -= asker_miktar
											yerelordu[3] += asker_miktar
											botşehir.remove("Grigon")
											oşehir.append("Grigon")		
									elif değişiklik==şehirler[4]:
										if düşmanordu[4]>=1:
											if anaalan==şehirler[5]:
												yerelordu[5] -= asker_miktar
												yerelordu[4] += asker_miktar
											elif değişiklik==şehirler[5]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[4],düşmanordu[4])
											g=liste[0]
											yerelordu.pop(4)
											yerelordu.insert(4,g)
											h=liste[1]
											düşmanordu.pop(4)
											düşmanordu.insert(4,h)
											if düşmanordu[4]==0:
												botşehir.remove("Selaken")
												oşehir.append("Selaken")
										elif düşmanordu[4]==0:
											yerelordu[5] -= asker_miktar
											yerelordu[4] += asker_miktar
											botşehir.remove("Selaken")
											oşehir.append("Selaken")
									elif değişiklik==şehirler[0]:
										if düşmanordu[0]>=1:
											if anaalan==şehirler[5]:
												yerelordu[5] -= asker_miktar
												yerelordu[0] += asker_miktar
											elif değişiklik==şehirler[5]:
												print("Aynı Şehire İlerleyemezsiniz.")
												continue	
											self.oyun.savaşş(yerelordu[0],düşmanordu[0])
											g=liste[0]
											yerelordu.pop(0)
											yerelordu.insert(0,g)
											h=liste[1]
											düşmanordu.pop(0)
											düşmanordu.insert(0,h)
											if düşmanordu[0]==0:
												botşehir.remove("Konstiten")
												oşehir.append("Konstiten")
										elif düşmanordu[0]==0:
											yerelordu[5] -= asker_miktar
											yerelordu[0] += asker_miktar
											botşehir.remove("Konstiten")
											oşehir.append("Konstiten")
								elif değişiklik in oşehir:
									if değişiklik==şehirler[1]:
										yerelordu[5] -= asker_miktar
										yerelordu[1] += asker_miktar
									elif değişiklik==şehirler[5]:
										print("Aynı Şehire İlerleyemezsiniz.")
										continue	
									elif değişiklik==şehirler[2]:
										yerelordu[5] -= asker_miktar
										yerelordu[0] += asker_miktar
									elif değişiklik==şehirler[3]:
										yerelordu[5] -= asker_miktar
										yerelordu[3] += asker_miktar
									elif değişiklik==şehirler[4]:
										yerelordu[5] -= asker_miktar
										yerelordu[4] += asker_miktar
									elif değişiklik==şehirler[0]:
										yerelordu[5] -= asker_miktar
										yerelordu[0] += asker_miktar
									else:
										print("hatalı işlem")
					else:
						print("Bu Şehir Sizin Sınırlarınız içerisinde değil!")
						time.sleep(1)
				except:
					print("Hatalı giriş")
	def savaşş(self,x,y):
		global liste
		global liste2
		while True:	
			liste.clear()
			liste2.clear()	    
			ihtimal=random.randint(0,10)
			print(ihtimal)
			if x>y:
				if ihtimal>=6:
					ihtimal-=1
			elif y>x:
				if ihtimal<=5:
					ihtimal+=1
			print(ihtimal)             
			if ihtimal==0 or ihtimal==1 or ihtimal==2 or ihtimal==3 or ihtimal==4 or ihtimal==5:
				print("üstünlük sende")
				işlem=random.randint(1,10)
				if işlem==1:
					x-=x*10/100
					y-=y*2/100
				elif işlem==2 or işlem==3 or işlem==4 or işlem==5:
					x-=x*5/100
					y-=y*5/100
				elif işlem==6 or işlem==7:
					x-=x*5/100
					y-=y*10/100
				elif işlem==8 or işlem==9 or işlem==10:
					x-=x*5/100
					y-=y*15/100      
			if ihtimal==6 or ihtimal==7 or ihtimal==8 or ihtimal==9 or ihtimal==10 or ihtimal>=11:
				print("üstünlük rakipte")
				işlem2=random.randint(1,10)
				print(işlem2)
				if işlem2==1:
					x-=x*2/100
					y-=y*10/100
				elif işlem2==2 or işlem2==3 or işlem2==4 or işlem2==5:
					x-=x*5/100
					y-=y*5/100
				elif işlem2==6 or işlem2==7:
					x-=x*10/100
					y-=y*5/100
				elif işlem2==8 or işlem2==9 or işlem2==10:
					x-=x*15/100
					y-=y*5/100 	            
			if x<=10 or y<=10:
				if x<=10:
					x=0
					print("kaybettiniz.")
				elif y<=10:
					y=0  
					print("kazandınız...")
				print("bitti")
				x=round(x)
				y=round(y)
				if len(liste)>=1:
					liste2.append(x)
					liste2.append(y)
				else:
					liste.append(x)
					liste.append(y)
				print(liste)
				print("Kalan Ordun:",x)
				break
	def başlat(self):
		print("-"*30)
		başkanadı=input("Başkan Adınızı Seçiniz : ")
		print("-"*30)
		self.başkan=başkanadı
	def savaşyüzdesi(self):
		global yüzde
		global sayı
		if self.ilişki>0:
			yüzde=random.randint(1,1000)
			sayı=random.randint(1,1000)
			if yüzde==sayı:
				print("Savaş ilanı!")
				#self.savaşdurumu="Aktif" olması için burada fonksiyon çalıştırcaz
		elif self.ilişki<0:
			yüzde=random.randint(1,900)
			sayı=random.randint(1,900)
			if yüzde==sayı:
				print("Savaş ilanı!")
				#self.savaşdurumu="Aktif" olması için burada fonksiyon çalıştırcaz
		elif self.ilişki<-10:
			yüzde=random.randint(1,700)
			sayı=random.randint(1,700)
			if yüzde==sayı:
				print("Savaş ilanı!")
		elif self.ilişki<-20:
			yüzde=random.randint(1,600)
			sayı=random.randint(1,600)
			if yüzde==sayı:
				print("Savaş ilanı!")
		elif self.ilişki<-30:
			yüzde=random.randint(1,500)
			sayı=random.randint(1,500)
			if yüzde==sayı:
				print("Savaş ilanı!")
		elif self.ilişki<-40:
			yüzde=random.randint(1,400)
			sayı=random.randint(1,400)
			if yüzde==sayı:
				print("Savaş ilanı!")
		elif self.ilişki<-50:
			yüzde=random.randint(1,300)
			sayı=random.randint(1,300)
			if yüzde==sayı:
				print("Savaş ilanı!")
		elif self.ilişki<-60:
			yüzde=random.randint(1,200)
			sayı=random.randint(1,200)
			if yüzde==sayı:
				print("Savaş ilanı!")
		elif self.ilişki<-70:
			yüzde=random.randint(1,200)
			sayı=random.randint(1,200)
			if yüzde==sayı:
				print("Savaş ilanı!")						
		elif self.ilişki<-80:
			yüzde=random.randint(1,100)
			sayı=random.randint(1,100)
			if yüzde==sayı:
				print("Savaş ilanı!")
		elif self.ilişki<-90:
			yüzde=random.randint(1,50)
			sayı=random.randint(1,50)
			if yüzde==sayı:
				print("Savaş ilanı!")
		elif self.ilişki==-99:
			yüzde=random.randint(1,10)
			sayı=random.randint(1,10)
			if yüzde==sayı:
				print("Savaş ilanı!")		
	def rakipsavaşilanı(self):
		if yüzde==sayı:
			self.savaşdurumu="Savaş"
	def savaşilanı(self):
		if self.savaşdurumu=="Barış":
			self.savaşdurumu="Savaş"
		elif self.savaşdurumu=="Savaş":
			print("Zaten Bu ülke ile savaştasınız.!")	
	def toplamordum(self):
		self.toplamordu-=self.toplamordu
		for i in yerelordu:
			self.toplamordu += i
		self.düşmanordu-=self.düşmanordu
		for b in düşmanordu:
			self.düşmanordu+=i
		print("brr")	
	def haritayabak(self):
			for i in şehirler:
				if i in oşehir:
					print(i+"+")
				else:
					print(i)
	def güngeç(self):
		self.gün += 1
		self.şehirsistem.ordueşitleme()	
		if len(oşehir)==1:
			self.para += 100
		elif len(oşehir)==2:
			self.para += 200
		elif len(oşehir)==3:
			self.para += 300
		elif len(oşehir)==4:
			self.para += 400
		elif len(oşehir)==5:
			self.para += 500
		else:
			print(":D")
		self.ilişki -= 1
		if self.ilişki<-99:
			self.ilişki=-99
		elif self.ilişki>99:
			self.ilişki=99
		self.toplamordu-=self.toplamordu
		for i in yerelordu:
			self.toplamordu+=i
		self.düşmanordu-=self.düşmanordu
		for b in düşmanordu:
			self.düşmanordu+=b	
		self.savaşyüzdesi()
		self.rakipsavaşilanı()
		print("Yeni Güne Geçtiniz!")
		print(düşmanordu)			
	
	def diplomasipaneli(self):
		print("""
{}
\tÜlke Başkanı: {}\tİlişkiniz: {}\tDiplomatik Durum: {}
{}
1)Savaş İlan Et/Barış İmzala
2)İlişkini İyileştir
3)İlişkini Kötüleştir
4)
5)
{}
Q)Menüye Geri Dön
					""".format(self.aga*60,botbaşkan,self.ilişki,self.savaşdurumu,self.aga*60,self.aga*60))
	def __str__(self):
			return("""
{}
\t\t      Ülke Başkanı: {}
{}
Mevcut Toplam Ordun: {}\t\tMevcut Paran: {}
{}
1)Gün Geç
2)Haritaya Bak
3)Asker Panel
4)Teknoloji Geliştir
5)Diplomasi
6)Bildirimler
					""".format(self.aga*60,self.başkan,self.aga*60,self.toplamordu,self.para,self.aga*60))
	def askeral(self):
		print("""
{}
Paranız: {}         Asker Durumunuz: {}
{}
Şehir Seçimi Yapınız: 
{}
{}			""".format(self.aga*60,self.para,self.toplamordu,self.aga*60,self.aga*60,oşehir))
		input("Bir Seçim Yapınız: ")


furkan=oyun()
furkan.şehirsistem.ordueşitleme()
furkan.savaşş(yerelordu[1],düşmanordu[5])
print(yerelordu[1],düşmanordu[5])
furkan.başlat()
furkan.toplamordum()


while True:
	print(furkan)
	işlem=input("Hangi İşlemi Yapacaksınız : ")
	if işlem=="1":
		furkan.güngeç()
		furkan.bot.botgüngeç()
		furkan.bot.düşmanordular()
	elif işlem=="2":
		furkan.haritayabak()
	elif işlem=="3":
		print("""
------------------------------------------
1)Asker Al
2)Asker Azalt
3)Askerlerin Yerini Değiştir
------------------------------------------
			""")
		işlem=input("Bir İşlem Seçiniz : ")
		if işlem=="q" or işlem=="Q":
			break
		elif işlem=="1":
			furkan.şehirsistem.orduekle()
		elif işlem=="2":
			pass
		elif işlem=="3":
			furkan.şehirsistem.orduoynat()
		else:
			print("Geçersiz işlem")
			time.sleep(1)			
	elif işlem=="4":
		pass
	elif işlem=="5":
		furkan.diplomasipaneli()
		işlem=input("Bir İşlem Seçiniz : ")
		if işlem=="1":
			furkan.savaşilanı()
	elif işlem=="6":
		pass



