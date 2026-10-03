require_relative 'aluno'
require_relative 'professor'
require_relative 'turma'

a1 = Aluno.new("João", 20, "123456789")
a1 = Aluno.new("Maria", 22, "987654321")
p1 = Professor.new("Carlos", 35, "Matemática")

t1 = Turma.new([a1, a2], p1)

puts t1.alunos