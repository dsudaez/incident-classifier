from flask import Flask, redirect, url_for, request

 
app = Flask(__name__)

@app.route('/success/<incident>')
def success(incident):
    return 'Incidencia: %s' % incident
 
 
@app.route('/incident', methods=['POST', 'GET'])
def incident():
    if request.method == 'POST':
        print(request.form)
        user = request.form['nm']
        return redirect(url_for('success', incident=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', incident=user))
 
 
if __name__ == '__main__':
    app.run(debug=True)