# -*- coding: utf-8 -*-

## Columnista v0.1 ##

## Next steps ##

## 1. agregar variables: persona responsable + problem types
## 2. agregar más variabilidad a las oraciones
## 3. scrape news websites para determinar "el problema del día"
## 4. generar permalinks para todas las columnas generadas

import random
from flask import Flask, render_template

class Issue:
	
	""" Issues and parameters to generate columns. """

	def __init__(self, name, entities, quality):
		self.name = name
		self.entities = entities
		self.quality = quality ## if issue bad, we want less of it, if good, we want more of it
		self.entity = None


	def select_entity(self):
		self.entity = self.entities[random.randint(0, len(self.entities)-1)]


class Entity:

	""" Entities responsible for issues. """

	def __init__(self, name, category):
		self.name = name
		self.category = category # private or public? or maybe political+civic too?
		self.responsible = None # name of the person responsible for the entity

## initialise Flask app

app = Flask(__name__)

## Parameters ## 

problem_list = [
	Issue("educación", ["Congreso", "Ministerio de Educación", 'modelo económico neoliberal', 'comunismo pro-soviético', 'velasquismo', 'caviarismo'], "good"),
	Issue("salud", ["Congreso", "Ministerio de Salud", 'modelo económico neoliberal', 'comunismo pro-soviético', 'velasquismo', 'caviarismo'], "good"),
	Issue("corrupción", ["Congreso", "Poder Judicial", 'fujimorismo', 'aprismo', 'caviarismo'], "bad"),
	Issue('seguridad ciudadana', ['Ministerio del Interior', 'Congreso', 'Poder Judicial', 'fujimorismo', 'aprismo', 'caviarismo'], 'good'),
	Issue('minería ilegal', ['Congreso', 'Ministerio del Ambiente', 'modelo económico neoliberal', 'fujimorismo', 'caviarismo'], 'bad'),
	Issue('concentración de medios', ['Grupo El Comercio', 'comunismo pro-soviético', 'fujimorismo', 'caviarismo'], 'bad')
	]

