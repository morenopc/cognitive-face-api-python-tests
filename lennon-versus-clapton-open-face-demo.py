import cognitive_face as CF

KEY = '6df731c1d1c243ef88a420fe93f86c69'
CF.Key.set(KEY)

upload_images = True

image_ulrs = [
    'https://raw.githubusercontent.com/cmusatyalab/openface/master/images/examples/lennon-1.jpg',
    'https://raw.githubusercontent.com/cmusatyalab/openface/master/images/examples/lennon-2.jpg',
    'https://raw.githubusercontent.com/cmusatyalab/openface/master/images/examples/clapton-1.jpg',
    'https://raw.githubusercontent.com/cmusatyalab/openface/master/images/examples/clapton-2.jpg'
]

face_id_list = [
    '358e3fa6-0496-4d28-843c-8f33c51e90ff',
    '5580fec1-637b-454b-9b9e-20cb9f4a8f10',
    '67cc3954-3844-4c90-939d-b79d796ffdbc',
    '82eefe09-d051-4812-b653-a623d03fcbde'
]


def face_detect(image_ulrs):
    results = []
    for img_url in image_ulrs:
        results.append(CF.face.detect(img_url))
    return results


# Face - Verify

verify_results = []
verify_results.append(CF.face.verify(face_id_list[0], face_id_list[1]))
verify_results.append(CF.face.verify(face_id_list[0], face_id_list[2]))
verify_results.append(CF.face.verify(face_id_list[0], face_id_list[3]))
verify_results.append(CF.face.verify(face_id_list[1], face_id_list[2]))
verify_results.append(CF.face.verify(face_id_list[1], face_id_list[3]))
verify_results.append(CF.face.verify(face_id_list[2], face_id_list[3]))

print('*' * 80)
print('Openface versus Microsoft Cognitive Services face API')
print('*' * 80)
print('Lennon 1 vesus Lennon 2 result 0.763')
print(verify_results[0])
print('[openface]  %.2f%%' % ((1 - (0.763 / 4)) * 100))
print('[Microsoft] %.2f%%' % (verify_results[0].get('confidence') * 100))
print('Lennon 1 vesus Clapton 1 result 1.132')
print(verify_results[1])
print('[openface] %.2f%%' % ((1 - (1.132 / 4)) * 100))
print('[Microsoft] %.2f%%' % (verify_results[1].get('confidence') * 100))
print('Lennon 1 vesus Clapton 2 result 1.145')
print(verify_results[2])
print('[openface] %.2f%%' % ((1 - (1.145 / 4)) * 100))
print('[Microsoft] %.2f%%' % (verify_results[2].get('confidence') * 100))
print('Lennon 2 vesus Clapton 1 result 1.447')
print(verify_results[3])
print('[openface] %.2f%%' % ((1 - (1.447 / 4)) * 100))
print('[Microsoft] %.2f%%' % (verify_results[3].get('confidence') * 100))
print('Lennon 2 vesus Clapton 2 result 1.521')
print(verify_results[4])
print('[openface] %.2f%%' % ((1 - (1.521 / 4)) * 100))
print('[Microsoft] %.2f%%' % (verify_results[4].get('confidence') * 100))
print('Clapton 1 vesus Clapton 2 result 0.318')
print(verify_results[5])
print('[openface] %.2f%%' % ((1 - (0.318 / 4)) * 100))
print('[Microsoft] %.2f%%' % (verify_results[5].get('confidence') * 100))
