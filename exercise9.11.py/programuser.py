from modeluser import Admin

admin_utama = Admin("Budi", "Santoso", "budis", "budi@email.com", "Jakarta")

admin_utama.greetuser()
print()
admin_utama.privileges.show_privileges()
