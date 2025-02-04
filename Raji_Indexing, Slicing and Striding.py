#Indexing
a="vijayawada"
a[2]
'j'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
 
 
b="i love vijayawada"
b[3]+b[4]+b[5]+b[6]
'ove '
b[2]+b[3]+b[4]+b[5]
'love'
b[7]+b[8]+b[9]+b[10]+b[11]+b[12]+b[13]+b[14]+b[15]+b[16]
'vijayawada'

a="Beautiful is better than ugly"
a[25]+a[26]+a[27]+a[28]
'ugly'
a[13]+a[14]+a[15]+a[16]+a[17]+a[18]
'better'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]
'Beautiful'

a="Team work"
a[0]+a[1]+a[2]
'Tea'
a[5]+a[6]+a[7]+a[8]
'work'

#Negative indexing
a="rani papa"
a[-1]+a[-2]+a[-3]+a[-4]
'apap'
a[-4]+a[-3]+a[-2]+a[-1]
'papa'
a[-9]+a[-8]+a[-7]+a[-6]
'rani'
a="work until you succeed"
a[-11]+a[-10]+a[-9]
'you'
a[-17]+a[-16]+a[-15]+a[-14]+a[-13]
'until'
a[-22]+a[-21]+a[-20]+a[-19]
'work'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'succeed'
a="i am learning python"
a[-15]+a[-14]+a[-13]+a[-12]+a[-11]
'learn'
a[-18]+a[-17]
'am'


#slicing
a="caratredj"
a[0:4]
'cara'
a[4:8]
'tredj'

a="simple is better than complex"
a[21:28]
' comple'
a[22:29]
'complex'
a[10:16]
'better'
a[0:6]
'simple'
a[17:21]
'than'
a="vizag is city of destiny"
a[0:5]
'vizag'
a[17:24]
'destiny'

#Negative slicing
a="india wins the world cup"
a[-24:-19]
'india'
a[-9:-4]
'world'
a[-18:-15]
'win'
a[-4:-1]
' cu'
a[-4:-0]
''
a[-3:]
'cup'
a="east or west vijayawada is best"
a[-23:-19]
'west'
a[-4:]
'best'
a[-31:-27]
'east'
a[-18:-8]
'vijayawada'
a="why not 175"
a[-3:]
'175'
a[-11:-8]
'why'
a[-7:-4]
'not'

