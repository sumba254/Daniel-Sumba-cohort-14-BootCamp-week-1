'''class Add:
	"""docstring for add"""

	def __init__(self, skill,status):
		self.skill = skill
		self.status = status
	
	def skill(self):
		return '{} {}'.format(self.skill, self.status)




skill_1 = Add('python', 'studied')
skill_2 = Add('python', 'unstudied')


print (Add.skill(skill_2))
print (Add.skill(skill_1))'''
from psa import *


class viewSkill(PSA):
	
	def __init__(self, database):
		super(viewSkill,self).__init__(database)
		for item in database:
			if item[skill] == None:
				self.skill = []
			else:
				self.skill = skill
	
	def viewAll(self):
		for item in self.skill:
			print ('-->', skill)
    
	def viewStudied(self):
		studiedskills = []
		for status in skill:
	   		if status == studied:
	   			studiedskills.append(skill)
	   			print studiedskills


   	def veiwUnstudied():
   		unstudiedskills=[]
   		for status in skill:
	   		if status == unstudied:
	   			unstudiedskills.append(skill)
	   			print unstudiedskills
 

   	def viewProgress():
   		progress = (len(studiedskills)/len(skills))*100
   		print progress




