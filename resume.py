Header = '>>>This resume is totally made up with the help of python.'
Name = 'Richa Verma'
Title = 'vricha211697@gmail.com'
Contact = '632607'
add ='Lakhimpur-Kheri'
SkillsHeader = 'SKILLS'
SkillsDesc= '. Python\n. C\n. DBMS\n. Creative Thinking\n. SQL\n. Operating System\n. Data Structure and Algorithms\n. Mathematics\n. Problem Solving'
Languages = 'LANGUAGES'
LanguagesDesc = ' Hindi\n English\n Punjabi'
Objective='OBJECTIVE'
Obj = ' As a recent graduate,I am seeking a role which allows\n me to continue learning and perfecting my skills as I\n provide high-quality work,and encourages me to\n flourish as a Software Engineer.'
MyTime = 'MY WORKS'
mytimedesc = '. Billing Software\n. Resume with lot of Annotations\n. Student Management System \n. Chatbot using IBM WATSON'
quote='let\'s speak the CODE'
Education = 'EDUCATION'
a='Bachelor Of Technology'
b='APJ Abdul Kalam Technical University'
c='2016-2020'
d='Higher Secondary Certificate '
e='City Montessori School'
f='2014-2015'
g='Seconary School Certificate'
h='Jawahar Navodaya Vidyalya'
i='2012-2013'
j='PASSION'
k=' Chess\n Writing\n Sketching\n Solving Puzzles'
l='FIND ME ONLINE'
m=' @vricha211697\n @/richa-verma-20895315a'
n='MY LIFE PHILOSOPHY'
o=' Anyone who has ever made anything of\n importance was Hardwork,Determination\n and Disciplined.'
import  matplotlib.pyplot as plt
from matplotlib.offsetbox import  TextArea,DrawingArea,OffsetImage,AnnotationBbox
import matplotlib.image as mpimg
#import numpy as np
#import  pandas as pd

plt.rcParams['font.family'] = 'DejaVu Sans' #runtime configuration contains the default styles for every plot element you create
fig,ax = plt.subplots(figsize=(8.5,11))


#new.axis('off')

ax.set_title('RESUME',weight="bold")
ax.axvline(x=.5,ymin=0,ymax=1,color='#007ACC',alpha=0.0,linewidth = 50)
plt.axvline(x=0.1,color='#000000',alpha=0.5,linewidth=300)
#plt.axhline(y=.88,xmin=0,xmax=1,color='black',linewidth=3)

ax.set_facecolor('White')
plt.axis('off')
plt.annotate(Header,(0.45,0.98),weight='regular',fontsize=8,alpha = 0.75)
plt.annotate(Name,(0.04,.96),weight='bold',fontsize=22)
plt.annotate(Title,(0.06,.93),weight='regular',color='blue',fontsize=10)
plt.annotate(Contact,(0.12,.91),weight='regular',fontsize=10,color='#ffffff')
plt.annotate(add,(0.1,.89),weight='regular',fontsize=10,color='#ffffff')
plt.axhline(y=.85,xmin=0,xmax=0.396,color='black',linewidth=20)
plt.annotate(SkillsHeader,(0.02,.84),weight='bold',color='white',fontsize=14)
plt.annotate(SkillsDesc,(0.02,.66),weight='bold',color='white',fontsize=10)
plt.axhline(y=.60,xmin=0,xmax=0.396,color='black',linewidth=20)
plt.annotate(Languages,(0.02,.59),weight='bold',color='white',fontsize=14)
plt.annotate(LanguagesDesc,(0.02,.51),weight='bold',color='white',fontsize=10)
plt.axhline(y=.45,xmin=0,xmax=0.396,color='black',linewidth=20)
plt.annotate(MyTime,(0.02,.44),weight='bold',color='white',fontsize=14)
plt.annotate(mytimedesc,(0.02,.36),weight='bold',color='white',fontsize=10)
plt.annotate(quote,(0.02,.32),weight='bold',color='#C5B53B',fontsize=10)
plt.annotate(Objective,(0.44,.95),weight='bold',color='black',fontsize=14)
plt.annotate(Obj,(0.44,.87),weight='regular',color='black',fontsize=10)
plt.axhline(y=.86,xmin=0.44,xmax=1,color='black',linewidth=1)
plt.annotate(Education,(0.44,.82),weight='bold',color='black',fontsize=14)
plt.annotate(a,(0.44,.78),weight='bold',color='black',fontsize=12)
plt.annotate(b,(0.44,.76),weight='bold',color='#C5B53B',fontsize=10)
plt.annotate(c,(0.44,.74),weight='regular',color='black',fontsize=10)
plt.annotate(d,(0.44,.70),weight='bold',color='black',fontsize=12)
plt.annotate(e,(0.44,.68),weight='bold',color='#C5B53B',fontsize=10)
plt.annotate(f,(0.44,.66),weight='regular',color='black',fontsize=10)
plt.annotate(g,(0.44,.62),weight='bold',color='black',fontsize=12)
plt.annotate(h,(0.44,.60),weight='bold',color='#C5B53B',fontsize=10)
plt.annotate(i,(0.44,.58),weight='regular',color='black',fontsize=10)
plt.axhline(y=.56,xmin=0.44,xmax=1,color='black',linewidth=1)
plt.annotate(j,(0.44,.52),weight='bold',color='black',fontsize=14)
plt.annotate(k,(0.44,.44),weight='regular',color='black',fontsize=10)
plt.axhline(y=.40,xmin=0.44,xmax=1,color='black',linewidth=1)
plt.annotate(l,(0.44,.36),weight='bold',color='black',fontsize=14)
plt.annotate(m,(0.44,.31),weight='regular',color='black',fontsize=10)
plt.axhline(y=.28,xmin=0.44,xmax=1,color='black',linewidth=1)
plt.annotate(n,(0.44,.24),weight='bold',color='black',fontsize=14)
plt.annotate(o,(0.44,.18),weight='bold',fontsize=10,color='#C5B53B')


#adding image

#img = mpimg.imread('C:\\shitty\\MSTI\\imagefiles\\richhh.jpg')
#imagebox = OffsetImage(img,zoom=0.025)
#ab = AnnotationBbox(imagebox,(0.06,0.91))
#ax.add_artist(ab)
#plt.show()
plt.savefig('resumeeeee.png',dpi=300,bbox_inches='tight')
