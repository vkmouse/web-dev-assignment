import json
from flask import Flask, request, session
from member_system.repository import UnitOfWork

def configureAPIRoutes(app: Flask, unitOfWork: UnitOfWork):
    @app.route('/api/member', methods=['GET'])
    def memberapi():
        if request.method == 'GET':
            data = None
            username = request.args.get('username')
            if username != None and session.get('name'):
                member = unitOfWork.memberRepository.getMemberByUsername(username)
                if member != None:
                    data = {
                        'id': member.id,
                        'name': member.name,
                        'username': member.username
                    }
            return json.dumps({'data': data})