entity_list = [
	Entity("Presidente", "publico"),
	Entity("Congreso", "publico"),
	Entity("Ministerio de Educación", "publico"),
	Entity("Poder Judicial", "publico"),
	Entity("Ministerio de Salud", "publico"),
	Entity('Ministerio del Interior', 'publico'),
	Entity('Grupo El Comercio', 'privado'),
	Entity('Ministerio del Ambiente', 'publico'),
	Entity('modelo económico neoliberal', 'conceptual'),
	Entity('velasquismo', 'conceptual'),
	Entity('comunismo pro-soviético', 'conceptual'),
	Entity('caviarismo', 'conceptual'),
	Entity('fujimorismo', 'conceptual'),
	Entity('aprismo', 'conceptual')
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
	if problem.quality == 'bad':
		sentence1 = "El problema de la " + problem.name + " en el Perú está completamente fuera de control. "
	else:
		sentence1 = 'Una vez más recordamos que la ' + problem.name + ' sigue siendo uno de los problemas más importantes demorando el desarrollo del Perú. '
	if entity.category == 'conceptual':
		sentence2 = 'Resulta inexplicable que aún hoy los peruanos sigan a merced de experimentos agotados producto del ' + entity.name + '. '
	else:
		sentence2 = "Es hora de que el " + entity.name + " tome cartas en el asunto antes de que la situación empeore. "

	return sentence1.decode('utf-8') + sentence2.decode('utf-8')

def build_second_para(problem, entity):
	if entity.category == "publico":
		if problem.quality == 'good':
			sentence1 = "Es innegable que los problemas que enfrentamos hoy en día en torno a la " + problem.name + " encuentran su origen en el deficiente manejo que el " + entity.name + " ha hecho de la situación. "
			sentence2 = "La " + problem.name + " se beneficiaría enormemente de las ventajas universalmente reconocidas que puede traer la gestión privada. "
			sentence3 = "Es indudable, entonces, que para resolver el problema de la " + problem.name + " en el Perú, tenemos que empezar a discutir seriamente la privatización de la " + problem.name + ". "
		elif problem.quality == 'bad':
			sentence1 = 'El agravamiento de la ' + problem.name + ' en los últimos años refleja la incapacidad del sector público para ejercer una gestión eficiente de los recursos. '
			sentence2 = 'Si seguimos por el mismo camino, solo lograremos constatar la bancarrota total del ' + entity.name + ' y su capacidad para resolver el probelma. '
			sentence3 = 'Una solución definitiva al problema de la ' + problem.name + ' requiere de la participación de nuevos actores, especialmente del apoyo del sector privado.'
	elif entity.category == 'privado':
		sentence1 = "A pesar de los esfuerzos del " + entity.name + " por traer a la modernidad el ámbito de la " + problem.name + ", es inaceptable la manera como el Estado busca perpetuar su control sobre la libertad privada. "
		sentence2 = "Cualquier observador informado podrá reconocer como un exceso innecesario de regulación y controles estatales operan como candado a toda forma de progreso y mejora en el ámbito de la " + problem.name + ". "
		sentence3 = "Solo un esfuerzo sostenido para liberar al sector privado de estas ataduras podrá permitir que instituciones como el " + entity.name + " encuentren los incentivos necesarios para llevar a cabo transformaciones importantes."
	elif entity.category == 'conceptual':
		sentence1 = 'El Perú se encuentra hoy persistiendo bajo el injusto azote del ' + entity.name + ' y quienes aún se declaran sus seguidores. '
		sentence2 = 'Pero este tipo de entrampamientos ideológicos no hacen sino agravar los ya de por sí complicados problemas que enfrenta la ' + problem.name + ' peruana. '
		sentence3 = 'Los defensores del ' + entity.name + ' harían bien en preguntarse: ¿Queremos vivir en un país donde la ' + problem.name + ' permanezca en el mismo marasmo en el que se ha encontrado las últimas dos décadas?'

	return sentence1.decode('utf-8') + sentence2.decode('utf-8') + sentence3.decode('utf-8')

def build_third_para(problem, entity):
	if entity.category == "publico":
		sentence1 = "Una gestión privada para la " + problem.name + " garantizará eficiencia, transparencia, y el mejor uso de los recursos públicos. "
		if problem.quality == 'good':
			sentence2 = "Ya no tiene sentido que mantengamos instituciones ineficientes y pobladas de corrupción que demoran el progreso de la " + problem.name + " peruana. "
		elif problem.quality == 'bad':
			sentence2 = 'Es por culpa de actitudes trasnochadas que aún el día de hoy la' + problem.name + 'sigue demorando el gran proceso de modernización que atraviesa el Perú.'
		sentence3 = "La " + problem.name + " que el Perú necesita pasa por una modernización total de la manera como funciona el " + entity.name + "."
	elif entity.category == 'privado':
		sentence1 = 'Es cuestión simplemente de contemplar los resultados obtenidos en todos los países desarrollados tras la desregulación de la ' + problem.name + ' para entender la urgencia de estas acciones en el Perú. '
		sentence2 = 'El presente marco regulatorio parece estar diseñado para interrumpir y dificultar en todo lo posible el trabajo de el ' + entity.name + '. '
		sentence3 = 'Si queremos realmente comportarnos como una nación moderna, tenemos que esforzarnos porque el Estado no se vuelva un obstáculo para el progreso y el desarrollo que el sector privado busca generar en la ' + problem.name + '.'
	elif entity.category == 'conceptual':
		sentence1 = 'Si queremos realmente convertirnos en una nación moderna, es hora de dejar de lado las ideas trasnochadas del ' + entity.name + ' que no hacen sino atarnos al atraso y el subdesarrollo. '
		sentence2 = 'La prosperidad a la que todos aspiramos depende de nuestra capacidad para mejorar la ' + problem.name + ' para generar mayores oportunidades para todos los peruanos. '
		sentence3 = 'El ' + entity.name + ', en cambio, no busca sino excluir del futuro del país a todos aquellos que no comulguen con sus principios e ideales.'

	return sentence1.decode('utf-8') + sentence2.decode('utf-8') + sentence3.decode('utf-8')

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

	return render_template('base.html', columna=columna)

if __name__ == "__main__":
	app.debug = True
	app.run()

