from data import inserir_habito, inserir_registro

class Habito:
	def __init__(self, nome, frequencia, meta_diaria):
		self.nome = nome
		self.frequencia = frequencia
		self.meta_diaria = meta_diaria

	def salvar(self):
		inserir_habito(self.nome, self.frequencia, self.meta_diaria)

	def __str__(self):
		return self.nome

class Registro:
	def __init__(self, data, habito_id, status):
		self.data = data
		self.habito_id = habito_id
		self.status = status

	def salvar(self):
		inserir_registro(self.data, self.habito_id, self.status)

	def __str__(self):
		return f'{self.data} {self.habito_id} {self.status}'