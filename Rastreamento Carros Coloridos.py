import numpy as np
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX 

cap = cv2.VideoCapture('imagens/carros.mp4')
ret, old = cap.read()
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Cria o objeto para gravar vídeo

out = cv2.VideoWriter('saida.mp4', fourcc, 25.0, (old.shape[1] , old.shape[0]))  # Determina o nome do arquivo de saída, sua taxa de FPS e sua resolução.
while True:
    
    ret,frame = cap.read()
    if not ret:
        exit()
    
    #BGR
    #Vermelho
    lower_r = np.array([0,0, 149], dtype=np.uint8)  
    upper_r = np.array([135, 106, 255], dtype=np.uint8)
    
    #Verde
    lower_g = np.array([0,110, 0], dtype=np.uint8)  
    upper_g = np.array([105, 193, 87], dtype=np.uint8)
    
    #Azul
    lower_b = np.array([105,0, 0], dtype=np.uint8)  
    upper_b = np.array([223, 83, 204], dtype=np.uint8)
    
    #Amarelo
    lower_y = np.array([0,142, 149], dtype=np.uint8)  
    upper_y = np.array([135, 255, 255], dtype=np.uint8)

    #Construindo as máscaras de cada cor
    mask_r = cv2.inRange(frame, lower_r, upper_r)
    
    mask_g = cv2.inRange(frame, lower_g, upper_g)
    
    mask_b = cv2.inRange(frame, lower_b, upper_b)
    
    mask_y = cv2.inRange(frame, lower_y, upper_y)
    
    #Encontrar contornos das máscaras
    contours_r, hierarchy_r = cv2.findContours(mask_r, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    contours_g, hierarchy_g = cv2.findContours(mask_g, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    contours_b, hierarchy_b = cv2.findContours(mask_b, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    contours_y, hierarchy_y = cv2.findContours(mask_y, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours_r)>0:
        for cnts in contours_r:
            (x,y,w,h) = cv2.boundingRect(cnts) # Cria retângulos com os limites dos contornos
            if w > 25 and h > 25:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4, cv2.LINE_AA) # imprime o retângulo no Frame

                cv2.putText(frame, 'VERMELHO', (x+5,y-5), font,.8, [0,0,255], 1, cv2.LINE_AA) # Imprime o texto das coordenadas
                
    if len(contours_g)>0:
        for cnts in contours_g:
            (x,y,w,h) = cv2.boundingRect(cnts) 
            if w > 25 and h > 25:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 128, 0), 4, cv2.LINE_AA) 

                cv2.putText(frame, 'VERDE', (x+5,y-5), font,.8, [0,128,0], 1, cv2.LINE_AA) 
    
    if len(contours_b)>0:
        for cnts in contours_b:
            (x,y,w,h) = cv2.boundingRect(cnts) 
            if w > 25 and h > 25:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 4, cv2.LINE_AA) 

                cv2.putText(frame, 'AZUL', (x+5,y-5), font,.8, [255, 0, 0], 1, cv2.LINE_AA) 
                
    if len(contours_y)>0:
        for cnts in contours_y:
            (x,y,w,h) = cv2.boundingRect(cnts) 
            if w > 25 and h > 25:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 4, cv2.LINE_AA) 

                cv2.putText(frame, 'AMARELO', (x+5,y-5), font,.8, [0,255,255], 1, cv2.LINE_AA) 
                
    cv2.imshow('frame', frame )
    out.write(frame) # Grava o frame atual no video
    c = cv2.waitKey(15)
    
    if c == ord('q'):
        out.release()
        break
        

out.release()    
cv2.destroyAllWindows()