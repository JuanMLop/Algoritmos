from cuentaCorriente import CuentaCorriente
from cuentaAhorros import CuentaAhorros
from CDT import CDT

class SimuladorBancario:
    '''----------------------------
    #Atributos
    ----------------------------'''
    cedula=""
    nombre=""
    mesActual= ""

    """----------------------------
    # Asociaciones
    ----------------------------"""
    saldoCorriente= CuentaCorriente()
    saldoAhorros= CuentaAhorros()
    cdt= CDT()
    '''----------------------------
    # Metodos
    ----------------------------'''
    
    def ConsignarCorriente(self, saldo):
    # Aqui va el codigo del medoto
        return self.saldoCorriente.ConsignarValor(saldo)
    
    def CalcularSaldo(self):
    # Aqui va el codigo del medoto
        return "Su saldo total es:"(self.saldoCorriente.saldo + self.saldoAhorros.saldo)
        
    def PasarSaldo(self):
        self.saldoAhorros= self.saldoAhorros + self.saldoCorriente
        return self.saldoAhorros

    def ConsultarSaldoCuentaCorriente(self):
    # Aqui va el codigo del medoto
        return self.saldoCorriente.ConsultarSaldo()
    
    def RetirarTodo (self):
    # Aqui va el codigo del medoto
        return ":"(self.saldoCorriente.saldo - self.saldoAhorros.saldo - self.cdt.saldo)
    
    def DuplicarTodo (self, saldo):
        return ":"(self.saldoCorriente.saldo + self.saldoAhorros.saldo + self.cdt.saldo) *2

        

    

    
