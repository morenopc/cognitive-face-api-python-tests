import cognitive_face as CF

# Replace with a valid Subscription Key here.
KEY = '6df731c1d1c243ef88a420fe93f86c69'
CF.Key.set(KEY)

img_url = ('http://www.blastr.com/sites/blastr/files/styles/width_1280/'
           'public/images/frodo-baggins-LOTR.jpg')
result = CF.face.detect(img_url)
print result
