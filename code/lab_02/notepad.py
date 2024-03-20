import datetime


class Note:
    counter = 0

    def __init__(self, text, tag):
        self.text = text
        self.tag = tag
        self.date = datetime.date.today()
        self.id = Note.counter  # type(self).id
        Note.counter += 1

    def match(self, phrase):
        return phrase in self.text or phrase in self.tag

    def __str__(self):
        return f'id: {self.id}\ndata: {self.date}\ntext: {self.text}\ntag: {self.tag}'


class Notebook:

    def __init__(self):
        self.notes = list()

    def new_note(self, text, tag):
        self.notes.append(Note(text, tag))

    def modify_text(self, id, new_text):
        for note in self.notes:
            if note.id == id:
                note.text = new_text

    def modify_tag(self, id, new_tag):
        for note in self.notes:
            if note.id == id:
                note.tag = new_tag

    def search(self, phrase):
        return [note for note in self.notes if note.match(phrase)]
