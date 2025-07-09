#
import json

aluno = {
    "nome": "Carlos",
    "idade": 17,
    "aprovado": True
}

aluno_json = json.dumps(aluno)
print(aluno_json)
