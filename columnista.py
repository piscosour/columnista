# -*- coding: utf-8 -*-

# 1. escoger un tema de coyuntura
# 2. identificar entidad responsable
# 3. si entidad = pública
# 	--> privatización
# 4. si entidad = privada
# 	--> desregulación
# 5. generar texto
# 	primer párrafo: problem statement + identificar al responsable
# 	segundo párrafo: "problema de fondo"
# 	tercer párrafo: "solución"


# lista de problemas
# educación
# corrupción
# salud
# medio ambiente
# infraestructura

# entes responsables
# Presidente
# Congreso
# Poder Judicial
# Ministerio de Educación
# Ministerio de Salud
# Ministerio del Medio Ambiente
# Municipalidad de Lima

import random
from flask import Flask, render_template

class Problem:
	
	""" Problems and parameters to generate columns. """

	def __init__(self, name, entities):
		self.name = name
		self.entities = entities
		self.entity = None

	def select_entity(self):
		self.entity = self.entities[random.randint(0, len(self.entities)-1)]


class Entity:

	""" Entities responsible for problems. """

	def __init__(self, name, category):
		self.name = name
		self.category = category

app = Flask(__name__)

## Parameters ## 

problem_list = [
	Problem("educación", ["Presidente", "Congreso", "Ministerio de Educación"]),
	Problem("salud", ["Presidente", "Congreso", "Ministerio de Salud"]),
	Problem("corrupción", ["Congreso", "Poder Judicial"])
	]

entity_list = [
	Entity("Presidente", "publico"),
	Entity("Congreso", "publico"),
	Entity("Ministerio de Educación", "publico"),
	Entity("Poder Judicial", "publico"),
	Entity("Ministerio de Salud", "publico")
	]

## Column generation ## 

def problem_picker():
	active_problem = problem_list[random.randint(0, len(problem_list)-1)]
	active_problem.select_entity() 
	for entity in entity_list:
		if entity.name == active_problem.entity:
			active_entity = entity

	return (active_problem, active_entity)

def build_first_para(problem, entity):
	sentence1 = "El problema de la " + problem.name + " en el Perú está completamente fuera de control. "
	sentence2 = "Es hora de que el " + entity.name + " tome cartas en el asunto antes de que la situación empeore. "

	return sentence1 + sentence2

def build_second_para(problem, entity):
	if entity.category == "publico":
		sentence1 = "Es innegable que los problemas que enfrenamos hoy en día en torno a la " + problem.name + " encuentran su origen en el deficiente manejo que el " + entity.name + " ha hecho de la situación. "
		sentence2 = "La " + problem.name + " se beneficiaría enormemente de las ventajas universalmente reconocidas que puede traer la gestión privada. "
		sentence3 = "Es indudable, entonces, que para resolver el problema de la " + problem.name + " en el Perú, tenemos que empezar a discutir seriamente la privatización del " + entity.name + ". "

	return sentence1 + sentence2 + sentence3

def build_third_para(problem, entity):
	if entity.category == "publico":
		sentence1 = "Una gestión privada para el " + entity.name + " garantizará eficiencia, transparencia, y el mejor uso de los recursos públicos. "
		sentence2 = "Ya no tiene sentido que mantengamos instituciones ineficientes y pobladas de corrupción que demoran el progreso de la " + problem.name + " peruana. "
		sentence3 = "La " + problem.name + " que el Perú necesita pasa por una modernización total de la manera como funciona el " + entity.name + "."

	return sentence1 + sentence2 + sentence3

def gen_column():
	parameters = problem_picker()
	problem = parameters[0]
	entity = parameters[1]

	first = build_first_para(problem, entity)
	second = build_second_para(problem, entity)
	third = build_third_para(problem, entity)

	columna = [first, second, third]

	return columna

## Web front-end ## 

@app.route('/')
def render_column():
	columna = gen_column()

	return "<p>" + columna[0] + "</p><p>" + columna[1] + "</p><p>" + columna[2] + "</p>"

if __name__ == "__main__":
	app.debug = True
	app.run()

