# Mismatch test from
# https://bamos.github.io/2016/01/19/openface-0.2.0/

import cognitive_face as CF

KEY = '6df731c1d1c243ef88a420fe93f86c69'
CF.Key.set(KEY)

face_id_list = [
    '50935bff-73bb-4aab-a095-a735e7cd8ae5',  # Abdel Madi Shabned
    'f1838661-189c-43c0-b3f9-1863b6c793cc',  # Dean Barker
    '03601f8e-3d53-4f88-b157-b0d1b591267b'   # Giancarlo Fisichella
]

# Face - Verify

verify_results = []
verify_results.append(CF.face.verify(face_id_list[0], face_id_list[1]))
verify_results.append(CF.face.verify(face_id_list[0], face_id_list[2]))

print('*' * 80)
print('Openface versus Microsoft Cognitive Services face API')
print('*' * 80)
print(verify_results[0])
print(verify_results[1])
