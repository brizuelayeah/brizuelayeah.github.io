from flask import Flask, request, render_template, send_from_directory
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail with your email server details
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '820773@unizar.es'
app.config['MAIL_PASSWORD'] = 'esteEsMiTFGFinal.117'

mail = Mail(app)

@app.route('/')
def contact_form():
    return render_template('contact_form.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        subject = request.form['subject']
        sender_name = request.form['name']
        sender_email = request.form['email']
        message_body = request.form['message']

        # Create the email message
        msg = Message(subject, sender=f"{sender_name} <{app.config['MAIL_USERNAME']}>", recipients=['820773@unizar.es'])
        msg.body = f"Name: {sender_name}\nEmail: {sender_email}\n\n{message_body}"

        # Send the email
        try:
            mail.send(msg)
            return "Email sent successfully!"
        except Exception as e:
            return f"Failed to send email. Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
