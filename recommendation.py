import eyed3
import sys
import os
import urllib2
import random

start=0
start2=500

dicti = {'a':0}
dict2={'b':0}
lister=['Absorbing the Power of the internet....','Linux is Love, Linux is life','I like progressive rock, what\'s your taste?','Music Music Music!','Mmmm that song\'s amazing','Rivers know this: there is no hurry. We shall get there some day.','There is no pain....','Thanks to Last.FM for their API','One good thing about music, when it hits you, you feel no pain','Siddharth\'s my name in case you wanted to know','Hate Waiting, don\'t you?','Written with love on Python']
opener = urllib2.build_opener(
                urllib2.HTTPHandler(),
                urllib2.HTTPSHandler(),
                urllib2.ProxyHandler({'http': '10.3.100.207:8080'}))


def downdata(tracks,artist,start,start2,dicti,lister):
	urllib2.install_opener(opener)
	link = "http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist="
	b="&track="
	art=artist
	tra=tracks
	link=link+art+b+tra
	link=link+"&api_key=6a3498b0806fbc8c7e7b865aa704aaab&format=json"
	a=urllib2.urlopen(link).read()
	print(random.choice(lister))
	for i in range(5):
		start2=a.find('t":{"name":',start2)
		temp2=a.find("mbid",start2)
		#print a[start2+12:temp2-3]
		artistdata=a[start2+12:temp2-3]
		start2=temp2
		start=a.find('},{"name":',start)
		temp=a.find("playcount",start)
		trackdata=a[start+11:temp-3]
		#print trackdata
		start=temp
		#print ""
		dicti[trackdata] = dicti.get(trackdata, 0) + 1
		dict2.update({trackdata:artistdata})
	

	#print max(dicti, key=dicti.get)
	#print dicti


def mp3gen():
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3" or os.path.splitext(filename)[1] == ".Mp3":
                yield os.path.join(root, filename)

for mp3file in mp3gen(): 
	audio=eyed3.load(mp3file)
	downdata(audio.tag.title,audio.tag.artist,start,start2,dicti,lister)

print ""
print ""
print "There There! That took some time. Phew! But Here I am Listing 3 songs that I think you should listen to :-)"
temp1=max(dicti, key=dicti.get)
temp11=dict2[temp1]
del(dicti[temp1])
print temp1+' by '+temp11
temp2=max(dicti, key=dicti.get)
del(dicti[temp2])
temp21=dict2[temp2]
print temp2+' by '+temp21
temp3=max(dicti, key=dicti.get)
temp31=dict2[temp3]
print temp3+' by '+temp31

print 'Hope it was worth it!'
