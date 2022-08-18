from GeekTechebannyi.month2.lesson4.hw4.file_executor.create import create_file
from GeekTechebannyi.month2.lesson4.hw4.file_executor.delete import delete_file
from GeekTechebannyi.month2.lesson4.hw4.file_executor.write import write_to_file

print(create_file("aruuke", 'txt'))
write_to_file("aruuke.txt", "Aruuke КРАШ")
print(delete_file("aruuke.txt"))