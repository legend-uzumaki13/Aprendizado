class Turma
  attr_reader :alunos, :professor
  def initialize(alunos, professor)
    @alunos = Array.new
    @professor = professor
end