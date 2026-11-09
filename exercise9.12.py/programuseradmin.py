from moduladmin import Admin

admin_baru = Admin("Siti", "Aisyah", "sitiais", "siti@email.com", "Bandung")

admin_baru.greetuser()
print()
admin_baru.privileges.show_privileges()
