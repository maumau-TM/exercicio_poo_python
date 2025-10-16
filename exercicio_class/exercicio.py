class ContaBancaria:
    def __init__ (self, titular, numero):
        self.titular = titular
        self.saldo = 0.0
        self.numero = numero

    def depositar(self, valor):
        if valor > 0:
            text = f'Valor depositado de R${valor}, feito com sucesso.'
            self.saldo =+ valor   
            print(text)
        else:
            print('O valor do depósito precisa ser maior que 0')
        
    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de R${valor} feito com sucesso')
            else: 
                print("saldo insuficiente para fazer o saque")
        else:
            print("O valor do saque precisa ser maior que 0.")

triplex_lula = ContaBancaria("Luis Inacio Lula", 40028922)
triplex_lula.depositar(100)
triplex_lula.sacar(10)
print(f"\nseu saldo é: {triplex_lula.saldo}\nSeu numero é: {triplex_lula.numero} \nSeu nome é: Seu nome")
            

