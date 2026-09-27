module Operacoes
  def subt(a1, a2)
    lista = []
    lista.append(a1, a2)
    lista.inject(:-)
  end

  def sum(a1, a2)
    lista = []
    lista.push(a1, a2)
    lista.inject(:+)
  end
end

class Calculadora
  include Operacoes
  def initialize(a1, a2)
    puts "qual operação você quer fazer? (+) / (-)"
    calc = gets.chomp

    case calc

    when "+"
      puts sum(a1, a2)

    when "-"
      puts subt(a1, a2)
    end
  end
end

puts "escreva um número: "
a1 = gets.chomp.to_i
puts "escreva mais um número: "
a2 = gets.chomp.to_i

c1 = Calculadora.new(a1, a2)