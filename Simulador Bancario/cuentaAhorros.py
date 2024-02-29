class CuentaAhorros:
    #simulacion cuenta de ahorros
    '''----------------------------
    #Atributos
    ----------------------------'''
    saldo= ""
    interesesMensuales= ""
    '''----------------------------
    # Metodos
    ----------------------------'''
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
    def ConsultarSaldo (self):
        # Aqui va el codigo del medoto
        return self.saldo
    def Interesesmensuales (self):
        nSaldo= self.saldo * 0,0
        nSaldo= self.saldo + nSaldo
        self.saldo= nSaldo
        return "Su saldo este mes es de:" + self.saldo
    
    

