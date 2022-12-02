import json
from typing import Dict

from pydantic import BaseModel
from datetime import datetime

class CreateNoteResponse(BaseModel):
    id: str
    answer: str

class ReadNoteResponse(BaseModel):
    id: int
    text: str

class GetTimeInfoResponse(BaseModel):
    created_at: datetime
    updated_at: datetime

class UpdateNoteResponse(BaseModel):
    id: int

class DeleteNoteResponse(BaseModel):
    id: int

class UncorrectTokenResponse(BaseModel):
    answer: str

class Note():
    id = 0
    text = ''
    created_at = datetime.now()
    updated_at = created_at

    def __init__(self, id,  text, created_at, updated_at):
        self.id = id
        self.text = text
        self.created_at = created_at
        self.updated_at = updated_at

    def update(self, text, updated_at):
        self.text = text
        self.updatd_at = updated_at

    def toString(self):
        return str(self.id) + ", " + self.text + ', ' + str(self.created_at) + ', ' + str(self.updated_at)

class NoteStore():
    id = -1
    notes = {}
    def __init__(self):
        with open("notes.txt", "r") as f:
            buf = f.readline().split(', ')
            while buf != ['']:
                bufStr = buf[3][0:len(buf[3]) - 1]
                note = Note(buf[0], buf[1], buf[2], bufStr)
                self.notes[note.id] = note
                buf = f.readline().split(', ')
        print(self.notes)
        with open("id.txt", "r") as f:
            self.id = f.readline()
        print(self.id)

    def writeData(self):
        with open("notes.txt", "w") as f:
            for id in self.notes.keys():
                f.write(self.notes[id].toString() + "\n")
        with open("id.txt", "w") as f:
            f.write(str(self.id), f)

    # def writeData(self):
    #     keys = self.notes.keys()
    #     for key in keys:
    #         self.notes[key] = self.notes[key].toDict()
    #     with open("notes.json", "w") as f:
    #         json.dump(self.notes, f)
    #     with open("id.txt", "w") as f:
    #         f.write(id, f)

