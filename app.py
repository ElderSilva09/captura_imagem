import cv2

def capturar_e_salvar():

    webcam = cv2.VideoCapture(0)

    if not webcam.isOpened():
        print("Erro❗: Não foi possível acessar a webcam.")
        return # early return

    # Configuração da fonte do texto
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    escala = 0.6
    cor_texto = (255, 0, 0)
    espessura = 1

    print("[ESPAÇO] Capturar e salvar uma foto \n [ESC] Sair")

    while True: # do-while
        status, frame = webcam.read() #desenpacotamento / umpack

        if not status:
            print("Falha ao receber o frame da webcam")
            break

        frame_limpo = frame.copy()

        cv2.rectangle(frame, (10, 10), (320, 75), (0, 0, 0), -1)
        cv2.putText(frame, "[ESPAÇO] Salvar foto", (20, 35), fonte, escala, cor_texto, espessura)
        cv2.putText(frame, "[ESC] Sair", (20,60), fonte, escala, cor_texto, espessura) 

        cv2.imshow("Captura da Webcam local", frame)

        tecla = cv2.waitKey(1) & 0xFF

        if tecla == 32:
            cv2.imwrite("foto.jpg", frame_limpo)
            print("Foto salva: foto.jpg")

            foto_cinza = cv2.cvtColor(frame_limpo, cv2.COLOR_BGR2GRAY)
            cv2.imwrite("foto_cinza.jpg", foto_cinza)

            foto_invertida = cv2.cvtColor(frame_limpo, cv2.COLOR_RGB2BGR)
            cv2.imwrite("foto_invertida.jpg", foto_invertida)

            foto_alienigena = cv2.cvtColor(frame_limpo, cv2.COLOR_BGR2HLS_FULL)
            cv2.imwrite("foto_alienigena.jpg", foto_alienigena)

            foto_nordeste = cv2.cvtColor(frame_limpo, cv2.COLOR_BGR2LUV)
            cv2.imwrite("foto_nordeste.jpg", foto_nordeste)

            foto_mexico = cv2.cvtColor(frame_limpo, cv2.COLOR_BGR2LAB)
            cv2.imwrite("foto_mexico.jpg", foto_mexico)

            foto_clone = cv2.cvtColor(frame_limpo, cv2.COLOR_BGR2YUV_I420)
            cv2.imwrite("foto_clone.jpg", foto_clone)

            foto_red = cv2.cvtColor(frame_limpo, cv2.COLOR_BGR2HSV)
            cv2.imwrite("foto_red.jpg", foto_red)

            foto_cinza_invertido = cv2.cvtColor(frame_limpo, cv2.COLOR_BGR2XYZ)
            cv2.imwrite("foto_cinza_invertido.jpg", foto_cinza_invertido)

            

            
    


        elif tecla == 27:
            print("Encerramento câmera...")
            break
    webcam.realese()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capturar_e_salvar()