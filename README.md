# keylogger
Un keylogger (registrador de pulsaciones de teclas) es un tipo de software o hardware diseñado para registrar las teclas que un usuario presiona en un teclado

*Este codigo no fue realizado con malas intenciones ni con el deseo de perjudicar a nadie, este archivo fue creado con intenciones didacticas y de aprendizaje.*

Este codigo en particular de python, al activarse toma registro de todas las teclas que se pulsen y las va agregando a un documento .txt (0.txt, asi se llama el documento) el cual va recibiendo la informacion y cuando se registre cierta cantidad de caracteres (especificada en el codigo en la linea: 30, pueden modificar esto para que se envie con menos o mas caracteres cada mail) entonces se envia un mail con todo el contenido del archivo .txt para luego vaciarlo y que se pueda seguir llenando de los proximos registros. Se puede suspender el codigo al tocar la tecla definida previamente: "esc" de escape o con ctrl + C si estas desde una terminal

La variable 'smtp_password' NO es tu contraseña de mail (si estas usando Gmail, en caso contrario con tu contraseña de mail deberia bastar), es un codigo que debemos crear nosotros debido a las ultimas politicas de google (es decir que en teoria solo debemos preocuparnos por este apartado solo si tenemos Gmail).
Para ver este tema debemos ir a 'https://myaccount.google.com/security' y habiendo activado la 'Verificación en dos pasos' debemos buscar en la barra de busquedas: ´Contraseñas de aplicaciones´ ahi cuando le den click, crean una nueva contraseña de aplicacion y le ponen el nombre que quieran, copian ese codigo y le quitan los espacios.  Entonces vuelven al codigo kb.py y reemplazan smtp_password con el codigo que copiaron.
Aclaro que si estas usando Gmail y decidis usar tu contraseña en la variable 'smtp_password' el codigo no va a funcionar.
