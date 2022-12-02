import datetime

import fastapi

from model import Note, CreateNoteResponse, ReadNoteResponse, GetTimeInfoResponse, NoteStore,\
    UpdateNoteResponse, DeleteNoteResponse, UncorrectTokenResponse


api_router = fastapi.APIRouter()

tokens = {}
with open("tokens.txt", "r") as f:
    buf = f.readline().split('. ')
    while buf != ['']:
        bufStr = buf[1][0:len(buf[1]) - 1]
        tokens[bufStr] = buf[0]
        buf = f.readline().split('. ')
notes = {}
id = -1

@api_router.post("/create_note", response_model=CreateNoteResponse)
def create_note(text: str, token: str):
    global id
    global notes
    keys = tokens.keys()
    if not token in keys:
        print("uncorrect")
        return CreateNoteResponse(
            id='',
            answer="Uncorrect token"
        )
    fileNameNote = 'notes' + tokens[token] + '.txt'
    fileNameId = 'id' + tokens[token] + '.txt'
    with open(fileNameNote, "r") as f:
        buf = f.readline().split(', ')
        while buf != ['']:
            bufStr = buf[3][0:len(buf[3]) - 1]
            note = Note(buf[0], buf[1], buf[2], bufStr)
            notes[note.id] = note
            buf = f.readline().split(', ')
    with open(fileNameId, "r") as f:
        id = int(f.readline())
    id += 1
    with open(fileNameId, "w") as f:
        f.write(str(id))
    note = Note(id, text, datetime.datetime.now(), datetime.datetime.now())
    notes[id] = note
    with open(fileNameNote, "w") as f:
        for id in notes.keys():
            f.write(notes[id].toString() + "\n")
    return CreateNoteResponse(
        id=str(id),
        answer=''
    )

@api_router.get("/read_note", response_model=ReadNoteResponse)
def read_note(id: int, token: str):
    global notes
    fileNameNote = 'notes' + tokens[token] + '.txt'
    with open(fileNameNote, "r") as f:
        buf = f.readline().split(', ')
        while buf != ['']:
            bufStr = buf[3][0:len(buf[3]) - 1]
            note = Note(buf[0], buf[1], buf[2], bufStr)
            notes[note.id] = note
            buf = f.readline().split(', ')
    note = notes[str(id)]
    return ReadNoteResponse(
        id=id,
        text=note.text
    )

@api_router.get("/get_time_info", response_model=GetTimeInfoResponse)
def get_time_info(id: int, token: str):
    global notes
    fileNameNote = 'notes' + tokens[token] + '.txt'
    with open(fileNameNote, "r") as f:
        buf = f.readline().split(', ')
        while buf != ['']:
            bufStr = buf[3][0:len(buf[3]) - 1]
            note = Note(buf[0], buf[1], buf[2], bufStr)
            notes[note.id] = note
            buf = f.readline().split(', ')
    note = notes[id]
    return GetTimeInfoResponse(
        created_at=note.created_at,
        updated_at=note.updated_at
    )

@api_router.put("/update_note", response_model=UpdateNoteResponse)
def update_note(id: int, text: str, token: str):
    global notes
    fileNameNote = 'notes' + tokens[token] + '.txt'
    with open(fileNameNote, "r") as f:
        buf = f.readline().split(', ')
        while buf != ['']:
            bufStr = buf[3][0:len(buf[3]) - 1]
            note = Note(buf[0], buf[1], buf[2], bufStr)
            notes[note.id] = note
            buf = f.readline().split(', ')
    note = notes[str(id)]
    note.text = text
    note.updated_at = datetime.datetime.now()
    with open(fileNameNote, "w") as f:
        for id in notes.keys():
            f.write(notes[id].toString() + "\n")
    return UpdateNoteResponse(
        id=id,
    )

@api_router.delete("/delete_note", response_model=DeleteNoteResponse)
def delete_note(id: int, token: str):
    global notes
    fileNameNote = 'notes' + tokens[token] + '.txt'
    with open(fileNameNote, "r") as f:
        buf = f.readline().split(', ')
        while buf != ['']:
            bufStr = buf[3][0:len(buf[3]) - 1]
            note = Note(buf[0], buf[1], buf[2], bufStr)
            notes[note.id] = note
            buf = f.readline().split(', ')
    notes.pop(str(id))
    with open(fileNameNote, "w") as f:
        for id in notes.keys():
            f.write(notes[id].toString() + "\n")
    return DeleteNoteResponse(
        id=id,
    )

@api_router.get("/id_list", response_model=dict[int, int])
def show_id_list(token: str):
    global notes
    fileNameNote = 'notes' + tokens[token] + '.txt'
    with open(fileNameNote, "r") as f:
        buf = f.readline().split(', ')
        while buf != ['']:
            bufStr = buf[3][0:len(buf[3]) - 1]
            note = Note(buf[0], buf[1], buf[2], bufStr)
            notes[note.id] = note
            buf = f.readline().split(', ')
    response = {}
    keys = notes.keys()
    k = 0
    for key in keys:
        response[k] = key
        k += 1
    return response

