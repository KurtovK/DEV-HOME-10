from tkinter import *
from tkinter import messagebox
import datetime
import sqlite3
class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.creation_date = ""
        self.character_count = 0


class NotesApp:
    def __init__(self):
        self.notes = []

        self.window = Tk()
        self.window.title("Заметки")

        self.title_label = Label(self.window, text="Заголовок:")
        self.title_label.grid(row=0, column=0)

        self.title_entry = Entry(self.window)
        self.title_entry.grid(row=0, column=1)

        self.content_label = Label(self.window, text="Содержимое:")
        self.content_label.grid(row=1, column=0)

        self.content_entry = Entry(self.window)
        self.content_entry.grid(row=1, column=1)

        self.add_button = Button(self.window, text="Добавить", command=self.add_note)
        self.add_button.grid(row=2, column=0)

        self.delete_button = Button(self.window, text="Удалить", command=self.delete_note)
        self.delete_button.grid(row=2, column=1)

        self.modify_button = Button(self.window, text="Изменить", command=self.modify_note)
        self.modify_button.grid(row=2, column=2)

        self.clear_button = Button(self.window, text="Очистить", command=self.clear_notes)
        self.clear_button.grid(row=2, column=3)

        self.view_button = Button(self.window, text="Просмотр", command=self.view_notes)
        self.view_button.grid(row=2, column=4)

        self.notes_text = Text(self.window, height=10, width=50)
        self.notes_text.grid(row=3, columnspan=5)

    def add_note(self):
        title = self.title_entry.get()
        content = self.content_entry.get()

        note = Note(title, content)
        note.creation_date = "Текущая дата"  # Здесь можно добавить код для получения текущей даты

        note.character_count = len(content)

        self.notes.append(note)

        messagebox.showinfo("Добавление заметки", "Заметка успешно добавлена!")

    def delete_note(self):
        if len(self.notes) >= 10:
            messagebox.showwarning("Удаление заметки", "Необходимо оставить хотя бы 10 заметок")
        else:
            title = self.title_entry.get()
            content = self.content_entry.get()

            for note in self.notes:
                if note.title == title and note.content == content:
                    self.notes.remove(note)
                    messagebox.showinfo("Удаление заметки", "Заметка успешно удалена!")
                    return

            messagebox.showwarning("Удаление заметки", "Заметка не найдена!")

    def modify_note(self):
        title = self.title_entry.get()
        content = self.content_entry.get()

        for note in self.notes:
            if note.title == title:
                note.content = content
                note.character_count = len(content)
                messagebox.showinfo("Изменение заметки", "Заметка успешно изменена!")
                return

        messagebox.showwarning("Изменение заметки", "Заметка не найдена!")

    def clear_notes(self):
        self.notes.clear()
        messagebox.showinfo("Очистка заметок", "Все заметки успешно удалены!")

    def view_notes(self):
        self.notes_text.delete(1.0, END)

        self.notes.sort(key=lambda note: note.creation_date)
        for note in self.notes[:10]:
            self.notes_text.insert(END, f"Заголовок: {note.title}\n")
            self.notes_text.insert(END, f"Содержимое: {note.content}\n")
            self.notes_text.insert(END, f"Дата создания: {note.creation_date}\n")
            self.notes_text.insert(END, f"Количество символов: {note.character_count}\n")
            self.notes_text.insert(END, "=" * 50 + "\n\n")

    def run(self):
        self.window.mainloop()

def create_note():
    note = input("Введите вашу заметку: ")
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note_with_date = f"{current_date}: {note}\n"
    return note_with_date
def save_to_file(notes):
    filename = input("Введите имя файла, в который хотите сохранить заметки: ")
    with open(filename, "a") as file:
        file.writelines(notes)
        print("Заметки успешно сохранены!")



def save_to_database(notes):
    connection = sqlite3.connect("notes.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            note TEXT
        )
    """)

    for note in notes:
        cursor.execute("INSERT INTO notes (note) VALUES (?)", (note,))

    connection.commit()
    connection.close()
    print("Заметки успешно сохранены в базе данных!")


def main():
    choice = input("Выберите действие (1 - создать заметку, 2 - сохранить заметки): ")

    if choice == "1":
        note = create_note()
        print("Заметка успешно создана!")
        print(note)
    elif choice == "2":
        notes = []
        count = int(input("Введите количество заметок: "))

        for _ in range(count):
            note = create_note()
            notes.append(note)

        save_option = input("Выберите опцию сохранения (1 - в файл, 2 - в базу данных): ")

        if save_option == "1":
            save_to_file(notes)
        elif save_option == "2":
            save_to_database(notes)

    else:
        print("Некорректный ввод. Попробуйте снова.")
app = NotesApp()
app.run()