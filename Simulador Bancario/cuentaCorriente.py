class CuentaCorriente:
    #Aqui van datos de la simulacion
    '''----------------------------
    # Atributos
    ----------------------------'''
    saldo= ""
    '''----------------------------
    # Metodo
    ----------------------------'''
    saldo= 0
    def ConsultarSaldo (self):
        # Aqui va el codigo del medoto
        return self.saldo
    
    def ConsignarValor (self,saldo):
        nSaldo= self.saldo + ""
        self.saldo= nSaldo
        # Aqui va el codigo del medoto
        return "Ingrese nuevo valor" + ""

    def RetirarValor (self,saldo):
        nSaldo= self.saldo - ""
        self.saldo= nSaldo
        # Aqui va el codigo del medoto
        return "Retire" + ""
    