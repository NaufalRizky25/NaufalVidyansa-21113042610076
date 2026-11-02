def build_profile(first, last, **user_info):

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


my_profile = build_profile(
    'budi', 'santoso',
    location='yogyakarta',
    field='computer science',
    hobby='fotografi'
)

print("--- Hasil Profil Pengguna (8-13) ---")
print(my_profile)
