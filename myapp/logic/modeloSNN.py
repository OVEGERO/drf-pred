from keras.models import load_model
import pickle
import os
from keras.utils import pad_sequences

class modeloSNN():

    def cargarRNN(self, nombreArchivo):
        ruta = '/app/resources'
        nombre_archivo = nombreArchivo + '.h5'
        ruta_archivo = os.path.join(ruta, nombre_archivo)
        modelo = load_model(ruta_archivo)
        print("Red Neuronal Cargada desde Archivo") 
        return modelo

    def cargarTokenizer(self, nombreArchivo):
        ruta = '/app/resources'
        nombre_archivo = nombreArchivo + '.pickle'
        ruta_archivo = os.path.join(ruta, nombre_archivo)
        with open(ruta_archivo, 'rb') as handle:
            tokenizer = pickle.load(handle)
            return tokenizer
        
    def predecirNuevasMuestras(self, Comentario):
        data = [Comentario]
        dic = {0: 'Mala', 1: 'Bueno', 2: 'Excelente'}
        self.tokenizer = self.cargarTokenizer(self,'tokenizer')
        self.model = self.cargarRNN(self,'modelo_base')
        X = self.tokenizer.texts_to_sequences(data)
        X = pad_sequences(X, maxlen=166)
        pred = self.model.predict(X)[0]
        resp = ''
        if pred.argmax(axis=0) == 0:
            resp = (f'La calificación del restaurante es: {dic[pred.argmax(axis=0)]}. Con una certeza del {round(pred[pred.argmax(axis=0)]*100, 4)}%')
        elif pred.argmax(axis=0) == 1:
            resp = (f'La calificación del restaurante es: {dic[pred.argmax(axis=0)]}. Con una certeza del {round(pred[pred.argmax(axis=0)]*100, 4)}%')
        else:
            resp = (f'La calificación del restaurante es: {dic[pred.argmax(axis=0)]}. Con una certeza del {round(pred[pred.argmax(axis=0)]*100, 4)}%')
        return resp 