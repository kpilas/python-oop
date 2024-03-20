from notepad import Notebook
import sys


class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.option = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def show_menu(self):
        print("1 - pokaż notatki")
        print("2 - wyszukaj notatki")
        print("3 - stwórz notatkę")
        print("4 - modyfikuj notatkę")
        print("5 - zakończ")

    def run(self):
        while True:
            self.show_menu()
            op = input("Twój wybór: ")
            action = self.option.get(op)
            if action:
                action()
            else:
                print('Błędny wybór')

    def quit(self):
        print("Koniec programu")
        sys.exit(0)

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes

        for note in notes:
            print(note)

    def search_notes(self):
        phrase = input("Podaj czego szukasz: ")
        self.show_notes(self.notebook.search(phrase))

    def add_note(self):
        text = input("Podaj tekst notatki: ")
        tag = input('Podaj tag notatki: ')
        self.notebook.new_note(text, tag)


    def modify_note(self):
        id = int(input('Podaj id notatki do modyfikacji: '))
        for note in self.notebook.notes:
            if id == note.id:
                text = input("Podaj tekst notatki: ")
                tag = input('Podaj tag notatki: ')
                self.notebook.modify_tag(id, text)
                self.notebook.modify_text(id, tag)
                break
        else:
            print('Nie ma takiej notatki')


Menu().run()