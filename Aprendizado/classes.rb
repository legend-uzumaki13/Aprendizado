class Pessoa
  attr_accessor :nome, :idade
end

a1 = Pessoa.new

a1.nome = "Nicolas"
a1.idade = 17


print a1.nome, ", ", a1.idade

