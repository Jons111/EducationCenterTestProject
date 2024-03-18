from fastapi import HTTPException


def the_one(id, model, db):
    the_one = db.query(model).filter(model.id == id).first()
    if not the_one:
        raise HTTPException(status_code=400, detail=f"Bazada bunday {model} yo'q!")
    return the_one


def the_one_username(username, model, db):
    the_one = db.query(model).filter(model.username == username, ).first()
    if the_one:
        raise HTTPException(status_code=400, detail=f"Bazada bunday username({username}) mavjud!")
    return the_one


def the_one_model_name(name, model, db):
    the_one = db.query(model).filter(model.name == name).first()
    if the_one:
        raise HTTPException(status_code=400, detail=f"Bazada bunday name({name}) mavjud!")
    return the_one


def the_one_model_number(number, model, db):
    the_one = db.query(model).filter(model.number == number, ).first()
    if the_one:
        raise HTTPException(status_code=400, detail=f"Bazada bunday number({number}) mavjud!")
    return the_one
