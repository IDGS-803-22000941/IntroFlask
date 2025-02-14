from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/cinepolis', methods=['GET', 'POST'])
def cinepolis():
    total_a_pagar = 0
    nombre_comprador = ""
    
    if request.method == 'POST':
        nombre = request.form.get('user_name')
        cantidad_compradores = int(request.form.get('user_cantidad', 0))
        cantidad_boletas = int(request.form.get('user_boletas', 0))
        tiene_tarjeta = request.form.get('indicacion_si') == 'si'
        
        precio_boleta = 12.000
        total = cantidad_boletas * precio_boleta
        
        if 3 <= cantidad_boletas <= 5:
            total *= 0.90  
        elif cantidad_boletas >= 6:
            total *= 0.85  
        
        if tiene_tarjeta:
            total *= 0.90
        
        total_a_pagar = round(total, 2)
        nombre_comprador = nombre
    
    return render_template('pantallacine.html', total_a_pagar=total_a_pagar, nombre_comprador=nombre_comprador)
if __name__ == '__main__':
    app.run(debug=True)
