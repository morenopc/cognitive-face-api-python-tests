import cognitive_face as CF

KEY = '6df731c1d1c243ef88a420fe93f86c69'
CF.Key.set(KEY)

upload_images = True

# http://www.blastr.com/sites/blastr/files/styles/width_1280/public/images/frodo-baggins-LOTR.jpg
# http://1.bp.blogspot.com/_0f7Muu8izqA/S12b9KKNwtI/AAAAAAAAB0k/ohvpsCAftF8/s320/DYLANFrodo-Cage.jpg
# http://www.informationen-bilder.de/der-herr-der-ringe/frodo-ring.jpg
# https://i.imgur.com/2PjwjSk.jpg
# http://cdn.designrshub.com/wp-content/uploads/2013/04/frodo-baggins-artworks-19.jpg
# https://i.ytimg.com/vi/lhunBWw57Rg/maxresdefault.jpg
# http://a4.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE1ODA0OTcxODgwNTgwNjIx.jpg
# https://s-media-cache-ak0.pinimg.com/236x/09/b1/b7/09b1b7ea30f496fc9a31ccde57d67ed2.jpg
# http://www.thescribesdesk.com/wp-content/uploads/2011/06/elijah-wood-hobbit-frodo-baggins-ring.jpg
# https://pbs.twimg.com/profile_images/413503396272824320/M0Ol0Usb.jpeg


labels_list = [
    'default', 'Cage face', 'Ring rage face', 'Uranium', 'Draw', 'Megan Fox',
    'Glasses', 'Young', 'Getting the ring', 'Mummified'
]

face_id_list = [
    '80d5be8e-9b3b-4ca5-ac4f-f5463cdd4706',  # default
    '5f8b72f0-13c0-40c9-bd23-baa4f27f10a2',  # Cage face
    '89a11710-7122-4706-812e-1005ae5ec559',  # Ring rage face
    '3ed9a455-83a3-4e30-99d0-06c4bec7bee1',  # Uranium
    '07d048c1-43b1-47e4-b128-ef46d5acf469',  # Draw
    '8d103137-119b-4a73-8ac2-9ee74eac5e9e',  # Megan Fox
    'cd921a9f-4f75-489f-9b87-a0ef611e9306',  # Glasses
    'cacfc5c6-bcfb-4e4f-8c03-a888507e0250',  # Young
    '11eac0a5-4845-476e-8c88-a30e5bb4243c',  # Getting the ring
    '81b3544f-7053-474f-903a-7022a2360526',  # Mummified
]

# Face - Verify

verify_results = []
for face_id in face_id_list:
    verify_results.append(CF.face.verify(face_id_list[0], face_id))

print('*' * 80)
print('Frodo Baggins Face Verification')
print('*' * 80)

for result, label in zip(verify_results, labels_list):
    print('%s: %s' % (label, result))


# default: {u'isIdentical': True, u'confidence': 1.0}
# Cage face: {u'isIdentical': True, u'confidence': 0.52642}
# Ring rage face: {u'isIdentical': False, u'confidence': 0.38489}
# Uranium: {u'isIdentical': True, u'confidence': 0.78551}
# Draw: {u'isIdentical': True, u'confidence': 0.66936}
# Megan Fox: {u'isIdentical': False, u'confidence': 0.0}
# Glasses: {u'isIdentical': True, u'confidence': 0.57066}
# Young: {u'isIdentical': False, u'confidence': 0.32143}
# Getting the ring: {u'isIdentical': True, u'confidence': 0.60453}
# Mummified: {u'isIdentical': True, u'confidence': 0.54449}
