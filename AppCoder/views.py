from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.models import Curso

def curso(self):
    curso = Curso(nombre='Desarrollo web', camada=167400)
    curso.save()
    documento = f"Curso: {curso.nombre} - Camada: {curso.camada}"
    return HTTPResponse(documento)
