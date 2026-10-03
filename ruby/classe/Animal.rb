module Comunicar
  def comunicar(nome)
    puts "Olá, eu sou o #{nome}"
  end
end

class Animal
  attr_reader :nome, :especie
  
  def initialize(nome, especie)
    @nome = nome
    @especie = especie
  end
end

a1 = Animal.new("bob", "ovudo")

puts a1.nome
puts a1.especie