from flask import Flask
from flask import request
from flask import session

from member_system.core import UnitOfWork

def configureAPIRoutes(app: Flask, unitOfWork: UnitOfWork):
    @app.route('/api/member', methods=['GET', 'PATCH'])
    def apiMember():
        if request.method == 'GET':
            return memberGet(unitOfWork)
        elif request.method == 'PATCH':
            return memberPatch(unitOfWork)

def memberGet(unitOfWork: UnitOfWork):
    username = request.args.get('username')
    isValid = username and session.get('name')
    if isValid:
        return memberGetIfValid(unitOfWork, username)
    return {'data': None}

def memberGetIfValid(unitOfWork: UnitOfWork, username: str):
    member = unitOfWork.memberRepository.getMemberByUsername(username)
    if member == None:
        return {'data': None}
    return { 
        'data': {
            'id': member.id,
            'name': member.name,
            'username': member.username
        }
    }

def memberPatch(unitOfWork: UnitOfWork):
    if request.content_type == 'application/json':
        id = session.get('id')
        newName = request.get_json()['name']
        if newName and id:
            return memberPatchIfValid(unitOfWork, id, newName)
    return {'error': True}

def memberPatchIfValid(unitOfWork: UnitOfWork, id: int, newName: str):
    success = unitOfWork.memberRepository.updateNameById(id, newName)
    if success:
        session['name'] = newName
        return {'ok': True}
    else:
        return {'error': True}