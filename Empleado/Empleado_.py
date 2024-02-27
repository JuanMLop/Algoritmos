class Empleado:

    #Aqui va el codigo

    '''----------------------------
    #Atributos
    ----------------------------'''
    nombre= ""  
    apellido= ""

    '''----------------------------
    # 1= Masculino y 2= Femenino
    ----------------------------'''
    sexo= ""
    salario= ""

    '''----------------------------
    # Metodos
    ----------------------------'''
    def CambiarSalario(self, nuevoSalario):
        # Aqui va el codigo del medoto
        return 0
    def CambiarEmpleado(self, nNombre, nApellido, nSexo, nSalrio):
        # Aqui va el codigo del medoto
        return  None
    def ConsultarSalario(self):
        # Aqui va el codigo del medoto
        return self.salario
    def ConsultarNombre(self):
    # Aqui va el codigo del medoto
        return self.nombre
    def ConsultarApellido(self):
    # Aqui va el codigo del medoto
        return self.apellido
    def ConsultarNombreCompleto(self):
        # Aqui va el codigo del medoto
        return self.nombre +" "+ self.apellido
    def AumentoSalario(self):
        nSalario= self.salario * 0.05
        nSalario= nSalario + self.salario
        self.salario= nSalario
        return "El nuevo salario es de: " + self.salario
    
