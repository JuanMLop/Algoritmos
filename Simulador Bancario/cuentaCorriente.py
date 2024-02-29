class CuentaCorriente:
    #Aqui van datos de la simulacion
    '''----------------------------
    # Atributos
    ----------------------------'''
    saldo= ""
    '''----------------------------
    # Metodo
    ----------------------------'''
    
    def ConsultarSaldo (self):
        # Aqui va el codigo del medoto
        return self.saldo
    
    def ConsignarValor (self, monto):
        nSaldo= self.saldo + monto
        self.saldo= nSaldo
        # Aqui va el codigo del medoto
        return nSaldo

    def RetirarValor (self, monto):
        nSaldo=self.saldo - monto
        self.saldo= nSaldo
        # Aqui va el codigo del medoto
        return nSaldo
    
