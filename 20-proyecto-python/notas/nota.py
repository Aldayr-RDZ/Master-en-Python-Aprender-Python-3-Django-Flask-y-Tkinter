import usuarios.conexion as conexion 

connect = conexion.conectar
conexion_basededatos = connect[0]
cursor = connect[1]

class Nota:

    def __init__(self, usuario_id, titulo="", descripcion=""):
        self.usuario_id= usuario_id
        self.titulo= titulo
        self.descripcion= descripcion

    def guardar(self):
        sql ='INSERT INTO notas (usuario_id, titulo, descripcion, fecha) VALUES(%s, %s, %s, NOW())'
        nota = (self.usuario_id, self.titulo, self.descripcion)
        cursor.execute(sql, nota)
        conexion_basededatos.commit()
        return[ cursor.rowcount, self]
        
    
    def listar(self):
        sql = f'SELECT * FROM notas WHERE usuario_id = {self.usuario_id}'
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
        
    def eliminar(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%' "
        cursor.execute(sql)
        conexion_basededatos.commit()
        return [cursor.rowcount, self]